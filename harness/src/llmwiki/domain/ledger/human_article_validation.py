"""Validation for evidence-pack-backed human articles."""

from __future__ import annotations

import re

from llmwiki.domain.ledger.article_evidence_coverage import uncovered_required_evidence
from llmwiki.domain.ledger.evidence_pack import EvidencePack
from llmwiki.domain.ledger.human_article import (
    ArticleBlock,
    ArticleFinding,
    ArticleValidationResult,
    HumanArticle,
)
from llmwiki.domain.ledger.human_article_quality import (
    clipped_fragment_findings,
    copied_phrase_findings,
)
from llmwiki.domain.ledger.page_synthesis_text import canonical_text, split_sentences
from llmwiki.domain.ledger.page_title_lint import is_weak_topic_identity

_PLACEHOLDER_PATTERNS = (
    re.compile(r"\.\.\.(?![A-Za-z_$])"),
    re.compile(r"\[[^\]]*(?:todo|tbd|placeholder|truncated)[^\]]*]", re.IGNORECASE),
    re.compile(r"\b(?:todo|tbd|placeholder|lorem ipsum)\b", re.IGNORECASE),
)
_MARKDOWN_HEAD_RE = re.compile(r"^\s{0,3}#{1,6}\s+\S", re.MULTILINE)


def validate_human_article(
    pack: EvidencePack, article: HumanArticle
) -> ArticleValidationResult:
    findings: list[ArticleFinding] = []
    findings.extend(_identity_findings(pack, article))
    findings.extend(_empty_findings(pack, article))
    findings.extend(_weak_topic_findings(pack))
    findings.extend(_claim_support_findings(pack, article))
    findings.extend(_evidence_coverage_findings(pack, article))
    findings.extend(_sentence_coverage_findings(pack, article))
    findings.extend(_claim_rendering_findings(pack, article))
    findings.extend(_claim_mapping_findings(pack, article))
    findings.extend(_placeholder_findings(pack, article))
    findings.extend(_raw_markdown_findings(pack, article))
    findings.extend(_navigation_text_findings(pack, article))
    findings.extend(clipped_fragment_findings(pack, article))
    findings.extend(copied_phrase_findings(pack, article))
    return ArticleValidationResult(
        accepted=not any(finding.severity == "blocking" for finding in findings),
        findings=tuple(findings),
    )


def article_block_texts(block: ArticleBlock) -> tuple[str, ...]:
    if block.block_kind == "table":
        return tuple(cell for row in block.table_rows for cell in row)
    if block.items:
        return block.items
    if block.text:
        return (block.text,)
    return ()


def article_factual_sentences(block: ArticleBlock) -> tuple[str, ...]:
    if block.block_kind not in {"paragraph", "bullet-list", "numbered-list", "ordered-list"}:
        return ()
    return tuple(
        sentence
        for text in article_block_texts(block)
        for sentence in split_sentences(text)
        if sentence.strip()
    )


def _identity_findings(pack: EvidencePack, article: HumanArticle) -> tuple[ArticleFinding, ...]:
    findings: list[ArticleFinding] = []
    if article.page_id != pack.page_id:
        findings.append(_finding(pack, "article-page-id-mismatch", article.page_id))
    if article.title.strip() != pack.title.strip():
        findings.append(_finding(pack, "article-title-mismatch", article.title))
    return tuple(findings)


def _empty_findings(pack: EvidencePack, article: HumanArticle) -> tuple[ArticleFinding, ...]:
    findings: list[ArticleFinding] = []
    if not pack.items:
        findings.append(_finding(pack, "no-evidence-pack-items", "evidence pack is empty"))
    if not article.sections or not article.claims:
        findings.append(_finding(pack, "empty-article", "article has no sections or claims"))
    return tuple(findings)


def _weak_topic_findings(pack: EvidencePack) -> tuple[ArticleFinding, ...]:
    if pack.page_family not in {"topic-concept", "broad-topic"}:
        return ()
    if not is_weak_topic_identity(pack.title) and not is_weak_topic_identity(pack.page_id):
        return ()
    return (
        _finding(
            pack,
            "weak-topic-identity",
            f"topic label {pack.title!r} is malformed or too weak for publication",
        ),
    )


def _claim_support_findings(
    pack: EvidencePack, article: HumanArticle
) -> tuple[ArticleFinding, ...]:
    selected = pack.support_ref_codes
    findings: list[ArticleFinding] = []
    for claim in article.claims:
        if not claim.support_refs:
            findings.append(
                _finding(pack, "missing-support-ref", "article claim has no support refs", claim)
            )
        for support_ref in claim.support_refs:
            if support_ref.code not in selected:
                findings.append(
                    _finding(
                        pack,
                        "unknown-support-ref",
                        "article claim references support outside EvidencePack",
                        claim,
                        support_ref.code,
                    )
                )
    return tuple(findings)


def _evidence_coverage_findings(
    pack: EvidencePack, article: HumanArticle
) -> tuple[ArticleFinding, ...]:
    findings: list[ArticleFinding] = []
    for requirement in uncovered_required_evidence(pack, article):
        refs = tuple(ref.code for ref in requirement.support_refs)
        refs_text = ", ".join(refs)
        findings.append(
            _finding(
                pack,
                "uncovered-required-evidence",
                "article omits required evidence "
                f"{requirement.requirement_id}: {refs_text}",
                support_ref=refs_text,
            )
        )
    return tuple(findings)


def _sentence_coverage_findings(
    pack: EvidencePack, article: HumanArticle
) -> tuple[ArticleFinding, ...]:
    claimed = {_normalize(claim.sentence): claim for claim in article.claims}
    findings: list[ArticleFinding] = []
    for section in article.sections:
        for block in section.blocks:
            for sentence in article_factual_sentences(block):
                if _normalize(sentence) not in claimed:
                    findings.append(
                        _finding(
                            pack,
                            "unmapped-factual-sentence",
                            f"sentence has no ArticleClaim: {sentence}",
                            block_id=block.block_id,
                            section_id=section.section_id,
                        )
                    )
    return tuple(findings)


def _claim_rendering_findings(
    pack: EvidencePack, article: HumanArticle
) -> tuple[ArticleFinding, ...]:
    rendered = {
        _normalize(sentence)
        for section in article.sections
        for block in section.blocks
        for sentence in article_factual_sentences(block)
    }
    findings: list[ArticleFinding] = []
    for claim in article.claims:
        if _normalize(claim.sentence) not in rendered:
            findings.append(
                _finding(
                    pack,
                    "unrendered-article-claim",
                    f"article claim does not appear in article prose: {claim.sentence}",
                    claim,
                )
            )
    return tuple(findings)


def _claim_mapping_findings(
    pack: EvidencePack, article: HumanArticle
) -> tuple[ArticleFinding, ...]:
    claim_ids = {claim.claim_id for claim in article.claims}
    mapped_ids = {
        claim_id
        for section in article.sections
        for claim_id in section.article_claim_ids
    }
    findings: list[ArticleFinding] = []
    for claim in article.claims:
        if claim.claim_id not in mapped_ids:
            findings.append(
                _finding(
                    pack,
                    "unmapped-article-claim",
                    "article claim is not listed in any ArticleSection.article_claim_ids",
                    claim,
                )
            )
    for section in article.sections:
        for claim_id in section.article_claim_ids:
            if claim_id not in claim_ids:
                findings.append(
                    ArticleFinding(
                        "blocking",
                        "unknown-section-claim-id",
                        pack.page_id,
                        f"section references unknown article claim id: {claim_id}",
                        claim_id,
                        "",
                        "",
                        section.section_id,
                    )
                )
    return tuple(findings)


def _placeholder_findings(pack: EvidencePack, article: HumanArticle) -> tuple[ArticleFinding, ...]:
    findings: list[ArticleFinding] = []
    for block in _blocks(article):
        for text in article_block_texts(block):
            if "…" in text or any(pattern.search(text) for pattern in _PLACEHOLDER_PATTERNS):
                findings.append(
                    _finding(
                        pack,
                        "placeholder-text",
                        "article contains placeholder or truncation text",
                        block_id=block.block_id,
                    )
                )
    return tuple(findings)


def _raw_markdown_findings(pack: EvidencePack, article: HumanArticle) -> tuple[ArticleFinding, ...]:
    findings: list[ArticleFinding] = []
    for block in _blocks(article):
        for text in article_block_texts(block):
            stripped = text.strip()
            if stripped == "---" or _MARKDOWN_HEAD_RE.search(text):
                findings.append(
                    _finding(
                        pack,
                        "raw-markdown-prose",
                        "article blocks must not contain model-authored markdown structure",
                        block_id=block.block_id,
                    )
                )
    return tuple(findings)


def _navigation_text_findings(
    pack: EvidencePack, article: HumanArticle
) -> tuple[ArticleFinding, ...]:
    blocked = tuple(
        canonical_text(link.preview_text)
        for link in article.related_links
        if canonical_text(link.preview_text)
    )
    if not blocked:
        return ()
    findings: list[ArticleFinding] = []
    for block in _blocks(article):
        for sentence in article_factual_sentences(block):
            normalized = canonical_text(sentence)
            if normalized in blocked:
                findings.append(
                    _finding(
                        pack,
                        "navigation-summary-prose",
                        "article reuses navigation preview text as factual prose",
                        block_id=block.block_id,
                    )
                )
    return tuple(findings)


def _blocks(article: HumanArticle) -> tuple[ArticleBlock, ...]:
    return tuple(block for section in article.sections for block in section.blocks)


def _normalize(text: str) -> str:
    return " ".join(text.split()).strip()


def _finding(
    pack: EvidencePack,
    finding_type: str,
    message: str,
    claim: object | None = None,
    support_ref: str = "",
    *,
    block_id: str = "",
    section_id: str = "",
) -> ArticleFinding:
    claim_id = getattr(claim, "claim_id", "")
    return ArticleFinding(
        "blocking",
        finding_type,
        pack.page_id,
        message,
        claim_id,
        support_ref,
        block_id,
        section_id,
    )
