"""Locator matching against generated source evidence registries."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Literal

from llmwiki.domain.citations import Citation, CitationFinding
from llmwiki.domain.evidence_registry import EvidenceRegistry

LocatorConfidence = Literal[
    "exact", "canonicalized-local", "local-window", "canonicalized-global", "none"
]


@dataclass(frozen=True)
class LocatorMatch:
    locator: str
    confidence: LocatorConfidence
    finding_code: str = ""
    suggested_locator: str = ""


def locator_match_for_citation(
    citation: Citation, registry: EvidenceRegistry
) -> tuple[LocatorMatch, CitationFinding | None]:
    if citation.line_range is None:
        return LocatorMatch(citation.raw_text, "none"), None
    lines = registry.source_lines(citation.source_path)
    if lines is None:
        return LocatorMatch(citation.raw_text, "none"), None
    start, end = citation.line_range
    if end > len(lines):
        return LocatorMatch(citation.raw_text, "none", "locator-out-of-range"), _finding(
            citation,
            "fail",
            "locator-out-of-range",
            f"Locator normalized:L{start}-L{end} is outside {citation.source_path} "
            f"({len(lines)} lines).",
        )
    if citation.evidence_text is None:
        return LocatorMatch(citation.raw_text, "none"), None
    span = "\n".join(lines[start - 1 : end])
    evidence = citation.evidence_text.strip()
    if evidence.lower() in span.lower():
        return LocatorMatch(citation.raw_text, "exact"), None
    evidence_key = canonicalize_evidence_text(evidence)
    span_key = canonicalize_evidence_text(span)
    if evidence_key and evidence_key in span_key:
        return LocatorMatch(citation.raw_text, "canonicalized-local"), _finding(
            citation,
            "warn",
            "evidence-canonicalized",
            "Evidence matches the cited locator after source-text canonicalization.",
        )
    window_start = max(1, start - 2)
    window_end = min(len(lines), end + 2)
    window = "\n".join(lines[window_start - 1 : window_end])
    if evidence_key and evidence_key in canonicalize_evidence_text(window):
        return LocatorMatch(
            citation.raw_text,
            "local-window",
            "evidence-outside-locator",
            _locator(window_start, window_end),
        ), _finding(
            citation,
            "warn",
            "evidence-outside-locator",
            f"Evidence appears near the cited normalized locator. "
            f"Suggested locator: {_locator(window_start, window_end)}.",
        )
    suggested = suggested_locator(evidence_key, lines)
    if suggested:
        return LocatorMatch(
            citation.raw_text, "canonicalized-global", "evidence-outside-locator", suggested
        ), _finding(
            citation,
            "warn",
            "evidence-outside-locator",
            "Evidence appears in the source but outside the cited normalized locator. "
            f"Suggested locator: {suggested}.",
        )
    return LocatorMatch(citation.raw_text, "none", "evidence-not-found"), _finding(
        citation,
        "fail",
        "evidence-not-found",
        "Quoted/table evidence was not found at the cited locator or elsewhere in the source.",
    )


def source_range_finding(citation: Citation, registry: EvidenceRegistry) -> CitationFinding | None:
    ranges = registry.ranges_for_page(citation.page_name, citation.source_path)
    if not ranges:
        return None
    if any(source_range.contains(citation) for source_range in ranges):
        return None
    return _finding(
        citation,
        "warn",
        "source-range-violation",
        "Citation locator is outside the planned source range for this page.",
    )


def canonicalize_evidence_text(text: str) -> str:
    text = re.sub(r"\bPage\s+\d+\b", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"(?<=\w)-\s+(?=\w)", "", text)
    text = re.sub(r"[\u2010-\u2015\u2212]", "-", text)
    text = re.sub(r"[“”]", '"', text)
    text = re.sub(r"[‘’]", "'", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def suggested_locator(evidence_key: str, lines: tuple[str, ...]) -> str:
    if not evidence_key:
        return ""
    for window_size in (1, 2, 3, 4):
        for start_index in range(1, len(lines) + 1):
            end_index = min(len(lines), start_index + window_size - 1)
            span = "\n".join(lines[start_index - 1 : end_index])
            if evidence_key in canonicalize_evidence_text(span):
                return _locator(start_index, end_index)
    return ""


def _locator(start: int, end: int) -> str:
    return f"normalized:L{start}" if start == end else f"normalized:L{start}-L{end}"


def _finding(
    citation: Citation,
    severity: str,
    code: str,
    message: str,
) -> CitationFinding:
    return CitationFinding(
        page_name=citation.page_name,
        severity=severity,  # type: ignore[arg-type]
        citation_text=citation.raw_text,
        code=code,  # type: ignore[arg-type]
        message=message,
    )
