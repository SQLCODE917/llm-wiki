"""Wiki tools exposed to the model, bound to a WikiStore."""

from __future__ import annotations

from typing import Literal

from forge.core.workflow import ToolDef, ToolSpec
from pydantic import BaseModel, Field, field_validator

from llmwiki.domain.evidence import EvidencePolicy
from llmwiki.domain.ingest_route_plan import IngestRoutePlanError, IngestRoutePlanState
from llmwiki.domain.naming import singular_plural_collision
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.domain.search import render_hits, search_pages
from llmwiki.pdf.intermediate import OCR_MARKER
from llmwiki.store import WikiStore, WikiStoreError
from llmwiki.workflows.planned_write_tools import (
    PlannedWritePageParams as PlannedWritePageParams,
)
from llmwiki.workflows.planned_write_tools import (
    planned_write_page_tool as planned_write_page_tool,
)

_PAGE_PREVIEW_MARKER = (
    "\n\n[TRUNCATED: page preview; do not rewrite from this partial read. "
    "For this chunk, write a separate source page instead of rereading this page.]"
)


def _strip_pipeline_markers(page_body: str) -> str:
    """PageBody hygiene at the wiki boundary: extraction-pipeline markers
    (e.g. the OCR caveat tag) are internal plumbing, never PageBody content —
    observed quoted verbatim into a page despite the schema forbidding it."""
    return "\n".join(line for line in page_body.splitlines() if OCR_MARKER not in line)


def _normalize_source_value(value: str) -> str:
    stripped = value.strip()
    if "(raw/" in stripped and ")" in stripped:
        stripped = stripped.split("(raw/", 1)[1].split(")", 1)[0]
    return stripped.removeprefix("raw/")


class ReadSourceParams(BaseModel):
    source_locator: str = Field(
        description="RawSource locator relative to raw/, e.g. 'article.md'."
    )


class SearchWikiParams(BaseModel):
    query: str = Field(description="Search terms to match against WikiPage page_ids and content.")


class ReadIndexParams(BaseModel):
    """No parameters — the index is one document."""


class ReadPageParams(BaseModel):
    page_id: str = Field(description="WikiPage page_id, e.g. 'bronze-age-collapse'.")


class WritePageParams(BaseModel):
    page_id: str = Field(
        description="WikiPage page_id as a kebab-case slug. Reuse an existing page_id to update."
    )
    page_kind: Literal["source", "entity", "concept", "synthesis"] = Field(
        description="WikiPage page_kind: source (summary of one raw source), entity, "
        "concept, or synthesis (cross-source analysis)."
    )
    summary: str = Field(description="One-line summary of the page, used in the wiki index.")
    page_body: str = Field(
        description="Full PageBody markdown. Link related pages inline with [[page_id]]. "
        "Cite evidence as (raw/<source_locator>). Do not include frontmatter."
    )
    sources: list[str] = Field(
        default_factory=list,
        description="RawSource locators this page draws on, e.g. ['article.md'].",
    )

    @field_validator("sources", mode="before")
    @classmethod
    def coerce_single_source(cls, value: object) -> object:
        if isinstance(value, str):
            return [_normalize_source_value(value)]
        return value


class FinishParams(BaseModel):
    report: str = Field(description="Short report of what was done and what changed.")


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
        hits = search_pages(store.page_texts(), params.query)
        return render_hits(hits)

    return ToolDef(
        spec=ToolSpec(
            name="search_wiki",
            description="Search wiki pages by page_id and content; returns matching "
            "page_ids with snippets.",
            parameters=SearchWikiParams,
        ),
        callable=_search_wiki,
    )


def read_index_tool(store: WikiStore, read_tracker: set[str] | None = None) -> ToolDef:
    """Index-first navigation (pattern doc): the catalog answers questions
    about the wiki itself and its coverage that content search cannot."""

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


def read_page_tool(
    store: WikiStore,
    read_tracker: set[str] | None = None,
    max_chars: int | None = None,
    track_truncated_reads: bool = True,
) -> ToolDef:
    previewed: set[str] = set()

    def _read_page(**kwargs: object) -> str:
        params = ReadPageParams(**kwargs)  # type: ignore[arg-type]
        text = store.read_page(params.page_id)
        truncated = max_chars is not None and len(text) > max_chars
        if truncated and params.page_id in previewed:
            return (
                f"WikiPage '{params.page_id}' is too large for this chunk run and was "
                "already previewed. Do not call read_page for it again; write "
                "a separate source page for the current chunk or inspect a "
                "smaller related page."
            )
        if read_tracker is not None and (track_truncated_reads or not truncated):
            read_tracker.add(params.page_id)
        if truncated and max_chars is not None:
            previewed.add(params.page_id)
            return text[:max_chars] + _PAGE_PREVIEW_MARKER
        return text

    description = "Read the full text of one wiki page."
    if max_chars is not None:
        description = (
            "Read a bounded preview of one wiki page. If the result is marked "
            "TRUNCATED, do not rewrite that page from the preview."
        )
    return ToolDef(
        spec=ToolSpec(
            name="read_page",
            description=description,
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
    evidence_policy: EvidencePolicy | None = None,
    new_page_prefix: str | None = None,
    prevent_singular_plural_siblings: bool = False,
    ingest_route_plan_state: IngestRoutePlanState | None = None,
    recoverable_errors: bool = False,
) -> ToolDef:
    """write_page, optionally guarded by a read-before-rewrite contract.

    When *read_tracker* is shared with read_page_tool, rewriting an existing
    page that wasn't read this run raises — write_page replaces the whole
    page, and a 14B reliably "reconstructs" content it never saw (observed
    live twice; docs/open-questions.md #10). New pages are unaffected.

    *write_log*, when provided, records each successfully written page_id
    — the machine record behind manifest.pages_written and the salience
    write-count signal.
    """

    def _write_page(**kwargs: object) -> str:
        params = WritePageParams(**kwargs)  # type: ignore[arg-type]
        if ingest_route_plan_state is not None:
            try:
                ingest_route_plan_state.authorize_page_write(params.page_id, params.page_kind)
            except IngestRoutePlanError as exc:
                if not recoverable_errors:
                    raise
                return (
                    "No page was written. The active ingest route plan rejected "
                    f"write_page: {exc} Use a PageId and PageKind authorized by "
                    "the deterministic PagePlan, or record the material as a route "
                    "gap in plan_pages before continuing. You must successfully "
                    "write an authorized page before finish_chunk. "
                    f"Authorized targets: {_active_plan_targets(ingest_route_plan_state)}"
                )
        if (
            read_tracker is not None
            and params.page_id not in read_tracker
            and params.page_id in store.list_pages()
        ):
            if not recoverable_errors:
                raise WikiStoreError(
                    f"WikiPage '{params.page_id}' already exists and write_page replaces "
                    f"it entirely. Call read_page(page_id='{params.page_id}') first, "
                    "then rewrite it carrying forward the content you keep."
                )
            return (
                "No page was written. "
                f"WikiPage '{params.page_id}' already exists and write_page replaces "
                f"it entirely. Call read_page(page_id='{params.page_id}') first, "
                "then call write_page again carrying forward the content you keep. "
                "You must successfully write the authorized page before finishing."
            )
        if new_page_prefix is not None and params.page_id not in store.list_pages():
            valid = params.page_id == new_page_prefix or params.page_id.startswith(
                f"{new_page_prefix}-"
            )
            if not valid:
                raise WikiStoreError(
                    f"New WikiPage '{params.page_id}' must use the active ingest profile "
                    f"namespace prefix '{new_page_prefix}'. Use "
                    f"'{new_page_prefix}-{params.page_id}' "
                    "or update an existing generic page only after reading it first."
                )
        if (
            prevent_singular_plural_siblings
            and new_page_prefix is not None
            and params.page_id not in store.list_pages()
        ):
            collision = singular_plural_collision(
                params.page_id,
                set(store.list_pages()),
                namespace=new_page_prefix,
            )
            if collision is not None:
                raise WikiStoreError(collision.render_for_tool())
        body = _strip_pipeline_markers(params.page_body)
        policy = evidence_policy or EvidencePolicy()
        inventory = store.source_inventory() if policy.enabled else None
        resolver = store.source_resolver() if policy.enabled else None
        evidence = policy.check_page(params.page_id, body, inventory, resolver)
        if not evidence.allowed:
            raise WikiStoreError(
                evidence.render_for_tool(params.page_id)
                + "\nCorrect the citation path, range, or cited raw source before retrying."
            )
        page = WikiPage(
            page_metadata=PageMetadata(
                page_id=params.page_id,
                page_kind=params.page_kind,
                summary=params.summary,
                sources=tuple(params.sources),
                updated=today,
            ),
            page_body=body,
        )
        store.write_page(page)
        if write_log is not None:
            write_log.append(params.page_id)
        response = f"Wrote wiki/{params.page_id}.md and updated its index entry."
        if evidence.has_warnings:
            response += "\n\n" + evidence.render_for_tool(params.page_id)
        return response

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


def _active_plan_targets(state: IngestRoutePlanState) -> str:
    if state.active_plan is None:
        return "none; call plan_pages again."
    return ", ".join(
        f"{page.metadata.page_id} (PageKind {page.metadata.page_kind})"
        for page in state.active_plan.planned_pages
    )
