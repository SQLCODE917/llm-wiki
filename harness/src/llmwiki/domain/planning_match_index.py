"""Index WikiMatch records by extracted unit id."""

from __future__ import annotations

from llmwiki.domain.objects import WikiMatch


def matches_by_unit_id(
    matches: tuple[WikiMatch, ...],
) -> dict[str, tuple[WikiMatch, ...]]:
    grouped: dict[str, list[WikiMatch]] = {}
    for match in matches:
        unit_id = match_unit_id(match)
        if unit_id:
            grouped.setdefault(unit_id, []).append(match)
    return {unit_id: tuple(items) for unit_id, items in grouped.items()}


def matches_for_units(
    matches_by_unit: dict[str, tuple[WikiMatch, ...]], unit_ids: frozenset[str]
) -> tuple[WikiMatch, ...]:
    selected: list[WikiMatch] = []
    seen: set[tuple[str, str]] = set()
    for unit_id in sorted(unit_ids):
        for match in matches_by_unit.get(unit_id, ()):
            key = (match.page_id, match.match_reason)
            if key not in seen:
                selected.append(match)
                seen.add(key)
    return tuple(selected)


def match_unit_id(match: WikiMatch) -> str:
    if ":" not in match.match_reason:
        return ""
    suffix = match.match_reason.rsplit(":", 1)[1]
    return suffix if suffix.startswith("unit-") else ""
