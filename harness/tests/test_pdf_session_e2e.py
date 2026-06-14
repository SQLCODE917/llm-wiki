"""End-to-end chunked-PDF ingest: real WorkflowRunner + store, fake LLM,
fake extractor. Covers the map loop, resume semantics, digest hand-off,
and the single log entry on completion.
"""

import pytest
from fakes import FakeClient
from forge.context import ContextManager, NoCompact
from forge.core.workflow import ToolCall

from llmwiki.config import WikiPaths
from llmwiki.domain.pages import WikiPage
from llmwiki.pdf import PdfError
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


def _write_page_call(name: str) -> ToolCall:
    return ToolCall(
        tool="write_page",
        args={"name": name, "category": "source", "summary": f"About {name}.", "content": "Body."},
    )


def _session(
    store: WikiStore, script: list, paths: WikiPaths, extraction: ExtractionResult
) -> Session:
    notes_seen: list[str] = []
    session = Session(
        store=store,
        client=FakeClient(script),
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        today=TODAY,
        runs_dir=paths.root / "runs",
        run_id="pdf-test",
        extract_pdf=lambda pdf, rel, reextract: extraction,
        on_chunk_note=notes_seen.append,
    )
    object.__setattr__(session, "_notes_seen", notes_seen)  # test-side capture
    return session


def _map_turns(page: str, note: str) -> list:
    return [
        [ToolCall(tool="search_wiki", args={"query": page})],
        [_write_page_call(page)],
        [ToolCall(tool="finish_chunk", args={"report": note})],
    ]


_INTEGRATE_TURNS = [
    [_write_page_call("javascriptallonge")],
    [ToolCall(tool="finish_ingest", args={"report": "Hub linked to 2 chapter pages."})],
]


class TestPdfIngest:
    async def test_full_map_then_integrate(self, store: WikiStore, paths: WikiPaths) -> None:
        # The PDF must exist for source_path resolution in the real flow; the
        # fake extractor ignores it but Session resolves the raw path first.
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths)
        script = (
            _map_turns("functions", "noted functions")
            + _map_turns("closures", "noted closures")
            + _INTEGRATE_TURNS
        )
        session = _session(store, script, paths, extraction)
        result = await session.ingest("book.pdf")

        assert result.output == "Hub linked to 2 chapter pages."
        # Both map chunks wrote pages; integrate wrote the hub.
        assert {"functions", "closures", "javascriptallonge"} <= set(store.list_pages())
        # Manifest on disk: all done + integrated, notes captured.
        saved = from_json((extraction.cache_dir / "manifest.json").read_text(encoding="utf-8"))
        assert saved.all_done and saved.integrated
        assert saved.chunks[0].notes == "noted functions"
        # One log entry for the whole ingest.
        log = paths.log_path.read_text(encoding="utf-8")
        assert log.count("ingest | book.pdf") == 1
        # Supervision notes streamed per chunk.
        assert len(session._notes_seen) == 2  # type: ignore[attr-defined]
        assert "[chunk 1/2]" in session._notes_seen[0]  # type: ignore[attr-defined]

    async def test_resume_skips_done_chunks(self, store: WikiStore, paths: WikiPaths) -> None:
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths, statuses=("done", "pending"))
        script = _map_turns("closures", "resumed fine") + _INTEGRATE_TURNS
        session = _session(store, script, paths, extraction)
        result = await session.ingest("book.pdf")

        assert result.output == "Hub linked to 2 chapter pages."
        saved = from_json((extraction.cache_dir / "manifest.json").read_text(encoding="utf-8"))
        assert saved.all_done and saved.integrated
        # Chunk 1's pre-existing notes survived; only chunk 2 ran.
        assert saved.chunks[0].notes == "done already"
        assert saved.chunks[1].notes == "resumed fine"

    async def test_digest_reaches_integrate_run(self, store: WikiStore, paths: WikiPaths) -> None:
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths)
        script = (
            _map_turns("functions", "claims about functions")
            + _map_turns("closures", "claims about closures")
            + _INTEGRATE_TURNS
        )
        session = _session(store, script, paths, extraction)
        await session.ingest("book.pdf")

        fake: FakeClient = session.client
        integrate_first_turn = fake.sent[-2]  # first integrate request
        user_msgs = [m["content"] for m in integrate_first_turn if m.get("role") == "user"]
        assert any(
            "claims about functions" in c and "claims about closures" in c for c in user_msgs
        )
        assert any("p.1-10" in c for c in user_msgs)

    async def test_chunk_text_and_citation_reach_map_run(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths)
        script = _map_turns("functions", "n1") + _map_turns("closures", "n2") + _INTEGRATE_TURNS
        session = _session(store, script, paths, extraction)
        await session.ingest("book.pdf")

        fake: FakeClient = session.client
        first_map_turn = fake.sent[0]
        user_msgs = [m["content"] for m in first_map_turn if m.get("role") == "user"]
        assert any("functions are values" in c for c in user_msgs)
        assert any("(raw/book.pdf p.1-10)" in c for c in user_msgs)

    async def test_writes_recorded_and_salience_reaches_integrate(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        # A pre-existing concept page that both chunk pages link to — it must
        # appear ranked in the computed salience block handed to integrate.
        store.write_page(
            WikiPage(
                name="iterable",
                category="concept",
                summary="Core protocol.",
                body="Central concept.",
                sources=("raw/book.pdf",),  # in scope for the book's salience
                updated=TODAY,
            )
        )
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths)

        def _linked_write(name: str) -> ToolCall:
            return ToolCall(
                tool="write_page",
                args={
                    "name": name,
                    "category": "source",
                    "summary": f"About {name}.",
                    "content": "Builds on [[iterable]].",
                    "sources": ["raw/book.pdf"],
                },
            )

        script = [
            [ToolCall(tool="search_wiki", args={"query": "functions"})],
            [_linked_write("functions")],
            [ToolCall(tool="finish_chunk", args={"report": "n1"})],
            [ToolCall(tool="search_wiki", args={"query": "closures"})],
            [_linked_write("closures")],
            [ToolCall(tool="finish_chunk", args={"report": "n2"})],
            *_INTEGRATE_TURNS,
        ]
        session = _session(store, script, paths, extraction)
        await session.ingest("book.pdf")

        # Machine record landed in the manifest.
        saved = from_json((extraction.cache_dir / "manifest.json").read_text(encoding="utf-8"))
        assert saved.chunks[0].pages_written == ("functions",)
        assert saved.chunks[1].pages_written == ("closures",)
        # The integrate run received the computed salience block with the
        # linked concept ranked in it, plus the per-chunk machine record.
        fake: FakeClient = session.client
        integrate_msgs = [m["content"] for m in fake.sent[-2] if m.get("role") == "user"]
        assert any("Salience report" in c and "[[iterable]] (links 2" in c for c in integrate_msgs)
        assert any("Pages written (recorded): [[functions]]" in c for c in integrate_msgs)

    async def test_hub_key_lists_reconciled_after_integrate(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        # The model writes the hub WITH its own (merged, stale) key lists;
        # the harness must replace them with computed ones post-run.
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths, statuses=("done", "done"))
        chunks_dir = extraction.cache_dir / "chunks"
        (chunks_dir / "0001.md").write_text("iterable " * 12, encoding="utf-8")
        store.write_page(
            WikiPage(
                name="iterable",
                category="concept",
                summary="Core protocol.",
                body="Central.",
                sources=("raw/book.pdf",),
                updated=TODAY,
            )
        )
        script = [
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "name": "book",  # slugify('book.pdf'.stem) == the hub
                        "category": "source",
                        "summary": "Hub.",
                        "content": "Summary prose.\n\n**Key entities**: [[matthew-knox]].",
                        "sources": ["raw/book.pdf"],
                    },
                )
            ],
            [ToolCall(tool="finish_ingest", args={"report": "hub written"})],
        ]
        session = _session(store, script, paths, extraction)
        await session.ingest("book.pdf", reintegrate=True)

        hub_text = store.read_page("book")
        assert "Summary prose." in hub_text
        assert "matthew-knox" not in hub_text  # model's stale list replaced
        assert "**Key concepts:** [[iterable]]" in hub_text

    async def test_reintegrate_runs_integrate_only(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths, statuses=("done", "done"))
        session = _session(store, list(_INTEGRATE_TURNS), paths, extraction)
        result = await session.ingest("book.pdf", reintegrate=True)
        assert result.output == "Hub linked to 2 chapter pages."
        assert "ingest | book.pdf" in paths.log_path.read_text(encoding="utf-8")

    async def test_reintegrate_with_pending_chunks_refuses(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths)  # both pending
        session = _session(store, [], paths, extraction)
        with pytest.raises(PdfError, match="pending"):
            await session.ingest("book.pdf", reintegrate=True)
