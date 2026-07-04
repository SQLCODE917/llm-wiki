"""Article lint domain contracts."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ArticleLintFinding:
    finding_id: str
    page_id: str
    severity: str
    finding_code: str
    message: str
    source_anchor: str = ""
    article_claim_id: str = ""
    support_ref: str = ""


@dataclass(frozen=True)
class ArticleAuthorityMetrics:
    page_id: str
    factual_sentence_count: int
    cited_factual_sentence_count: int
    uncited_factual_sentence_count: int
    unknown_support_ref_count: int
    authority_coverage_ratio: float


@dataclass(frozen=True)
class ArticleCoherenceMetrics:
    page_id: str
    clipped_sentence_count: int
    copied_phrase_finding_count: int
    unreadable_technical_evidence_count: int
    missing_related_preview_count: int


@dataclass(frozen=True)
class PublicationGate:
    page_id: str
    decision: str
    blocking_finding_ids: tuple[str, ...]


@dataclass(frozen=True)
class ArticleLintRun:
    article_lint_run_id: str
    article_lint_run_fingerprint: str
    page_id: str
    source_id: str
    page_body_hash: str
    findings: tuple[ArticleLintFinding, ...]
    authority_metrics: ArticleAuthorityMetrics
    coherence_metrics: ArticleCoherenceMetrics
    publication_gate: PublicationGate
