"""Map Docling documents into the PDF domain model."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.layout_structure import (
    LayoutDocument,
    LayoutMatch,
    compile_layout_structure,
    layout_box_from_bbox,
)

CodeTextResolver = Callable[[Any], str]


def document_model_from_docling_document(
    document: Any,
    source_locator: str,
    source_hash: str,
    extractor_version: str,
    code_text_resolver: CodeTextResolver | None = None,
    layout_document: LayoutDocument | None = None,
) -> DocumentModel:
    heading_stack: list[str] = []
    elements: list[DocumentElement] = []

    for item, _level in document.iterate_items():
        text = _item_text(item)
        element_kind = _element_kind(item)
        if element_kind == "code_block" and code_text_resolver is not None:
            text = code_text_resolver(item) or text
        if not text and element_kind != "picture":
            continue

        heading_level = _heading_level(item) if element_kind == "heading" else 0
        if element_kind == "heading":
            level = heading_level
            del heading_stack[level - 1 :]
            heading_stack.append(text)
            heading_path = " > ".join(heading_stack)
        else:
            heading_path = " > ".join(heading_stack) or "Document"

        page_start, page_end = _page_span(item)
        layout = _layout_match(item, text, page_start, layout_document)
        body_state = _body_state(item, heading_path, text)
        markdown = _item_markdown(item, element_kind, text)

        elements.append(
            DocumentElement(
                element_id=f"element-{len(elements) + 1:06d}",
                element_kind=element_kind,
                body_state=body_state,
                heading_path=heading_path,
                page_start=page_start,
                page_end=page_end,
                text=text,
                markdown=markdown,
                heading_level=heading_level,
                layout_font_size=layout.font_size,
                layout_x0=layout.x0,
                layout_y0=layout.y0,
            )
        )

    model = DocumentModel(
        source_locator=source_locator,
        source_hash=source_hash,
        extractor_name="docling",
        extractor_version=extractor_version,
        elements=tuple(elements),
    )
    if layout_document is None:
        return model
    return compile_layout_structure(model, body_font_size=layout_document.body_font_size)


def _element_kind(item: Any) -> str:
    label = _enum_value(getattr(item, "label", ""))
    if label == "section_header":
        return "heading"
    if label == "code":
        return "code_block"
    if label == "table":
        return "table"
    if label == "list_item":
        return "list_item"
    if label == "picture":
        return "picture"
    return "paragraph"


def _heading_level(item: Any) -> int:
    raw_level = getattr(item, "level", 1) or 1
    try:
        level = int(raw_level)
    except (TypeError, ValueError):
        level = 1
    return max(1, min(level, 6))


def _item_text(item: Any) -> str:
    text = getattr(item, "text", "")
    if text is None:
        return ""
    return str(text).strip()


def _item_markdown(item: Any, element_kind: str, text: str) -> str:
    exported = _exported_markdown(item)
    if not text:
        return exported
    if element_kind == "heading":
        level = _heading_level(item)
        return f"{'#' * level} {text}"
    if element_kind == "code_block":
        if _has_fence(exported):
            return exported
        return f"```\n{text.rstrip()}\n```"
    if element_kind == "table" and exported:
        return exported
    if element_kind == "list_item" and not text.lstrip().startswith(("-", "*")):
        return f"- {text}"
    return text


def _exported_markdown(item: Any) -> str:
    for name in ("export_to_markdown", "to_markdown"):
        export = getattr(item, name, None)
        if not callable(export):
            continue
        try:
            value = export()
        except TypeError:
            continue
        if value is not None and str(value).strip():
            return str(value).strip()
    return ""


def _has_fence(markdown: str) -> bool:
    stripped = markdown.lstrip()
    return stripped.startswith("```") or stripped.startswith("~~~")


def _page_span(item: Any) -> tuple[int, int]:
    pages: list[int] = []
    for prov in getattr(item, "prov", []) or []:
        page_no = getattr(prov, "page_no", 0)
        try:
            page = int(page_no)
        except (TypeError, ValueError):
            page = 0
        if page > 0:
            pages.append(page)
    if not pages:
        return (0, 0)
    return (min(pages), max(pages))


def _layout_match(
    item: Any, text: str, page_no: int, layout_document: LayoutDocument | None
) -> LayoutMatch:
    if layout_document is None or page_no <= 0:
        return LayoutMatch()
    box = None
    for prov in getattr(item, "prov", []) or []:
        try:
            prov_page = int(getattr(prov, "page_no", 0) or 0)
        except (TypeError, ValueError):
            prov_page = 0
        if prov_page != page_no:
            continue
        page_height = layout_document.page_heights.get(page_no, 0.0)
        box = layout_box_from_bbox(page_no, page_height, getattr(prov, "bbox", None))
        if box is not None:
            break
    return layout_document.match(page_no, text, box)


def _body_state(item: Any, heading_path: str, text: str) -> str:
    content_layer = _enum_value(getattr(item, "content_layer", "body"))
    if content_layer and content_layer != "body":
        return "furniture"
    heading_parts = [part.strip() for part in heading_path.split(">")]
    if _is_table_of_contents(text) or any(_is_table_of_contents(part) for part in heading_parts):
        return "table_of_contents"
    return "body"


def _is_table_of_contents(value: str) -> bool:
    normalized = " ".join(value.lower().split())
    return normalized in {"contents", "table of contents"}


def _enum_value(value: Any) -> str:
    raw = getattr(value, "value", value)
    return str(raw)
