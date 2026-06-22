"""Source-scoped page helpers for ingest confidence checks."""

from __future__ import annotations

from pathlib import Path

from llmwiki.domain.pages import PageError, parse_page, slugify


def source_scoped_pages(page_texts: dict[str, str], source_locator: str) -> dict[str, str]:
    return {
        page_id: text
        for page_id, text in page_texts.items()
        if _page_matches_source(page_id, text, source_locator)
    }


def page_body(text: str) -> str:
    try:
        return parse_page(text).page_body
    except PageError:
        return text


def _page_matches_source(page_id: str, text: str, source_locator: str) -> bool:
    try:
        page = parse_page(text)
    except PageError:
        return False
    target = _normalize_source(source_locator)
    sources = (*page.sources, page.page_metadata.source_id)
    if any(_normalize_source(source) == target for source in sources):
        return True
    return page_id == slugify(Path(source_locator).stem)


def _normalize_source(source: str) -> str:
    return source.strip().removeprefix("raw/").split(" p.", maxsplit=1)[0].strip()
