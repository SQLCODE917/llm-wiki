"""Build a normalized source map for markdown sources."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass

from llmwiki.domain.pages import slugify
from llmwiki.domain.source_map import NormalizedSourceMap, SourceAnchor, SourceBlock

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
_LIST_RE = re.compile(r"^\s*(?:[-*]|\d+[.)])\s+\S")


@dataclass(frozen=True)
class _PendingBlock:
    block_type: str
    lines: tuple[str, ...]
    start_line: int
    end_line: int
    section_path: str


def markdown_source_map(source_locator: str, text: str) -> NormalizedSourceMap:
    source_hash = _digest(text)
    blocks: list[SourceBlock] = []
    pending: list[str] = []
    pending_type = "paragraph"
    pending_start = 1
    section_stack: list[str] = []
    in_code = False

    def flush(end_line: int) -> None:
        nonlocal pending, pending_type, pending_start
        if not any(line.strip() for line in pending):
            pending = []
            return
        _append_block(
            blocks,
            source_locator,
            source_hash,
            _PendingBlock(
                pending_type,
                tuple(pending),
                pending_start,
                end_line,
                " / ".join(section_stack),
            ),
        )
        pending = []
        pending_type = "paragraph"

    lines = text.splitlines()
    for index, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            if not in_code:
                flush(index - 1)
                pending_start = index
                pending_type = "code"
                pending = [line]
                in_code = True
            else:
                pending.append(line)
                flush(index)
                in_code = False
            continue
        if in_code:
            pending.append(line)
            continue
        heading = _HEADING_RE.match(line)
        if heading is not None:
            flush(index - 1)
            level = len(heading.group(1))
            label = heading.group(2).strip()
            section_stack = section_stack[: level - 1]
            section_stack.append(label)
            _append_block(
                blocks,
                source_locator,
                source_hash,
                _PendingBlock("heading", (label,), index, index, " / ".join(section_stack)),
            )
            continue
        if not stripped:
            flush(index - 1)
            continue
        line_type = "list" if _LIST_RE.match(line) else "paragraph"
        if pending and pending_type != line_type:
            flush(index - 1)
        if not pending:
            pending_start = index
            pending_type = line_type
        pending.append(line)
    flush(len(lines))
    return NormalizedSourceMap(
        source_id=slugify(source_locator.rsplit(".", 1)[0]),
        source_locator=source_locator,
        source_hash=source_hash,
        extractor_name="markdown-source-map",
        extractor_version="1",
        source_blocks=tuple(blocks),
    )


def _append_block(
    blocks: list[SourceBlock],
    source_locator: str,
    source_hash: str,
    pending: _PendingBlock,
) -> None:
    source_order = len(blocks) + 1
    text = "\n".join(pending.lines).strip()
    fingerprint = _digest(" ".join(text.split()))[:16]
    block_id = f"source-block-{_digest(f'{source_hash}|{source_order}|{fingerprint}')[:16]}"
    anchor = SourceAnchor(
        source_locator=source_locator,
        source_hash=source_hash,
        page_span=(pending.start_line, pending.end_line),
        element_path=("markdown", str(source_order)),
        text_fingerprint=fingerprint,
    )
    blocks.append(
        SourceBlock(
            source_block_id=block_id,
            source_anchor=anchor,
            block_type=pending.block_type,  # type: ignore[arg-type]
            source_text=text,
            page_span=anchor.page_span,
            section_path=pending.section_path,
            parent_block_id="",
            child_block_ids=(),
            confidence=1.0,
            source_order=source_order,
        )
    )


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
