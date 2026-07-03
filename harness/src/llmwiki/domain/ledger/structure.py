"""Document structure: the authoritative extracted source organization.

``DocumentStructure`` is a sibling artifact to the claim ledger. It stores the
source's organization (headings, chapters, sections, glossary/index/reference
entries) — never subject-matter claims — plus the disposition assigned to each
extracted unit. Structurally flat sources get a root-only structure.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from functools import cached_property


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

    @cached_property
    def _nodes_by_id(self) -> dict[str, StructureNode]:
        return {node.structure_node_id: node for node in self.structure_nodes}

    @cached_property
    def _children_by_parent_id(self) -> dict[str, tuple[StructureNode, ...]]:
        grouped: dict[str, list[StructureNode]] = defaultdict(list)
        for node in self.structure_nodes:
            if node.parent_structure_node_id:
                grouped[node.parent_structure_node_id].append(node)
        return {
            parent_id: tuple(sorted(children, key=lambda item: item.source_order))
            for parent_id, children in grouped.items()
        }

    def node(self, node_id: str) -> StructureNode | None:
        return self._nodes_by_id.get(node_id)

    def parent(self, node_id: str) -> StructureNode | None:
        node = self.node(node_id)
        if node is None or not node.parent_structure_node_id:
            return None
        return self.node(node.parent_structure_node_id)

    def children(self, node_id: str) -> tuple[StructureNode, ...]:
        return self._children_by_parent_id.get(node_id, ())

    def descendants(self, node_id: str) -> tuple[StructureNode, ...]:
        descendants: list[StructureNode] = []
        pending = list(reversed(self.children(node_id)))
        while pending:
            current = pending.pop()
            descendants.append(current)
            pending.extend(reversed(self.children(current.structure_node_id)))
        return tuple(sorted(descendants, key=lambda item: item.source_order))

    def label_path(self, node_id: str, *, include_root: bool = False) -> tuple[str, ...]:
        labels: list[str] = []
        for ancestor_id in reversed(self.ancestry(node_id)):
            node = self.node(ancestor_id)
            if node is None:
                continue
            if node.structure_node_kind == "root" and not include_root:
                continue
            if node.heading_text.strip():
                labels.append(node.heading_text.strip())
        return tuple(labels)

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
