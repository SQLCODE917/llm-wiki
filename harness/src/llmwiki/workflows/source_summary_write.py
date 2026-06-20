"""Shared source-summary write mapping for model-facing tools."""

from __future__ import annotations

import json
from dataclasses import asdict

from pydantic import BaseModel, Field

from llmwiki.domain.objects import PlannedPageWrite, SourceSummaryBullet, SourceSummaryDraft
from llmwiki.domain.page_body_contracts import (
    render_page_body_findings,
    render_source_summary_draft,
    validate_page_body,
    validate_source_summary_draft,
)
from llmwiki.pdf.intermediate import OCR_MARKER
from llmwiki.store import WikiStore, WikiStoreError


class SourceSummaryBulletParams(BaseModel):
    bullet_text: str = Field(
        description="One concise paraphrased claim bullet with required source citation."
    )
    covered_source_claims: list[str] = Field(
        description="SourceClaim ids from the SourceSummaryPlan covered by this bullet."
    )


class PlannedWriteSourceSummaryParams(BaseModel):
    source_record_text: str = Field(
        description="Short source record paragraph. Do not include internal SourceClaim ids."
    )
    claim_bullets: list[SourceSummaryBulletParams] = Field(
        description="Three to five concise claim bullets covering every selected SourceClaim."
    )


def strip_pipeline_markers(text: str) -> str:
    return "\n".join(line for line in text.splitlines() if OCR_MARKER not in line)


def source_summary_page_body(
    store: WikiStore,
    planned_write: PlannedPageWrite,
    source_record_text: str,
    claim_bullets: list[SourceSummaryBulletParams],
) -> tuple[str, SourceSummaryDraft]:
    if planned_write.source_summary_plan is None:
        raise WikiStoreError("This PlannedPageWrite has no SourceSummaryPlan.")
    draft = SourceSummaryDraft(
        source_record_text=strip_pipeline_markers(source_record_text),
        claim_bullets=tuple(
            SourceSummaryBullet(
                bullet_text=strip_pipeline_markers(bullet.bullet_text),
                covered_source_claims=tuple(bullet.covered_source_claims),
            )
            for bullet in claim_bullets
        ),
    )
    source_text = page_body_contract_source_text(store, planned_write)
    findings = validate_source_summary_draft(
        draft,
        planned_write.source_summary_plan,
        source_text=source_text,
    )
    if findings:
        raise WikiStoreError(
            render_page_body_findings(findings, planned_write.resolved_page_body_contract)
        )
    body = render_source_summary_draft(draft)
    body_findings = validate_page_body(
        body,
        planned_write.resolved_page_body_contract,
        source_text=source_text,
    )
    if body_findings:
        raise WikiStoreError(
            render_page_body_findings(body_findings, planned_write.resolved_page_body_contract)
        )
    return body, draft


def page_body_contract_source_text(store: WikiStore, planned_write: PlannedPageWrite) -> str:
    if not planned_write.evidence:
        return ""
    raw_source = planned_write.evidence[0].raw_source
    if raw_source.source_format != "markdown":
        return ""
    return store.read_source(raw_source.source_locator)


def write_source_summary_draft_artifact(
    store: WikiStore,
    planned_write: PlannedPageWrite,
    draft: SourceSummaryDraft,
) -> None:
    if not planned_write.evidence:
        return
    raw_source = planned_write.evidence[0].raw_source
    store.write_source_summary_draft_artifact(
        raw_source.source_locator,
        planned_write.write_id,
        json.dumps(asdict(draft), indent=2, ensure_ascii=False, sort_keys=True),
    )
