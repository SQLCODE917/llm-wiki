"""Harness-owned backlog for missing wiki page candidates."""

from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, replace
from typing import Literal

from llmwiki.domain.pages import slugify

CandidateStatus = Literal["discovered", "queued", "promoted", "rejected", "merged"]
_ACTIVE_STATUSES = {"discovered", "queued"}


@dataclass(frozen=True)
class CandidateSignal:
    display_name: str
    category_guess: str
    reason: str
    source_page: str

    @property
    def slug(self) -> str:
        return slugify(self.display_name)


@dataclass(frozen=True)
class CandidateRecord:
    slug: str
    display_name: str
    category_guess: str
    aliases: tuple[str, ...]
    reasons: tuple[str, ...]
    source_pages: tuple[str, ...]
    mention_count: int
    status: CandidateStatus
    first_seen: str
    last_seen: str
    status_reason: str = ""

    def render(self) -> str:
        source_count = len(self.source_pages)
        aliases = f"; aliases: {', '.join(self.aliases)}" if self.aliases else ""
        reason = f"; status reason: {self.status_reason}" if self.status_reason else ""
        return (
            f"- {self.display_name} (`{self.slug}`, {self.category_guess}) — "
            f"{self.status}; mentions {self.mention_count}; sources {source_count}"
            f"{aliases}{reason}"
        )


@dataclass(frozen=True)
class CandidateBacklog:
    records: tuple[CandidateRecord, ...] = ()

    def by_slug(self) -> dict[str, CandidateRecord]:
        return {record.slug: record for record in self.records}

    def top(self, limit: int = 8) -> tuple[CandidateRecord, ...]:
        active = [record for record in self.records if record.status in _ACTIVE_STATUSES]
        return tuple(
            sorted(
                active,
                key=lambda record: (
                    record.status != "queued",
                    -record.mention_count,
                    -len(record.source_pages),
                    record.slug,
                ),
            )[:limit]
        )

    def render(self, limit: int = 8) -> str:
        top = self.top(limit)
        if not top:
            return "No active candidate pages from explicit missing double-bracket links."
        return "\n".join(record.render() for record in top)

    def to_json_text(self) -> str:
        payload = {"records": [_record_to_json(record) for record in self.records]}
        return json.dumps(payload, indent=2, sort_keys=True) + "\n"

    @classmethod
    def from_json_text(cls, text: str) -> CandidateBacklog:
        return backlog_from_json_text(text)


def backlog_from_json_text(text: str) -> CandidateBacklog:
    if not text.strip():
        return CandidateBacklog()
    payload = json.loads(text)
    records = tuple(_record_from_json(item) for item in payload.get("records", []))
    return CandidateBacklog(records=tuple(sorted(records, key=lambda record: record.slug)))


def update_candidate_backlog(
    backlog: CandidateBacklog,
    signals: Sequence[CandidateSignal],
    *,
    existing_pages: set[str],
    today: str,
) -> CandidateBacklog:
    records = backlog.by_slug()
    for slug, record in tuple(records.items()):
        if record.status in _ACTIVE_STATUSES and slug in existing_pages:
            records[slug] = replace(record, status="promoted", last_seen=today)

    for signal in signals:
        slug = signal.slug
        if not slug or slug in existing_pages:
            continue
        existing = records.get(slug)
        if existing is None:
            records[slug] = CandidateRecord(
                slug=slug,
                display_name=signal.display_name,
                category_guess=signal.category_guess,
                aliases=(),
                reasons=(signal.reason,),
                source_pages=(signal.source_page,),
                mention_count=1,
                status="discovered",
                first_seen=today,
                last_seen=today,
            )
            continue
        updated = _merge_signal(existing, signal, today)
        records[slug] = _promote_if_ready(updated)
    return CandidateBacklog(records=tuple(sorted(records.values(), key=lambda record: record.slug)))


def reject_candidate(
    backlog: CandidateBacklog, slug: str, reason: str, today: str
) -> CandidateBacklog:
    records = backlog.by_slug()
    record = records.get(slug)
    if record is None:
        record = CandidateRecord(
            slug=slug,
            display_name=slug.replace("-", " "),
            category_guess="concept",
            aliases=(),
            reasons=(),
            source_pages=(),
            mention_count=0,
            status="rejected",
            first_seen=today,
            last_seen=today,
            status_reason=reason,
        )
    else:
        record = replace(record, status="rejected", status_reason=reason, last_seen=today)
    records[slug] = record
    return CandidateBacklog(records=tuple(sorted(records.values(), key=lambda item: item.slug)))


def signals_from_broken_links(
    broken_links: Mapping[str, tuple[str, ...]],
) -> tuple[CandidateSignal, ...]:
    signals: list[CandidateSignal] = []
    for source_page, targets in sorted(broken_links.items()):
        for target in targets:
            signals.append(
                CandidateSignal(
                    display_name=target,
                    category_guess="concept",
                    reason=f"linked from [[{source_page}]] but no page exists",
                    source_page=source_page,
                )
            )
    return tuple(signals)


def _merge_signal(record: CandidateRecord, signal: CandidateSignal, today: str) -> CandidateRecord:
    aliases = _append_unique(record.aliases, signal.display_name)
    reasons = _append_unique(record.reasons, signal.reason)
    source_pages = _append_unique(record.source_pages, signal.source_page)
    return replace(
        record,
        aliases=aliases,
        reasons=reasons,
        source_pages=source_pages,
        mention_count=record.mention_count + 1,
        last_seen=today,
    )


def _promote_if_ready(record: CandidateRecord) -> CandidateRecord:
    if record.status != "discovered":
        return record
    if record.mention_count >= 2 or len(record.source_pages) >= 2:
        return replace(record, status="queued")
    return record


def _append_unique(values: tuple[str, ...], value: str) -> tuple[str, ...]:
    if value in values:
        return values
    return (*values, value)


def _record_to_json(record: CandidateRecord) -> dict[str, object]:
    return {
        "slug": record.slug,
        "display_name": record.display_name,
        "category_guess": record.category_guess,
        "aliases": list(record.aliases),
        "reasons": list(record.reasons),
        "source_pages": list(record.source_pages),
        "mention_count": record.mention_count,
        "status": record.status,
        "first_seen": record.first_seen,
        "last_seen": record.last_seen,
        "status_reason": record.status_reason,
    }


def _record_from_json(raw: Mapping[str, object]) -> CandidateRecord:
    return CandidateRecord(
        slug=str(raw["slug"]),
        display_name=str(raw["display_name"]),
        category_guess=str(raw["category_guess"]),
        aliases=_string_tuple(raw.get("aliases", [])),
        reasons=_string_tuple(raw.get("reasons", [])),
        source_pages=_string_tuple(raw.get("source_pages", [])),
        mention_count=_int(raw["mention_count"]),
        status=_status(str(raw["status"])),
        first_seen=str(raw["first_seen"]),
        last_seen=str(raw["last_seen"]),
        status_reason=str(raw.get("status_reason", "")),
    )


def _string_tuple(value: object) -> tuple[str, ...]:
    if not isinstance(value, list):
        return ()
    return tuple(str(item) for item in value)


def _int(value: object) -> int:
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        return int(value)
    raise ValueError(f"Expected integer JSON value, got {value!r}")


def _status(value: str) -> CandidateStatus:
    if value in {"discovered", "queued", "promoted", "rejected", "merged"}:
        return value  # type: ignore[return-value]
    raise ValueError(f"Unknown candidate status: {value}")
