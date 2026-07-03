"""End-to-end PDF ingest for ledger-first projection."""

from fakes import FakeClient
from forge.context import ContextManager, NoCompact

from llmwiki.config import WikiPaths
from llmwiki.domain.objects import ExtractedUnit, PagePlan, RawSource, SourceBundle
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.domain.planning import page_plan_to_json
from llmwiki.pdf.manifest import ChunkRecord, Manifest, from_json
from llmwiki.pdf.pipeline import ExtractionResult
from llmwiki.runtime.session import Session
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


def _persisted_plan() -> PagePlan:
    raw_source = RawSource.from_locator("book.pdf")
    return PagePlan(
        plan_id="previous-run-pdf-book",
        source_bundle=SourceBundle.one(raw_source),
        extracted_units=(
            ExtractedUnit(
                unit_id="unit-0001",
                raw_source=raw_source,
                locator="p.1-10",
                heading_path="Functions",
                text="Chunk one: functions are values.",
                extraction_status="ok",
            ),
            ExtractedUnit(
                unit_id="unit-0002",
                raw_source=raw_source,
                locator="p.11-20",
                heading_path="Closures",
                text="Chunk two: closures capture scope.",
                extraction_status="ok",
            ),
        ),
        source_claims=(),
        source_claim_groups=(),
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
    plan = _persisted_plan()
    store.write_page_plan_artifacts("book.pdf", page_plan_to_json(plan), "persisted")

    def fail_build_page_plan(**_kwargs: object) -> PagePlan:
        raise AssertionError("partial resume should reuse the persisted PagePlan")

    monkeypatch.setattr("llmwiki.runtime.session.build_page_plan", fail_build_page_plan)

    loaded = session._pdf_page_plan(session._ingest_run("book.pdf"), "book.pdf", extraction)

    assert loaded == plan


async def test_pdf_ingest_consults_extraction_cache_before_persisted_page_plan(
    store: WikiStore, paths: WikiPaths
) -> None:
    (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
    stale_plan_json = page_plan_to_json(_persisted_plan()).replace(
        "Chunk one: functions are values.", "Stale cached text."
    )
    store.write_page_plan_artifacts("book.pdf", stale_plan_json, "persisted")
    extraction = _fake_extraction(paths)
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

    assert result.output.startswith("Claim-ledger ingest of raw/book.pdf")
    assert extraction_calls == [True]
    page_plan_json = store.read_page_plan_artifact("book.pdf")
    assert page_plan_json is not None
    assert "Chunk one: functions are values." in page_plan_json
    assert "Stale cached text." not in page_plan_json
    assert store.list_pages() == ["book"]
    assert "closures capture scope" in store.read_page("book")
    assert not session.client.sent


async def test_pdf_ingest_writes_ledger_projection(store: WikiStore, paths: WikiPaths) -> None:
    (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
    extraction = _fake_extraction(paths)
    session = _session(store, paths, extraction)

    result = await session.ingest("book.pdf")

    assert result.output.startswith("Claim-ledger ingest of raw/book.pdf")
    assert store.list_pages() == ["book"]
    book = store.read_page("book")
    assert "projection_coverage:" in book
    assert "page_family: source-manifest" in book
    assert "## Page Families" in book
    ledger_dir = store.page_plan_artifact_dir("book.pdf") / "ledger"
    assert (ledger_dir / "claim-ledger.json").is_file()
    assert (ledger_dir / "projection-coverage.json").is_file()
    assert (ledger_dir / "section-plan.json").is_file()
    assert (ledger_dir / "topics.json").is_file()
    saved = from_json((extraction.cache_dir / "manifest.json").read_text(encoding="utf-8"))
    assert saved.integrated
    assert not saved.all_done
    assert not session.client.sent
    assert session._notes_seen == [  # type: ignore[attr-defined]
        "Claim-ledger projection (general-prose): 1 usable entries, 0 technical atoms, "
        "1 needs-review, 0 linked page(s); write decision write-with-review-work."
    ]
    assert paths.log_path.read_text(encoding="utf-8").count("ingest | book.pdf") == 1


async def test_reintegrate_refreshes_ledger_projection_with_pending_manifest(
    store: WikiStore, paths: WikiPaths
) -> None:
    (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
    extraction = _fake_extraction(paths)
    session = _session(store, paths, extraction)

    result = await session.ingest("book.pdf", reintegrate=True)

    assert result.output.startswith("Claim-ledger ingest of raw/book.pdf")
    saved = from_json((extraction.cache_dir / "manifest.json").read_text(encoding="utf-8"))
    assert saved.integrated
    assert store.read_claim_ledger_artifact("book.pdf") is not None


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
