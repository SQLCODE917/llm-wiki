"""Structured human article contracts for generated public pages."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from llmwiki.domain.ledger.coverage import ProjectionCoverage
from llmwiki.domain.ledger.evidence_pack import EvidencePack, SupportRef


@dataclass(frozen=True)
class ArticleBlock:
    block_id: str
    block_kind: str
    text: str = ""
    items: tuple[str, ...] = ()
    table_rows: tuple[tuple[str, ...], ...] = ()


@dataclass(frozen=True)
class ArticleSection:
    section_id: str
    heading: str
    blocks: tuple[ArticleBlock, ...]
    article_claim_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class ArticleClaim:
    claim_id: str
    sentence: str
    support_refs: tuple[SupportRef, ...]
    claim_role: str = "fact"


@dataclass(frozen=True)
class ArticleCitation:
    claim_id: str
    support_ref: SupportRef
    citation_label: str
    source_anchor_label: str = ""


@dataclass(frozen=True)
class ArticleRelatedLink:
    page_id: str
    label: str
    relation: str
    preview_text: str
    shared_support_refs: tuple[SupportRef, ...] = ()


@dataclass(frozen=True)
class ArticleFinding:
    severity: str
    finding_type: str
    page_id: str
    message: str
    claim_id: str = ""
    support_ref: str = ""
    block_id: str = ""
    section_id: str = ""


@dataclass(frozen=True)
class HumanArticle:
    page_id: str
    title: str
    sections: tuple[ArticleSection, ...]
    claims: tuple[ArticleClaim, ...]
    related_links: tuple[ArticleRelatedLink, ...] = ()
    source_trail_items: tuple[str, ...] = ()
    findings: tuple[ArticleFinding, ...] = ()


@dataclass(frozen=True)
class ArticleValidationResult:
    accepted: bool
    findings: tuple[ArticleFinding, ...]


@dataclass(frozen=True)
class HumanArticleRecord:
    article: HumanArticle
    page_body_hash: str
    projection_coverage: ProjectionCoverage


@dataclass(frozen=True)
class HumanArticleOutput:
    records: tuple[HumanArticleRecord, ...]
    findings: tuple[ArticleFinding, ...]


class ArticleWriter(Protocol):
    def write_article(
        self,
        pack: EvidencePack,
        findings: tuple[ArticleFinding, ...] = (),
    ) -> HumanArticle: ...


class RejectingArticleWriter:
    """Default writer when no model-backed article implementation is enabled."""

    def write_article(
        self,
        pack: EvidencePack,
        findings: tuple[ArticleFinding, ...] = (),
    ) -> HumanArticle:
        return HumanArticle(pack.page_id, pack.title, (), ())
