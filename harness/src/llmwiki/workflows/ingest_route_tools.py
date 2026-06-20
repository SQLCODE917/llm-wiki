"""Model-facing ingest route plan tools."""

from __future__ import annotations

from typing import Literal

from forge.core.workflow import ToolDef, ToolSpec
from pydantic import BaseModel, Field, field_validator

from llmwiki.domain.ingest_route_plan import (
    IngestRoutePlan,
    IngestRoutePlanError,
    IngestRoutePlanState,
    PlannedPage,
    RouteGap,
)
from llmwiki.domain.pages import PageMetadata
from llmwiki.workflows.tools import _normalize_source_value


class PlannedPageMetadataParams(BaseModel):
    page_id: str = Field(description="Kebab-case wiki page ID.")
    page_kind: Literal["source", "entity", "concept", "synthesis"] = Field(
        description="WikiPage page_kind."
    )
    summary: str = Field(description="One-line index summary.")
    sources: list[str] = Field(default_factory=list, description="Raw source references.")

    @field_validator("sources", mode="before")
    @classmethod
    def coerce_single_source(cls, value: object) -> object:
        if isinstance(value, str):
            return [_normalize_source_value(value)]
        return value


class PlannedPageParams(BaseModel):
    metadata: PlannedPageMetadataParams
    role: str = Field(description="Page role in this ingest route plan.")
    action: Literal["create", "enrich"] = Field(description="Whether to create or enrich.")
    source_scope: str = Field(description="Source path, chunk, page range, or locator.")
    confidence: Literal["high", "medium", "low"] = Field(description="Routing confidence.")
    rationale: str = Field(description="Why this page target belongs in the wiki.")


class RouteGapParams(BaseModel):
    reason: Literal[
        "too-granular",
        "weak-evidence",
        "ambiguous-existing-page",
        "out-of-profile-scope",
        "needs-curator-review",
    ] = Field(description="Why no page write is planned.")
    source_scope: str = Field(description="Source path, chunk, page range, or locator.")
    summary: str = Field(description="Deferred material summary.")


class PlanPagesParams(BaseModel):
    planned_pages: list[PlannedPageParams] = Field(
        description="Authorized page targets for this ingest route plan."
    )
    gaps: list[RouteGapParams] = Field(
        default_factory=list,
        description="Source material that should not become a page in this run.",
    )


def plan_pages_tool(state: IngestRoutePlanState, recoverable_errors: bool = False) -> ToolDef:
    def _plan_pages(**kwargs: object) -> str:
        params = PlanPagesParams(**kwargs)  # type: ignore[arg-type]
        plan = IngestRoutePlan(
            source_locator=state.context.source_locator,
            scope=state.context.scope,
            chunk_id=state.context.chunk_id,
            profile_ids=state.context.profile_ids,
            planned_pages=tuple(_planned_page(page) for page in params.planned_pages),
            gaps=tuple(
                RouteGap(
                    reason=gap.reason,
                    source_scope=gap.source_scope,
                    summary=gap.summary,
                )
                for gap in params.gaps
            ),
        )
        try:
            summary = state.accept(plan)
        except IngestRoutePlanError as exc:
            if not recoverable_errors:
                raise
            return (
                "No ingest route plan was accepted. The deterministic PagePlan "
                f"rejected plan_pages: {exc} Submit a new plan using only "
                "authorized PageIds, PageKinds, and plan_pages actions, or record "
                "unsupported material as a route gap."
            )
        gap_lines = "\n".join(f"- {gap.summary}" for gap in plan.gaps)
        return (
            "Validated ingest route plan: "
            f"{summary.render()}. write_page may only write planned page IDs."
            + (f"\n\nRoute gaps:\n{gap_lines}" if gap_lines else "")
        )

    return ToolDef(
        spec=ToolSpec(
            name="plan_pages",
            description=(
                "Submit the ingest route plan before page writes. The harness "
                "validates planned page IDs, page kinds, actions, source scope, "
                "naming rules, and route gaps."
            ),
            parameters=PlanPagesParams,
        ),
        callable=_plan_pages,
    )


def _planned_page(page: PlannedPageParams) -> PlannedPage:
    return PlannedPage(
        metadata=PageMetadata(
            page_id=page.metadata.page_id,
            page_kind=page.metadata.page_kind,
            summary=page.metadata.summary,
            sources=tuple(page.metadata.sources),
        ),
        role=page.role,
        action=page.action,
        source_scope=page.source_scope,
        confidence=page.confidence,
        rationale=page.rationale,
    )
