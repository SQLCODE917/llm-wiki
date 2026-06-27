"""SourceCoverageArtifact domain records.

Coverage is a ledger-side audit of source extraction: every source element is
either tied to source ranges and downstream objects, or excluded by a reusable
structural reason. It is not a quality gate; it makes early data loss visible.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.builder import SegmentInput
from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.structure import DocumentStructure


@dataclass(frozen=True)
class SourceElementRecord:
    source_element_id: str
    element_kind: str
    body_state: str
    heading_path: str
    page_locator: str
    has_source_text: bool


@dataclass(frozen=True)
class SourceElementCoverageRecord:
    source_element_id: str
    element_kind: str
    body_state: str
    heading_path: str
    page_locator: str
    coverage_status: str
    coverage_kind: str
    source_range_ids: tuple[str, ...] = ()
    extracted_unit_disposition: str = ""
    ledger_entry_ids: tuple[str, ...] = ()
    technical_atom_ids: tuple[str, ...] = ()
    structure_node_ids: tuple[str, ...] = ()
    excluded_reason: str = ""


@dataclass(frozen=True)
class SourceCoverage:
    source_locator: str
    source_hash: str
    total_elements: int
    covered_elements: int
    excluded_elements: int
    gap_elements: int
    records: tuple[SourceElementCoverageRecord, ...]


def build_source_coverage(
    *,
    source_locator: str,
    source_hash: str,
    elements: tuple[SourceElementRecord, ...],
    segments: tuple[SegmentInput, ...],
    ledger: ClaimLedger,
    structure: DocumentStructure,
) -> SourceCoverage:
    range_by_element = _ranges_by_element(segments)
    entries_by_range = _entries_by_range(ledger)
    atoms_by_range = _atoms_by_range(ledger)
    nodes_by_range = _nodes_by_range(structure)
    disposition_by_range = {
        record.source_range_id: record.disposition for record in structure.dispositions
    }
    records = tuple(
        _record(
            element,
            range_by_element.get(element.source_element_id, ()),
            entries_by_range,
            atoms_by_range,
            nodes_by_range,
            disposition_by_range,
        )
        for element in elements
    )
    excluded = sum(1 for record in records if record.coverage_status == "excluded")
    gaps = sum(1 for record in records if record.coverage_status == "gap")
    return SourceCoverage(
        source_locator=source_locator,
        source_hash=source_hash,
        total_elements=len(records),
        covered_elements=len(records) - excluded - gaps,
        excluded_elements=excluded,
        gap_elements=gaps,
        records=records,
    )


def source_coverage_id(coverage: SourceCoverage) -> str:
    return deterministic_id("source-coverage", coverage.source_hash, coverage.source_locator)


def _record(
    element: SourceElementRecord,
    source_range_ids: tuple[str, ...],
    entries_by_range: dict[str, tuple[str, ...]],
    atoms_by_range: dict[str, tuple[str, ...]],
    nodes_by_range: dict[str, tuple[str, ...]],
    disposition_by_range: dict[str, str],
) -> SourceElementCoverageRecord:
    if source_range_ids:
        return SourceElementCoverageRecord(
            source_element_id=element.source_element_id,
            element_kind=element.element_kind,
            body_state=element.body_state,
            heading_path=element.heading_path,
            page_locator=element.page_locator,
            coverage_status="covered",
            coverage_kind=_coverage_kind(source_range_ids, entries_by_range, atoms_by_range),
            source_range_ids=source_range_ids,
            extracted_unit_disposition=_first(disposition_by_range, source_range_ids),
            ledger_entry_ids=_collect(entries_by_range, source_range_ids),
            technical_atom_ids=_collect(atoms_by_range, source_range_ids),
            structure_node_ids=_collect(nodes_by_range, source_range_ids),
        )
    status, kind, reason = _excluded_or_gap(element)
    return SourceElementCoverageRecord(
        source_element_id=element.source_element_id,
        element_kind=element.element_kind,
        body_state=element.body_state,
        heading_path=element.heading_path,
        page_locator=element.page_locator,
        coverage_status=status,
        coverage_kind=kind,
        excluded_reason=reason,
    )


def _coverage_kind(
    source_range_ids: tuple[str, ...],
    entries_by_range: dict[str, tuple[str, ...]],
    atoms_by_range: dict[str, tuple[str, ...]],
) -> str:
    if _collect(atoms_by_range, source_range_ids):
        return "technical-atom"
    if _collect(entries_by_range, source_range_ids):
        return "ledger-entry"
    return "segment"


def _excluded_or_gap(element: SourceElementRecord) -> tuple[str, str, str]:
    if element.body_state != "body":
        return ("excluded", "excluded-furniture", "non-body element")
    if element.element_kind == "table_of_contents":
        return ("excluded", "excluded-table-of-contents", "table-of-contents element")
    if not element.has_source_text:
        return ("excluded", "excluded-empty", "empty body element")
    return ("gap", "uncovered-body", "body element not represented by a segment")


def _ranges_by_element(segments: tuple[SegmentInput, ...]) -> dict[str, tuple[str, ...]]:
    mapped: dict[str, list[str]] = {}
    for item in segments:
        for element_id in item.segment.source_element_ids:
            mapped.setdefault(element_id, []).append(item.segment.source_range_id)
    return {key: tuple(values) for key, values in mapped.items()}


def _entries_by_range(ledger: ClaimLedger) -> dict[str, tuple[str, ...]]:
    mapped: dict[str, list[str]] = {}
    for entry in ledger.entries:
        mapped.setdefault(entry.source_range_id, []).append(entry.ledger_entry_id)
    return {key: tuple(values) for key, values in mapped.items()}


def _atoms_by_range(ledger: ClaimLedger) -> dict[str, tuple[str, ...]]:
    mapped: dict[str, list[str]] = {}
    for atom in ledger.technical_atoms:
        mapped.setdefault(atom.source_range_id, []).append(atom.technical_atom_id)
    return {key: tuple(values) for key, values in mapped.items()}


def _nodes_by_range(structure: DocumentStructure) -> dict[str, tuple[str, ...]]:
    mapped: dict[str, list[str]] = {}
    for node in structure.structure_nodes:
        mapped.setdefault(node.source_range_id, []).append(node.structure_node_id)
    return {key: tuple(values) for key, values in mapped.items()}


def _collect(
    mapping: dict[str, tuple[str, ...]], source_range_ids: tuple[str, ...]
) -> tuple[str, ...]:
    return tuple(value for range_id in source_range_ids for value in mapping.get(range_id, ()))


def _first(mapping: dict[str, str], source_range_ids: tuple[str, ...]) -> str:
    for range_id in source_range_ids:
        if range_id in mapping:
            return mapping[range_id]
    return ""
