"""Shared helpers for compiler page candidate planning."""

from __future__ import annotations

from collections import defaultdict

from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.page_publication import PageCandidate
from llmwiki.domain.ledger.page_title_lint import lint_page_title
from llmwiki.domain.pages import PageError, slugify
from llmwiki.domain.source_map import NormalizedSourceMap
from llmwiki.domain.typed_evidence import TypedEvidenceRecord


def page_candidate(
    source_page_id: str,
    source_map: NormalizedSourceMap,
    source_profile_kind: str,
    title: str,
    page_kind: str,
    page_family: str,
    origin: str,
    support: tuple[str, ...],
    source_order: int,
    *,
    slug_prefix: str = "",
) -> PageCandidate:
    slug = safe_slug(title)
    page_id = (
        f"{source_page_id}-{slug}"
        if not slug_prefix
        else f"{source_page_id}-{slug_prefix}-{slug}"
    )
    return PageCandidate(
        page_candidate_id=deterministic_id(
            "page-candidate", source_map.source_hash, page_id, origin
        ),
        source_id=source_page_id,
        source_hash=source_map.source_hash,
        source_profile_kind=source_profile_kind,
        page_id=page_id,
        title=title,
        page_kind=page_kind,
        page_family=page_family,
        origin=origin,
        rank_score=float(len(support)),
        source_order=source_order,
        supporting_evidence_record_ids=support,
        title_findings=lint_page_title(title, page_id, page_family),
    )


def topic_records(records: tuple[TypedEvidenceRecord, ...]) -> tuple[TypedEvidenceRecord, ...]:
    return tuple(
        record
        for record in records
        if record.evidence_record_type
        in {
            "argument",
            "code_example",
            "definition",
            "entity_fact",
            "formula",
            "rule",
            "table_fact",
        }
    )


def recipe_records(records: tuple[TypedEvidenceRecord, ...]) -> tuple[TypedEvidenceRecord, ...]:
    return tuple(
        record
        for record in records
        if record.evidence_record_type
        in {"argument", "code_example", "definition", "procedure_step"}
    )


def recipe_support(records: tuple[TypedEvidenceRecord, ...]) -> bool:
    recipe = recipe_records(records)
    return (
        any(record.evidence_record_type == "code_example" for record in recipe)
        and len(recipe) >= 2
    )


def records_of_type(
    records: tuple[TypedEvidenceRecord, ...], record_type: str
) -> tuple[TypedEvidenceRecord, ...]:
    return tuple(record for record in records if record.evidence_record_type == record_type)


def top_level_groups(
    groups: dict[str, tuple[TypedEvidenceRecord, ...]]
) -> dict[str, tuple[TypedEvidenceRecord, ...]]:
    top: dict[str, list[TypedEvidenceRecord]] = defaultdict(list)
    for section, records in groups.items():
        top[section.split(" / ", 1)[0]].extend(records)
    return {section: tuple(records) for section, records in top.items()}


def section_title(section: str, source_locator: str) -> str:
    label = section.split(" / ")[-1].strip() if section else ""
    if label and label != "Overview":
        return label
    return source_locator.rsplit(".", 1)[0].replace("-", " ").replace("_", " ").title()


def source_order(
    source_map: NormalizedSourceMap, records: tuple[TypedEvidenceRecord, ...]
) -> int:
    block_by_id = source_map.source_blocks_by_id
    orders = [
        block_by_id[block_id].source_order
        for record in records
        for block_id in record.source_block_ids
        if block_id in block_by_id
    ]
    return min(orders) if orders else 10_000


def safe_slug(title: str) -> str:
    try:
        return slugify(title)
    except PageError:
        return "untitled"


def dedupe_candidates(candidates: list[PageCandidate]) -> tuple[PageCandidate, ...]:
    by_id: dict[str, PageCandidate] = {}
    for candidate in candidates:
        current = by_id.get(candidate.page_id)
        if current is None or len(candidate.supporting_evidence_record_ids) > len(
            current.supporting_evidence_record_ids
        ):
            by_id[candidate.page_id] = candidate
    return tuple(sorted(by_id.values(), key=lambda item: (item.source_order, item.page_id)))
