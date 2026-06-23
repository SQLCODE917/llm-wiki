"""End-to-end chunked-PDF ingest: real WorkflowRunner + store, fake LLM,
fake extractor. Covers the map loop, resume semantics, digest hand-off,
and the single log entry on completion.
"""

import json

import pytest
from fakes import FakeClient
from forge.context import ContextManager, NoCompact
from forge.core.workflow import ToolCall
from helpers import wiki_page

from llmwiki.config import WikiPaths
from llmwiki.domain.objects import (
    ExtractedUnit,
    PagePlan,
    RawSource,
    SourceBundle,
    SourcePageGroup,
)
from llmwiki.domain.planning import page_plan_to_json
from llmwiki.domain.technical_atom_io import technical_atom_catalog_to_json
from llmwiki.domain.technical_atoms import TechnicalAtomCatalog
from llmwiki.pdf import PdfError
from llmwiki.pdf.manifest import ChunkRecord, Manifest, from_json
from llmwiki.pdf.pipeline import ExtractionResult
from llmwiki.runtime.session import Session, _required_hub_page_map
from llmwiki.store import WikiStore

TODAY = "2026-06-11"
BOOK_HUB = "book"
FUNCTIONS_PAGE = "book-functions"
CLOSURES_PAGE = "book-closures"


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


def test_required_hub_page_map_dedupes_source_page_groups() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    plan = PagePlan(
        plan_id="plan-book",
        source_bundle=SourceBundle.one(raw_source),
        extracted_units=(),
        source_claims=(),
        source_claim_groups=(),
        candidate_claims=(),
        candidate_topics=(),
        candidate_entities=(),
        topic_clusters=(),
        wiki_matches=(),
        claim_comparisons=(),
        planned_writes=(),
        source_page_groups=(
            _source_page_group(raw_source, "book-summary", "Summary", "unit-0001"),
            _source_page_group(raw_source, "book-summary", "Summary", "unit-0002"),
            _source_page_group(raw_source, BOOK_HUB, "Hub", "unit-0003"),
            _source_page_group(raw_source, FUNCTIONS_PAGE, "Functions", "unit-0004"),
        ),
    )
    manifest = Manifest(source="book.pdf", sha256="deadbeef" * 8, chunks=())

    targets, entries = _required_hub_page_map(plan, manifest, BOOK_HUB)

    assert targets == ("book-summary", FUNCTIONS_PAGE)
    assert entries == (("book-summary", "Summary"), (FUNCTIONS_PAGE, "Functions"))


def _source_page_group(
    raw_source: RawSource, page_id: str, heading: str, unit_id: str
) -> SourcePageGroup:
    return SourcePageGroup(
        source_page_group_id=f"source-page-group-{unit_id}-{unit_id}",
        raw_source=raw_source,
        page_id=page_id,
        extracted_units=(unit_id,),
        first_heading=heading,
        last_heading=heading,
        first_locator="p.1",
        last_locator="p.1",
        token_estimate=20,
    )


def _write_page_call(name: str) -> ToolCall:
    content = "The source page summarizes this PDF stage."
    if name == BOOK_HUB:
        content = f"Hub links [[{FUNCTIONS_PAGE}]] and [[{CLOSURES_PAGE}]]."
    return ToolCall(
        tool="write_page",
        args=_source_summary_write_args(name, claim_text=content),
    )


def _source_summary_write_args(
    name: str,
    *,
    claim_text: str,
    record_text: str | None = None,
) -> dict[str, object]:
    citation = _citation_for(name)
    claim_ids = _source_claim_ids_for(name)
    bullets = [
        {
            "bullet_text": f"{claim_text} ({citation})",
            "covered_source_claims": list(claim_ids),
        },
        {
            "bullet_text": f"The draft keeps the selected source coverage visible. ({citation})",
            "covered_source_claims": [claim_ids[0]],
        },
        {
            "bullet_text": f"The source summary remains concise and cited. ({citation})",
            "covered_source_claims": [claim_ids[-1]],
        },
    ]
    return {
        "page_id": name,
        "page_kind": "source",
        "summary": f"About {name}.",
        "source_record_text": f"{record_text or f'Source record for [[{name}]].'} ({citation})",
        "claim_bullets": bullets,
        "sources": ["book.pdf"],
    }


def _citation_for(name: str) -> str:
    if name == FUNCTIONS_PAGE:
        return "raw/book.pdf p.1-10"
    if name == CLOSURES_PAGE:
        return "raw/book.pdf p.11-20"
    return "raw/book.pdf"


def _source_claim_ids_for(name: str) -> tuple[str, ...]:
    if name == FUNCTIONS_PAGE:
        return ("source-claim-unit-0001-0001",)
    if name == CLOSURES_PAGE:
        return ("source-claim-unit-0002-0001",)
    return ("source-claim-unit-0001-0001", "source-claim-unit-0002-0001")


def _plan_page_call(name: str, gaps: list[dict[str, str]] | None = None) -> ToolCall:
    return ToolCall(
        tool="plan_pages",
        args={
            "planned_pages": [
                {
                    "metadata": {
                        "page_id": name,
                        "page_kind": "source",
                        "summary": f"About {name}.",
                        "sources": ["book.pdf"],
                    },
                    "role": "source page for this PDF ingest stage",
                    "action": "create",
                    "source_scope": "book.pdf",
                    "confidence": "high",
                    "rationale": f"{name} is the durable page for this PDF ingest stage.",
                }
            ],
            "gaps": gaps or [],
        },
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


def _map_turns(page: str, note: str, gaps: list[dict[str, str]] | None = None) -> list:
    return [
        [ToolCall(tool="search_wiki", args={"query": page})],
        [_plan_page_call(page, gaps=gaps)],
        [_write_page_call(page)],
        [ToolCall(tool="finish_chunk", args={"report": note})],
    ]


def _integrate_turns(
    *,
    claim_text: str = f"Hub links [[{FUNCTIONS_PAGE}]] and [[{CLOSURES_PAGE}]].",
) -> list:
    return [
        [_plan_page_call(BOOK_HUB)],
        [
            ToolCall(
                tool="write_page",
                args=_source_summary_write_args(BOOK_HUB, claim_text=claim_text),
            )
        ],
        [ToolCall(tool="finish_ingest", args={"report": "Hub linked to 2 chapter pages."})],
    ]


_INTEGRATE_TURNS = _integrate_turns()


class TestPdfIngest:
    def test_partial_resume_reuses_matching_persisted_page_plan(
        self, store: WikiStore, paths: WikiPaths, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths, statuses=("done", "pending"))
        session = _session(store, [], paths, extraction)
        raw_source = RawSource.from_locator("book.pdf")
        plan = PagePlan(
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
        store.write_page_plan_artifacts("book.pdf", page_plan_to_json(plan), "persisted")

        def fail_build_page_plan(**_kwargs: object) -> PagePlan:
            raise AssertionError("partial resume should reuse the persisted PagePlan")

        monkeypatch.setattr("llmwiki.runtime.session.build_page_plan", fail_build_page_plan)

        loaded = session._pdf_page_plan(session._ingest_run("book.pdf"), "book.pdf", extraction)

        assert loaded == plan

    async def test_full_map_then_integrate(self, store: WikiStore, paths: WikiPaths) -> None:
        # The PDF must exist for source_locator resolution in the real flow; the
        # fake extractor ignores it but Session resolves the raw path first.
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths)
        script = (
            _map_turns(FUNCTIONS_PAGE, "noted functions")
            + _map_turns(CLOSURES_PAGE, "noted closures")
            + _INTEGRATE_TURNS
        )
        session = _session(store, script, paths, extraction)
        result = await session.ingest("book.pdf")

        assert result.output == "Hub linked to 2 chapter pages."
        # Both map chunks wrote pages; integrate wrote the hub.
        assert {FUNCTIONS_PAGE, CLOSURES_PAGE, BOOK_HUB} <= set(store.list_pages())
        # Manifest on disk: all done + integrated, notes captured.
        saved = from_json((extraction.cache_dir / "manifest.json").read_text(encoding="utf-8"))
        assert saved.all_done and saved.integrated
        assert saved.chunks[0].notes == "noted functions"
        assert saved.chunks[0].route_plan_pages == 1
        assert saved.chunks[0].route_plan_gaps == 0
        # One log entry for the whole ingest.
        log = paths.log_path.read_text(encoding="utf-8")
        assert log.count("ingest | book.pdf") == 1
        # Supervision notes streamed per chunk.
        assert len(session._notes_seen) == 2  # type: ignore[attr-defined]
        assert "[chunk 1/2]" in session._notes_seen[0]  # type: ignore[attr-defined]

    async def test_resume_skips_done_chunks(self, store: WikiStore, paths: WikiPaths) -> None:
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths, statuses=("done", "pending"))
        script = _map_turns(CLOSURES_PAGE, "resumed fine") + _INTEGRATE_TURNS
        session = _session(store, script, paths, extraction)
        result = await session.ingest("book.pdf")

        assert result.output == "Hub linked to 2 chapter pages."
        saved = from_json((extraction.cache_dir / "manifest.json").read_text(encoding="utf-8"))
        assert saved.all_done and saved.integrated
        # Chunk 1's pre-existing notes survived; only chunk 2 ran.
        assert saved.chunks[0].notes == "done already"
        assert saved.chunks[1].notes == "resumed fine"

    async def test_page_map_reaches_integrate_run(self, store: WikiStore, paths: WikiPaths) -> None:
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths)
        script = (
            _map_turns(FUNCTIONS_PAGE, "claims about functions")
            + _map_turns(CLOSURES_PAGE, "claims about closures")
            + _INTEGRATE_TURNS
        )
        session = _session(store, script, paths, extraction)
        await session.ingest("book.pdf")

        fake: FakeClient = session.client
        integrate_first_turn = fake.sent[-2]  # first integrate request
        user_msgs = [m["content"] for m in integrate_first_turn if m.get("role") == "user"]
        assert any("Machine-recorded chunk page map" in c for c in user_msgs)
        assert any(
            f"[[{FUNCTIONS_PAGE}]]" in c and f"[[{CLOSURES_PAGE}]]" in c
            for c in user_msgs
        )
        assert any("p.1-10" in c for c in user_msgs)

    async def test_chunk_text_and_citation_reach_map_run(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths)
        script = (
            _map_turns(FUNCTIONS_PAGE, "n1")
            + _map_turns(CLOSURES_PAGE, "n2")
            + _INTEGRATE_TURNS
        )
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
            wiki_page(
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
                args=_source_summary_write_args(
                    name,
                    claim_text="Builds on [[iterable]].",
                ),
            )

        script = [
            [ToolCall(tool="search_wiki", args={"query": FUNCTIONS_PAGE})],
            [_plan_page_call(FUNCTIONS_PAGE)],
            [_linked_write(FUNCTIONS_PAGE)],
            [ToolCall(tool="finish_chunk", args={"report": "n1"})],
            [ToolCall(tool="search_wiki", args={"query": CLOSURES_PAGE})],
            [_plan_page_call(CLOSURES_PAGE)],
            [_linked_write(CLOSURES_PAGE)],
            [ToolCall(tool="finish_chunk", args={"report": "n2"})],
            *_integrate_turns(
                claim_text=(
                    f"Hub links [[{FUNCTIONS_PAGE}]], [[{CLOSURES_PAGE}]], "
                    "and [[iterable]]."
                ),
            ),
        ]
        session = _session(store, script, paths, extraction)
        await session.ingest("book.pdf")

        # Machine record landed in the manifest.
        saved = from_json((extraction.cache_dir / "manifest.json").read_text(encoding="utf-8"))
        assert saved.chunks[0].pages_written == (FUNCTIONS_PAGE,)
        assert saved.chunks[1].pages_written == (CLOSURES_PAGE,)
        # The integrate run received the computed salience block with the
        # linked concept ranked in it, plus the per-chunk machine record.
        fake: FakeClient = session.client
        integrate_msgs = [m["content"] for m in fake.sent[-2] if m.get("role") == "user"]
        assert any("Salience report" in c and "[[iterable]] (links 2" in c for c in integrate_msgs)
        assert any("Chunk 1" in c and f"[[{FUNCTIONS_PAGE}]]" in c for c in integrate_msgs)

    async def test_route_plan_gaps_are_recorded_in_manifest(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths)
        gaps = [
            {
                "reason": "too-granular",
                "source_scope": "book.pdf p.1-10",
                "summary": "Minor syntax aside folded into the chapter page.",
            }
        ]
        script = (
            _map_turns(FUNCTIONS_PAGE, "n1", gaps=gaps)
            + _map_turns(CLOSURES_PAGE, "n2")
            + _INTEGRATE_TURNS
        )
        session = _session(store, script, paths, extraction)
        await session.ingest("book.pdf")

        saved = from_json((extraction.cache_dir / "manifest.json").read_text(encoding="utf-8"))
        assert saved.chunks[0].route_plan_pages == 1
        assert saved.chunks[0].route_plan_gaps == 1
        assert saved.chunks[0].route_gap_summaries == (
            "Minor syntax aside folded into the chapter page.",
        )

    async def test_heading_only_chunk_is_deterministic_route_gap(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        cache_dir = paths.cache_dir / "heading-only"
        chunks_dir = cache_dir / "chunks"
        chunks_dir.mkdir(parents=True, exist_ok=True)
        (chunks_dir / "0001.md").write_text("# Title Only", encoding="utf-8")
        (chunks_dir / "0002.md").write_text(
            "Closures capture lexical scope.", encoding="utf-8"
        )
        extraction = ExtractionResult(
            manifest=Manifest(
                source="book.pdf",
                sha256="bead" * 16,
                chunks=(
                    ChunkRecord(1, "Title Only", 1, 1, 8),
                    ChunkRecord(2, "Closures", 11, 20, 20),
                ),
            ),
            cache_dir=cache_dir,
        )
        session = _session(
            store,
            _map_turns(CLOSURES_PAGE, "noted closures") + _INTEGRATE_TURNS,
            paths,
            extraction,
        )

        await session.ingest("book.pdf")

        saved = from_json((cache_dir / "manifest.json").read_text(encoding="utf-8"))
        assert saved.chunks[0].pages_written == ()
        assert saved.chunks[0].route_plan_gaps == 1
        assert saved.chunks[0].route_gap_summaries == (
            "Title Only (pages 1-1): no claim-bearing source-page material.",
        )
        assert saved.chunks[1].pages_written == (CLOSURES_PAGE,)
        fake: FakeClient = session.client
        first_user_messages = [m["content"] for m in fake.sent[0] if m.get("role") == "user"]
        assert any("Ingest chunk 2 of 2" in content for content in first_user_messages)

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
            wiki_page(
                name="iterable",
                category="concept",
                summary="Core protocol.",
                body="Central.",
                sources=("raw/book.pdf",),
                updated=TODAY,
            )
        )
        script = [
            [_plan_page_call("book")],
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_write_args(
                        "book",
                        claim_text="Summary prose for the hub and [[iterable]].",
                        record_text="Summary prose.\n\n**Key entities**: [[matthew-knox]].",
                    ),
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

    async def test_reintegrate_replays_matching_source_summary_artifacts(
        self, store: WikiStore, paths: WikiPaths, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths, statuses=("done", "done"))
        session = _session(store, list(_INTEGRATE_TURNS), paths, extraction)
        plan = session._pdf_page_plan(
            session._ingest_run("book.pdf"),
            "book.pdf",
            extraction,
            reuse_persisted=False,
        )
        write = next(
            item for item in plan.planned_writes if item.page_metadata.page_id == FUNCTIONS_PAGE
        )
        assert write.source_summary_plan is not None
        store.write_page_plan_artifacts("book.pdf", page_plan_to_json(plan), "persisted")
        store.write_technical_atom_catalog_artifact(
            "book.pdf",
            technical_atom_catalog_to_json(
                TechnicalAtomCatalog(
                    catalog_id="catalog-book",
                    source_locator="book.pdf",
                    artifact_fingerprint=plan.plan_id,
                    technical_atoms=(),
                )
            ),
        )
        store.write_source_summary_draft_artifact(
            "book.pdf",
            write.write_id,
            json.dumps(
                {
                    "source_record_text": "Functions refreshed. (raw/book.pdf p.1-10)",
                    "claim_bullets": [
                        {
                            "bullet_text": "Functions are values. (raw/book.pdf p.1-10)",
                            "covered_source_claims": list(
                                write.source_summary_plan.selected_source_claims
                            ),
                        }
                    ],
                }
            ),
        )
        store.write_page(
            wiki_page(
                name=FUNCTIONS_PAGE,
                category="source",
                summary="Stale.",
                body="Old rendered page.",
                sources=("raw/book.pdf p.1-10",),
                updated=TODAY,
            )
        )

        def fail_build_technical_atom_catalog(**_kwargs: object) -> TechnicalAtomCatalog:
            raise AssertionError("reintegrate should reuse a matching TechnicalAtomCatalog")

        def fail_page_plan_to_json(_plan: PagePlan) -> str:
            raise AssertionError("reintegrate should reuse the persisted PagePlan JSON")

        monkeypatch.setattr(
            "llmwiki.runtime.session.build_technical_atom_catalog",
            fail_build_technical_atom_catalog,
        )
        monkeypatch.setattr("llmwiki.runtime.session.page_plan_to_json", fail_page_plan_to_json)

        await session.ingest("book.pdf", reintegrate=True)

        refreshed = store.read_page(FUNCTIONS_PAGE)
        assert "Functions refreshed." in refreshed
        assert "Old rendered page." not in refreshed

    async def test_reintegrate_with_pending_chunks_refuses(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths)  # both pending
        session = _session(store, [], paths, extraction)
        with pytest.raises(PdfError, match="pending"):
            await session.ingest("book.pdf", reintegrate=True)
