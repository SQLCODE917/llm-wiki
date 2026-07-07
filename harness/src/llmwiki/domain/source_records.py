"""Source-record boundaries recovered from normalized source blocks."""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.source_map import NormalizedSourceMap, SourceBlock

_FIELD_ASSIGNMENT = re.compile(r"(?<!\S)[A-Z][A-Za-z0-9 /()-]{0,36}=")
_BRACKET_GROUP = re.compile(r"(\[|【|《)\s*([^\]】》]{1,96}?)\s*(\]|】|》)")
_MIN_REPEATED_BOUNDARIES = 2


@dataclass(frozen=True)
class SourceRecordBoundary:
    source_block_id: str
    source_order: int
    label: str
    parent_section_path: str
    reason_codes: tuple[str, ...]


@dataclass(frozen=True)
class SourceRecord:
    source_record_id: str
    label: str
    parent_section_path: str
    first_source_order: int
    last_source_order: int
    source_block_ids: tuple[str, ...]
    field_names: tuple[str, ...]
    reason_codes: tuple[str, ...]


@dataclass(frozen=True)
class SourceRecordPlan:
    source_id: str
    source_hash: str
    records: tuple[SourceRecord, ...]
    source_record_block_ids: tuple[str, ...]

    @property
    def record_count(self) -> int:
        return len(self.records)


def build_source_record_plan(source_map: NormalizedSourceMap) -> SourceRecordPlan:
    blocks = tuple(sorted(source_map.source_blocks, key=lambda item: item.source_order))
    boundaries = tuple(
        boundary
        for block in blocks
        if (boundary := _boundary_for_block(block)) is not None
    )
    supported = _supported_boundaries(boundaries, blocks)
    records = tuple(
        _record_for_boundary(source_map, boundary, supported, blocks, index)
        for index, boundary in enumerate(supported)
    )
    return SourceRecordPlan(
        source_map.source_id,
        source_map.source_hash,
        records,
        tuple(block_id for record in records for block_id in record.source_block_ids),
    )


def _boundary_for_block(block: SourceBlock) -> SourceRecordBoundary | None:
    if block.block_type not in {"heading", "paragraph", "list"}:
        return None
    label, reasons = _record_label(block.source_text)
    if not label:
        return None
    return SourceRecordBoundary(
        block.source_block_id,
        block.source_order,
        label,
        block.section_path or "Overview",
        reasons,
    )


def _record_label(text: str) -> tuple[str, tuple[str, ...]]:
    plain = _plain(text)
    groups = _BRACKET_GROUP.findall(plain)
    if groups:
        opener, label, _closer = groups[-1]
        if opener in ("[", "【") and _short_label(label):
            reasons = ["bracket-record-label"]
            if len(groups) > 1:
                reasons.append("container-plus-record-label")
            return label, tuple(reasons)
    if _field_density(plain) >= 2:
        label = _leading_field_label(plain)
        if label and _short_label(label):
            return label, ("field-dense-record-label",)
    return "", ()


def _supported_boundaries(
    boundaries: tuple[SourceRecordBoundary, ...], blocks: tuple[SourceBlock, ...]
) -> tuple[SourceRecordBoundary, ...]:
    counts: dict[str, int] = {}
    for boundary in boundaries:
        counts[boundary.parent_section_path] = counts.get(boundary.parent_section_path, 0) + 1
    supported: list[SourceRecordBoundary] = []
    for index, boundary in enumerate(boundaries):
        repeated = counts.get(boundary.parent_section_path, 0) >= _MIN_REPEATED_BOUNDARIES
        last_order = _last_order(boundary, boundaries, blocks, index)
        shaped = len(_field_names(blocks, boundary.source_order, last_order)) >= 2
        field_dense = "field-dense-record-label" in boundary.reason_codes
        if shaped and (repeated or field_dense):
            supported.append(boundary)
    return tuple(supported)


def _record_for_boundary(
    source_map: NormalizedSourceMap,
    boundary: SourceRecordBoundary,
    boundaries: tuple[SourceRecordBoundary, ...],
    blocks: tuple[SourceBlock, ...],
    index: int,
) -> SourceRecord:
    last_order = _last_order(boundary, boundaries, blocks, index)
    block_ids = tuple(
        block.source_block_id
        for block in blocks
        if boundary.source_order <= block.source_order <= last_order
    )
    fields = _field_names(blocks, boundary.source_order, last_order)
    return SourceRecord(
        f"source-record-{source_map.source_hash[:8]}-{boundary.source_order:05d}",
        boundary.label,
        boundary.parent_section_path,
        boundary.source_order,
        last_order,
        block_ids,
        fields,
        boundary.reason_codes,
    )


def _last_order(
    boundary: SourceRecordBoundary,
    boundaries: tuple[SourceRecordBoundary, ...],
    blocks: tuple[SourceBlock, ...],
    index: int,
) -> int:
    next_order = next(
        (
            candidate.source_order
            for candidate in boundaries[index + 1 :]
            if candidate.source_order > boundary.source_order
        ),
        0,
    )
    last_order = boundary.source_order
    for block in blocks:
        if block.source_order < boundary.source_order:
            continue
        if next_order and block.source_order >= next_order:
            break
        if block.source_order > boundary.source_order and block.block_type == "heading":
            break
        last_order = block.source_order
    return last_order


def _field_names(
    blocks: tuple[SourceBlock, ...], start_order: int, last_order: int
) -> tuple[str, ...]:
    names: list[str] = []
    for block in blocks:
        if not start_order <= block.source_order <= last_order:
            continue
        names.extend(
            match.group(0).rstrip("=").strip()
            for match in _FIELD_ASSIGNMENT.finditer(block.source_text)
        )
    return tuple(dict.fromkeys(name for name in names if name))


def _plain(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _short_label(text: str) -> bool:
    return 0 < len(text.split()) <= 10 and len(text) <= 96


def _field_density(text: str) -> int:
    return len(_FIELD_ASSIGNMENT.findall(text))


def _leading_field_label(text: str) -> str:
    match = _FIELD_ASSIGNMENT.search(text)
    if match is None:
        return ""
    return match.group(0).rstrip("=").strip()
