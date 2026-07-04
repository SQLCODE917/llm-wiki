"""Normalized source map domain objects and prompt windows."""

from __future__ import annotations

import hashlib
import json
from collections.abc import Callable, Sequence
from dataclasses import asdict, dataclass
from typing import Literal

SourceBlockType = Literal["heading", "paragraph", "list", "code", "table", "figure", "unknown"]
SourceMapSeverity = Literal["blocker", "warning", "info"]


@dataclass(frozen=True)
class SourceAnchor:
    source_locator: str
    source_hash: str
    page_span: tuple[int, int]
    element_path: tuple[str, ...]
    text_fingerprint: str
    bounding_boxes: tuple[tuple[float, float, float, float], ...] = ()


@dataclass(frozen=True)
class SourceBlock:
    source_block_id: str
    source_anchor: SourceAnchor
    block_type: SourceBlockType
    source_text: str
    page_span: tuple[int, int]
    section_path: str
    parent_block_id: str
    child_block_ids: tuple[str, ...]
    confidence: float
    source_order: int


@dataclass(frozen=True)
class SourceMapFinding:
    finding_id: str
    severity: SourceMapSeverity
    finding_code: str
    source_anchor: SourceAnchor
    message: str


@dataclass(frozen=True)
class NormalizedSourceMap:
    source_id: str
    source_locator: str
    source_hash: str
    extractor_name: str
    extractor_version: str
    source_blocks: tuple[SourceBlock, ...]
    findings: tuple[SourceMapFinding, ...] = ()

    @property
    def low_confidence_block_count(self) -> int:
        return sum(1 for block in self.source_blocks if block.confidence < 1.0)

    @property
    def source_blocks_by_id(self) -> dict[str, SourceBlock]:
        return {block.source_block_id: block for block in self.source_blocks}


@dataclass(frozen=True)
class PromptWindow:
    prompt_window_id: str
    source_block_ids: tuple[str, ...]
    token_estimate: int
    text: str


def normalized_source_map_to_json(source_map: NormalizedSourceMap) -> str:
    return json.dumps(asdict(source_map), indent=2, ensure_ascii=False)


def normalized_source_map_from_json(text: str) -> NormalizedSourceMap:
    data = json.loads(text)
    return NormalizedSourceMap(
        source_id=data["source_id"],
        source_locator=data["source_locator"],
        source_hash=data["source_hash"],
        extractor_name=data["extractor_name"],
        extractor_version=data["extractor_version"],
        source_blocks=tuple(_source_block_from_data(item) for item in data["source_blocks"]),
        findings=tuple(_finding_from_data(item) for item in data.get("findings", ())),
    )


def prompt_windows_to_json(windows: tuple[PromptWindow, ...]) -> str:
    return json.dumps([asdict(window) for window in windows], indent=2, ensure_ascii=False)


def prompt_windows_from_json(text: str) -> tuple[PromptWindow, ...]:
    data = json.loads(text)
    return tuple(
        PromptWindow(
            prompt_window_id=item["prompt_window_id"],
            source_block_ids=tuple(item["source_block_ids"]),
            token_estimate=item["token_estimate"],
            text=item["text"],
        )
        for item in data
    )


def source_map_text(source_map: NormalizedSourceMap) -> str:
    return "\n\n".join(
        block.source_text.strip()
        for block in sorted(source_map.source_blocks, key=lambda item: item.source_order)
        if block.source_text.strip()
    )


def build_prompt_windows(
    source_map: NormalizedSourceMap,
    *,
    budget_tokens: int,
    estimate_tokens: Callable[[str], int],
) -> tuple[PromptWindow, ...]:
    blocks = tuple(
        block
        for block in sorted(source_map.source_blocks, key=lambda item: item.source_order)
        if block.source_text.strip()
    )
    windows: list[PromptWindow] = []
    current: list[SourceBlock] = []
    heading_context_by_section: dict[str, SourceBlock] = {}

    for block in blocks:
        if block.block_type == "heading":
            heading_context_by_section[block.section_path] = block
        candidate = _dedupe_blocks((*current, block))
        if current and estimate_tokens(_join_blocks(candidate)) > budget_tokens:
            _append_window(windows, source_map, current, estimate_tokens)
            current = []
        if not current and block.block_type != "heading":
            context = heading_context_by_section.get(block.section_path)
            if context is not None and context.source_block_id != block.source_block_id:
                contextual = (context, block)
                if estimate_tokens(_join_blocks(contextual)) <= budget_tokens:
                    current = [context]
        current = list(_dedupe_blocks((*current, block)))
        if estimate_tokens(_join_blocks(tuple(current))) > budget_tokens and len(current) > 1:
            overflow = current.pop()
            _append_window(windows, source_map, current, estimate_tokens)
            current = [overflow]

    _append_window(windows, source_map, current, estimate_tokens)
    return tuple(windows)


def _append_window(
    windows: list[PromptWindow],
    source_map: NormalizedSourceMap,
    blocks: Sequence[SourceBlock],
    estimate_tokens: Callable[[str], int],
) -> None:
    selected = tuple(block for block in blocks if block.source_text.strip())
    if not selected:
        return
    text = _join_blocks(selected)
    index = len(windows) + 1
    identity = "|".join(
        (
            source_map.source_hash,
            str(index),
            ",".join(block.source_block_id for block in selected),
            _digest(text)[:16],
        )
    )
    windows.append(
        PromptWindow(
            prompt_window_id=f"prompt-window-{_digest(identity)[:16]}",
            source_block_ids=tuple(block.source_block_id for block in selected),
            token_estimate=estimate_tokens(text),
            text=text,
        )
    )


def _source_block_from_data(data: dict[str, object]) -> SourceBlock:
    return SourceBlock(
        source_block_id=str(data["source_block_id"]),
        source_anchor=_anchor_from_data(data["source_anchor"]),
        block_type=data["block_type"],  # type: ignore[arg-type]
        source_text=str(data["source_text"]),
        page_span=_page_span_from_data(data["page_span"]),
        section_path=str(data["section_path"]),
        parent_block_id=str(data["parent_block_id"]),
        child_block_ids=_string_tuple_from_data(data["child_block_ids"]),
        confidence=_float_from_data(data["confidence"]),
        source_order=_int_from_data(data["source_order"]),
    )


def _finding_from_data(data: dict[str, object]) -> SourceMapFinding:
    return SourceMapFinding(
        finding_id=str(data["finding_id"]),
        severity=data["severity"],  # type: ignore[arg-type]
        finding_code=str(data["finding_code"]),
        source_anchor=_anchor_from_data(data["source_anchor"]),
        message=str(data["message"]),
    )


def _anchor_from_data(data: object) -> SourceAnchor:
    if not isinstance(data, dict):
        raise ValueError("source anchor must be an object")
    return SourceAnchor(
        source_locator=str(data["source_locator"]),
        source_hash=str(data["source_hash"]),
        page_span=_page_span_from_data(data["page_span"]),
        element_path=_string_tuple_from_data(data["element_path"]),
        text_fingerprint=str(data["text_fingerprint"]),
        bounding_boxes=_bounding_boxes_from_data(data.get("bounding_boxes", ())),
    )


def _page_span_from_data(data: object) -> tuple[int, int]:
    if not isinstance(data, list | tuple) or len(data) != 2:
        raise ValueError("page span must contain exactly two values")
    return (_int_from_data(data[0]), _int_from_data(data[1]))


def _string_tuple_from_data(data: object) -> tuple[str, ...]:
    if not isinstance(data, list | tuple):
        raise ValueError("expected a sequence of strings")
    return tuple(str(item) for item in data)


def _bounding_boxes_from_data(data: object) -> tuple[tuple[float, float, float, float], ...]:
    if not isinstance(data, list | tuple):
        raise ValueError("expected a sequence of bounding boxes")
    boxes: list[tuple[float, float, float, float]] = []
    for box in data:
        if not isinstance(box, list | tuple) or len(box) != 4:
            raise ValueError("bounding box must contain exactly four values")
        boxes.append(
            (
                _float_from_data(box[0]),
                _float_from_data(box[1]),
                _float_from_data(box[2]),
                _float_from_data(box[3]),
            )
        )
    return tuple(boxes)


def _float_from_data(data: object) -> float:
    if isinstance(data, int | float | str):
        return float(data)
    raise ValueError("expected a numeric value")


def _int_from_data(data: object) -> int:
    if isinstance(data, int | str):
        return int(data)
    raise ValueError("expected an integer value")


def _join_blocks(blocks: Sequence[SourceBlock]) -> str:
    return "\n\n".join(block.source_text.strip() for block in blocks if block.source_text.strip())


def _dedupe_blocks(blocks: Sequence[SourceBlock]) -> tuple[SourceBlock, ...]:
    deduped: dict[str, SourceBlock] = {}
    for block in blocks:
        deduped[block.source_block_id] = block
    return tuple(deduped.values())


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
