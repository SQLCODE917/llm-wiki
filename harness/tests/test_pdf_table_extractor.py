from pathlib import Path

import pytest

import llmwiki.pdf.table_extractor as table_extractor
from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.table_extractor import _TableEnrichmentFailure, enrich_document_model_with_tables


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
        lambda path, model: _TableEnrichmentFailure("killed by signal 11"),
    )

    assert enrich_document_model_with_tables(Path("book.pdf"), original) == original
