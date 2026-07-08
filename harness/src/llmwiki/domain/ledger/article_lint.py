"""Deterministic lint and publication gates for rendered human articles."""

from __future__ import annotations

import re
from dataclasses import replace

from llmwiki.domain.ledger.article_evidence_coverage import (
    article_evidence_coverage_metrics,
)
from llmwiki.domain.ledger.article_lint_contracts import (
    ArticleAuthorityMetrics,
    ArticleCoherenceMetrics,
    ArticleLintFinding,
    ArticleLintRun,
    PublicationGate,
)
from llmwiki.domain.ledger.canonical import artifact_fingerprint, deterministic_id
from llmwiki.domain.ledger.coverage import RenderedPage
from llmwiki.domain.ledger.evidence_pack import EvidencePack
from llmwiki.domain.ledger.human_article import ArticleClaim, ArticleFinding, HumanArticle
from llmwiki.domain.ledger.human_article_validation import (
    article_factual_sentences,
    validate_human_article,
)
from llmwiki.domain.ledger.page_title_lint import PageTitleFinding

_INLINE_CITATION_RE = re.compile(r"_\(([^)]*)\)_")
_SUPPORT_ID_RE = re.compile(
    r"\b(?:atom|typed-evidence-record|ledger|anchor|evidence-block):[a-z0-9-]+"
)


def lint_human_article(
    *,
    article: HumanArticle,
    rendered: RenderedPage,
    pack: EvidencePack,
    title_findings: tuple[PageTitleFinding, ...] = (),
) -> ArticleLintRun:
    findings: list[ArticleLintFinding] = []
    findings.extend(_validation_findings(pack, article))
    findings.extend(_title_findings(pack, title_findings))
    findings.extend(_rendered_citation_findings(pack, article, rendered))
    findings.extend(_technical_readability_findings(pack, rendered))
    findings.extend(_related_link_findings(pack, article))
    authority = _authority_metrics(pack, article, rendered, findings)
    coherence = _coherence_metrics(pack, findings)
    evidence_coverage = article_evidence_coverage_metrics(pack, article)
    blocking_ids = tuple(f.finding_id for f in findings if f.severity == "blocking")
    gate = PublicationGate(
        page_id=pack.page_id,
        decision="blocked" if blocking_ids else "accepted",
        blocking_finding_ids=blocking_ids,
    )
    draft = ArticleLintRun(
        article_lint_run_id=deterministic_id("article-lint-run", pack.source_hash, pack.page_id),
        article_lint_run_fingerprint="",
        page_id=pack.page_id,
        source_id=pack.source_id,
        page_body_hash=rendered.page_body_hash,
        findings=tuple(findings),
        authority_metrics=authority,
        coherence_metrics=coherence,
        evidence_coverage_metrics=evidence_coverage,
        publication_gate=gate,
    )
    fingerprint = artifact_fingerprint(draft, exclude=("article_lint_run_fingerprint",))
    return replace(draft, article_lint_run_fingerprint=fingerprint)


def _validation_findings(
    pack: EvidencePack, article: HumanArticle
) -> tuple[ArticleLintFinding, ...]:
    return tuple(
        _from_article_finding(pack, finding)
        for finding in validate_human_article(pack, article).findings
    )


def _title_findings(
    pack: EvidencePack, title_findings: tuple[PageTitleFinding, ...]
) -> tuple[ArticleLintFinding, ...]:
    return tuple(
        _finding(pack, "title-lint-failed", finding.message, severity=finding.severity)
        for finding in title_findings
    )


def _rendered_citation_findings(
    pack: EvidencePack, article: HumanArticle, rendered: RenderedPage
) -> tuple[ArticleLintFinding, ...]:
    findings: list[ArticleLintFinding] = []
    known_labels = {item.citation_label for item in pack.items if item.citation_label}
    for label in _inline_citation_labels(rendered.page_body):
        if label and label not in known_labels:
            findings.append(
                _finding(
                    pack,
                    "unknown-citation-label",
                    f"citation {label!r} is not in the evidence pack",
                )
            )
    for claim in article.claims:
        missing = tuple(
            label
            for label in _claim_citation_labels(pack, claim)
            if label not in rendered.page_body
        )
        if missing:
            findings.append(
                _finding(
                    pack,
                    "missing-claim-citation",
                    "rendered markdown omits citation labels: " + ", ".join(missing),
                    claim_id=claim.claim_id,
                )
            )
    return tuple(findings)


def _technical_readability_findings(
    pack: EvidencePack, rendered: RenderedPage
) -> tuple[ArticleLintFinding, ...]:
    technical_items = tuple(
        item
        for item in pack.items
        if item.evidence_record_type in {"code_example", "formula", "table_fact"}
    )
    if not technical_items:
        return ()
    findings: list[ArticleLintFinding] = []
    for item in technical_items:
        if item.payload_text.strip() and item.payload_text.strip() in rendered.page_body:
            continue
        if _SUPPORT_ID_RE.search(rendered.page_body):
            findings.append(
                _finding(
                    pack,
                    "unreadable-technical-evidence",
                    "rendered technical evidence exposes ids without readable payload context",
                    support_ref=item.support_ref.code,
                )
            )
    return tuple(findings)


def _related_link_findings(
    pack: EvidencePack, article: HumanArticle
) -> tuple[ArticleLintFinding, ...]:
    selected = pack.support_ref_codes
    findings: list[ArticleLintFinding] = []
    for link in article.related_links:
        if not link.preview_text.strip():
            findings.append(
                _finding(
                    pack,
                    "missing-related-link-preview",
                    f"related link {link.page_id!r} has no preview",
                )
            )
        for support_ref in link.shared_support_refs:
            if support_ref.code not in selected:
                findings.append(
                    _finding(
                        pack,
                        "unknown-related-link-support-ref",
                        "related link references support outside EvidencePack",
                        support_ref=support_ref.code,
                    )
                )
    return tuple(findings)


def _authority_metrics(
    pack: EvidencePack,
    article: HumanArticle,
    rendered: RenderedPage,
    findings: list[ArticleLintFinding],
) -> ArticleAuthorityMetrics:
    factual = _factual_sentences(article)
    cited = sum(
        1 for sentence in factual if _sentence_has_citation(article, pack, rendered, sentence)
    )
    unknown = sum(1 for finding in findings if finding.finding_code == "unknown-support-ref")
    ratio = cited / len(factual) if factual else 0.0
    return ArticleAuthorityMetrics(
        pack.page_id,
        len(factual),
        cited,
        len(factual) - cited,
        unknown,
        ratio,
    )


def _coherence_metrics(
    pack: EvidencePack, findings: list[ArticleLintFinding]
) -> ArticleCoherenceMetrics:
    return ArticleCoherenceMetrics(
        pack.page_id,
        sum(1 for f in findings if f.finding_code == "clipped-evidence-fragment"),
        sum(1 for f in findings if f.finding_code == "copied-source-phrases"),
        sum(1 for f in findings if f.finding_code == "unreadable-technical-evidence"),
        sum(1 for f in findings if f.finding_code == "missing-related-link-preview"),
    )


def _factual_sentences(article: HumanArticle) -> tuple[str, ...]:
    return tuple(
        sentence
        for section in article.sections
        for block in section.blocks
        for sentence in article_factual_sentences(block)
    )


def _sentence_has_citation(
    article: HumanArticle, pack: EvidencePack, rendered: RenderedPage, sentence: str
) -> bool:
    claim = next(
        (
            claim
            for claim in article.claims
            if _normalize(claim.sentence) == _normalize(sentence)
        ),
        None,
    )
    if claim is None:
        return False
    labels = _claim_citation_labels(pack, claim)
    return bool(labels) and all(label in rendered.page_body for label in labels)


def _claim_citation_labels(pack: EvidencePack, claim: ArticleClaim) -> tuple[str, ...]:
    items = {item.support_ref.code: item for item in pack.items}
    return tuple(
        item.citation_label
        for support_ref in claim.support_refs
        if (item := items.get(support_ref.code)) is not None and item.citation_label
    )


def _inline_citation_labels(body: str) -> tuple[str, ...]:
    labels: list[str] = []
    for match in _INLINE_CITATION_RE.finditer(body):
        labels.extend(
            part.strip()
            for part in match.group(1).split(";")
            if part.strip() and not part.strip().startswith("shared support:")
        )
    return tuple(labels)


def _from_article_finding(pack: EvidencePack, finding: ArticleFinding) -> ArticleLintFinding:
    return _finding(
        pack,
        finding.finding_type,
        finding.message,
        severity=finding.severity,
        claim_id=finding.claim_id,
        support_ref=finding.support_ref,
    )


def _finding(
    pack: EvidencePack,
    finding_code: str,
    message: str,
    *,
    severity: str = "blocking",
    claim_id: str = "",
    support_ref: str = "",
    source_anchor: str = "",
) -> ArticleLintFinding:
    finding_id = deterministic_id(
        "article-lint-finding",
        pack.source_hash,
        pack.page_id,
        finding_code,
        message,
        claim_id,
        support_ref,
    )
    return ArticleLintFinding(
        finding_id,
        pack.page_id,
        severity,
        finding_code,
        message,
        source_anchor,
        claim_id,
        support_ref,
    )


def _normalize(text: str) -> str:
    return " ".join(text.split()).strip()
