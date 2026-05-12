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


# Patterns for parsing locators
RANGE_RE = re.compile(
    r"^(?:(?P<prefix>[A-Za-z0-9_-]+):)?normalized:L(?P<start>\d+)(?:-L?(?P<end>\d+))?$",
    re.IGNORECASE,
)

SIMPLE_LINE_RE = re.compile(r"^L?(\d+)(?:-L?(\d+))?$", re.IGNORECASE)


@dataclass(frozen=True)
class SourceRange:
    """A range within a normalized source file."""
    start: int  # 1-indexed
    end: int    # 1-indexed, inclusive
    source: str = "normalized"  # Usually "normalized" or a source slug


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
