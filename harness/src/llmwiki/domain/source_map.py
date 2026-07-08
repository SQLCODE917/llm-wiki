"""Normalized source map domain objects and prompt windows."""

from __future__ import annotations

import hashlib
import json
from collections.abc import Callable, Sequence
from dataclasses import asdict, dataclass
from typing import Literal

from llmwiki.domain.strict_json import (
    expect_array,
    expect_float,
    expect_int,
    expect_literal,
    expect_object,
    expect_str,
)

SourceBlockType = Literal["heading", "paragraph", "list", "code", "table", "figure", "unknown"]
SourceMapSeverity = Literal["blocker", "warning", "info"]
SOURCE_BLOCK_TYPES: tuple[SourceBlockType, ...] = (
    "heading",
    "paragraph",
    "list",
    "code",
    "table",
    "figure",
    "unknown",
)
SOURCE_MAP_SEVERITIES: tuple[SourceMapSeverity, ...] = ("blocker", "warning", "info")


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
    data = expect_object(json.loads(text), "normalized source map")
    return NormalizedSourceMap(
        source_id=expect_str(data["source_id"], "source_id"),
        source_locator=expect_str(data["source_locator"], "source_locator"),
        source_hash=expect_str(data["source_hash"], "source_hash"),
        extractor_name=expect_str(data["extractor_name"], "extractor_name"),
        extractor_version=expect_str(data["extractor_version"], "extractor_version"),
        source_blocks=tuple(
            _source_block_from_data(item)
            for item in expect_array(data["source_blocks"], "source_blocks")
        ),
        findings=tuple(
            _finding_from_data(item)
            for item in expect_array(data.get("findings", []), "findings")
        ),
    )


def prompt_windows_to_json(windows: tuple[PromptWindow, ...]) -> str:
    return json.dumps([asdict(window) for window in windows], indent=2, ensure_ascii=False)


def prompt_windows_from_json(text: str) -> tuple[PromptWindow, ...]:
    data = expect_array(json.loads(text), "prompt windows")
    return tuple(
        PromptWindow(
            prompt_window_id=expect_str(
                expect_object(item, "prompt window")["prompt_window_id"],
                "prompt_window_id",
            ),
            source_block_ids=tuple(
                expect_str(block_id, "source_block_id")
                for block_id in expect_array(
                    expect_object(item, "prompt window")["source_block_ids"],
                    "source_block_ids",
                )
            ),
            token_estimate=expect_int(
                expect_object(item, "prompt window")["token_estimate"],
                "token_estimate",
            ),
            text=expect_str(expect_object(item, "prompt window")["text"], "text"),
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


def _source_block_from_data(raw: object) -> SourceBlock:
    data = expect_object(raw, "source block")
    return SourceBlock(
        source_block_id=expect_str(data["source_block_id"], "source_block_id"),
        source_anchor=_anchor_from_data(data["source_anchor"]),
        block_type=expect_literal(data["block_type"], SOURCE_BLOCK_TYPES, "block_type"),
        source_text=expect_str(data["source_text"], "source_text"),
        page_span=_page_span_from_data(data["page_span"]),
        section_path=expect_str(data["section_path"], "section_path"),
        parent_block_id=expect_str(data["parent_block_id"], "parent_block_id"),
        child_block_ids=_string_tuple_from_data(data["child_block_ids"]),
        confidence=expect_float(data["confidence"], "confidence"),
        source_order=expect_int(data["source_order"], "source_order"),
    )


def _finding_from_data(raw: object) -> SourceMapFinding:
    data = expect_object(raw, "source map finding")
    return SourceMapFinding(
        finding_id=expect_str(data["finding_id"], "finding_id"),
        severity=expect_literal(data["severity"], SOURCE_MAP_SEVERITIES, "severity"),
        finding_code=expect_str(data["finding_code"], "finding_code"),
        source_anchor=_anchor_from_data(data["source_anchor"]),
        message=expect_str(data["message"], "message"),
    )


def _anchor_from_data(data: object) -> SourceAnchor:
    data = expect_object(data, "source anchor")
    return SourceAnchor(
        source_locator=expect_str(data["source_locator"], "source_locator"),
        source_hash=expect_str(data["source_hash"], "source_hash"),
        page_span=_page_span_from_data(data["page_span"]),
        element_path=_string_tuple_from_data(data["element_path"]),
        text_fingerprint=expect_str(data["text_fingerprint"], "text_fingerprint"),
        bounding_boxes=_bounding_boxes_from_data(data.get("bounding_boxes", [])),
    )


def _page_span_from_data(data: object) -> tuple[int, int]:
    if not isinstance(data, list) or len(data) != 2:
        raise ValueError("page span must contain exactly two values")
    return (expect_int(data[0], "page_span[0]"), expect_int(data[1], "page_span[1]"))


def _string_tuple_from_data(data: object) -> tuple[str, ...]:
    return tuple(expect_str(item, "string sequence item") for item in expect_array(data))


def _bounding_boxes_from_data(data: object) -> tuple[tuple[float, float, float, float], ...]:
    boxes: list[tuple[float, float, float, float]] = []
    for box in expect_array(data, "bounding_boxes"):
        if not isinstance(box, list) or len(box) != 4:
            raise ValueError("bounding box must contain exactly four values")
        boxes.append(
            (
                expect_float(box[0], "bounding_box[0]"),
                expect_float(box[1], "bounding_box[1]"),
                expect_float(box[2], "bounding_box[2]"),
                expect_float(box[3], "bounding_box[3]"),
            )
        )
    return tuple(boxes)


def _join_blocks(blocks: Sequence[SourceBlock]) -> str:
    return "\n\n".join(block.source_text.strip() for block in blocks if block.source_text.strip())


def _dedupe_blocks(blocks: Sequence[SourceBlock]) -> tuple[SourceBlock, ...]:
    deduped: dict[str, SourceBlock] = {}
    for block in blocks:
        deduped[block.source_block_id] = block
    return tuple(deduped.values())


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
