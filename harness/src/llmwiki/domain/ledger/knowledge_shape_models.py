"""Domain records for source-agnostic knowledge shapes."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class KnowledgeShapeCandidate:
    shape_kind: str
    knowledge_shape_id: str
    label: str
    structure_node_id: str
    source_range_id: str
    entry_ids: tuple[str, ...]
    atom_ids: tuple[str, ...]
    child_structure_node_ids: tuple[str, ...]
    evidence_roles: tuple[str, ...]
    score: int


@dataclass(frozen=True)
class KnowledgeShapeCatalog:
    knowledge_shape_catalog_id: str
    knowledge_shape_catalog_fingerprint: str
    source_locator: str
    source_hash: str
    candidates: tuple[KnowledgeShapeCandidate, ...]

    def candidates_of_kind(self, shape_kind: str) -> tuple[KnowledgeShapeCandidate, ...]:
        return tuple(item for item in self.candidates if item.shape_kind == shape_kind)
