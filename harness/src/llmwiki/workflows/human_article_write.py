"""Forge workflow for writing structured human articles from evidence packs."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from forge.core.workflow import ToolDef, ToolSpec, Workflow
from pydantic import BaseModel, Field, model_validator

from llmwiki.domain.ledger.evidence_pack import EvidencePack, EvidencePackItem, SupportRef
from llmwiki.domain.ledger.human_article import (
    ArticleBlock,
    ArticleClaim,
    ArticleFinding,
    ArticleRelatedLink,
    ArticleSection,
    HumanArticle,
)
from llmwiki.domain.model_profile import DEFAULT_MODEL_PROFILE, ModelProfile

_PROMPT_EVIDENCE_ITEM_LIMIT = 24
_PROMPT_SOURCE_TEXT_CHARS = 1_600
_PROMPT_PAYLOAD_TEXT_CHARS = 1_200
_PROMPT_JSON_OVERHEAD_CHARS = 450


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
    support_refs: list[str] = Field(
        description="Evidence support aliases from this prompt, such as S1 or S2."
    )
    claim_role: str = "fact"


class ArticleRelatedLinkParams(BaseModel):
    page_id: str
    label: str
    relation: str
    preview_text: str
    shared_support_refs: list[str] = Field(
        default_factory=list,
        description="Shared evidence support aliases from this prompt, such as S1 or S2.",
    )


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


@dataclass(frozen=True)
class ArticleSupportAlias:
    alias: str
    support_ref: SupportRef


@dataclass(frozen=True)
class ArticlePromptEvidenceItem:
    alias: str
    item: EvidencePackItem
    source_text: str
    payload_text: str
    source_text_omitted_chars: int
    payload_text_omitted_chars: int


@dataclass(frozen=True)
class ArticleSupportAliases:
    entries: tuple[ArticleSupportAlias, ...]

    @property
    def allowed_aliases(self) -> tuple[str, ...]:
        return tuple(entry.alias for entry in self.entries)

    @property
    def allowed_aliases_text(self) -> str:
        return ", ".join(self.allowed_aliases)

    def support_ref_for(self, alias: str) -> SupportRef:
        for entry in self.entries:
            if entry.alias == alias:
                return entry.support_ref
        raise ValueError(
            f"Unknown support alias {alias!r}; allowed aliases: {self.allowed_aliases_text}."
        )


def article_support_aliases(pack: EvidencePack) -> ArticleSupportAliases:
    return ArticleSupportAliases(
        tuple(
            ArticleSupportAlias(f"S{index}", item.support_ref)
            for index, item in enumerate(pack.items, start=1)
        )
    )


def article_prompt_evidence_items(
    pack: EvidencePack,
    model_profile: ModelProfile = DEFAULT_MODEL_PROFILE,
) -> tuple[ArticlePromptEvidenceItem, ...]:
    budget_chars = model_profile.chars_for_tokens(model_profile.evidence_pack_prompt_tokens)
    budget_chars = max(4_000, budget_chars - 4_000)
    selected: list[ArticlePromptEvidenceItem] = []
    used_chars = 0
    for item in pack.items:
        alias = f"S{len(selected) + 1}"
        prompt_item = ArticlePromptEvidenceItem(
            alias=alias,
            item=item,
            source_text=_exact_prefix(item.source_text, _PROMPT_SOURCE_TEXT_CHARS),
            payload_text=_exact_prefix(item.payload_text, _PROMPT_PAYLOAD_TEXT_CHARS),
            source_text_omitted_chars=_omitted_chars(
                item.source_text, _PROMPT_SOURCE_TEXT_CHARS
            ),
            payload_text_omitted_chars=_omitted_chars(
                item.payload_text, _PROMPT_PAYLOAD_TEXT_CHARS
            ),
        )
        item_chars = (
            len(prompt_item.source_text)
            + len(prompt_item.payload_text)
            + _PROMPT_JSON_OVERHEAD_CHARS
        )
        if selected and (
            len(selected) >= _PROMPT_EVIDENCE_ITEM_LIMIT
            or used_chars + item_chars > budget_chars
        ):
            break
        selected.append(prompt_item)
        used_chars += item_chars
    return tuple(selected)


def article_prompt_support_aliases(pack: EvidencePack) -> ArticleSupportAliases:
    return ArticleSupportAliases(
        tuple(
            ArticleSupportAlias(item.alias, item.item.support_ref)
            for item in article_prompt_evidence_items(pack)
        )
    )


_SYSTEM_PROMPT = """Write one structured HumanArticle from one EvidencePack.

Use only EvidencePack items as factual support. Do not write markdown headings,
frontmatter, citations, source trails, or final wiki markdown. The harness will
render markdown after validation. Every factual sentence in article blocks must
appear verbatim as one ArticleClaim.sentence and cite selected support_refs using
only support_alias values from the prompt, such as S1 or S2. If the evidence is too
weak, call write_article with empty sections and claims rather than inventing or
clipping text.

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
    aliases = article_prompt_support_aliases(pack)

    def _write_article(**kwargs: object) -> str:
        params = WriteArticleParams(**kwargs)  # type: ignore[arg-type]
        article = human_article_from_params(params, aliases)
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
                f"Use only support aliases listed in the evidence pack: "
                f"{aliases.allowed_aliases_text}."
            ),
            parameters=WriteArticleParams,
        ),
        callable=_write_article,
    )


def render_human_article_prompt(
    pack: EvidencePack, findings: tuple[ArticleFinding, ...] = ()
) -> str:
    prompt_items = article_prompt_evidence_items(pack)
    payload = {
        "page": {
            "page_id": pack.page_id,
            "page_kind": pack.page_kind,
            "page_family": pack.page_family,
            "title": pack.title,
            "source_id": pack.source_id,
            "source_profile_kind": pack.source_profile_kind,
        },
        "instructions": {
            "support_refs": "Use only support_alias values like S1 in support_refs.",
        },
        "evidence_items": [
            {
                "support_alias": prompt_item.alias,
                "evidence_record_type": prompt_item.item.evidence_record_type,
                "source_text": prompt_item.source_text,
                "payload_text": prompt_item.payload_text,
                "source_text_omitted_chars": prompt_item.source_text_omitted_chars,
                "payload_text_omitted_chars": prompt_item.payload_text_omitted_chars,
                "citation_label": prompt_item.item.citation_label,
                "section_path": prompt_item.item.section_path,
            }
            for prompt_item in prompt_items
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


def human_article_from_params(
    params: WriteArticleParams, support_aliases: ArticleSupportAliases | None = None
) -> HumanArticle:
    support_ref_from_code = (
        support_aliases.support_ref_for if support_aliases is not None else _support_ref_from_code
    )
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
                tuple(support_ref_from_code(ref) for ref in claim.support_refs),
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
                tuple(support_ref_from_code(ref) for ref in link.shared_support_refs),
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


def _exact_prefix(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip()


def _omitted_chars(text: str, max_chars: int) -> int:
    return max(0, len(text) - max_chars)
