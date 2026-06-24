"""PDF cache handling for ingest confidence artifact preparation."""

from __future__ import annotations

import hashlib
from collections.abc import Callable
from pathlib import Path

from llmwiki.domain.ingest_confidence import (
    ArtifactReuseDecision,
    ValidationFinding,
    validation_finding,
)
from llmwiki.pdf.pipeline import ExtractionResult, cache_has_current_pdf_artifacts
from llmwiki.store import WikiStore

PdfExtractFn = Callable[[Path, str, bool], ExtractionResult]


def raw_source_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def pdf_extraction_artifact(
    store: WikiStore,
    cache_dir: Path,
    source_locator: str,
    source_hash: str,
    *,
    fresh: bool,
    extract_pdf: PdfExtractFn | None,
) -> tuple[ExtractionResult | None, ArtifactReuseDecision | None, tuple[ValidationFinding, ...]]:
    if not source_locator.lower().endswith(".pdf"):
        return None, None, ()
    existing = _pdf_extraction_result(cache_dir, source_locator, source_hash)
    has_current_artifacts = (
        existing is not None and cache_has_current_pdf_artifacts(existing.cache_dir)
    )
    decision = ArtifactReuseDecision(
        artifact_kind="pdf-extraction",
        artifact_path=str(existing.cache_dir if existing else cache_dir),
        decision="reuse" if has_current_artifacts and not fresh else "rebuild",
        reason=(
            "source hash matches"
            if has_current_artifacts and not fresh
            else "cache lacks current PDF table artifacts"
            if existing is not None and not has_current_artifacts
            else "cache missing, stale, or fresh"
        ),
        fingerprint=source_hash[:16],
    )
    if has_current_artifacts and not fresh:
        return existing, decision, ()
    if extract_pdf is None:
        return (
            None,
            decision,
            (runtime_finding(source_locator, "PDF extraction cache is unavailable."),),
        )
    try:
        return (
            extract_pdf(store.raw_source_path(source_locator), source_locator, True),
            decision,
            (),
        )
    except Exception as exc:
        return (
            None,
            decision,
            (runtime_finding(source_locator, f"PDF extraction rebuild failed: {exc}"),),
        )


def runtime_finding(source_locator: str, message: str) -> ValidationFinding:
    return validation_finding(
        severity="blocker",
        category="runtime",
        source_locator=source_locator,
        message=message,
    )


def _pdf_extraction_result(
    cache_dir: Path, source_locator: str, source_hash: str
) -> ExtractionResult | None:
    from llmwiki.pdf.manifest import from_json as manifest_from_json

    for manifest_path in sorted(cache_dir.glob("*/manifest.json")):
        try:
            manifest = manifest_from_json(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if manifest.source == source_locator and manifest.sha256 == source_hash:
            return ExtractionResult(manifest=manifest, cache_dir=manifest_path.parent)
    return None
