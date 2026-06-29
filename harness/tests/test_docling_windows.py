from __future__ import annotations

import pytest

from llmwiki.pdf.docling_runtime import DoclingAttemptFailure
from llmwiki.pdf.docling_windows import (
    PageWindow,
    docling_window_timeout_seconds,
    extract_document_model_windowed,
    page_windows,
    should_use_page_windows,
)
from llmwiki.pdf.document import DocumentElement, DocumentModel


def _model(text: str, page: int = 1) -> DocumentModel:
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
                page_start=page,
                page_end=page,
                text=text,
                markdown=text,
            ),
        ),
    )


def test_page_windows_cover_document() -> None:
    assert page_windows(125, 60) == (
        PageWindow(1, 60),
        PageWindow(61, 120),
        PageWindow(121, 125),
    )


def test_should_use_page_windows_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LLMWIKI_DOCLING_FULL_PAGE_LIMIT", "10")

    assert should_use_page_windows(11) is True
    assert should_use_page_windows(10) is False


def test_window_timeout_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LLMWIKI_DOCLING_WINDOW_TIMEOUT_SECONDS", "17")

    assert docling_window_timeout_seconds() == 17


def test_windowed_extraction_merges_successful_windows(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("LLMWIKI_DOCLING_WINDOW_PAGES", "2")

    result = extract_document_model_windowed(
        3,
        "cpu",
        lambda window: _model(window.label(), window.start),
    )

    assert isinstance(result, DocumentModel)
    assert [element.text for element in result.elements] == ["pages 1-2", "pages 3-3"]
    assert [element.element_id for element in result.elements] == [
        "element-000001",
        "element-000002",
    ]


def test_windowed_extraction_splits_failed_ranges(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("LLMWIKI_DOCLING_WINDOW_PAGES", "4")
    calls: list[PageWindow] = []

    def extract(window: PageWindow) -> DocumentModel | DoclingAttemptFailure:
        calls.append(window)
        if window == PageWindow(1, 4):
            return DoclingAttemptFailure("cpu", "range failed")
        return _model(window.label(), window.start)

    result = extract_document_model_windowed(4, "cpu", extract)

    assert isinstance(result, DocumentModel)
    assert calls == [PageWindow(1, 4), PageWindow(1, 2), PageWindow(3, 4)]
    assert [element.text for element in result.elements] == ["pages 1-2", "pages 3-4"]


def test_windowed_extraction_reports_single_page_failure(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("LLMWIKI_DOCLING_WINDOW_PAGES", "1")

    result = extract_document_model_windowed(
        1,
        "cpu",
        lambda _: DoclingAttemptFailure("cpu", "segfault"),
    )

    assert result == DoclingAttemptFailure("cpu", "pages 1-1: segfault")
