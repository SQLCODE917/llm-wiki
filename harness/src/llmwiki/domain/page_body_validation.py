"""Deterministic PageBody validation for resolved contracts."""

from __future__ import annotations

import re
from collections import Counter

from llmwiki.domain.page_body_contracts import PageBodyFinding, ResolvedPageBodyContract
from llmwiki.domain.source_claim_quality import SOURCE_FRAMING_PREFIXES
from llmwiki.domain.source_summary import (
    SourceSummaryDraft,
    SourceSummaryPlan,
    render_missing_source_summary_claims,
)
from llmwiki.domain.source_summary_citations import (
    normalized_citation_text,
    source_summary_bullet_cites_required_locator,
)

_WORD_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)?", re.IGNORECASE)
_BULLET_RE = re.compile(r"^\s*[-*]\s+\S+", re.MULTILINE)
_RAW_CITATION_TEXT_RE = re.compile(r"\(?raw/[^\n)\]]+\)?")
_COPIED_NGRAM_SIZE = 8
_UNCERTAINTY_PATTERNS = {
    "may": r"\bmay\b",
    "might": r"\bmight\b",
    "possible": r"\bpossible\b|\bpossibly\b",
    "suggest": r"\bsuggest\w*\b",
    "uncertain": r"\buncertain\b",
    "unknown": r"\bunknown\b",
    "unconfirmed": r"\bunconfirmed\b",
    "does not specify": r"\bdoes not\b.+\bspecify\b",
    "does not confirm": r"\bdoes not\b.+\bconfirm\b",
    "does not state": r"\bdoes not\b.+\bstate\b",
    "not specified": r"\bnot\b.+\bspecified\b",
    "not confirmed": r"\bnot\b.+\bconfirmed\b",
    "verify": r"\[verify\]",
}


def validate_page_body(
    page_body: str,
    contract: ResolvedPageBodyContract,
    source_text: str = "",
) -> tuple[PageBodyFinding, ...]:
    findings: list[PageBodyFinding] = []
    findings.extend(_placeholder_findings(page_body))
    findings.extend(_section_findings(page_body, contract))
    findings.extend(_markdown_shape_findings(page_body, contract))
    findings.extend(_grounding_findings(page_body, contract))
    findings.extend(_length_findings(page_body, source_text, contract))
    findings.extend(_copy_findings(page_body, source_text, contract))
    return tuple(findings)


def render_source_summary_draft(draft: SourceSummaryDraft) -> str:
    bullets = "\n".join(f"- {bullet.bullet_text.strip()}" for bullet in draft.claim_bullets)
    return (
        "## Source record\n\n"
        f"{draft.source_record_text.strip()}\n\n"
        "## Key supported claims\n\n"
        f"{bullets}"
    )


def validate_source_summary_draft(
    draft: SourceSummaryDraft,
    plan: SourceSummaryPlan,
    source_text: str = "",
) -> tuple[PageBodyFinding, ...]:
    findings: list[PageBodyFinding] = []
    covered_claims = tuple(
        claim_id for bullet in draft.claim_bullets for claim_id in bullet.covered_source_claims
    )
    selected_claims = set(plan.selected_source_claims)
    missing_claims = tuple(
        claim_id for claim_id in plan.selected_source_claims if claim_id not in covered_claims
    )
    unknown_claims = tuple(
        claim_id for claim_id in covered_claims if claim_id not in selected_claims
    )
    if missing_claims:
        findings.append(
            PageBodyFinding(
                "SelectedSourceClaims",
                "missing coverage for "
                + render_missing_source_summary_claims(plan, missing_claims),
            )
        )
    if unknown_claims:
        findings.append(
            PageBodyFinding(
                "SelectedSourceClaims",
                "covers claims outside SourceSummaryPlan: " + ", ".join(unknown_claims),
            )
        )
    findings.extend(_source_framing_bullet_findings(draft))
    findings.extend(_source_summary_bullet_citation_findings(draft, plan))
    findings.extend(_source_claim_id_findings(draft, plan))
    findings.extend(_draft_copy_findings(draft, source_text))
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
        "Do not append fixes to the rejected PageBody.\n"
        "For source-summary, write a short paraphrase with the required sections, "
        "enough claim bullets, and coverage of the selected source claims. "
        "Start bullets with the subject or finding, not with source-framing phrases "
        "such as 'The source discusses'. Keep bullets short enough to avoid copied phrases."
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


def _placeholder_findings(page_body: str) -> tuple[PageBodyFinding, ...]:
    if "…" not in page_body and not _contains_placeholder_ascii_ellipsis(page_body):
        return ()
    return (
        PageBodyFinding(
            "PlaceholderText",
            "remove ellipses or truncation placeholders from PageBody prose",
        ),
    )


def _contains_placeholder_ascii_ellipsis(page_body: str) -> bool:
    for match in re.finditer(r"\.\.\.", page_body):
        next_char = page_body[match.end() : match.end() + 1]
        if next_char and (next_char.isalpha() or next_char in {"_", "$"}):
            continue
        if _is_technical_operator_ellipsis(page_body, match.start(), match.end()):
            continue
        return True
    return False


def _is_technical_operator_ellipsis(text: str, start: int, end: int) -> bool:
    prev_char = text[start - 1 : start] if start else ""
    next_char = text[end : end + 1]
    context = text[max(0, start - 80) : min(len(text), end + 80)].lower()
    if _is_function_call_ellipsis(text, start) and _has_function_call_context(context):
        return True
    if prev_char == "(" and next_char == ")" and _has_ellipsis_operator_context(context):
        return True
    has_operator_boundary = (
        bool(prev_char) and (prev_char.isspace() or prev_char in "[({,")
    ) or (
        bool(next_char) and (next_char.isspace() or next_char in "])},;")
    )
    return _has_ellipsis_operator_context(context) and has_operator_boundary


def _is_function_call_ellipsis(text: str, start: int) -> bool:
    return re.search(r"[A-Za-z_$][\w$]*\($", text[:start]) is not None


def _has_function_call_context(context: str) -> bool:
    return any(
        term in context
        for term in (
            "call",
            "decorator",
            "function",
            "iterator",
            "method",
            "operator",
        )
    )


def _has_ellipsis_operator_context(context: str) -> bool:
    return any(
        term in context
        for term in (
            "destructur",
            "gather",
            "rest parameter",
            "rest operator",
            "spread operator",
            "spread syntax",
            "spread",
            "the ... notation",
            "... notation",
            "... operation",
            "parameter",
            "argument",
        )
    )


def _markdown_shape_findings(
    page_body: str, contract: ResolvedPageBodyContract
) -> tuple[PageBodyFinding, ...]:
    if contract.required_markdown_shape != "claim-bullets":
        return ()
    bullet_count = len(_BULLET_RE.findall(page_body))
    min_bullets = contract.min_claim_bullets or 2
    findings: list[PageBodyFinding] = []
    if bullet_count < min_bullets:
        findings.append(
            PageBodyFinding(
                "RequiredMarkdownShape",
                f"expected at least {min_bullets} markdown bullet claims",
            )
        )
    if contract.max_claim_bullets and bullet_count > contract.max_claim_bullets:
        findings.append(
            PageBodyFinding(
                "RequiredMarkdownShape",
                f"expected at most {contract.max_claim_bullets} markdown bullet claims",
            )
        )
    return tuple(findings)


def _grounding_findings(
    page_body: str, contract: ResolvedPageBodyContract
) -> tuple[PageBodyFinding, ...]:
    findings: list[PageBodyFinding] = []
    normalized_body = normalized_citation_text(page_body)
    for page_id in contract.required_link_page_ids:
        if f"[[{page_id}]]" not in page_body:
            findings.append(PageBodyFinding("RequiredLinkPageIds", f"missing [[{page_id}]]"))
    for citation in contract.required_source_citations:
        if normalized_citation_text(citation) not in normalized_body:
            findings.append(PageBodyFinding("RequiredSourceCitations", f"missing {citation}"))
    if contract.required_uncertainty_terms and not _preserves_uncertainty(
        page_body, contract.required_uncertainty_terms
    ):
        terms = ", ".join(contract.required_uncertainty_terms)
        findings.append(
            PageBodyFinding(
                "RequiredUncertaintyTerms",
                "source_record_text or one bullet_text must include at least one "
                f"literal source uncertainty term: {terms}",
            )
        )
    return tuple(findings)


def _length_findings(
    page_body: str,
    source_text: str,
    contract: ResolvedPageBodyContract,
) -> tuple[PageBodyFinding, ...]:
    page_words = len(_words(_without_raw_citation_text(page_body)))
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
    body_ngrams = _ngrams(_words(_without_raw_citation_text(page_body)), _COPIED_NGRAM_SIZE)
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


def _draft_copy_findings(
    draft: SourceSummaryDraft, source_text: str
) -> tuple[PageBodyFinding, ...]:
    if not source_text:
        return ()
    source_ngrams = set(_ngrams(_words(source_text), _COPIED_NGRAM_SIZE))
    if not source_ngrams:
        return ()
    findings: list[PageBodyFinding] = []
    copied_record = _first_copied_ngram(draft.source_record_text, source_ngrams)
    if copied_record is not None:
        findings.append(
            PageBodyFinding(
                "CopiedSourcePhrase",
                f"source_record_text copies source phrase: {' '.join(copied_record)}",
            )
        )
    for index, bullet in enumerate(draft.claim_bullets, start=1):
        copied = _first_copied_ngram(bullet.bullet_text, source_ngrams)
        if copied is not None:
            findings.append(
                PageBodyFinding(
                    "CopiedSourcePhrase",
                    f"bullet {index} copies source phrase: {' '.join(copied)}",
                )
            )
    return tuple(findings)


def _first_copied_ngram(
    text: str, source_ngrams: set[tuple[str, ...]]
) -> tuple[str, ...] | None:
    text_ngrams = _ngrams(_words(text), _COPIED_NGRAM_SIZE)
    return next((ngram for ngram in text_ngrams if ngram in source_ngrams), None)


def _source_summary_bullet_citation_findings(
    draft: SourceSummaryDraft, plan: SourceSummaryPlan
) -> tuple[PageBodyFinding, ...]:
    if not plan.required_source_citations:
        return ()
    findings: list[PageBodyFinding] = []
    for index, bullet in enumerate(draft.claim_bullets, start=1):
        if not source_summary_bullet_cites_required_locator(
            bullet.bullet_text, plan.required_source_citations
        ):
            required = plan.required_source_citations[0]
            findings.append(
                PageBodyFinding(
                    "SourceSummaryBulletCitation",
                    f"bullet {index} bullet_text must cite {required} "
                    "or a narrower locator within it",
                )
            )
    return tuple(findings)


def _source_framing_bullet_findings(
    draft: SourceSummaryDraft,
) -> tuple[PageBodyFinding, ...]:
    findings: list[PageBodyFinding] = []
    for index, bullet in enumerate(draft.claim_bullets, start=1):
        bullet_text = bullet.bullet_text.strip().lower()
        if any(bullet_text.startswith(prefix) for prefix in SOURCE_FRAMING_PREFIXES):
            findings.append(
                PageBodyFinding(
                    "SourceFramingBullet",
                    f"bullet {index} must start with the subject or finding, not source framing",
                )
            )
    return tuple(findings)


def _source_claim_id_findings(
    draft: SourceSummaryDraft, plan: SourceSummaryPlan
) -> tuple[PageBodyFinding, ...]:
    text_fields = [draft.source_record_text] + [
        bullet.bullet_text for bullet in draft.claim_bullets
    ]
    leaked = tuple(
        claim_id
        for claim_id in plan.selected_source_claims
        if any(claim_id in text for text in text_fields)
    )
    if not leaked:
        return ()
    return (
        PageBodyFinding(
            "SourceClaimIdLeak",
            "internal SourceClaim ids must not appear in source_record_text or bullet_text: "
            + ", ".join(leaked),
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


def _without_raw_citation_text(text: str) -> str:
    return _RAW_CITATION_TEXT_RE.sub("", text)


def _ngrams(words: tuple[str, ...], size: int) -> tuple[tuple[str, ...], ...]:
    if len(words) < size:
        return ()
    return tuple(tuple(words[index : index + size]) for index in range(len(words) - size + 1))
