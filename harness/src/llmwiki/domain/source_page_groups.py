"""Adaptive grouping of extracted source units into source pages."""

from __future__ import annotations

import re
from pathlib import Path

from llmwiki.domain.objects import (
    ExtractedUnit,
    PageMap,
    PageMapLink,
    RawSource,
    SourceClaim,
    SourcePageGroup,
    WikiMatch,
)
from llmwiki.domain.pages import parse_page, slugify
from llmwiki.domain.planning_analysis import same_section_identity

SOURCE_WRITE_GROUPING_THRESHOLD = 40
SOURCE_WRITE_GROUP_UNIT_LIMIT = 5
SOURCE_WRITE_GROUP_TOKEN_BUDGET = 2_200
SOURCE_PAGE_ID_MAX_CHARS = 96


def source_page_groups(
    *,
    raw_source: RawSource,
    extracted_units: tuple[ExtractedUnit, ...],
    existing_pages: dict[str, str],
    wiki_matches: tuple[WikiMatch, ...],
    source_claims: tuple[SourceClaim, ...],
    new_page_prefix: str | None = None,
) -> tuple[SourcePageGroup, ...]:
    matches_by_unit = _matches_by_unit(wiki_matches)
    claims_by_unit = _claims_by_unit(source_claims)
    prefix = new_page_prefix or slugify(Path(raw_source.source_locator).stem)
    source_units = _source_page_units(extracted_units, claims_by_unit)
    if len(extracted_units) <= SOURCE_WRITE_GROUPING_THRESHOLD:
        return _exact_groups(raw_source, source_units, existing_pages, matches_by_unit, prefix)
    return _adaptive_groups(
        raw_source,
        source_units,
        existing_pages,
        matches_by_unit,
        claims_by_unit,
        prefix,
    )


def page_map_for_groups(raw_source: RawSource, groups: tuple[SourcePageGroup, ...]) -> PageMap:
    return PageMap(
        source_id=raw_source.source_locator,
        links=tuple(
            PageMapLink(
                page_id=group.page_id,
                label=source_page_group_label(group),
                source_page_group_id=group.source_page_group_id,
            )
            for group in groups
        ),
    )


def source_page_group_label(group: SourcePageGroup) -> str:
    if group.first_heading == group.last_heading:
        return group.first_heading
    return f"{group.first_heading} through {group.last_heading}"


def _exact_groups(
    raw_source: RawSource,
    units: tuple[ExtractedUnit, ...],
    existing_pages: dict[str, str],
    matches_by_unit: dict[str, tuple[WikiMatch, ...]],
    prefix: str,
) -> tuple[SourcePageGroup, ...]:
    return tuple(
        _group(
            raw_source,
            (unit,),
            _target_page_id(unit, existing_pages, matches_by_unit.get(unit.unit_id, ()), prefix),
        )
        for unit in units
    )


def _adaptive_groups(
    raw_source: RawSource,
    units: tuple[ExtractedUnit, ...],
    existing_pages: dict[str, str],
    matches_by_unit: dict[str, tuple[WikiMatch, ...]],
    claims_by_unit: dict[str, tuple[SourceClaim, ...]],
    prefix: str,
) -> tuple[SourcePageGroup, ...]:
    groups: list[SourcePageGroup] = []
    current: list[ExtractedUnit] = []
    current_tokens = 0
    used_page_ids = set(existing_pages)

    def flush() -> None:
        nonlocal current, current_tokens
        if not current:
            return
        page_id = _group_page_id(prefix, tuple(current), used_page_ids)
        groups.append(_group(raw_source, tuple(current), page_id))
        current = []
        current_tokens = 0

    for index, unit in enumerate(units):
        target = _target_page_id(
            unit, existing_pages, matches_by_unit.get(unit.unit_id, ()), prefix
        )
        default_target = _default_source_page(unit, prefix)
        previous_unit = units[index - 1] if index > 0 else None
        next_unit = units[index + 1] if index + 1 < len(units) else None
        if target in existing_pages or target != default_target or _keep_one_unit(
            unit, previous_unit, next_unit, claims_by_unit
        ):
            flush()
            groups.append(_group(raw_source, (unit,), target))
            used_page_ids.add(target)
            continue
        unit_tokens = _unit_tokens(unit)
        if current and (
            _top_level(current[-1].heading_path) != _top_level(unit.heading_path)
            or len(current) >= SOURCE_WRITE_GROUP_UNIT_LIMIT
            or current_tokens + unit_tokens > SOURCE_WRITE_GROUP_TOKEN_BUDGET
        ):
            flush()
        current.append(unit)
        current_tokens += unit_tokens

    flush()
    return tuple(groups)


def _group(
    raw_source: RawSource, units: tuple[ExtractedUnit, ...], page_id: str
) -> SourcePageGroup:
    first = units[0]
    last = units[-1]
    return SourcePageGroup(
        source_page_group_id=f"source-page-group-{first.unit_id}-{last.unit_id}",
        raw_source=raw_source,
        page_id=page_id,
        extracted_units=tuple(unit.unit_id for unit in units),
        first_heading=first.heading_path,
        last_heading=last.heading_path,
        first_locator=first.locator,
        last_locator=last.locator,
        token_estimate=sum(_unit_tokens(unit) for unit in units),
    )


def _target_page_id(
    unit: ExtractedUnit,
    existing_pages: dict[str, str],
    matches: tuple[WikiMatch, ...],
    prefix: str,
) -> str:
    default_page = _default_source_page(unit, prefix)
    if default_page in existing_pages:
        return default_page
    for page_id in existing_pages:
        if page_id.startswith(f"{prefix}-") and same_section_identity(
            unit.heading_path, page_id.removeprefix(f"{prefix}-")
        ):
            return page_id
    for match in matches:
        if (
            match.page_id.startswith(f"{prefix}-")
            and _page_kind(match.page_id, existing_pages) == "source"
            and same_section_identity(unit.heading_path, match.page_id.removeprefix(f"{prefix}-"))
        ):
            return match.page_id
    return default_page


def _default_source_page(unit: ExtractedUnit, prefix: str) -> str:
    heading = slugify(unit.heading_path)
    if heading == prefix or heading.startswith(f"{prefix}-"):
        return heading
    return slugify(f"{prefix}-{unit.heading_path}")


def _group_page_id(
    prefix: str,
    units: tuple[ExtractedUnit, ...],
    used_page_ids: set[str],
) -> str:
    if len(units) == 1 or units[0].heading_path == units[-1].heading_path:
        base = _default_source_page(units[0], prefix)
    else:
        base = slugify(f"{prefix}-{units[0].heading_path}-through-{units[-1].heading_path}")
    base = _truncate_page_id(base)
    page_id = base
    suffix = 2
    while page_id in used_page_ids:
        suffix_text = f"-{suffix}"
        page_id = (
            f"{_truncate_page_id(base, SOURCE_PAGE_ID_MAX_CHARS - len(suffix_text))}{suffix_text}"
        )
        suffix += 1
    used_page_ids.add(page_id)
    return page_id


def _keep_one_unit(
    unit: ExtractedUnit,
    previous_unit: ExtractedUnit | None,
    next_unit: ExtractedUnit | None,
    claims_by_unit: dict[str, tuple[SourceClaim, ...]],
) -> bool:
    central_claims = (
        claim
        for claim in claims_by_unit.get(unit.unit_id, ())
        if claim.claim_eligibility == "eligible" and claim.claim_centrality > 0
    )
    return any(central_claims) and not _has_shared_parent(unit, previous_unit, next_unit)


def _has_shared_parent(
    unit: ExtractedUnit,
    previous_unit: ExtractedUnit | None,
    next_unit: ExtractedUnit | None,
) -> bool:
    parent = _parent_heading(unit.heading_path)
    if not parent:
        return False
    neighbors = tuple(neighbor for neighbor in (previous_unit, next_unit) if neighbor is not None)
    return any(_parent_heading(neighbor.heading_path) == parent for neighbor in neighbors)


def _top_level(heading_path: str) -> str:
    if ">" in heading_path:
        return heading_path.split(">", 1)[0].strip()
    match = re.match(r"^\s*(\d+)(?:[.\s-]|$)", heading_path)
    return match.group(1) if match else heading_path.strip()


def _parent_heading(heading_path: str) -> str:
    if ">" in heading_path:
        return heading_path.rsplit(">", 1)[0].strip()
    match = re.match(r"^\s*(\d+)\.", heading_path)
    return match.group(1) if match else ""


def _unit_tokens(unit: ExtractedUnit) -> int:
    return max(1, len(unit.text.split()))


def _source_page_units(
    units: tuple[ExtractedUnit, ...],
    claims_by_unit: dict[str, tuple[SourceClaim, ...]],
) -> tuple[ExtractedUnit, ...]:
    return tuple(unit for unit in units if _has_source_page_material(unit, claims_by_unit))


def _has_source_page_material(
    unit: ExtractedUnit, claims_by_unit: dict[str, tuple[SourceClaim, ...]]
) -> bool:
    if claims_by_unit.get(unit.unit_id):
        return True
    return any(
        line.strip() and not line.lstrip().startswith("#") for line in unit.text.splitlines()
    )


def _truncate_page_id(page_id: str, max_chars: int = SOURCE_PAGE_ID_MAX_CHARS) -> str:
    if len(page_id) <= max_chars:
        return page_id
    parts: list[str] = []
    for part in page_id.split("-"):
        candidate = "-".join([*parts, part])
        if len(candidate) > max_chars:
            break
        parts.append(part)
    return "-".join(parts) if parts else page_id[:max_chars].rstrip("-")


def _claims_by_unit(claims: tuple[SourceClaim, ...]) -> dict[str, tuple[SourceClaim, ...]]:
    grouped: dict[str, list[SourceClaim]] = {}
    for claim in claims:
        grouped.setdefault(claim.extracted_unit_id, []).append(claim)
    return {unit_id: tuple(items) for unit_id, items in grouped.items()}


def _matches_by_unit(matches: tuple[WikiMatch, ...]) -> dict[str, tuple[WikiMatch, ...]]:
    grouped: dict[str, list[WikiMatch]] = {}
    for match in matches:
        if ":" not in match.match_reason:
            continue
        unit_id = match.match_reason.split(":", 1)[1]
        grouped.setdefault(unit_id, []).append(match)
    return {unit_id: tuple(items[:5]) for unit_id, items in grouped.items()}


def _page_kind(page_id: str, existing_pages: dict[str, str]) -> str:
    try:
        return parse_page(existing_pages[page_id]).page_kind
    except Exception:
        return ""
