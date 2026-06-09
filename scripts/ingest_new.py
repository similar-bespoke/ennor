#!/usr/bin/env python3
"""
Ingest new PDFs that haven't been converted yet.

Compares PDFs in the repo against existing markdown files in the
knowledge base and only converts new/missing ones. Also copies
new PDFs into source_pdfs/ and regenerates INDEX.md.

Usage:
    python3 scripts/ingest_new.py                    # convert any new PDFs
    python3 scripts/ingest_new.py --force 1.5        # re-convert specific doc(s)
    python3 scripts/ingest_new.py --dry-run           # show what would be converted
"""

import argparse
import os
import re
import shutil
import sys
from pathlib import Path

# Add scripts dir to path so we can import the converter
sys.path.insert(0, str(Path(__file__).parent))

from convert_to_markdown import (
    ENNOR_DIR,
    OUTPUT_DIR,
    CATEGORIES,
    parse_base_content,
    match_pdf_to_metadata,
    extract_pdf,
    generate_markdown,
    slugify,
    find_all_pdfs,
)
from update_index import scan_knowledge_base, generate_index


def get_existing_sources() -> set[str]:
    """Get set of source_pdf values from existing markdown files."""
    sources = set()
    for root, dirs, files in os.walk(OUTPUT_DIR):
        rel_root = Path(root).relative_to(OUTPUT_DIR)
        if str(rel_root).startswith("source_pdfs"):
            continue
        for f in files:
            if not f.endswith(".md") or f == "INDEX.md":
                continue
            filepath = Path(root) / f
            with open(filepath, "r", encoding="utf-8") as fh:
                in_fm = False
                for line in fh:
                    line = line.strip()
                    if line == "---":
                        if in_fm:
                            break
                        in_fm = True
                        continue
                    if in_fm and line.startswith("source_pdf:"):
                        src = line.split(":", 1)[1].strip().strip('"')
                        sources.add(src)
                        break
    return sources


def main():
    parser = argparse.ArgumentParser(description="Ingest new PDFs into Ennor knowledge base")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be converted without doing it")
    parser.add_argument("--force", nargs="*", help="Force re-conversion of specific doc IDs (e.g., 1.5 2.1.1)")
    args = parser.parse_args()

    # Parse metadata
    base_content = ENNOR_DIR / "base_content.md"
    metadata = parse_base_content(base_content) if base_content.exists() else {}

    # Find all PDFs and existing conversions
    all_pdfs = find_all_pdfs(ENNOR_DIR)
    existing_sources = get_existing_sources()

    # Determine what needs conversion
    to_convert = []
    for pdf_path in all_pdfs:
        rel_path = str(pdf_path.relative_to(ENNOR_DIR))

        if args.force is not None:
            # Force mode: convert if doc_id matches any in --force list
            m = re.match(r"^(\d+(?:\.\d+)*)\s+", pdf_path.name)
            doc_id = m.group(1) if m else ""
            if doc_id in args.force or rel_path in args.force:
                to_convert.append(pdf_path)
        else:
            # Normal mode: convert if not already in knowledge base
            if rel_path not in existing_sources:
                to_convert.append(pdf_path)

    if not to_convert:
        print("Nothing new to convert. Knowledge base is up to date.")
        return

    print(f"Found {len(to_convert)} PDF(s) to convert:\n")
    for p in to_convert:
        print(f"  {p.relative_to(ENNOR_DIR)}")

    if args.dry_run:
        print("\n(dry run — no files written)")
        return

    print()

    # Convert each
    source_pdfs_dir = OUTPUT_DIR / "source_pdfs"
    source_pdfs_dir.mkdir(exist_ok=True)

    for i, pdf_path in enumerate(to_convert):
        rel_path = pdf_path.relative_to(ENNOR_DIR)
        print(f"[{i+1}/{len(to_convert)}] {rel_path}")

        meta = match_pdf_to_metadata(pdf_path, metadata)
        cat_dir = OUTPUT_DIR / meta["category_dir"]
        cat_dir.mkdir(parents=True, exist_ok=True)

        extraction = extract_pdf(pdf_path)
        if extraction.get("error"):
            print(f"  ERROR: {extraction['error']}")

        pdf_stem = pdf_path.stem
        out_name = f"{slugify(pdf_stem)}.md"
        out_path = cat_dir / out_name

        md_content = generate_markdown(meta, extraction, str(rel_path))
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        # Copy PDF to source_pdfs/
        dest_pdf_dir = source_pdfs_dir
        if pdf_path.parent != ENNOR_DIR:
            sub = pdf_path.parent.relative_to(ENNOR_DIR)
            dest_pdf_dir = source_pdfs_dir / sub
            dest_pdf_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(pdf_path, dest_pdf_dir / pdf_path.name)

        method = extraction["method"]
        pages = extraction["page_count"]
        print(f"  → {out_path.relative_to(OUTPUT_DIR)} ({pages}pp, {method})")

    # Regenerate index
    print("\nRegenerating INDEX.md...")
    results = scan_knowledge_base()
    generate_index(results)

    print(f"\nDone. {len(to_convert)} new document(s) added.")


if __name__ == "__main__":
    main()
