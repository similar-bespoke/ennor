#!/usr/bin/env python3
"""
Ennor Technical Manuals → QMD-Ready Markdown Converter

Converts all PDFs in the Ennor repo into well-structured Markdown files
with YAML frontmatter, ready for Etta to index via QMD.

Usage:
    python3 convert_to_markdown.py

Output:
    ennor_knowledge_base/
    ├── INDEX.md              (master reference)
    ├── 01_engine_bay/
    │   ├── 1.1_yanmar_8lv370.md
    │   └── ...
    ├── 02_energy_management/
    │   └── ...
    └── ...
"""

import fitz  # PyMuPDF
import os
import re
import sys
import hashlib
from pathlib import Path
from datetime import datetime

# Optional OCR imports
try:
    from pdf2image import convert_from_path
    import pytesseract
    HAS_OCR = True
except ImportError:
    HAS_OCR = False
    print("WARNING: pdf2image/pytesseract not available. Scanned PDFs will have limited text.")


# === Configuration ===

ENNOR_DIR = Path(__file__).parent.parent  # repo root (scripts/ is one level down)
OUTPUT_DIR = ENNOR_DIR / "ennor_knowledge_base"
MIN_CHARS_FOR_NATIVE = 50  # avg chars per page below this = likely scanned
OCR_DPI = 200

# Category mapping from base_content.md section numbers
CATEGORIES = {
    "0": ("00_vessel_specification", "Vessel Specification"),
    "1": ("01_engine_bay", "Engine Bay"),
    "2": ("02_energy_management", "Energy Management"),
    "3": ("03_thrusters", "Thrusters"),
    "4": ("04_helm", "Helm"),
    "5": ("05_topside", "Topside"),
    "6": ("06_galley", "Galley"),
    "7": ("07_cockpit", "Cockpit"),
    "8": ("08_pumps_and_heads", "Pumps & Heads"),
    "9": ("09_sundries", "Sundries"),
}


# === Metadata Parsing ===

def parse_base_content(path: Path) -> dict:
    """Parse base_content.md to build doc_id → metadata mapping."""
    metadata = {}
    current_category = None

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip()

            # Section headers like "## 1. Engine Bay"
            m = re.match(r"^## (\d+)\.\s+(.+)", line)
            if m:
                current_category = m.group(1)
                continue

            # List items like "- 1.1 Yanmar 8LV370 -"
            m = re.match(r"^\s*-\s+(\d+(?:\.\d+)+)\s+(.+)", line)
            if m:
                doc_id = m.group(1)
                # Clean up the description: remove trailing dashes, bold markers, links
                desc = m.group(2).strip().rstrip("-").strip()
                desc = re.sub(r"\*\*[^*]+\*\*", "", desc).strip()  # remove **notes**
                desc = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", desc)  # [text](url) → text
                desc = re.sub(r"\s+", " ", desc).strip().rstrip("-").strip()

                # Determine category from doc_id prefix
                cat_key = doc_id.split(".")[0]
                if cat_key in CATEGORIES:
                    cat_dir, cat_name = CATEGORIES[cat_key]
                else:
                    cat_dir, cat_name = "99_other", "Other"

                metadata[doc_id] = {
                    "doc_id": doc_id,
                    "title": desc if desc else doc_id,
                    "category": cat_name,
                    "category_dir": cat_dir,
                }

    return metadata


def match_pdf_to_metadata(pdf_path: Path, metadata: dict) -> dict:
    """Match a PDF filename to its metadata entry."""
    filename = pdf_path.name

    # Extract doc_id from filename (e.g., "2.1.1 Mastervolt..." → "2.1.1")
    m = re.match(r"^(\d+(?:\.\d+)*)\s+", filename)
    if m:
        doc_id = m.group(1)
        if doc_id in metadata:
            return metadata[doc_id]

        # Build metadata from filename if not in base_content.md
        desc = filename[m.end():].replace(".pdf", "").strip()
        cat_key = doc_id.split(".")[0]
        cat_dir, cat_name = CATEGORIES.get(cat_key, ("99_other", "Other"))
        return {
            "doc_id": doc_id,
            "title": desc if desc else doc_id,
            "category": cat_name,
            "category_dir": cat_dir,
        }

    # CZone library files — no doc_id prefix
    desc = filename.replace(".pdf", "").strip()
    return {
        "doc_id": "",
        "title": desc,
        "category": "Energy Management",
        "category_dir": "02_energy_management/czone",
    }


# === PDF Text Extraction ===

def extract_native_text(doc: fitz.Document) -> tuple[list[str], float]:
    """Extract text using PyMuPDF's native text layer. Returns (pages, avg_chars)."""
    pages = []
    total_chars = 0
    for i in range(doc.page_count):
        text = doc[i].get_text("text")
        pages.append(text)
        total_chars += len(text)
    avg = total_chars / doc.page_count if doc.page_count > 0 else 0
    return pages, avg


def ocr_pdf(pdf_path: Path, dpi: int = 200) -> list[str]:
    """OCR a scanned PDF page by page. Memory-safe: one page at a time."""
    if not HAS_OCR:
        return []

    pages = []
    try:
        # Get page count first
        doc = fitz.open(str(pdf_path))
        page_count = doc.page_count
        doc.close()

        for i in range(page_count):
            try:
                images = convert_from_path(
                    str(pdf_path),
                    dpi=dpi,
                    first_page=i + 1,
                    last_page=i + 1,
                )
                if images:
                    text = pytesseract.image_to_string(images[0])
                    pages.append(text)
                del images
            except Exception as e:
                pages.append(f"[OCR failed for page {i+1}: {e}]")
                continue
    except Exception as e:
        print(f"  OCR error: {e}")
    return pages


def extract_pdf(pdf_path: Path) -> dict:
    """Extract text from a PDF, using OCR fallback if needed."""
    try:
        doc = fitz.open(str(pdf_path))
    except Exception as e:
        return {
            "pages": [],
            "page_count": 0,
            "method": "error",
            "error": str(e),
        }

    page_count = doc.page_count
    pages, avg_chars = extract_native_text(doc)
    doc.close()

    if avg_chars >= MIN_CHARS_FOR_NATIVE:
        return {
            "pages": pages,
            "page_count": page_count,
            "method": "native",
        }

    # Scanned PDF — try OCR
    print(f"  Low text density ({avg_chars:.0f} avg chars/page), attempting OCR...")
    ocr_pages = ocr_pdf(pdf_path, OCR_DPI)
    if ocr_pages:
        return {
            "pages": ocr_pages,
            "page_count": page_count,
            "method": "ocr",
        }

    # Return whatever native extraction got (may be sparse)
    return {
        "pages": pages,
        "page_count": page_count,
        "method": "native_limited",
    }


# === Text Cleaning ===

def clean_text(text: str) -> str:
    """Clean extracted text for markdown output."""
    # Collapse excessive whitespace
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    # Remove common PDF artifacts
    text = re.sub(r"^\d{2}/\d{2}/\d{4},?\s*\d{2}:\d{2}.*$", "", text, flags=re.MULTILINE)
    # Remove form feed characters
    text = text.replace("\x0c", "")
    # Strip trailing whitespace per line
    text = "\n".join(line.rstrip() for line in text.splitlines())
    return text.strip()


# === Markdown Generation ===

def slugify(text: str) -> str:
    """Convert text to a filesystem-safe slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "_", text)
    text = text.strip("_")
    return text[:80]


def generate_markdown(meta: dict, extraction: dict, source_pdf: str) -> str:
    """Generate a complete markdown document with YAML frontmatter."""
    lines = []

    # YAML frontmatter
    lines.append("---")
    lines.append("vessel: Ennor")
    if meta["doc_id"]:
        lines.append(f'doc_id: "{meta["doc_id"]}"')
    lines.append(f'title: "{meta["title"]}"')
    lines.append(f'category: "{meta["category"]}"')
    lines.append(f'source_pdf: "{source_pdf}"')
    lines.append(f'extraction_method: {extraction["method"]}')
    lines.append(f"page_count: {extraction['page_count']}")
    lines.append(f'converted: "{datetime.now().strftime("%Y-%m-%d")}"')
    lines.append("---")
    lines.append("")

    # Document header
    lines.append(f"# {meta['title']}")
    lines.append("")
    if meta["doc_id"]:
        lines.append(f"**Vessel:** Ennor | **Section:** {meta['doc_id']} | **Category:** {meta['category']}")
    else:
        lines.append(f"**Vessel:** Ennor | **Category:** {meta['category']}")
    lines.append(f"**Source PDF:** {source_pdf} | **Pages:** {extraction['page_count']} | **Extraction:** {extraction['method']}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Page content
    if extraction.get("error"):
        lines.append(f"> **Extraction Error:** {extraction['error']}")
        lines.append(">")
        lines.append("> This PDF could not be opened. It may be corrupted or password-protected.")
    elif not extraction["pages"]:
        lines.append("> **No text could be extracted from this PDF.**")
    else:
        for i, page_text in enumerate(extraction["pages"]):
            cleaned = clean_text(page_text)
            if cleaned:
                if extraction["page_count"] > 5:
                    lines.append(f"## Page {i+1}")
                    lines.append("")
                lines.append(cleaned)
                lines.append("")

    return "\n".join(lines)


# === Main Pipeline ===

def find_all_pdfs(base_dir: Path) -> list[Path]:
    """Find all PDFs in the repo."""
    pdfs = []
    for root, dirs, files in os.walk(base_dir):
        # Skip output directory and .git
        rel = Path(root).relative_to(base_dir)
        if str(rel).startswith(("ennor_knowledge_base", ".git", "encrypted")):
            continue
        for f in sorted(files):
            if f.lower().endswith(".pdf"):
                pdfs.append(Path(root) / f)
    return pdfs


def main():
    print("=" * 60)
    print("Ennor Technical Manuals → QMD-Ready Markdown")
    print("=" * 60)

    # Parse metadata from base_content.md
    base_content = ENNOR_DIR / "base_content.md"
    if base_content.exists():
        metadata = parse_base_content(base_content)
        print(f"\nParsed {len(metadata)} entries from base_content.md")
    else:
        metadata = {}
        print("\nWARNING: base_content.md not found, using filename-only metadata")

    # Find all PDFs
    pdfs = find_all_pdfs(ENNOR_DIR)
    print(f"Found {len(pdfs)} PDFs to convert\n")

    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Track results for INDEX.md
    results = []
    errors = []

    for i, pdf_path in enumerate(pdfs):
        rel_path = pdf_path.relative_to(ENNOR_DIR)
        print(f"[{i+1}/{len(pdfs)}] {rel_path}")

        # Match to metadata
        meta = match_pdf_to_metadata(pdf_path, metadata)

        # Create category subdirectory
        cat_dir = OUTPUT_DIR / meta["category_dir"]
        cat_dir.mkdir(parents=True, exist_ok=True)

        # Extract text
        extraction = extract_pdf(pdf_path)

        if extraction.get("error"):
            errors.append((str(rel_path), extraction["error"]))
            print(f"  ERROR: {extraction['error']}")

        # Generate output filename — use PDF filename to avoid collisions
        # when multiple PDFs share the same doc_id (e.g., 5.4 has 3 Omnisense PDFs)
        pdf_stem = pdf_path.stem  # e.g. "5.4 Omnisense Ulysses-Micro-Manual"
        out_name = f"{slugify(pdf_stem)}.md"

        out_path = cat_dir / out_name

        # Generate and write markdown
        md_content = generate_markdown(meta, extraction, str(rel_path))
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        result_out = str(out_path.relative_to(OUTPUT_DIR))
        method = extraction["method"]
        pages = extraction["page_count"]
        print(f"  → {result_out} ({pages}pp, {method})")

        results.append({
            "meta": meta,
            "output": result_out,
            "pages": pages,
            "method": method,
            "has_error": bool(extraction.get("error")),
        })

    # Generate INDEX.md
    print(f"\nGenerating INDEX.md...")
    generate_index(results, errors)

    # Summary
    print("\n" + "=" * 60)
    print("CONVERSION COMPLETE")
    print("=" * 60)
    native = sum(1 for r in results if r["method"] == "native")
    ocr = sum(1 for r in results if r["method"] == "ocr")
    limited = sum(1 for r in results if r["method"] == "native_limited")
    errs = sum(1 for r in results if r["has_error"])
    print(f"  Total files: {len(results)}")
    print(f"  Native text: {native}")
    print(f"  OCR:         {ocr}")
    print(f"  Limited:     {limited}")
    print(f"  Errors:      {errs}")
    print(f"\nOutput: {OUTPUT_DIR}")
    print(f"\nTo index with QMD on Aetidigm:")
    print(f"  qmd add ennor /path/to/ennor_knowledge_base")
    print(f"  qmd update && qmd embed")


def generate_index(results: list, errors: list):
    """Generate the master INDEX.md file."""
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

    # Group by category
    by_category = {}
    for r in results:
        cat = r["meta"]["category"]
        by_category.setdefault(cat, []).append(r)

    for cat_name, cat_results in by_category.items():
        lines.append(f"## {cat_name}")
        lines.append("")
        lines.append("| Doc ID | Title | Pages | Extraction |")
        lines.append("|--------|-------|-------|------------|")
        for r in sorted(cat_results, key=lambda x: x["meta"]["doc_id"]):
            doc_id = r["meta"]["doc_id"] or "-"
            title = r["meta"]["title"]
            pages = r["pages"]
            method = r["method"]
            flag = " ⚠" if r["has_error"] else ""
            lines.append(f"| {doc_id} | {title} | {pages} | {method}{flag} |")
        lines.append("")

    if errors:
        lines.append("## Extraction Errors")
        lines.append("")
        for pdf_name, err in errors:
            lines.append(f"- **{pdf_name}**: {err}")
        lines.append("")

    with open(OUTPUT_DIR / "INDEX.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
