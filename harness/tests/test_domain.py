"""Data-in/data-out tests for the pure domain layer."""

from pathlib import Path

import pytest

from llmwiki.domain.candidates import (
    CandidateBacklog,
    CandidateRecord,
    CandidateSignal,
    reject_candidate,
    update_candidate_backlog,
)
from llmwiki.domain.citations import SourceInventory, inspect_citations, parse_citations
from llmwiki.domain.contradictions import (
    ContradictionFinding,
    collapse_findings,
    select_contradiction_candidates,
)
from llmwiki.domain.evidence import EvidencePolicy
from llmwiki.domain.graph import build_wiki_graph, graph_status
from llmwiki.domain.grounding import (
    ClaimCandidate,
    GroundingAuditReport,
    GroundingSelection,
    GroundingVerdict,
    select_grounding_claims,
)
from llmwiki.domain.index import index_page_ids, parse_index, upsert_index_entry
from llmwiki.domain.ingest_route_history import (
    IngestRoutePlanRecord,
    ingest_route_plan_record_from_json_line,
    ingest_route_plan_records_from_jsonl,
)
from llmwiki.domain.ingest_route_plan import (
    IngestRouteContext,
    IngestRoutePlan,
    IngestRoutePlanError,
    IngestRoutePlanState,
    PlannedPage,
    RouteGap,
    validate_ingest_route_plan,
)
from llmwiki.domain.links import compute_findings, extract_links
from llmwiki.domain.log import format_log_entry
from llmwiki.domain.objects import IngestRun, RawSource, SourceBundle
from llmwiki.domain.pages import (
    LOCAL_FLAT_STRUCTURE,
    PageError,
    PageMetadata,
    PathTemplate,
    WikiPage,
    WikiStructure,
    parse_page,
    render_page,
)
from llmwiki.domain.search import render_hits, search_pages
from llmwiki.domain.semantic_lint import (
    SemanticFinding,
    SemanticLintCandidate,
    SemanticLintReport,
    SemanticLintSelection,
    select_semantic_lint_candidates,
)


class InMemorySourceResolver:
    def __init__(self, sources: dict[str, str]) -> None:
        self._sources = {path: tuple(text.splitlines()) for path, text in sources.items()}

    def source_lines(self, source_path: str) -> tuple[str, ...] | None:
        return self._sources.get(source_path)


INDEX = """# Index

## Sources

- [[alpha-source]] — about alpha

## Entities

## Concepts

- [[bravo]] — concept b
- [[delta]] — concept d

## Syntheses
"""


def _wiki_page(
    page_id: str,
    page_kind: str,
    summary: str,
    page_body: str,
    *,
    sources: tuple[str, ...] = (),
    updated: str = "",
) -> WikiPage:
    return WikiPage(
        page_metadata=PageMetadata(
            page_id=page_id,
            page_kind=page_kind,
            summary=summary,
            sources=sources,
            updated=updated,
        ),
        page_body=page_body,
    )


class TestPages:
    def test_render_parse_roundtrip(self) -> None:
        page = WikiPage(
            page_metadata=PageMetadata(
                page_id="bronze-age",
                page_kind="concept",
                summary="The Bronze Age collapse.",
                sources=("article.md",),
                updated="2026-06-10",
            ),
            page_body="Linked to [[sea-peoples]].\n\nEvidence: (raw/article.md)",
        )
        rendered = render_page(page)
        assert "page_id: bronze-age" in rendered
        assert "page_kind: concept" in rendered
        assert "category:" not in rendered
        assert parse_page(rendered) == page

    @pytest.mark.parametrize("name", ["Bad Name", "UPPER", "trailing-", "-leading", "a--b", ""])
    def test_invalid_names_rejected(self, name: str) -> None:
        with pytest.raises(PageError):
            PageMetadata(page_id=name, page_kind="entity", summary="s")

    def test_invalid_category_rejected(self) -> None:
        with pytest.raises(PageError):
            PageMetadata(page_id="ok", page_kind="article", summary="s")

    def test_summary_collapsed_to_one_line(self) -> None:
        with pytest.raises(PageError):
            PageMetadata(page_id="ok", page_kind="entity", summary="  \n ")

    def test_nested_structure_renders_from_metadata(self) -> None:
        structure = WikiStructure(
            structure_id="nested",
            default_path_template=PathTemplate(
                template_text="{PageKind}/{PageId}.md",
                required_page_metadata_fields=("PageKind", "PageId"),
            ),
        )
        metadata = PageMetadata(page_id="closure", page_kind="concept", summary="Closure.")

        assert structure.render_path(metadata).as_posix() == "concept/closure.md"


class TestIngestRoutePlans:
    def test_domain_objects_cover_local_flat_wiki(self) -> None:
        source = RawSource.from_locator("rules/book.pdf")
        bundle = SourceBundle.one(source)
        metadata = PageMetadata(
            page_id="rules-book",
            page_kind="source",
            summary="Rules book.",
            sources=("rules/book.pdf",),
        )
        run = IngestRun(source_bundle=bundle)

        assert source.source_locator == "rules/book.pdf"
        assert source.source_format == "pdf"
        assert LOCAL_FLAT_STRUCTURE.render_path(metadata).as_posix() == "rules-book.md"
        assert run.source_bundle == bundle
        assert run.wiki_structure == LOCAL_FLAT_STRUCTURE

    def test_source_bundle_rejects_empty_raw_sources(self) -> None:
        with pytest.raises(ValueError, match="SourceBundle"):
            SourceBundle(raw_sources=())

    def test_valid_route_plan_is_accepted_and_authorizes_page_write(self) -> None:
        state = IngestRoutePlanState(IngestRouteContext(source_locator="moon.md", scope="source"))
        plan = _route_plan("moon")

        summary = state.accept(plan)
        authorized = state.authorize_page_write("moon", "source")

        assert summary.planned_page_count == 1
        assert authorized.metadata.page_id == "moon"

    def test_route_plan_rejects_invalid_category(self) -> None:
        with pytest.raises(PageError):
            _planned_page("moon", page_kind="article")

    def test_route_plan_must_match_run_context(self) -> None:
        context = IngestRouteContext(
            source_locator="moon.md", scope="source", profile_ids=("rules",)
        )
        plan = _route_plan("moon", profile_ids=())

        with pytest.raises(IngestRoutePlanError, match="profile_ids"):
            validate_ingest_route_plan(plan, context)

    def test_route_plan_rejects_duplicate_page_ids(self) -> None:
        page = _planned_page("moon")
        plan = IngestRoutePlan(
            source_locator="moon.md",
            scope="source",
            profile_ids=(),
            planned_pages=(page, page),
        )

        with pytest.raises(IngestRoutePlanError, match="Duplicate"):
            validate_ingest_route_plan(plan, IngestRouteContext("moon.md", "source"))

    def test_route_plan_rejects_action_that_disagrees_with_existing_page(self) -> None:
        plan = _route_plan("moon")
        context = IngestRouteContext("moon.md", "source", existing_pages=frozenset({"moon"}))

        with pytest.raises(IngestRoutePlanError, match="exists"):
            validate_ingest_route_plan(plan, context)

    def test_route_plan_rejects_new_page_outside_namespace(self) -> None:
        plan = _route_plan("moon")
        context = IngestRouteContext("moon.md", "source", new_page_prefix="lunar-notes")

        with pytest.raises(IngestRoutePlanError, match="namespace prefix"):
            validate_ingest_route_plan(plan, context)

    def test_route_gaps_are_validated_and_summarized(self) -> None:
        plan = _route_plan(
            "moon",
            gaps=(
                RouteGap(
                    reason="too-granular",
                    source_scope="moon.md",
                    summary="Minor aside belongs inside the source page.",
                ),
            ),
        )

        summary = plan.summary()

        assert summary.route_gap_count == 1
        assert summary.route_gap_summaries == ("Minor aside belongs inside the source page.",)

    def test_route_plan_record_jsonl_roundtrip(self) -> None:
        plan = _route_plan(
            "moon",
            gaps=(
                RouteGap(
                    reason="too-granular",
                    source_scope="moon.md",
                    summary="Minor aside belongs inside the source page.",
                ),
            ),
        )
        record = IngestRoutePlanRecord.from_plan(
            plan,
            date="2026-06-18",
            run_id="run-1",
            page_writes=("moon",),
        )

        line = record.to_json_line()

        assert ingest_route_plan_record_from_json_line(line) == record
        assert ingest_route_plan_records_from_jsonl(line + "\n") == (record,)


def _planned_page(
    page_id: str,
    *,
    page_kind: str = "source",
    action: str = "create",
) -> PlannedPage:
    return PlannedPage(
        metadata=PageMetadata(page_id=page_id, page_kind=page_kind, summary="Lunar notes."),
        role="primary source page",
        action=action,  # type: ignore[arg-type]
        source_scope="moon.md",
        confidence="high",
        rationale="The source is about the Moon.",
    )


def _route_plan(
    page_id: str,
    *,
    profile_ids: tuple[str, ...] = (),
    gaps: tuple[RouteGap, ...] = (),
) -> IngestRoutePlan:
    return IngestRoutePlan(
        source_locator="moon.md",
        scope="source",
        profile_ids=profile_ids,
        planned_pages=(_planned_page(page_id),),
        gaps=gaps,
    )


class TestIndex:
    def test_parse_extracts_entries_with_categories(self) -> None:
        entries = parse_index(INDEX)
        assert [(e.page_id, e.page_kind) for e in entries] == [
            ("alpha-source", "source"),
            ("bravo", "concept"),
            ("delta", "concept"),
        ]

    def test_upsert_inserts_sorted_within_category(self) -> None:
        updated = upsert_index_entry(
            INDEX,
            PageMetadata(page_id="charlie", page_kind="concept", summary="concept c"),
        )
        page_ids = [e.page_id for e in parse_index(updated) if e.page_kind == "concept"]
        assert page_ids == ["bravo", "charlie", "delta"]

    def test_upsert_replaces_existing_entry(self) -> None:
        updated = upsert_index_entry(
            INDEX,
            PageMetadata(page_id="bravo", page_kind="concept", summary="new summary"),
        )
        entries = {e.page_id: e.summary for e in parse_index(updated)}
        assert entries["bravo"] == "new summary"
        assert len([e for e in parse_index(updated) if e.page_id == "bravo"]) == 1

    def test_upsert_moves_page_between_categories(self) -> None:
        updated = upsert_index_entry(
            INDEX,
            PageMetadata(page_id="bravo", page_kind="synthesis", summary="now a synthesis"),
        )
        entries = {e.page_id: e.page_kind for e in parse_index(updated)}
        assert entries["bravo"] == "synthesis"

    def test_upsert_into_empty_category(self) -> None:
        updated = upsert_index_entry(
            INDEX,
            PageMetadata(page_id="ada", page_kind="entity", summary="a person"),
        )
        assert ("ada", "entity") in [(e.page_id, e.page_kind) for e in parse_index(updated)]


class TestSharedObjectBoundaryLanguage:
    def test_old_page_validation_names_are_not_defined(self) -> None:
        pages_text = Path("harness/src/llmwiki/domain/pages.py").read_text(encoding="utf-8")

        assert "PAGE_CATEGORIES" not in pages_text
        assert "validate_page_name" not in pages_text
        assert "validate_category" not in pages_text
        assert "_legacy_page_args" not in pages_text
        assert "def __init__" not in pages_text

    def test_index_page_ids(self) -> None:
        assert index_page_ids(INDEX) == {"alpha-source", "bravo", "delta"}


class TestCandidates:
    def test_candidate_canonicalization_and_alias_deduplication(self) -> None:
        backlog = update_candidate_backlog(
            CandidateBacklog(),
            (
                CandidateSignal("NaN", "concept", "linked from alpha", "alpha"),
                CandidateSignal("nan", "concept", "linked from beta", "beta"),
            ),
            existing_pages=set(),
            today="2026-06-15",
        )

        assert len(backlog.records) == 1
        record = backlog.records[0]
        assert record.slug == "nan"
        assert record.mention_count == 2
        assert record.status == "queued"
        assert record.source_pages == ("alpha", "beta")

    def test_existing_pages_are_marked_promoted_not_reported_active(self) -> None:
        backlog = CandidateBacklog(
            (
                CandidateRecord(
                    slug="iterable",
                    display_name="iterable",
                    category_guess="concept",
                    aliases=(),
                    reasons=("linked from alpha",),
                    source_pages=("alpha",),
                    mention_count=1,
                    status="queued",
                    first_seen="2026-06-14",
                    last_seen="2026-06-14",
                ),
            )
        )

        updated = update_candidate_backlog(
            backlog,
            (),
            existing_pages={"iterable"},
            today="2026-06-15",
        )

        assert updated.records[0].status == "promoted"
        assert updated.top() == ()

    def test_rejected_candidates_stay_rejected_across_updates(self) -> None:
        rejected = reject_candidate(CandidateBacklog(), "nan", "covered by number", "2026-06-14")

        updated = update_candidate_backlog(
            rejected,
            (CandidateSignal("nan", "concept", "linked from alpha", "alpha"),),
            existing_pages=set(),
            today="2026-06-15",
        )

        assert updated.records[0].status == "rejected"
        assert updated.records[0].status_reason == "covered by number"
        assert updated.records[0].mention_count == 1

    def test_backlog_json_roundtrip(self) -> None:
        backlog = update_candidate_backlog(
            CandidateBacklog(),
            (CandidateSignal("left variadic functions", "concept", "linked", "alpha"),),
            existing_pages=set(),
            today="2026-06-15",
        )

        assert CandidateBacklog.from_json_text(backlog.to_json_text()) == backlog


class TestSemanticLint:
    def test_selection_is_bounded_and_reasoned_from_overlapping_pages(self) -> None:
        pages = {
            "alpha": render_page(
                _wiki_page(
                    "alpha",
                    "concept",
                    "A.",
                    "Feature arrived in ES2015. See [[beta]]. (raw/book.md)",
                    sources=("book.md",),
                    updated="2026-06-10",
                )
            ),
            "beta": render_page(
                _wiki_page(
                    "beta",
                    "concept",
                    "B.",
                    "Feature details changed later. See [[alpha]]. (raw/book.md)",
                    sources=("book.md",),
                    updated="2026-06-15",
                )
            ),
            "gamma": render_page(
                _wiki_page("gamma", "concept", "G.", "Unrelated.", updated="2026-06-15")
            ),
        }

        selection = select_semantic_lint_candidates(
            pages,
            CandidateBacklog(),
            max_items=1,
        )

        assert selection.candidate_count == 1
        assert selection.audited_count == 1
        assert selection.skipped_count == 0
        assert selection.candidates[0].page_names == ("alpha", "beta")
        assert "shared raw citations" in selection.candidates[0].reason

    def test_selection_includes_candidate_backlog_data_gaps(self) -> None:
        backlog = update_candidate_backlog(
            CandidateBacklog(),
            (
                CandidateSignal("iterable", "concept", "linked from alpha", "alpha"),
                CandidateSignal("iterable", "concept", "linked from beta", "beta"),
            ),
            existing_pages=set(),
            today="2026-06-15",
        )
        pages = {
            "alpha": render_page(_wiki_page("alpha", "concept", "A.", "Mentions [[iterable]].")),
            "beta": render_page(_wiki_page("beta", "concept", "B.", "Mentions [[iterable]].")),
        }

        selection = select_semantic_lint_candidates(pages, backlog, max_items=5)

        data_gap = next(item for item in selection.candidates if item.missing_concept)
        assert data_gap.missing_concept == "iterable"
        assert "data gap candidate" in data_gap.reason

    def test_broad_shared_source_alone_does_not_create_candidate(self) -> None:
        pages = {
            "alpha": render_page(
                _wiki_page("alpha", "concept", "A.", "General notes.", sources=("book.pdf",))
            ),
            "beta": render_page(
                _wiki_page("beta", "concept", "B.", "Other notes.", sources=("book.pdf",))
            ),
        }

        selection = select_semantic_lint_candidates(pages, CandidateBacklog(), max_items=5)

        assert selection.candidate_count == 0

    def test_report_includes_scope_findings_and_uncertainty(self) -> None:
        selection = SemanticLintSelection(
            candidates=(
                SemanticLintCandidate(
                    reason="data gap candidate",
                    page_names=("alpha",),
                    missing_concept="iterable",
                    excerpt="[[alpha]] mentions iterable.",
                    score=5,
                ),
            ),
            candidate_count=3,
            max_items=1,
        )
        report = SemanticLintReport(
            selection=selection,
            findings=(
                SemanticFinding(
                    kind="data_gap",
                    affected_pages=("alpha",),
                    rationale="Repeated missing topic.",
                    evidence_consulted="[[alpha]]",
                    recommended_action="Consider ingesting a source.",
                ),
            ),
            model_report="Audited one item.",
        ).render()

        assert "Candidate items discovered: 3" in report
        assert "Skipped by cap: 2" in report
        assert "Finding 1: data_gap" in report
        assert "bounded semantic lint pass" in report


class TestLog:
    def test_entry_has_greppable_prefix(self) -> None:
        entry = format_log_entry("2026-06-10", "ingest", "article.md", "Wrote 3 pages.")
        assert "## [2026-06-10] ingest | article.md" in entry
        assert "Wrote 3 pages." in entry

    def test_subject_collapsed_and_truncated(self) -> None:
        entry = format_log_entry("2026-06-10", "query", "a\nb" + "x" * 200, "d")
        prefix_line = next(line for line in entry.splitlines() if line.startswith("## ["))
        assert "\n" not in prefix_line
        assert len(prefix_line) < 120


class TestLinks:
    def test_extract_links(self) -> None:
        assert extract_links(
            "See [[alpha]], [[beta-2|shown label]], and [[gamma]]. Not [link]."
        ) == {"alpha", "beta-2", "gamma"}

    def test_findings_detect_all_issue_kinds(self) -> None:
        pages = {
            "alpha": "links to [[beta]] and [[ghost]]",
            "beta": "no links here",
            "gamma": "links to [[alpha]]",
        }
        findings = compute_findings(pages, index_page_ids={"alpha", "beta", "zombie"})
        assert findings.broken_links == {"alpha": ("ghost",)}
        assert findings.orphan_pages == ("gamma",)
        assert findings.missing_from_index == ("gamma",)
        assert findings.stale_index_entries == ("zombie",)
        assert not findings.is_clean
        assert "ghost" in findings.render()

    def test_clean_wiki_is_clean(self) -> None:
        pages = {"alpha": "see [[beta]]", "beta": "see [[alpha]]"}
        findings = compute_findings(pages, index_page_ids={"alpha", "beta"})
        assert findings.is_clean

    def test_single_page_is_not_an_orphan(self) -> None:
        findings = compute_findings({"only": "text"}, index_page_ids={"only"})
        assert findings.orphan_pages == ()

    def test_exempt_pages_do_not_create_graph_findings_or_inbound_credit(self) -> None:
        findings = compute_findings(
            {
                "alpha": "No links.",
                "wiki-health": "Report mentions [[alpha]] and [[ghost]].",
            },
            index_page_ids={"alpha", "wiki-health"},
            exempt_from_orphans=frozenset({"wiki-health"}),
        )
        assert findings.broken_links == {}
        assert findings.orphan_pages == ("alpha",)

    def test_source_hubs_are_not_reported_as_orphans(self) -> None:
        pages = {
            "book": render_page(
                _wiki_page(
                    "book",
                    "source",
                    "Book hub.",
                    "Hub source page.",
                    sources=("raw/book.pdf",),
                )
            ),
            "book-functions": render_page(
                _wiki_page(
                    "book-functions",
                    "source",
                    "Functions chapter.",
                    "Unlinked chapter page.",
                    sources=("raw/book.pdf p.1-10",),
                )
            ),
        }

        findings = compute_findings(pages, index_page_ids={"book", "book-functions"})

        assert findings.orphan_pages == ("book-functions",)


class TestGraph:
    def test_graph_output_is_deterministic_and_excludes_system_pages(self) -> None:
        pages = {
            "alpha": render_page(
                _wiki_page(
                    "alpha",
                    "concept",
                    "Alpha summary.",
                    "See [[beta]].",
                    sources=("article.md",),
                )
            ),
            "beta": render_page(_wiki_page("beta", "entity", "Beta summary.", "Back.")),
            "wiki-health": render_page(
                _wiki_page("wiki-health", "synthesis", "Report.", "Links [[ghost]].")
            ),
        }

        first = build_wiki_graph(pages, generated_date="2026-06-15")
        second = build_wiki_graph(pages, generated_date="2026-06-15")

        assert first.to_json_text() == second.to_json_text()
        assert [node.name for node in first.nodes] == ["alpha", "beta"]
        assert first.edges[0].source == "alpha"
        assert first.edges[0].target == "beta"
        assert first.edges[0].resolved

    def test_graph_represents_unresolved_edges(self) -> None:
        pages = {"alpha": render_page(_wiki_page("alpha", "concept", "A.", "See [[ghost]]."))}

        graph = build_wiki_graph(pages, generated_date="2026-06-15")

        assert len(graph.edges) == 1
        assert graph.edges[0].target == "ghost"
        assert not graph.edges[0].resolved

    def test_graph_status_ignores_generated_date_but_detects_stale_content(self) -> None:
        pages = {"alpha": render_page(_wiki_page("alpha", "concept", "A.", "See [[beta]]."))}
        graph = build_wiki_graph(pages, generated_date="2026-06-15")
        same_graph_new_date = build_wiki_graph(pages, generated_date="2026-06-16")
        changed_graph = build_wiki_graph(
            {"alpha": render_page(_wiki_page("alpha", "concept", "A.", "See [[gamma]]."))},
            generated_date="2026-06-16",
        )

        assert graph_status(same_graph_new_date, graph.to_json_text()).status == "current"
        assert graph_status(changed_graph, graph.to_json_text()).status == "stale"


class TestCitations:
    INVENTORY = SourceInventory.from_raw_relative_paths(
        [
            "article.md",
            "book.pdf",
            "nested/source.md",
            "Sword World RPG - Complete Edition.pdf",
            "javascriptallonge.pdf",
        ]
    )

    def test_markdown_source_citation(self) -> None:
        report = inspect_citations(
            "alpha",
            "A supported claim. (raw/article.md)",
            self.INVENTORY,
        )
        assert report.is_clean
        assert [(c.source_path, c.page_range, c.line_range) for c in report.citations] == [
            ("raw/article.md", None, None)
        ]

    def test_pdf_page_range(self) -> None:
        report = inspect_citations(
            "alpha",
            "A book claim. (raw/book.pdf p.28-41)",
            self.INVENTORY,
        )
        assert report.is_clean
        assert report.citations[0].page_range == (28, 41)

    def test_pdf_path_with_spaces(self) -> None:
        report = inspect_citations(
            "alpha",
            "A rulebook claim. (raw/Sword World RPG - Complete Edition.pdf p.50-56)",
            self.INVENTORY,
        )
        assert report.is_clean
        assert report.citations[0].source_path == ("raw/Sword World RPG - Complete Edition.pdf")
        assert report.citations[0].page_range == (50, 56)

    def test_citation_trailing_sentence_period_is_not_part_of_path(self) -> None:
        report = inspect_citations(
            "alpha",
            "A source-level claim cites raw/javascriptallonge.pdf.",
            self.INVENTORY,
        )
        assert report.is_clean
        assert report.citations[0].source_path == "raw/javascriptallonge.pdf"

    def test_extra_uncertainty_text_after_locator_does_not_break_citation(self) -> None:
        report = inspect_citations(
            "alpha",
            "A narrative claim. (raw/javascriptallonge.pdf p.261-272, may)",
            self.INVENTORY,
        )
        assert report.is_clean
        assert report.citations[0].page_range == (261, 272)

    def test_non_ascii_page_range_hyphen_is_normalized(self) -> None:
        report = inspect_citations(
            "alpha",
            "A generated citation. (raw/book.pdf p.113‑117)",
            self.INVENTORY,
        )
        assert report.is_clean
        assert report.citations[0].page_range == (113, 117)

    def test_normalized_line_range_with_source_context(self) -> None:
        report = inspect_citations(
            "alpha",
            "A line-backed claim. (raw/article.md normalized:L12-L20)",
            self.INVENTORY,
        )
        assert report.is_clean
        assert report.citations[0].line_range == (12, 20)

    def test_standalone_normalized_locator_is_malformed(self) -> None:
        report = parse_citations("alpha", "Line-only locator normalized:L12-L20.")
        assert [finding.code for finding in report.findings] == ["malformed-line-range"]

    def test_malformed_page_range(self) -> None:
        report = inspect_citations(
            "alpha",
            "A bad locator. (raw/book.pdf p.xx-41)",
            self.INVENTORY,
        )
        assert [finding.code for finding in report.findings] == ["malformed-page-range"]
        assert report.findings[0].severity == "fail"

    def test_malformed_ordered_ranges(self) -> None:
        report = inspect_citations(
            "alpha",
            "Ranges must increase. (raw/book.pdf p.41-28) (raw/article.md normalized:L20-L12)",
            self.INVENTORY,
        )
        assert [finding.code for finding in report.findings] == [
            "malformed-page-range",
            "malformed-line-range",
        ]

    def test_missing_source(self) -> None:
        report = inspect_citations(
            "alpha",
            "Missing source. (raw/missing.md)",
            self.INVENTORY,
        )
        assert [finding.code for finding in report.findings] == ["missing-source"]
        assert report.findings[0].citation_text == "raw/missing.md"

    def test_path_traversal_attempt(self) -> None:
        report = inspect_citations(
            "alpha",
            "No escape. (raw/../secret.md)",
            self.INVENTORY,
        )
        assert [finding.code for finding in report.findings] == ["path-outside-raw"]
        assert report.findings[0].severity == "fail"

    def test_ocr_caveat_detection(self) -> None:
        report = parse_citations(
            "alpha",
            'The exact label was "[figure text (OCR, unverified): ANTIDOTE DECAF]".',
        )
        assert [finding.code for finding in report.findings] == ["ocr-verbatim-risk"]
        assert report.findings[0].severity == "warn"

    def test_no_citations_is_valid_input(self) -> None:
        report = inspect_citations("alpha", "No evidence cited here yet.", self.INVENTORY)
        assert report == parse_citations("alpha", "No evidence cited here yet.")

    def test_normalized_locator_exact_quoted_evidence_passes(self) -> None:
        policy = EvidencePolicy(mode="fail")
        resolver = InMemorySourceResolver({"raw/article.md": "Intro\nAlpha beta evidence.\nEnd"})
        result = policy.check_page(
            "alpha",
            '"Alpha beta evidence." (raw/article.md normalized:L2)',
            self.INVENTORY,
            resolver,
        )
        assert result.allowed
        assert result.findings == ()

    def test_normalized_locator_canonicalized_local_warns(self) -> None:
        policy = EvidencePolicy(mode="warn")
        resolver = InMemorySourceResolver({"raw/article.md": "Intro\nAlpha   beta evidence.\nEnd"})
        result = policy.check_page(
            "alpha",
            '"Alpha beta evidence." (raw/article.md normalized:L2)',
            self.INVENTORY,
            resolver,
        )
        assert [finding.code for finding in result.findings] == ["evidence-canonicalized"]
        assert result.findings[0].severity == "warn"

    def test_normalized_locator_global_match_warns_with_suggestion(self) -> None:
        policy = EvidencePolicy(mode="warn")
        resolver = InMemorySourceResolver({"raw/article.md": "Wrong line.\nElsewhere evidence."})
        result = policy.check_page(
            "alpha",
            '"Elsewhere evidence." (raw/article.md normalized:L1)',
            self.INVENTORY,
            resolver,
        )
        assert [finding.code for finding in result.findings] == ["evidence-outside-locator"]
        assert "Suggested locator: normalized:L2" in result.findings[0].message

    def test_normalized_locator_out_of_range_fails(self) -> None:
        policy = EvidencePolicy(mode="fail")
        resolver = InMemorySourceResolver({"raw/article.md": "Only one line."})
        result = policy.check_page(
            "alpha",
            '"Only one line." (raw/article.md normalized:L2)',
            self.INVENTORY,
            resolver,
        )
        assert [finding.code for finding in result.findings] == ["locator-out-of-range"]
        assert not result.allowed

    def test_normalized_locator_fabricated_quote_fails(self) -> None:
        policy = EvidencePolicy(mode="fail")
        resolver = InMemorySourceResolver({"raw/article.md": "Real source text."})
        result = policy.check_page(
            "alpha",
            '"Fabricated quote." (raw/article.md normalized:L1)',
            self.INVENTORY,
            resolver,
        )
        assert [finding.code for finding in result.findings] == ["evidence-not-found"]
        assert not result.allowed

    def test_normalized_locator_table_cell_evidence(self) -> None:
        policy = EvidencePolicy(mode="fail")
        resolver = InMemorySourceResolver({"raw/article.md": "Table evidence text."})
        result = policy.check_page(
            "alpha",
            "| Claim | Table evidence text. | raw/article.md normalized:L1 |",
            self.INVENTORY,
            resolver,
        )
        assert result.findings == ()


class TestGrounding:
    INVENTORY = SourceInventory.from_raw_relative_paths(["article.md"])

    def test_selector_skips_pages_with_fatal_evidence_findings(self) -> None:
        resolver = InMemorySourceResolver({"raw/article.md": "Actual source line."})
        pages = {
            "alpha": render_page(
                _wiki_page(
                    "alpha",
                    "concept",
                    "A.",
                    '"Fabricated source line." (raw/article.md normalized:L1)',
                )
            )
        }

        selection = select_grounding_claims(
            pages,
            self.INVENTORY,
            resolver,
            max_claims=5,
        )

        assert selection.candidates == ()
        assert selection.candidate_count == 0
        assert [finding.code for finding in selection.deterministic_findings] == [
            "evidence-not-found"
        ]

    def test_selector_bounds_claims_and_reports_skipped_count(self) -> None:
        resolver = InMemorySourceResolver(
            {
                "raw/article.md": (
                    "Alpha evidence supports the first claim.\n"
                    "Beta evidence supports the second claim."
                )
            }
        )
        pages = {
            "alpha": render_page(
                _wiki_page(
                    "alpha",
                    "concept",
                    "A.",
                    "Alpha evidence supports the first claim. "
                    "(raw/article.md normalized:L1)\n"
                    "Beta evidence supports the second claim. "
                    "(raw/article.md normalized:L2)",
                )
            )
        }

        selection = select_grounding_claims(
            pages,
            self.INVENTORY,
            resolver,
            max_claims=1,
        )

        assert selection.candidate_count == 2
        assert selection.audited_count == 1
        assert selection.skipped_count == 1
        assert "Alpha evidence" in selection.candidates[0].evidence_excerpt

    def test_selector_ignores_citation_labels_and_citation_only_lines(self) -> None:
        resolver = InMemorySourceResolver({"raw/article.md": "Actual claim evidence."})
        pages = {
            "alpha": render_page(
                _wiki_page(
                    "alpha",
                    "concept",
                    "A.",
                    "Citations: (raw/article.md normalized:L1)\n"
                    "- (raw/article.md normalized:L1)\n"
                    "Cited in: [[related-page]] (raw/article.md normalized:L1)\n"
                    "Actual claim evidence. (raw/article.md normalized:L1)",
                )
            )
        }

        selection = select_grounding_claims(
            pages,
            self.INVENTORY,
            resolver,
            max_claims=5,
        )

        assert selection.candidate_count == 1
        assert selection.candidates[0].claim_text == "Actual claim evidence."

    def test_report_renders_scope_deterministic_findings_and_verdicts(self) -> None:
        selection = GroundingSelection(
            candidates=(
                ClaimCandidate(
                    page_name="alpha",
                    claim_text="The claim is broader than the excerpt.",
                    local_context="The claim is broader than the excerpt. (raw/article.md)",
                    citation_text="raw/article.md",
                    evidence_excerpt="The excerpt supports only part.",
                ),
            ),
            deterministic_findings=(),
            candidate_count=2,
            max_claims=1,
        )
        report = GroundingAuditReport(
            selection=selection,
            verdicts=(
                GroundingVerdict(
                    page_name="alpha",
                    claim_text="The claim is broader than the excerpt.",
                    verdict="too_broad",
                    rationale="The citation supports only part of the statement.",
                    recommended_action="Narrow the page claim or add stronger evidence.",
                ),
            ),
            model_report="Audited one claim.",
        ).render()

        assert "Claim candidates discovered: 2" in report
        assert "Skipped by cap: 1" in report
        assert "Verdict 1: WARN - too_broad" in report
        assert "Audited one claim." in report


class TestContradictions:
    def test_candidate_selection_shared_sources(self) -> None:
        pages = {
            "alpha": render_page(
                _wiki_page("alpha", "concept", "A.", "Alpha claim.", sources=("book.md",))
            ),
            "beta": render_page(
                _wiki_page("beta", "concept", "B.", "Beta claim.", sources=("book.md",))
            ),
        }
        selection = select_contradiction_candidates(pages)
        assert selection.candidate_count == 1
        assert selection.candidates[0].reasons[0] == "shared sources: book.md"

    def test_candidate_selection_direct_link(self) -> None:
        pages = {
            "alpha": render_page(_wiki_page("alpha", "concept", "A.", "See [[beta]].")),
            "beta": render_page(_wiki_page("beta", "concept", "B.", "Beta claim.")),
        }
        selection = select_contradiction_candidates(pages)
        assert selection.candidate_count == 1
        assert "direct wiki link" in selection.candidates[0].reasons

    def test_candidate_selection_shared_raw_citations(self) -> None:
        pages = {
            "alpha": render_page(_wiki_page("alpha", "concept", "A.", "Claim. (raw/book.md)")),
            "beta": render_page(_wiki_page("beta", "concept", "B.", "Other claim. (raw/book.md)")),
        }
        selection = select_contradiction_candidates(pages)
        assert selection.candidate_count == 1
        assert selection.candidates[0].reasons[0] == "shared raw citations: raw/book.md"

    def test_candidate_selection_keyword_overlap(self) -> None:
        pages = {
            "alpha": render_page(
                _wiki_page("alpha", "concept", "A.", "Orbit mechanics require transfer windows.")
            ),
            "beta": render_page(
                _wiki_page("beta", "concept", "B.", "Transfer windows shape orbit mechanics.")
            ),
        }
        selection = select_contradiction_candidates(pages)
        assert selection.candidate_count == 1
        assert selection.candidates[0].reasons[0].startswith("keyword overlap:")

    def test_candidate_selection_cap_reports_skipped(self) -> None:
        pages = {
            name: render_page(
                _wiki_page(name, "concept", f"{name}.", "Claim.", sources=("book.md",))
            )
            for name in ("alpha", "beta", "gamma", "delta")
        }
        selection = select_contradiction_candidates(pages, max_pairs=2)
        assert selection.candidate_count == 6
        assert selection.audited_count == 2
        assert selection.skipped_count == 4

    def test_duplicate_findings_are_collapsed(self) -> None:
        finding = ContradictionFinding(
            page_a="alpha",
            claim_a="ES2015 introduced the feature.",
            page_b="beta",
            claim_b="ES2019 introduced the feature.",
            severity="medium",
            rationale="The years conflict.",
            recommended_action="Inspect source dates.",
        )
        duplicate = ContradictionFinding(
            page_a="beta",
            claim_a="ES2019 introduced the feature.",
            page_b="alpha",
            claim_b="ES2015 introduced the feature.",
            severity="high",
            rationale="Same conflict.",
            recommended_action="Inspect source dates.",
        )
        assert collapse_findings((finding, duplicate)) == (finding,)


class TestSearch:
    PAGES = {
        "bronze-age": "The Bronze Age collapse affected the Hittites.",
        "sea-peoples": "The Sea Peoples raided during the Bronze Age collapse collapse.",
        "unrelated": "Nothing relevant here.",
    }

    def test_ranks_by_term_frequency_and_name_match(self) -> None:
        hits = search_pages(self.PAGES, "bronze collapse")
        assert [h.name for h in hits] == ["bronze-age", "sea-peoples"]

    def test_no_match_returns_empty(self) -> None:
        assert search_pages(self.PAGES, "quasar") == []

    def test_no_match_message_points_to_index_tool(self) -> None:
        message = render_hits([])
        assert "read_index" in message
        assert "read_page" not in message

    def test_snippet_contains_context(self) -> None:
        hits = search_pages(self.PAGES, "hittites")
        assert "Hittites" in hits[0].snippet
