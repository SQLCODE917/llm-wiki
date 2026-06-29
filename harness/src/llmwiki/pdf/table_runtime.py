"""Crash-isolated table enrichment helpers."""

from __future__ import annotations

import traceback
from dataclasses import dataclass
from multiprocessing import get_context
from pathlib import Path
from tempfile import TemporaryDirectory

from llmwiki.pdf.document import DocumentModel, document_model_from_json, document_model_to_json

_TABLE_ENRICHMENT_TIMEOUT_SECONDS = 5 * 60


@dataclass(frozen=True)
class TableEnrichmentFailure:
    detail: str


def enrich_document_model_isolated(
    pdf_path: Path, model: DocumentModel
) -> DocumentModel | TableEnrichmentFailure:
    context = get_context("spawn")
    with TemporaryDirectory(prefix="llmwiki-tables-") as temp_dir:
        input_path = Path(temp_dir) / "input.json"
        output_path = Path(temp_dir) / "output.json"
        error_path = Path(temp_dir) / "error.txt"
        input_path.write_text(document_model_to_json(model), encoding="utf-8")
        process = context.Process(
            target=_table_enrichment_worker,
            args=(str(pdf_path), str(input_path), str(output_path), str(error_path)),
        )
        process.start()
        process.join(_TABLE_ENRICHMENT_TIMEOUT_SECONDS)
        if process.is_alive():
            process.terminate()
            process.join()
            return TableEnrichmentFailure("timed out")
        if process.exitcode == 0 and output_path.is_file():
            return document_model_from_json(output_path.read_text(encoding="utf-8"))
        detail = error_path.read_text(encoding="utf-8").strip() if error_path.is_file() else ""
        return TableEnrichmentFailure(detail or _exit_detail(process.exitcode))


def _table_enrichment_worker(
    pdf_path: str, input_path: str, output_path: str, error_path: str
) -> None:
    try:
        from llmwiki.pdf.table_extractor import _enrich_document_model_with_tables_in_process

        model = document_model_from_json(Path(input_path).read_text(encoding="utf-8"))
        enriched = _enrich_document_model_with_tables_in_process(Path(pdf_path), model)
        Path(output_path).write_text(document_model_to_json(enriched), encoding="utf-8")
    except BaseException:
        Path(error_path).write_text(traceback.format_exc(), encoding="utf-8")
        raise


def _exit_detail(exitcode: int | None) -> str:
    if exitcode is None:
        return "no child-process exit code"
    if exitcode < 0:
        return f"killed by signal {-exitcode}"
    return f"exited with code {exitcode}"
