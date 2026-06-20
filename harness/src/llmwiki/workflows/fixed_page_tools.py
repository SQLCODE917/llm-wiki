"""Workflow-specific write adapters for fixed destination pages."""

from __future__ import annotations

import json
from typing import Any, cast

from forge.core.workflow import ToolDef, ToolSpec
from pydantic import BaseModel, Field, field_validator, model_validator

from llmwiki.domain.evidence import EvidencePolicy
from llmwiki.domain.ingest_route_plan import IngestRoutePlanState
from llmwiki.domain.links import extract_links
from llmwiki.store import WikiStore, WikiStoreError
from llmwiki.workflows.source_summary_write import SourceSummaryBulletParams
from llmwiki.workflows.tools import _normalize_source_value, write_page_tool


class WriteFixedSourcePageParams(BaseModel):
    summary: str = Field(description="One-line source hub summary, used in the wiki index.")
    page_body: str | None = Field(
        default=None,
        description="Full PageBody markdown for the source hub. Link related pages "
        "inline with [[page_id]]. Cite evidence as (raw/<source_locator>). "
        "Do not include frontmatter.",
    )
    source_record_text: str | None = Field(
        default=None,
        description="For a source-summary PlannedPageWrite, short source record text.",
    )
    claim_bullets: list[SourceSummaryBulletParams] = Field(
        default_factory=list,
        description="For a source-summary PlannedPageWrite, claim bullets with coverage ids.",
    )
    sources: list[str] = Field(
        default_factory=list,
        description="Raw source paths this page draws on, e.g. ['article.md'].",
    )

    @model_validator(mode="before")
    @classmethod
    def rescue_malformed_args(cls, value: object) -> object:
        if not isinstance(value, dict):
            return value
        data: dict[str, Any] = {str(key).strip(): item for key, item in value.items()}
        summary = data.get("summary")
        if "page_body" not in data and isinstance(summary, str):
            marker = "\nparameter=page_body>\n"
            if marker in summary:
                clean_summary, page_body = summary.split(marker, maxsplit=1)
                data["summary"] = clean_summary.strip()
                data["page_body"] = page_body
        return data

    @field_validator("sources", mode="before")
    @classmethod
    def coerce_single_source(cls, value: object) -> object:
        if isinstance(value, str):
            try:
                parsed = json.loads(value)
            except json.JSONDecodeError:
                parsed = value
            if isinstance(parsed, list):
                return [_normalize_source_value(str(item)) for item in parsed]
            return [_normalize_source_value(value)]
        return value


def write_fixed_source_page_tool(
    store: WikiStore,
    today: str,
    *,
    page_id: str,
    read_tracker: set[str] | None = None,
    evidence_policy: EvidencePolicy | None = None,
    new_page_prefix: str | None = None,
    required_link_targets: tuple[str, ...] = (),
    min_required_links: int = 0,
    ingest_route_plan_state: IngestRoutePlanState | None = None,
    recoverable_errors: bool = False,
) -> ToolDef:
    required_target_set = frozenset(required_link_targets)
    base = write_page_tool(
        store,
        today,
        read_tracker=read_tracker,
        evidence_policy=evidence_policy,
        new_page_prefix=new_page_prefix,
        ingest_route_plan_state=ingest_route_plan_state,
        recoverable_errors=recoverable_errors,
    )

    def _write_page(**kwargs: object) -> str:
        params = WriteFixedSourcePageParams(**kwargs)  # type: ignore[arg-type]
        if params.source_record_text is not None or params.claim_bullets:
            if params.source_record_text is None or not params.claim_bullets:
                raise WikiStoreError(
                    "Source-summary hub writes require source_record_text and claim_bullets."
                )
            source_record_text = _source_record_with_required_links(
                params.source_record_text,
                params.claim_bullets,
                required_link_targets,
                required_target_set,
                min_required_links,
            )
            return cast(
                str,
                base.callable(
                    page_id=page_id,
                    page_kind="source",
                    summary=params.summary,
                    source_record_text=source_record_text,
                    claim_bullets=[bullet.model_dump() for bullet in params.claim_bullets],
                    sources=params.sources,
                ),
            )
        if params.page_body is None:
            raise WikiStoreError("Fixed source hub writes require page_body or SourceSummaryDraft.")
        body = _page_body_with_required_links(
            params.page_body,
            required_link_targets,
            required_target_set,
            min_required_links,
        )
        return cast(
            str,
            base.callable(
                page_id=page_id,
                page_kind="source",
                summary=params.summary,
                page_body=body,
                sources=params.sources,
            ),
        )

    return ToolDef(
        spec=ToolSpec(
            name="write_page",
            description=(
                f"Write the fixed source hub WikiPage '{page_id}'. This workflow "
                "does not create or update chapter pages."
            ),
            parameters=WriteFixedSourcePageParams,
        ),
        callable=_write_page,
    )


def _source_record_with_required_links(
    source_record_text: str,
    claim_bullets: list[SourceSummaryBulletParams],
    required_link_targets: tuple[str, ...],
    required_target_set: frozenset[str],
    min_required_links: int,
) -> str:
    if min_required_links <= 0:
        return source_record_text
    draft_text = "\n".join([source_record_text, *(bullet.bullet_text for bullet in claim_bullets)])
    linked_targets = extract_links(draft_text) & required_target_set
    if len(linked_targets) >= min_required_links:
        return source_record_text
    return _append_page_map_links(
        source_record_text,
        required_link_targets,
        linked_targets,
        min_required_links,
    )


def _page_body_with_required_links(
    page_body: str,
    required_link_targets: tuple[str, ...],
    required_target_set: frozenset[str],
    min_required_links: int,
) -> str:
    if min_required_links <= 0:
        return page_body
    linked_targets = extract_links(page_body) & required_target_set
    if len(linked_targets) >= min_required_links:
        return page_body
    return _append_page_map_links(
        page_body,
        required_link_targets,
        linked_targets,
        min_required_links,
    )


def _append_page_map_links(
    text: str,
    required_link_targets: tuple[str, ...],
    linked_targets: set[str] | frozenset[str],
    min_required_links: int,
) -> str:
    target_count = min(24, len(required_link_targets))
    missing = [page_id for page_id in required_link_targets if page_id not in linked_targets]
    fill_count = max(min_required_links - len(linked_targets), target_count)
    links = "\n".join(f"- [[{page_id}]]" for page_id in missing[:fill_count])
    return (
        f"{text.rstrip()}\n\n"
        "## Page-Map Navigation\n\n"
        "The harness added these links from the chunk page map so "
        "the book-scale hub remains navigable:\n\n"
        f"{links}"
    )
