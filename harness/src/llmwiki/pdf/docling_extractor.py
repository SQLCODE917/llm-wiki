"""Docling adapter for DocumentModel."""

from __future__ import annotations

import os
import traceback
from dataclasses import dataclass
from importlib.metadata import PackageNotFoundError, version
from multiprocessing import get_context
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

from llmwiki.pdf.document import (
    DocumentElement,
    DocumentModel,
    document_model_from_json,
    document_model_to_json,
)

_DOCLING_TIMEOUT_SECONDS = 20 * 60
_DEFAULT_DOCLING_DEVICES = ("cpu",)
_DOCLING_DEVICE_ENV = "LLMWIKI_DOCLING_DEVICES"
_VALID_DOCLING_DEVICES = frozenset({"auto", "cpu", "cuda"})


@dataclass(frozen=True)
class _DoclingAttemptFailure:
    device: str
    detail: str


def extract_document_model(pdf_path: Path, source_locator: str, source_hash: str) -> DocumentModel:
    failures: list[_DoclingAttemptFailure] = []
    for device in docling_devices():
        result = _extract_document_model_isolated(pdf_path, source_locator, source_hash, device)
        if isinstance(result, DocumentModel):
            return result
        failures.append(result)
    raise RuntimeError(
        "Docling extraction failed for "
        f"{source_locator}: "
        + "; ".join(f"{failure.device}: {failure.detail}" for failure in failures)
    )


def docling_devices() -> tuple[str, ...]:
    raw_devices = os.environ.get(_DOCLING_DEVICE_ENV)
    if raw_devices is None or not raw_devices.strip():
        return _DEFAULT_DOCLING_DEVICES
    devices = tuple(device.strip().lower() for device in raw_devices.split(",") if device.strip())
    invalid = tuple(device for device in devices if device not in _VALID_DOCLING_DEVICES)
    if not devices or invalid:
        valid = ", ".join(sorted(_VALID_DOCLING_DEVICES))
        raise ValueError(
            f"{_DOCLING_DEVICE_ENV} must contain comma-separated values from: {valid}."
        )
    return devices


def _extract_document_model_isolated(
    pdf_path: Path, source_locator: str, source_hash: str, device: str
) -> DocumentModel | _DoclingAttemptFailure:
    context = get_context("spawn")
    with TemporaryDirectory(prefix="llmwiki-docling-") as temp_dir:
        output_path = Path(temp_dir) / "document_model.json"
        error_path = Path(temp_dir) / "error.txt"
        process = context.Process(
            target=_docling_worker,
            args=(
                str(pdf_path),
                source_locator,
                source_hash,
                device,
                str(output_path),
                str(error_path),
            ),
        )
        process.start()
        process.join(_DOCLING_TIMEOUT_SECONDS)
        if process.is_alive():
            process.terminate()
            process.join()
            return _DoclingAttemptFailure(device, "timed out")
        if process.exitcode == 0 and output_path.is_file():
            return document_model_from_json(output_path.read_text(encoding="utf-8"))
        detail = error_path.read_text(encoding="utf-8").strip() if error_path.is_file() else ""
        return _DoclingAttemptFailure(device, detail or _exit_detail(process.exitcode))


def _docling_worker(
    pdf_path: str,
    source_locator: str,
    source_hash: str,
    device: str,
    output_path: str,
    error_path: str,
) -> None:
    try:
        model = _extract_document_model_in_process(
            Path(pdf_path), source_locator, source_hash, device
        )
        Path(output_path).write_text(document_model_to_json(model), encoding="utf-8")
    except BaseException:
        Path(error_path).write_text(traceback.format_exc(), encoding="utf-8")
        raise


def _exit_detail(exitcode: int | None) -> str:
    if exitcode is None:
        return "no child-process exit code"
    if exitcode < 0:
        return f"killed by signal {-exitcode}"
    return f"exited with code {exitcode}"


def _extract_document_model_in_process(
    pdf_path: Path, source_locator: str, source_hash: str, device: str = "auto"
) -> DocumentModel:
    from docling.datamodel.base_models import InputFormat
    from docling.document_converter import DocumentConverter, PdfFormatOption

    pipeline_options = pdf_pipeline_options(device)
    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options),
        }
    )
    result = converter.convert(pdf_path)
    return document_model_from_docling_document(
        result.document,
        source_locator=source_locator,
        source_hash=source_hash,
        extractor_version=_docling_version(),
    )


def pdf_pipeline_options(device: str = "auto") -> Any:
    from docling.datamodel.accelerator_options import AcceleratorDevice, AcceleratorOptions
    from docling.datamodel.pipeline_options import PdfPipelineOptions

    pipeline_options = PdfPipelineOptions()
    if device == "cpu":
        pipeline_options.accelerator_options = AcceleratorOptions(device=AcceleratorDevice.CPU)
    if device == "cuda":
        pipeline_options.accelerator_options = AcceleratorOptions(device=AcceleratorDevice.CUDA)
    pipeline_options.do_ocr = False
    # The harness has a source-neutral table recovery layer after Docling. Avoid
    # Docling TableFormer here: it is slower, less portable, and can fail inside
    # native/ML dependencies before our table fallback has a chance to run.
    pipeline_options.do_table_structure = False
    return pipeline_options


def document_model_from_docling_document(
    document: Any,
    source_locator: str,
    source_hash: str,
    extractor_version: str,
) -> DocumentModel:
    heading_stack: list[str] = []
    elements: list[DocumentElement] = []

    for item, _level in document.iterate_items():
        text = _item_text(item)
        element_kind = _element_kind(item)
        if not text and element_kind != "picture":
            continue

        if element_kind == "heading":
            level = _heading_level(item)
            del heading_stack[level - 1 :]
            heading_stack.append(text)
            heading_path = " > ".join(heading_stack)
        else:
            heading_path = " > ".join(heading_stack) or "Document"

        page_start, page_end = _page_span(item)
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
            )
        )

    return DocumentModel(
        source_locator=source_locator,
        source_hash=source_hash,
        extractor_name="docling",
        extractor_version=extractor_version,
        elements=tuple(elements),
    )


def _docling_version() -> str:
    try:
        return version("docling")
    except PackageNotFoundError:
        return "unknown"


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
    if not text:
        return ""
    if element_kind == "heading":
        level = _heading_level(item)
        return f"{'#' * level} {text}"
    if element_kind == "code_block":
        return f"```\n{text.rstrip()}\n```"
    if element_kind == "list_item" and not text.lstrip().startswith(("-", "*")):
        return f"- {text}"
    return text


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
