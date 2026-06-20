"""Deterministic PageBody validation for resolved contracts."""

from __future__ import annotations

import re
from collections import Counter

from llmwiki.domain.page_body_contracts import PageBodyFinding, ResolvedPageBodyContract

_WORD_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)?", re.IGNORECASE)
_BULLET_RE = re.compile(r"^\s*[-*]\s+\S+", re.MULTILINE)
_COPIED_NGRAM_SIZE = 8
_UNCERTAINTY_PATTERNS = {
    "may": r"\bmay\b",
    "might": r"\bmight\b",
    "possible": r"\bpossible\b|\bpossibly\b",
    "suggest": r"\bsuggest\w*\b",
    "uncertain": r"\buncertain\b",
    "unknown": r"\bunknown\b",
    "unconfirmed": r"\bunconfirmed\b",
    "verify": r"\[verify\]",
}


def validate_page_body(
    page_body: str,
    contract: ResolvedPageBodyContract,
    source_text: str = "",
) -> tuple[PageBodyFinding, ...]:
    findings: list[PageBodyFinding] = []
    findings.extend(_section_findings(page_body, contract))
    findings.extend(_markdown_shape_findings(page_body, contract))
    findings.extend(_grounding_findings(page_body, contract))
    findings.extend(_length_findings(page_body, source_text, contract))
    findings.extend(_copy_findings(page_body, source_text, contract))
    return tuple(findings)


def render_page_body_findings(
    findings: tuple[PageBodyFinding, ...],
    contract: ResolvedPageBodyContract,
) -> str:
    rendered = "\n".join(f"- {finding.finding_type}: {finding.detail}" for finding in findings)
    return (
        f"PageBody violates ResolvedPageBodyContract '{contract.contract_id}'.\n"
        f"{rendered}\n"
        "Replace the whole PlannedPageWrite PageBody and satisfy every finding.\n"
        "Do not append fixes to the rejected PageBody."
    )


def uncertainty_terms_in_text(text: str) -> tuple[str, ...]:
    lowered = text.lower()
    return tuple(
        term for term, pattern in _UNCERTAINTY_PATTERNS.items() if re.search(pattern, lowered)
    )


def _section_findings(
    page_body: str, contract: ResolvedPageBodyContract
) -> tuple[PageBodyFinding, ...]:
    normalized_body = page_body.lower()
    return tuple(
        PageBodyFinding("RequiredSections", f"missing section {section!r}")
        for section in contract.required_sections
        if section.lower() not in normalized_body
    )


def _markdown_shape_findings(
    page_body: str, contract: ResolvedPageBodyContract
) -> tuple[PageBodyFinding, ...]:
    if contract.required_markdown_shape != "claim-bullets":
        return ()
    bullet_count = len(_BULLET_RE.findall(page_body))
    min_bullets = contract.min_claim_bullets or 2
    if bullet_count >= min_bullets:
        return ()
    return (
        PageBodyFinding(
            "RequiredMarkdownShape",
            f"expected at least {min_bullets} markdown bullet claims",
        ),
    )


def _grounding_findings(
    page_body: str, contract: ResolvedPageBodyContract
) -> tuple[PageBodyFinding, ...]:
    findings: list[PageBodyFinding] = []
    for page_id in contract.required_link_page_ids:
        if f"[[{page_id}]]" not in page_body:
            findings.append(PageBodyFinding("RequiredLinkPageIds", f"missing [[{page_id}]]"))
    for citation in contract.required_source_citations:
        if citation not in page_body:
            findings.append(PageBodyFinding("RequiredSourceCitations", f"missing {citation}"))
    if contract.required_uncertainty_terms and not _preserves_uncertainty(
        page_body, contract.required_uncertainty_terms
    ):
        terms = ", ".join(contract.required_uncertainty_terms)
        findings.append(
            PageBodyFinding(
                "RequiredUncertaintyTerms",
                f"missing at least one source uncertainty term: {terms}",
            )
        )
    return tuple(findings)


def _length_findings(
    page_body: str,
    source_text: str,
    contract: ResolvedPageBodyContract,
) -> tuple[PageBodyFinding, ...]:
    page_words = len(_words(page_body))
    findings: list[PageBodyFinding] = []
    if contract.max_words and page_words > contract.max_words:
        findings.append(
            PageBodyFinding("MaxWords", f"{page_words} words exceeds {contract.max_words}")
        )
    source_words = len(_words(source_text))
    if (
        source_words >= contract.max_words > 0
        and contract.max_source_word_ratio
        and page_words / source_words > contract.max_source_word_ratio
    ):
        findings.append(
            PageBodyFinding(
                "MaxSourceWordRatio",
                f"{page_words}/{source_words} exceeds {contract.max_source_word_ratio:.2f}",
            )
        )
    return tuple(findings)


def _copy_findings(
    page_body: str,
    source_text: str,
    contract: ResolvedPageBodyContract,
) -> tuple[PageBodyFinding, ...]:
    if not source_text or contract.max_copied_ngram_ratio >= 1.0:
        return ()
    source_ngrams = set(_ngrams(_words(source_text), _COPIED_NGRAM_SIZE))
    body_ngrams = _ngrams(_words(page_body), _COPIED_NGRAM_SIZE)
    if not source_ngrams or not body_ngrams:
        return ()
    copied = sum(count for ngram, count in Counter(body_ngrams).items() if ngram in source_ngrams)
    ratio = copied / len(body_ngrams)
    if ratio <= contract.max_copied_ngram_ratio:
        return ()
    return (
        PageBodyFinding(
            "MaxCopiedNGramRatio",
            f"{ratio:.2f} exceeds {contract.max_copied_ngram_ratio:.2f}",
        ),
    )


def _preserves_uncertainty(page_body: str, terms: tuple[str, ...]) -> bool:
    lowered = page_body.lower()
    return any(
        re.search(_UNCERTAINTY_PATTERNS.get(term, rf"\b{re.escape(term)}\b"), lowered)
        for term in terms
    )


def _words(text: str) -> tuple[str, ...]:
    return tuple(match.group(0).lower() for match in _WORD_RE.finditer(text))


def _ngrams(words: tuple[str, ...], size: int) -> tuple[tuple[str, ...], ...]:
    if len(words) < size:
        return ()
    return tuple(tuple(words[index : index + size]) for index in range(len(words) - size + 1))
