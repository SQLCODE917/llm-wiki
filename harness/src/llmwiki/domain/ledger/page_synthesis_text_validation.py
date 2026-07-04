"""Lossy-summary and clipped-fragment checks for page synthesis drafts."""

from __future__ import annotations

from llmwiki.domain.ledger.page_synthesis import (
    PageDraft,
    PageSynthesisFinding,
    PageSynthesisPlan,
)
from llmwiki.domain.ledger.page_synthesis_text import canonical_text, factual_sentences, words


def navigation_text_findings(
    plan: PageSynthesisPlan, draft: PageDraft
) -> tuple[PageSynthesisFinding, ...]:
    blocked_texts = tuple(
        (summary.summary_kind, summary.summary_text)
        for summary in plan.evidence_set.navigation_summaries
        if summary.summary_text.strip()
    ) + tuple(
        ("prompt-context-digest", digest.digest_text)
        for digest in plan.evidence_set.prompt_context_digests
        if digest.digest_text.strip()
    )
    if not blocked_texts:
        return ()
    findings: list[PageSynthesisFinding] = []
    normalized_blocked = tuple(
        (kind, canonical_text(text)) for kind, text in blocked_texts if canonical_text(text)
    )
    for block in draft.blocks:
        for sentence in factual_sentences(block):
            normalized_sentence = canonical_text(sentence)
            for kind, blocked in normalized_blocked:
                if normalized_sentence == blocked or (
                    len(normalized_sentence) >= 24 and normalized_sentence in blocked
                ):
                    findings.append(
                        _finding(
                            plan,
                            "navigation-summary-prose"
                            if kind != "prompt-context-digest"
                            else "prompt-context-digest-prose",
                            f"draft reuses non-renderable {kind} text",
                            block_id=block.block_id,
                        )
                    )
                    break
    return tuple(findings)


def clipped_fragment_findings(
    plan: PageSynthesisPlan, draft: PageDraft
) -> tuple[PageSynthesisFinding, ...]:
    items_by_ref = {item.support_ref.code: item for item in plan.evidence_set.items}
    findings: list[PageSynthesisFinding] = []
    for claim in draft.claims:
        claim_words = words(claim.sentence)
        if len(claim_words) < 5:
            continue
        for support_ref in claim.support_refs:
            item = items_by_ref.get(support_ref.code)
            if item is None:
                continue
            source_words = words(item.evidence_text)
            if _looks_like_clipped_fragment(claim_words, source_words):
                findings.append(
                    _finding(
                        plan,
                        "clipped-evidence-fragment",
                        "draft claim appears to be a clipped source fragment",
                        claim_id=claim.claim_id,
                        support_ref=support_ref.code,
                    )
                )
                break
    return tuple(findings)


def _looks_like_clipped_fragment(
    claim_words: tuple[str, ...], source_words: tuple[str, ...]
) -> bool:
    if len(source_words) <= len(claim_words) + 2:
        return False
    if claim_words == source_words[: len(claim_words)]:
        return True
    return _is_ordered_subsequence(claim_words, source_words) and (
        len(source_words) - len(claim_words) >= 3
    )


def _is_ordered_subsequence(needle: tuple[str, ...], haystack: tuple[str, ...]) -> bool:
    if not needle:
        return False
    index = 0
    for word in haystack:
        if word == needle[index]:
            index += 1
            if index == len(needle):
                return True
    return False


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
