"""Document structure: the authoritative extracted source organization.

``DocumentStructure`` is a sibling artifact to the claim ledger. It stores the
source's organization (headings, chapters, sections, glossary/index/reference
entries) — never subject-matter claims — plus the disposition assigned to each
extracted unit. Structurally flat sources get a root-only structure.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class StructureNode:
    structure_node_id: str
    structure_node_kind: str
    heading_text: str
    source_range_id: str
    source_locator: str
    source_order: int
    depth: int = 0
    parent_structure_node_id: str = ""
    evidence_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class ExtractedUnitDispositionRecord:
    extracted_unit_id: str
    source_range_id: str
    disposition: str
    source_order: int = 0


@dataclass(frozen=True)
class DocumentStructure:
    root_node_id: str
    structure_nodes: tuple[StructureNode, ...]
    dispositions: tuple[ExtractedUnitDispositionRecord, ...] = ()

    def node(self, node_id: str) -> StructureNode | None:
        for candidate in self.structure_nodes:
            if candidate.structure_node_id == node_id:
                return candidate
        return None

    def ancestry(self, node_id: str) -> tuple[str, ...]:
        """Node ids from the given node outward to the root (nearest first)."""
        chain: list[str] = []
        current = self.node(node_id)
        seen: set[str] = set()
        while current is not None and current.structure_node_id not in seen:
            seen.add(current.structure_node_id)
            chain.append(current.structure_node_id)
            if not current.parent_structure_node_id:
                break
            current = self.node(current.parent_structure_node_id)
        return tuple(chain)

    def disposition_counts(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for record in self.dispositions:
            counts[record.disposition] = counts.get(record.disposition, 0) + 1
        return counts
