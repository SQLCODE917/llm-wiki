"""Compact page maps for context-bounded wiki exploration."""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.links import extract_links
from llmwiki.domain.pages import PageError, PageMetadata, parse_page
from llmwiki.domain.retrieval import query_terms, token_keys_for_text

_HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.+?)\s*$")
_SOURCE_RANGE_RE = re.compile(r"source-range-[a-z0-9]+-\d+")
DEFAULT_PAGE_MAP_MAX_CHARS = 2_800
_RELATED_PAGE_LIMIT = 6
_CITATION_LIMIT = 3


@dataclass(frozen=True)
class PageSectionMap:
    level: int
    title: str
    offset: int
    end_offset: int
    citations: tuple[str, ...]


@dataclass(frozen=True)
class PageMap:
    page_id: str
    page_kind: str
    page_family: str
    summary: str
    sources: tuple[str, ...]
    related_page_ids: tuple[str, ...]
    sections: tuple[PageSectionMap, ...]
    total_sections: int
    focus_query: str | None = None
    focus_matched_sections: int | None = None


def inspect_page_text(
    page_id: str,
    text: str,
    *,
    max_sections: int = 80,
    focus_query: str | None = None,
) -> PageMap:
    metadata = _metadata(page_id, text)
    headings = _heading_positions(text)
    selected_indexes, focus_matched_sections = _select_section_indexes(
        headings, max_sections=max_sections, focus_query=focus_query
    )
    sections = tuple(_section_for_heading(text, headings, index) for index in selected_indexes)
    return PageMap(
        page_id=metadata.page_id,
        page_kind=metadata.page_kind,
        page_family=metadata.page_family,
        summary=metadata.summary,
        sources=metadata.sources,
        related_page_ids=tuple(sorted(extract_links(text))[:_RELATED_PAGE_LIMIT]),
        sections=sections,
        total_sections=len(headings),
        focus_query=focus_query,
        focus_matched_sections=focus_matched_sections,
    )


def render_page_map(page_map: PageMap, *, max_chars: int = DEFAULT_PAGE_MAP_MAX_CHARS) -> str:
    lines = [
        f"Page map for [[{page_map.page_id}]]",
        f"kind: {page_map.page_kind}",
        f"family: {page_map.page_family or 'unspecified'}",
        f"summary: {page_map.summary}",
    ]
    if page_map.sources:
        lines.append("sources: " + ", ".join(page_map.sources))
    if page_map.related_page_ids:
        links = ", ".join(f"[[{page_id}]]" for page_id in page_map.related_page_ids)
        lines.append("related pages: " + links)
    lines.append(f"total sections: {page_map.total_sections}")
    if page_map.focus_query:
        matched = page_map.focus_matched_sections or 0
        lines.append(f"focus query: {page_map.focus_query!r} ({matched} heading match(es))")
    lines.extend(
        [
            "",
            "Sections:",
            "Use read_page with the listed offset only for sections that are needed.",
        ]
    )
    if page_map.focus_query and not page_map.focus_matched_sections:
        lines.append(
            "No section headings matched the focus query; treat absent procedure "
            "coverage as missing unless another retrieved page names it directly."
        )
    omitted = 0
    for index, section in enumerate(page_map.sections):
        indent = "  " * max(section.level - 1, 0)
        citation_text = ""
        if section.citations:
            citation_text = " citations: " + ", ".join(section.citations[:_CITATION_LIMIT])
        line = (
            f"{indent}- h{section.level} {section.title} "
            f"(chars {section.offset}-{section.end_offset}){citation_text}"
        )
        if _would_exceed(lines, line, max_chars):
            omitted = len(page_map.sections) - index
            break
        lines.append(line)
    if omitted:
        note = f"... {omitted} section(s) omitted from this bounded page map."
        while _would_exceed(lines, note, max_chars) and len(lines) > 1:
            lines.pop()
        if not _would_exceed(lines, note, max_chars):
            lines.append(note)
    return "\n".join(lines)


def _metadata(page_id: str, text: str) -> PageMetadata:
    try:
        return parse_page(text).page_metadata
    except PageError:
        return PageMetadata(page_id=page_id, page_kind="concept", summary="Invalid page metadata.")


def _would_exceed(lines: list[str], next_line: str, max_chars: int) -> bool:
    return len("\n".join((*lines, next_line))) > max_chars


def _select_section_indexes(
    headings: tuple[tuple[int, int, str], ...],
    *,
    max_sections: int,
    focus_query: str | None,
) -> tuple[tuple[int, ...], int | None]:
    if not focus_query:
        return tuple(range(min(len(headings), max_sections))), None
    terms = {term for term in query_terms(focus_query) if len(term) >= 3}
    if not terms:
        return tuple(range(min(len(headings), max_sections))), None
    matches = tuple(
        index for index, heading in enumerate(headings) if _heading_matches_focus(heading, terms)
    )
    if not matches:
        return tuple(range(min(len(headings), min(max_sections, 18)))), 0
    selected = _with_ancestors_and_neighbors(headings, matches)
    return selected[:max_sections], len(matches)


def _heading_matches_focus(heading: tuple[int, int, str], terms: set[str]) -> bool:
    title_keys = token_keys_for_text(heading[2])
    return all(token_keys_for_text(term) & title_keys for term in terms)


def _with_ancestors_and_neighbors(
    headings: tuple[tuple[int, int, str], ...], matches: tuple[int, ...]
) -> tuple[int, ...]:
    selected: set[int] = set()
    for index in matches:
        selected.add(index)
        selected.update(_sibling_indexes(headings, index))
        selected.update(_child_indexes(headings, index, limit=2))
        selected.update(_ancestor_indexes(headings, index))
    return tuple(sorted(selected))


def _sibling_indexes(headings: tuple[tuple[int, int, str], ...], index: int) -> tuple[int, ...]:
    siblings: list[int] = []
    level = headings[index][0]
    for candidate in range(index - 1, -1, -1):
        candidate_level = headings[candidate][0]
        if candidate_level == level:
            siblings.append(candidate)
            break
        if candidate_level < level:
            break
    for candidate in range(index + 1, len(headings)):
        candidate_level = headings[candidate][0]
        if candidate_level == level:
            siblings.append(candidate)
            break
        if candidate_level < level:
            break
    return tuple(siblings)


def _child_indexes(
    headings: tuple[tuple[int, int, str], ...], index: int, *, limit: int
) -> tuple[int, ...]:
    children: list[int] = []
    level = headings[index][0]
    for candidate in range(index + 1, len(headings)):
        candidate_level = headings[candidate][0]
        if candidate_level <= level:
            break
        if candidate_level == level + 1:
            children.append(candidate)
            if len(children) >= limit:
                break
    return tuple(children)


def _ancestor_indexes(headings: tuple[tuple[int, int, str], ...], index: int) -> tuple[int, ...]:
    ancestors: list[int] = []
    child_level = headings[index][0]
    for candidate in range(index - 1, -1, -1):
        level = headings[candidate][0]
        if level < child_level:
            ancestors.append(candidate)
            child_level = level
    return tuple(ancestors)


def _heading_positions(text: str) -> tuple[tuple[int, int, str], ...]:
    positions: list[tuple[int, int, str]] = []
    offset = 0
    for line in text.splitlines(keepends=True):
        match = _HEADING_RE.match(line.rstrip("\n"))
        if match:
            positions.append((len(match["marks"]), offset, match["title"]))
        offset += len(line)
    return tuple(positions)


def _section_for_heading(
    text: str, headings: tuple[tuple[int, int, str], ...], index: int
) -> PageSectionMap:
    level, offset, title = headings[index]
    end_offset = len(text)
    for next_level, next_offset, _ in headings[index + 1 :]:
        if next_level <= level:
            end_offset = next_offset
            break
    citations = tuple(dict.fromkeys(_SOURCE_RANGE_RE.findall(text[offset:end_offset])))
    return PageSectionMap(
        level=level,
        title=title,
        offset=offset,
        end_offset=end_offset,
        citations=citations,
    )
