"""Validation for structured synthesized page drafts."""

from __future__ import annotations

import re
from collections import Counter

from llmwiki.domain.ledger.page_synthesis import (
    DraftValidationResult,
    PageDraft,
    PageSynthesisFinding,
    PageSynthesisPlan,
)
from llmwiki.domain.ledger.page_synthesis_text import block_texts, factual_sentences, ngrams, words
from llmwiki.domain.ledger.page_synthesis_text_validation import (
    clipped_fragment_findings,
    navigation_text_findings,
)
from llmwiki.domain.ledger.page_title_lint import is_weak_topic_identity

_COPIED_NGRAM_SIZE = 8
_MAX_COPIED_NGRAM_RATIO = 0.50
_PLACEHOLDER_PATTERNS = (
    re.compile(r"\.\.\.(?![A-Za-z_$])"),
    re.compile(r"\[[^\]]*(?:todo|tbd|placeholder|truncated)[^\]]*]", re.IGNORECASE),
    re.compile(r"\b(?:todo|tbd|placeholder|lorem ipsum)\b", re.IGNORECASE),
)


def validate_page_draft(plan: PageSynthesisPlan, draft: PageDraft) -> DraftValidationResult:
    findings: list[PageSynthesisFinding] = []
    findings.extend(_identity_findings(plan, draft))
    findings.extend(_empty_draft_findings(plan, draft))
    findings.extend(_weak_topic_findings(plan))
    findings.extend(_placeholder_findings(plan, draft))
    findings.extend(_claim_support_findings(plan, draft))
    findings.extend(_sentence_coverage_findings(plan, draft))
    findings.extend(navigation_text_findings(plan, draft))
    findings.extend(clipped_fragment_findings(plan, draft))
    findings.extend(_copied_phrase_findings(plan, draft))
    return DraftValidationResult(
        accepted=not any(finding.severity == "blocking" for finding in findings),
        findings=tuple(findings),
    )


def _empty_draft_findings(
    plan: PageSynthesisPlan, draft: PageDraft
) -> tuple[PageSynthesisFinding, ...]:
    findings: list[PageSynthesisFinding] = []
    if not plan.evidence_set.items:
        findings.append(_finding(plan, "no-selected-evidence", "plan has no selected evidence"))
    if not draft.blocks or not draft.claims:
        findings.append(_finding(plan, "empty-draft", "draft has no factual prose claims"))
    return tuple(findings)


def _identity_findings(
    plan: PageSynthesisPlan, draft: PageDraft
) -> tuple[PageSynthesisFinding, ...]:
    findings: list[PageSynthesisFinding] = []
    if draft.page_id != plan.page_id:
        findings.append(
            _finding(plan, "draft-page-id-mismatch", f"draft page_id {draft.page_id!r}")
        )
    if draft.title.strip() != plan.title.strip():
        findings.append(_finding(plan, "draft-title-mismatch", f"draft title {draft.title!r}"))
    return tuple(findings)


def _weak_topic_findings(plan: PageSynthesisPlan) -> tuple[PageSynthesisFinding, ...]:
    if plan.page_family not in {"topic-concept", "broad-topic"}:
        return ()
    if not is_weak_topic_identity(plan.title) and not is_weak_topic_identity(plan.page_id):
        return ()
    return (
        _finding(
            plan,
            "weak-topic-identity",
            f"topic label {plan.title!r} is malformed or too weak for synthesis",
        ),
    )


def _placeholder_findings(
    plan: PageSynthesisPlan, draft: PageDraft
) -> tuple[PageSynthesisFinding, ...]:
    findings: list[PageSynthesisFinding] = []
    for block in draft.blocks:
        for text in block_texts(block):
            if "…" in text or any(pattern.search(text) for pattern in _PLACEHOLDER_PATTERNS):
                findings.append(
                    _finding(
                        plan,
                        "placeholder-text",
                        "draft contains placeholder or truncation text",
                        block_id=block.block_id,
                    )
                )
    return tuple(findings)


def _claim_support_findings(
    plan: PageSynthesisPlan, draft: PageDraft
) -> tuple[PageSynthesisFinding, ...]:
    selected = plan.selected_support_codes
    findings: list[PageSynthesisFinding] = []
    for claim in draft.claims:
        if not claim.support_refs:
            findings.append(
                _finding(
                    plan,
                    "missing-support-ref",
                    "draft claim has no support refs",
                    claim_id=claim.claim_id,
                )
            )
        for support_ref in claim.support_refs:
            if support_ref.code not in selected:
                findings.append(
                    _finding(
                        plan,
                        "unknown-support-ref",
                        "draft claim references support outside PageSynthesisPlan",
                        claim_id=claim.claim_id,
                        support_ref=support_ref.code,
                    )
                )
    return tuple(findings)


def _sentence_coverage_findings(
    plan: PageSynthesisPlan, draft: PageDraft
) -> tuple[PageSynthesisFinding, ...]:
    claimed = {_normalize_sentence(claim.sentence): claim for claim in draft.claims}
    findings: list[PageSynthesisFinding] = []
    for block in draft.blocks:
        for sentence in factual_sentences(block):
            if _normalize_sentence(sentence) not in claimed:
                findings.append(
                    _finding(
                        plan,
                        "unmapped-factual-sentence",
                        f"sentence has no DraftClaim: {sentence}",
                        block_id=block.block_id,
                    )
                )
    return tuple(findings)


def _copied_phrase_findings(
    plan: PageSynthesisPlan, draft: PageDraft
) -> tuple[PageSynthesisFinding, ...]:
    source_text = " ".join(
        item.evidence_text for item in plan.evidence_set.items if item.evidence_text
    )
    source_ngrams = set(ngrams(tuple(words(source_text)), _COPIED_NGRAM_SIZE))
    if not source_ngrams:
        return ()
    draft_text = " ".join(text for block in draft.blocks for text in block_texts(block))
    draft_words = tuple(words(draft_text))
    draft_ngrams = ngrams(draft_words, _COPIED_NGRAM_SIZE)
    if not draft_ngrams:
        return ()
    copied = sum(count for ngram, count in Counter(draft_ngrams).items() if ngram in source_ngrams)
    ratio = copied / len(draft_ngrams)
    if ratio <= _MAX_COPIED_NGRAM_RATIO:
        return ()
    return (
        _finding(
            plan,
            "copied-source-phrases",
            f"copied 8-gram ratio {ratio:.2f} exceeds {_MAX_COPIED_NGRAM_RATIO:.2f}",
        ),
    )


def _normalize_sentence(text: str) -> str:
    return " ".join(text.split()).strip()


def _finding(
    plan: PageSynthesisPlan,
    finding_type: str,
    message: str,
    *,
    claim_id: str = "",
    support_ref: str = "",
    block_id: str = "",
) -> PageSynthesisFinding:
    return PageSynthesisFinding(
        severity="blocking",
        finding_type=finding_type,
        page_id=plan.page_id,
        message=message,
        claim_id=claim_id,
        support_ref=support_ref,
        block_id=block_id,
    )
