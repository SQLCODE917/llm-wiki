#!/usr/bin/env python3
"""Classify validation failures into categories for targeted repair.

Each failure is classified into a category that determines:
1. Whether it can be fixed deterministically (no LLM needed)
2. What specific repair function to use
3. What hints to provide if LLM repair is needed
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class FailureCategory(Enum):
    """Categories of validation failures."""

    # Deterministically fixable - frontmatter
    FRONTMATTER_MISSING_KEY = "frontmatter_missing_key"
    FRONTMATTER_BAD_TYPE = "frontmatter_bad_type"
    FRONTMATTER_BAD_STATUS = "frontmatter_bad_status"

    # Deterministically fixable - structure
    MISSING_SOURCE_LINK = "missing_source_link"
    MISSING_SOURCE_SECTION = "missing_source_section"
    PLACEHOLDER_TEXT = "placeholder_text"
    EMPTY_SECTION = "empty_section"
    DUPLICATE_HEADING = "duplicate_heading"
    MISSING_H1_TITLE = "missing_h1_title"

    # Deterministically fixable - table format
    MALFORMED_TABLE = "malformed_table"
    BAD_LOCATOR_FORMAT = "bad_locator_format"
    BAD_SOURCE_CELL = "bad_source_cell"

    # Partially deterministic - can suggest fixes
    LOCATOR_OUT_OF_RANGE = "locator_out_of_range"
    EVIDENCE_MISMATCH = "evidence_mismatch"
    EVIDENCE_NOT_IN_LOCATOR = "evidence_not_in_locator"

    # Requires LLM
    TOO_FEW_CLAIMS = "too_few_claims"
    CLAIM_TOO_SHORT = "claim_too_short"
    CLAIM_COPIES_EVIDENCE = "claim_copies_evidence"
    WEAK_CLAIM_TEXT = "weak_claim_text"
    UNSUPPORTED_CLAIM = "unsupported_claim"
    EVIDENCE_TOO_SHORT = "evidence_too_short"
    WEAK_EVIDENCE = "weak_evidence"

    # Structural issues requiring content decisions
    MISSING_STEPS_SECTION = "missing_steps_section"
    MISSING_REFERENCE_DATA = "missing_reference_data"
    UNCREATED_CANDIDATE_MENTION = "uncreated_candidate_mention"

    # File scope issues (runner artifacts, not page content)
    FILE_SCOPE_VIOLATION = "file_scope_violation"

    # Unknown
    UNKNOWN = "unknown"


# Categories that can be fixed without LLM
DETERMINISTIC_CATEGORIES = {
    FailureCategory.FRONTMATTER_MISSING_KEY,
    FailureCategory.FRONTMATTER_BAD_TYPE,
    FailureCategory.FRONTMATTER_BAD_STATUS,
    FailureCategory.MISSING_SOURCE_LINK,
    FailureCategory.MISSING_SOURCE_SECTION,
    FailureCategory.PLACEHOLDER_TEXT,
    FailureCategory.EMPTY_SECTION,
    FailureCategory.BAD_SOURCE_CELL,
    FailureCategory.FILE_SCOPE_VIOLATION,  # Ignore these
}

# Categories that can suggest fixes but may need LLM
SEMI_DETERMINISTIC_CATEGORIES = {
    FailureCategory.LOCATOR_OUT_OF_RANGE,
    FailureCategory.EVIDENCE_MISMATCH,
    FailureCategory.EVIDENCE_NOT_IN_LOCATOR,
    FailureCategory.BAD_LOCATOR_FORMAT,
    FailureCategory.DUPLICATE_HEADING,
}


@dataclass
class ValidationFailure:
    """A classified validation failure."""
    category: FailureCategory
    page: str
    message: str
    row: int | None = None  # For row-specific failures
    field: str | None = None  # For field-specific failures
    value: str | None = None  # Current problematic value
    expected: str | None = None  # Expected value or format
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
    def needs_llm(self) -> bool:
        """Whether this failure requires LLM to fix."""
        return not self.deterministic_fix and not self.semi_deterministic


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
    """Classify a single validation failure line."""

    # Skip non-failure lines
    if not line.strip().startswith("FAIL:"):
        return None

    # Extract page path if present
    page_match = re.search(r"FAIL:\s*([\w/.-]+\.md):", line)
    if page_match:
        page = page_match.group(1)

    # Try each pattern
    for pattern, (category, extract_type) in PATTERNS.items():
        match = re.search(pattern, line, re.IGNORECASE)
        if match:
            failure = ValidationFailure(
                category=category,
                page=page,
                message=line.replace("FAIL:", "").strip(),
            )

            # Extract additional info based on pattern type
            if extract_type == "field" and match.groups():
                failure.field = match.group(1)
            elif extract_type == "row" and match.groups():
                failure.row = int(match.group(1))
            elif extract_type == "row_value" and len(match.groups()) >= 2:
                failure.row = int(match.group(1))
                failure.value = match.group(2)
            elif extract_type == "value" and match.groups():
                failure.value = match.group(1)

            # Add fix hints for deterministic categories
            failure.fix_hint = get_fix_hint(failure)

            return failure

    # Unknown failure type
    return ValidationFailure(
        category=FailureCategory.UNKNOWN,
        page=page,
        message=line.replace("FAIL:", "").strip(),
    )


def get_fix_hint(failure: ValidationFailure) -> str | None:
    """Get a specific fix hint for the failure."""
    hints = {
        FailureCategory.FRONTMATTER_MISSING_KEY:
            f"Add '{failure.field}' to frontmatter with appropriate default",
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
            f"Locator {failure.value} is outside allowed range. Use evidence from within source_ranges.",
        FailureCategory.CLAIM_COPIES_EVIDENCE:
            "Rewrite claim in your own words; don't copy the evidence text",
        FailureCategory.TOO_FEW_CLAIMS:
            "Add more source-backed claims with evidence table rows",
        FailureCategory.FILE_SCOPE_VIOLATION:
            None,  # Ignore these - they're runner artifacts
    }
    return hints.get(failure.category)


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
