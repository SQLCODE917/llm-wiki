"""Ingest route plan contracts and validation."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

from llmwiki.domain.naming import singular_plural_collision
from llmwiki.domain.objects import (
    IngestRun,
    PagePlan,
    PlannedPageWrite,
    RawSource,
    SourceBundle,
)
from llmwiki.domain.pages import (
    PageMetadata,
    slugify,
    validate_page_id,
)

INGEST_ROUTE_PLAN_VERSION = "ingest-route-plan.v1"
PAGE_ACTIONS = ("create", "enrich")
CONFIDENCE_LEVELS = ("high", "medium", "low")
ROUTE_GAP_REASONS = (
    "too-granular",
    "weak-evidence",
    "ambiguous-existing-page",
    "out-of-profile-scope",
    "needs-curator-review",
)

type PageAction = Literal["create", "enrich"]
type ConfidenceLevel = Literal["high", "medium", "low"]
type RouteGapReason = Literal[
    "too-granular",
    "weak-evidence",
    "ambiguous-existing-page",
    "out-of-profile-scope",
    "needs-curator-review",
]
type IngestRoutePlanScope = Literal["source", "pdf-chunk", "pdf-integrate"]

__all__ = [
    "RawSource",
    "SourceBundle",
    "IngestRouteContext",
    "IngestRoutePlan",
    "IngestRoutePlanError",
    "IngestRoutePlanState",
    "IngestRoutePlanSummary",
    "IngestRun",
    "PlannedPage",
    "RouteGap",
    "validate_ingest_route_plan",
]


class IngestRoutePlanError(ValueError):
    """Invalid ingest route plan; message is safe to feed back to the model."""


@dataclass(frozen=True)
class PlannedPage:
    metadata: PageMetadata
    role: str
    action: PageAction
    source_scope: str
    confidence: ConfidenceLevel
    rationale: str

    def __post_init__(self) -> None:
        _require_text(self.role, "role")
        _require_text(self.source_scope, "source_scope")
        _require_text(self.rationale, "rationale")
        if self.action not in PAGE_ACTIONS:
            raise IngestRoutePlanError(f"Invalid planned page action {self.action!r}.")
        if self.confidence not in CONFIDENCE_LEVELS:
            raise IngestRoutePlanError(f"Invalid planned page confidence {self.confidence!r}.")


@dataclass(frozen=True)
class RouteGap:
    reason: RouteGapReason
    source_scope: str
    summary: str

    def __post_init__(self) -> None:
        if self.reason not in ROUTE_GAP_REASONS:
            raise IngestRoutePlanError(f"Invalid route gap reason {self.reason!r}.")
        _require_text(self.source_scope, "source_scope")
        _require_text(self.summary, "summary")


@dataclass(frozen=True)
class IngestRoutePlan:
    source_locator: str
    scope: IngestRoutePlanScope
    profile_ids: tuple[str, ...]
    planned_pages: tuple[PlannedPage, ...]
    gaps: tuple[RouteGap, ...] = ()
    chunk_id: int | None = None
    version: str = INGEST_ROUTE_PLAN_VERSION

    def summary(self) -> IngestRoutePlanSummary:
        return IngestRoutePlanSummary(
            planned_page_count=len(self.planned_pages),
            route_gap_count=len(self.gaps),
            route_gap_summaries=tuple(gap.summary for gap in self.gaps),
        )


@dataclass(frozen=True)
class IngestRoutePlanSummary:
    planned_page_count: int = 0
    route_gap_count: int = 0
    route_gap_summaries: tuple[str, ...] = ()

    def render(self) -> str:
        return f"planned pages: {self.planned_page_count}; route gaps: {self.route_gap_count}"


@dataclass(frozen=True)
class IngestRouteContext:
    source_locator: str
    scope: IngestRoutePlanScope
    profile_ids: tuple[str, ...] = ()
    chunk_id: int | None = None
    page_plan: PagePlan | None = None
    existing_pages: frozenset[str] = field(default_factory=frozenset)
    new_page_prefix: str | None = None
    prevent_singular_plural_siblings: bool = False


@dataclass
class IngestRoutePlanState:
    context: IngestRouteContext
    active_plan: IngestRoutePlan | None = None

    def accept(self, plan: IngestRoutePlan) -> IngestRoutePlanSummary:
        validate_ingest_route_plan(plan, self.context)
        self.active_plan = plan
        return plan.summary()

    def summary(self) -> IngestRoutePlanSummary:
        if self.active_plan is None:
            return IngestRoutePlanSummary()
        return self.active_plan.summary()

    def authorize_page_write(self, page_id: str, page_kind: str) -> PlannedPage:
        if self.active_plan is None:
            raise IngestRoutePlanError(
                "Ingest requires a validated ingest route plan before write_page."
            )
        matches = [
            page for page in self.active_plan.planned_pages if page.metadata.page_id == page_id
        ]
        if not matches:
            raise IngestRoutePlanError(
                f"Page write for {page_id!r} is not in the active ingest route plan. "
                "Call plan_pages with the intended page target or record a route gap."
            )
        planned = matches[0]
        if planned.metadata.page_kind != page_kind:
            raise IngestRoutePlanError(
                f"Page write for {page_id!r} used page_kind {page_kind!r}, "
                f"but the active ingest route plan uses {planned.metadata.page_kind!r}."
            )
        return planned

    def planned_page_write(self, page_id: str) -> PlannedPageWrite | None:
        if self.context.page_plan is None:
            return None
        matches = tuple(
            write
            for write in self.context.page_plan.planned_writes
            if write.action != "defer" and write.page_metadata.page_id == page_id
        )
        if self.context.scope == "pdf-chunk" and self.context.chunk_id is not None:
            unit_id = f"unit-{self.context.chunk_id:04d}"
            scoped = tuple(write for write in matches if unit_id in write.extracted_units)
            if scoped:
                return scoped[0]
        return next(
            iter(matches),
            None,
        )


def validate_ingest_route_plan(
    plan: IngestRoutePlan, context: IngestRouteContext
) -> IngestRoutePlan:
    if plan.version != INGEST_ROUTE_PLAN_VERSION:
        raise IngestRoutePlanError(f"Invalid ingest route plan version {plan.version!r}.")
    if plan.source_locator != context.source_locator:
        raise IngestRoutePlanError("Ingest route plan source_locator does not match this run.")
    if plan.scope != context.scope:
        raise IngestRoutePlanError("Ingest route plan scope does not match this run.")
    if plan.chunk_id != context.chunk_id:
        raise IngestRoutePlanError("Ingest route plan chunk_id does not match this run.")
    if plan.profile_ids != context.profile_ids:
        raise IngestRoutePlanError("Ingest route plan profile_ids do not match this run.")
    seen: set[str] = set()
    for planned_page in plan.planned_pages:
        page_id = validate_page_id(planned_page.metadata.page_id)
        if page_id in seen:
            raise IngestRoutePlanError(f"Duplicate planned page ID {page_id!r}.")
        seen.add(page_id)
        _validate_page_plan_target(planned_page, context)
        _validate_action_for_existing_page(planned_page, context.existing_pages)
        _validate_new_page_id(planned_page, context)
    return plan


def _validate_page_plan_target(planned_page: PlannedPage, context: IngestRouteContext) -> None:
    if context.page_plan is None:
        return
    planned_targets = _authorized_page_plan_targets(context)
    page_id = planned_page.metadata.page_id
    if page_id not in planned_targets:
        allowed = ", ".join(sorted(planned_targets)) or "none"
        raise IngestRoutePlanError(
            f"PagePlan does not authorize PageId {page_id!r}. Allowed PageIds: {allowed}."
        )
    expected_page_kind = planned_targets[page_id]
    if planned_page.metadata.page_kind != expected_page_kind:
        raise IngestRoutePlanError(
            f"PagePlan authorizes PageId {page_id!r} as PageKind {expected_page_kind!r}, "
            f"not {planned_page.metadata.page_kind!r}."
        )


def _authorized_page_plan_targets(context: IngestRouteContext) -> dict[str, str]:
    if context.page_plan is None:
        return {}
    hub_page_id = slugify(Path(context.source_locator).stem)
    targets = {
        write.page_metadata.page_id: write.page_metadata.page_kind
        for write in context.page_plan.planned_writes
        if write.action != "defer"
    }
    if context.scope == "pdf-integrate":
        return {hub_page_id: targets[hub_page_id]} if hub_page_id in targets else {}
    if context.scope != "pdf-chunk" or context.chunk_id is None:
        return targets
    unit_id = f"unit-{context.chunk_id:04d}"
    return {
        write.page_metadata.page_id: write.page_metadata.page_kind
        for write in context.page_plan.planned_writes
        if write.action != "defer"
        and write.page_metadata.page_id != hub_page_id
        and unit_id in write.extracted_units
    }


def _validate_action_for_existing_page(
    planned_page: PlannedPage, existing_pages: frozenset[str]
) -> None:
    page_id = planned_page.metadata.page_id
    exists = page_id in existing_pages
    if planned_page.action == "create" and exists:
        raise IngestRoutePlanError(f"Planned page {page_id!r} exists; use action 'enrich'.")
    if planned_page.action == "enrich" and not exists:
        raise IngestRoutePlanError(f"Planned page {page_id!r} is missing; use action 'create'.")


def _validate_new_page_id(planned_page: PlannedPage, context: IngestRouteContext) -> None:
    page_id = planned_page.metadata.page_id
    if planned_page.action != "create":
        return
    if context.new_page_prefix is not None:
        valid = page_id == context.new_page_prefix or page_id.startswith(
            f"{context.new_page_prefix}-"
        )
        if not valid:
            raise IngestRoutePlanError(
                f"New WikiPage {page_id!r} must use namespace prefix {context.new_page_prefix!r}."
            )
    if context.prevent_singular_plural_siblings and context.new_page_prefix is not None:
        collision = singular_plural_collision(
            page_id,
            set(context.existing_pages),
            namespace=context.new_page_prefix,
        )
        if collision is not None:
            raise IngestRoutePlanError(collision.render_for_tool())


def _require_text(value: str, field_name: str) -> None:
    if not value.strip():
        raise IngestRoutePlanError(f"Planned route field {field_name!r} must be non-empty.")
