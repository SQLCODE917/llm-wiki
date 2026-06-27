"""PDF manifest behavior around ledger-first ingest."""

from fakes import FakeClient
from forge.context import ContextManager, NoCompact

from llmwiki.config import WikiPaths
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.pdf.manifest import ChunkRecord, Manifest, from_json
from llmwiki.pdf.pipeline import ExtractionResult
from llmwiki.runtime.session import Session
from llmwiki.store import WikiStore

TODAY = "2026-06-19"


def _extraction_with_stale_done_chunk(paths: WikiPaths) -> ExtractionResult:
    cache_dir = paths.cache_dir / "deadbeef"
    chunks_dir = cache_dir / "chunks"
    chunks_dir.mkdir(parents=True, exist_ok=True)
    (chunks_dir / "0001.md").write_text("Chunk one: functions are values.", encoding="utf-8")
    (chunks_dir / "0002.md").write_text("Chunk two: closures capture scope.", encoding="utf-8")
    return ExtractionResult(
        manifest=Manifest(
            source="book.pdf",
            sha256="deadbeef" * 8,
            chunks=(
                ChunkRecord(
                    1,
                    "Functions",
                    1,
                    10,
                    4000,
                    status="done",
                    notes="done in a cleared wiki",
                    pages_written=("book-functions",),
                ),
                ChunkRecord(2, "Closures", 11, 20, 3800),
            ),
        ),
        cache_dir=cache_dir,
    )


def _session(store: WikiStore, paths: WikiPaths, extraction: ExtractionResult) -> Session:
    return Session(
        store=store,
        client=FakeClient([]),
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        today=TODAY,
        runs_dir=paths.root / "runs",
        run_id="pdf-stale-resume-test",
        extract_pdf=lambda _pdf, _rel, _reextract: extraction,
    )


async def test_plain_pdf_ingest_uses_ledger_projection_despite_stale_done_chunks(
    store: WikiStore, paths: WikiPaths
) -> None:
    (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
    extraction = _extraction_with_stale_done_chunk(paths)
    store.write_page(
        WikiPage.from_metadata(
            PageMetadata(
                page_id="book-functions",
                page_kind="source",
                summary="Stale generated page.",
                sources=("raw/book.pdf",),
                updated=TODAY,
            ),
            "# Old chunk page",
        )
    )
    session = _session(store, paths, extraction)

    await session.ingest("book.pdf")

    saved = from_json((extraction.cache_dir / "manifest.json").read_text(encoding="utf-8"))
    assert saved.integrated
    assert saved.chunks[0].status == "done"
    assert saved.chunks[0].notes == "done in a cleared wiki"
    assert store.list_pages() == ["book"]
    assert store.read_claim_ledger_artifact("book.pdf") is not None


def test_manifest_requeues_planned_done_chunk_without_recorded_writes() -> None:
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
                status="done",
                notes="claimed done",
                route_plan_pages=1,
            ),
        ),
        integrated=True,
    )

    repaired = manifest.requeue_missing_pages(frozenset())

    assert repaired.pending[0].chunk_id == 1
    assert not repaired.integrated


def test_manifest_requeues_done_chunk_that_only_wrote_hub() -> None:
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
                status="done",
                notes="claimed hub write",
                pages_written=("book",),
                route_plan_pages=2,
            ),
        ),
        integrated=True,
    )

    repaired = manifest.requeue_missing_pages(frozenset({"book"}), hub_page_id="book")

    assert repaired.pending[0].chunk_id == 1
    assert not repaired.integrated


def test_manifest_requeues_done_chunk_when_page_plan_target_changes() -> None:
    manifest = Manifest(
        source="book.pdf",
        sha256="deadbeef" * 8,
        chunks=(
            ChunkRecord(
                58,
                "Treasure and Rewards",
                241,
                242,
                4000,
                status="done",
                notes="Recovered existing wiki page(s): skills",
                pages_written=("skills",),
                route_plan_pages=1,
            ),
        ),
        integrated=True,
    )

    repaired = manifest.requeue_mismatched_pages({58: ("treasure-and-rewards",)})

    assert repaired.pending[0].chunk_id == 58
    assert not repaired.integrated


def test_manifest_requeues_done_chunk_when_page_source_does_not_match() -> None:
    manifest = Manifest(
        source="book.pdf",
        sha256="deadbeef" * 8,
        chunks=(
            ChunkRecord(
                1,
                "Front matter",
                1,
                10,
                4000,
                status="done",
                notes="wrong source page was present",
                pages_written=("book-front-matter",),
                route_plan_pages=1,
            ),
        ),
        integrated=True,
    )

    repaired = manifest.requeue_pages_with_wrong_source(
        {"book-front-matter": ("raw/other.pdf p.1-10",)}, "book.pdf"
    )

    assert repaired.pending[0].chunk_id == 1
    assert not repaired.integrated
