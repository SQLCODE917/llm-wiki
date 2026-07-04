"""Plan public page candidates directly from typed evidence and source blocks."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

from llmwiki.domain.ledger.page_publication import (
    PAGE_FAMILY_BROAD_TOPIC,
    PAGE_FAMILY_COLLECTION_PAGE,
    PAGE_FAMILY_PROCEDURE_GUIDE,
    PAGE_FAMILY_RECIPE_PATTERN,
    PAGE_FAMILY_SECTION_REFERENCE,
    PAGE_FAMILY_TOPIC_CONCEPT,
    PageCandidate,
)
from llmwiki.domain.source_map import NormalizedSourceMap
from llmwiki.domain.typed_evidence import EvidenceRecordSet, TypedEvidenceRecord
from llmwiki.runtime.compiler_candidate_helpers import (
    dedupe_candidates,
    page_candidate,
    recipe_records,
    recipe_support,
    records_of_type,
    section_title,
    source_order,
    top_level_groups,
    topic_records,
)


@dataclass(frozen=True)
class CompilerPageCandidateInputs:
    candidates: tuple[PageCandidate, ...]


def build_compiler_page_candidates(
    *,
    source_page_id: str,
    source_map: NormalizedSourceMap,
    record_set: EvidenceRecordSet,
    source_profile_kind: str,
) -> CompilerPageCandidateInputs:
    records = record_set.accepted_records
    by_section = _records_by_section(source_map, records)
    candidates: list[PageCandidate] = []
    candidates.extend(
        _topic_candidate(source_page_id, source_map, source_profile_kind, section, items)
        for section, items in by_section.items()
        if len(topic_records(items)) >= 2
    )
    candidates.extend(
        _procedure_candidate(source_page_id, source_map, source_profile_kind, section, items)
        for section, items in by_section.items()
        if len(records_of_type(items, "procedure_step")) >= 2
    )
    candidates.extend(
        _recipe_candidate(source_page_id, source_map, source_profile_kind, section, items)
        for section, items in by_section.items()
        if recipe_support(items)
    )
    candidates.extend(
        _collection_candidate(source_page_id, source_map, source_profile_kind, section, items)
        for section, items in top_level_groups(by_section).items()
        if len(items) >= 3
    )
    candidates.extend(
        _section_candidate(source_page_id, source_map, source_profile_kind, section, items)
        for section, items in by_section.items()
        if items
    )
    broad = _broad_candidate(source_page_id, source_map, source_profile_kind, records)
    if broad is not None:
        candidates.append(broad)
    return CompilerPageCandidateInputs(tuple(dedupe_candidates(candidates)))


def _records_by_section(
    source_map: NormalizedSourceMap, records: tuple[TypedEvidenceRecord, ...]
) -> dict[str, tuple[TypedEvidenceRecord, ...]]:
    block_by_id = source_map.source_blocks_by_id
    groups: dict[str, list[TypedEvidenceRecord]] = defaultdict(list)
    for record in records:
        block = next(
            (
                block_by_id[block_id]
                for block_id in record.source_block_ids
                if block_id in block_by_id
            ),
            None,
        )
        section = block.section_path if block is not None and block.section_path else "Overview"
        groups[section].append(record)
    return {section: tuple(items) for section, items in groups.items()}


def _topic_candidate(
    source_page_id: str,
    source_map: NormalizedSourceMap,
    source_profile_kind: str,
    section: str,
    records: tuple[TypedEvidenceRecord, ...],
) -> PageCandidate:
    title = section_title(section, source_map.source_locator)
    support = tuple(record.typed_evidence_record_id for record in topic_records(records))
    return page_candidate(
        source_page_id,
        source_map,
        source_profile_kind,
        title,
        "concept",
        PAGE_FAMILY_TOPIC_CONCEPT,
        "typed-evidence-topic",
        support,
        source_order(source_map, records),
    )


def _procedure_candidate(
    source_page_id: str,
    source_map: NormalizedSourceMap,
    source_profile_kind: str,
    section: str,
    records: tuple[TypedEvidenceRecord, ...],
) -> PageCandidate:
    title = section_title(section, source_map.source_locator)
    support = tuple(record.typed_evidence_record_id for record in records)
    return page_candidate(
        source_page_id,
        source_map,
        source_profile_kind,
        title,
        "procedure",
        PAGE_FAMILY_PROCEDURE_GUIDE,
        "typed-evidence-procedure",
        support,
        source_order(source_map, records),
        slug_prefix="procedure",
    )


def _recipe_candidate(
    source_page_id: str,
    source_map: NormalizedSourceMap,
    source_profile_kind: str,
    section: str,
    records: tuple[TypedEvidenceRecord, ...],
) -> PageCandidate:
    title = section_title(section, source_map.source_locator)
    support = tuple(record.typed_evidence_record_id for record in recipe_records(records))
    return page_candidate(
        source_page_id,
        source_map,
        source_profile_kind,
        title,
        "recipe",
        PAGE_FAMILY_RECIPE_PATTERN,
        "typed-evidence-recipe",
        support,
        source_order(source_map, records),
        slug_prefix="recipe",
    )


def _collection_candidate(
    source_page_id: str,
    source_map: NormalizedSourceMap,
    source_profile_kind: str,
    section: str,
    records: tuple[TypedEvidenceRecord, ...],
) -> PageCandidate:
    title = section_title(section, source_map.source_locator)
    support = tuple(record.typed_evidence_record_id for record in records)
    return page_candidate(
        source_page_id,
        source_map,
        source_profile_kind,
        title,
        "source",
        PAGE_FAMILY_COLLECTION_PAGE,
        "typed-evidence-collection",
        support,
        source_order(source_map, records),
        slug_prefix="collection",
    )


def _section_candidate(
    source_page_id: str,
    source_map: NormalizedSourceMap,
    source_profile_kind: str,
    section: str,
    records: tuple[TypedEvidenceRecord, ...],
) -> PageCandidate:
    title = section_title(section, source_map.source_locator)
    support = tuple(record.typed_evidence_record_id for record in records)
    return page_candidate(
        source_page_id,
        source_map,
        source_profile_kind,
        title,
        "source",
        PAGE_FAMILY_SECTION_REFERENCE,
        "typed-evidence-section",
        support,
        source_order(source_map, records),
        slug_prefix="section",
    )


def _broad_candidate(
    source_page_id: str,
    source_map: NormalizedSourceMap,
    source_profile_kind: str,
    records: tuple[TypedEvidenceRecord, ...],
) -> PageCandidate | None:
    if len(records) < 8:
        return None
    title = f"{section_title('', source_map.source_locator)} Overview"
    support = tuple(record.typed_evidence_record_id for record in records[:16])
    return page_candidate(
        source_page_id,
        source_map,
        source_profile_kind,
        title,
        "concept",
        PAGE_FAMILY_BROAD_TOPIC,
        "typed-evidence-broad-topic",
        support,
        source_order(source_map, records),
        slug_prefix="overview",
    )
