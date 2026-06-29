"""Crash-isolated Docling execution helpers."""

from __future__ import annotations

import os
import traceback
from dataclasses import dataclass
from multiprocessing import get_context
from pathlib import Path
from tempfile import TemporaryDirectory

from llmwiki.pdf.document import document_model_from_json, document_model_to_json

_DOCLING_TIMEOUT_SECONDS = 20 * 60
_DEFAULT_DOCLING_DEVICES = ("cpu",)
_DOCLING_DEVICE_ENV = "LLMWIKI_DOCLING_DEVICES"
_VALID_DOCLING_DEVICES = frozenset({"auto", "cpu", "cuda"})


@dataclass(frozen=True)
class DoclingAttemptFailure:
    device: str
    detail: str


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


def extract_document_model_isolated(
    pdf_path: Path,
    source_locator: str,
    source_hash: str,
    device: str,
    page_range: tuple[int, int] | None = None,
    timeout_seconds: int | None = None,
) -> object:
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
                page_range,
                str(output_path),
                str(error_path),
            ),
        )
        process.start()
        process.join(timeout_seconds or _DOCLING_TIMEOUT_SECONDS)
        if process.is_alive():
            process.terminate()
            process.join()
            return DoclingAttemptFailure(device, "timed out")
        if process.exitcode == 0 and output_path.is_file():
            return document_model_from_json(output_path.read_text(encoding="utf-8"))
        detail = error_path.read_text(encoding="utf-8").strip() if error_path.is_file() else ""
        return DoclingAttemptFailure(device, detail or _exit_detail(process.exitcode))


def _docling_worker(
    pdf_path: str,
    source_locator: str,
    source_hash: str,
    device: str,
    page_range: tuple[int, int] | None,
    output_path: str,
    error_path: str,
) -> None:
    try:
        from llmwiki.pdf.docling_extractor import _extract_document_model_in_process

        model = _extract_document_model_in_process(
            Path(pdf_path), source_locator, source_hash, device, page_range
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
