"""Line-addressed evidence checks for normalized raw-source locators."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from typing import Literal, Protocol

from llmwiki.domain.citations import Citation, CitationFinding, FindingCode

MatchConfidence = Literal["exact", "canonicalized-local", "canonicalized-global", "none"]


class SourceTextResolver(Protocol):
    def source_lines(self, source_path: str) -> tuple[str, ...] | None:
        """Return 1-indexed-addressable source lines for a raw citation path."""


@dataclass(frozen=True)
class ResolvedLocator:
    source_path: str
    line_range: tuple[int, int]
    text: str
    confidence: MatchConfidence


def resolve_normalized_evidence(
    citation: Citation, resolver: SourceTextResolver
) -> tuple[ResolvedLocator | None, CitationFinding | None]:
    """Resolve and validate one citation's normalized locator, if present."""

    if citation.line_range is None:
        return None, None
    lines = resolver.source_lines(citation.source_path)
    if lines is None:
        return None, None
    start, end = citation.line_range
    if start < 1 or end < start:
        return None, _finding(
            citation,
            "fail",
            "invalid-locator",
            "Normalized line locators must be positive and ordered.",
        )
    if end > len(lines):
        return None, _finding(
            citation,
            "fail",
            "locator-out-of-range",
            f"Locator normalized:L{start}-L{end} is outside {citation.source_path} "
            f"({len(lines)} lines).",
        )
    span = "\n".join(lines[start - 1 : end])
    evidence = citation.evidence_text
    if evidence is None:
        return ResolvedLocator(citation.source_path, (start, end), span, "none"), None
    return _match_evidence(citation, lines, span)


def _match_evidence(
    citation: Citation, lines: tuple[str, ...], span: str
) -> tuple[ResolvedLocator | None, CitationFinding | None]:
    assert citation.line_range is not None
    assert citation.evidence_text is not None
    start, end = citation.line_range
    evidence = citation.evidence_text.strip()
    if evidence.lower() in span.lower():
        return ResolvedLocator(citation.source_path, (start, end), span, "exact"), None
    evidence_key = _canonicalize(evidence)
    span_key = _canonicalize(span)
    if evidence_key and evidence_key in span_key:
        return ResolvedLocator(citation.source_path, (start, end), span, "canonicalized-local"), (
            _finding(
                citation,
                "warn",
                "evidence-canonicalized",
                "Evidence matches the cited locator only after whitespace/Unicode normalization.",
            )
        )
    full_text = "\n".join(lines)
    if evidence_key and evidence_key in _canonicalize(full_text):
        suggested = _suggest_locator(evidence_key, lines)
        message = "Evidence appears in the source but outside the cited normalized locator."
        if suggested is not None:
            message += f" Suggested locator: {suggested}."
        return ResolvedLocator(citation.source_path, (start, end), span, "canonicalized-global"), (
            _finding(citation, "warn", "evidence-outside-locator", message)
        )
    return None, _finding(
        citation,
        "fail",
        "evidence-not-found",
        "Quoted/table evidence was not found at the cited locator or elsewhere in the source.",
    )


def _suggest_locator(evidence_key: str, lines: tuple[str, ...]) -> str | None:
    for index, line in enumerate(lines, start=1):
        if evidence_key in _canonicalize(line):
            return f"normalized:L{index}"
    for start in range(1, len(lines) + 1):
        joined = "\n".join(lines[start - 1 : min(len(lines), start + 2)])
        if evidence_key in _canonicalize(joined):
            return f"normalized:L{start}-L{min(len(lines), start + 2)}"
    return None


def _canonicalize(text: str) -> str:
    normalized = unicodedata.normalize("NFKC", text)
    normalized = re.sub(r"[\u2010-\u2015\u2212]", "-", normalized)
    normalized = re.sub(r"(?<=\w)-\s+(?=\w)", "", normalized)
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized.strip().lower()


def _finding(
    citation: Citation, severity: Literal["warn", "fail"], code: FindingCode, message: str
) -> CitationFinding:
    return CitationFinding(
        page_name=citation.page_name,
        severity=severity,
        citation_text=citation.raw_text,
        code=code,
        message=message,
    )
