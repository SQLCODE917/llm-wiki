"""Docling adapter for DocumentModel.

This module keeps Docling-specific types out of the PDF domain objects.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any

import pymupdf

from llmwiki.pdf import docling_runtime as _docling_runtime
from llmwiki.pdf.code_text import pdf_code_text as _pdf_code_text
from llmwiki.pdf.docling_document import document_model_from_docling_document
from llmwiki.pdf.docling_windows import (
    PageWindow,
    docling_window_timeout_seconds,
    extract_document_model_windowed,
    should_use_page_windows,
)
from llmwiki.pdf.document import DocumentModel
from llmwiki.pdf.layout_structure import layout_document_from_pdf

_DoclingAttemptFailure = _docling_runtime.DoclingAttemptFailure
docling_devices = _docling_runtime.docling_devices
_extract_document_model_isolated = _docling_runtime.extract_document_model_isolated


def extract_document_model(pdf_path: Path, source_locator: str, source_hash: str) -> DocumentModel:
    page_count = _pdf_page_count(pdf_path)
    failures: list[_DoclingAttemptFailure] = []
    for device in docling_devices():
        result = _extract_with_device(pdf_path, source_locator, source_hash, device, page_count)
        if isinstance(result, DocumentModel):
            return result
        if isinstance(result, _DoclingAttemptFailure):
            failures.append(result)
    raise RuntimeError(
        "Docling extraction failed for "
        f"{source_locator}: "
        + "; ".join(f"{failure.device}: {failure.detail}" for failure in failures)
    )


def _extract_with_device(
    pdf_path: Path,
    source_locator: str,
    source_hash: str,
    device: str,
    page_count: int,
) -> DocumentModel | _DoclingAttemptFailure:
    if should_use_page_windows(page_count):
        return _extract_windows_for_device(
            pdf_path, source_locator, source_hash, device, page_count
        )
    full = _extract_document_model_isolated(pdf_path, source_locator, source_hash, device)
    if isinstance(full, DocumentModel):
        return full
    if not isinstance(full, _DoclingAttemptFailure):
        full = _DoclingAttemptFailure(device, "unexpected extraction result")
    windowed = _extract_windows_for_device(
        pdf_path, source_locator, source_hash, device, page_count
    )
    if isinstance(windowed, DocumentModel):
        return windowed
    return _DoclingAttemptFailure(
        device,
        f"full document failed: {full.detail}; page windows failed: {windowed.detail}",
    )


def _extract_windows_for_device(
    pdf_path: Path,
    source_locator: str,
    source_hash: str,
    device: str,
    page_count: int,
) -> DocumentModel | _DoclingAttemptFailure:
    def extract_window(window: PageWindow) -> DocumentModel | _DoclingAttemptFailure:
        result = _extract_document_model_isolated(
            pdf_path,
            source_locator,
            source_hash,
            device,
            page_range=(window.start, window.end),
            timeout_seconds=docling_window_timeout_seconds(),
        )
        if isinstance(result, DocumentModel):
            return result
        if isinstance(result, _DoclingAttemptFailure):
            return result
        return _DoclingAttemptFailure(device, "unexpected extraction result")

    return extract_document_model_windowed(page_count, device, extract_window)


def _extract_document_model_in_process(
    pdf_path: Path,
    source_locator: str,
    source_hash: str,
    device: str = "auto",
    page_range: tuple[int, int] | None = None,
) -> DocumentModel:
    from docling.datamodel.base_models import InputFormat
    from docling.document_converter import (
        DocumentConverter,
        PdfFormatOption,
    )

    pipeline_options = pdf_pipeline_options(device)
    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options),
        }
    )
    if page_range is None:
        result = converter.convert(pdf_path)
    else:
        result = converter.convert(pdf_path, page_range=page_range)
    with pymupdf.open(pdf_path) as pdf_doc:  # type: ignore[no-untyped-call]
        layout_document = layout_document_from_pdf(pdf_doc)

        def code_text_resolver(item: Any) -> str:
            return _pdf_code_text(pdf_doc, item)

        return document_model_from_docling_document(
            result.document,
            source_locator=source_locator,
            source_hash=source_hash,
            extractor_version=_docling_version(),
            code_text_resolver=code_text_resolver,
            layout_document=layout_document,
        )


def _pdf_page_count(pdf_path: Path) -> int:
    with pymupdf.open(pdf_path) as pdf_doc:  # type: ignore[no-untyped-call]
        return len(pdf_doc)


def pdf_pipeline_options(device: str = "auto") -> Any:
    from docling.datamodel.pipeline_options import PdfPipelineOptions

    pipeline_options = PdfPipelineOptions()
    _set_accelerator_device(pipeline_options, device)
    pipeline_options.do_ocr = False
    if hasattr(pipeline_options, "do_table_structure"):
        pipeline_options.do_table_structure = False
    return pipeline_options


def _set_accelerator_device(pipeline_options: Any, device: str) -> None:
    if device == "auto":
        return
    try:
        from docling.datamodel.accelerator_options import AcceleratorDevice, AcceleratorOptions
    except ImportError:
        return
    selected = {
        "cpu": AcceleratorDevice.CPU,
        "cuda": AcceleratorDevice.CUDA,
    }.get(device)
    if selected is not None:
        pipeline_options.accelerator_options = AcceleratorOptions(device=selected)


def _docling_version() -> str:
    try:
        return version("docling")
    except PackageNotFoundError:
        return "unknown"
