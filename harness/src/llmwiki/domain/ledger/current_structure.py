"""Document-structure helpers for current-artifact claim ledgers."""

from __future__ import annotations

from llmwiki.domain.evidence_registry import EvidenceRegistry, SourceRange
from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.structure import (
    DocumentStructure,
    ExtractedUnitDispositionRecord,
    StructureNode,
)
from llmwiki.domain.objects import PagePlan


def build_current_document_structure(
    *,
    source_locator: str,
    source_hash: str,
    page_plan: PagePlan,
    evidence_registry: EvidenceRegistry,
) -> DocumentStructure:
    root_id = deterministic_id("structure-node", source_hash, source_locator, "root")
    nodes = [StructureNode(root_id, "root", source_locator, "root", source_locator, 0)]
    for order, source_range in enumerate(evidence_registry.source_ranges, start=1):
        nodes.append(_node(source_hash, source_range, order, root_id))
    return DocumentStructure(
        root_id,
        tuple(nodes),
        _dispositions(page_plan, evidence_registry.source_ranges),
    )


def current_source_hash(
    source_locator: str, page_plan: PagePlan, evidence_registry: EvidenceRegistry
) -> str:
    for source_text in evidence_registry.source_texts:
        if source_text.source_locator == source_locator:
            return source_text.source_hash
    for unit in page_plan.extracted_units:
        if unit.raw_source.source_locator == source_locator and unit.source_hash:
            return unit.source_hash
    return deterministic_id("source-hash", source_locator)


def source_hash_for_range(registry: EvidenceRegistry, source_range: SourceRange) -> str:
    for source_text in registry.source_texts:
        if source_text.source_locator == source_range.source_locator:
            return source_text.source_hash
    return ""


def source_range_by_unit(
    page_plan: PagePlan, source_ranges: tuple[SourceRange, ...]
) -> dict[str, SourceRange]:
    ranges_by_page = {source_range.page_id: source_range for source_range in source_ranges}
    result: dict[str, SourceRange] = {}
    for write in page_plan.planned_writes:
        source_range = ranges_by_page.get(write.page_metadata.page_id)
        if source_range is None:
            continue
        for unit_id in write.extracted_units:
            result.setdefault(unit_id, source_range)
    return result


def node_by_page(structure: DocumentStructure) -> dict[str, str]:
    result: dict[str, str] = {}
    for node in structure.structure_nodes:
        if node.source_range_id.startswith("source-range-"):
            result[node.source_range_id.removeprefix("source-range-")] = node.structure_node_id
    return result


def _node(
    source_hash: str, source_range: SourceRange, source_order: int, root_id: str
) -> StructureNode:
    heading = source_range.heading_path.strip() or source_range.page_id
    return StructureNode(
        structure_node_id=deterministic_id(
            "structure-node", source_hash, source_range.source_range_id
        ),
        structure_node_kind="section",
        heading_text=heading,
        source_range_id=source_range.source_range_id,
        source_locator=source_range.source_locator,
        source_order=source_order,
        depth=1,
        parent_structure_node_id=root_id,
    )


def _dispositions(
    page_plan: PagePlan, source_ranges: tuple[SourceRange, ...]
) -> tuple[ExtractedUnitDispositionRecord, ...]:
    ranges = source_range_by_unit(page_plan, source_ranges)
    eligible_units = {
        claim.extracted_unit_id
        for claim in page_plan.source_claims
        if claim.claim_eligibility == "eligible"
    }
    records: list[ExtractedUnitDispositionRecord] = []
    for order, unit in enumerate(page_plan.extracted_units, start=1):
        source_range = ranges.get(unit.unit_id)
        if source_range is None:
            continue
        disposition = "accepted" if unit.unit_id in eligible_units else "non-claim"
        records.append(
            ExtractedUnitDispositionRecord(
                unit.unit_id, source_range.source_range_id, disposition, order
            )
        )
    return tuple(records)
