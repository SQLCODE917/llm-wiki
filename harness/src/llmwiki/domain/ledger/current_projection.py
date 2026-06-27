"""Projection coverage for the current PagePlan-based ingest path."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.evidence_registry import EvidenceRegistry, SourceRange
from llmwiki.domain.ledger.canonical import deterministic_id, short_digest
from llmwiki.domain.ledger.coverage import (
    PageBodyBuilder,
    ProjectionCoverage,
    ProjectionCoverageEntry,
    clean_statement,
)
from llmwiki.domain.ledger.current_structure import source_range_by_unit
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.pointers import (
    claim_ledger_pointer,
    document_structure_pointer,
)
from llmwiki.domain.ledger.projection import ProjectionSourceSupport
from llmwiki.domain.objects import PagePlan, PlannedPageWrite, SourceClaim


@dataclass(frozen=True)
class CurrentProjectionCoverage:
    source_support: ProjectionSourceSupport
    page_body_hash: str
    coverage: ProjectionCoverage


def build_projection_source_support(
    *,
    source_locator: str,
    source_hash: str,
    claim_ledger_id: str,
    claim_ledger_fingerprint: str,
    document_structure_id: str,
    document_structure_fingerprint: str,
) -> ProjectionSourceSupport:
    return ProjectionSourceSupport(
        projection_source_support_id=deterministic_id(
            "projection-source-support", source_hash, claim_ledger_id
        ),
        source_hash=source_hash,
        source_locator=source_locator,
        claim_ledger_pointer=claim_ledger_pointer(claim_ledger_id, claim_ledger_fingerprint),
        document_structure_pointer=document_structure_pointer(
            document_structure_id, document_structure_fingerprint
        ),
    )


def build_current_projection_coverage(
    *,
    page_plan: PagePlan,
    evidence_registry: EvidenceRegistry,
    ledger: ClaimLedger,
    source_support: ProjectionSourceSupport,
) -> CurrentProjectionCoverage:
    ranges_by_unit = source_range_by_unit(page_plan, evidence_registry.source_ranges)
    claims_by_id = {claim.source_claim_id: claim for claim in page_plan.source_claims}
    entries_by_claim = claim_entry_by_source_claim_id(
        page_plan, evidence_registry, ledger, claims_by_id
    )
    builder = PageBodyBuilder()
    builder.add(f"# Planned projection: {page_plan.plan_id}\n\n")
    entries: list[ProjectionCoverageEntry] = []
    for write in page_plan.planned_writes:
        builder.add(f"## {write.page_metadata.page_id}\n\n")
        _append_claim_entries(builder, entries, page_plan, write, entries_by_claim, claims_by_id)
        _append_atom_entries(builder, entries, page_plan, write, ledger, ranges_by_unit)
        _append_review_entries(builder, entries, page_plan, write, ledger, ranges_by_unit)
    return CurrentProjectionCoverage(
        source_support=source_support,
        page_body_hash=short_digest(builder.text(), 32),
        coverage=ProjectionCoverage(tuple(entries)),
    )


def claim_entry_by_source_claim_id(
    page_plan: PagePlan,
    evidence_registry: EvidenceRegistry,
    ledger: ClaimLedger,
    claims_by_id: dict[str, SourceClaim] | None = None,
) -> dict[str, LedgerEntry]:
    ranges_by_unit = source_range_by_unit(page_plan, evidence_registry.source_ranges)
    claims = claims_by_id or {claim.source_claim_id: claim for claim in page_plan.source_claims}
    usable_claim_entries = [
        entry
        for entry in ledger.entries
        if entry.ledger_entry_kind in {"claim", "event", "concept", "relationship", "quotation"}
    ]
    result: dict[str, LedgerEntry] = {}
    for claim_id, claim in claims.items():
        source_range = ranges_by_unit.get(claim.extracted_unit_id)
        if source_range is None:
            continue
        for entry in usable_claim_entries:
            if (
                entry.source_range_id == source_range.source_range_id
                and entry.source_text == claim.statement
            ):
                result[claim_id] = entry
                break
    return result


def write_source_range_ids(
    write: PlannedPageWrite, ranges_by_unit: dict[str, SourceRange]
) -> frozenset[str]:
    return frozenset(
        source_range.source_range_id
        for unit_id in write.extracted_units
        if (source_range := ranges_by_unit.get(unit_id)) is not None
    )


def _append_claim_entries(
    builder: PageBodyBuilder,
    entries: list[ProjectionCoverageEntry],
    page_plan: PagePlan,
    write: PlannedPageWrite,
    entries_by_claim: dict[str, LedgerEntry],
    claims_by_id: dict[str, SourceClaim],
) -> None:
    for claim_id in _write_claim_ids(page_plan, write):
        claim = claims_by_id.get(claim_id)
        entry = entries_by_claim.get(claim_id)
        if claim is None or entry is None:
            continue
        text_range = builder.add(
            f"- {clean_statement(entry.normalized_text or entry.source_text)}\n"
        )
        entries.append(
            ProjectionCoverageEntry(
                projection_coverage_entry_id=deterministic_id(
                    "projection-coverage-entry",
                    page_plan.plan_id,
                    write.write_id,
                    "generated-page-claim",
                    entry.ledger_entry_id,
                ),
                projection_coverage_unit_kind="generated-page-claim",
                page_text_range=text_range,
                selected_ledger_entry_ids=(entry.ledger_entry_id,),
            )
        )


def _append_atom_entries(
    builder: PageBodyBuilder,
    entries: list[ProjectionCoverageEntry],
    page_plan: PagePlan,
    write: PlannedPageWrite,
    ledger: ClaimLedger,
    ranges_by_unit: dict[str, SourceRange],
) -> None:
    write_ranges = write_source_range_ids(write, ranges_by_unit)
    if not write_ranges:
        return
    for entry in ledger.usable_entries:
        if entry.ledger_entry_kind != "technical-atom" or entry.source_range_id not in write_ranges:
            continue
        text_range = builder.add(f"- Technical {entry.technical_atom_kind} atom\n")
        entries.append(
            ProjectionCoverageEntry(
                projection_coverage_entry_id=deterministic_id(
                    "projection-coverage-entry",
                    page_plan.plan_id,
                    write.write_id,
                    "rendered-technical-atom-block",
                    entry.technical_atom_id,
                ),
                projection_coverage_unit_kind="rendered-technical-atom-block",
                page_text_range=text_range,
                technical_atom_id=entry.technical_atom_id,
            )
        )


def _append_review_entries(
    builder: PageBodyBuilder,
    entries: list[ProjectionCoverageEntry],
    page_plan: PagePlan,
    write: PlannedPageWrite,
    ledger: ClaimLedger,
    ranges_by_unit: dict[str, SourceRange],
) -> None:
    write_ranges = write_source_range_ids(write, ranges_by_unit)
    for entry in ledger.needs_review_entries:
        if entry.source_range_id not in write_ranges:
            continue
        text_range = builder.add(f"- Needs review: {clean_statement(entry.source_text)}\n")
        entries.append(
            ProjectionCoverageEntry(
                projection_coverage_entry_id=deterministic_id(
                    "projection-coverage-entry",
                    page_plan.plan_id,
                    write.write_id,
                    "source-review-item",
                    entry.ledger_entry_id,
                ),
                projection_coverage_unit_kind="source-review-item",
                page_text_range=text_range,
                ledger_entry_id=entry.ledger_entry_id,
            )
        )


def _write_claim_ids(page_plan: PagePlan, write: PlannedPageWrite) -> tuple[str, ...]:
    if write.source_summary_plan is not None:
        return write.source_summary_plan.selected_source_claims
    unit_ids = frozenset(write.extracted_units)
    return tuple(
        claim.source_claim_id
        for claim in page_plan.source_claims
        if claim.extracted_unit_id in unit_ids
    )
