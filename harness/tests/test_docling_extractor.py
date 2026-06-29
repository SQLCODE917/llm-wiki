from pathlib import Path
from types import SimpleNamespace
from typing import Any

import pytest

from llmwiki.pdf import docling_extractor
from llmwiki.pdf.docling_extractor import (
    _DoclingAttemptFailure,
    _pdf_code_text,
    docling_devices,
    document_model_from_docling_document,
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


class _Doc:
    def __init__(self, items: tuple[Any, ...]) -> None:
        self.items = items

    def iterate_items(self) -> tuple[tuple[Any, int], ...]:
        return tuple((item, 1) for item in self.items)


class _PdfDoc:
    def __init__(self, page: Any) -> None:
        self.page = page

    def __len__(self) -> int:
        return 1

    def __getitem__(self, index: int) -> Any:
        assert index == 0
        return self.page


class _Page:
    def __init__(self) -> None:
        self.rect = SimpleNamespace(height=100.0)
        self.clip = None

    def get_text(self, kind: str, *, clip: Any, sort: bool) -> list[tuple[Any, ...]]:
        assert kind == "blocks"
        assert sort is True
        self.clip = clip
        return [
            (0, 0, 0, 0, "line one\nline two", 0, 0),
            (0, 0, 0, 0, "}", 0, 0),
        ]


def test_docling_code_block_uses_resolved_multiline_source_text() -> None:
    item = SimpleNamespace(
        label="code",
        text="line one line two }",
        prov=(SimpleNamespace(page_no=1),),
    )

    model = document_model_from_docling_document(
        _Doc((item,)),
        source_locator="source.pdf",
        source_hash="abc",
        extractor_version="test",
        code_text_resolver=lambda _: "line one\nline two\n}",
    )

    assert len(model.elements) == 1
    element = model.elements[0]
    assert element.element_kind == "code_block"
    assert element.text == "line one\nline two\n}"
    assert element.markdown == "```\nline one\nline two\n}\n```"


def test_pdf_code_text_joins_block_text_inside_docling_bbox() -> None:
    page = _Page()
    pdf_doc = _PdfDoc(page)
    bbox = SimpleNamespace(
        l=10,
        r=20,
        t=60,
        b=50,
        coord_origin=SimpleNamespace(value="BOTTOMLEFT"),
    )
    item = SimpleNamespace(prov=(SimpleNamespace(page_no=1, bbox=bbox),))

    text = _pdf_code_text(pdf_doc, item)

    assert text == "line one\nline two\n}"
    assert page.clip is not None
    assert page.clip.x0 == 9.0
    assert page.clip.y0 == 39.0
    assert page.clip.x1 == 21.0
    assert page.clip.y1 == 51.0


def test_docling_pdf_options_leave_tables_to_harness_recovery() -> None:
    options = pdf_pipeline_options()

    assert options.do_ocr is False
    if hasattr(options, "do_table_structure"):
        assert options.do_table_structure is False


def test_docling_devices_default_to_cpu(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("LLMWIKI_DOCLING_DEVICES", raising=False)

    assert docling_devices() == ("cpu",)


def test_docling_devices_accept_explicit_retry_order(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LLMWIKI_DOCLING_DEVICES", "auto,cpu")

    assert docling_devices() == ("auto", "cpu")


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

    monkeypatch.setenv("LLMWIKI_DOCLING_DEVICES", "auto,cpu")
    monkeypatch.setattr(docling_extractor, "_extract_document_model_isolated", fake_isolated)

    actual = extract_document_model(Path("book.pdf"), "book.pdf", "source-hash")

    assert actual == expected
    assert calls == ["auto", "cpu"]


def test_docling_extraction_reports_all_attempt_failures(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_isolated(
        pdf_path: Path, source_locator: str, source_hash: str, device: str
    ) -> DocumentModel | _DoclingAttemptFailure:
        return _DoclingAttemptFailure(device, f"{device} failed")

    monkeypatch.setenv("LLMWIKI_DOCLING_DEVICES", "auto,cpu")
    monkeypatch.setattr(docling_extractor, "_extract_document_model_isolated", fake_isolated)

    with pytest.raises(RuntimeError, match="auto: auto failed; cpu: cpu failed"):
        extract_document_model(Path("book.pdf"), "book.pdf", "source-hash")
