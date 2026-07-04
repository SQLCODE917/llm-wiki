"""Forge workflow for evidence-contracted page synthesis drafts."""

from __future__ import annotations

import json
from typing import Any

from forge.core.workflow import ToolDef, ToolSpec, Workflow
from pydantic import BaseModel, Field, model_validator

from llmwiki.domain.ledger.page_synthesis import (
    DraftBlock,
    DraftClaim,
    EvidenceSupportRef,
    PageDraft,
    PageSynthesisFinding,
    PageSynthesisPlan,
)


class DraftBlockParams(BaseModel):
    block_id: str = Field(description="Stable id for this draft block, unique within the page.")
    block_kind: str = Field(description="paragraph, bullet-list, ordered-list, or table.")
    heading: str = Field(default="", description="Optional section heading for this block.")
    text: str = Field(default="", description="Paragraph text when block_kind is paragraph.")
    items: list[str] = Field(
        default_factory=list,
        description="List item text when block_kind is bullet-list or ordered-list.",
    )
    table_rows: list[list[str]] = Field(
        default_factory=list,
        description="Table rows when block_kind is table.",
    )


class DraftClaimParams(BaseModel):
    claim_id: str = Field(description="Stable id for this factual sentence claim.")
    sentence: str = Field(description="One factual sentence appearing verbatim in a draft block.")
    support_refs: list[str] = Field(
        description="Selected support refs such as ledger:entry-id, atom:atom-id, "
        "anchor:stable-anchor, or evidence-block:block-id.",
    )


class DraftPageParams(BaseModel):
    page_id: str = Field(description="The PageSynthesisPlan page_id.")
    title: str = Field(description="The PageSynthesisPlan title.")
    blocks: list[DraftBlockParams] = Field(
        description="Rendered text blocks. Do not include markdown citations."
    )
    claims: list[DraftClaimParams] = Field(
        description="One DraftClaim for every factual prose sentence in blocks."
    )

    @model_validator(mode="before")
    @classmethod
    def rescue_single_block_or_claim(cls, value: object) -> object:
        if not isinstance(value, dict):
            return value
        data: dict[str, Any] = {str(key): item for key, item in value.items()}
        if isinstance(data.get("blocks"), dict):
            data["blocks"] = [data["blocks"]]
        if isinstance(data.get("claims"), dict):
            data["claims"] = [data["claims"]]
        return data


_SYSTEM_PROMPT = """You draft one persistent wiki page from a PageSynthesisPlan.

Use only the provided evidence items as factual support. Summaries, previews,
digests, and related-link labels are navigation-only and must not become factual
page prose. Call draft_page exactly once with structured blocks and DraftClaim
records. Every factual sentence in blocks must appear verbatim as one
DraftClaim.sentence and cite selected support_refs from the plan. Do not copy
long source phrases; paraphrase while preserving facts. If the evidence is too
weak, submit an empty draft rather than inventing or clipping text.

Schema:
{schema}
"""


def build_page_synthesis_draft_workflow(plan: PageSynthesisPlan) -> Workflow:
    tool = draft_page_tool(plan)
    return Workflow(
        name="page-synthesis-draft",
        description="Draft one evidence-contracted wiki page.",
        tools={tool.name: tool},
        required_steps=[],
        terminal_tool="draft_page",
        system_prompt_template=_SYSTEM_PROMPT,
    )


def draft_page_tool(plan: PageSynthesisPlan) -> ToolDef:
    def _draft_page(**kwargs: object) -> str:
        params = DraftPageParams(**kwargs)  # type: ignore[arg-type]
        draft = page_draft_from_params(params)
        if draft.page_id != plan.page_id:
            raise ValueError(f"Draft page_id {draft.page_id!r} does not match {plan.page_id!r}.")
        return page_draft_to_json(draft)

    return ToolDef(
        spec=ToolSpec(
            name="draft_page",
            description=(
                f"Submit the structured PageDraft for [[{plan.page_id}]]. "
                "Use only support_refs listed in the prompt evidence set."
            ),
            parameters=DraftPageParams,
        ),
        callable=_draft_page,
    )


def render_page_synthesis_prompt(
    plan: PageSynthesisPlan, findings: tuple[PageSynthesisFinding, ...] = ()
) -> str:
    payload = {
        "page": {
            "page_id": plan.page_id,
            "page_kind": plan.page_kind,
            "page_family": plan.page_family,
            "title": plan.title,
            "source_page_id": plan.source_page_id,
            "source_locator": plan.source_locator,
            "source_section_page_ids": list(plan.source_section_page_ids),
        },
        "outline": [
            {
                "heading": section.heading,
                "purpose": section.purpose,
                "block_kind": section.block_kind,
                "support_refs": [ref.code for ref in section.support_refs],
            }
            for section in plan.outline
        ],
        "evidence_items": [
            {
                "support_ref": item.support_ref.code,
                "evidence_kind": item.evidence_kind,
                "section_label": item.section_label,
                "citation": item.citation,
                "source_locator": item.source_locator,
                "source_range_ids": list(item.source_range_ids),
                "ledger_entry_ids": list(item.ledger_entry_ids),
                "technical_atom_id": item.technical_atom_id,
                "evidence_block_id": item.evidence_block_id,
                "evidence_text": item.evidence_text,
            }
            for item in plan.evidence_set.items
        ],
        "related_links": [
            {
                "page_id": link.page_id,
                "label": link.label,
                "relation": link.relation,
                "shared_support_refs": [ref.code for ref in link.support_refs],
            }
            for link in plan.related_links
        ],
        "previous_validation_findings": [
            {
                "severity": finding.severity,
                "finding_type": finding.finding_type,
                "message": finding.message,
                "claim_id": finding.claim_id,
                "support_ref": finding.support_ref,
                "block_id": finding.block_id,
            }
            for finding in findings
        ],
    }
    return json.dumps(payload, ensure_ascii=True, indent=2)


def page_draft_from_params(params: DraftPageParams) -> PageDraft:
    return PageDraft(
        params.page_id,
        params.title,
        tuple(
            DraftBlock(
                block.block_id,
                block.block_kind,
                block.heading,
                block.text,
                tuple(block.items),
                tuple(tuple(row) for row in block.table_rows),
            )
            for block in params.blocks
        ),
        tuple(
            DraftClaim(
                claim.claim_id,
                claim.sentence,
                tuple(_support_ref_from_code(ref) for ref in claim.support_refs),
            )
            for claim in params.claims
        ),
    )


def page_draft_to_json(draft: PageDraft) -> str:
    return json.dumps(
        {
            "page_id": draft.page_id,
            "title": draft.title,
            "blocks": [
                {
                    "block_id": block.block_id,
                    "block_kind": block.block_kind,
                    "heading": block.heading,
                    "text": block.text,
                    "items": list(block.items),
                    "table_rows": [list(row) for row in block.table_rows],
                }
                for block in draft.blocks
            ],
            "claims": [
                {
                    "claim_id": claim.claim_id,
                    "sentence": claim.sentence,
                    "support_refs": [ref.code for ref in claim.support_refs],
                }
                for claim in draft.claims
            ],
        },
        ensure_ascii=True,
        sort_keys=True,
    )


def page_draft_from_json(text: str) -> PageDraft:
    data = json.loads(text)
    return page_draft_from_params(DraftPageParams(**data))


def _support_ref_from_code(code: str) -> EvidenceSupportRef:
    support_kind, separator, support_id = code.partition(":")
    if not separator or not support_kind or not support_id:
        raise ValueError(f"Support ref must be formatted as kind:id, got {code!r}.")
    return EvidenceSupportRef(support_kind, support_id)
