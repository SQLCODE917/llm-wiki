from __future__ import annotations

import pytest

from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.document_merge import merge_document_models


def _element(
    element_id: str,
    kind: str,
    heading_path: str,
    text: str,
    page: int,
) -> DocumentElement:
    return DocumentElement(
        element_id=element_id,
        element_kind=kind,
        body_state="body",
        heading_path=heading_path,
        page_start=page,
        page_end=page,
        text=text,
        markdown=f"# {text}" if kind == "heading" else text,
    )


def _model(*elements: DocumentElement, source_hash: str = "source-hash") -> DocumentModel:
    return DocumentModel(
        source_locator="book.pdf",
        source_hash=source_hash,
        extractor_name="docling",
        extractor_version="test",
        elements=tuple(elements),
    )


def test_merge_document_models_renumbers_elements() -> None:
    merged = merge_document_models(
        (
            _model(_element("element-000001", "paragraph", "First", "alpha", 1)),
            _model(_element("element-000001", "paragraph", "Second", "beta", 2)),
        )
    )

    assert [element.element_id for element in merged.elements] == [
        "element-000001",
        "element-000002",
    ]
    assert [element.text for element in merged.elements] == ["alpha", "beta"]


def test_merge_document_models_carries_heading_context_across_windows() -> None:
    merged = merge_document_models(
        (
            _model(
                _element("element-000001", "heading", "Skeleton Warrior", "Skeleton Warrior", 10),
                _element("element-000002", "paragraph", "Skeleton Warrior", "It obeys.", 10),
            ),
            _model(
                _element(
                    "element-000001",
                    "paragraph",
                    "Document",
                    "Only the caster commands it.",
                    11,
                )
            ),
        )
    )

    assert [element.heading_path for element in merged.elements] == [
        "Skeleton Warrior",
        "Skeleton Warrior",
        "Skeleton Warrior",
    ]


def test_merge_document_models_rejects_different_sources() -> None:
    with pytest.raises(ValueError, match="different source hashes"):
        merge_document_models(
            (
                _model(_element("element-000001", "paragraph", "Document", "alpha", 1)),
                _model(
                    _element("element-000001", "paragraph", "Document", "beta", 2),
                    source_hash="other",
                ),
            )
        )
