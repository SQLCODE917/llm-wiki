"""Extraction pipeline orchestrator: PDF -> cached DocumentModel + chunks + manifest.

Derived artifacts live under <cache_root>/<sha256-prefix>/ — disposable,
reproducible, never part of the wiki's three layers. Re-running with an
existing manifest is a cache hit (the resume path).
"""

from __future__ import annotations

import hashlib
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from llmwiki.pdf import ScannedPdfError
from llmwiki.pdf.classify import PdfKind, classify_pdf
from llmwiki.pdf.document import (
    DocumentModel,
    SourceChunk,
    build_source_chunks,
    build_source_sections,
    document_model_to_json,
    source_sections_to_json,
)
from llmwiki.pdf.manifest import ChunkRecord, Manifest, from_json, to_json
from llmwiki.pdf.recognizer import TextRecognizer

_MANIFEST_FILE = "manifest.json"
_DOCUMENT_MODEL_FILE = "document_model.json"
_SOURCE_SECTIONS_FILE = "source_sections.json"
_CHUNK_DIR = "chunks"

DocumentExtractFn = Callable[[Path, str, str], DocumentModel]


@dataclass(frozen=True)
class ExtractionResult:
    manifest: Manifest
    cache_dir: Path


def chunk_file(cache_dir: Path, chunk_id: int) -> Path:
    return cache_dir / _CHUNK_DIR / f"{chunk_id:04d}.md"


def read_source_text(cache_dir: Path) -> str:
    """The whole extracted source (all chunks) — salience's mention corpus."""
    chunk_dir = cache_dir / _CHUNK_DIR
    if not chunk_dir.is_dir():
        return ""
    return "\n\n".join(p.read_text(encoding="utf-8") for p in sorted(chunk_dir.glob("*.md")))


def save_manifest(result: ExtractionResult) -> None:
    (result.cache_dir / _MANIFEST_FILE).write_text(to_json(result.manifest), encoding="utf-8")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def ensure_extracted(
    pdf_path: Path,
    source_rel: str,
    cache_root: Path,
    recognizer: TextRecognizer,
    reextract: bool = False,
    document_extractor: DocumentExtractFn | None = None,
) -> ExtractionResult:
    """Extract + chunk the PDF, or return the cached manifest (resume)."""
    _ = recognizer
    sha = _sha256(pdf_path)
    cache_dir = cache_root / sha[:16]
    manifest_path = cache_dir / _MANIFEST_FILE

    if manifest_path.exists() and not reextract:
        return ExtractionResult(
            manifest=from_json(manifest_path.read_text(encoding="utf-8")),
            cache_dir=cache_dir,
        )

    from llmwiki.pdf.extractor import read_page_char_counts

    if classify_pdf(read_page_char_counts(pdf_path)) is PdfKind.SCANNED:
        raise ScannedPdfError(
            f"raw/{source_rel} looks like a scanned (image-only) PDF; "
            "whole-document OCR is not enabled yet "
            "(docs/2026-06-11-pdf-ingestion-design.md)."
        )

    cache_dir.mkdir(parents=True, exist_ok=True)
    document_extractor = document_extractor or _default_document_extractor()
    document_model = document_extractor(pdf_path, source_rel, sha)
    source_sections = build_source_sections(document_model)
    source_chunks = build_source_chunks(document_model, source_sections)

    (cache_dir / _DOCUMENT_MODEL_FILE).write_text(
        document_model_to_json(document_model), encoding="utf-8"
    )
    (cache_dir / _SOURCE_SECTIONS_FILE).write_text(
        source_sections_to_json(source_sections), encoding="utf-8"
    )

    chunk_dir = cache_dir / _CHUNK_DIR
    chunk_dir.mkdir(parents=True, exist_ok=True)
    for old_chunk in chunk_dir.glob("*.md"):
        old_chunk.unlink()
    for chunk in source_chunks:
        chunk_file(cache_dir, chunk.chunk_id).write_text(chunk.text, encoding="utf-8")

    manifest = Manifest(
        source=source_rel,
        sha256=sha,
        extractor_name=document_model.extractor_name,
        chunks=tuple(_record(c) for c in source_chunks),
    )
    result = ExtractionResult(manifest=manifest, cache_dir=cache_dir)
    save_manifest(result)
    return result


def _default_document_extractor() -> DocumentExtractFn:
    from llmwiki.pdf.docling_extractor import extract_document_model

    return extract_document_model


def _record(chunk: SourceChunk) -> ChunkRecord:
    return ChunkRecord(
        chunk_id=chunk.chunk_id,
        heading=chunk.heading_path,
        start_page=chunk.page_start,
        end_page=chunk.page_end,
        token_estimate=chunk.token_estimate,
    )
