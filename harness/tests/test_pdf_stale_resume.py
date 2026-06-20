"""PDF resume safety when generated wiki pages were cleared."""

import json
from typing import cast

import pytest
from fakes import FakeClient
from forge.context import ContextManager, NoCompact
from forge.core.workflow import ToolCall

from llmwiki.config import WikiPaths
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.pdf import PdfError
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
                    pages_written=("functions",),
                ),
                ChunkRecord(2, "Closures", 11, 20, 3800),
            ),
        ),
        cache_dir=cache_dir,
    )


def _one_chunk_extraction(paths: WikiPaths) -> ExtractionResult:
    cache_dir = paths.cache_dir / "feedface"
    chunks_dir = cache_dir / "chunks"
    chunks_dir.mkdir(parents=True, exist_ok=True)
    (chunks_dir / "0001.md").write_text("Chunk one: functions are values.", encoding="utf-8")
    return ExtractionResult(
        manifest=Manifest(
            source="book.pdf",
            sha256="feedface" * 8,
            chunks=(ChunkRecord(1, "Functions", 1, 10, 4000),),
        ),
        cache_dir=cache_dir,
    )


def _plan_page_call(page_id: str, *, action: str = "create") -> ToolCall:
    return ToolCall(
        tool="plan_pages",
        args={
            "planned_pages": [
                {
                    "metadata": {
                        "page_id": page_id,
                        "page_kind": "source",
                        "summary": f"About {page_id}.",
                        "sources": ["book.pdf"],
                    },
                    "role": "source page for this PDF ingest stage",
                    "action": action,
                    "source_scope": "book.pdf",
                    "confidence": "high",
                    "rationale": f"{page_id} is the durable page for this PDF ingest stage.",
                }
            ],
            "gaps": [],
        },
    )


def _write_page_call(
    page_id: str,
    *,
    claim_ids: tuple[str, ...] | None = None,
) -> ToolCall:
    return ToolCall(
        tool="write_page",
        args=_source_summary_write_args(page_id, claim_ids=claim_ids),
    )


def _source_summary_write_args(
    page_id: str,
    *,
    claim_ids: tuple[str, ...] | None = None,
) -> dict[str, object]:
    active_claim_ids = claim_ids or _source_claim_ids_for(page_id)
    citation = _citation_for(page_id)
    claim_text = "Hub links [[functions]] and [[closures]]."
    if page_id != "book":
        claim_text = f"The {page_id} source page summarizes this PDF stage."
    return {
        "page_id": page_id,
        "page_kind": "source",
        "summary": f"About {page_id}.",
        "source_record_text": f"Source record for [[{page_id}]]. ({citation})",
        "claim_bullets": [
            {
                "bullet_text": f"{claim_text} ({citation})",
                "covered_source_claims": list(active_claim_ids),
            },
            {
                "bullet_text": f"The draft preserves planned source coverage. ({citation})",
                "covered_source_claims": [active_claim_ids[0]],
            },
            {
                "bullet_text": f"The summary keeps the cited PDF support visible. ({citation})",
                "covered_source_claims": [active_claim_ids[-1]],
            },
        ],
        "sources": ["book.pdf"],
    }


def _source_summary_body(args: dict[str, object]) -> str:
    claim_bullets = cast(list[dict[str, object]], args["claim_bullets"])
    bullets = "\n".join(f"- {bullet['bullet_text']}" for bullet in claim_bullets)
    return (
        f"## Source record\n\n{args['source_record_text']}\n\n"
        f"## Key supported claims\n\n{bullets}"
    )


def _write_source_summary_artifact(
    store: WikiStore,
    source_locator: str,
    page_id: str,
    args: dict[str, object],
) -> None:
    draft = {
        "source_record_text": args["source_record_text"],
        "claim_bullets": args["claim_bullets"],
    }
    store.write_source_summary_draft_artifact(
        source_locator,
        f"write-{page_id}",
        json.dumps(draft, indent=2, ensure_ascii=False, sort_keys=True),
    )


def _citation_for(page_id: str) -> str:
    if page_id == "functions":
        return "raw/book.pdf p.1-10"
    if page_id == "closures":
        return "raw/book.pdf p.11-20"
    return "raw/book.pdf"


def _source_claim_ids_for(page_id: str) -> tuple[str, ...]:
    if page_id == "functions":
        return ("source-claim-unit-0001-0001",)
    if page_id == "closures":
        return ("source-claim-unit-0002-0001",)
    return ("source-claim-unit-0001-0001", "source-claim-unit-0002-0001")


def _book_write_for_one_chunk() -> ToolCall:
    args = _source_summary_write_args(
        "book",
        claim_ids=("source-claim-unit-0001-0001",),
    )
    args["summary"] = "Book hub."
    return ToolCall(
        tool="write_page",
        args=args,
    )


def _map_turns(page_id: str, note: str) -> list[list[ToolCall]]:
    return [
        [ToolCall(tool="search_wiki", args={"query": page_id})],
        [_plan_page_call(page_id)],
        [_write_page_call(page_id)],
        [ToolCall(tool="finish_chunk", args={"report": note})],
    ]


async def test_plain_pdf_ingest_requeues_done_chunks_with_missing_pages(
    store: WikiStore, paths: WikiPaths
) -> None:
    (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
    extraction = _extraction_with_stale_done_chunk(paths)
    script = (
        _map_turns("functions", "rewritten functions")
        + _map_turns("closures", "written closures")
        + [
            [_plan_page_call("book")],
            [_write_page_call("book")],
            [ToolCall(tool="finish_ingest", args={"report": "hub written"})],
        ]
    )
    session = Session(
        store=store,
        client=FakeClient(script),
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        today=TODAY,
        runs_dir=paths.root / "runs",
        run_id="pdf-stale-resume-test",
        extract_pdf=lambda _pdf, _rel, _reextract: extraction,
    )

    await session.ingest("book.pdf")

    saved = from_json((extraction.cache_dir / "manifest.json").read_text(encoding="utf-8"))
    assert saved.integrated
    assert saved.chunks[0].notes == "rewritten functions"
    assert saved.chunks[0].pages_written == ("functions",)
    assert {"functions", "closures", "book"} <= set(store.list_pages())


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


async def test_pdf_chunk_without_successful_write_is_not_marked_done(
    store: WikiStore, paths: WikiPaths
) -> None:
    (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
    extraction = _one_chunk_extraction(paths)
    script = [
        [ToolCall(tool="search_wiki", args={"query": "functions"})],
        [_plan_page_call("functions")],
        [
            ToolCall(
                tool="write_page",
                args={
                    "page_id": "side-topic",
                    "page_kind": "concept",
                    "summary": "Side topic.",
                    "page_body": "Body.",
                },
            )
        ],
        [ToolCall(tool="finish_chunk", args={"report": "claimed done"})],
    ]
    session = Session(
        store=store,
        client=FakeClient(script),
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        today=TODAY,
        runs_dir=paths.root / "runs",
        run_id="pdf-no-write-test",
        extract_pdf=lambda _pdf, _rel, _reextract: extraction,
    )

    with pytest.raises(PdfError, match="successful page write"):
        await session.ingest("book.pdf")

    assert store.list_pages() == []


async def test_pending_pdf_chunk_rewrites_existing_source_summary_page(
    store: WikiStore, paths: WikiPaths
) -> None:
    (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
    args = _source_summary_write_args("functions")
    store.write_page(
        WikiPage.from_metadata(
            PageMetadata(page_id="functions", page_kind="source", summary="Existing functions."),
            _source_summary_body(args),
        )
    )
    _write_source_summary_artifact(store, "book.pdf", "functions", args)
    extraction = _one_chunk_extraction(paths)
    script = [
        [ToolCall(tool="search_wiki", args={"query": "functions"})],
        [_plan_page_call("functions", action="enrich")],
        [ToolCall(tool="read_page", args={"page_id": "functions"})],
        [_write_page_call("functions")],
        [ToolCall(tool="finish_chunk", args={"report": "rewritten functions"})],
        [_plan_page_call("book")],
        [_book_write_for_one_chunk()],
        [ToolCall(tool="finish_ingest", args={"report": "hub written"})],
    ]
    session = Session(
        store=store,
        client=FakeClient(script),
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        today=TODAY,
        runs_dir=paths.root / "runs",
        run_id="pdf-recover-existing-test",
        extract_pdf=lambda _pdf, _rel, _reextract: extraction,
    )

    await session.ingest("book.pdf")

    saved = from_json((extraction.cache_dir / "manifest.json").read_text(encoding="utf-8"))
    assert saved.all_done
    assert saved.chunks[0].notes == "rewritten functions"
    assert saved.chunks[0].pages_written == ("functions",)


async def test_pending_pdf_chunk_rewrites_stale_source_summary_artifact(
    store: WikiStore, paths: WikiPaths
) -> None:
    (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
    stale_args = _source_summary_write_args("functions", claim_ids=("source-claim-stale",))
    store.write_page(
        WikiPage.from_metadata(
            PageMetadata(page_id="functions", page_kind="source", summary="Stale functions."),
            _source_summary_body(stale_args),
        )
    )
    _write_source_summary_artifact(store, "book.pdf", "functions", stale_args)
    extraction = _one_chunk_extraction(paths)
    script = [
        [ToolCall(tool="search_wiki", args={"query": "functions"})],
        [_plan_page_call("functions", action="enrich")],
        [ToolCall(tool="read_page", args={"page_id": "functions"})],
        [_write_page_call("functions")],
        [ToolCall(tool="finish_chunk", args={"report": "rewritten functions"})],
        [_plan_page_call("book")],
        [_book_write_for_one_chunk()],
        [ToolCall(tool="finish_ingest", args={"report": "hub written"})],
    ]
    session = Session(
        store=store,
        client=FakeClient(script),
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        today=TODAY,
        runs_dir=paths.root / "runs",
        run_id="pdf-stale-artifact-test",
        extract_pdf=lambda _pdf, _rel, _reextract: extraction,
    )

    await session.ingest("book.pdf")

    saved = from_json((extraction.cache_dir / "manifest.json").read_text(encoding="utf-8"))
    assert saved.all_done
    assert saved.chunks[0].notes == "rewritten functions"
    assert "source-claim-stale" not in (
        store.page_plan_artifact_dir("book.pdf")
        / "accepted-source-summaries"
        / "write-functions.json"
    ).read_text(encoding="utf-8")
