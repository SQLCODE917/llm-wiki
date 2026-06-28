"""Enrich structured PDF extraction with recovered table elements."""

from __future__ import annotations

import traceback
from dataclasses import dataclass
from multiprocessing import get_context
from pathlib import Path
from tempfile import TemporaryDirectory

from llmwiki.pdf.document import (
    DocumentElement,
    DocumentModel,
    document_model_from_json,
    document_model_to_json,
)
from llmwiki.pdf.table_candidate_model import TableCandidate
from llmwiki.pdf.table_candidates import table_candidates

_TABLE_ENRICHMENT_TIMEOUT_SECONDS = 5 * 60


@dataclass(frozen=True)
class _TableEnrichmentFailure:
    detail: str


def enrich_document_model_with_tables(pdf_path: Path, model: DocumentModel) -> DocumentModel:
    """Add fallback table elements that the primary extractor missed."""
    result = _enrich_document_model_isolated(pdf_path, model)
    if isinstance(result, DocumentModel):
        return result
    return model


def _enrich_document_model_isolated(
    pdf_path: Path, model: DocumentModel
) -> DocumentModel | _TableEnrichmentFailure:
    context = get_context("spawn")
    with TemporaryDirectory(prefix="llmwiki-tables-") as temp_dir:
        input_path = Path(temp_dir) / "input.json"
        output_path = Path(temp_dir) / "output.json"
        error_path = Path(temp_dir) / "error.txt"
        input_path.write_text(document_model_to_json(model), encoding="utf-8")
        process = context.Process(
            target=_table_enrichment_worker,
            args=(str(pdf_path), str(input_path), str(output_path), str(error_path)),
        )
        process.start()
        process.join(_TABLE_ENRICHMENT_TIMEOUT_SECONDS)
        if process.is_alive():
            process.terminate()
            process.join()
            return _TableEnrichmentFailure("timed out")
        if process.exitcode == 0 and output_path.is_file():
            return document_model_from_json(output_path.read_text(encoding="utf-8"))
        detail = error_path.read_text(encoding="utf-8").strip() if error_path.is_file() else ""
        return _TableEnrichmentFailure(detail or _exit_detail(process.exitcode))


def _table_enrichment_worker(
    pdf_path: str, input_path: str, output_path: str, error_path: str
) -> None:
    try:
        model = document_model_from_json(Path(input_path).read_text(encoding="utf-8"))
        enriched = _enrich_document_model_with_tables_in_process(Path(pdf_path), model)
        Path(output_path).write_text(document_model_to_json(enriched), encoding="utf-8")
    except BaseException:
        Path(error_path).write_text(traceback.format_exc(), encoding="utf-8")
        raise


def _exit_detail(exitcode: int | None) -> str:
    if exitcode is None:
        return "no child-process exit code"
    if exitcode < 0:
        return f"killed by signal {-exitcode}"
    return f"exited with code {exitcode}"


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
        )
        insert_at = _insert_index(elements, index, candidate)
        insertions.setdefault(insert_at, []).append(element)
        if index is not None and not candidate.insert_after_anchor:
            skip_ids.update(_degraded_fragment_ids(elements, index, candidate))

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
    for element in reversed(elements):
        if element.page_start <= candidate.page_start and element.heading_path:
            return element.heading_path
    return "Document"


def _page_insert_index(elements: list[DocumentElement], candidate: TableCandidate) -> int:
    for index, element in enumerate(elements):
        if element.page_start > candidate.page_start:
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
    skipped: set[str] = set()
    for element in elements[index:]:
        if element.element_kind == "heading" and element.element_id != elements[index].element_id:
            break
        if element.page_start > candidate.page_end:
            break
        text_key = _norm(element.text)
        if text_key and text_key in raw_key:
            skipped.add(element.element_id)
            continue
        if skipped:
            break
    return skipped


def _norm(text: str) -> str:
    return " ".join(text.replace("\t", " ").lower().split())
