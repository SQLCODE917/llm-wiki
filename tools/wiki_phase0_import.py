#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


MARKDOWN_SUFFIXES = {".md", ".markdown"}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Phase 0 import and normalize one inbox source.")
    parser.add_argument(
        "source", help="source file, normally under raw/inbox/")
    parser.add_argument("slug", help="source slug, e.g. aoe2-basics")
    parser.add_argument(
        "--source-type", choices=["auto", "pdf", "markdown"], default="auto")
    parser.add_argument("--marker-bin", default="marker_single",
                        help="PDF normalizer command")
    parser.add_argument("--torch-device", default="cuda",
                        help="TORCH_DEVICE value for marker_single")
    parser.add_argument(
        "--pdf-extractor",
        choices=["auto", "marker", "pymupdf", "pdfplumber"],
        default="auto",
        help="PDF extraction backend; auto tries marker first, then pymupdf",
    )
    parser.add_argument(
        "--reuse-imported",
        action="store_true",
        help="allow an existing immutable imported original only if its bytes match the source",
    )
    parser.add_argument(
        "--overwrite-normalized",
        action="store_true",
        help="replace raw/normalized/<slug>/ before writing normalized output",
    )
    parser.add_argument(
        "--allow-outside-inbox",
        action="store_true",
        help="allow source paths outside raw/inbox/ for tests or controlled migrations",
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="print planned actions without writing files")
    args = parser.parse_args()

    repo = Path.cwd().resolve()
    source = Path(args.source)
    if not source.is_absolute():
        source = (Path.cwd() / source).resolve()
    if not source.is_file():
        print(f"FAIL: source does not exist: {source}", file=sys.stderr)
        return 2
    if not valid_slug(args.slug):
        print(
            f"FAIL: invalid slug {args.slug!r}; use lowercase letters, numbers, and hyphens", file=sys.stderr)
        return 2
    if not args.allow_outside_inbox and not is_relative_to(source, repo / "raw/inbox"):
        print(
            f"FAIL: source must be under raw/inbox/ unless --allow-outside-inbox is used: {source}", file=sys.stderr)
        return 2

    source_type = detect_source_type(source, args.source_type)
    imported_dir = repo / "raw/imported" / args.slug
    normalized_dir = repo / "raw/normalized" / args.slug
    imported_file = imported_dir / imported_filename(source_type)

    actions = planned_actions(source, imported_file,
                              normalized_dir, source_type, args)
    if args.dry_run:
        print("\n".join(actions))
        return 0

    try:
        prepare_imported(source, imported_dir,
                         imported_file, args.reuse_imported)
        prepare_normalized(normalized_dir, args.overwrite_normalized)
        if source_type == "markdown":
            normalized_target = normalized_dir / "source.md"
            shutil.copy2(source, normalized_target)
        elif source_type == "pdf":
            extractor = select_pdf_extractor(
                args.pdf_extractor, args.marker_bin)
            if extractor == "marker":
                command = marker_command(
                    args.marker_bin, source, normalized_dir)
                env = os.environ.copy()
                env["TORCH_DEVICE"] = args.torch_device
                completed = subprocess.run(
                    command, env=env, text=True, check=False)
                if completed.returncode != 0:
                    print(
                        f"FAIL: marker command exited with {completed.returncode}", file=sys.stderr)
                    return completed.returncode
            elif extractor == "pymupdf":
                if not extract_pdf_pymupdf(source, normalized_dir):
                    return 1
            elif extractor == "pdfplumber":
                if not extract_pdf_pdfplumber(source, normalized_dir):
                    return 1
            else:
                print(f"FAIL: no PDF extractor available", file=sys.stderr)
                return 1
            if not list(normalized_dir.rglob("*.md")):
                print(
                    f"FAIL: PDF extraction produced no markdown under {normalized_dir}", file=sys.stderr)
                return 1
            # Apply PDF normalization cleanup
            post_process_normalized_dir(normalized_dir)
        else:
            raise AssertionError(f"unhandled source type {source_type}")
    except Phase0Error as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print(f"imported: {imported_file.relative_to(repo).as_posix()}")
    print(f"normalized: {normalized_dir.relative_to(repo).as_posix()}/")
    return 0


class Phase0Error(Exception):
    pass


def valid_slug(slug: str) -> bool:
    return re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug) is not None


def detect_source_type(source: Path, requested: str) -> str:
    if requested != "auto":
        return requested
    suffix = source.suffix.lower()
    if suffix == ".pdf":
        return "pdf"
    if suffix in MARKDOWN_SUFFIXES:
        return "markdown"
    raise SystemExit(
        f"FAIL: cannot infer source type from {source.name!r}; pass --source-type")


def imported_filename(source_type: str) -> str:
    if source_type == "pdf":
        return "original.pdf"
    if source_type == "markdown":
        return "original.md"
    raise AssertionError(f"unhandled source type {source_type}")


def planned_actions(source: Path, imported_file: Path, normalized_dir: Path, source_type: str, args) -> list[str]:
    actions = [
        f"source_type: {source_type}",
        f"copy: {source.as_posix()} -> {imported_file.as_posix()}",
    ]
    if source_type == "markdown":
        actions.append(
            f"copy: {source.as_posix()} -> {(normalized_dir / 'source.md').as_posix()}")
    else:
        command = " ".join(marker_command(
            args.marker_bin, source, normalized_dir))
        actions.append(f"run: TORCH_DEVICE={args.torch_device} {command}")
    if args.reuse_imported:
        actions.append("reuse_imported: true")
    if args.overwrite_normalized:
        actions.append("overwrite_normalized: true")
    return actions


def prepare_imported(source: Path, imported_dir: Path, imported_file: Path, reuse_imported: bool) -> None:
    imported_dir.mkdir(parents=True, exist_ok=True)
    if imported_file.exists():
        if not reuse_imported:
            raise Phase0Error(
                f"{imported_file} already exists; raw/imported is immutable, so use a new slug or --reuse-imported if bytes match"
            )
        if sha256(source) != sha256(imported_file):
            raise Phase0Error(
                f"{imported_file} exists but does not match {source}")
        return
    existing = [path for path in imported_dir.iterdir()
                if path.name != ".keep"]
    if existing:
        names = ", ".join(path.name for path in existing)
        raise Phase0Error(f"{imported_dir} contains unexpected files: {names}")
    shutil.copy2(source, imported_file)


def prepare_normalized(normalized_dir: Path, overwrite: bool) -> None:
    if normalized_dir.exists():
        existing = [path for path in normalized_dir.iterdir()
                    if path.name != ".keep"]
        if existing and not overwrite:
            raise Phase0Error(
                f"{normalized_dir} already contains normalized output; pass --overwrite-normalized to replace it")
        if existing and overwrite:
            shutil.rmtree(normalized_dir)
    normalized_dir.mkdir(parents=True, exist_ok=True)


def marker_command(marker_bin: str, source: Path, output_dir: Path) -> list[str]:
    return [
        marker_bin,
        source.as_posix(),
        "--output_format",
        "markdown",
        "--output_dir",
        output_dir.as_posix(),
        "--disable_tqdm",
    ]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError:
        return False
    return True


def select_pdf_extractor(requested: str, marker_bin: str) -> str:
    """Select the best available PDF extractor."""
    if requested != "auto":
        return requested

    # Try marker first (best quality)
    if shutil.which(marker_bin):
        return "marker"

    # Fallback to pymupdf (fast, good quality)
    try:
        import pymupdf  # noqa: F401
        return "pymupdf"
    except ImportError:
        pass

    # Fallback to pdfplumber (slower but pure Python)
    try:
        import pdfplumber  # noqa: F401
        return "pdfplumber"
    except ImportError:
        pass

    return "none"


def extract_pdf_pymupdf(source: Path, output_dir: Path) -> bool:
    """Extract PDF to markdown using PyMuPDF (fitz)."""
    try:
        import pymupdf
    except ImportError:
        print("FAIL: pymupdf not installed", file=sys.stderr)
        return False

    try:
        doc = pymupdf.open(source)
        output_path = output_dir / "source.md"
        page_count = doc.page_count

        lines = []
        lines.append(f"# {source.stem}\n")
        lines.append(
            f"*Extracted from {source.name} ({page_count} pages)*\n\n")

        for page_num in range(page_count):
            page = doc[page_num]
            text = page.get_text("text")

            if text.strip():
                lines.append(f"\n---\n<!-- page {page_num + 1} -->\n\n")
                # Clean up the text
                cleaned = clean_extracted_text(text)
                lines.append(cleaned)

        doc.close()
        output_path.write_text("\n".join(lines))
        print(f"Extracted {page_count} pages using pymupdf")
        return True

    except Exception as e:
        print(f"FAIL: pymupdf extraction error: {e}", file=sys.stderr)
        return False


def extract_pdf_pdfplumber(source: Path, output_dir: Path) -> bool:
    """Extract PDF to markdown using pdfplumber."""
    try:
        import pdfplumber
    except ImportError:
        print("FAIL: pdfplumber not installed", file=sys.stderr)
        return False

    try:
        output_path = output_dir / "source.md"
        lines = []

        with pdfplumber.open(source) as pdf:
            lines.append(f"# {source.stem}\n")
            lines.append(
                f"*Extracted from {source.name} ({len(pdf.pages)} pages)*\n\n")

            for page_num, page in enumerate(pdf.pages):
                text = page.extract_text() or ""

                if text.strip():
                    lines.append(f"\n---\n<!-- page {page_num + 1} -->\n\n")
                    cleaned = clean_extracted_text(text)
                    lines.append(cleaned)

        output_path.write_text("\n".join(lines))
        print(f"Extracted {len(pdf.pages)} pages using pdfplumber")
        return True

    except Exception as e:
        print(f"FAIL: pdfplumber extraction error: {e}", file=sys.stderr)
        return False


def clean_extracted_text(text: str) -> str:
    """Clean up extracted text for better markdown formatting."""
    # Remove excessive whitespace
    lines = text.splitlines()
    cleaned_lines = []

    for line in lines:
        stripped = line.strip()
        if stripped:
            cleaned_lines.append(stripped)
        elif cleaned_lines and cleaned_lines[-1] != "":
            cleaned_lines.append("")  # Keep single blank lines

    # Join and remove excessive newlines
    result = "\n".join(cleaned_lines)
    result = re.sub(r'\n{3,}', '\n\n', result)

    return result


def normalize_pdf_markdown(text: str) -> str:
    """Normalize PDF-extracted markdown to improve evidence validation.

    This is a Phase 0 cleanup that makes the normalized source easier to
    work with during extraction and synthesis. It does NOT replace the
    canonicalization done during validation, but it reduces common artifacts.

    Safe transformations:
    - Join soft-hyphenated line breaks: left-\\nhand -> left-hand
    - Collapse excessive blank lines
    - Normalize dash variants to ASCII hyphen

    Unsafe/avoided transformations (done only during validation):
    - Removing page break markers (<!-- page N -->)
    - Removing page headers/footers
    - Joining all line wraps (destroys paragraph structure)
    """
    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Join soft-hyphenated line wraps:
    # left-\nhand -> left-hand (preserve the hyphen in compounds)
    # This makes evidence excerpts more likely to match
    text = re.sub(r"(\w)-\n(\w)", r"\1-\2", text)

    # Normalize Unicode dash variants to ASCII hyphen
    dash_chars = [
        "\u2010",  # Hyphen
        "\u2011",  # Non-breaking hyphen
        "\u2012",  # Figure dash
        "\u2013",  # En dash
        "\u2014",  # Em dash
        "\u2015",  # Horizontal bar
        "‐",       # Another hyphen variant
    ]
    for dash in dash_chars:
        text = text.replace(dash, "-")

    # Normalize Unicode quotes
    text = text.replace("\u2018", "'")  # Left single quote
    text = text.replace("\u2019", "'")  # Right single quote
    text = text.replace("\u201c", '"')  # Left double quote
    text = text.replace("\u201d", '"')  # Right double quote

    # Collapse excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text


def post_process_normalized_dir(normalized_dir: Path) -> None:
    """Apply normalization to all markdown files in the normalized directory."""
    for md_file in normalized_dir.rglob("*.md"):
        original = md_file.read_text()
        normalized = normalize_pdf_markdown(original)
        if normalized != original:
            md_file.write_text(normalized)
            print(f"  normalized: {md_file.name}")


if __name__ == "__main__":
    sys.exit(main())
