"""LedgerProjectionPlanner: select usable ledger entries for a SourceWikiPage.

The planner builds the source-structure spine from the document structure,
orders sections by source order, and routes usable claim-like entries to
generated page claims and usable technical-atom entries to rendered atom
blocks within their nearest section. needs-review entries become source review
items; rejected and non-claim units become disposition counts. Only usable
entries reach prose.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.pointers import PortableArtifactPointer
from llmwiki.domain.ledger.structure import DocumentStructure

_CLAIM_KINDS = ("claim", "event", "concept", "relationship", "quotation")


@dataclass(frozen=True)
class ProjectionSourceSupport:
    projection_source_support_id: str
    source_hash: str
    source_locator: str
    claim_ledger_pointer: PortableArtifactPointer
    document_structure_pointer: PortableArtifactPointer


@dataclass(frozen=True)
class PlannedClaim:
    selected_ledger_entry_ids: tuple[str, ...]
    text: str
    citation_label: str


@dataclass(frozen=True)
class PlannedAtomBlock:
    technical_atom_id: str
    source_order: int
    citation_label: str


@dataclass(frozen=True)
class PlannedSection:
    structure_node_id: str
    heading_text: str
    depth: int
    source_order: int
    claims: tuple[PlannedClaim, ...]
    atom_blocks: tuple[PlannedAtomBlock, ...]


@dataclass(frozen=True)
class PlannedReviewItem:
    ledger_entry_id: str
    text: str
    citation_label: str
    review_reason_kind: str
    review_reason_detail: str


@dataclass(frozen=True)
class PlannedDispositionCount:
    disposition: str
    count: int


@dataclass(frozen=True)
class LedgerProjectionPlan:
    wiki_page_locator: str
    page_kind: str
    title: str
    source_support: ProjectionSourceSupport
    sections: tuple[PlannedSection, ...]
    review_items: tuple[PlannedReviewItem, ...]
    disposition_counts: tuple[PlannedDispositionCount, ...]


def plan_source_page(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    *,
    wiki_page_locator: str,
    title: str,
    source_support: ProjectionSourceSupport,
) -> LedgerProjectionPlan:
    nearest = _entries_by_nearest_node(ledger, structure)
    sections: list[PlannedSection] = []
    for node in sorted(structure.structure_nodes, key=lambda n: n.source_order):
        entries = nearest.get(node.structure_node_id, [])
        claims = tuple(
            PlannedClaim((entry_id,), text, label)
            for entry_id, text, label in _claim_units(entries)
        )
        atom_blocks = tuple(
            PlannedAtomBlock(atom_id, order, label)
            for atom_id, order, label in _atom_units(ledger, entries)
        )
        if node.structure_node_kind == "root" and not claims and not atom_blocks:
            continue
        heading = title if node.structure_node_kind == "root" else node.heading_text
        sections.append(
            PlannedSection(
                node.structure_node_id, heading, node.depth, node.source_order, claims, atom_blocks
            )
        )
    review_items = tuple(
        PlannedReviewItem(
            entry.ledger_entry_id,
            entry.source_text,
            _citation(entry.source_locator, entry.source_range_id),
            entry.review_reason.reason_kind if entry.review_reason else "needs-review",
            entry.review_reason.detail if entry.review_reason else "",
        )
        for entry in ledger.needs_review_entries
    )
    counts = structure.disposition_counts()
    disposition_counts = tuple(
        PlannedDispositionCount(disposition, counts[disposition])
        for disposition in ("rejected", "non-claim")
        if counts.get(disposition)
    )
    return LedgerProjectionPlan(
        wiki_page_locator=wiki_page_locator,
        page_kind="source",
        title=title,
        source_support=source_support,
        sections=tuple(sections),
        review_items=review_items,
        disposition_counts=disposition_counts,
    )


def _entries_by_nearest_node(
    ledger: ClaimLedger, structure: DocumentStructure
) -> dict[str, list[LedgerEntry]]:
    by_node: dict[str, list[LedgerEntry]] = {}
    for entry in ledger.usable_entries:
        node_id = (
            entry.structure_node_ids[0] if entry.structure_node_ids else structure.root_node_id
        )
        by_node.setdefault(node_id, []).append(entry)
    return by_node


def _claim_units(entries: list[LedgerEntry]) -> list[tuple[str, str, str]]:
    units = []
    for entry in entries:
        if entry.ledger_entry_kind not in _CLAIM_KINDS:
            continue
        text = entry.normalized_text or entry.source_text
        if not text.strip():
            continue
        units.append(
            (
                entry.ledger_entry_id,
                text.strip(),
                _citation(entry.source_locator, entry.source_range_id),
            )
        )
    return units


def _atom_units(ledger: ClaimLedger, entries: list[LedgerEntry]) -> list[tuple[str, int, str]]:
    units = []
    for entry in entries:
        if entry.ledger_entry_kind != "technical-atom":
            continue
        units.append(
            (
                entry.technical_atom_id,
                _source_order(ledger, entry.source_range_id),
                _citation(entry.source_locator, entry.source_range_id),
            )
        )
    return sorted(units, key=lambda item: item[1])


def _source_order(ledger: ClaimLedger, source_range_id: str) -> int:
    for index, statement in enumerate(ledger.source_statements):
        if statement.source_range_id == source_range_id:
            return index
    return 0


def _citation(source_locator: str, source_range_id: str) -> str:
    return f"{source_locator} ({source_range_id})"
