"""Extraction pipeline orchestrator: PDF -> cached chunks + manifest.

Derived artifacts live under <cache_root>/<sha256-prefix>/ — disposable,
reproducible, never part of the wiki's three layers. Re-running with an
existing manifest is a cache hit (the resume path); OCR results, including
confirmed-empty ones, are cached so re-extraction never re-runs recognition.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

from llmwiki.pdf import ScannedPdfError
from llmwiki.pdf.chunking import Chunk, build_sections, pack_chunks
from llmwiki.pdf.classify import PdfKind, classify_pdf
from llmwiki.pdf.extractor import extract_pdf, read_page_char_counts
from llmwiki.pdf.intermediate import fold_ocr_into_page
from llmwiki.pdf.manifest import ChunkRecord, Manifest, from_json, to_json
from llmwiki.pdf.recognizer import TextRecognizer, usable_text

_MANIFEST_FILE = "manifest.json"
_OCR_FILE = "ocr.json"
_CHUNK_DIR = "chunks"


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


def _run_figure_ocr(
    cache_dir: Path, image_files: list[str], recognizer: TextRecognizer
) -> dict[str, str]:
    """OCR every extracted figure once; cache all results, empty included."""
    ocr_path = cache_dir / _OCR_FILE
    if ocr_path.exists():
        cached: dict[str, str | None] = json.loads(ocr_path.read_text(encoding="utf-8"))
    else:
        cached = {}
    for name in image_files:
        if name not in cached:
            spans = recognizer.recognize(cache_dir / "images" / name)
            cached[name] = usable_text(spans)  # None == decorative == normal
    ocr_path.write_text(json.dumps(cached, indent=2, ensure_ascii=False), encoding="utf-8")
    return {name: text for name, text in cached.items() if text}


def ensure_extracted(
    pdf_path: Path,
    source_rel: str,
    cache_root: Path,
    recognizer: TextRecognizer,
    reextract: bool = False,
) -> ExtractionResult:
    """Extract + chunk the PDF, or return the cached manifest (resume)."""
    sha = _sha256(pdf_path)
    cache_dir = cache_root / sha[:16]
    manifest_path = cache_dir / _MANIFEST_FILE

    if manifest_path.exists() and not reextract:
        return ExtractionResult(
            manifest=from_json(manifest_path.read_text(encoding="utf-8")),
            cache_dir=cache_dir,
        )

    if classify_pdf(read_page_char_counts(pdf_path)) is PdfKind.SCANNED:
        raise ScannedPdfError(
            f"raw/{source_rel} looks like a scanned (image-only) PDF; "
            "whole-document OCR is not enabled yet "
            "(docs/2026-06-11-pdf-ingestion-design.md)."
        )

    extracted = extract_pdf(pdf_path, cache_dir)
    figure_text = _run_figure_ocr(cache_dir, extracted.image_files, recognizer)
    page_texts = [fold_ocr_into_page(t, figure_text) for t in extracted.page_texts]

    chunks = pack_chunks(build_sections(extracted.toc, page_texts))
    (cache_dir / _CHUNK_DIR).mkdir(parents=True, exist_ok=True)
    for chunk in chunks:
        chunk_file(cache_dir, chunk.chunk_id).write_text(chunk.text, encoding="utf-8")

    manifest = Manifest(
        source=source_rel,
        sha256=sha,
        chunks=tuple(_record(c) for c in chunks),
    )
    result = ExtractionResult(manifest=manifest, cache_dir=cache_dir)
    save_manifest(result)
    return result


def _record(chunk: Chunk) -> ChunkRecord:
    return ChunkRecord(
        chunk_id=chunk.chunk_id,
        heading=chunk.heading,
        start_page=chunk.start_page,
        end_page=chunk.end_page,
        token_estimate=chunk.token_estimate,
    )
