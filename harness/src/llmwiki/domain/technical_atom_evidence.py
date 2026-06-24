"""Evidence selectors used while building TechnicalAtom records."""

from __future__ import annotations

from llmwiki.domain.evidence_registry import EvidenceRecord


def records_by_claim(
    records: tuple[EvidenceRecord, ...],
) -> dict[str, tuple[EvidenceRecord, ...]]:
    grouped: dict[str, list[EvidenceRecord]] = {}
    for record in records:
        if record.source_claim_id:
            grouped.setdefault(record.source_claim_id, []).append(record)
    return {claim_id: tuple(items) for claim_id, items in grouped.items()}


def records_by_range(
    records: tuple[EvidenceRecord, ...],
) -> dict[str, tuple[EvidenceRecord, ...]]:
    grouped: dict[str, list[EvidenceRecord]] = {}
    for record in records:
        grouped.setdefault(record.source_range_id, []).append(record)
    return {range_id: tuple(items) for range_id, items in grouped.items()}


def selected_source_claim_ids(
    source_claim_ids: tuple[str, ...], records: tuple[EvidenceRecord, ...]
) -> tuple[str, ...]:
    if source_claim_ids:
        return tuple(dict.fromkeys(source_claim_ids))
    return tuple(
        dict.fromkeys(record.source_claim_id for record in records if record.source_claim_id)
    )[:3]


def records_for_evidence_ids(
    records: tuple[EvidenceRecord, ...], evidence_ids: tuple[str, ...]
) -> tuple[EvidenceRecord, ...]:
    selected = set(evidence_ids)
    return tuple(record for record in records if record.evidence_id in selected)
