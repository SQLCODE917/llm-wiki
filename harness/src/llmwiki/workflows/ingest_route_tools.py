"""Model-facing ingest route plan tools."""

from __future__ import annotations

import ast
from typing import Literal, cast

from forge.core.workflow import ToolDef, ToolSpec
from pydantic import BaseModel, Field, ValidationError, field_validator

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


def plan_pages_tool(
    state: IngestRoutePlanState,
    recoverable_errors: bool = False,
    prerequisites: list[str] | None = None,
) -> ToolDef:
    tool_prerequisites: list[str | dict[str, str]] = list(prerequisites or [])

    def _plan_pages(**kwargs: object) -> str:
        kwargs = _rescued_plan_pages_kwargs(kwargs, state)
        try:
            params = PlanPagesParams(**kwargs)  # type: ignore[arg-type]
        except ValidationError as exc:
            if not recoverable_errors:
                raise
            return _recoverable_plan_error(
                "plan_pages arguments did not match the required schema:\n"
                f"{exc}\n"
                "Each planned page must include metadata {page_id, page_kind, "
                "summary, sources}, role, action, source_scope, confidence, "
                "and rationale."
            )
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
            return _recoverable_plan_error(
                "The deterministic PagePlan rejected plan_pages: "
                f"{exc} Submit a new plan using only authorized PageIds, "
                "PageKinds, and plan_pages actions, or record unsupported "
                "material as a route gap."
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
        prerequisites=tool_prerequisites,
    )


def _recoverable_plan_error(detail: str) -> str:
    return (
        "No ingest route plan was accepted.\n"
        f"{detail}\n"
        "Call plan_pages again with a corrected full replacement plan before "
        "calling write_page."
    )


def _rescued_plan_pages_kwargs(
    kwargs: dict[str, object],
    state: IngestRoutePlanState,
) -> dict[str, object]:
    if state.context.page_plan is None:
        return kwargs
    planned_pages = kwargs.get("planned_pages")
    if isinstance(planned_pages, str):
        planned_pages = _literal_list(planned_pages)
    if not isinstance(planned_pages, list):
        return kwargs
    rescued = dict(kwargs)
    rescued["planned_pages"] = [
        _rescued_planned_page(page, state) if isinstance(page, dict) else page
        for page in planned_pages
    ]
    rescued.setdefault("gaps", [])
    return rescued


def _literal_list(value: str) -> object:
    try:
        parsed = ast.literal_eval(value)
    except (SyntaxError, ValueError, SystemError):
        return value
    return parsed if isinstance(parsed, list) else value


def _rescued_planned_page(
    page: dict[object, object],
    state: IngestRoutePlanState,
) -> dict[str, object]:
    raw_metadata = page.get("metadata")
    metadata = (
        dict(cast(dict[object, object], raw_metadata)) if isinstance(raw_metadata, dict) else {}
    )
    page_id = str(metadata.get("page_id") or page.get("page_id") or "")
    planned_write = state.planned_page_write(page_id) if page_id else None
    if planned_write is not None:
        page_metadata = planned_write.page_metadata
        metadata.setdefault("page_id", page_metadata.page_id)
        metadata.setdefault("page_kind", page_metadata.page_kind)
        metadata.setdefault("summary", page_metadata.summary)
        metadata.setdefault("sources", list(page_metadata.sources))
    else:
        metadata.setdefault("page_id", page_id)
        if "page_kind" in page:
            metadata.setdefault("page_kind", page["page_kind"])
        metadata.setdefault(
            "summary",
            page_id.replace("-", " ").title() if page_id else "Source page",
        )
        metadata.setdefault("sources", [f"raw/{state.context.source_locator}"])
    rescued = {
        "metadata": metadata,
        "role": page.get("role") or _default_role(planned_write),
        "action": _rescued_action(page.get("action"), page_id, state),
        "source_scope": _rescued_source_scope(page.get("source_scope"), state),
        "confidence": _rescued_confidence(page.get("confidence")),
        "rationale": page.get("rationale") or _default_rationale(page_id),
    }
    return rescued


def _default_role(planned_write: object | None) -> str:
    if getattr(planned_write, "source_summary_plan", None) is not None:
        return "source-summary"
    return "source page for this ingest stage"


def _rescued_action(value: object, page_id: str, state: IngestRoutePlanState) -> str:
    _ = value
    return "enrich" if page_id in state.context.existing_pages else "create"


def _rescued_source_scope(value: object, state: IngestRoutePlanState) -> str:
    if isinstance(value, str) and value.strip():
        return value
    return f"raw/{state.context.source_locator}"


def _rescued_confidence(value: object) -> str:
    if value in ("high", "medium", "low"):
        return str(value)
    return "high"


def _default_rationale(page_id: str) -> str:
    if page_id:
        return f"{page_id} is authorized by the deterministic PagePlan."
    return "This page target is authorized by the deterministic PagePlan."


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
