"""DocumentModel composition helpers."""

from __future__ import annotations

from dataclasses import replace

from llmwiki.pdf.document import DocumentElement, DocumentModel, _has_lexical_content


def merge_document_models(models: tuple[DocumentModel, ...]) -> DocumentModel:
    """Merge source-compatible document models and assign stable element ids."""
    if not models:
        raise ValueError("Cannot merge zero document models.")
    _validate_compatible(models)
    return DocumentModel(
        source_locator=models[0].source_locator,
        source_hash=models[0].source_hash,
        extractor_name=models[0].extractor_name,
        extractor_version=models[0].extractor_version,
        elements=_renumber_elements(_carry_heading_context(_ordered_elements(models))),
    )


def _validate_compatible(models: tuple[DocumentModel, ...]) -> None:
    first = models[0]
    for model in models[1:]:
        if model.source_locator != first.source_locator:
            raise ValueError("Cannot merge document models from different sources.")
        if model.source_hash != first.source_hash:
            raise ValueError("Cannot merge document models with different source hashes.")
        if model.extractor_name != first.extractor_name:
            raise ValueError("Cannot merge document models from different extractors.")
        if model.extractor_version != first.extractor_version:
            raise ValueError("Cannot merge document models from different extractor versions.")


def _ordered_elements(models: tuple[DocumentModel, ...]) -> tuple[DocumentElement, ...]:
    return tuple(element for model in models for element in model.elements)


def _renumber_elements(elements: tuple[DocumentElement, ...]) -> tuple[DocumentElement, ...]:
    return tuple(
        replace(element, element_id=f"element-{index:06d}")
        for index, element in enumerate(elements, start=1)
    )


def _carry_heading_context(elements: tuple[DocumentElement, ...]) -> tuple[DocumentElement, ...]:
    carried = "Document"
    repaired: list[DocumentElement] = []
    for element in elements:
        if element.body_state != "body":
            repaired.append(element)
            continue
        if element.element_kind == "heading":
            carried = _heading_path(element, carried)
            repaired.append(element)
            continue
        if element.heading_path == "Document" and carried != "Document":
            repaired.append(replace(element, heading_path=carried))
        else:
            repaired.append(element)
    return tuple(repaired)


def _heading_path(element: DocumentElement, fallback: str) -> str:
    candidates = (element.heading_path, element.text)
    for candidate in candidates:
        cleaned = " ".join(candidate.split())
        if cleaned != "Document" and _has_lexical_content(cleaned):
            return cleaned
    return fallback
