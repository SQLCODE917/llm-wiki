"""Recover exact code-block text from PDF bounding boxes."""

from __future__ import annotations

from typing import Any

import pymupdf


def pdf_code_text(pdf_doc: Any, item: Any) -> str:
    parts: list[str] = []
    for prov in getattr(item, "prov", []) or []:
        page_no = _page_no(prov)
        if page_no <= 0 or page_no > len(pdf_doc):
            continue
        bbox = getattr(prov, "bbox", None)
        if bbox is None:
            continue
        page = pdf_doc[page_no - 1]
        text = _text_from_page_blocks(page, _clip_rect(page, bbox))
        if text:
            parts.append(text)
    return "\n".join(parts).strip()


def _page_no(prov: Any) -> int:
    try:
        return int(getattr(prov, "page_no", 0))
    except (TypeError, ValueError):
        return 0


def _clip_rect(page: Any, bbox: Any) -> pymupdf.Rect:
    left = _float_attr(bbox, "l")
    right = _float_attr(bbox, "r")
    top = _float_attr(bbox, "t")
    bottom = _float_attr(bbox, "b")
    origin = _enum_value(getattr(bbox, "coord_origin", "")).lower()
    if origin == "bottomleft":
        page_height = float(page.rect.height)
        y0 = page_height - max(top, bottom)
        y1 = page_height - min(top, bottom)
    else:
        y0 = min(top, bottom)
        y1 = max(top, bottom)
    x0 = min(left, right)
    x1 = max(left, right)
    pad = 1.0
    return pymupdf.Rect(x0 - pad, y0 - pad, x1 + pad, y1 + pad)  # type: ignore[no-untyped-call]


def _float_attr(value: Any, attr: str) -> float:
    try:
        return float(getattr(value, attr))
    except (TypeError, ValueError):
        return 0.0


def _text_from_page_blocks(page: Any, rect: pymupdf.Rect) -> str:
    blocks = page.get_text("blocks", clip=rect, sort=True)
    parts = [str(block[4]).strip() for block in blocks if len(block) > 4 and str(block[4]).strip()]
    return "\n".join(parts).strip()


def _enum_value(value: Any) -> str:
    raw = getattr(value, "value", value)
    if raw is None:
        return ""
    return str(raw).split(".")[-1].lower()
