"""Page-windowed Docling extraction policy."""

from __future__ import annotations

import os
from collections.abc import Callable
from dataclasses import dataclass

from llmwiki.pdf.docling_runtime import DoclingAttemptFailure
from llmwiki.pdf.document import DocumentModel
from llmwiki.pdf.document_merge import merge_document_models

_WINDOW_PAGES_ENV = "LLMWIKI_DOCLING_WINDOW_PAGES"
_FULL_PAGE_LIMIT_ENV = "LLMWIKI_DOCLING_FULL_PAGE_LIMIT"
_WINDOW_TIMEOUT_SECONDS_ENV = "LLMWIKI_DOCLING_WINDOW_TIMEOUT_SECONDS"
_DEFAULT_WINDOW_PAGES = 40
_DEFAULT_FULL_PAGE_LIMIT = 120
_DEFAULT_WINDOW_TIMEOUT_SECONDS = 240

ExtractPageWindow = Callable[["PageWindow"], DocumentModel | DoclingAttemptFailure]


@dataclass(frozen=True)
class PageWindow:
    start: int
    end: int

    @property
    def page_count(self) -> int:
        return self.end - self.start + 1

    def split(self) -> tuple[PageWindow, PageWindow]:
        midpoint = self.start + (self.page_count // 2) - 1
        return (PageWindow(self.start, midpoint), PageWindow(midpoint + 1, self.end))

    def label(self) -> str:
        return f"pages {self.start}-{self.end}"


def should_use_page_windows(page_count: int) -> bool:
    return page_count > docling_full_page_limit()


def page_windows(page_count: int, window_pages: int | None = None) -> tuple[PageWindow, ...]:
    if page_count <= 0:
        return ()
    size = window_pages or docling_window_pages()
    return tuple(
        PageWindow(start, min(start + size - 1, page_count))
        for start in range(1, page_count + 1, size)
    )


def extract_document_model_windowed(
    page_count: int,
    device: str,
    extract_window: ExtractPageWindow,
) -> DocumentModel | DoclingAttemptFailure:
    models: list[DocumentModel] = []
    for window in page_windows(page_count):
        result = _extract_window_or_split(window, device, extract_window)
        if isinstance(result, DoclingAttemptFailure):
            return result
        models.append(result)
    if not models:
        return DoclingAttemptFailure(device, "PDF has no pages")
    return merge_document_models(tuple(models))


def docling_window_pages() -> int:
    return _positive_int_env(_WINDOW_PAGES_ENV, _DEFAULT_WINDOW_PAGES)


def docling_full_page_limit() -> int:
    return _nonnegative_int_env(_FULL_PAGE_LIMIT_ENV, _DEFAULT_FULL_PAGE_LIMIT)


def docling_window_timeout_seconds() -> int:
    return _positive_int_env(_WINDOW_TIMEOUT_SECONDS_ENV, _DEFAULT_WINDOW_TIMEOUT_SECONDS)


def _extract_window_or_split(
    window: PageWindow,
    device: str,
    extract_window: ExtractPageWindow,
) -> DocumentModel | DoclingAttemptFailure:
    result = extract_window(window)
    if isinstance(result, DocumentModel):
        return result
    if window.page_count <= 1:
        return _window_failure(device, window, result)
    left, right = window.split()
    left_result = _extract_window_or_split(left, device, extract_window)
    if isinstance(left_result, DoclingAttemptFailure):
        return left_result
    right_result = _extract_window_or_split(right, device, extract_window)
    if isinstance(right_result, DoclingAttemptFailure):
        return right_result
    return merge_document_models((left_result, right_result))


def _window_failure(
    device: str, window: PageWindow, failure: DoclingAttemptFailure
) -> DoclingAttemptFailure:
    return DoclingAttemptFailure(device, f"{window.label()}: {failure.detail}")


def _positive_int_env(name: str, default: int) -> int:
    value = _optional_int_env(name)
    if value is None:
        return default
    if value <= 0:
        raise ValueError(f"{name} must be a positive integer.")
    return value


def _nonnegative_int_env(name: str, default: int) -> int:
    value = _optional_int_env(name)
    if value is None:
        return default
    if value < 0:
        raise ValueError(f"{name} must be zero or a positive integer.")
    return value


def _optional_int_env(name: str) -> int | None:
    raw = os.environ.get(name)
    if raw is None or not raw.strip():
        return None
    try:
        return int(raw)
    except ValueError as exc:
        raise ValueError(f"{name} must be an integer.") from exc
