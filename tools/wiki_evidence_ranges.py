#!/usr/bin/env python3
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


RANGE_RE = re.compile(
    r"^(?:(?P<source>[A-Za-z0-9_-]+):)?normalized:L(?P<start>\d+)(?:-L?(?P<end>\d+))?$",
    re.IGNORECASE,
)
HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.+?)\s*$")


def normalize_locator(loc: str) -> str:
    """Normalize locator to always-range format: L123 → L123-L123.

    This ensures consistent format throughout the pipeline.
    Single lines become trivial ranges (L123-L123).
    """
    match = re.search(r'L(\d+)(?:-L?(\d+))?', loc, re.IGNORECASE)
    if not match:
        return loc
    start = int(match.group(1))
    end = int(match.group(2)) if match.group(2) else start
    # Preserve any prefix (like source slug)
    prefix_match = re.match(
        r'^([A-Za-z0-9_-]+:)?normalized:', loc, re.IGNORECASE)
    prefix = prefix_match.group(0) if prefix_match else "normalized:"
    return f"{prefix}L{start}-L{end}"


@dataclass(frozen=True)
class SourceRange:
    start: int
    end: int
    reason: str


@dataclass(frozen=True)
class SourceRangeResult:
    ranges: list[SourceRange]
    invalid: list[str]
    declared: bool


@dataclass(frozen=True)
class SourceHeading:
    line: int
    level: int
    raw_title: str
    clean_title: str


def source_ranges_for_page(
    *,
    page: Path,
    frontmatter: dict[str, object],
    source_slug: str,
    source_lines: list[str],
    related_title: str | None = None,
) -> SourceRangeResult:
    declared, invalid = declared_source_ranges(frontmatter, source_slug)
    if declared or invalid:
        return SourceRangeResult(ranges=declared, invalid=invalid, declared=True)

    aliases = page_aliases(page, frontmatter.get("title"), related_title)
    return SourceRangeResult(
        ranges=derive_ranges_from_headings(source_lines, aliases),
        invalid=[],
        declared=False,
    )


def source_ranges_for_candidate(candidate_path: str, source_lines: list[str], title: str | None = None) -> list[SourceRange]:
    aliases = page_aliases(Path(candidate_path), title, None)
    return derive_ranges_from_headings(source_lines, aliases)


def declared_source_ranges(frontmatter: dict[str, object], source_slug: str) -> tuple[list[SourceRange], list[str]]:
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
    cleaned = raw.strip().strip("`")
    match = RANGE_RE.fullmatch(cleaned)
    if not match:
        return None
    prefix = match.group("source")
    if source_slug and prefix and prefix != source_slug:
        return None
    start = int(match.group("start"))
    end = int(match.group("end") or start)
    if start < 1 or end < start:
        return None
    return SourceRange(start=start, end=end, reason="declared in frontmatter")


def parse_locator_range(locator: str) -> tuple[int, int] | None:
    cleaned = locator.strip().strip("`")
    match = RANGE_RE.fullmatch(cleaned)
    if not match:
        return None
    start = int(match.group("start"))
    end = int(match.group("end") or start)
    if start < 1 or end < start:
        return None
    return start, end


def locator_within_ranges(start: int, end: int, ranges: list[SourceRange]) -> bool:
    """Check if locator is strictly contained within any allowed range."""
    return any(start >= allowed.start and end <= allowed.end for allowed in ranges)


# Maximum line slop for off-by-one tolerance
MAX_LOCATOR_SLOP = 2


def locator_within_tolerance(start: int, end: int, ranges: list[SourceRange]) -> SourceRange | None:
    """Check if locator is within tolerance of any allowed range.

    Returns the matching range if within tolerance, None otherwise.
    This handles common off-by-one errors from model context expansion.
    """
    for allowed in ranges:
        # Check if model's range overlaps with allowed range within tolerance
        if (allowed.start - MAX_LOCATOR_SLOP <= start <= allowed.start + MAX_LOCATOR_SLOP
                and allowed.end - MAX_LOCATOR_SLOP <= end <= allowed.end + MAX_LOCATOR_SLOP):
            return allowed
    return None


def canonicalize_locator(start: int, end: int, canonical: SourceRange) -> str:
    """Return the canonical locator string for the given range."""
    return f"normalized:L{canonical.start}-L{canonical.end}"


def format_ranges(ranges: list[SourceRange]) -> str:
    if not ranges:
        return "none"
    return ", ".join(format_range(allowed) for allowed in ranges)


def format_range(allowed: SourceRange) -> str:
    return f"normalized:L{allowed.start}-L{allowed.end}"


def page_aliases(page: Path, title: object, related_title: str | None) -> set[str]:
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
    words = re.findall(r"[A-Za-z0-9']+", text.replace("-", " "))
    while words and words[0].lower() in {"aoe2", "aok", "age", "empires", "ii"}:
        words = words[1:]
    return " ".join(words)


def derive_ranges_from_headings(source_lines: list[str], aliases: set[str]) -> list[SourceRange]:
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
    text = re.sub(r"<[^>]+>", " ", raw_title)
    text = re.sub(r"\[[^\]]+\]\([^)]+\)", " ", text)
    text = text.replace("`", " ")
    text = re.sub(r"^\s*\d+(?:\.\d+)*[.)]?\s+", "", text)
    return " ".join(text.split())


def canonical_key(text: str) -> str:
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
