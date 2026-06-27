"""Build a DocumentStructure from ordered source segments.

Heading segments become structure nodes; their depth comes from the heading
level (a reusable structural signal), so the nesting is source-neutral. Every
other segment is mapped to its nearest containing heading node, or the root
node when a source is structurally flat.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.canonical import deterministic_id, short_digest
from llmwiki.domain.ledger.segments import SourceSegment
from llmwiki.domain.ledger.structure import StructureNode

_DEPTH_KIND = {1: "chapter", 2: "section"}


@dataclass(frozen=True)
class StructurePlan:
    root_node_id: str
    nodes: tuple[StructureNode, ...]
    node_for_segment: dict[str, str]


def build_structure(
    source_hash: str, source_locator: str, segments: tuple[SourceSegment, ...]
) -> StructurePlan:
    root_id = deterministic_id("structure-node", source_hash, "root", "root")
    root = StructureNode(
        structure_node_id=root_id,
        structure_node_kind="root",
        heading_text=source_locator,
        source_range_id="root",
        source_locator=source_locator,
        source_order=0,
    )
    nodes: list[StructureNode] = [root]
    node_for_segment: dict[str, str] = {}
    # stack of (depth, node_id) for ancestry resolution
    open_headings: list[tuple[int, str]] = []
    for order, segment in enumerate(segments, start=1):
        if segment.segment_kind == "heading":
            depth = _heading_depth(segment.text)
            while open_headings and open_headings[-1][0] >= depth:
                open_headings.pop()
            parent_id = open_headings[-1][1] if open_headings else root_id
            heading_text = segment.text.lstrip("#").strip()
            node_id = deterministic_id(
                "structure-node",
                source_hash,
                segment.source_range_id,
                _DEPTH_KIND.get(depth, "heading"),
                short_digest(heading_text.lower()),
            )
            nodes.append(
                StructureNode(
                    structure_node_id=node_id,
                    structure_node_kind=_DEPTH_KIND.get(depth, "heading"),
                    heading_text=heading_text,
                    source_range_id=segment.source_range_id,
                    source_locator=segment.source_locator,
                    source_order=order,
                    depth=depth,
                    parent_structure_node_id=parent_id,
                    evidence_ids=segment.evidence_ids,
                )
            )
            open_headings.append((depth, node_id))
            node_for_segment[segment.segment_id] = node_id
        else:
            node_for_segment[segment.segment_id] = (
                open_headings[-1][1] if open_headings else root_id
            )
    return StructurePlan(root_id, tuple(nodes), node_for_segment)


def _heading_depth(text: str) -> int:
    stripped = text.lstrip()
    depth = len(stripped) - len(stripped.lstrip("#"))
    return depth if depth > 0 else 1
