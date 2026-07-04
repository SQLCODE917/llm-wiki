from pathlib import Path

from llmwiki.config import WikiPaths
from llmwiki.domain.source_map import normalized_source_map_to_json
from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.manifest import ChunkRecord, Manifest, to_json
from llmwiki.pdf.pipeline import ExtractionResult, source_map_file
from llmwiki.pdf.source_map_builder import build_normalized_source_map
from llmwiki.runtime.ingest_confidence_page_plan_artifacts import build_current_page_plan
from llmwiki.runtime.ingest_confidence_pdf_cache import (
    pdf_extraction_artifact,
    raw_source_hash,
)
from llmwiki.store import WikiStore


def test_pdf_extraction_cache_rebuilds_when_current_artifacts_are_missing(
    paths: WikiPaths,
) -> None:
    raw_path = paths.raw_dir / "book.pdf"
    raw_path.write_bytes(b"fake pdf bytes")
    source_hash = raw_source_hash(raw_path)
    cache_dir = paths.cache_dir / source_hash[:16]
    cache_dir.mkdir(parents=True)
    manifest = Manifest(
        source="book.pdf",
        sha256=source_hash,
        chunks=(ChunkRecord(1, "Rules", 1, 1, 10),),
        extractor_name="docling",
    )
    (cache_dir / "manifest.json").write_text(to_json(manifest), encoding="utf-8")
    calls = 0

    def extract_pdf(_path: Path, _locator: str, _fresh: bool) -> ExtractionResult:
        nonlocal calls
        calls += 1
        return ExtractionResult(manifest=manifest, cache_dir=cache_dir)

    _result, decision, findings = pdf_extraction_artifact(
        WikiStore(paths),
        paths.cache_dir,
        "book.pdf",
        source_hash,
        fresh=False,
        extract_pdf=extract_pdf,
    )

    assert calls == 1
    assert decision is not None
    assert decision.decision == "rebuild"
    assert "current PDF table artifacts" in decision.reason
    assert findings == ()


def test_current_page_plan_uses_source_map_when_chunks_are_missing(paths: WikiPaths) -> None:
    raw_path = paths.raw_dir / "book.pdf"
    raw_path.write_bytes(b"fake pdf bytes")
    source_hash = raw_source_hash(raw_path)
    cache_dir = paths.cache_dir / source_hash[:16]
    cache_dir.mkdir(parents=True)
    manifest = Manifest(
        source="book.pdf",
        sha256=source_hash,
        chunks=(ChunkRecord(1, "Rules", 1, 1, 10),),
        extractor_name="docling",
    )
    model = DocumentModel(
        source_locator="book.pdf",
        source_hash=source_hash,
        extractor_name="docling",
        extractor_version="test",
        elements=(
            DocumentElement(
                element_id="element-000001",
                element_kind="heading",
                body_state="body",
                heading_path="Rules",
                page_start=1,
                page_end=1,
                text="Rules",
                markdown="# Rules",
            ),
            DocumentElement(
                element_id="element-000002",
                element_kind="paragraph",
                body_state="body",
                heading_path="Rules",
                page_start=1,
                page_end=1,
                text="Rules come from the source map.",
                markdown="Rules come from the source map.",
            ),
        ),
    )
    result = ExtractionResult(manifest=manifest, cache_dir=cache_dir)
    source_map_file(cache_dir).write_text(
        normalized_source_map_to_json(build_normalized_source_map(model)),
        encoding="utf-8",
    )

    plan = build_current_page_plan(WikiStore(paths), "book.pdf", "2026-07-04", (), result)

    assert plan is not None
    assert plan.extracted_units[0].unit_id.startswith("prompt-window-")
    assert "source map" in plan.extracted_units[0].text
