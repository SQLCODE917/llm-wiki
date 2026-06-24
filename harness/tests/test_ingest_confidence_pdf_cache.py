from pathlib import Path

from llmwiki.config import WikiPaths
from llmwiki.pdf.manifest import ChunkRecord, Manifest, to_json
from llmwiki.pdf.pipeline import ExtractionResult
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
