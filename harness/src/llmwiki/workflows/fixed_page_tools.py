"""Workflow-specific write adapters for fixed destination pages."""

from __future__ import annotations

import json
from typing import Any, cast

from forge.core.workflow import ToolDef, ToolSpec
from pydantic import BaseModel, Field, field_validator, model_validator

from llmwiki.domain.evidence import EvidencePolicy
from llmwiki.domain.ingest_route_plan import IngestRoutePlanState
from llmwiki.domain.links import extract_links
from llmwiki.store import WikiStore
from llmwiki.workflows.tools import _normalize_source_value, write_page_tool


class WriteFixedSourcePageParams(BaseModel):
    summary: str = Field(description="One-line source hub summary, used in the wiki index.")
    page_body: str = Field(
        description="Full PageBody markdown for the source hub. Link related pages "
        "inline with [[page_id]]. Cite evidence as (raw/<source_locator>). "
        "Do not include frontmatter."
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
        body = params.page_body
        if min_required_links > 0:
            linked_targets = extract_links(body) & required_target_set
            if len(linked_targets) < min_required_links:
                target_count = min(24, len(required_link_targets))
                missing = [
                    page_id for page_id in required_link_targets if page_id not in linked_targets
                ]
                fill_count = max(min_required_links - len(linked_targets), target_count)
                links = "\n".join(f"- [[{page_id}]]" for page_id in missing[:fill_count])
                body += (
                    "\n\n## Page-Map Navigation\n\n"
                    "The harness added these links from the chunk page map so "
                    "the book-scale hub remains navigable:\n\n"
                    f"{links}"
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
