"""Build a DocumentStructure from ordered source segments.

Heading segments become structure nodes; their depth comes from the heading
level (a reusable structural signal), so the nesting is source-neutral. Every
other segment is mapped to its nearest containing heading node, or the root
node when a source is structurally flat.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, replace

from llmwiki.domain.ledger.canonical import deterministic_id, short_digest
from llmwiki.domain.ledger.segments import SourceSegment
from llmwiki.domain.ledger.structure import StructureNode

_DEPTH_KIND = {1: "chapter", 2: "section"}
_MARKDOWN_DECORATION = re.compile(r"[*_`]+")
_TRAILING_MARKER = re.compile(r"\s+#+\s*$")
_WHITESPACE = re.compile(r"\s+")
_PENDING_NUMBER_MARKER_WINDOW = 24


@dataclass(frozen=True)
class StructurePlan:
    root_node_id: str
    nodes: tuple[StructureNode, ...]
    node_for_segment: dict[str, str]


@dataclass(frozen=True)
class _OpenHeading:
    depth: int
    node_id: str
    canonical_label: str
    number_path: tuple[int, ...]
    is_number_marker: bool
    title_bound: bool = True


@dataclass(frozen=True)
class _PendingNumberMarker:
    heading: _OpenHeading
    stack: tuple[_OpenHeading, ...]
    previous_node_id: str
    source_order: int


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
    open_headings: list[_OpenHeading] = []
    pending_markers: dict[tuple[int, ...], _PendingNumberMarker] = {}
    for index, segment in enumerate(segments):
        order = index + 1
        if segment.segment_kind == "heading":
            depth = _heading_depth(segment.text)
            heading_text = _heading_text(segment.text)
            canonical_label = _canonical_heading_label(heading_text)
            number_path = _heading_number_path(canonical_label)
            is_number_marker = _is_number_marker(canonical_label, number_path)
            previous_node_id = _previous_node_id(open_headings, root_id)
            pending = _pending_marker_for_title(
                pending_markers, canonical_label, segments, index, order
            )
            if pending is not None:
                heading_text = _numbered_title(pending.heading.number_path, heading_text)
                canonical_label = _canonical_heading_label(heading_text)
                bound = replace(pending.heading, canonical_label=canonical_label, title_bound=True)
                _replace_node_heading(nodes, bound.node_id, heading_text, segment.evidence_ids)
                open_headings = [*pending.stack[:-1], bound]
                pending_markers.pop(pending.heading.number_path, None)
                node_for_segment[segment.segment_id] = bound.node_id
                continue
            while open_headings and open_headings[-1].depth >= depth:
                if _number_parent(open_headings[-1].number_path, number_path):
                    break
                if (
                    open_headings[-1].is_number_marker
                    and open_headings[-1].title_bound
                    and not number_path
                ):
                    break
                open_headings.pop()
            if (
                open_headings
                and number_path
                and open_headings[-1].number_path == number_path
                and is_number_marker
            ):
                node_for_segment[segment.segment_id] = open_headings[-1].node_id
                continue
            while open_headings and _number_conflicts(open_headings[-1].number_path, number_path):
                open_headings.pop()
            if (
                open_headings
                and canonical_label
                and _same_heading(open_headings[-1].canonical_label, canonical_label)
            ):
                node_for_segment[segment.segment_id] = open_headings[-1].node_id
                continue
            parent_id = open_headings[-1].node_id if open_headings else root_id
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
            heading = _OpenHeading(
                depth,
                node_id,
                canonical_label,
                number_path,
                is_number_marker,
                title_bound=not is_number_marker,
            )
            open_headings.append(heading)
            if is_number_marker:
                pending_markers[number_path] = _PendingNumberMarker(
                    heading=heading,
                    stack=tuple(open_headings),
                    previous_node_id=previous_node_id,
                    source_order=order,
                )
            node_for_segment[segment.segment_id] = node_id
        else:
            node_for_segment[segment.segment_id] = _node_for_non_heading(
                open_headings, pending_markers, segment, root_id
            )
    return StructurePlan(root_id, tuple(nodes), node_for_segment)


def _heading_depth(text: str) -> int:
    stripped = text.lstrip()
    depth = len(stripped) - len(stripped.lstrip("#"))
    return depth if depth > 0 else 1


def _heading_text(text: str) -> str:
    stripped = text.lstrip()
    without_opening = stripped.lstrip("#").strip()
    return _TRAILING_MARKER.sub("", without_opening).strip()


def _canonical_heading_label(text: str) -> str:
    without_decoration = _MARKDOWN_DECORATION.sub("", text)
    return _WHITESPACE.sub(" ", without_decoration).strip().casefold()


def _heading_number_path(label: str) -> tuple[int, ...]:
    words = label.strip()
    match = re.match(
        r"^(?:(?:chapter|section|part|appendix|book)\s+)?(\d+(?:\.\d+)*)\b",
        words,
        re.IGNORECASE,
    )
    if match is None:
        return ()
    return tuple(int(part) for part in match.group(1).split("."))


def _number_conflicts(parent: tuple[int, ...], child: tuple[int, ...]) -> bool:
    if not parent or not child:
        return False
    if parent == child:
        return False
    return not (len(parent) < len(child) and child[: len(parent)] == parent)


def _number_parent(parent: tuple[int, ...], child: tuple[int, ...]) -> bool:
    return bool(parent and child and len(parent) < len(child) and child[: len(parent)] == parent)


def _is_number_marker(label: str, number_path: tuple[int, ...]) -> bool:
    marker = ".".join(str(part) for part in number_path)
    return label == marker


def _same_heading(parent_label: str, child_label: str) -> bool:
    return parent_label == child_label or _without_leading_number(parent_label) == child_label


def _without_leading_number(label: str) -> str:
    return re.sub(
        r"^(?:(?:chapter|section|part|appendix|book)\s+)?\d+(?:\.\d+)*\s*[-:.]?\s*",
        "",
        label,
        count=1,
    ).strip()


def _pending_marker_for_title(
    pending_markers: dict[tuple[int, ...], _PendingNumberMarker],
    canonical_label: str,
    segments: tuple[SourceSegment, ...],
    index: int,
    order: int,
) -> _PendingNumberMarker | None:
    for pending in sorted(pending_markers.values(), key=lambda item: -item.source_order):
        if order - pending.source_order > _PENDING_NUMBER_MARKER_WINDOW:
            continue
        if order - pending.source_order == 1:
            return pending
        if _nearby_numbered_title(pending.heading.number_path, canonical_label, segments, index):
            return pending
    return None


def _nearby_numbered_title(
    number_path: tuple[int, ...],
    canonical_label: str,
    segments: tuple[SourceSegment, ...],
    index: int,
) -> bool:
    for segment in segments[index : index + 4]:
        candidate = _canonical_heading_label(_heading_text(segment.text))
        if _heading_number_path(candidate) != number_path:
            continue
        if _same_heading(candidate, canonical_label):
            return True
    return False


def _numbered_title(number_path: tuple[int, ...], title: str) -> str:
    return f"{'.'.join(str(part) for part in number_path)} {title}".strip()


def _replace_node_heading(
    nodes: list[StructureNode], node_id: str, heading_text: str, evidence_ids: tuple[str, ...]
) -> None:
    for index, node in enumerate(nodes):
        if node.structure_node_id != node_id:
            continue
        nodes[index] = replace(
            node,
            heading_text=heading_text,
            evidence_ids=tuple(dict.fromkeys((*node.evidence_ids, *evidence_ids))),
        )
        return


def _previous_node_id(open_headings: list[_OpenHeading], root_id: str) -> str:
    for heading in reversed(open_headings):
        if heading.title_bound or not heading.is_number_marker:
            return heading.node_id
    return root_id


def _node_for_non_heading(
    open_headings: list[_OpenHeading],
    pending_markers: dict[tuple[int, ...], _PendingNumberMarker],
    segment: SourceSegment,
    root_id: str,
) -> str:
    if not open_headings:
        return root_id
    current = open_headings[-1]
    if not current.is_number_marker or current.title_bound:
        return current.node_id
    pending = pending_markers.get(current.number_path)
    if pending is None:
        return current.node_id
    if _heading_number_path(_canonical_heading_label(segment.text)) == current.number_path:
        return current.node_id
    return pending.previous_node_id
