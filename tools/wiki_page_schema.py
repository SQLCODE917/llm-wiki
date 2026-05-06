#!/usr/bin/env python3
"""JSON schema for structured wiki page output.

The LLM outputs a JSON object conforming to WikiPageSchema.
Deterministic code renders it to markdown and expands evidence IDs.

Benefits:
- Validation = schema validation (instant, precise)
- Repair = patch specific fields, not re-prompt entire pages
- Evidence expansion = trivial lookup in claims array
- No markdown parsing errors
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import date
from typing import TYPE_CHECKING, Any, Literal

if TYPE_CHECKING:
    from wiki_phase2_benchmark import EvidenceBankResult


# -----------------------------------------------------------------------------
# Schema Types
# -----------------------------------------------------------------------------

@dataclass
class Frontmatter:
    """YAML frontmatter for a wiki page."""
    title: str
    type: Literal["source", "entity", "concept", "procedure", "reference", "analysis"]
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
# Schema Validation
# -----------------------------------------------------------------------------

@dataclass
class ValidationIssue:
    """A schema validation issue."""
    field: str
    message: str
    severity: Literal["error", "warning"] = "error"


def validate_schema(page: WikiPageSchema) -> list[ValidationIssue]:
    """Validate a WikiPageSchema for completeness and correctness."""
    issues: list[ValidationIssue] = []
    
    # Path validation
    if not page.path:
        issues.append(ValidationIssue("path", "Missing path"))
    elif not page.path.startswith("wiki/"):
        issues.append(ValidationIssue("path", f"Path must start with wiki/: {page.path}"))
    elif not page.path.endswith(".md"):
        issues.append(ValidationIssue("path", f"Path must end with .md: {page.path}"))
    
    # Frontmatter validation
    if not page.frontmatter.title:
        issues.append(ValidationIssue("frontmatter.title", "Missing title"))
    
    if page.frontmatter.type not in ("source", "entity", "concept", "procedure", "reference", "analysis"):
        issues.append(ValidationIssue("frontmatter.type", f"Invalid type: {page.frontmatter.type}"))
    
    if not page.frontmatter.sources and page.frontmatter.type != "source":
        issues.append(ValidationIssue("frontmatter.sources", "Synthesized pages must have sources", "warning"))
    
    # Section validation
    has_claims_section = False
    for i, sec in enumerate(page.sections):
        if not sec.heading:
            issues.append(ValidationIssue(f"sections[{i}].heading", "Missing heading"))
        if sec.claims_table:
            has_claims_section = True
    
    # Claims validation
    if page.claims and not has_claims_section:
        issues.append(ValidationIssue("sections", "Claims exist but no section has claims_table=true"))
    
    for i, claim in enumerate(page.claims):
        if not claim.claim:
            issues.append(ValidationIssue(f"claims[{i}].claim", "Empty claim text"))
        if not claim.evidence_ids:
            issues.append(ValidationIssue(f"claims[{i}].evidence_ids", "Claim has no evidence IDs"))
    
    # Type-specific validation
    if page.frontmatter.type == "procedure":
        has_steps = any("step" in sec.heading.lower() for sec in page.sections)
        if not has_steps:
            issues.append(ValidationIssue("sections", "Procedure pages require ## Steps section", "warning"))
    
    if page.frontmatter.type == "reference":
        has_reference = any("reference" in sec.heading.lower() for sec in page.sections)
        if not has_reference:
            issues.append(ValidationIssue("sections", "Reference pages require ## Reference data section", "warning"))
    
    return issues


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


def render_claims_table(
    claims: list[Claim],
    evidence_bank: "EvidenceBankResult | None",
    slug: str,
) -> str:
    """Render claims as a 4-column evidence table."""
    if not claims:
        return "No claims."
    
    lines = ["| Claim | Evidence | Locator | Source |"]
    lines.append("| --- | --- | --- | --- |")
    
    for claim in claims:
        claim_text = claim.claim
        
        # Collect evidence for all IDs
        evidence_parts: list[str] = []
        locator_parts: list[str] = []
        
        for eid in claim.evidence_ids:
            eid_upper = eid.upper()
            if evidence_bank and eid_upper in evidence_bank.items:
                item = evidence_bank.items[eid_upper]
                evidence_parts.append(f'"{item.text}"')
                locator_parts.append(f"`{item.locator}`")
            else:
                evidence_parts.append(f"[{eid}: not found]")
                locator_parts.append("")
        
        evidence_cell = " ".join(evidence_parts) if evidence_parts else "N/A"
        locator_cell = " ".join(locator_parts) if locator_parts else "N/A"
        source_cell = f"[Source](../sources/{slug}.md)" if slug else ""
        
        # Escape pipes in claim text
        claim_text = claim_text.replace("|", "\\|")
        evidence_cell = evidence_cell.replace("|", "\\|")
        
        lines.append(f"| {claim_text} | {evidence_cell} | {locator_cell} | {source_cell} |")
    
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
    
    # Frontmatter
    parts.append(render_frontmatter(page.frontmatter))
    parts.append("")
    
    # Title
    parts.append(f"# {page.frontmatter.title}")
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
    """Parse LLM JSON response and render to markdown.
    
    Returns:
        Tuple of (markdown_content, parsed_schema, validation_issues)
        If parsing fails, returns (error_message, None, [error_issue])
    """
    data = extract_json_from_response(response)
    if data is None:
        return (
            "",
            None,
            [ValidationIssue("response", "Could not extract JSON from response")],
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


# -----------------------------------------------------------------------------
# CLI for Testing
# -----------------------------------------------------------------------------

def main() -> int:
    import argparse
    import sys
    
    parser = argparse.ArgumentParser(description="Test JSON schema parsing and rendering")
    parser.add_argument("json_file", help="JSON file to parse")
    parser.add_argument("--slug", default="", help="Source slug for links")
    parser.add_argument("--validate-only", action="store_true", help="Only validate, don't render")
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
