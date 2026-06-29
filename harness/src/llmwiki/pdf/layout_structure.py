"""Layout-derived source structure for PDF document models."""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, replace
from typing import Any

from llmwiki.pdf.document import DocumentElement, DocumentModel


@dataclass(frozen=True)
class LayoutBox:
    page_no: int
    x0: float
    y0: float
    x1: float
    y1: float


@dataclass(frozen=True)
class LayoutLine:
    page_no: int
    text: str
    font_size: float
    x0: float
    y0: float
    y1: float


@dataclass(frozen=True)
class LayoutMatch:
    font_size: float = 0.0
    x0: float = 0.0
    y0: float = 0.0


@dataclass(frozen=True)
class LayoutDocument:
    page_heights: dict[int, float]
    lines: tuple[LayoutLine, ...]

    @property
    def body_font_size(self) -> float:
        counts = Counter(line.font_size for line in self.lines if line.font_size > 0)
        return counts.most_common(1)[0][0] if counts else 0.0

    def match(self, page_no: int, text: str, box: LayoutBox | None = None) -> LayoutMatch:
        lines = tuple(line for line in self.lines if line.page_no == page_no)
        if box is not None:
            overlap = tuple(line for line in lines if _overlaps(line, box))
            text_overlap = tuple(line for line in overlap if _text_overlaps(text, line.text))
            if text_overlap:
                return _match_from_lines(text_overlap)
            if overlap:
                return _match_from_lines(overlap)
        text_matches = tuple(line for line in lines if _text_overlaps(text, line.text))
        return _match_from_lines(text_matches)


def layout_document_from_pdf(pdf_doc: Any) -> LayoutDocument:
    lines: list[LayoutLine] = []
    heights: dict[int, float] = {}
    for page_index, page in enumerate(pdf_doc, start=1):
        heights[page_index] = float(page.rect.height)
        for block in page.get_text("dict", sort=True).get("blocks", []):
            for line in block.get("lines", []):
                spans = [span for span in line.get("spans", []) if span.get("text", "").strip()]
                if not spans:
                    continue
                text = " ".join(str(span["text"]).strip() for span in spans).strip()
                if not text:
                    continue
                bbox = line.get("bbox", (0.0, 0.0, 0.0, 0.0))
                lines.append(
                    LayoutLine(
                        page_no=page_index,
                        text=text,
                        font_size=round(max(float(span.get("size", 0.0)) for span in spans), 1),
                        x0=float(bbox[0]),
                        y0=float(bbox[1]),
                        y1=float(bbox[3]),
                    )
                )
    return LayoutDocument(heights, tuple(lines))


def layout_box_from_bbox(page_no: int, page_height: float, bbox: Any) -> LayoutBox | None:
    if bbox is None:
        return None
    try:
        left = float(bbox.l)
        right = float(bbox.r)
        top = float(bbox.t)
        bottom = float(bbox.b)
    except (AttributeError, TypeError, ValueError):
        return None
    origin = _enum_value(getattr(bbox, "coord_origin", "")).lower()
    if origin == "bottomleft":
        y0 = page_height - max(top, bottom)
        y1 = page_height - min(top, bottom)
    else:
        y0 = min(top, bottom)
        y1 = max(top, bottom)
    return LayoutBox(page_no, min(left, right), y0, max(left, right), y1)


def compile_layout_structure(model: DocumentModel, *, body_font_size: float) -> DocumentModel:
    accepted = _accepted_heading_ids(model.elements, body_font_size)
    level_by_size = _level_by_size(
        tuple(e.layout_font_size for e in model.elements if e.element_id in accepted)
    )
    stack: list[tuple[int, str]] = []
    previous_heading: DocumentElement | None = None
    elements: list[DocumentElement] = []
    for element in model.elements:
        if element.element_kind == "heading" and element.element_id in accepted:
            if _duplicate_fragment(previous_heading, element):
                elements.append(_demote(element, _stack_path(stack)))
                continue
            level = level_by_size.get(element.layout_font_size, element.heading_level or 1)
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, element.text))
            heading_path = _stack_path(stack)
            previous_heading = element
            elements.append(
                replace(
                    element,
                    heading_level=level,
                    heading_path=heading_path,
                    markdown=f"{'#' * level} {element.text}",
                )
            )
            continue
        if element.element_kind == "heading":
            elements.append(_demote(element, _stack_path(stack)))
        else:
            elements.append(replace(element, heading_path=_stack_path(stack)))
    return replace(model, elements=tuple(elements))


def _accepted_heading_ids(
    elements: tuple[DocumentElement, ...], body_font_size: float
) -> set[str]:
    headings = tuple(e for e in elements if e.element_kind == "heading")
    if not headings:
        return set()
    threshold = body_font_size * 1.08 if body_font_size else 0.0
    accepted = {
        e.element_id
        for e in headings
        if e.heading_level > 1 or (e.layout_font_size and e.layout_font_size >= threshold)
    }
    return accepted or {e.element_id for e in headings}


def _level_by_size(sizes: tuple[float, ...]) -> dict[float, int]:
    tiers: list[float] = []
    for size in sorted({size for size in sizes if size > 0}, reverse=True):
        if not tiers or abs(tiers[-1] - size) > 0.6:
            tiers.append(size)
    return {size: min(index + 1, 6) for index, size in enumerate(tiers)}


def _duplicate_fragment(previous: DocumentElement | None, current: DocumentElement) -> bool:
    if previous is None or previous.page_start != current.page_start:
        return False
    if abs(previous.layout_y0 - current.layout_y0) > 42.0:
        return False
    if abs(previous.layout_font_size - current.layout_font_size) > 0.6:
        return False
    prev = _norm(previous.text)
    cur = _norm(current.text)
    return bool(prev and cur and prev != cur and (cur in prev or prev in cur))


def _demote(element: DocumentElement, heading_path: str) -> DocumentElement:
    return replace(
        element,
        element_kind="paragraph",
        heading_level=0,
        heading_path=heading_path,
        markdown=element.text,
    )


def _match_from_lines(lines: tuple[LayoutLine, ...]) -> LayoutMatch:
    if not lines:
        return LayoutMatch()
    return LayoutMatch(
        font_size=max(line.font_size for line in lines),
        x0=min(line.x0 for line in lines),
        y0=min(line.y0 for line in lines),
    )


def _overlaps(line: LayoutLine, box: LayoutBox) -> bool:
    return line.y1 >= box.y0 - 3.0 and line.y0 <= box.y1 + 3.0


def _text_overlaps(left: str, right: str) -> bool:
    a = _norm(left)
    b = _norm(right)
    return bool(a and b and (a == b or a in b or b in a))


def _stack_path(stack: list[tuple[int, str]]) -> str:
    return " > ".join(label for _level, label in stack) or "Document"


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold()


def _enum_value(value: Any) -> str:
    raw = getattr(value, "value", value)
    return str(raw)
