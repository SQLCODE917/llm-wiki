"""Forge workflow for writing structured human articles from evidence packs."""

from __future__ import annotations

import json
from typing import Any

from forge.core.workflow import ToolDef, ToolSpec, Workflow
from pydantic import BaseModel, Field, model_validator

from llmwiki.domain.ledger.evidence_pack import EvidencePack, SupportRef
from llmwiki.domain.ledger.human_article import (
    ArticleBlock,
    ArticleClaim,
    ArticleFinding,
    ArticleRelatedLink,
    ArticleSection,
    HumanArticle,
)


class ArticleBlockParams(BaseModel):
    block_id: str
    block_kind: str = Field(description="paragraph, bullet-list, numbered-list, table, or code.")
    text: str = ""
    items: list[str] = Field(default_factory=list)
    table_rows: list[list[str]] = Field(default_factory=list)


class ArticleSectionParams(BaseModel):
    section_id: str
    heading: str
    blocks: list[ArticleBlockParams]
    article_claim_ids: list[str] = Field(default_factory=list)


class ArticleClaimParams(BaseModel):
    claim_id: str
    sentence: str
    support_refs: list[str]
    claim_role: str = "fact"


class ArticleRelatedLinkParams(BaseModel):
    page_id: str
    label: str
    relation: str
    preview_text: str
    shared_support_refs: list[str] = Field(default_factory=list)


class WriteArticleParams(BaseModel):
    page_id: str
    title: str
    sections: list[ArticleSectionParams]
    claims: list[ArticleClaimParams]
    related_links: list[ArticleRelatedLinkParams] = Field(default_factory=list)
    source_trail_items: list[str] = Field(default_factory=list)

    @model_validator(mode="before")
    @classmethod
    def rescue_singletons(cls, value: object) -> object:
        if not isinstance(value, dict):
            return value
        data: dict[str, Any] = {str(key): item for key, item in value.items()}
        for key in ("sections", "claims", "related_links", "source_trail_items"):
            if isinstance(data.get(key), dict):
                data[key] = [data[key]]
        return data


_SYSTEM_PROMPT = """Write one structured HumanArticle from one EvidencePack.

Use only EvidencePack items as factual support. Do not write markdown headings,
frontmatter, citations, source trails, or final wiki markdown. The harness will
render markdown after validation. Every factual sentence in article blocks must
appear verbatim as one ArticleClaim.sentence and cite selected support_refs from
the pack. If the evidence is too weak, call write_article with empty sections
and claims rather than inventing or clipping text.

Schema:
{schema}
"""


def build_human_article_workflow(pack: EvidencePack) -> Workflow:
    tool = write_article_tool(pack)
    return Workflow(
        name="human-article-write",
        description="Write one evidence-pack-backed HumanArticle.",
        tools={tool.name: tool},
        required_steps=[],
        terminal_tool="write_article",
        system_prompt_template=_SYSTEM_PROMPT,
    )


def write_article_tool(pack: EvidencePack) -> ToolDef:
    def _write_article(**kwargs: object) -> str:
        params = WriteArticleParams(**kwargs)  # type: ignore[arg-type]
        article = human_article_from_params(params)
        if article.page_id != pack.page_id:
            raise ValueError(
                f"Article page_id {article.page_id!r} does not match {pack.page_id!r}."
            )
        return human_article_to_json(article)

    return ToolDef(
        spec=ToolSpec(
            name="write_article",
            description=(
                f"Submit the structured HumanArticle for [[{pack.page_id}]]. "
                "Use only support_refs listed in the evidence pack."
            ),
            parameters=WriteArticleParams,
        ),
        callable=_write_article,
    )


def render_human_article_prompt(
    pack: EvidencePack, findings: tuple[ArticleFinding, ...] = ()
) -> str:
    payload = {
        "page": {
            "page_id": pack.page_id,
            "page_kind": pack.page_kind,
            "page_family": pack.page_family,
            "title": pack.title,
            "source_id": pack.source_id,
            "source_profile_kind": pack.source_profile_kind,
        },
        "evidence_items": [
            {
                "support_ref": item.support_ref.code,
                "typed_evidence_record_id": item.typed_evidence_record_id,
                "evidence_record_type": item.evidence_record_type,
                "source_block_ids": list(item.source_block_ids),
                "source_text": item.source_text,
                "payload_text": item.payload_text,
                "citation_label": item.citation_label,
                "section_path": item.section_path,
            }
            for item in pack.items
        ],
        "previous_validation_findings": [
            {
                "severity": finding.severity,
                "finding_type": finding.finding_type,
                "message": finding.message,
                "claim_id": finding.claim_id,
                "support_ref": finding.support_ref,
                "block_id": finding.block_id,
                "section_id": finding.section_id,
            }
            for finding in findings
        ],
    }
    return json.dumps(payload, ensure_ascii=True, indent=2)


def human_article_from_params(params: WriteArticleParams) -> HumanArticle:
    return HumanArticle(
        params.page_id,
        params.title,
        tuple(
            ArticleSection(
                section.section_id,
                section.heading,
                tuple(
                    ArticleBlock(
                        block.block_id,
                        block.block_kind,
                        block.text,
                        tuple(block.items),
                        tuple(tuple(row) for row in block.table_rows),
                    )
                    for block in section.blocks
                ),
                tuple(section.article_claim_ids),
            )
            for section in params.sections
        ),
        tuple(
            ArticleClaim(
                claim.claim_id,
                claim.sentence,
                tuple(_support_ref_from_code(ref) for ref in claim.support_refs),
                claim.claim_role,
            )
            for claim in params.claims
        ),
        tuple(
            ArticleRelatedLink(
                link.page_id,
                link.label,
                link.relation,
                link.preview_text,
                tuple(_support_ref_from_code(ref) for ref in link.shared_support_refs),
            )
            for link in params.related_links
        ),
        tuple(params.source_trail_items),
    )


def human_article_to_json(article: HumanArticle) -> str:
    return json.dumps(_human_article_json(article), ensure_ascii=True, sort_keys=True)


def human_article_from_json(text: str) -> HumanArticle:
    return human_article_from_params(WriteArticleParams(**json.loads(text)))


def _human_article_json(article: HumanArticle) -> dict[str, object]:
    return {
        "page_id": article.page_id,
        "title": article.title,
        "sections": [
            {
                "section_id": section.section_id,
                "heading": section.heading,
                "blocks": [
                    {
                        "block_id": block.block_id,
                        "block_kind": block.block_kind,
                        "text": block.text,
                        "items": list(block.items),
                        "table_rows": [list(row) for row in block.table_rows],
                    }
                    for block in section.blocks
                ],
                "article_claim_ids": list(section.article_claim_ids),
            }
            for section in article.sections
        ],
        "claims": [
            {
                "claim_id": claim.claim_id,
                "sentence": claim.sentence,
                "support_refs": [ref.code for ref in claim.support_refs],
                "claim_role": claim.claim_role,
            }
            for claim in article.claims
        ],
        "related_links": [
            {
                "page_id": link.page_id,
                "label": link.label,
                "relation": link.relation,
                "preview_text": link.preview_text,
                "shared_support_refs": [ref.code for ref in link.shared_support_refs],
            }
            for link in article.related_links
        ],
        "source_trail_items": list(article.source_trail_items),
    }


def _support_ref_from_code(code: str) -> SupportRef:
    support_kind, separator, support_id = code.partition(":")
    if not separator or not support_kind or not support_id:
        raise ValueError(f"Support ref must be formatted as kind:id, got {code!r}.")
    return SupportRef(support_kind, support_id)
