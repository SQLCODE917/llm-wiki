"""PyMuPDF adapter for DocumentModel."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any, cast

import pymupdf

from llmwiki.pdf.document import DocumentElement, DocumentModel


def extract_document_model(pdf_path: Path, source_locator: str, source_hash: str) -> DocumentModel:
    import pymupdf4llm  # type: ignore[import-untyped]

    pages = cast(
        list[dict[str, Any]],
        pymupdf4llm.to_markdown(
            str(pdf_path),
            page_chunks=True,
            write_images=False,
            show_progress=False,
        ),
    )
    heading_by_page = _heading_by_page(pdf_path)
    elements: list[DocumentElement] = []
    current_heading = ""

    for page_number, page in enumerate(pages, 1):
        heading = heading_by_page.get(page_number, current_heading or "Document")
        if heading != current_heading:
            current_heading = heading
            elements.append(
                _element(
                    index=len(elements) + 1,
                    element_kind="heading",
                    heading_path=heading,
                    page_number=page_number,
                    text=heading,
                    markdown=f"# {heading}",
                )
            )
        markdown = str(page.get("text", "")).strip()
        if markdown:
            elements.append(
                _element(
                    index=len(elements) + 1,
                    element_kind="paragraph",
                    heading_path=current_heading or "Document",
                    page_number=page_number,
                    text=markdown,
                    markdown=markdown,
                )
            )

    return DocumentModel(
        source_locator=source_locator,
        source_hash=source_hash,
        extractor_name="pymupdf4llm",
        extractor_version=_package_version("pymupdf4llm"),
        elements=tuple(elements),
    )


def _heading_by_page(pdf_path: Path) -> dict[int, str]:
    headings: dict[int, str] = {}
    active = "Document"
    with pymupdf.open(pdf_path) as doc:  # type: ignore[no-untyped-call]
        toc = sorted((int(page), str(title).strip()) for _level, title, page in doc.get_toc())
        cursor = 0
        for page_number in range(1, len(doc) + 1):
            while cursor < len(toc) and toc[cursor][0] <= page_number:
                _start_page, title = toc[cursor]
                if title:
                    active = title
                cursor += 1
            headings[page_number] = active
    return headings


def _element(
    *,
    index: int,
    element_kind: str,
    heading_path: str,
    page_number: int,
    text: str,
    markdown: str,
) -> DocumentElement:
    return DocumentElement(
        element_id=f"element-{index:06d}",
        element_kind=element_kind,
        body_state="body",
        heading_path=heading_path,
        page_start=page_number,
        page_end=page_number,
        text=text,
        markdown=markdown,
    )


def _package_version(package_name: str) -> str:
    try:
        return version(package_name)
    except PackageNotFoundError:
        return "unknown"
