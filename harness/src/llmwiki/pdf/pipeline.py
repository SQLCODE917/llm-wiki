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
from typing import Literal

from llmwiki.pdf import ScannedPdfError
from llmwiki.pdf.classify import PdfKind, classify_pdf
from llmwiki.pdf.document import (
    DocumentModel,
    SourceChunk,
    _has_lexical_content,
    build_source_chunks,
    build_source_sections,
    document_model_from_json,
    document_model_to_json,
    source_sections_to_json,
)
from llmwiki.pdf.manifest import ChunkRecord, Manifest, from_json, to_json
from llmwiki.pdf.recognizer import TextRecognizer
from llmwiki.pdf.table_extractor import enrich_document_model_with_tables

_MANIFEST_FILE = "manifest.json"
_DOCUMENT_MODEL_FILE = "document_model.json"
_SOURCE_SECTIONS_FILE = "source_sections.json"
_CHUNK_DIR = "chunks"

DocumentExtractFn = Callable[[Path, str, str], DocumentModel]
DocumentExtractorName = Literal["docling", "pymupdf"]
VALID_DOCUMENT_EXTRACTORS: tuple[DocumentExtractorName, ...] = ("docling", "pymupdf")


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


def read_document_model(cache_dir: Path) -> DocumentModel | None:
    path = cache_dir / _DOCUMENT_MODEL_FILE
    if not path.is_file():
        return None
    return document_model_from_json(path.read_text(encoding="utf-8"))


def cache_has_current_pdf_artifacts(cache_dir: Path) -> bool:
    return (
        (cache_dir / _MANIFEST_FILE).is_file()
        and (cache_dir / _DOCUMENT_MODEL_FILE).is_file()
        and (cache_dir / _SOURCE_SECTIONS_FILE).is_file()
    )


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
    document_extractor_name: str = "docling",
) -> ExtractionResult:
    """Extract + chunk the PDF, or return the cached manifest (resume)."""
    _ = recognizer
    sha = _sha256(pdf_path)
    cache_dir = cache_root / sha[:16]
    manifest_path = cache_dir / _MANIFEST_FILE

    if cache_has_current_pdf_artifacts(cache_dir) and not reextract:
        manifest = from_json(manifest_path.read_text(encoding="utf-8"))
        if manifest.integrated:
            return ExtractionResult(manifest=manifest, cache_dir=cache_dir)
        if _requires_derived_artifact_rebuild(cache_dir, manifest):
            document_model = document_model_from_json(
                (cache_dir / _DOCUMENT_MODEL_FILE).read_text(encoding="utf-8")
            )
            return _write_derived_artifacts(cache_dir, source_rel, document_model)
        return ExtractionResult(
            manifest=manifest,
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
    document_extractor = document_extractor or document_extractor_by_name(document_extractor_name)
    document_model = document_extractor(pdf_path, source_rel, sha)
    document_model = enrich_document_model_with_tables(pdf_path, document_model)
    return _write_derived_artifacts(cache_dir, source_rel, document_model)


def _write_derived_artifacts(
    cache_dir: Path,
    source_rel: str,
    document_model: DocumentModel,
) -> ExtractionResult:
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
        sha256=document_model.source_hash,
        extractor_name=document_model.extractor_name,
        chunks=tuple(_record(c) for c in source_chunks),
    )
    result = ExtractionResult(manifest=manifest, cache_dir=cache_dir)
    save_manifest(result)
    return result


def _requires_derived_artifact_rebuild(cache_dir: Path, manifest: Manifest) -> bool:
    for record in manifest.chunks:
        if not _has_lexical_content(record.heading):
            return True
        path = chunk_file(cache_dir, record.chunk_id)
        if path.is_file() and not _has_lexical_content(path.read_text(encoding="utf-8")):
            return True
    return False


def document_extractor_by_name(name: str) -> DocumentExtractFn:
    if name == "docling":
        from llmwiki.pdf.docling_extractor import extract_document_model

        return extract_document_model
    if name == "pymupdf":
        from llmwiki.pdf.pymupdf_document_extractor import extract_document_model

        return extract_document_model
    valid = ", ".join(VALID_DOCUMENT_EXTRACTORS)
    raise ValueError(f"Unknown PDF extractor {name!r}. Valid extractors: {valid}.")


def _record(chunk: SourceChunk) -> ChunkRecord:
    return ChunkRecord(
        chunk_id=chunk.chunk_id,
        heading=chunk.heading_path,
        start_page=chunk.page_start,
        end_page=chunk.page_end,
        token_estimate=chunk.token_estimate,
    )
