"""Build normalized source maps from structured PDF document models."""

from __future__ import annotations

import hashlib
import re
from dataclasses import replace

from llmwiki.domain.evidence_locator_index import canonicalize_evidence_text
from llmwiki.domain.source_map import (
    NormalizedSourceMap,
    SourceAnchor,
    SourceBlock,
    SourceBlockType,
    SourceMapFinding,
)
from llmwiki.pdf.document import DocumentElement, DocumentModel, _has_lexical_content

_SHORT_FURNITURE_WORD_LIMIT = 5
_HEADER_Y_MAX = 80.0
_FOOTER_Y_MIN = 720.0


def build_normalized_source_map(model: DocumentModel) -> NormalizedSourceMap:
    blocks: list[SourceBlock] = []
    findings: list[SourceMapFinding] = []
    parent_by_section: dict[str, str] = {}
    child_ids_by_parent: dict[str, list[str]] = {}

    for source_order, element in enumerate(model.elements, start=1):
        source_text = _source_text(element)
        anchor = _source_anchor(model, element, source_text)
        if element.body_state != "body":
            findings.append(
                _finding(
                    model,
                    source_order,
                    _finding_code_for_body_state(element.body_state),
                    anchor,
                    f"Element {element.element_id} is {element.body_state}.",
                    severity="info",
                )
            )
            continue
        if not _has_lexical_content(source_text) and element.element_kind != "picture":
            findings.append(
                _finding(
                    model,
                    source_order,
                    "empty-body-element",
                    anchor,
                    f"Element {element.element_id} has no lexical source text.",
                    severity="warning",
                )
            )
            continue
        if _header_or_footer_candidate(element, source_text):
            findings.append(
                _finding(
                    model,
                    source_order,
                    "header-footer-candidate",
                    anchor,
                    f"Element {element.element_id} looks like repeated page furniture.",
                    severity="info",
                )
            )
        if element.page_start <= 0 or element.page_end <= 0:
            findings.append(
                _finding(
                    model,
                    source_order,
                    "missing-page-span",
                    anchor,
                    f"Element {element.element_id} has no stable page span.",
                    severity="warning",
                )
            )
        block = _source_block(
            model,
            element,
            source_order,
            source_text,
            anchor,
            parent_by_section.get(element.heading_path, ""),
        )
        if block.block_type == "heading":
            parent_by_section[element.heading_path] = block.source_block_id
        elif block.parent_block_id:
            child_ids_by_parent.setdefault(block.parent_block_id, []).append(block.source_block_id)
        blocks.append(block)
        if block.block_type in {"table", "code"}:
            findings.append(
                _finding(
                    model,
                    source_order,
                    f"{block.block_type}-block-candidate",
                    anchor,
                    f"Element {element.element_id} is a {block.block_type} block.",
                    severity="info",
                )
            )

    blocks_with_children = tuple(
        replace(block, child_block_ids=tuple(child_ids_by_parent.get(block.source_block_id, ())))
        for block in blocks
    )
    return NormalizedSourceMap(
        source_id=f"source-{_digest(f'{model.source_locator}|{model.source_hash}')[:16]}",
        source_locator=model.source_locator,
        source_hash=model.source_hash,
        extractor_name=model.extractor_name,
        extractor_version=model.extractor_version,
        source_blocks=blocks_with_children,
        findings=tuple(findings),
    )


def _source_block(
    model: DocumentModel,
    element: DocumentElement,
    source_order: int,
    source_text: str,
    anchor: SourceAnchor,
    parent_block_id: str,
) -> SourceBlock:
    block_type = _block_type(element)
    identity = "|".join(
        (
            model.source_hash,
            str(source_order),
            element.element_id,
            _page_span_text(element),
            anchor.text_fingerprint,
        )
    )
    return SourceBlock(
        source_block_id=f"source-block-{_digest(identity)[:16]}",
        source_anchor=anchor,
        block_type=block_type,
        source_text=source_text,
        page_span=(element.page_start, element.page_end),
        section_path=_section_path(element),
        parent_block_id=parent_block_id if block_type != "heading" else "",
        child_block_ids=(),
        confidence=_confidence(element, source_text),
        source_order=source_order,
    )


def _source_anchor(
    model: DocumentModel, element: DocumentElement, source_text: str
) -> SourceAnchor:
    return SourceAnchor(
        source_locator=model.source_locator,
        source_hash=model.source_hash,
        page_span=(element.page_start, element.page_end),
        element_path=(element.element_id,),
        text_fingerprint=_digest(canonicalize_evidence_text(source_text))[:16],
        bounding_boxes=_bounding_boxes(element),
    )


def _finding(
    model: DocumentModel,
    source_order: int,
    code: str,
    anchor: SourceAnchor,
    message: str,
    *,
    severity: str,
) -> SourceMapFinding:
    identity = "|".join((model.source_hash, str(source_order), code, anchor.text_fingerprint))
    return SourceMapFinding(
        finding_id=f"source-map-finding-{_digest(identity)[:16]}",
        severity=severity,  # type: ignore[arg-type]
        finding_code=code,
        source_anchor=anchor,
        message=message,
    )


def _source_text(element: DocumentElement) -> str:
    text = (element.markdown or element.text).strip()
    if text:
        return text
    if element.element_kind == "picture":
        return "[Figure]"
    return ""


def _block_type(element: DocumentElement) -> SourceBlockType:
    if element.element_kind == "heading":
        return "heading"
    if element.element_kind == "list_item":
        return "list"
    if element.element_kind == "code_block":
        return "code"
    if element.element_kind == "table":
        return "table"
    if element.element_kind == "picture":
        return "figure"
    if element.element_kind == "paragraph":
        return "paragraph"
    return "unknown"


def _section_path(element: DocumentElement) -> str:
    section = " ".join((element.heading_path or "Document").split())
    return section or "Document"


def _confidence(element: DocumentElement, source_text: str) -> float:
    if element.page_start <= 0 or element.page_end <= 0:
        return 0.5
    if _layout_fragment(source_text):
        return 0.75
    if _header_or_footer_candidate(element, source_text):
        return 0.8
    return 1.0


def _layout_fragment(text: str) -> bool:
    stripped = " ".join(text.split())
    if not stripped:
        return False
    if re.search(r"\b\w+\s+-\s+\w+\b", stripped):
        return True
    return len(stripped.split()) <= 4 and not stripped.endswith((".", ":", ";", "?", "!"))


def _header_or_footer_candidate(element: DocumentElement, source_text: str) -> bool:
    if element.layout_y0 <= 0:
        return False
    if element.element_kind == "heading":
        return False
    if len(source_text.split()) > _SHORT_FURNITURE_WORD_LIMIT:
        return False
    return element.layout_y0 <= _HEADER_Y_MAX or element.layout_y0 >= _FOOTER_Y_MIN


def _finding_code_for_body_state(body_state: str) -> str:
    if body_state == "table_of_contents":
        return "table-of-contents"
    if body_state in {"header", "footer", "furniture"}:
        return f"{body_state}-candidate"
    return "non-body-element"


def _bounding_boxes(element: DocumentElement) -> tuple[tuple[float, float, float, float], ...]:
    if element.layout_x0 <= 0 and element.layout_y0 <= 0:
        return ()
    return ((element.layout_x0, element.layout_y0, element.layout_x0, element.layout_y0),)


def _page_span_text(element: DocumentElement) -> str:
    return f"{element.page_start}-{element.page_end}"


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
