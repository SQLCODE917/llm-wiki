#!/usr/bin/env python3
"""JSON schema for structured wiki page output.

The LLM outputs a JSON object conforming to WikiPageSchema.
Deterministic code renders it to markdown and expands evidence IDs.

Validation is split into two phases:
1. Schema validation (validate_schema_structured) - validates JSON structure
   - Runs BEFORE rendering
   - Failures indicate model issues (bad JSON, missing fields, wrong types)
   - Repair target: re-prompt model with specific field errors

2. Render validation (validate_rendered_page) - validates rendered markdown
   - Runs AFTER rendering
   - Failures indicate potential renderer bugs (malformed tables, broken links)
   - Repair target: fix the renderer, not the model

Benefits:
- Schema validation = instant, precise, identifies model errors
- Render validation = catches code bugs before wiki/ corruption
- Repair = patch specific fields, not re-prompt entire pages
- Evidence expansion = trivial lookup in claims array

TODO: Remove ValidationIssue and validate_schema() after callers migrate.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field, replace
from datetime import date
from typing import TYPE_CHECKING, Any, Literal

from wiki_failure_classifier import (
    FailureCategory,
    FailureSeverity,
    ValidationFailure,
    fail,
)

if TYPE_CHECKING:
    from wiki_phase2_benchmark import EvidenceBankResult


# -----------------------------------------------------------------------------
# Schema Types
# -----------------------------------------------------------------------------

@dataclass
class Frontmatter:
    """YAML frontmatter for a wiki page."""
    title: str
    type: Literal["source", "entity", "concept",
                  "procedure", "reference", "analysis"]
    tags: list[str] = field(default_factory=list)
    status: Literal["draft", "reviewed", "stable"] = "draft"
    last_updated: str = ""  # YYYY-MM-DD
    sources: list[str] = field(default_factory=list)
    source_ranges: list[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.last_updated:
            self.last_updated = date.today().isoformat()


@dataclass
class Section:
    """A section of the wiki page."""
    heading: str
    level: int = 2
    content: str | None = None  # Markdown content (paragraphs, lists, etc.)
    claims_table: bool = False  # If True, render claims table here


@dataclass
class Claim:
    """A source-backed claim with evidence ID references."""
    claim: str
    evidence_ids: list[str]  # e.g., ["E03", "E07"]


@dataclass
class WikiPageSchema:
    """Complete schema for a wiki page."""
    path: str  # e.g., "wiki/concepts/functions.md"
    frontmatter: Frontmatter
    sections: list[Section]
    claims: list[Claim]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "WikiPageSchema":
        """Parse from JSON dict (as output by LLM)."""
        fm_data = data.get("frontmatter", {})
        frontmatter = Frontmatter(
            title=fm_data.get("title", "Untitled"),
            type=fm_data.get("type", "concept"),
            tags=fm_data.get("tags", []),
            status=fm_data.get("status", "draft"),
            last_updated=fm_data.get("last_updated", ""),
            sources=fm_data.get("sources", []),
            source_ranges=fm_data.get("source_ranges", []),
        )

        sections = []
        for sec in data.get("sections", []):
            sections.append(Section(
                heading=sec.get("heading", ""),
                level=sec.get("level", 2),
                content=sec.get("content"),
                claims_table=sec.get("claims_table", False),
            ))

        claims = []
        for c in data.get("claims", []):
            claims.append(Claim(
                claim=c.get("claim", ""),
                evidence_ids=c.get("evidence_ids", []),
            ))

        return cls(
            path=data.get("path", ""),
            frontmatter=frontmatter,
            sections=sections,
            claims=claims,
        )


# -----------------------------------------------------------------------------
# Schema Validation (Pre-Render)
# -----------------------------------------------------------------------------

@dataclass
class ValidationIssue:
    """A schema validation issue (legacy, use ValidationFailure instead)."""
    field: str
    message: str
    severity: Literal["error", "warning"] = "error"


def validate_schema_structured(
    page: WikiPageSchema,
    evidence_bank: "EvidenceBankResult | None" = None,
) -> list[ValidationFailure]:
    """Validate a WikiPageSchema with structured failures.

    This is PRE-RENDER validation - it validates the JSON structure before
    the deterministic renderer runs. Failures here indicate model issues.

    Args:
        page: The parsed page schema
        evidence_bank: Evidence bank for validating evidence ID references

    Returns:
        List of ValidationFailure objects
    """
    failures: list[ValidationFailure] = []
    page_path = page.path or "<unknown>"

    # Path validation
    if not page.path:
        fail(failures, FailureCategory.FRONTMATTER_MISSING_KEY, page_path,
             "missing path in schema",
             field="path",
             fix_hint="Add path field to JSON output")
    elif not page.path.startswith("wiki/"):
        fail(failures, FailureCategory.FRONTMATTER_INVALID_VALUE, page_path,
             f"path must start with wiki/: {page.path}",
             field="path", value=page.path,
             fix_hint="Path should be wiki/concepts/name.md or similar")
    elif not page.path.endswith(".md"):
        fail(failures, FailureCategory.FRONTMATTER_INVALID_VALUE, page_path,
             f"path must end with .md: {page.path}",
             field="path", value=page.path,
             fix_hint="Path should end with .md")

    # Frontmatter validation
    if not page.frontmatter.title:
        fail(failures, FailureCategory.FRONTMATTER_MISSING_KEY, page_path,
             "missing title in frontmatter",
             field="frontmatter.title",
             fix_hint="Add title to frontmatter")

    valid_types = ("source", "entity", "concept",
                   "procedure", "reference", "analysis")
    if page.frontmatter.type not in valid_types:
        fail(failures, FailureCategory.FRONTMATTER_INVALID_VALUE, page_path,
             f"invalid type: {page.frontmatter.type}",
             field="frontmatter.type", value=page.frontmatter.type, expected=list(valid_types),
             fix_hint=f"Type must be one of: {', '.join(valid_types)}")

    if not page.frontmatter.sources and page.frontmatter.type != "source":
        fail(failures, FailureCategory.FRONTMATTER_MISSING_KEY, page_path,
             "synthesized pages must have sources",
             field="frontmatter.sources",
             severity=FailureSeverity.WARNING,
             fix_hint="Add source page paths to frontmatter.sources")

    # Section validation
    has_claims_section = False
    for i, sec in enumerate(page.sections):
        if not sec.heading:
            fail(failures, FailureCategory.EMPTY_SECTION, page_path,
                 f"section {i} has empty heading",
                 field=f"sections[{i}].heading",
                 fix_hint="Add heading text to section")
        if sec.claims_table:
            has_claims_section = True

    # Claims validation
    if page.claims and not has_claims_section:
        fail(failures, FailureCategory.STRUCTURE_VIOLATION, page_path,
             "claims exist but no section has claims_table=true",
             field="sections",
             fix_hint="Set claims_table: true on the Source-backed details section")

    for i, claim in enumerate(page.claims):
        if not claim.claim:
            fail(failures, FailureCategory.CLAIM_TOO_SHORT, page_path,
                 f"claim {i} has empty text",
                 row=i, field=f"claims[{i}].claim",
                 fix_hint="Add claim text")
        if not claim.evidence_ids:
            fail(failures, FailureCategory.INVALID_EVIDENCE_ID, page_path,
                 f"claim {i} has no evidence IDs",
                 row=i, field=f"claims[{i}].evidence_ids",
                 fix_hint="Add evidence_ids array with IDs like [\"E01\", \"E03\"]")
        elif evidence_bank:
            # Validate evidence IDs exist in bank
            for eid in claim.evidence_ids:
                eid_upper = eid.upper()
                if eid_upper not in evidence_bank.items:
                    fail(failures, FailureCategory.INVALID_EVIDENCE_ID, page_path,
                         f"claim {i} references unknown evidence ID: {eid}",
                         row=i, field=f"claims[{i}].evidence_ids", value=eid,
                         fix_hint=f"Use only evidence IDs from the evidence bank")

    # Type-specific validation
    if page.frontmatter.type == "procedure":
        has_steps = any("step" in sec.heading.lower() for sec in page.sections)
        if not has_steps:
            fail(failures, FailureCategory.MISSING_REQUIRED_SECTION, page_path,
                 "procedure pages require ## Steps section",
                 field="sections",
                 severity=FailureSeverity.WARNING,
                 fix_hint="Add a section with heading 'Steps'")

    if page.frontmatter.type == "reference":
        has_reference = any("reference" in sec.heading.lower()
                            for sec in page.sections)
        if not has_reference:
            fail(failures, FailureCategory.MISSING_REQUIRED_SECTION, page_path,
                 "reference pages require ## Reference data section",
                 field="sections",
                 severity=FailureSeverity.WARNING,
                 fix_hint="Add a section with heading 'Reference data'")

    return failures


def validate_schema(page: WikiPageSchema) -> list[ValidationIssue]:
    """Legacy wrapper - use validate_schema_structured instead."""
    structured = validate_schema_structured(page)
    issues: list[ValidationIssue] = []
    for f in structured:
        severity: Literal["error", "warning"] = (
            "warning" if f.severity == FailureSeverity.WARNING else "error"
        )
        issues.append(ValidationIssue(
            field=f.field or "unknown",
            message=f.message,
            severity=severity,
        ))
    return issues


# -----------------------------------------------------------------------------
# Render Validation (Post-Render)
# -----------------------------------------------------------------------------

def validate_rendered_page(
    markdown: str,
    page: WikiPageSchema,
    evidence_bank: "EvidenceBankResult | None" = None,
) -> list[ValidationFailure]:
    """Validate rendered markdown for potential renderer bugs.

    This is POST-RENDER validation - it validates the markdown output
    from the deterministic renderer. Failures here indicate CODE BUGS
    in the renderer, not model issues.

    If this function ever returns failures, it's a signal to fix
    render_page(), not to re-prompt the model.

    Args:
        markdown: The rendered markdown content
        page: The original schema (for cross-reference)
        evidence_bank: Evidence bank used during rendering

    Returns:
        List of ValidationFailure objects (ideally empty)
    """
    failures: list[ValidationFailure] = []
    page_path = page.path or "<unknown>"

    # Check frontmatter was rendered
    if not markdown.startswith("---"):
        fail(failures, FailureCategory.MALFORMED_TABLE, page_path,
             "rendered page missing YAML frontmatter",
             field="frontmatter",
             fix_hint="RENDERER BUG: render_frontmatter() failed")

    # Check H1 title present
    if f"# {page.frontmatter.title}" not in markdown:
        fail(failures, FailureCategory.MISSING_H1_TITLE, page_path,
             f"rendered page missing H1 title: {page.frontmatter.title}",
             field="title",
             fix_hint="RENDERER BUG: title not rendered")

    # Check all sections were rendered
    for sec in page.sections:
        heading_prefix = "#" * sec.level
        expected_heading = f"{heading_prefix} {sec.heading}"
        if sec.heading and expected_heading not in markdown:
            fail(failures, FailureCategory.MISSING_REQUIRED_SECTION, page_path,
                 f"rendered page missing section: {sec.heading}",
                 field=f"section:{sec.heading}",
                 fix_hint=f"RENDERER BUG: section '{sec.heading}' not rendered")

    # Check claims table structure if claims exist
    if page.claims:
        # Should have 4-column header
        table_header = "| Claim | Evidence | Locator | Source |"
        if table_header not in markdown:
            fail(failures, FailureCategory.MALFORMED_TABLE, page_path,
                 "claims table missing expected 4-column header",
                 field="claims_table",
                 fix_hint="RENDERER BUG: render_claims_table() header wrong")

        # Each claim should appear in the table
        for i, claim in enumerate(page.claims):
            # Claims may have pipes escaped
            claim_text = claim.claim.replace("|", "\\|")
            if claim_text[:30] not in markdown:
                fail(failures, FailureCategory.MALFORMED_TABLE, page_path,
                     f"claim {i} not found in rendered output",
                     row=i, field=f"claims[{i}]",
                     fix_hint=f"RENDERER BUG: claim {i} not rendered")

    # Check evidence IDs were expanded (not left as [E01])
    evidence_id_pattern = r'\[E\d{2}\]'
    unexpanded = re.findall(evidence_id_pattern, markdown)
    if unexpanded:
        fail(failures, FailureCategory.INVALID_EVIDENCE_ID, page_path,
             f"rendered page contains unexpanded evidence IDs: {unexpanded[:3]}",
             field="evidence_ids",
             fix_hint=f"RENDERER BUG: {len(unexpanded)} evidence IDs not expanded")

    return failures


# -----------------------------------------------------------------------------
# Markdown Renderer
# -----------------------------------------------------------------------------

def render_frontmatter(fm: Frontmatter) -> str:
    """Render frontmatter to YAML."""
    lines = ["---"]
    lines.append(f"title: {fm.title}")
    lines.append(f"type: {fm.type}")

    if fm.tags:
        lines.append(f"tags: [{', '.join(fm.tags)}]")
    else:
        lines.append("tags: []")

    lines.append(f"status: {fm.status}")
    lines.append(f"last_updated: {fm.last_updated}")

    if fm.sources:
        lines.append("sources:")
        for src in fm.sources:
            lines.append(f"  - {src}")
    else:
        lines.append("sources: []")

    if fm.source_ranges:
        lines.append("source_ranges:")
        for sr in fm.source_ranges:
            lines.append(f"  - {sr}")

    lines.append("---")
    return "\n".join(lines)


def make_table_safe(text: str, max_len: int = 200) -> str:
    """Make text safe for markdown table cells.

    - Collapses all whitespace (including newlines) to single spaces
    - Escapes pipe characters
    - Truncates long text with ellipsis
    """
    # Collapse all whitespace to single spaces
    safe = " ".join(text.split())
    # Escape pipe characters
    safe = safe.replace("|", "\\|")
    # Truncate if too long
    if len(safe) > max_len:
        safe = safe[:max_len - 3].rsplit(" ", 1)[0] + "..."
    return safe


def render_claims_table(
    claims: list[Claim],
    evidence_bank: "EvidenceBankResult | None",
    slug: str,
) -> str:
    """Render claims as a 4-column evidence table.

    Each claim-evidence pair gets its own row. If a claim has multiple
    evidence IDs, it's expanded into multiple rows.
    """
    if not claims:
        return "No claims."

    lines = ["| Claim | Evidence | Locator | Source |"]
    lines.append("| --- | --- | --- | --- |")

    source_cell = f"[Source](../sources/{slug}.md)" if slug else ""

    for claim in claims:
        claim_text = make_table_safe(claim.claim)

        if not claim.evidence_ids:
            # Claim without evidence
            lines.append(f"| {claim_text} | N/A | N/A | {source_cell} |")
            continue

        # One row per evidence ID
        for eid in claim.evidence_ids:
            eid_upper = eid.upper()
            if evidence_bank and eid_upper in evidence_bank.items:
                item = evidence_bank.items[eid_upper]
                evidence_cell = f'"{make_table_safe(item.text)}"'
                locator_cell = f"`{item.locator}`"
            else:
                evidence_cell = f"[{eid}: not found]"
                locator_cell = "N/A"

            lines.append(
                f"| {claim_text} | {evidence_cell} | {locator_cell} | {source_cell} |")

    return "\n".join(lines)


def render_section(
    section: Section,
    claims: list[Claim],
    evidence_bank: "EvidenceBankResult | None",
    slug: str,
) -> str:
    """Render a section to markdown."""
    heading_prefix = "#" * section.level
    lines = [f"{heading_prefix} {section.heading}"]
    lines.append("")

    if section.claims_table:
        lines.append(render_claims_table(claims, evidence_bank, slug))
    elif section.content:
        lines.append(section.content)
    else:
        lines.append("None.")

    lines.append("")
    return "\n".join(lines)


def compute_source_ranges(
    claims: list[Claim],
    evidence_bank: "EvidenceBankResult | None",
    slug: str,
) -> list[str]:
    """Compute source_ranges from evidence IDs used in claims.

    Returns list of source ranges like 'slug:normalized:L123-L123'.
    """
    if not evidence_bank:
        return []

    locators = set()
    for claim in claims:
        for eid in claim.evidence_ids:
            eid_upper = eid.upper()
            if eid_upper in evidence_bank.items:
                item = evidence_bank.items[eid_upper]
                locators.add(item.locator)

    # Convert locators to source_ranges format
    ranges = []
    for loc in sorted(locators):
        # Parse the locator to extract line numbers
        match = re.search(r'L(\d+)(?:-L(\d+))?', loc)
        if match:
            start = int(match.group(1))
            end = int(match.group(2)) if match.group(2) else start
            ranges.append(f"{slug}:normalized:L{start}-L{end}")

    return ranges


def render_page(
    page: WikiPageSchema,
    evidence_bank: "EvidenceBankResult | None" = None,
    slug: str = "",
) -> str:
    """Render a WikiPageSchema to markdown.

    Args:
        page: The parsed page schema
        evidence_bank: Evidence bank for expanding IDs to full evidence
        slug: Source slug for generating source links

    Returns:
        Complete markdown page content
    """
    parts: list[str] = []

    # Fix source_ranges to match evidence IDs used
    frontmatter = page.frontmatter
    if evidence_bank and slug and page.claims:
        correct_ranges = compute_source_ranges(
            page.claims, evidence_bank, slug)
        if correct_ranges:
            frontmatter = replace(frontmatter, source_ranges=correct_ranges)

    # Frontmatter
    parts.append(render_frontmatter(frontmatter))
    parts.append("")

    # Title
    parts.append(f"# {frontmatter.title}")
    parts.append("")

    # Sections
    for section in page.sections:
        parts.append(render_section(section, page.claims, evidence_bank, slug))

    return "\n".join(parts)


# -----------------------------------------------------------------------------
# JSON Parsing from LLM Output
# -----------------------------------------------------------------------------

def extract_json_from_response(response: str) -> dict[str, Any] | None:
    """Extract JSON object from LLM response.

    Handles:
    - Pure JSON response
    - JSON in ```json code block
    - JSON with preamble/postamble text
    """
    # Try pure JSON first
    try:
        return json.loads(response.strip())
    except json.JSONDecodeError:
        pass

    # Try to extract from code block
    json_block = re.search(r"```(?:json)?\s*\n(.*?)\n```", response, re.DOTALL)
    if json_block:
        try:
            return json.loads(json_block.group(1))
        except json.JSONDecodeError:
            pass

    # Try to find JSON object in text
    # Look for first { and last }
    first_brace = response.find("{")
    last_brace = response.rfind("}")
    if first_brace != -1 and last_brace != -1 and last_brace > first_brace:
        try:
            return json.loads(response[first_brace:last_brace + 1])
        except json.JSONDecodeError:
            pass

    return None


def parse_llm_response(
    response: str,
    evidence_bank: "EvidenceBankResult | None" = None,
    slug: str = "",
) -> tuple[str, WikiPageSchema | None, list[ValidationIssue]]:
    """Parse LLM JSON response and render to markdown (legacy wrapper).

    Use parse_llm_response_structured() for new code.

    Returns:
        Tuple of (markdown_content, parsed_schema, validation_issues)
        If parsing fails, returns (error_message, None, [error_issue])
    """
    data = extract_json_from_response(response)
    if data is None:
        return (
            "",
            None,
            [ValidationIssue(
                "response", "Could not extract JSON from response")],
        )

    try:
        page = WikiPageSchema.from_json(data)
    except Exception as e:
        return (
            "",
            None,
            [ValidationIssue("schema", f"Schema parsing failed: {e}")],
        )

    issues = validate_schema(page)
    errors = [i for i in issues if i.severity == "error"]

    if errors:
        # Return empty content but include the parsed schema for repair
        return ("", page, issues)

    markdown = render_page(page, evidence_bank, slug)
    return (markdown, page, issues)


@dataclass
class ParseResult:
    """Result of parsing LLM response with structured validation."""
    markdown: str
    schema: WikiPageSchema | None
    schema_failures: list[ValidationFailure]
    render_failures: list[ValidationFailure]

    @property
    def success(self) -> bool:
        """True if no error-level failures in schema validation."""
        return not any(
            f.severity == FailureSeverity.ERROR
            for f in self.schema_failures
        )

    @property
    def all_failures(self) -> list[ValidationFailure]:
        """All failures from both schema and render validation."""
        return self.schema_failures + self.render_failures

    @property
    def has_renderer_bugs(self) -> bool:
        """True if any render validation failures exist."""
        return len(self.render_failures) > 0


def parse_llm_response_structured(
    response: str,
    evidence_bank: "EvidenceBankResult | None" = None,
    slug: str = "",
) -> ParseResult:
    """Parse LLM JSON response with structured validation split.

    Validation phases:
    1. JSON extraction - can we find valid JSON?
    2. Schema parsing - does the JSON match WikiPageSchema?
    3. Schema validation - are all required fields present and valid?
    4. Rendering - convert schema to markdown
    5. Render validation - is the rendered markdown well-formed?

    Phase 1-3 failures indicate model issues (re-prompt needed).
    Phase 5 failures indicate renderer bugs (code fix needed).

    Args:
        response: Raw LLM output string
        evidence_bank: Evidence bank for expanding IDs
        slug: Source slug for generating source links

    Returns:
        ParseResult with markdown, schema, and categorized failures
    """
    # Phase 1: JSON extraction
    data = extract_json_from_response(response)
    if data is None:
        return ParseResult(
            markdown="",
            schema=None,
            schema_failures=[ValidationFailure(
                category=FailureCategory.FRONTMATTER_PARSE_ERROR,
                page="<response>",
                message="Could not extract JSON from response",
                fix_hint="Model output must be valid JSON or JSON in ```json block",
            )],
            render_failures=[],
        )

    # Phase 2: Schema parsing
    try:
        page = WikiPageSchema.from_json(data)
    except Exception as e:
        return ParseResult(
            markdown="",
            schema=None,
            schema_failures=[ValidationFailure(
                category=FailureCategory.FRONTMATTER_PARSE_ERROR,
                page="<response>",
                message=f"Schema parsing failed: {e}",
                fix_hint="JSON structure doesn't match WikiPageSchema",
            )],
            render_failures=[],
        )

    # Phase 3: Schema validation (pre-render)
    schema_failures = validate_schema_structured(page, evidence_bank)
    errors = [f for f in schema_failures if f.severity == FailureSeverity.ERROR]

    if errors:
        # Don't render if schema has errors - return schema for repair
        return ParseResult(
            markdown="",
            schema=page,
            schema_failures=schema_failures,
            render_failures=[],
        )

    # Phase 4: Rendering
    markdown = render_page(page, evidence_bank, slug)

    # Phase 5: Render validation (post-render)
    render_failures = validate_rendered_page(markdown, page, evidence_bank)

    return ParseResult(
        markdown=markdown,
        schema=page,
        schema_failures=schema_failures,
        render_failures=render_failures,
    )


# -----------------------------------------------------------------------------
# CLI for Testing
# -----------------------------------------------------------------------------

def main() -> int:
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description="Test JSON schema parsing and rendering")
    parser.add_argument("json_file", help="JSON file to parse")
    parser.add_argument("--slug", default="", help="Source slug for links")
    parser.add_argument("--validate-only", action="store_true",
                        help="Only validate, don't render")
    args = parser.parse_args()

    from pathlib import Path

    json_path = Path(args.json_file)
    if not json_path.exists():
        print(f"File not found: {json_path}", file=sys.stderr)
        return 1

    data = json.loads(json_path.read_text())
    page = WikiPageSchema.from_json(data)

    issues = validate_schema(page)
    if issues:
        print("Validation issues:")
        for issue in issues:
            print(f"  [{issue.severity}] {issue.field}: {issue.message}")

    if args.validate_only:
        errors = [i for i in issues if i.severity == "error"]
        return 1 if errors else 0

    markdown = render_page(page, evidence_bank=None, slug=args.slug)
    print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
