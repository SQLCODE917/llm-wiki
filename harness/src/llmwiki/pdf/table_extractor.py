"""Enrich structured PDF extraction with recovered table elements."""

from __future__ import annotations

from pathlib import Path

from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.table_candidate_model import TableCandidate
from llmwiki.pdf.table_candidates import table_candidates
from llmwiki.pdf.table_runtime import (
    enrich_document_model_isolated as _enrich_document_model_isolated,
)


def enrich_document_model_with_tables(pdf_path: Path, model: DocumentModel) -> DocumentModel:
    """Add fallback table elements that the primary extractor missed."""
    result = _enrich_document_model_isolated(pdf_path, model)
    if isinstance(result, DocumentModel):
        return result
    return model


def _enrich_document_model_with_tables_in_process(
    pdf_path: Path, model: DocumentModel
) -> DocumentModel:
    candidates = table_candidates(pdf_path, model)
    if not candidates:
        return model

    elements = list(model.elements)
    insertions: dict[int, list[DocumentElement]] = {}
    skip_ids: set[str] = set()
    for offset, candidate in enumerate(candidates, start=1):
        index = _anchor_element_index(elements, candidate)
        heading_path = _heading_path_for_candidate(elements, index, candidate)
        element = DocumentElement(
            element_id=f"fallback-table-{offset:06d}",
            element_kind="table",
            body_state="body",
            heading_path=heading_path,
            page_start=candidate.page_start,
            page_end=candidate.page_end,
            text=candidate.raw_text,
            markdown=candidate.raw_text,
            layout_y0=candidate.y0,
        )
        insert_at = _insert_index(elements, index, candidate)
        insertions.setdefault(insert_at, []).append(element)
        if index is not None and not candidate.insert_after_anchor:
            skip_ids.update(_degraded_fragment_ids(elements, index, candidate))
        elif index is None:
            skip_ids.update(_degraded_fragment_ids(elements, max(0, insert_at - 1), candidate))

    enriched: list[DocumentElement] = []
    for index, element in enumerate(elements):
        enriched.extend(insertions.pop(index, ()))
        if element.element_id not in skip_ids:
            enriched.append(element)
    for remaining in (insertions[index] for index in sorted(insertions)):
        enriched.extend(remaining)
    return DocumentModel(
        source_locator=model.source_locator,
        source_hash=model.source_hash,
        extractor_name=model.extractor_name,
        extractor_version=model.extractor_version,
        elements=tuple(enriched),
    )


def _anchor_element_index(elements: list[DocumentElement], candidate: TableCandidate) -> int | None:
    anchor = candidate.anchor_text or candidate.caption
    if not anchor:
        return None
    anchor_key = _norm(anchor)
    for index, element in enumerate(elements):
        if element.page_start != candidate.page_start:
            continue
        if element.element_kind not in {"paragraph", "heading"}:
            continue
        if _norm(element.text) == anchor_key:
            return index
    return None


def _heading_path_for_candidate(
    elements: list[DocumentElement], index: int | None, candidate: TableCandidate
) -> str:
    if index is not None:
        return elements[index].heading_path
    same_page = _same_page_preceding_element(elements, candidate)
    if same_page is not None:
        return same_page.heading_path
    for element in reversed(elements):
        if element.page_start < candidate.page_start and element.heading_path:
            return element.heading_path
    return "Document"


def _same_page_preceding_element(
    elements: list[DocumentElement], candidate: TableCandidate
) -> DocumentElement | None:
    candidates = [
        (element.layout_y0, index, element)
        for index, element in enumerate(elements)
        if element.page_start == candidate.page_start
        and element.heading_path
        and element.layout_y0 <= candidate.y0
    ]
    if not candidates:
        return None
    return max(candidates, key=lambda item: (item[0], item[1]))[2]


def _page_insert_index(elements: list[DocumentElement], candidate: TableCandidate) -> int:
    for index, element in enumerate(elements):
        if element.page_start > candidate.page_start:
            return index
        if (
            element.page_start == candidate.page_start
            and candidate.y0 > 0
            and element.layout_y0 > candidate.y0
        ):
            return index
    return len(elements)


def _insert_index(
    elements: list[DocumentElement], index: int | None, candidate: TableCandidate
) -> int:
    if index is None:
        return _page_insert_index(elements, candidate)
    return index + 1 if candidate.insert_after_anchor else index


def _degraded_fragment_ids(
    elements: list[DocumentElement], index: int, candidate: TableCandidate
) -> set[str]:
    raw_key = _norm(candidate.raw_text)
    caption_key = _norm(candidate.caption)
    skipped: set[str] = set()
    for element in elements[index:]:
        if element.element_kind == "heading" and element.element_id != elements[index].element_id:
            break
        if element.page_start > candidate.page_end:
            break
        text_key = _norm(element.text)
        if (
            caption_key
            and caption_key in text_key
            and _short_caption_fragment(text_key, caption_key)
        ):
            skipped.add(element.element_id)
            continue
        if text_key and text_key in raw_key:
            skipped.add(element.element_id)
            continue
        if skipped:
            break
    return skipped


def _short_caption_fragment(text_key: str, caption_key: str) -> bool:
    return len(text_key.split()) <= len(caption_key.split()) + 3


def _norm(text: str) -> str:
    return " ".join(text.replace("\t", " ").replace("|", " ").lower().split())
