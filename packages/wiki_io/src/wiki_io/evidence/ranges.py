"""Source range utilities for wiki ingestion pipeline.

Handles parsing and validation of source locators like `normalized:L12-L34`.

Usage:
    from wiki_io.evidence import SourceRange, normalize_locator, parse_locator_range
    
    range_obj = SourceRange(start=12, end=34, source="normalized")
    locator = normalize_locator("L12-34")  # Returns "normalized:L12-L34"
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


# Patterns for parsing locators
RANGE_RE = re.compile(
    r"^(?:(?P<prefix>[A-Za-z0-9_-]+):)?normalized:L(?P<start>\d+)(?:-L?(?P<end>\d+))?$",
    re.IGNORECASE,
)

SIMPLE_LINE_RE = re.compile(r"^L?(\d+)(?:-L?(\d+))?$", re.IGNORECASE)

HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.+?)\s*$")

# Maximum line slop for off-by-one tolerance
MAX_LOCATOR_SLOP = 2


@dataclass(frozen=True)
class SourceRange:
    """A range within a normalized source file."""
    start: int  # 1-indexed
    end: int    # 1-indexed, inclusive
    source: str = "normalized"  # Usually "normalized" or a source slug
    reason: str = ""  # Why this range was selected (for debugging)


@dataclass(frozen=True)
class SourceRangeResult:
    """Result of source range lookup for a page."""
    ranges: list[SourceRange]
    invalid: list[str]
    declared: bool  # True if from frontmatter, False if derived from headings


@dataclass(frozen=True)
class SourceHeading:
    """A heading found in the source document."""
    line: int
    level: int
    raw_title: str
    clean_title: str


def normalize_locator(locator: str) -> str:
    """Normalize a locator to canonical format.

    Examples:
        "L12" -> "normalized:L12"
        "L12-34" -> "normalized:L12-L34"
        "normalized:L12-L34" -> "normalized:L12-L34"
        "`normalized:L12`" -> "normalized:L12"
    """
    stripped = locator.strip().strip("`")

    # Handle shorthand formats
    match = SIMPLE_LINE_RE.match(stripped)
    if match:
        start = int(match.group(1))
        end = match.group(2)
        if end:
            return f"normalized:L{start}-L{int(end)}"
        return f"normalized:L{start}"

    # Handle full format
    match = RANGE_RE.match(stripped)
    if match:
        prefix = match.group("prefix") or ""
        start = int(match.group("start"))
        end = match.group("end")

        base = f"{prefix}:normalized" if prefix else "normalized"
        if end:
            return f"{base}:L{start}-L{int(end)}"
        return f"{base}:L{start}"

    # Return as-is if not recognized
    return stripped


def parse_locator_range(locator: str) -> SourceRange | None:
    """Parse a locator string into a SourceRange.

    Returns None if locator cannot be parsed.
    """
    stripped = locator.strip().strip("`")

    # Handle shorthand
    match = SIMPLE_LINE_RE.match(stripped)
    if match:
        start = int(match.group(1))
        end = int(match.group(2)) if match.group(2) else start
        return SourceRange(start=start, end=end, source="normalized")

    # Handle full format
    match = RANGE_RE.match(stripped)
    if match:
        prefix = match.group("prefix") or ""
        start = int(match.group("start"))
        end = int(match.group("end")) if match.group("end") else start
        source = f"{prefix}:normalized" if prefix else "normalized"
        return SourceRange(start=start, end=end, source=source)

    return None


def locator_to_range(locator: str) -> tuple[int, int] | None:
    """Parse locator to (start, end) tuple.

    Convenience function returning only line numbers.
    """
    parsed = parse_locator_range(locator)
    if parsed is None:
        return None
    return (parsed.start, parsed.end)


def locator_within_ranges(locator: str, ranges: list[SourceRange]) -> bool:
    """Check if a locator falls within any of the given ranges.

    Used for range-gated Phase 2 validation to ensure evidence
    stays within declared source_ranges.
    """
    parsed = parse_locator_range(locator)
    if parsed is None:
        return False

    for r in ranges:
        # Same source (or compatible)
        if r.source in ("normalized", parsed.source) or parsed.source == "normalized":
            if parsed.start >= r.start and parsed.end <= r.end:
                return True

    return False


def ranges_overlap(a: SourceRange, b: SourceRange) -> bool:
    """Check if two source ranges overlap."""
    if a.source != b.source:
        return False
    return a.start <= b.end and b.start <= a.end


def merge_ranges(ranges: list[SourceRange]) -> list[SourceRange]:
    """Merge overlapping source ranges.

    Returns a sorted list of non-overlapping ranges.
    """
    if not ranges:
        return []

    # Group by source
    by_source: dict[str, list[SourceRange]] = {}
    for r in ranges:
        by_source.setdefault(r.source, []).append(r)

    merged: list[SourceRange] = []
    for source, source_ranges in by_source.items():
        sorted_ranges = sorted(source_ranges, key=lambda r: (r.start, r.end))
        current = sorted_ranges[0]

        for r in sorted_ranges[1:]:
            if r.start <= current.end + 1:
                # Overlapping or adjacent - extend
                current = SourceRange(
                    start=current.start,
                    end=max(current.end, r.end),
                    source=source,
                )
            else:
                # Gap - emit current and start new
                merged.append(current)
                current = r

        merged.append(current)

    return sorted(merged, key=lambda r: (r.source, r.start))


def format_locator(start: int, end: int | None = None, slug: str | None = None) -> str:
    """Format line numbers into a canonical locator string.

    Args:
        start: Start line (1-indexed)
        end: Optional end line (1-indexed, inclusive)
        slug: Optional source slug prefix

    Returns:
        Formatted locator like "normalized:L12" or "js-allonge:normalized:L12-L34"
    """
    base = f"{slug}:normalized" if slug else "normalized"
    if end and end != start:
        return f"{base}:L{start}-L{end}"
    return f"{base}:L{start}"


def format_ranges(ranges: list[SourceRange]) -> str:
    """Format a list of source ranges as a comma-separated string."""
    if not ranges:
        return "none"
    return ", ".join(format_range(r) for r in ranges)


def format_range(allowed: SourceRange) -> str:
    """Format a single source range as a locator string."""
    return f"normalized:L{allowed.start}-L{allowed.end}"


def source_ranges_for_page(
    *,
    page: Path,
    frontmatter: dict[str, object],
    source_slug: str,
    source_lines: list[str],
    related_title: str | None = None,
) -> SourceRangeResult:
    """Get source ranges for a wiki page.

    First checks for declared source_ranges in frontmatter.
    If not declared, derives ranges from source headings that match the page title.
    """
    declared, invalid = declared_source_ranges(frontmatter, source_slug)
    if declared or invalid:
        return SourceRangeResult(ranges=declared, invalid=invalid, declared=True)

    aliases = page_aliases(page, frontmatter.get("title"), related_title)
    return SourceRangeResult(
        ranges=derive_ranges_from_headings(source_lines, aliases),
        invalid=[],
        declared=False,
    )


def source_ranges_for_candidate(
    candidate_path: str,
    source_lines: list[str],
    title: str | None = None
) -> list[SourceRange]:
    """Get source ranges for a candidate page path."""
    aliases = page_aliases(Path(candidate_path), title, None)
    return derive_ranges_from_headings(source_lines, aliases)


def declared_source_ranges(
    frontmatter: dict[str, object],
    source_slug: str
) -> tuple[list[SourceRange], list[str]]:
    """Parse source_ranges from frontmatter.

    Returns (ranges, invalid_entries).
    """
    raw_values = frontmatter.get(
        "source_ranges") or frontmatter.get("evidence_ranges")
    if raw_values is None:
        return [], []
    if isinstance(raw_values, str):
        values: Iterable[object] = [raw_values]
    elif isinstance(raw_values, list):
        values = raw_values
    else:
        return [], [f"source_ranges must be a string or list, got {type(raw_values).__name__}"]

    ranges: list[SourceRange] = []
    invalid: list[str] = []
    for raw in values:
        if not isinstance(raw, str):
            invalid.append(
                f"source range value must be a string, got {type(raw).__name__}")
            continue
        parsed = parse_source_range(raw, source_slug)
        if parsed is None:
            invalid.append(
                f"could not parse source range {raw!r}; expected normalized:L12-L34 or {source_slug}:normalized:L12-L34")
            continue
        ranges.append(parsed)
    return ranges, invalid


def parse_source_range(raw: str, source_slug: str | None = None) -> SourceRange | None:
    """Parse a source range string like 'normalized:L12-L34'."""
    cleaned = raw.strip().strip("`")
    match = RANGE_RE.fullmatch(cleaned)
    if not match:
        return None
    prefix = match.group("prefix")
    if source_slug and prefix and prefix != source_slug:
        return None
    start = int(match.group("start"))
    end = int(match.group("end") or start)
    if start < 1 or end < start:
        return None
    return SourceRange(start=start, end=end, reason="declared in frontmatter")


def locator_within_tolerance(
    start: int,
    end: int,
    ranges: list[SourceRange]
) -> SourceRange | None:
    """Check if locator is within tolerance of any allowed range.

    Returns the matching range if within tolerance, None otherwise.
    This handles common off-by-one errors from model context expansion.
    """
    for allowed in ranges:
        if (allowed.start - MAX_LOCATOR_SLOP <= start <= allowed.start + MAX_LOCATOR_SLOP
                and allowed.end - MAX_LOCATOR_SLOP <= end <= allowed.end + MAX_LOCATOR_SLOP):
            return allowed
    return None


def canonicalize_locator(start: int, end: int, canonical: SourceRange) -> str:
    """Return the canonical locator string for the given range."""
    return f"normalized:L{canonical.start}-L{canonical.end}"


def page_aliases(page: Path, title: object, related_title: str | None) -> set[str]:
    """Generate aliases for page title matching against source headings."""
    raw_aliases = {
        page.stem,
        page.stem.replace("-", " "),
    }
    if isinstance(title, str):
        raw_aliases.add(title)
    if related_title:
        raw_aliases.add(related_title)
    aliases: set[str] = set()
    for raw in raw_aliases:
        aliases.add(canonical_key(raw))
        aliases.add(canonical_key(strip_domain_prefix(raw)))
    return {alias for alias in aliases if alias}


def strip_domain_prefix(text: str) -> str:
    """Remove domain-specific prefixes like 'aoe2' from text."""
    words = re.findall(r"[A-Za-z0-9']+", text.replace("-", " "))
    while words and words[0].lower() in {"aoe2", "aok", "age", "empires", "ii"}:
        words = words[1:]
    return " ".join(words)


def derive_ranges_from_headings(source_lines: list[str], aliases: set[str]) -> list[SourceRange]:
    """Derive source ranges from headings that match the given aliases."""
    headings = source_headings(source_lines)
    ranges: list[SourceRange] = []
    for index, heading in enumerate(headings):
        key = canonical_key(heading.clean_title)
        if key not in aliases:
            continue
        end = len(source_lines)
        for next_heading in headings[index + 1:]:
            if next_heading.level <= heading.level:
                end = next_heading.line - 1
                break
        ranges.append(
            SourceRange(
                start=heading.line,
                end=end,
                reason=f"derived from heading {heading.raw_title!r} at normalized:L{heading.line}",
            )
        )
    return ranges


def source_headings(source_lines: list[str]) -> list[SourceHeading]:
    """Extract all headings from source lines."""
    headings: list[SourceHeading] = []
    for line_number, line in enumerate(source_lines, start=1):
        match = HEADING_RE.match(line.strip())
        if not match:
            continue
        raw_title = match.group("title").strip()
        clean_title = clean_heading_title(raw_title)
        if not clean_title:
            continue
        headings.append(
            SourceHeading(
                line=line_number,
                level=len(match.group("marks")),
                raw_title=raw_title,
                clean_title=clean_title,
            )
        )
    return headings


def clean_heading_title(raw_title: str) -> str:
    """Clean a heading title for comparison."""
    text = re.sub(r"<[^>]+>", " ", raw_title)
    text = re.sub(r"\[[^\]]+\]\([^)]+\)", " ", text)
    text = text.replace("`", " ")
    text = re.sub(r"^\s*\d+(?:\.\d+)*[.)]?\s+", "", text)
    return " ".join(text.split())


def canonical_key(text: str) -> str:
    """Convert text to a canonical key for comparison."""
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\[[^\]]+\]\([^)]+\)", " ", text)
    text = re.sub(r"^\s*\d+(?:\.\d+)*[.)]?\s+", "", text)
    tokens: list[str] = []
    for raw in re.findall(r"[A-Za-z0-9']+", text.replace("-", " ").lower()):
        token = raw.strip("'")
        if token.endswith("'s"):
            token = token[:-2]
        if len(token) > 4 and token.endswith("s"):
            token = token[:-1]
        if token in {"aoe2", "aok", "age", "empires", "ii"}:
            continue
        tokens.append(token)
    return " ".join(tokens)
