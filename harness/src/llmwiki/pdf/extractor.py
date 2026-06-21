"""PyMuPDF extraction adapter: PDF -> per-page markdown + images + TOC.

The only module that touches PyMuPDF for extraction. Returns plain data;
classification and chunking decisions stay in the pure domain modules.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

import pymupdf

from llmwiki.pdf.chunking import TocEntry
from llmwiki.pdf.intermediate import relativize_image_refs

# Skip images smaller than this fraction of the page area (badges, rules).
_IMAGE_SIZE_LIMIT = 0.05


@dataclass(frozen=True)
class ExtractedPdf:
    page_texts: list[str]  # markdown per page, image refs relative to cache dir
    page_char_counts: list[int]  # raw text-layer sizes (classification input)
    toc: list[TocEntry]
    image_files: list[str]  # file names written under <cache>/images/


def read_page_char_counts(pdf_path: Path) -> list[int]:
    """Cheap text-layer probe for classification — no markdown conversion."""
    with pymupdf.open(pdf_path) as doc:  # type: ignore[no-untyped-call]
        return [len(page.get_text()) for page in doc]


def extract_pdf(pdf_path: Path, cache_dir: Path) -> ExtractedPdf:
    """Convert the PDF to per-page markdown; write figures to <cache>/images."""
    import pymupdf4llm  # type: ignore[import-untyped]

    images_dir = cache_dir / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    # page_chunks=True switches the return type to one dict per page.
    pages = cast(
        list[dict[str, Any]],
        pymupdf4llm.to_markdown(
            str(pdf_path),
            page_chunks=True,
            write_images=True,
            image_path=str(images_dir),
            image_format="jpg",
            image_size_limit=_IMAGE_SIZE_LIMIT,
            show_progress=False,
        ),
    )
    page_texts = [relativize_image_refs(page["text"], str(images_dir)) for page in pages]

    with pymupdf.open(pdf_path) as doc:  # type: ignore[no-untyped-call]
        char_counts = [len(page.get_text()) for page in doc]
        toc = [
            TocEntry(level=lvl, title=title, start_page=start)
            for lvl, title, start in doc.get_toc()
        ]

    image_files = sorted(p.name for p in images_dir.iterdir() if p.is_file())
    return ExtractedPdf(
        page_texts=page_texts,
        page_char_counts=char_counts,
        toc=toc,
        image_files=image_files,
    )
