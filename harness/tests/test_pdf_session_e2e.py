"""End-to-end PDF ingest for the source compiler path."""

import pytest
from fakes import FakeClient
from forge.context import ContextManager, NoCompact

from llmwiki.config import WikiPaths
from llmwiki.domain.objects import PagePlan, RawSource, SourceBundle
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.domain.planning import page_plan_to_json
from llmwiki.domain.source_claims import source_claim_groups
from llmwiki.domain.source_map import normalized_source_map_to_json
from llmwiki.domain.source_profile_selector import select_source_profile
from llmwiki.domain.source_profiles import build_evidence_extraction_plan
from llmwiki.domain.typed_evidence_producer import DeterministicTypedEvidenceProducer
from llmwiki.pdf import PdfError
from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.manifest import ChunkRecord, Manifest, from_json
from llmwiki.pdf.pipeline import ExtractionResult, read_source_map, source_map_file
from llmwiki.pdf.source_map_builder import build_normalized_source_map
from llmwiki.runtime.pdf_source_units import extracted_units_from_pdf_cache
from llmwiki.runtime.session import Session
from llmwiki.runtime.typed_evidence_source_claims import source_claims_from_typed_evidence
from llmwiki.store import WikiStore

TODAY = "2026-06-11"


def _fake_extraction(
    paths: WikiPaths, statuses: tuple[str, str] = ("pending", "pending")
) -> ExtractionResult:
    cache_dir = paths.cache_dir / "deadbeef"
    chunks_dir = cache_dir / "chunks"
    chunks_dir.mkdir(parents=True, exist_ok=True)
    (chunks_dir / "0001.md").write_text("Chunk one: functions are values.", encoding="utf-8")
    (chunks_dir / "0002.md").write_text("Chunk two: closures capture scope.", encoding="utf-8")
    manifest = Manifest(
        source="book.pdf",
        sha256="deadbeef" * 8,
        chunks=(
            ChunkRecord(
                1,
                "Functions",
                1,
                10,
                4000,
                status=statuses[0],
                notes="done already" if statuses[0] == "done" else "",
            ),
            ChunkRecord(2, "Closures", 11, 20, 3800, status=statuses[1]),
        ),
    )
    model = DocumentModel(
        source_locator="book.pdf",
        source_hash=manifest.sha256,
        extractor_name="docling",
        extractor_version="test",
        elements=(
            DocumentElement(
                element_id="element-000001",
                element_kind="heading",
                body_state="body",
                heading_path="Functions",
                page_start=1,
                page_end=1,
                text="Functions",
                markdown="# Functions",
            ),
            DocumentElement(
                element_id="element-000002",
                element_kind="paragraph",
                body_state="body",
                heading_path="Functions",
                page_start=1,
                page_end=10,
                text="Chunk one: functions are values.",
                markdown="Chunk one: functions are values.",
            ),
            DocumentElement(
                element_id="element-000003",
                element_kind="heading",
                body_state="body",
                heading_path="Closures",
                page_start=11,
                page_end=11,
                text="Closures",
                markdown="# Closures",
            ),
            DocumentElement(
                element_id="element-000004",
                element_kind="paragraph",
                body_state="body",
                heading_path="Closures",
                page_start=11,
                page_end=20,
                text="Chunk two: closures capture scope.",
                markdown="Chunk two: closures capture scope.",
            ),
        ),
    )
    source_map_file(cache_dir).write_text(
        normalized_source_map_to_json(build_normalized_source_map(model)),
        encoding="utf-8",
    )
    return ExtractionResult(manifest=manifest, cache_dir=cache_dir)


def _session(store: WikiStore, paths: WikiPaths, extraction: ExtractionResult) -> Session:
    notes_seen: list[str] = []
    session = Session(
        store=store,
        client=FakeClient([]),
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        today=TODAY,
        runs_dir=paths.root / "runs",
        run_id="pdf-test",
        extract_pdf=lambda _pdf, _rel, _reextract: extraction,
        on_chunk_note=notes_seen.append,
    )
    object.__setattr__(session, "_notes_seen", notes_seen)
    return session


def _persisted_plan(extraction: ExtractionResult) -> PagePlan:
    raw_source = RawSource.from_locator("book.pdf")
    source_map = read_source_map(extraction.cache_dir)
    assert source_map is not None
    profile_artifact = select_source_profile(source_map)
    extraction_plan = build_evidence_extraction_plan(
        source_map,
        profile_artifact.source_profile,
        profile_artifact.evidence_vocabulary,
    )
    record_set = DeterministicTypedEvidenceProducer().build_record_set(
        source_map,
        profile_artifact,
        extraction_plan,
    )
    source_claims = source_claims_from_typed_evidence(
        raw_source=raw_source,
        source_map=source_map,
        record_set=record_set,
    )
    return PagePlan(
        plan_id="previous-run-pdf-book",
        source_bundle=SourceBundle.one(raw_source),
        extracted_units=extracted_units_from_pdf_cache(raw_source, extraction.cache_dir),
        source_claims=source_claims,
        source_claim_groups=source_claim_groups(source_claims),
        candidate_claims=(),
        candidate_topics=(),
        candidate_entities=(),
        topic_clusters=(),
        wiki_matches=(),
        claim_comparisons=(),
        planned_writes=(),
    )


def test_partial_resume_reuses_matching_persisted_page_plan(
    store: WikiStore, paths: WikiPaths, monkeypatch
) -> None:
    (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
    extraction = _fake_extraction(paths, statuses=("done", "pending"))
    session = _session(store, paths, extraction)
    plan = _persisted_plan(extraction)
    store.write_page_plan_artifacts("book.pdf", page_plan_to_json(plan), "persisted")

    def fail_build_page_plan(**_kwargs: object) -> PagePlan:
        raise AssertionError("partial resume should reuse the persisted PagePlan")

    monkeypatch.setattr("llmwiki.runtime.session.build_page_plan", fail_build_page_plan)

    loaded = session._pdf_page_plan(session._ingest_run("book.pdf"), "book.pdf", extraction)

    assert loaded == plan


async def test_pdf_ingest_ignores_stale_page_plan_cache(
    store: WikiStore, paths: WikiPaths
) -> None:
    (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
    extraction = _fake_extraction(paths)
    stale_plan_json = page_plan_to_json(_persisted_plan(extraction)).replace(
        "Chunk one: functions are values.", "Stale cached text."
    )
    store.write_page_plan_artifacts("book.pdf", stale_plan_json, "persisted")
    extraction_calls: list[bool] = []
    session = Session(
        store=store,
        client=FakeClient([]),
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        today=TODAY,
        runs_dir=paths.root / "runs",
        run_id="pdf-test",
        extract_pdf=lambda _pdf, _rel, _reextract: extraction_calls.append(True) or extraction,
    )

    result = await session.ingest("book.pdf")

    assert result.output.startswith("Ingest compiler run ")
    assert extraction_calls == [True]
    page_plan_json = store.read_page_plan_artifact("book.pdf")
    assert page_plan_json is not None
    assert "Stale cached text." in page_plan_json
    artifact_dir = store.ingest_compiler_artifact_dir("book.pdf")
    assert (artifact_dir / "normalized-source-map.json").is_file()
    assert (artifact_dir / "ingest-artifact-set.json").is_file()
    assert store.list_pages() == ["book"]
    assert "## Compiler Summary" in store.read_page("book")
    assert not session.client.sent


async def test_pdf_ingest_writes_compiler_artifacts(store: WikiStore, paths: WikiPaths) -> None:
    (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
    extraction = _fake_extraction(paths)
    session = _session(store, paths, extraction)

    result = await session.ingest("book.pdf")

    assert result.output.startswith("Ingest compiler run ")
    assert store.list_pages() == ["book"]
    book = store.read_page("book")
    assert "projection_coverage:" in book
    assert "page_family: source-manifest" in book
    assert "## Compiler Summary" in book
    assert "Publication budget:" in book
    assert "Evidence packs:" in book
    artifact_dir = store.ingest_compiler_artifact_dir("book.pdf")
    expected = {
        "ingest-artifact-set.json",
        "normalized-source-map.json",
        "source-profile.json",
        "evidence-extraction-plan.json",
        "evidence-record-set.json",
        "page-publication-plan.json",
        "publication-walkability-report.md",
        "evidence-pack-set.json",
        "human-article.json",
        "human-article-findings.json",
        "article-lint-runs.json",
        "diagnostic-question-set.json",
        "staged-pages.json",
        "lint-run.json",
        "publish-run.json",
    }
    assert expected.issubset({path.name for path in artifact_dir.iterdir()})
    assert not (artifact_dir / "claim-ledger.json").exists()
    saved = from_json((extraction.cache_dir / "manifest.json").read_text(encoding="utf-8"))
    assert saved.integrated
    assert not saved.all_done
    assert not session.client.sent
    assert session._notes_seen  # type: ignore[attr-defined]
    assert session._notes_seen[0].startswith("Ingest compiler run ")  # type: ignore[attr-defined]
    assert paths.log_path.read_text(encoding="utf-8").count("ingest | book.pdf") == 1


def test_pdf_page_plan_uses_source_map_when_chunk_files_are_missing(
    store: WikiStore, paths: WikiPaths
) -> None:
    (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
    extraction = _fake_extraction(paths)
    for chunk_path in (extraction.cache_dir / "chunks").glob("*.md"):
        chunk_path.unlink()
    session = _session(store, paths, extraction)

    plan = session._pdf_page_plan(session._ingest_run("book.pdf"), "book.pdf", extraction)

    assert any("functions are values" in unit.text for unit in plan.extracted_units)
    assert any(unit.unit_id.startswith("prompt-window-") for unit in plan.extracted_units)


def test_pdf_page_plan_fails_without_source_map(store: WikiStore, paths: WikiPaths) -> None:
    (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
    extraction = _fake_extraction(paths)
    source_map_file(extraction.cache_dir).unlink()
    session = _session(store, paths, extraction)

    with pytest.raises(PdfError, match="missing normalized source map"):
        session._pdf_page_plan(session._ingest_run("book.pdf"), "book.pdf", extraction)


async def test_reintegrate_is_removed(
    store: WikiStore, paths: WikiPaths
) -> None:
    (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
    extraction = _fake_extraction(paths)
    session = _session(store, paths, extraction)

    with pytest.raises(PdfError, match="removed"):
        await session.ingest("book.pdf", reintegrate=True)


async def test_pdf_ingest_removes_stale_generated_source_pages(
    store: WikiStore, paths: WikiPaths
) -> None:
    (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
    store.write_page(
        WikiPage.from_metadata(
            PageMetadata(
                page_id="book-functions",
                page_kind="source",
                summary="Stale generated chunk page.",
                sources=("raw/book.pdf",),
                updated=TODAY,
            ),
            "# Stale\n\nOld chunk projection.",
        )
    )
    extraction = _fake_extraction(paths)
    session = _session(store, paths, extraction)

    await session.ingest("book.pdf")

    assert store.list_pages() == ["book"]
