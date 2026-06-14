"""Wiki tools exposed to the model, bound to a WikiStore.

Each callable validates its arguments with the same Pydantic model that the
LLM sees as the tool schema, then delegates to the store. Domain/store
errors raise with corrective messages — forge feeds them back on the
tool-error channel for self-correction.
"""

from __future__ import annotations

from typing import Literal

from forge.core.workflow import ToolDef, ToolSpec
from pydantic import BaseModel, Field

from llmwiki.domain.pages import WikiPage
from llmwiki.domain.search import render_hits, search_pages
from llmwiki.pdf.intermediate import OCR_MARKER
from llmwiki.store import WikiStore, WikiStoreError


def _strip_pipeline_markers(content: str) -> str:
    """Content hygiene at the wiki boundary: extraction-pipeline markers
    (e.g. the OCR caveat tag) are internal plumbing, never wiki content —
    observed quoted verbatim into a page despite the schema forbidding it."""
    return "\n".join(line for line in content.splitlines() if OCR_MARKER not in line)


class ReadSourceParams(BaseModel):
    path: str = Field(description="Source path relative to raw/, e.g. 'article.md'.")


class SearchWikiParams(BaseModel):
    query: str = Field(description="Search terms to match against wiki page names and content.")


class ReadIndexParams(BaseModel):
    """No parameters — the index is one document."""


class ReadPageParams(BaseModel):
    name: str = Field(description="Wiki page name (kebab-case slug), e.g. 'bronze-age-collapse'.")


class WritePageParams(BaseModel):
    name: str = Field(
        description="Page name as a kebab-case slug. Reuse an existing name to update that page."
    )
    category: Literal["source", "entity", "concept", "synthesis"] = Field(
        description="Page category: source (summary of one raw source), entity, "
        "concept, or synthesis (cross-source analysis)."
    )
    summary: str = Field(description="One-line summary of the page, used in the wiki index.")
    content: str = Field(
        description="Full markdown body. Link related pages inline with [[page-name]]. "
        "Cite evidence as (raw/<source-path>). Do not include frontmatter."
    )
    sources: list[str] = Field(
        default_factory=list,
        description="Raw source paths this page draws on, e.g. ['article.md'].",
    )


class FinishParams(BaseModel):
    report: str = Field(description="Short report of what was done and what changed.")


def read_source_tool(store: WikiStore) -> ToolDef:
    def _read_source(**kwargs: object) -> str:
        params = ReadSourceParams(**kwargs)  # type: ignore[arg-type]
        return store.read_source(params.path)

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
        hits = search_pages(store.page_texts(), params.query)
        return render_hits(hits)

    return ToolDef(
        spec=ToolSpec(
            name="search_wiki",
            description="Search wiki pages by name and content; returns matching "
            "page names with snippets.",
            parameters=SearchWikiParams,
        ),
        callable=_search_wiki,
    )


def read_index_tool(store: WikiStore) -> ToolDef:
    """Index-first navigation (pattern doc): the catalog answers questions
    about the wiki itself and its coverage that content search cannot."""

    def _read_index(**kwargs: object) -> str:
        ReadIndexParams(**kwargs)
        return store.read_index()

    return ToolDef(
        spec=ToolSpec(
            name="read_index",
            description="Read the wiki's index: the catalog of every page "
            "with a one-line summary, grouped by category. Use this for "
            "questions about the wiki itself or what it covers.",
            parameters=ReadIndexParams,
        ),
        callable=_read_index,
    )


def read_page_tool(store: WikiStore, read_tracker: set[str] | None = None) -> ToolDef:
    def _read_page(**kwargs: object) -> str:
        params = ReadPageParams(**kwargs)  # type: ignore[arg-type]
        text = store.read_page(params.name)
        if read_tracker is not None:
            read_tracker.add(params.name)
        return text

    return ToolDef(
        spec=ToolSpec(
            name="read_page",
            description="Read the full text of one wiki page.",
            parameters=ReadPageParams,
        ),
        callable=_read_page,
    )


def write_page_tool(
    store: WikiStore,
    today: str,
    prerequisites: list[str | dict[str, str]] | None = None,
    read_tracker: set[str] | None = None,
    write_log: list[str] | None = None,
) -> ToolDef:
    """write_page, optionally guarded by a read-before-rewrite contract.

    When *read_tracker* is shared with read_page_tool, rewriting an existing
    page that wasn't read this run raises — write_page replaces the whole
    page, and a 14B reliably "reconstructs" content it never saw (observed
    live twice; docs/open-questions.md #10). New pages are unaffected.

    *write_log*, when provided, records each successfully written page name
    — the machine record behind manifest.pages_written and the salience
    write-count signal.
    """

    def _write_page(**kwargs: object) -> str:
        params = WritePageParams(**kwargs)  # type: ignore[arg-type]
        if (
            read_tracker is not None
            and params.name not in read_tracker
            and params.name in store.list_pages()
        ):
            raise WikiStoreError(
                f"Page '{params.name}' already exists and write_page replaces "
                f"it entirely. Call read_page(name='{params.name}') first, "
                "then rewrite it carrying forward the content you keep."
            )
        page = WikiPage(
            name=params.name,
            category=params.category,
            summary=params.summary,
            body=_strip_pipeline_markers(params.content),
            sources=tuple(params.sources),
            updated=today,
        )
        store.write_page(page)
        if write_log is not None:
            write_log.append(params.name)
        return f"Wrote wiki/{params.name}.md and updated its index entry."

    return ToolDef(
        spec=ToolSpec(
            name="write_page",
            description="Create a new wiki page, or update one you have "
            "already read this run (write replaces the whole page); the "
            "index entry is maintained automatically.",
            parameters=WritePageParams,
        ),
        callable=_write_page,
        prerequisites=prerequisites or [],
    )


def finish_tool(name: str, description: str) -> ToolDef:
    def _finish(**kwargs: object) -> str:
        params = FinishParams(**kwargs)  # type: ignore[arg-type]
        return params.report

    return ToolDef(
        spec=ToolSpec(name=name, description=description, parameters=FinishParams),
        callable=_finish,
    )
