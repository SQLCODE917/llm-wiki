#!/usr/bin/env python3
"""Shared evidence validation utilities for wiki ingestion.

This module provides unified evidence-in-locator validation logic used by both
wiki_check_synthesis.py and wiki_judge_claims.py to ensure consistent behavior.

The validation distinguishes between:
- Hard integrity failures (evidence fabricated, source missing)
- Soft locator precision issues (off-by-one, hyphenation, prefix match)
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Literal

# Hard failure reasons that should override LLM judge verdicts
HARD_FAIL_REASONS = frozenset({
    "source_not_found",
    "invalid_locator",
    "evidence_not_in_source",
    "locator_outside_source",
})


EvidenceLocationResult = Literal[
    "exact_match",        # Evidence found exactly in locator span
    # Evidence found after normalization (hyphenation, whitespace)
    "normalized_match",
    "prefix_match",       # Evidence prefix found in locator span
    "window_match",       # Evidence found within ±N lines of locator
    "source_match",       # Evidence found elsewhere in source (wrong locator)
    "not_found",          # Evidence not found anywhere in source
]


@dataclass
class EvidenceValidationResult:
    """Result of evidence-in-locator validation."""
    result: EvidenceLocationResult
    severity: Literal["pass", "warn", "fail"]
    reason: str
    suggested_locator: str | None = None
    is_hard_failure: bool = False

    @property
    def passes(self) -> bool:
        return self.severity in ("pass", "warn")


def looks_like_code(text: str) -> bool:
    """Check if text appears to be a code snippet.

    Programming books use code as first-class evidence. Code snippets should
    not be rejected for having few alphanumeric "words".

    Examples that should return True:
        () => 0
        x => x
        function () {}
        foo.bar(baz)
        [1, 2, 3]
        { a: 1 }
        if (x) y()
        return x + 1
        //=> 42
    """
    stripped = text.strip()
    if not stripped:
        return False

    code_signals = [
        r"=>",                                          # Arrow functions
        r"\b(function|return|const|let|var|if|else|for|while|class|new|yield|import|export|async|await)\b",
        r"[{}\[\]();]",                                 # Brackets/parens
        r"\w+\s*\([^)]*\)",                             # Function calls
        r"//\s*=>",                                     # REPL output markers
        r"[+\-*/%]=?|===?|!==?|<=|>=|\|\||&&",         # Operators
        r"^\s*\([^)]*\)\s*$",                           # Bare parenthetical
        r"^\s*`[^`]+`\s*$",                             # Inline code
    ]

    return any(re.search(p, stripped) for p in code_signals)


def normalize_for_search(text: str) -> str:
    """Normalize text for fuzzy matching.

    Handles:
    - Unicode normalization (dashes, quotes)
    - PDF line-break hyphenation (subprob-\\nlems -> subproblems)
    - Parenthetical phrases (removed to handle model paraphrasing)
    - Whitespace collapse
    - Trailing ellipsis/punctuation removal
    """
    replacements = {
        "\u00a0": " ",   # Non-breaking space
        "\u2010": "-",   # Hyphen
        "\u2011": "-",   # Non-breaking hyphen
        "\u2012": "-",   # Figure dash
        "\u2013": "-",   # En dash
        "\u2014": "-",   # Em dash
        "\u2015": "-",   # Horizontal bar
        "\u2018": "'",   # Left single quote
        "\u2019": "'",   # Right single quote
        "\u201c": '"',   # Left double quote
        "\u201d": '"',   # Right double quote
        "\u2026": "...",  # Ellipsis
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    # Join PDF line-break hyphenation: subprob-\nlems -> subproblems
    # Also handles subprob- lems (space after hyphen)
    text = re.sub(r"([A-Za-z])-\s*\n?\s*([a-z])", r"\1\2", text)

    # Remove parenthetical phrases - model may quote without parentheticals
    # E.g., "expression (including typing) to create" -> "expression to create"
    text = re.sub(r'\s*\([^)]*\)\s*', ' ', text)

    # Strip trailing ellipsis from truncated evidence
    text = re.sub(r'\.{3,}\s*$', '', text)

    # Strip trailing punctuation for flexible matching
    text = re.sub(r'[.:;,!?]+$', '', text)

    return " ".join(text.lower().split())


def validate_evidence_location(
    evidence: str,
    locator_start: int,
    locator_end: int,
    source_lines: list[str],
    *,
    window_size: int = 2,
) -> EvidenceValidationResult:
    """Validate that evidence appears at or near the cited locator.

    Args:
        evidence: The evidence text from the wiki page
        locator_start: Start line number (1-indexed)
        locator_end: End line number (1-indexed, inclusive)
        source_lines: All lines from the normalized source
        window_size: Lines to expand when checking near-matches (default: 2)

    Returns:
        EvidenceValidationResult with severity and reason
    """
    # Check locator validity first
    if locator_start < 1 or locator_end < locator_start:
        return EvidenceValidationResult(
            result="not_found",
            severity="fail",
            reason="invalid_locator",
            is_hard_failure=True,
        )

    if locator_end > len(source_lines):
        return EvidenceValidationResult(
            result="not_found",
            severity="fail",
            reason="locator_outside_source",
            is_hard_failure=True,
        )

    # Normalize evidence
    evidence_norm = normalize_for_search(evidence)
    if not evidence_norm:
        return EvidenceValidationResult(
            result="not_found",
            severity="fail",
            reason="empty_evidence",
            is_hard_failure=True,
        )

    # Get locator span text
    locator_text = "\n".join(source_lines[locator_start - 1:locator_end])
    locator_norm = normalize_for_search(locator_text)

    # Check 1: Exact match in locator span
    if evidence_norm in locator_norm:
        return EvidenceValidationResult(
            result="exact_match",
            severity="pass",
            reason="evidence found in locator span",
        )

    # Check 2: Prefix match in locator span (for truncated evidence)
    prefix_len = min(50, len(evidence))
    evidence_prefix = normalize_for_search(evidence[:prefix_len])
    if evidence_prefix and evidence_prefix in locator_norm:
        return EvidenceValidationResult(
            result="prefix_match",
            severity="pass",
            reason="evidence prefix found in locator span",
        )

    # Check 3: Evidence in expanded window (±N lines)
    window_start = max(1, locator_start - window_size)
    window_end = min(len(source_lines), locator_end + window_size)
    window_text = "\n".join(source_lines[window_start - 1:window_end])
    window_norm = normalize_for_search(window_text)

    if evidence_norm in window_norm:
        return EvidenceValidationResult(
            result="window_match",
            severity="warn",
            reason=f"evidence found near locator (within ±{window_size} lines)",
            suggested_locator=f"L{window_start}-L{window_end}",
        )

    if evidence_prefix and evidence_prefix in window_norm:
        return EvidenceValidationResult(
            result="window_match",
            severity="warn",
            reason=f"evidence prefix found near locator (within ±{window_size} lines)",
            suggested_locator=f"L{window_start}-L{window_end}",
        )

    # Check 4: Evidence found elsewhere in source (wrong locator)
    full_source = "\n".join(source_lines)
    full_source_norm = normalize_for_search(full_source)

    if evidence_norm in full_source_norm:
        # Try to find the actual location
        suggested = _find_evidence_location(evidence_norm, source_lines)
        return EvidenceValidationResult(
            result="source_match",
            severity="warn",
            reason="evidence found in source but not at locator; locator may be wrong",
            suggested_locator=suggested,
        )

    if evidence_prefix and evidence_prefix in full_source_norm:
        suggested = _find_evidence_location(evidence_prefix, source_lines)
        return EvidenceValidationResult(
            result="source_match",
            severity="warn",
            reason="evidence prefix found in source but not at locator",
            suggested_locator=suggested,
        )

    # Check 5: Evidence not found anywhere
    return EvidenceValidationResult(
        result="not_found",
        severity="fail",
        reason="evidence_not_in_source",
        is_hard_failure=True,
    )


def _find_evidence_location(evidence_norm: str, source_lines: list[str]) -> str | None:
    """Try to find where evidence appears in source and return suggested locator."""
    for i, line in enumerate(source_lines):
        line_norm = normalize_for_search(line)
        if evidence_norm in line_norm:
            return f"L{i + 1}"

    # Try multi-line search
    for i in range(len(source_lines) - 1):
        two_lines = "\n".join(source_lines[i:i + 2])
        two_lines_norm = normalize_for_search(two_lines)
        if evidence_norm in two_lines_norm:
            return f"L{i + 1}-L{i + 2}"

    return None


def is_evidence_too_short(evidence: str) -> bool:
    """Check if evidence is too short, accounting for code snippets.

    Code snippets like `() => 0` are valid evidence in programming books
    even if they have few alphanumeric words.
    """
    excerpt_words = re.findall(r"[A-Za-z0-9']+", evidence)

    # Short prose is suspicious, short code is not
    if len(excerpt_words) < 4 and len(evidence) < 24:
        if looks_like_code(evidence):
            return False  # Code snippets are valid evidence
        return True

    return False


def should_fail_on_deterministic_flag(reason: str) -> bool:
    """Check if a deterministic flag reason should cause a hard failure.

    Hard failures override LLM judge "supported" verdicts.
    Soft issues (locator precision) do not.
    """
    # Normalize reason to check against hard fail reasons
    reason_normalized = reason.lower().replace(" ", "_").replace("-", "_")

    # Check for hard failure patterns
    hard_patterns = [
        "source_not_found",
        "invalid_locator",
        "evidence_not_in_source",
        "locator_outside_source",
        "not_parseable",
        "outside_normalized_source",
        "fabricated",
        "contradicted",
    ]

    for pattern in hard_patterns:
        if pattern in reason_normalized:
            return True

    return False


# Weak evidence patterns that indicate navigation/metadata, not content
WEAK_EVIDENCE_PATTERNS = [
    r"^(chapter|section|part|page)\s+\d+",
    r"^table\s+of\s+contents",
    r"^\d+\.\d+",
    r"^see\s+(also|chapter|section)",
    r"^continued\s+(on|from)",
]


def is_weak_evidence(evidence: str) -> bool:
    """Check if evidence is navigation/metadata rather than content."""
    return any(re.search(p, evidence.strip(), re.IGNORECASE) for p in WEAK_EVIDENCE_PATTERNS)
