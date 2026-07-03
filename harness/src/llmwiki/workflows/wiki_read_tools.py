"""Forge adapters for reading and inspecting the wiki."""

from __future__ import annotations

from forge.core.workflow import ToolDef, ToolSpec
from pydantic import BaseModel, Field

from llmwiki.domain.chat_evidence_scope import ChatEvidenceScope
from llmwiki.domain.page_inspection import inspect_page_text, render_page_map
from llmwiki.domain.pages import parse_page
from llmwiki.domain.retrieval import render_context_pack, retrieve_wiki_context
from llmwiki.store import WikiStore, WikiStoreError

_READ_PAGE_DEFAULT_CHARS = 3_000
_READ_PAGE_MAX_CHARS = 5_000
type _FocusKey = tuple[tuple[str, ...], str]


class ReadSourceParams(BaseModel):
    source_locator: str = Field(
        description="RawSource locator relative to raw/, e.g. 'article.md'."
    )


class SearchWikiParams(BaseModel):
    query: str = Field(
        description="Search question or terms to match against the wiki index, page metadata, "
        "headings, links, and content."
    )


class ReadIndexParams(BaseModel):
    """No parameters - the index is one document."""


class InspectPageParams(BaseModel):
    page_id: str = Field(description="WikiPage page_id, e.g. 'bronze-age-collapse'.")
    max_sections: int = Field(
        default=40,
        ge=1,
        le=80,
        description="Maximum number of headings/sections to include in the compact page map.",
    )
    focus_query: str | None = Field(
        default=None,
        description=(
            "Optional topic or procedure phrase. When provided, the page map prioritizes "
            "matching section headings plus their ancestors and nearby siblings; if no "
            "headings match, treat that as missing coverage unless another page names "
            "the target directly."
        ),
    )


class ReadPageParams(BaseModel):
    page_id: str = Field(description="WikiPage page_id, e.g. 'bronze-age-collapse'.")
    offset: int = Field(
        default=0,
        ge=0,
        description="Character offset for chunked reads of large WikiPages.",
    )
    max_chars: int = Field(
        default=_READ_PAGE_DEFAULT_CHARS,
        ge=1,
        le=_READ_PAGE_MAX_CHARS,
        description=(
            "Maximum characters to return. Keep reads targeted; use offset for additional "
            "chunks only when the first chunk does not contain enough evidence."
        ),
    )


def read_source_tool(store: WikiStore) -> ToolDef:
    def _read_source(**kwargs: object) -> str:
        params = ReadSourceParams(**kwargs)  # type: ignore[arg-type]
        return store.read_source(params.source_locator)

    return ToolDef(
        spec=ToolSpec(
            name="read_source",
            description="Read one immutable source document from raw/.",
            parameters=ReadSourceParams,
        ),
        callable=_read_source,
    )


def search_wiki_tool(store: WikiStore) -> ToolDef:
    def _search_wiki(**kwargs: object) -> str:
        params = SearchWikiParams(**kwargs)  # type: ignore[arg-type]
        pack = retrieve_wiki_context(
            query=params.query,
            index_text=store.read_index(),
            page_texts=store.page_texts(),
        )
        return render_context_pack(pack)

    return ToolDef(
        spec=ToolSpec(
            name="search_wiki",
            description="Search the wiki's compiled navigation artifacts; returns matching "
            "page_ids with snippets, nearby links, and why each page matched.",
            parameters=SearchWikiParams,
        ),
        callable=_search_wiki,
    )


def read_index_tool(store: WikiStore, read_tracker: set[str] | None = None) -> ToolDef:
    """Index-first navigation for coverage/catalog questions."""

    def _read_index(**kwargs: object) -> str:
        ReadIndexParams(**kwargs)
        if read_tracker is not None:
            read_tracker.add("index.md")
        return store.read_index()

    return ToolDef(
        spec=ToolSpec(
            name="read_index",
            description="Read the wiki's index: the catalog of every page "
            "with a one-line summary, grouped by page_kind. Use this for "
            "questions about the wiki itself or what it covers.",
            parameters=ReadIndexParams,
        ),
        callable=_read_index,
    )


def inspect_page_tool(
    store: WikiStore, missing_focus_reports: set[str] | None = None
) -> ToolDef:
    missing_focus_by_source: set[_FocusKey] = set()

    def _inspect_page(**kwargs: object) -> str:
        params = InspectPageParams(**kwargs)  # type: ignore[arg-type]
        page_map = inspect_page_text(
            params.page_id,
            store.read_page(params.page_id),
            max_sections=params.max_sections,
            focus_query=params.focus_query,
        )
        focus_key = _focus_key(page_map.sources, params.focus_query)
        if focus_key is not None and focus_key in missing_focus_by_source:
            return _render_missing_focus_stop(page_map.sources, params.focus_query or "")
        if (
            focus_key is not None
            and page_map.page_family == "source-manifest"
            and page_map.focus_matched_sections == 0
        ):
            missing_focus_by_source.add(focus_key)
            if missing_focus_reports is not None:
                missing_focus_reports.add(
                    _missing_focus_label(page_map.sources, params.focus_query)
                )
        return render_page_map(page_map)

    return ToolDef(
        spec=ToolSpec(
            name="inspect_page",
            description=(
                "Return a compact map of one wiki page: metadata, related pages, headings, "
                "section character ranges, and source-range ids. Use this before read_page "
                "for complex procedures or large pages."
            ),
            parameters=InspectPageParams,
        ),
        callable=_inspect_page,
    )


def read_page_tool(
    store: WikiStore,
    read_tracker: set[str] | None = None,
    evidence_scope: ChatEvidenceScope | None = None,
) -> ToolDef:
    def _read_page(**kwargs: object) -> str:
        params = ReadPageParams(**kwargs)  # type: ignore[arg-type]
        text = store.read_page(params.page_id)
        if evidence_scope is not None:
            metadata = parse_page(text).page_metadata
            decision = evidence_scope.read_decision(metadata)
            if not decision.allowed:
                raise WikiStoreError(decision.message)
        if read_tracker is not None:
            read_tracker.add(params.page_id)
        return _read_page_chunk(params.page_id, text, params.offset, params.max_chars)

    return ToolDef(
        spec=ToolSpec(
            name="read_page",
            description=(
                "Read a bounded chunk of one wiki page. Use search_wiki first, then read only "
                "the most relevant page chunks needed to answer."
            ),
            parameters=ReadPageParams,
        ),
        callable=_read_page,
    )


def _focus_key(sources: tuple[str, ...], focus_query: str | None) -> _FocusKey | None:
    if not focus_query or not sources:
        return None
    return (tuple(sorted(sources)), " ".join(focus_query.lower().split()))


def _render_missing_focus_stop(sources: tuple[str, ...], focus_query: str) -> str:
    source_text = ", ".join(sources)
    return (
        "Focused source coverage was already checked on the source manifest.\n"
        f"source scope: {source_text}\n"
        f"focus query: {focus_query!r}\n"
        "No manifest section headings matched this focus. Stop inspecting related "
        "pages for this same source/procedure and answer that the wiki lacks "
        "source-backed procedure coverage unless another retrieved source page "
        "names it directly."
    )


def _missing_focus_label(sources: tuple[str, ...], focus_query: str | None) -> str:
    query = " ".join((focus_query or "").split())
    return f"{','.join(sorted(sources))}::{query}"


def _read_page_chunk(page_id: str, text: str, offset: int, max_chars: int) -> str:
    start = min(offset, len(text))
    end = min(start + max_chars, len(text))
    chunk = text[start:end]
    if start == 0 and end == len(text):
        return chunk
    lines = [
        f"[Showing wiki/{page_id}.md characters {start}-{end} of {len(text)}.]",
        "",
        chunk,
    ]
    if end < len(text):
        lines.extend(["", f"[Truncated. Continue with read_page offset={end}.]"])
    return "\n".join(lines)
