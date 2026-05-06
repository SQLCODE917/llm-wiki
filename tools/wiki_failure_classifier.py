#!/usr/bin/env python3
"""Structured validation failures for wiki compilation pipeline.

Each failure is classified into a category that determines:
1. Whether it can be fixed deterministically (no LLM needed)
2. What specific repair function to use
3. What hints to provide if LLM repair is needed

This module provides:
- FailureCategory enum for all known failure types
- FailureSeverity enum (error/warning)
- ValidationFailure dataclass (frozen for hashing/fingerprinting)
- fail() helper for creating failures
- render_failures_log() for human-readable output
- parse_validation_output() for legacy compatibility only
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any


class FailureSeverity(str, Enum):
    """Severity level for validation failures."""
    ERROR = "error"
    WARNING = "warning"


class FailureCategory(str, Enum):
    """Categories of validation failures."""

    # Deterministically fixable - frontmatter
    FRONTMATTER_MISSING_KEY = "frontmatter_missing_key"
    FRONTMATTER_BAD_VALUE = "frontmatter_bad_value"
    FRONTMATTER_INVALID_VALUE = "frontmatter_invalid_value"
    FRONTMATTER_BAD_TYPE = "frontmatter_bad_type"
    FRONTMATTER_BAD_STATUS = "frontmatter_bad_status"
    FRONTMATTER_PARSE_ERROR = "frontmatter_parse_error"

    # Deterministically fixable - structure
    MISSING_SOURCE_LINK = "missing_source_link"
    MISSING_SOURCE_SECTION = "missing_source_section"
    MISSING_SOURCES_SECTION = "missing_sources_section"
    MISSING_SOURCE_BACKLINK = "missing_source_backlink"
    MISSING_SOURCE_DETAILS = "missing_source_details"
    PLACEHOLDER_TEXT = "placeholder_text"
    EMPTY_SECTION = "empty_section"
    DUPLICATE_HEADING = "duplicate_heading"
    MISSING_H1_TITLE = "missing_h1_title"
    STRAY_FRONTMATTER = "stray_frontmatter"
    STRUCTURE_VIOLATION = "structure_violation"
    THIN_CONTENT = "thin_content"

    # Renderer/markdown failures (should be impossible with deterministic rendering)
    MALFORMED_TABLE = "malformed_table"
    MISSING_TABLE_COLUMN = "missing_table_column"
    BAD_SOURCE_CELL = "bad_source_cell"
    DIFF_MARKER = "diff_marker"

    # Evidence binding failures
    INVALID_EVIDENCE_ID = "invalid_evidence_id"
    BAD_LOCATOR_FORMAT = "bad_locator_format"
    LOCATOR_FORMAT_ERROR = "locator_format_error"
    LOCATOR_OUT_OF_RANGE = "locator_out_of_range"
    LOCATOR_OUTSIDE_RANGE = "locator_outside_range"
    EVIDENCE_MISMATCH = "evidence_mismatch"
    EVIDENCE_NOT_IN_LOCATOR = "evidence_not_in_locator"
    QUOTE_NOT_FOUND_AT_LOCATOR = "quote_not_found_at_locator"
    INVALID_SOURCE_RANGE = "invalid_source_range"
    MISSING_SOURCE_RANGE = "missing_source_range"
    WRONG_SOURCE_LINK = "wrong_source_link"

    # Evidence table structure
    MISSING_EVIDENCE_TABLE = "missing_evidence_table"
    EVIDENCE_TABLE_HEADER = "evidence_table_header"
    EVIDENCE_TABLE_STRUCTURE = "evidence_table_structure"
    REFERENCE_TABLE_STRUCTURE = "reference_table_structure"

    # Schema contract violations
    SCHEMA_FORBIDDEN_FIELD = "schema_forbidden_field"

    # Semantic failures (require LLM)
    TOO_FEW_CLAIMS = "too_few_claims"
    CLAIM_TOO_SHORT = "claim_too_short"
    CLAIM_COPIES_EVIDENCE = "claim_copies_evidence"
    WEAK_CLAIM_TEXT = "weak_claim_text"
    WEAK_CLAIM_LANGUAGE = "weak_claim_language"
    UNSUPPORTED_CLAIM = "unsupported_claim"
    CLAIM_OFF_TOPIC = "claim_off_topic"
    EVIDENCE_TOO_SHORT = "evidence_too_short"
    WEAK_EVIDENCE = "weak_evidence"
    REPEATED_PHRASE = "repeated_phrase"
    DUPLICATE_CLAIM = "duplicate_claim"
    OVERREACH = "overreach"
    OUT_OF_SCOPE = "out_of_scope"

    # Structural issues requiring content decisions
    MISSING_STEPS_SECTION = "missing_steps_section"
    MISSING_REFERENCE_DATA = "missing_reference_data"
    MISSING_REQUIRED_SECTION = "missing_required_section"
    UNCREATED_CANDIDATE_MENTION = "uncreated_candidate_mention"
    REFERENCE_TO_UNCREATED = "reference_to_uncreated"
    INVALID_EXECUTABLE_SECTION = "invalid_executable_section"
    TOO_FEW_STEPS = "too_few_steps"
    TOO_FEW_DATA_ROWS = "too_few_data_rows"

    # Wiki graph/link failures
    BROKEN_WIKI_LINK = "broken_wiki_link"
    BROKEN_LINK = "broken_link"
    TITLE_SLUG_MISMATCH = "title_slug_mismatch"

    # Synthesis-level failures (source page checks)
    MISSING_SOURCE_PAGE = "missing_source_page"
    TOO_FEW_SYNTH_PAGES = "too_few_synth_pages"
    TOO_MANY_SYNTH_PAGES = "too_many_synth_pages"
    UNAUTHORIZED_PAGE = "unauthorized_page"
    MISSING_ALLOWED_PAGE = "missing_allowed_page"
    UNLINKED_SYNTH_PAGE = "unlinked_synth_page"
    CANDIDATE_PAGE_EXISTS = "candidate_page_exists"

    # Related pages table failures
    RELATED_TABLE_STRUCTURE = "related_table_structure"

    # Character/encoding failures
    NON_ASCII_CHARS = "non_ascii_chars"

    # File scope issues (runner artifacts, not page content)
    FILE_SCOPE_VIOLATION = "file_scope_violation"

    # Unknown
    UNKNOWN = "unknown"


# Categories that can be fixed without LLM
DETERMINISTIC_CATEGORIES = {
    FailureCategory.FRONTMATTER_MISSING_KEY,
    FailureCategory.FRONTMATTER_BAD_VALUE,
    FailureCategory.FRONTMATTER_INVALID_VALUE,
    FailureCategory.FRONTMATTER_BAD_TYPE,
    FailureCategory.FRONTMATTER_BAD_STATUS,
    FailureCategory.FRONTMATTER_PARSE_ERROR,
    FailureCategory.MISSING_SOURCE_LINK,
    FailureCategory.MISSING_SOURCE_SECTION,
    FailureCategory.MISSING_SOURCES_SECTION,
    FailureCategory.MISSING_SOURCE_BACKLINK,
    FailureCategory.PLACEHOLDER_TEXT,
    FailureCategory.EMPTY_SECTION,
    FailureCategory.INVALID_EVIDENCE_ID,
    FailureCategory.BAD_SOURCE_CELL,
    FailureCategory.FILE_SCOPE_VIOLATION,
    FailureCategory.STRAY_FRONTMATTER,
    FailureCategory.CANDIDATE_PAGE_EXISTS,
    FailureCategory.NON_ASCII_CHARS,
    FailureCategory.WRONG_SOURCE_LINK,
}

# Categories that can suggest fixes but may need LLM
SEMI_DETERMINISTIC_CATEGORIES = {
    FailureCategory.BAD_LOCATOR_FORMAT,
    FailureCategory.LOCATOR_FORMAT_ERROR,
    FailureCategory.LOCATOR_OUT_OF_RANGE,
    FailureCategory.LOCATOR_OUTSIDE_RANGE,
    FailureCategory.EVIDENCE_MISMATCH,
    FailureCategory.EVIDENCE_NOT_IN_LOCATOR,
    FailureCategory.QUOTE_NOT_FOUND_AT_LOCATOR,
    FailureCategory.DUPLICATE_HEADING,
    FailureCategory.INVALID_SOURCE_RANGE,
    FailureCategory.MISSING_SOURCE_RANGE,
    FailureCategory.RELATED_TABLE_STRUCTURE,
    FailureCategory.EVIDENCE_TABLE_HEADER,
    FailureCategory.EVIDENCE_TABLE_STRUCTURE,
    FailureCategory.REFERENCE_TABLE_STRUCTURE,
    FailureCategory.MISSING_EVIDENCE_TABLE,
}

# Renderer bugs (should be impossible with deterministic rendering)
RENDERER_BUG_CATEGORIES = {
    FailureCategory.MALFORMED_TABLE,
    FailureCategory.MISSING_TABLE_COLUMN,
    FailureCategory.BAD_SOURCE_CELL,  # Also deterministic if renderer-owned
}


@dataclass(frozen=True)
class ValidationFailure:
    """A classified validation failure.

    frozen=True makes failures hashable for fingerprinting and deduplication.
    """
    category: FailureCategory
    page: str
    message: str
    severity: FailureSeverity = FailureSeverity.ERROR
    row: int | None = None  # For row-specific failures
    field: str | None = None  # For field-specific failures
    value: Any | None = None  # Current problematic value
    expected: Any | None = None  # Expected value or format
    fix_hint: str | None = None  # Specific repair instruction

    @property
    def deterministic_fix(self) -> bool:
        """Whether this failure can be fixed without LLM."""
        return self.category in DETERMINISTIC_CATEGORIES

    @property
    def semi_deterministic(self) -> bool:
        """Whether this failure can suggest fixes."""
        return self.category in SEMI_DETERMINISTIC_CATEGORIES

    @property
    def is_renderer_bug(self) -> bool:
        """Whether this failure indicates a renderer bug, not a model failure."""
        return self.category in RENDERER_BUG_CATEGORIES

    @property
    def needs_llm(self) -> bool:
        """Whether this failure requires LLM to fix."""
        return not self.deterministic_fix and not self.semi_deterministic


# ---------------------------------------------------------------------------
# Helper function for creating failures
# ---------------------------------------------------------------------------

def fail(
    failures: list[ValidationFailure],
    category: FailureCategory,
    page: str | Path,
    message: str,
    *,
    severity: FailureSeverity = FailureSeverity.ERROR,
    row: int | None = None,
    field: str | None = None,
    value: Any | None = None,
    expected: Any | None = None,
    fix_hint: str | None = None,
) -> None:
    """Append a ValidationFailure to the failures list.

    This helper keeps call sites short and consistent.
    """
    failures.append(
        ValidationFailure(
            category=category,
            page=str(page),
            message=message,
            severity=severity,
            row=row,
            field=field,
            value=value,
            expected=expected,
            fix_hint=fix_hint,
        )
    )


# ---------------------------------------------------------------------------
# Human-readable output renderer
# ---------------------------------------------------------------------------

def render_failures_log(failures: list[ValidationFailure]) -> str:
    """Render failures to human-readable log format.

    This is the ONLY place that formats FAIL: text.
    Do not parse this output programmatically.
    """
    if not failures:
        return "PASS\n"

    lines: list[str] = []
    for f in failures:
        # Main failure line
        prefix = "FAIL" if f.severity == FailureSeverity.ERROR else "WARN"
        parts = [f"{prefix}: {f.page}: {f.message}"]

        # Additional details in parentheses
        details = [f"category={f.category.value}"]
        if f.row is not None:
            details.append(f"row={f.row}")
        if f.field is not None:
            details.append(f"field={f.field}")

        parts.append(f" ({', '.join(details)})")
        lines.append("".join(parts))

        # Fix hint on separate line
        if f.fix_hint:
            lines.append(f"  Hint: {f.fix_hint}")

    return "\n".join(lines) + "\n"


def failure_fingerprint(failures: list[ValidationFailure]) -> tuple:
    """Create hashable fingerprint of failure set for progress detection.

    Returns a sorted tuple that can be compared to detect no-progress.
    """
    return tuple(
        sorted(
            (
                f.category.value,
                f.page,
                f.row,
                f.field,
                str(f.value) if f.value is not None else "",
                str(f.expected) if f.expected is not None else "",
            )
            for f in failures
        )
    )


def failure_to_json(f: ValidationFailure) -> dict:
    """Convert failure to JSON-serializable dict for JSONL logging."""
    return {
        "category": f.category.value,
        "severity": f.severity.value,
        "page": f.page,
        "message": f.message,
        "row": f.row,
        "field": f.field,
        "value": f.value if isinstance(f.value, (str, int, float, bool, type(None))) else str(f.value),
        "expected": f.expected if isinstance(f.expected, (str, int, float, bool, type(None))) else str(f.expected),
        "fix_hint": f.fix_hint,
        "deterministic_fix": f.deterministic_fix,
        "semi_deterministic": f.semi_deterministic,
    }


# ---------------------------------------------------------------------------
# Legacy compatibility: regex parsing of FAIL: lines
# ---------------------------------------------------------------------------
# TODO(remove after phase2 runner migration): compatibility only.
# New code should use check_synthesis_structured() directly.


# Regex patterns for parsing validation output
PATTERNS = {
    # Frontmatter issues
    r"missing frontmatter key ['\"]?(\w+)['\"]?": (
        FailureCategory.FRONTMATTER_MISSING_KEY, "field"
    ),
    r"type must be one of": (
        FailureCategory.FRONTMATTER_BAD_TYPE, None
    ),
    r"status must be one of": (
        FailureCategory.FRONTMATTER_BAD_STATUS, None
    ),

    # Structure issues
    r"missing H1 title": (
        FailureCategory.MISSING_H1_TITLE, None
    ),
    r"body must link back to": (
        FailureCategory.MISSING_SOURCE_LINK, None
    ),
    r"missing source.?page section": (
        FailureCategory.MISSING_SOURCE_SECTION, None
    ),
    r"contains placeholder text": (
        FailureCategory.PLACEHOLDER_TEXT, None
    ),
    r"empty section ['\"]?([^'\"]+)['\"]?": (
        FailureCategory.EMPTY_SECTION, "field"
    ),
    r"duplicate heading ['\"]?([^'\"]+)['\"]?": (
        FailureCategory.DUPLICATE_HEADING, "field"
    ),
    r"missing source-backed details section": (
        FailureCategory.TOO_FEW_CLAIMS, None
    ),
    r"synthesized pages must not mention uncreated": (
        FailureCategory.UNCREATED_CANDIDATE_MENTION, None
    ),

    # Evidence table - row specific
    r"evidence row (\d+) locator must look like": (
        FailureCategory.BAD_LOCATOR_FORMAT, "row"
    ),
    r"evidence row (\d+) locator ['\"]?([^'\"]+)['\"]? is outside allowed source range": (
        FailureCategory.LOCATOR_OUT_OF_RANGE, "row_value"
    ),
    r"evidence row (\d+) excerpt is not found in locator range": (
        FailureCategory.EVIDENCE_NOT_IN_LOCATOR, "row"
    ),
    r"evidence row (\d+) source cell must link": (
        FailureCategory.BAD_SOURCE_CELL, "row"
    ),
    r"evidence row (\d+) claim is too short": (
        FailureCategory.CLAIM_TOO_SHORT, "row"
    ),
    r"evidence row (\d+) claim repeats the evidence": (
        FailureCategory.CLAIM_COPIES_EVIDENCE, "row"
    ),
    r"evidence row (\d+) excerpt is too short": (
        FailureCategory.EVIDENCE_TOO_SHORT, "row"
    ),
    r"evidence row (\d+) excerpt is document navigation": (
        FailureCategory.WEAK_EVIDENCE, "row"
    ),
    r"fewer than (\d+) evidence rows": (
        FailureCategory.TOO_FEW_CLAIMS, "value"
    ),

    # Reference page specific
    r"Reference data row (\d+)": (
        FailureCategory.MISSING_REFERENCE_DATA, "row"
    ),
    r"missing.*Steps section": (
        FailureCategory.MISSING_STEPS_SECTION, None
    ),

    # File scope
    r"changed outside.*allowed files": (
        FailureCategory.FILE_SCOPE_VIOLATION, None
    ),
}


def classify_failure(line: str, page: str = "") -> ValidationFailure | None:
    """Classify a single validation failure line.

    LEGACY: Use for parsing existing log text only.
    New code should use check_synthesis_structured() directly.
    """
    # Skip non-failure lines
    if not line.strip().startswith("FAIL:"):
        return None

    # Extract page path if present
    page_match = re.search(r"FAIL:\s*([\w/.-]+\.md):", line)
    if page_match:
        page = page_match.group(1)

    message = line.replace("FAIL:", "").strip()

    # Try each pattern
    for pattern, (category, extract_type) in PATTERNS.items():
        match = re.search(pattern, line, re.IGNORECASE)
        if match:
            # Extract additional info based on pattern type
            field_val: str | None = None
            row_val: int | None = None
            value_val: str | None = None

            if extract_type == "field" and match.groups():
                field_val = match.group(1)
            elif extract_type == "row" and match.groups():
                row_val = int(match.group(1))
            elif extract_type == "row_value" and len(match.groups()) >= 2:
                row_val = int(match.group(1))
                value_val = match.group(2)
            elif extract_type == "value" and match.groups():
                value_val = match.group(1)

            # Get fix hint (need a partial failure for the hint function)
            fix_hint = _get_fix_hint_for_category(
                category, field_val, value_val)

            return ValidationFailure(
                category=category,
                page=page,
                message=message,
                row=row_val,
                field=field_val,
                value=value_val,
                fix_hint=fix_hint,
            )

    # Unknown failure type
    return ValidationFailure(
        category=FailureCategory.UNKNOWN,
        page=page,
        message=message,
    )


def _get_fix_hint_for_category(
    category: FailureCategory,
    field: str | None = None,
    value: str | None = None,
) -> str | None:
    """Get a specific fix hint for a failure category."""
    hints = {
        FailureCategory.FRONTMATTER_MISSING_KEY:
            f"Add '{field}' to frontmatter with appropriate default" if field else "Add missing frontmatter key",
        FailureCategory.MISSING_SOURCE_LINK:
            "Add source page to frontmatter.sources list",
        FailureCategory.MISSING_SOURCE_SECTION:
            "Add '## Source pages' section with link to source",
        FailureCategory.PLACEHOLDER_TEXT:
            "Remove 'Page title' and other placeholder text",
        FailureCategory.BAD_SOURCE_CELL:
            "Change source cell to [Source](../sources/SLUG.md) link format",
        FailureCategory.BAD_LOCATOR_FORMAT:
            "Use format `normalized:L123` or `normalized:L123-L456`",
        FailureCategory.LOCATOR_OUT_OF_RANGE:
            f"Locator {value} is outside allowed range. Use evidence from within source_ranges." if value else "Use evidence from within source_ranges",
        FailureCategory.CLAIM_COPIES_EVIDENCE:
            "Rewrite claim in your own words; don't copy the evidence text",
        FailureCategory.TOO_FEW_CLAIMS:
            "Add more source-backed claims with evidence table rows",
        FailureCategory.INVALID_EVIDENCE_ID:
            "Remove invalid evidence ID or replace with a valid ID from the evidence bank",
        FailureCategory.FILE_SCOPE_VIOLATION:
            None,  # Ignore these - they're runner artifacts
    }
    return hints.get(category)


def parse_validation_output(output: str) -> list[ValidationFailure]:
    """Parse validation output into classified failures."""
    failures = []
    current_page = ""

    for line in output.splitlines():
        line = line.strip()

        # Track current page context
        page_match = re.search(r"(wiki/[\w/.-]+\.md)", line)
        if page_match:
            current_page = page_match.group(1)

        # Classify failure lines
        if "FAIL:" in line:
            failure = classify_failure(line, current_page)
            if failure:
                failures.append(failure)

    return failures


def group_failures_by_page(failures: list[ValidationFailure]) -> dict[str, list[ValidationFailure]]:
    """Group failures by page path."""
    by_page: dict[str, list[ValidationFailure]] = {}
    for f in failures:
        if f.page not in by_page:
            by_page[f.page] = []
        by_page[f.page].append(f)
    return by_page


def summarize_failures(failures: list[ValidationFailure]) -> str:
    """Generate a summary of failures for logging."""
    if not failures:
        return "No failures"

    by_category: dict[FailureCategory, int] = {}
    for f in failures:
        by_category[f.category] = by_category.get(f.category, 0) + 1

    deterministic = sum(1 for f in failures if f.deterministic_fix)
    semi = sum(1 for f in failures if f.semi_deterministic)
    llm_needed = sum(1 for f in failures if f.needs_llm)

    lines = [
        f"Total failures: {len(failures)}",
        f"  Deterministic fixes: {deterministic}",
        f"  Semi-deterministic: {semi}",
        f"  Needs LLM: {llm_needed}",
        "",
        "By category:",
    ]
    for cat, count in sorted(by_category.items(), key=lambda x: -x[1]):
        lines.append(f"  {cat.value}: {count}")

    return "\n".join(lines)


def main() -> int:
    """CLI for testing failure classification."""
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description="Classify validation failures")
    parser.add_argument("input", nargs="?",
                        help="Validation log file (or stdin)")
    parser.add_argument("--summary", action="store_true",
                        help="Show summary only")
    args = parser.parse_args()

    if args.input:
        output = Path(args.input).read_text()
    else:
        output = sys.stdin.read()

    failures = parse_validation_output(output)

    if args.summary:
        print(summarize_failures(failures))
    else:
        for f in failures:
            det = "DET" if f.deterministic_fix else (
                "SEMI" if f.semi_deterministic else "LLM")
            print(f"[{det}] {f.category.value}: {f.page}")
            print(f"  {f.message}")
            if f.fix_hint:
                print(f"  Hint: {f.fix_hint}")
            print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
