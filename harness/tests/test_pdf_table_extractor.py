from pathlib import Path

import pytest

import llmwiki.pdf.table_extractor as table_extractor
from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.table_candidate_model import TableCandidate
from llmwiki.pdf.table_extractor import (
    _enrich_document_model_with_tables_in_process,
    enrich_document_model_with_tables,
)
from llmwiki.pdf.table_runtime import TableEnrichmentFailure


def _model(text: str) -> DocumentModel:
    return DocumentModel(
        source_locator="book.pdf",
        source_hash="source-hash",
        extractor_name="docling",
        extractor_version="test",
        elements=(
            DocumentElement(
                element_id="element-000001",
                element_kind="paragraph",
                body_state="body",
                heading_path="Document",
                page_start=1,
                page_end=1,
                text=text,
                markdown=text,
            ),
        ),
    )


def test_table_enrichment_uses_isolated_result(monkeypatch: pytest.MonkeyPatch) -> None:
    original = _model("body")
    enriched = _model("body with recovered table")

    monkeypatch.setattr(
        table_extractor, "_enrich_document_model_isolated", lambda path, model: enriched
    )

    assert enrich_document_model_with_tables(Path("book.pdf"), original) == enriched


def test_table_enrichment_keeps_original_model_after_native_failure(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    original = _model("body")

    monkeypatch.setattr(
        table_extractor,
        "_enrich_document_model_isolated",
        lambda path, model: TableEnrichmentFailure("killed by signal 11"),
    )

    assert enrich_document_model_with_tables(Path("book.pdf"), original) == original


def test_unanchored_table_uses_nearest_preceding_layout_heading(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    model = DocumentModel(
        source_locator="book.pdf",
        source_hash="source-hash",
        extractor_name="docling",
        extractor_version="test",
        elements=(
            _element("e1", "heading", "Traits > Virtue", "Virtue", 90.0),
            _element("e2", "list_item", "Traits > Virtue", "1 Ambitious 6 Honorable", 120.0),
            _element("e3", "heading", "Bonds", "Bonds", 320.0),
            _element("e4", "paragraph", "Bonds", "D20 Bond", 350.0),
        ),
    )
    candidate = TableCandidate(
        caption="",
        page_start=1,
        page_end=1,
        y0=118.0,
        raw_text="| 1 | Ambitious | 6 | Honorable |",
        extractor_stage="pymupdf-find-tables",
    )
    monkeypatch.setattr(table_extractor, "table_candidates", lambda path, model: (candidate,))

    enriched = _enrich_document_model_with_tables_in_process(Path("book.pdf"), model)
    table = next(element for element in enriched.elements if element.element_kind == "table")
    element_ids = [element.element_id for element in enriched.elements]

    assert table.heading_path == "Traits > Virtue"
    assert table.layout_y0 == 118.0
    assert element_ids.index(table.element_id) < element_ids.index("e3")
    assert "e2" not in element_ids


def _element(
    element_id: str,
    kind: str,
    heading_path: str,
    text: str,
    y0: float,
) -> DocumentElement:
    return DocumentElement(
        element_id=element_id,
        element_kind=kind,
        body_state="body",
        heading_path=heading_path,
        page_start=1,
        page_end=1,
        text=text,
        markdown=text,
        layout_y0=y0,
    )
