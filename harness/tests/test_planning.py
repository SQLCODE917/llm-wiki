"""Tests for global ingest planning."""

from fakes import FakeClient
from forge.context import ContextManager, NoCompact
from forge.core.workflow import ToolCall

from llmwiki.config import WikiPaths
from llmwiki.domain.objects import RawSource, SourceBundle
from llmwiki.domain.pages import (
    LOCAL_FLAT_STRUCTURE,
    PageMetadata,
    PathTemplate,
    WikiPage,
    WikiStructure,
    render_page,
)
from llmwiki.domain.planning import (
    build_markdown_page_plan,
    build_page_plan,
    observation_report,
    page_plan_to_json,
)
from llmwiki.domain.planning_analysis import build_extracted_unit
from llmwiki.pdf.manifest import ChunkRecord, Manifest
from llmwiki.pdf.pipeline import ExtractionResult
from llmwiki.runtime.session import Session
from llmwiki.store import WikiStore

TODAY = "2026-06-19"


def _page(page_id: str, page_body: str, page_kind: str = "source") -> str:
    return render_page(
        WikiPage.from_metadata(
            PageMetadata(page_id=page_id, page_kind=page_kind, summary=f"About {page_id}."),
            page_body,
        )
    )


def test_markdown_page_plan_creates_units_claims_writes_and_paths() -> None:
    raw_source = RawSource.from_locator("antikythera-mechanism.md")
    plan = build_markdown_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        source_text="# The Antikythera Mechanism\n\nThe device may predict eclipses.",
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
    )

    assert plan.extracted_units[0].source_hash
    assert plan.candidate_claims[0].evidence.raw_source == raw_source
    assert [write.page_metadata.page_id for write in plan.planned_writes] == [
        "antikythera-mechanism"
    ]
    assert all(write.evidence for write in plan.planned_writes)
    assert '"source_hash"' in page_plan_to_json(plan)
    report = observation_report(plan)
    assert "ExtractedUnits: 1" in report
    assert "`antikythera-mechanism.md`" in report


def test_existing_page_match_enriches_existing_page() -> None:
    raw_source = RawSource.from_locator("closures.pdf")
    unit = build_extracted_unit(
        unit_id="unit-0001",
        raw_source=raw_source,
        locator="p.1-2",
        heading_path="Closure",
        text="Closures capture lexical scope and preserve variables.",
    )

    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=(unit,),
        existing_pages={"closure": _page("closure", "A closure captures lexical scope.")},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
    )

    write = plan.planned_writes[0]
    assert write.page_metadata.page_id == "closure"
    assert write.action == "enrich-existing"
    assert plan.wiki_matches[0].page_id == "closure"


def test_source_section_identity_beats_semantic_similarity() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    unit = build_extracted_unit(
        unit_id="unit-0001",
        raw_source=raw_source,
        locator="p.109-125",
        heading_path="Self-Similarity",
        text="Recursive list mapping, folding, copy-on-write, and linked list examples.",
    )
    existing_pages = {
        "book-copy-on-write": _page(
            "book-copy-on-write",
            "copy-on-write linked list mapping folding recursion",
        ),
        "book-self-similarity": _page(
            "book-self-similarity",
            "recursive lists and self-similar data",
        ),
    }

    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=(unit,),
        existing_pages=existing_pages,
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
    )

    assert plan.planned_writes[0].page_metadata.page_id == "book-self-similarity"
    assert all(
        write.page_metadata.page_id != "book-copy-on-write"
        or "unit-0001" not in write.extracted_units
        for write in plan.planned_writes
    )


def test_nested_wiki_structure_projects_from_page_metadata() -> None:
    raw_source = RawSource.from_locator("antikythera-mechanism.md")
    nested = WikiStructure(
        structure_id="nested",
        default_path_template=PathTemplate(
            template_text="{PageKind}/{PageId}.md",
            required_page_metadata_fields=("PageKind", "PageId"),
        ),
    )

    plan = build_markdown_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        source_text="# The Antikythera Mechanism\n\nThe device may predict eclipses.",
        existing_pages={},
        wiki_structure=nested,
        today=TODAY,
    )

    paths = [write.projection.page_path for write in plan.planned_writes if write.projection]
    assert paths == ["source/antikythera-mechanism.md"]


class PagePlanSpyStore(WikiStore):
    def __init__(self, paths: WikiPaths) -> None:
        super().__init__(paths)
        self.write_checks: list[str] = []

    def write_page(self, page: WikiPage) -> None:
        plan_path = self.page_plan_artifact_dir("book.pdf") / "page-plan.json"
        assert plan_path.exists()
        self.write_checks.append(page.page_id)
        super().write_page(page)


def _fake_extraction(paths: WikiPaths) -> ExtractionResult:
    cache_dir = paths.cache_dir / "deadbeef"
    chunks_dir = cache_dir / "chunks"
    chunks_dir.mkdir(parents=True, exist_ok=True)
    (chunks_dir / "0001.md").write_text("Chunk one: functions are values.", encoding="utf-8")
    (chunks_dir / "0002.md").write_text("Chunk two: closures capture scope.", encoding="utf-8")
    manifest = Manifest(
        source="book.pdf",
        sha256="deadbeef" * 8,
        chunks=(
            ChunkRecord(1, "Functions", 1, 10, 4000),
            ChunkRecord(2, "Closures", 11, 20, 3800),
        ),
    )
    return ExtractionResult(manifest=manifest, cache_dir=cache_dir)


def _plan_page_call(page_id: str) -> ToolCall:
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
                    "action": "create",
                    "source_scope": "book.pdf",
                    "confidence": "high",
                    "rationale": f"{page_id} is the durable page for this PDF ingest stage.",
                }
            ],
            "gaps": [],
        },
    )


def _write_page_call(page_id: str) -> ToolCall:
    return ToolCall(
        tool="write_page",
        args={
            "page_id": page_id,
            "page_kind": "source",
            "summary": f"About {page_id}.",
            "page_body": "Hub links [[functions]] and [[closures]]."
            if page_id == "book"
            else "Body.",
        },
    )


def _turns(page_id: str, finish_tool: str, report: str) -> list[list[ToolCall]]:
    calls = [[_plan_page_call(page_id)], [_write_page_call(page_id)]]
    if finish_tool == "finish_chunk":
        return [
            [ToolCall(tool="search_wiki", args={"query": page_id})],
            *calls,
            [ToolCall(tool=finish_tool, args={"report": report})],
        ]
    return [*calls, [ToolCall(tool=finish_tool, args={"report": report})]]


async def test_fake_pdf_ingest_persists_page_plan_before_writes(paths: WikiPaths) -> None:
    (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
    store = PagePlanSpyStore(paths)
    extraction = _fake_extraction(paths)
    script = (
        _turns("functions", "finish_chunk", "noted functions")
        + _turns("closures", "finish_chunk", "noted closures")
        + _turns("book", "finish_ingest", "hub written")
    )
    session = Session(
        store=store,
        client=FakeClient(script),
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        today=TODAY,
        runs_dir=paths.root / "runs",
        run_id="pdf-test",
        extract_pdf=lambda _pdf, _locator, _reextract: extraction,
    )

    await session.ingest("book.pdf")

    assert store.write_checks == ["functions", "closures", "book"]
    plan_json = (store.page_plan_artifact_dir("book.pdf") / "page-plan.json").read_text(
        encoding="utf-8"
    )
    assert '"planned_writes"' in plan_json
