"""Evidence validation for wiki ingestion pipeline.

Validates that evidence excerpts appear at cited locators.

The validation distinguishes between:
- Hard integrity failures (evidence fabricated, source missing)
- Soft locator precision issues (off-by-one, hyphenation, prefix match)

Usage:
    from wiki_io.evidence import validate_evidence_location, canonicalize_for_evidence_match
    
    result = validate_evidence_location(evidence, start, end, source_lines)
    if result.is_hard_failure:
        print(f"FAIL: {result.reason}")
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
    "exact_match",             # Evidence found byte-exact in locator span
    "canonicalized_local",     # Evidence found after canonicalization in locator span
    # Evidence found after canonicalization near locator (±N lines)
    "canonicalized_window",
    "canonicalized_global",    # Evidence found after canonicalization elsewhere in source
    "prefix_match",            # Evidence prefix found in locator span
    "not_found",               # Evidence not found anywhere in source
]


MatchConfidence = Literal[
    "exact",                   # Byte-exact match
    "canonicalized-local",     # Canonicalized match at or near locator
    "canonicalized-global",    # Canonicalized match elsewhere in source
    "none",                    # No match found
]


@dataclass
class EvidenceValidationResult:
    """Result of evidence-in-locator validation."""
    result: EvidenceLocationResult
    severity: Literal["pass", "warn", "fail"]
    reason: str
    confidence: MatchConfidence = "none"
    suggested_locator: str | None = None
    is_hard_failure: bool = False

    @property
    def passes(self) -> bool:
        return self.severity in ("pass", "warn")


# Unicode character replacements for canonicalization
_UNICODE_REPLACEMENTS = {
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


def looks_like_code(text: str) -> bool:
    """Check if text appears to be a code snippet.

    Programming books use code as first-class evidence. Code snippets should
    not be rejected for having few alphanumeric "words".
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


def canonicalize_for_evidence_match(text: str) -> str:
    """Canonicalize text for evidence validation.

    This aggressive normalization handles PDF/Markdown extraction artifacts:
    - Page break markers (---, <!-- page N -->)
    - Hyphenated line wraps from column layouts
    - Inconsistent bullets and dashes
    - Whitespace and line wrap variations

    Intended only for validator comparison, not for user-facing text.
    """
    # Normalize line endings first
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Remove PDF page break artifacts
    text = re.sub(
        r"\n---\n\s*<!--\s*page\s+\d+\s*-->\s*\n",
        "\n",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\n\s*<!--\s*page\s+\d+\s*-->\s*\n",
        "\n",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r"\n\s*---\s*\n", "\n", text)

    # Remove isolated page numbers/headers
    text = re.sub(r"\n[A-Z][A-Za-z :'-]{5,50}\n\d{1,4}\n", "\n", text)
    text = re.sub(r"\n\d{1,4}\n(?=[A-Z])", "\n", text)
    text = re.sub(
        r"\n[A-Z][A-Za-z :'-]{5,50}\n[ivxlcdm]+\n", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"\n[ivxlcdm]+\n", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"\n[A-Z ]{3,30}\n", "\n", text)

    # Unicode normalization
    for old, new in _UNICODE_REPLACEMENTS.items():
        text = text.replace(old, new)

    # Normalize ASCII dash variants
    text = text.replace("‐", "-")

    # Un-escape Markdown table escapes
    text = text.replace(r'\|', '|')
    text = text.replace(r'\"', '"')
    text = text.replace(r"\'", "'")

    # Remove enclosing quotes
    text = text.strip()
    if (text.startswith('"') and text.endswith('"')) or \
       (text.startswith("'") and text.endswith("'")):
        text = text[1:-1]

    # Strip trailing ellipsis
    text = re.sub(r'\.{2,}\s*$', '', text)
    text = re.sub(r'…\s*$', '', text)

    # Join PDF hyphenated line wraps
    text = re.sub(r"(?<=\w)-\n(?=\w)", "-", text)

    # Join ordinary wrapped prose lines
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)

    # Collapse whitespace
    text = re.sub(r"\s+", " ", text)

    # Normalize bullet variants
    text = text.replace("●", "•").replace("* ", "• ")

    # Remove intra-word hyphens for compound word matching
    text = re.sub(r"(?<=\w)-(?=\w)", "", text)

    return text.strip().lower()


def validate_evidence_location(
    evidence: str,
    locator_start: int,
    locator_end: int,
    source_lines: list[str],
    *,
    window_size: int = 2,
) -> EvidenceValidationResult:
    """Validate that evidence appears at or near the cited locator.

    Uses artifact-tolerant canonicalization to handle PDF extraction issues
    like line-wrapped hyphenation, page break markers, and whitespace variations.

    Args:
        evidence: The evidence text from the wiki page
        locator_start: Start line number (1-indexed)
        locator_end: End line number (1-indexed, inclusive)
        source_lines: All lines from the normalized source
        window_size: Lines to expand when checking near-matches (default: 2)

    Returns:
        EvidenceValidationResult with severity, confidence, and reason
    """
    # Check locator validity first
    if locator_start < 1 or locator_end < locator_start:
        return EvidenceValidationResult(
            result="not_found",
            confidence="none",
            severity="fail",
            reason="invalid_locator",
            is_hard_failure=True,
        )

    if locator_end > len(source_lines):
        return EvidenceValidationResult(
            result="not_found",
            confidence="none",
            severity="fail",
            reason="locator_outside_source",
            is_hard_failure=True,
        )

    # Canonicalize evidence
    evidence_canonical = canonicalize_for_evidence_match(evidence)
    if not evidence_canonical:
        return EvidenceValidationResult(
            result="not_found",
            confidence="none",
            severity="fail",
            reason="empty_evidence",
            is_hard_failure=True,
        )

    # Get locator span text
    locator_text = "\n".join(source_lines[locator_start - 1:locator_end])
    locator_canonical = canonicalize_for_evidence_match(locator_text)

    # Check 1: Exact byte match in locator span
    evidence_stripped = evidence.strip().lower()
    locator_lower = locator_text.lower()
    if evidence_stripped in locator_lower:
        return EvidenceValidationResult(
            result="exact_match",
            confidence="exact",
            severity="pass",
            reason="evidence found byte-exact in locator span",
        )

    # Check 2: Canonicalized match in locator span
    if evidence_canonical in locator_canonical:
        return EvidenceValidationResult(
            result="canonicalized_local",
            confidence="canonicalized-local",
            severity="pass",
            reason="evidence found after canonicalization in locator span",
        )

    # Check 3: Prefix match (first N chars match)
    min_prefix = min(40, len(evidence_canonical))
    if min_prefix > 10 and evidence_canonical[:min_prefix] in locator_canonical:
        return EvidenceValidationResult(
            result="prefix_match",
            confidence="canonicalized-local",
            severity="warn",
            reason="evidence prefix matches locator span",
        )

    # Check 4: Expanded window around locator
    window_start = max(1, locator_start - window_size)
    window_end = min(len(source_lines), locator_end + window_size)
    window_text = "\n".join(source_lines[window_start - 1:window_end])
    window_canonical = canonicalize_for_evidence_match(window_text)

    if evidence_canonical in window_canonical:
        return EvidenceValidationResult(
            result="canonicalized_window",
            confidence="canonicalized-local",
            severity="warn",
            reason=f"evidence found within ±{window_size} lines of locator",
        )

    # Check 5: Global search in full source
    full_source = "\n".join(source_lines)
    full_canonical = canonicalize_for_evidence_match(full_source)

    if evidence_canonical in full_canonical:
        # Find where it actually appears for suggested locator
        suggested = _find_suggested_locator(evidence_canonical, source_lines)
        return EvidenceValidationResult(
            result="canonicalized_global",
            confidence="canonicalized-global",
            severity="warn",
            reason="evidence found elsewhere in source (locator may be wrong)",
            suggested_locator=suggested,
        )

    # Not found anywhere
    return EvidenceValidationResult(
        result="not_found",
        confidence="none",
        severity="fail",
        reason="evidence_not_in_source",
        is_hard_failure=True,
    )


def _find_suggested_locator(evidence_canonical: str, source_lines: list[str]) -> str | None:
    """Find the best locator for evidence in source lines."""
    for start_line in range(len(source_lines)):
        for end_line in range(start_line, min(start_line + 10, len(source_lines))):
            span_text = "\n".join(source_lines[start_line:end_line + 1])
            span_canonical = canonicalize_for_evidence_match(span_text)
            if evidence_canonical in span_canonical:
                return f"normalized:L{start_line + 1}-L{end_line + 1}"
    return None
