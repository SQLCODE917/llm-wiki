"""Workflow-specific write adapters for fixed destination pages."""

from __future__ import annotations

import json
from typing import Any, cast

from forge.core.workflow import ToolDef, ToolSpec
from pydantic import BaseModel, Field, field_validator, model_validator

from llmwiki.domain.evidence import EvidencePolicy
from llmwiki.domain.links import extract_links
from llmwiki.store import WikiStore
from llmwiki.workflows.tools import _normalize_source_value, write_page_tool


class WriteFixedSourcePageParams(BaseModel):
    summary: str = Field(description="One-line source hub summary, used in the wiki index.")
    content: str = Field(
        description="Full markdown body for the source hub. Link related pages "
        "inline with [[page-name]]. Cite evidence as (raw/<source-path>). "
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
        if "content" not in data and isinstance(summary, str):
            marker = "\nparameter=content>\n"
            if marker in summary:
                clean_summary, content = summary.split(marker, maxsplit=1)
                data["summary"] = clean_summary.strip()
                data["content"] = content
        if "content" not in data:
            for alias in ("body", "page_content", "markdown"):
                if alias in data:
                    data["content"] = data[alias]
                    break
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
    page_name: str,
    read_tracker: set[str] | None = None,
    evidence_policy: EvidencePolicy | None = None,
    new_page_prefix: str | None = None,
    required_link_targets: tuple[str, ...] = (),
    min_required_links: int = 0,
) -> ToolDef:
    required_target_set = frozenset(required_link_targets)
    base = write_page_tool(
        store,
        today,
        read_tracker=None,
        evidence_policy=evidence_policy,
        new_page_prefix=new_page_prefix,
    )

    def _write_page(**kwargs: object) -> str:
        params = WriteFixedSourcePageParams(**kwargs)  # type: ignore[arg-type]
        body = params.content
        if min_required_links > 0:
            linked_targets = extract_links(body) & required_target_set
            if len(linked_targets) < min_required_links:
                target_count = min(24, len(required_link_targets))
                missing = [name for name in required_link_targets if name not in linked_targets]
                fill_count = max(min_required_links - len(linked_targets), target_count)
                links = "\n".join(f"- [[{name}]]" for name in missing[:fill_count])
                body += (
                    "\n\n## Page-Map Navigation\n\n"
                    "The harness added these links from the chunk page map so "
                    "the book-scale hub remains navigable:\n\n"
                    f"{links}"
                )
        return cast(
            str,
            base.callable(
                name=page_name,
                category="source",
                summary=params.summary,
                content=body,
                sources=params.sources,
            ),
        )

    return ToolDef(
        spec=ToolSpec(
            name="write_page",
            description=(
                f"Write the fixed source hub page '{page_name}'. This workflow "
                "does not create or update chapter pages."
            ),
            parameters=WriteFixedSourcePageParams,
        ),
        callable=_write_page,
    )
