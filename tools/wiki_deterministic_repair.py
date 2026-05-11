#!/usr/bin/env python3
"""Deterministic repair functions for wiki pages.

These functions operate on WikiPageSchema objects and fix issues
without needing LLM intervention. After repairs, the page is
re-rendered to markdown.
"""
from __future__ import annotations

import re
from dataclasses import replace
from datetime import date
from pathlib import Path
from typing import TYPE_CHECKING

from wiki_failure_classifier import (
    FailureCategory,
    ValidationFailure,
    DETERMINISTIC_CATEGORIES,
)
from wiki_page_schema import (
    Claim,
    Frontmatter,
    Section,
    WikiPageSchema,
)

if TYPE_CHECKING:
    from wiki_phase2_benchmark import EvidenceBankResult


# Default values for missing frontmatter keys
FRONTMATTER_DEFAULTS = {
    "title": "Untitled",
    "type": "concept",
    "tags": [],
    "status": "draft",
    "last_updated": lambda: date.today().isoformat(),
    "sources": [],
    "source_ranges": [],
}


def repair_page(
    page: WikiPageSchema,
    failures: list[ValidationFailure],
    evidence_bank: "EvidenceBankResult | None",
    slug: str,
) -> tuple[WikiPageSchema, list[ValidationFailure]]:
    """
    Apply deterministic repairs to a page.

    Returns:
        Tuple of (repaired_page, remaining_failures)
        remaining_failures are those that couldn't be fixed deterministically
    """
    remaining: list[ValidationFailure] = []

    for failure in failures:
        if failure.category == FailureCategory.FRONTMATTER_MISSING_KEY:
            page = repair_frontmatter_missing_key(page, failure.field)
        elif failure.category == FailureCategory.FRONTMATTER_BAD_TYPE:
            page = repair_frontmatter_bad_type(page)
        elif failure.category == FailureCategory.FRONTMATTER_BAD_STATUS:
            page = repair_frontmatter_bad_status(page)
        elif failure.category == FailureCategory.MISSING_SOURCE_LINK:
            page = repair_missing_source_link(page, slug)
        elif failure.category == FailureCategory.MISSING_SOURCE_SECTION:
            page = repair_missing_source_section(page, slug)
        elif failure.category == FailureCategory.PLACEHOLDER_TEXT:
            page = repair_placeholder_text(page)
        elif failure.category == FailureCategory.EMPTY_SECTION:
            page = repair_empty_section(page, failure.field)
        elif failure.category == FailureCategory.BAD_SOURCE_CELL:
            # This is handled by the renderer now (always uses link format)
            pass
        elif failure.category == FailureCategory.FILE_SCOPE_VIOLATION:
            # Ignore these - they're runner artifacts, not page issues
            pass
        elif failure.category == FailureCategory.DUPLICATE_HEADING:
            page = repair_duplicate_heading(page, failure.field)
        elif failure.category == FailureCategory.BAD_LOCATOR_FORMAT:
            # Try to fix if we have evidence bank
            if evidence_bank and failure.row:
                page = repair_bad_locator(page, failure.row, evidence_bank)
            else:
                remaining.append(failure)
        elif failure.category == FailureCategory.LOCATOR_OUT_OF_RANGE:
            # Can suggest but needs content decision
            failure.fix_hint = suggest_in_range_evidence(
                page, failure.row, evidence_bank, slug
            )
            remaining.append(failure)
        elif failure.category in (
            FailureCategory.REFERENCE_TO_UNCREATED,
            FailureCategory.BROKEN_LINK,
        ):
            # Move uncreated page references from Related pages to Candidate pages
            page = repair_related_to_candidates(page)
        else:
            # Needs LLM
            remaining.append(failure)

    return page, remaining


def repair_frontmatter_missing_key(
    page: WikiPageSchema,
    key: str | None
) -> WikiPageSchema:
    """Add missing frontmatter key with sensible default."""
    if not key:
        return page

    default = FRONTMATTER_DEFAULTS.get(key)
    if default is None:
        return page

    value = default() if callable(default) else default

    # Create new frontmatter with the missing key
    fm_dict = {
        "title": page.frontmatter.title,
        "type": page.frontmatter.type,
        "tags": page.frontmatter.tags,
        "status": page.frontmatter.status,
        "last_updated": page.frontmatter.last_updated,
        "sources": page.frontmatter.sources,
        "source_ranges": page.frontmatter.source_ranges,
    }
    fm_dict[key] = value

    new_fm = Frontmatter(**fm_dict)
    return replace(page, frontmatter=new_fm)


def repair_frontmatter_bad_type(page: WikiPageSchema) -> WikiPageSchema:
    """Fix invalid type by inferring from path or defaulting to concept."""
    path = page.path
    if "entities/" in path:
        new_type = "entity"
    elif "procedures/" in path:
        new_type = "procedure"
    elif "references/" in path:
        new_type = "reference"
    elif "analyses/" in path:
        new_type = "analysis"
    elif "sources/" in path:
        new_type = "source"
    else:
        new_type = "concept"

    new_fm = replace(page.frontmatter, type=new_type)
    return replace(page, frontmatter=new_fm)


def repair_frontmatter_bad_status(page: WikiPageSchema) -> WikiPageSchema:
    """Fix invalid status by defaulting to draft."""
    new_fm = replace(page.frontmatter, status="draft")
    return replace(page, frontmatter=new_fm)


def repair_missing_source_link(page: WikiPageSchema, slug: str) -> WikiPageSchema:
    """Add source link to frontmatter if missing."""
    source_path = f"../sources/{slug}.md"

    if source_path not in page.frontmatter.sources:
        new_sources = list(page.frontmatter.sources) + [source_path]
        new_fm = replace(page.frontmatter, sources=new_sources)
        return replace(page, frontmatter=new_fm)

    return page


def repair_missing_source_section(page: WikiPageSchema, slug: str) -> WikiPageSchema:
    """Add Source pages section if missing."""
    # Check if we already have a source pages section
    has_source_section = any(
        "source" in s.heading.lower() and "backed" not in s.heading.lower()
        for s in page.sections
    )

    if not has_source_section:
        # Get title from slug for nicer display
        title = slug.replace("-", " ").title()
        new_section = Section(
            heading="Source pages",
            level=2,
            content=f"- [{title}](../sources/{slug}.md)"
        )
        new_sections = list(page.sections) + [new_section]
        return replace(page, sections=new_sections)

    return page


def repair_placeholder_text(page: WikiPageSchema) -> WikiPageSchema:
    """Remove placeholder text patterns."""
    placeholder_patterns = [
        r"Page title",
        r"Source-native group name",
        r"concrete evidence basis",
        r"not created yet",
    ]

    new_sections = []
    for section in page.sections:
        if section.content:
            new_content = section.content
            for pattern in placeholder_patterns:
                # Remove lines containing placeholders
                lines = new_content.splitlines()
                lines = [l for l in lines if not re.search(
                    pattern, l, re.IGNORECASE)]
                new_content = "\n".join(lines)

            # Clean up empty table rows
            new_content = re.sub(
                r"\n\|\s*\|\s*\|\s*\|\s*\|\s*\|\s*\|", "", new_content)
            new_content = new_content.strip()

            if new_content != section.content:
                section = replace(
                    section, content=new_content if new_content else "None.")

        new_sections.append(section)

    return replace(page, sections=new_sections)


def repair_empty_section(page: WikiPageSchema, heading: str | None) -> WikiPageSchema:
    """Fill empty section with 'None.' placeholder."""
    if not heading:
        return page

    new_sections = []
    for section in page.sections:
        if section.heading == heading and not section.content and not section.claims_table:
            section = replace(section, content="None.")
        new_sections.append(section)

    return replace(page, sections=new_sections)


def repair_duplicate_heading(page: WikiPageSchema, heading: str | None) -> WikiPageSchema:
    """Rename duplicate headings by adding suffix."""
    if not heading:
        return page

    seen: dict[str, int] = {}
    new_sections = []

    for section in page.sections:
        h = section.heading
        if h in seen:
            seen[h] += 1
            new_heading = f"{h} ({seen[h]})"
            section = replace(section, heading=new_heading)
        else:
            seen[h] = 1
        new_sections.append(section)

    return replace(page, sections=new_sections)


def repair_related_to_candidates(page: WikiPageSchema) -> WikiPageSchema:
    """Move uncreated page references from Related pages to Candidate pages.
    
    This handles two cases:
    1. "Page name (not created yet)" text references
    2. Markdown links to non-existent files
    
    Moves these to a Candidate pages section as plain text bullet points.
    """
    # Link pattern: [Link Text](../path/to/file.md)
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+\.md)\)")
    # "not created yet" pattern
    not_created_pattern = re.compile(r"([^-\n]+?)\s*\(not created yet\)", re.IGNORECASE)
    
    related_idx = None
    candidate_idx = None
    
    for i, section in enumerate(page.sections):
        if section.heading.lower() == "related pages":
            related_idx = i
        elif section.heading.lower() == "candidate pages":
            candidate_idx = i
    
    if related_idx is None:
        return page  # No Related pages section to repair
    
    related_section = page.sections[related_idx]
    if not related_section.content:
        return page
    
    # Extract uncreated pages
    uncreated_pages: list[str] = []
    valid_lines: list[str] = []
    
    for line in related_section.content.splitlines():
        line_modified = line
        has_broken_link = False
        
        # Check for broken links (links to files that don't exist)
        for match in link_pattern.finditer(line):
            link_text, link_path = match.groups()
            # Resolve relative to wiki/concepts (typical location)
            # We check from both common bases
            path_from_wiki = Path("wiki") / link_path.lstrip("../")
            path_from_concepts = Path("wiki/concepts") / link_path.lstrip("../")
            
            if not path_from_wiki.exists() and not path_from_concepts.exists():
                uncreated_pages.append(link_text.strip())
                # Remove the link from the line
                line_modified = line_modified.replace(match.group(0), "").strip()
                has_broken_link = True
        
        # Check for "not created yet" patterns
        for match in not_created_pattern.finditer(line_modified):
            page_name = match.group(1).strip()
            # Clean up bullet point or list marker
            page_name = re.sub(r"^[-*]\s*", "", page_name).strip()
            if page_name:
                uncreated_pages.append(page_name)
            # Remove the pattern from the line
            line_modified = line_modified.replace(match.group(0), "").strip()
        
        # Keep line if it still has content (valid links remaining)
        line_modified = line_modified.strip()
        # Remove empty bullet points
        if line_modified and line_modified not in ("-", "*", "•"):
            # Clean up lines that became just "- " or similar
            if re.match(r"^[-*•]\s*$", line_modified):
                continue
            valid_lines.append(line_modified)
    
    if not uncreated_pages:
        return page  # Nothing to move
    
    # Deduplicate uncreated pages
    seen = set()
    unique_uncreated = []
    for p in uncreated_pages:
        p_clean = p.strip()
        if p_clean and p_clean.lower() not in seen:
            seen.add(p_clean.lower())
            unique_uncreated.append(p_clean)
    
    # Build new sections list
    new_sections = list(page.sections)
    
    # Update Related pages section
    new_related_content = "\n".join(valid_lines) if valid_lines else "None."
    new_related = replace(related_section, content=new_related_content)
    new_sections[related_idx] = new_related
    
    # Build Candidate pages content
    candidate_content = "\n".join(f"- {p}" for p in unique_uncreated)
    
    if candidate_idx is not None:
        # Append to existing Candidate pages section
        existing = page.sections[candidate_idx]
        if existing.content and existing.content.strip() != "None.":
            candidate_content = existing.content.strip() + "\n" + candidate_content
        new_candidate = replace(existing, content=candidate_content)
        new_sections[candidate_idx] = new_candidate
    else:
        # Create new Candidate pages section after Related pages
        new_candidate = Section(
            heading="Candidate pages",
            level=2,
            content=candidate_content
        )
        # Insert after Related pages
        insert_idx = related_idx + 1
        new_sections.insert(insert_idx, new_candidate)
    
    return replace(page, sections=new_sections)


def repair_bad_locator(
    page: WikiPageSchema,
    row: int,
    evidence_bank: "EvidenceBankResult",
) -> WikiPageSchema:
    """Try to fix bad locator format using evidence bank."""
    if row < 1 or row > len(page.claims):
        return page

    claim = page.claims[row - 1]

    # Try to find valid locators from evidence bank for these IDs
    new_evidence_ids = []
    for eid in claim.evidence_ids:
        eid_upper = eid.upper()
        if eid_upper in evidence_bank.items:
            # The evidence bank has valid locators
            new_evidence_ids.append(eid_upper)

    if new_evidence_ids:
        new_claim = replace(claim, evidence_ids=new_evidence_ids)
        new_claims = list(page.claims)
        new_claims[row - 1] = new_claim
        return replace(page, claims=new_claims)

    return page


def suggest_in_range_evidence(
    page: WikiPageSchema,
    row: int | None,
    evidence_bank: "EvidenceBankResult | None",
    slug: str,
) -> str | None:
    """Suggest alternative evidence IDs that are within allowed range."""
    if not evidence_bank or not row or row > len(page.claims):
        return None

    # Parse source_ranges from frontmatter
    allowed_ranges: list[tuple[int, int]] = []
    for sr in page.frontmatter.source_ranges:
        match = re.search(r"L(\d+)(?:-L?(\d+))?", sr)
        if match:
            start = int(match.group(1))
            end = int(match.group(2)) if match.group(2) else start
            allowed_ranges.append((start, end))

    if not allowed_ranges:
        return None

    # Find evidence IDs within allowed ranges
    in_range_ids = []
    for eid, item in evidence_bank.items.items():
        match = re.search(r"L(\d+)", item.locator)
        if match:
            line = int(match.group(1))
            if any(start <= line <= end for start, end in allowed_ranges):
                in_range_ids.append(eid)

    if in_range_ids:
        return f"Consider using evidence IDs within allowed range: {', '.join(in_range_ids[:5])}"

    return None


def apply_repairs_and_render(
    page: WikiPageSchema,
    failures: list[ValidationFailure],
    evidence_bank: "EvidenceBankResult | None",
    slug: str,
    output_path: Path,
) -> tuple[list[ValidationFailure], bool]:
    """
    Apply repairs, render to markdown, and return remaining failures.

    Returns:
        Tuple of (remaining_failures, any_repairs_made)
    """
    from wiki_page_schema import render_page

    original_page = page
    repaired_page, remaining = repair_page(page, failures, evidence_bank, slug)

    any_repairs = repaired_page != original_page

    if any_repairs:
        markdown = render_page(repaired_page, evidence_bank, slug)
        output_path.write_text(markdown)

    return remaining, any_repairs


def main() -> int:
    """CLI for testing deterministic repairs."""
    import argparse
    import json
    import sys

    from wiki_page_schema import WikiPageSchema, render_page

    parser = argparse.ArgumentParser(
        description="Apply deterministic repairs to a page")
    parser.add_argument("json_file", help="JSON page file to repair")
    parser.add_argument("--slug", required=True, help="Source slug")
    parser.add_argument("--failures", help="Validation failures file")
    parser.add_argument("--output", help="Output markdown file")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show changes without writing")
    args = parser.parse_args()

    # Load page
    page_data = json.loads(Path(args.json_file).read_text())
    page = WikiPageSchema.from_json(page_data)

    # Load or create failures
    if args.failures:
        from wiki_failure_classifier import parse_validation_output
        failures = parse_validation_output(Path(args.failures).read_text())
    else:
        failures = []

    # Apply repairs
    repaired, remaining = repair_page(page, failures, None, args.slug)

    print(f"Original failures: {len(failures)}")
    print(f"Remaining after repair: {len(remaining)}")

    if args.dry_run:
        print("\nRepaired page would be:")
        print(render_page(repaired, None, args.slug))
    elif args.output:
        Path(args.output).write_text(render_page(repaired, None, args.slug))
        print(f"Wrote {args.output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
