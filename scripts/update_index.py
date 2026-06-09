#!/usr/bin/env python3
"""
Regenerate INDEX.md from existing markdown files in ennor_knowledge_base/.

Use this after adding, removing, or re-converting individual documents
without needing to re-run the full conversion pipeline.

Usage:
    python3 scripts/update_index.py
"""

import os
import re
from pathlib import Path
from datetime import datetime


ENNOR_DIR = Path(__file__).parent.parent
OUTPUT_DIR = ENNOR_DIR / "ennor_knowledge_base"

# Reverse lookup: directory name → display name
DIR_TO_CATEGORY = {
    "00_vessel_specification": "Vessel Specification",
    "01_engine_bay": "Engine Bay",
    "02_energy_management": "Energy Management",
    "03_thrusters": "Thrusters",
    "04_helm": "Helm",
    "05_topside": "Topside",
    "06_galley": "Galley",
    "07_cockpit": "Cockpit",
    "08_pumps_and_heads": "Pumps & Heads",
    "09_sundries": "Sundries",
}


def parse_frontmatter(filepath: Path) -> dict:
    """Extract YAML frontmatter fields from a markdown file."""
    meta = {}
    in_frontmatter = False
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "---":
                if in_frontmatter:
                    break  # end of frontmatter
                in_frontmatter = True
                continue
            if in_frontmatter:
                m = re.match(r'^(\w+):\s*"?(.+?)"?\s*$', line)
                if m:
                    meta[m.group(1)] = m.group(2)
    return meta


def scan_knowledge_base() -> list[dict]:
    """Scan all markdown files and extract their metadata."""
    results = []

    for root, dirs, files in os.walk(OUTPUT_DIR):
        # Skip source_pdfs
        rel_root = Path(root).relative_to(OUTPUT_DIR)
        if str(rel_root).startswith("source_pdfs"):
            continue

        for f in sorted(files):
            if not f.endswith(".md") or f == "INDEX.md":
                continue

            filepath = Path(root) / f
            meta = parse_frontmatter(filepath)

            # Determine category from directory
            parts = rel_root.parts
            if parts:
                top_dir = parts[0]
                category = DIR_TO_CATEGORY.get(top_dir, top_dir)
                # Sub-categories (e.g., czone/)
                if len(parts) > 1:
                    sub = " / ".join(p.replace("_", " ").title() for p in parts[1:])
                    category = f"{category} / {sub}"
            else:
                category = "Uncategorised"

            results.append({
                "doc_id": meta.get("doc_id", "-"),
                "title": meta.get("title", f),
                "category": category,
                "category_sort": top_dir if parts else "zz_uncategorised",
                "page_count": meta.get("page_count", "?"),
                "extraction_method": meta.get("extraction_method", "?"),
                "source_pdf": meta.get("source_pdf", ""),
                "filepath": str(filepath.relative_to(OUTPUT_DIR)),
                "has_error": meta.get("extraction_method") == "error",
            })

    return results


def generate_index(results: list[dict]):
    """Write INDEX.md from scanned results."""
    lines = []
    lines.append("---")
    lines.append("vessel: Ennor")
    lines.append('title: "Ennor Technical Manuals - Master Index"')
    lines.append(f'generated: "{datetime.now().strftime("%Y-%m-%d %H:%M")}"')
    lines.append(f"total_documents: {len(results)}")
    lines.append("---")
    lines.append("")
    lines.append("# Ennor Technical Manuals - Master Index")
    lines.append("")
    lines.append("**Vessel:** Ennor | **Call Sign:** MRRX5 | **MMSI:** 232059754 | **Registration:** SSR301572")
    lines.append("")
    lines.append("This knowledge base contains extracted text from all Ennor technical manuals,")
    lines.append("organized by vessel system category. Each document includes YAML frontmatter")
    lines.append("with structured metadata for search and filtering.")
    lines.append("")

    # Group by category, sorted by directory prefix (00_, 01_, etc.)
    by_category = {}
    cat_sort_keys = {}
    for r in results:
        cat = r["category"]
        by_category.setdefault(cat, []).append(r)
        cat_sort_keys.setdefault(cat, r.get("category_sort", cat))

    for cat_name in sorted(by_category.keys(), key=lambda c: cat_sort_keys.get(c, c)):
        cat_results = by_category[cat_name]
        lines.append(f"## {cat_name}")
        lines.append("")
        lines.append("| Doc ID | Title | Pages | Extraction |")
        lines.append("|--------|-------|-------|------------|")
        for r in sorted(cat_results, key=lambda x: x["doc_id"]):
            doc_id = r["doc_id"]
            title = r["title"]
            pages = r["page_count"]
            method = r["extraction_method"]
            flag = " ⚠" if r["has_error"] else ""
            lines.append(f"| {doc_id} | {title} | {pages} | {method}{flag} |")
        lines.append("")

    errors = [r for r in results if r["has_error"]]
    if errors:
        lines.append("## Extraction Errors")
        lines.append("")
        for r in errors:
            lines.append(f"- **{r['source_pdf']}**: Could not be opened (may be corrupted or placeholder)")
        lines.append("")

    index_path = OUTPUT_DIR / "INDEX.md"
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"INDEX.md updated: {len(results)} documents across {len(by_category)} categories")


def main():
    if not OUTPUT_DIR.exists():
        print(f"ERROR: {OUTPUT_DIR} does not exist. Run convert_to_markdown.py first.")
        return

    results = scan_knowledge_base()
    generate_index(results)


if __name__ == "__main__":
    main()
