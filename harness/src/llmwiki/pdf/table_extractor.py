"""Enrich structured PDF extraction with recovered table elements."""

from __future__ import annotations

import unicodedata
from pathlib import Path

from llmwiki.domain.ledger.table_cell_normalize import normalize_table_cell_text
from llmwiki.domain.ledger.tabular import row_marker_count
from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.table_candidate_model import TableCandidate
from llmwiki.pdf.table_candidate_quality import recovered_table_supersedes
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
        raw_text = _candidate_text(candidate, heading_path)
        element = DocumentElement(
            element_id=f"fallback-table-{offset:06d}",
            element_kind="table",
            body_state="body",
            heading_path=heading_path,
            page_start=candidate.page_start,
            page_end=candidate.page_end,
            text=raw_text,
            markdown=raw_text,
            layout_y0=candidate.y0,
        )
        insert_at = _insert_index(elements, index, candidate)
        insertions.setdefault(insert_at, []).append(element)
        if index is not None:
            skip_start = index + 1 if candidate.insert_after_anchor else index
            skip_ids.update(_degraded_fragment_ids(elements, skip_start, candidate, raw_text))
        elif index is None:
            skip_ids.update(
                _degraded_fragment_ids(elements, max(0, insert_at - 1), candidate, raw_text)
            )
        skip_ids.update(_superseded_table_ids(elements, candidate, raw_text))

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


def _candidate_text(candidate: TableCandidate, heading_path: str) -> str:
    title = _source_heading_title(heading_path)
    raw_text = candidate.raw_text.strip()
    if candidate.caption or not title or _norm(raw_text).startswith(_norm(title)):
        return raw_text
    return f"{title}\n{raw_text}"


def _source_heading_title(heading_path: str) -> str:
    title = " ".join((heading_path or "").split(">")[-1].split())
    if not title or title == "Document" or title.lower().endswith(".pdf"):
        return ""
    return title


def _degraded_fragment_ids(
    elements: list[DocumentElement], index: int, candidate: TableCandidate, raw_text: str
) -> set[str]:
    raw_key = _norm(raw_text)
    caption_key = _norm(candidate.caption)
    heading_path = elements[index].heading_path if index < len(elements) else ""
    skipped: set[str] = set()
    start_element_id = elements[index].element_id if index < len(elements) else ""
    for offset, element in enumerate(elements[index:], start=index):
        if element.element_kind == "heading" and element.element_id != start_element_id:
            break
        if element.page_start > candidate.page_end:
            break
        text_key = _norm(element.text)
        if skipped and _same_fragment_run(
            elements, offset, heading_path, raw_key, text_key, candidate.page_end
        ):
            skipped.add(element.element_id)
            continue
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


def _same_fragment_run(
    elements: list[DocumentElement],
    index: int,
    heading_path: str,
    raw_key: str,
    text_key: str,
    page_end: int,
) -> bool:
    element = elements[index]
    if element.heading_path != heading_path:
        return False
    text = element.text or element.markdown
    return (
        bool(text_key and text_key in raw_key)
        or row_marker_count(text) > 0
        or _punctuation_only(text)
        or (
            _short_recovered_cell_fragment(text_key, raw_key)
            and _row_marker_ahead(elements, index, heading_path, page_end)
        )
    )


def _superseded_table_ids(
    elements: list[DocumentElement], candidate: TableCandidate, raw_text: str
) -> set[str]:
    return {
        element.element_id
        for element in elements
        if element.element_kind == "table"
        and not (element.page_end < candidate.page_start or candidate.page_end < element.page_start)
        and recovered_table_supersedes(raw_text, element.text)
    }


def _short_caption_fragment(text_key: str, caption_key: str) -> bool:
    return len(text_key.split()) <= len(caption_key.split()) + 3


def _punctuation_only(text: str) -> bool:
    return bool(text.strip()) and not any(char.isalnum() for char in text)


def _short_recovered_cell_fragment(text_key: str, raw_key: str) -> bool:
    words = _content_words(text_key)
    if not words or len(words) > 6:
        return False
    return set(words).issubset(set(_content_words(raw_key)))


def _row_marker_ahead(
    elements: list[DocumentElement], index: int, heading_path: str, page_end: int
) -> bool:
    for element in elements[index + 1 :]:
        if element.element_kind == "heading" or element.heading_path != heading_path:
            return False
        if element.page_start > page_end:
            return False
        if row_marker_count(element.text or element.markdown) > 0:
            return True
    return False


def _content_words(text_key: str) -> tuple[str, ...]:
    words: list[str] = []
    for token in text_key.split():
        word = token.strip(".,;:!?()[]{}\"'")
        if word and any(char.isalnum() for char in word):
            words.append(word)
    return tuple(words)


def _norm(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = normalize_table_cell_text(text)
    return " ".join(text.replace("\t", " ").replace("|", " ").lower().split())
