from pathlib import Path

import pytest

from llmwiki.pdf import docling_extractor
from llmwiki.pdf.docling_extractor import (
    _DoclingAttemptFailure,
    extract_document_model,
    pdf_pipeline_options,
)
from llmwiki.pdf.document import DocumentModel


def _model() -> DocumentModel:
    return DocumentModel(
        source_locator="book.pdf",
        source_hash="source-hash",
        extractor_name="docling",
        extractor_version="test",
        elements=(),
    )


def test_docling_pdf_options_leave_tables_to_harness_recovery() -> None:
    options = pdf_pipeline_options()

    assert options.do_ocr is False
    assert options.do_table_structure is False


def test_docling_extraction_retries_cpu_after_auto_failure(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[str] = []
    expected = _model()

    def fake_isolated(
        pdf_path: Path, source_locator: str, source_hash: str, device: str
    ) -> DocumentModel | _DoclingAttemptFailure:
        calls.append(device)
        if device == "auto":
            return _DoclingAttemptFailure(device, "killed by signal 11")
        return expected

    monkeypatch.setattr(docling_extractor, "_extract_document_model_isolated", fake_isolated)

    actual = extract_document_model(Path("book.pdf"), "book.pdf", "source-hash")

    assert actual == expected
    assert calls == ["auto", "cpu"]


def test_docling_extraction_reports_all_attempt_failures(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_isolated(
        pdf_path: Path, source_locator: str, source_hash: str, device: str
    ) -> DocumentModel | _DoclingAttemptFailure:
        return _DoclingAttemptFailure(device, f"{device} failed")

    monkeypatch.setattr(docling_extractor, "_extract_document_model_isolated", fake_isolated)

    with pytest.raises(RuntimeError, match="auto: auto failed; cpu: cpu failed"):
        extract_document_model(Path("book.pdf"), "book.pdf", "source-hash")
