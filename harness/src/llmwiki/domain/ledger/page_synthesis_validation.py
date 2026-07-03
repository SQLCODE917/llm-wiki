"""Validation for structured synthesized page drafts."""

from __future__ import annotations

import re
from collections import Counter

from llmwiki.domain.ledger.page_synthesis import (
    DraftBlock,
    DraftValidationResult,
    PageDraft,
    PageSynthesisFinding,
    PageSynthesisPlan,
)

_WORD_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)?", re.IGNORECASE)
_SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s+")
_COPIED_NGRAM_SIZE = 8
_MAX_COPIED_NGRAM_RATIO = 0.50
_MALFORMED_TOPIC_LABELS = frozenset({"alway", "bonuse"})
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
    findings.extend(_copied_phrase_findings(plan, draft))
    return DraftValidationResult(
        accepted=not any(finding.severity == "blocking" for finding in findings),
        findings=tuple(findings),
    )


def _empty_draft_findings(
    plan: PageSynthesisPlan, draft: PageDraft
) -> tuple[PageSynthesisFinding, ...]:
    findings: list[PageSynthesisFinding] = []
    if not plan.selected_evidence:
        findings.append(_finding(plan, "no-selected-evidence", "plan has no selected evidence"))
    if not draft.blocks or not draft.claims:
        findings.append(_finding(plan, "empty-draft", "draft has no factual prose claims"))
    return tuple(findings)


def is_weak_topic_identity(label: str) -> bool:
    tokens = tuple(part for token in _words(label) for part in token.split("-") if part)
    if not tokens:
        return True
    return any(token in _MALFORMED_TOPIC_LABELS for token in tokens)


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
        for text in _block_texts(block):
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
        for sentence in _factual_sentences(block):
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
    source_text = " ".join(card.exact_text for card in plan.selected_evidence if card.exact_text)
    source_ngrams = set(_ngrams(tuple(_words(source_text)), _COPIED_NGRAM_SIZE))
    if not source_ngrams:
        return ()
    draft_text = " ".join(text for block in draft.blocks for text in _block_texts(block))
    draft_words = tuple(_words(draft_text))
    draft_ngrams = _ngrams(draft_words, _COPIED_NGRAM_SIZE)
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


def _factual_sentences(block: DraftBlock) -> tuple[str, ...]:
    if block.block_kind not in {"paragraph", "bullet-list", "numbered-list"}:
        return ()
    return tuple(
        sentence
        for text in _block_texts(block)
        for sentence in _split_sentences(text)
        if sentence.strip()
    )


def _block_texts(block: DraftBlock) -> tuple[str, ...]:
    if block.block_kind == "table":
        return tuple(cell for row in block.table_rows for cell in row)
    if block.items:
        return block.items
    if block.text:
        return (block.text,)
    return ()


def _split_sentences(text: str) -> tuple[str, ...]:
    cleaned = " ".join(text.split()).strip()
    if not cleaned:
        return ()
    sentences = tuple(part.strip() for part in _SENTENCE_END_RE.split(cleaned) if part.strip())
    return sentences or (cleaned,)


def _normalize_sentence(text: str) -> str:
    return " ".join(text.split()).strip()


def _words(text: str) -> tuple[str, ...]:
    return tuple(match.group(0).lower() for match in _WORD_RE.finditer(text))


def _ngrams(words: tuple[str, ...], size: int) -> tuple[tuple[str, ...], ...]:
    if len(words) < size:
        return ()
    return tuple(tuple(words[index : index + size]) for index in range(len(words) - size + 1))


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
