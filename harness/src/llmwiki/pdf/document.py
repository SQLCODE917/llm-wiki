"""Structured PDF extraction domain objects."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass

from llmwiki.pdf.chunking import CHUNK_TOKEN_BUDGET, estimate_tokens


@dataclass(frozen=True)
class DocumentElement:
    element_id: str
    element_kind: str
    body_state: str
    heading_path: str
    page_start: int
    page_end: int
    text: str
    markdown: str
    heading_level: int = 0


@dataclass(frozen=True)
class DocumentModel:
    source_locator: str
    source_hash: str
    extractor_name: str
    extractor_version: str
    elements: tuple[DocumentElement, ...]


@dataclass(frozen=True)
class SourceSection:
    section_id: str
    heading_path: str
    page_start: int
    page_end: int
    element_ids: tuple[str, ...]
    text: str


@dataclass(frozen=True)
class SourceChunk:
    chunk_id: int
    source_section_id: str
    heading_path: str
    page_start: int
    page_end: int
    text: str
    token_estimate: int


def document_model_to_json(model: DocumentModel) -> str:
    return json.dumps(asdict(model), indent=2, ensure_ascii=False)


def document_model_from_json(text: str) -> DocumentModel:
    data = json.loads(text)
    return DocumentModel(
        source_locator=data["source_locator"],
        source_hash=data["source_hash"],
        extractor_name=data["extractor_name"],
        extractor_version=data["extractor_version"],
        elements=tuple(DocumentElement(**element) for element in data["elements"]),
    )


def source_sections_to_json(sections: tuple[SourceSection, ...]) -> str:
    return json.dumps([asdict(section) for section in sections], indent=2, ensure_ascii=False)


def source_sections_from_json(text: str) -> tuple[SourceSection, ...]:
    data = json.loads(text)
    return tuple(
        SourceSection(
            section_id=section["section_id"],
            heading_path=section["heading_path"],
            page_start=section["page_start"],
            page_end=section["page_end"],
            element_ids=tuple(section["element_ids"]),
            text=section["text"],
        )
        for section in data
    )


def build_source_sections(model: DocumentModel) -> tuple[SourceSection, ...]:
    sections: list[SourceSection] = []
    current_heading = "Document"
    current_elements: list[DocumentElement] = []

    def flush() -> None:
        nonlocal current_elements
        section = _make_section(current_heading, current_elements, len(sections) + 1)
        if section is not None:
            sections.append(section)
        current_elements = []

    for element in model.elements:
        if element.body_state != "body":
            continue
        if not _element_markdown(element):
            continue
        if element.element_kind == "heading":
            flush()
            current_heading = element.heading_path or element.text or "Document"
            current_elements.append(element)
            continue
        element_heading = element.heading_path or current_heading
        if current_elements and element_heading != current_heading:
            flush()
            current_heading = element_heading
        elif not current_elements:
            current_heading = element_heading
        current_elements.append(element)

    flush()
    return tuple(sections)


def build_source_chunks(
    model: DocumentModel,
    sections: tuple[SourceSection, ...],
    budget_tokens: int = CHUNK_TOKEN_BUDGET,
) -> tuple[SourceChunk, ...]:
    chunks: list[SourceChunk] = []
    elements_by_id = {element.element_id: element for element in model.elements}

    for section in sections:
        section_elements = tuple(
            elements_by_id[element_id]
            for element_id in section.element_ids
            if element_id in elements_by_id
        )
        if not section_elements:
            _append_chunk(chunks, section, section.text)
            continue

        current: list[DocumentElement] = []
        part_no = 1

        def flush(flush_section: SourceSection) -> None:
            nonlocal current, part_no
            if not current:
                return
            text = _join_element_markdown(current)
            if part_no > 1 and not text.lstrip().startswith("#"):
                text = f"## {flush_section.heading_path}\n\n{text}"
            _append_chunk(chunks, flush_section, text, current)
            current = []
            part_no += 1

        for element in section_elements:
            element_text = _element_markdown(element)
            if not element_text:
                continue
            candidate = _join_element_markdown((*current, element))
            if current and estimate_tokens(candidate) > budget_tokens:
                flush(section)
            current.append(element)
        flush(section)

    return tuple(chunks)


def _append_chunk(
    chunks: list[SourceChunk],
    section: SourceSection,
    text: str,
    elements: list[DocumentElement] | None = None,
) -> None:
    page_start, page_end = (
        _element_page_span(elements) if elements else (section.page_start, section.page_end)
    )
    chunks.append(
        SourceChunk(
            chunk_id=len(chunks) + 1,
            source_section_id=section.section_id,
            heading_path=section.heading_path,
            page_start=page_start,
            page_end=page_end,
            text=text,
            token_estimate=estimate_tokens(text),
        )
    )


def _make_section(
    heading_path: str, elements: list[DocumentElement], section_number: int
) -> SourceSection | None:
    text = _join_element_markdown(elements)
    if not text:
        return None
    page_start, page_end = _element_page_span(elements)
    return SourceSection(
        section_id=f"section-{section_number:04d}-{_slug(heading_path)}",
        heading_path=heading_path,
        page_start=page_start,
        page_end=page_end,
        element_ids=tuple(element.element_id for element in elements),
        text=text,
    )


def _join_element_markdown(elements: tuple[DocumentElement, ...] | list[DocumentElement]) -> str:
    return "\n\n".join(
        element_text for element in elements if (element_text := _element_markdown(element))
    ).strip()


def _element_markdown(element: DocumentElement) -> str:
    return (element.markdown or element.text).strip()


def _element_page_span(
    elements: tuple[DocumentElement, ...] | list[DocumentElement],
) -> tuple[int, int]:
    page_starts = [element.page_start for element in elements if element.page_start > 0]
    page_ends = [element.page_end for element in elements if element.page_end > 0]
    if not page_starts or not page_ends:
        return (0, 0)
    return (min(page_starts), max(page_ends))


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:80] or "document"
