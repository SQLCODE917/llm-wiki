"""Tests for global ingest planning."""

from fakes import FakeClient
from forge.context import ContextManager, NoCompact
from forge.core.workflow import ToolCall

from llmwiki.config import WikiPaths
from llmwiki.domain.objects import Evidence, RawSource, SourceBundle, SourceClaim
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
from llmwiki.domain.planning_analysis import (
    build_extracted_unit,
    candidate_claims,
    cosine,
    embedding,
    same_section_identity,
)
from llmwiki.domain.source_map import normalized_source_map_to_json
from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.manifest import ChunkRecord, Manifest
from llmwiki.pdf.pipeline import ExtractionResult, source_map_file
from llmwiki.pdf.source_map_builder import build_normalized_source_map
from llmwiki.runtime.session import Session
from llmwiki.store import WikiStore

TODAY = "2026-06-19"
BOOK_HUB = "book"
FUNCTIONS_PAGE = "book-functions"
CLOSURES_PAGE = "book-closures"


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
    assert plan.source_claims[0].evidence.raw_source == raw_source
    assert plan.source_claim_groups
    assert plan.topic_clusters[0].source_claim_groups
    assert [write.page_metadata.page_id for write in plan.planned_writes] == [
        "antikythera-mechanism"
    ]
    assert plan.planned_writes[0].source_summary_plan is not None
    assert all(write.evidence for write in plan.planned_writes)
    assert '"source_hash"' in page_plan_to_json(plan)
    assert '"source_claims"' in page_plan_to_json(plan)
    assert '"source_summary_plan"' in page_plan_to_json(plan)
    report = observation_report(plan)
    assert "ExtractedUnits: 1" in report
    assert "SourceClaims: 1" in report
    assert "SourceClaimGroups: 1" in report
    assert "SourceSummaryPlan selected claim IDs" in report
    assert "`antikythera-mechanism.md`" in report
    assert "PageKind `source`" in report
    assert "plan_pages action `create`" in report
    assert "PagePlan action `create-new`" in report
    assert "claim_id `source-claim-unit-0001-0001`" in report
    assert "cue_terms `" in report
    assert "The device may predict eclipses." not in report
    assert "span `" not in report
    assert "source-summary-plan-antikythera-mechanism" not in report


def test_pdf_page_plan_can_prefix_new_chunk_pages() -> None:
    raw_source = RawSource.from_locator("Sword World RPG - Complete Edition.pdf")
    unit = build_extracted_unit(
        unit_id="unit-0001",
        raw_source=raw_source,
        locator="p.1-7",
        heading_path="Front matter",
        text="The rulebook introduces Sword World RPG.",
    )

    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=(unit,),
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
        new_page_prefix="sword-world-rpg-complete-edition",
    )

    assert [write.page_metadata.page_id for write in plan.planned_writes] == [
        "sword-world-rpg-complete-edition-front-matter",
        "sword-world-rpg-complete-edition",
    ]
    assert plan.planned_writes[0].source_summary_plan is not None
    assert plan.planned_writes[1].source_summary_plan is None


def test_observation_report_scopes_repeated_page_id_by_write_id() -> None:
    raw_source = RawSource.from_locator("javascriptallonge.pdf")
    early = build_extracted_unit(
        unit_id="unit-0065",
        raw_source=raw_source,
        locator="p.72-73",
        heading_path="Partial Application",
        text="Another basic building block is partial application.",
    )
    later = build_extracted_unit(
        unit_id="unit-0073",
        raw_source=raw_source,
        locator="p.80-81",
        heading_path="Partial Application",
        text="Many libraries provide some form of partial application.",
    )
    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=(early, later),
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
        new_page_prefix="javascriptallonge",
    )

    writes = tuple(
        write
        for write in plan.planned_writes
        if write.page_metadata.page_id == "javascriptallonge-partial-application"
    )
    report = observation_report(
        plan,
        target_page_ids=("javascriptallonge-partial-application",),
        target_write_ids=(writes[1].write_id,),
    )

    assert len(writes) == 2
    assert len({write.write_id for write in writes}) == 2
    assert "raw/javascriptallonge.pdf p.80-81" in report
    assert "source-claim-unit-0073" in report
    assert "raw/javascriptallonge.pdf p.72-73" not in report
    assert "source-claim-unit-0065" not in report


def test_prefixed_pdf_page_plan_ignores_existing_generic_section_page() -> None:
    raw_source = RawSource.from_locator("javascriptallonge.pdf")
    unit = build_extracted_unit(
        unit_id="unit-0001",
        raw_source=raw_source,
        locator="p.1-13",
        heading_path="Front matter",
        text="JavaScript Allonge introduces functions and closures.",
    )

    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=(unit,),
        existing_pages={
            "front-matter": _page("front-matter", "A generic front matter page."),
            "sword-world-rpg-complete-edition-front-matter": _page(
                "sword-world-rpg-complete-edition-front-matter",
                "A different PDF source page.",
            ),
        },
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
        new_page_prefix="javascriptallonge",
    )

    write = plan.planned_writes[0]
    assert write.page_metadata.page_id == "javascriptallonge-front-matter"
    assert write.action == "create-new"


def test_prefixed_pdf_page_plan_does_not_match_source_prefix_terms() -> None:
    raw_source = RawSource.from_locator("Sword World RPG - Complete Edition.pdf")
    unit = build_extracted_unit(
        unit_id="unit-0058",
        raw_source=raw_source,
        locator="p.241-242",
        heading_path="14.1 Treasure and Rewards in Sword World",
        text="Adventurers may recover treasure and rewards from ancient ruins.",
    )

    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=(unit,),
        existing_pages={
            "sword-world-rpg-complete-edition-1-3-skills": _page(
                "sword-world-rpg-complete-edition-1-3-skills",
                "Skills in Sword World RPG.",
            )
        },
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
        new_page_prefix="sword-world-rpg-complete-edition",
    )

    unit_write = plan.planned_writes[0]
    assert unit_write.page_metadata.page_id == (
        "sword-world-rpg-complete-edition-14-1-treasure-and-rewards-in-sword-world"
    )
    assert unit_write.action == "create-new"


def test_large_pdf_page_plan_groups_adjacent_source_units() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    units = tuple(
        build_extracted_unit(
            unit_id=f"unit-{index:04d}",
            raw_source=raw_source,
            locator=f"p.{index}",
            heading_path=f"1.{index} Topic {index}",
            text=f"Topic {index} explains a related chapter one rule.",
        )
        for index in range(1, 42)
    )

    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=units,
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
    )

    grouped = next(group for group in plan.source_page_groups if len(group.extracted_units) > 1)
    grouped_write = next(
        write for write in plan.planned_writes if write.page_metadata.page_id == grouped.page_id
    )
    assert grouped.page_id.startswith("book-1-1-topic-1-through-1-5-topic-5")
    assert grouped.extracted_units == tuple(f"unit-{index:04d}" for index in range(1, 6))
    assert grouped_write.page_metadata.sources == tuple(
        f"raw/book.pdf p.{index}" for index in range(1, 6)
    )
    assert '"source_page_groups"' in page_plan_to_json(plan)


def test_pdf_page_plan_skips_heading_only_source_units() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    heading_only = build_extracted_unit(
        unit_id="unit-0001",
        raw_source=raw_source,
        locator="p.1",
        heading_path="Programming from Functions to Classes",
        text="# Programming from Functions to Classes",
    )
    claim_units = tuple(
        build_extracted_unit(
            unit_id=f"unit-{index:04d}",
            raw_source=raw_source,
            locator=f"p.{index}",
            heading_path=f"1.{index} Topic {index}",
            text=f"Topic {index} explains a related rule.",
        )
        for index in range(2, 43)
    )

    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=(heading_only, *claim_units),
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
    )

    grouped_unit_ids = {
        unit_id for group in plan.source_page_groups for unit_id in group.extracted_units
    }
    non_hub_writes = [
        write for write in plan.planned_writes if write.page_metadata.page_id != BOOK_HUB
    ]
    assert "unit-0001" not in grouped_unit_ids
    assert all("unit-0001" not in write.extracted_units for write in non_hub_writes)


def test_large_pdf_existing_default_source_page_stays_one_unit() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    units = tuple(
        build_extracted_unit(
            unit_id=f"unit-{index:04d}",
            raw_source=raw_source,
            locator=f"p.{index}",
            heading_path=f"1.{index} Topic {index}",
            text=f"Topic {index} explains a related chapter one rule.",
        )
        for index in range(1, 42)
    )

    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=units,
        existing_pages={"book-1-37-topic-37": _page("book-1-37-topic-37", "Existing.")},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
    )

    write = next(
        write
        for write in plan.planned_writes
        if write.page_metadata.page_id == "book-1-37-topic-37"
    )
    assert write.action == "enrich-existing"
    assert write.extracted_units == ("unit-0037",)
    assert not any(
        "unit-0037" in group.extracted_units and group.page_id != "book-1-37-topic-37"
        for group in plan.source_page_groups
    )


def test_large_pdf_page_groups_split_on_top_level_heading() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    units = tuple(
        build_extracted_unit(
            unit_id=f"unit-{index:04d}",
            raw_source=raw_source,
            locator=f"p.{index}",
            heading_path=(
                f"1.{index} Chapter One Topic" if index <= 21 else f"2.{index} Chapter Two Topic"
            ),
            text=f"Topic {index} explains a rule.",
        )
        for index in range(1, 43)
    )

    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=units,
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
    )

    assert all(
        group.first_heading.split(".", 1)[0] == group.last_heading.split(".", 1)[0]
        for group in plan.source_page_groups
    )


def test_section_identity_uses_slug_identity_not_shared_terms() -> None:
    assert same_section_identity("Self-Similarity", "book-self-similarity")
    assert not same_section_identity(
        "1.4 Character Creation (part 2)",
        "sword-world-rpg-complete-edition-1-4-character-creation-part-1",
    )
    assert not same_section_identity(
        "14.1 Treasure and Rewards in Sword World",
        "sword-world-rpg-complete-edition-books-related-to-sword-world-rpg",
    )
    assert not same_section_identity("[", "book-create-undead")


def test_embedding_handles_long_text_with_bounded_norm() -> None:
    vector = embedding("alpha beta gamma " * 10000)

    assert set(vector) == {"alpha", "beta", "gamma"}
    assert 0.99 < sum(value * value for value in vector.values()) < 1.01


def test_observation_report_can_scope_planned_targets() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    functions = build_extracted_unit(
        unit_id="unit-0001",
        raw_source=raw_source,
        locator="p.1-10",
        heading_path="Functions",
        text="Functions are values.",
    )
    closures = build_extracted_unit(
        unit_id="unit-0002",
        raw_source=raw_source,
        locator="p.11-20",
        heading_path="Closures",
        text="Closures capture lexical scope.",
    )
    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=(functions, closures),
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
    )

    report = observation_report(plan, target_page_ids=("book-functions",))

    assert "Planned page targets shown: 1 of 3" in report
    assert "`book-functions`" in report
    assert "`book-closures`" not in report
    assert "`book`" not in report


def test_generic_existing_page_does_not_capture_source_section_page() -> None:
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
    assert write.page_metadata.page_id == "closures-closure"
    assert write.action == "create-new"
    assert plan.wiki_matches[0].page_id == "closure"


def test_existing_source_specific_page_match_enriches_existing_page() -> None:
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
        existing_pages={
            "closures-closure": _page(
                "closures-closure",
                "A source page about closure.",
            )
        },
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
    )

    write = plan.planned_writes[0]
    assert write.page_metadata.page_id == "closures-closure"
    assert write.action == "enrich-existing"


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


def test_candidate_claims_bounds_long_unpunctuated_units() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    unit = build_extracted_unit(
        unit_id="unit-0001",
        raw_source=raw_source,
        locator="p.1",
        heading_path="Long text",
        text="Functions return values. " + ("unpunctuated source text " * 5000),
    )

    claims = candidate_claims((unit,))

    assert claims
    assert all(len(claim.statement) <= 1800 for claim in claims)
    assert len(claims) <= 120


def test_page_plan_can_use_supplied_typed_source_claims() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    unit = build_extracted_unit(
        unit_id="prompt-window-0001",
        raw_source=raw_source,
        locator="p.1",
        heading_path="Functions",
        text="Raw prompt-window prose should not become a claim. Another raw sentence appears.",
    )
    evidence = Evidence(
        raw_source=raw_source,
        locator="book.pdf p.1 typed-evidence:record-1",
        claim="Functions are values.",
    )
    typed_claim = SourceClaim(
        source_claim_id="source-claim-typed-evidence-record-1",
        statement="Functions are values.",
        evidence=evidence,
        extracted_unit_id=unit.unit_id,
        source_span=evidence.locator,
        claim_role_tags=("definition",),
        claim_salience=0.91,
        claim_certainty="supported",
        subject_terms=("functions", "values"),
        claim_eligibility="eligible",
        claim_centrality=1.0,
    )

    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=(unit,),
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
        source_claim_items=(typed_claim,),
    )

    assert plan.source_claims == (typed_claim,)
    assert [claim.statement for claim in plan.candidate_claims] == ["Functions are values."]
    assert all("Raw prompt-window prose" not in claim.statement for claim in plan.source_claims)


def test_cosine_uses_explicit_bounded_loop_for_large_embeddings() -> None:
    left = {f"term-{index}": 0.001 for index in range(6000)}
    right = {f"term-{index}": 0.001 for index in range(3000, 9000)}

    assert cosine(left, right) > 0


def test_embedding_counts_a_bounded_token_window() -> None:
    vector = embedding(" ".join(f"term{index}" for index in range(5000)))

    assert len(vector) == 4096
    assert "term0" in vector
    assert "term4096" not in vector


class CompilerArtifactSpyStore(WikiStore):
    def __init__(self, paths: WikiPaths) -> None:
        super().__init__(paths)
        self.write_checks: list[str] = []

    def write_page(self, page: WikiPage) -> None:
        artifact_path = self.ingest_compiler_artifact_dir("book.pdf") / "ingest-artifact-set.json"
        assert artifact_path.exists()
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
        args=_source_summary_write_args(page_id),
    )


def _source_summary_write_args(page_id: str) -> dict[str, object]:
    citation = _citation_for(page_id)
    claim_ids = _source_claim_ids_for(page_id)
    claim_text = f"Hub links [[{FUNCTIONS_PAGE}]] and [[{CLOSURES_PAGE}]]."
    if page_id != BOOK_HUB:
        claim_text = f"The {page_id} source page summarizes this PDF stage."
    return {
        "page_id": page_id,
        "page_kind": "source",
        "summary": f"About {page_id}.",
        "source_record_text": f"Source record for [[{page_id}]]. ({citation})",
        "claim_bullets": [
            {
                "bullet_text": f"{claim_text} ({citation})",
                "covered_source_claims": list(claim_ids),
            },
            {
                "bullet_text": f"The draft preserves planned source coverage. ({citation})",
                "covered_source_claims": [claim_ids[0]],
            },
            {
                "bullet_text": f"The summary keeps the cited PDF support visible. ({citation})",
                "covered_source_claims": [claim_ids[-1]],
            },
        ],
        "sources": ["book.pdf"],
    }


def _citation_for(page_id: str) -> str:
    if page_id == FUNCTIONS_PAGE:
        return "raw/book.pdf p.1-10"
    if page_id == CLOSURES_PAGE:
        return "raw/book.pdf p.11-20"
    return "raw/book.pdf"


def _source_claim_ids_for(page_id: str) -> tuple[str, ...]:
    if page_id == FUNCTIONS_PAGE:
        return ("source-claim-unit-0001-0001",)
    if page_id == CLOSURES_PAGE:
        return ("source-claim-unit-0002-0001",)
    return ("source-claim-unit-0001-0001", "source-claim-unit-0002-0001")


def _turns(page_id: str, finish_tool: str, report: str) -> list[list[ToolCall]]:
    calls = [[_plan_page_call(page_id)], [_write_page_call(page_id)]]
    if finish_tool == "finish_chunk":
        return [
            [ToolCall(tool="search_wiki", args={"query": page_id})],
            *calls,
            [ToolCall(tool=finish_tool, args={"report": report})],
        ]
    return [*calls, [ToolCall(tool=finish_tool, args={"report": report})]]


async def test_fake_pdf_ingest_persists_compiler_artifacts_before_writes(
    paths: WikiPaths,
) -> None:
    (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
    store = CompilerArtifactSpyStore(paths)
    extraction = _fake_extraction(paths)
    session = Session(
        store=store,
        client=FakeClient([]),
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        today=TODAY,
        runs_dir=paths.root / "runs",
        run_id="pdf-test",
        extract_pdf=lambda _pdf, _locator, _reextract: extraction,
    )

    await session.ingest("book.pdf")

    assert store.write_checks == [BOOK_HUB]
    hub_page = store.read_page(BOOK_HUB)
    assert "projection_coverage:" in hub_page
    assert "page_family: source-manifest" in hub_page
    assert "## Compiler Summary" in hub_page
    artifact_dir = store.ingest_compiler_artifact_dir("book.pdf")
    assert (artifact_dir / "ingest-artifact-set.json").is_file()
    assert (artifact_dir / "page-publication-plan.json").is_file()
    assert (artifact_dir / "evidence-pack-set.json").is_file()
    assert (artifact_dir / "article-lint-runs.json").is_file()
