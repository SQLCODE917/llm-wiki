"""Curator-status and maintenance tests: deterministic, model-free health checks."""

from typing import NoReturn

import pytest

from llmwiki.cli import _build_parser, _curator_report, _run
from llmwiki.config import ConfigError, WikiPaths
from llmwiki.domain.evidence_registry import (
    EvidenceRecord,
    EvidenceRegistry,
    SourceRange,
    source_text_from_text,
)
from llmwiki.domain.evidence_registry_io import registry_to_json
from llmwiki.domain.graph import build_wiki_graph
from llmwiki.domain.index import empty_index
from llmwiki.domain.ingest_route_history import IngestRoutePlanRecord
from llmwiki.domain.pages import PageMetadata, WikiPage, render_page
from llmwiki.pdf.manifest import ChunkRecord, Manifest, to_json
from llmwiki.store import WikiStore

TODAY = "2026-06-10"


def _page(
    name: str,
    body: str,
    category: str = "concept",
    summary: str | None = None,
    sources: tuple[str, ...] = (),
) -> WikiPage:
    return WikiPage(
        page_metadata=PageMetadata(
            page_id=name,
            page_kind=category,
            summary=summary or f"{name} summary.",
            sources=sources,
            updated=TODAY,
        ),
        page_body=body,
    )


class TestCuratorReport:
    def test_empty_wiki_recommends_ingest(self, store: WikiStore, paths: WikiPaths) -> None:
        report = _curator_report(store, paths, "off")

        assert "# Curator Status" in report
        assert "Total wiki pages: 0" in report
        assert "Strict evidence mode: off. Citation validation skipped." in report
        assert "No salience entries." in report
        assert "Ingest a source" in report

    def test_healthy_wiki_has_no_deterministic_actions(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        (paths.raw_dir / "article.md").write_text("Source text.", encoding="utf-8")
        store.write_page(_page("alpha", "[[beta]]", sources=("article.md",)))
        store.write_page(_page("beta", "[[alpha]]", sources=("article.md",)))

        report = _curator_report(store, paths, "off")

        assert "Total wiki pages: 2" in report
        assert "Raw source files: 1" in report
        assert "No deterministic issues found" in report
        assert "No deterministic maintenance actions" in report

    def test_report_surfaces_broken_links_orphans_and_index_drift(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(_page("alpha", "Links to [[ghost]]."))
        store.write_page(_page("beta", "No inbound links."))
        paths.index_path.write_text(empty_index(), encoding="utf-8")

        report = _curator_report(store, paths, "off")

        assert "Broken [[links]]" in report
        assert "alpha links to missing page(s): ghost" in report
        assert "Orphan pages" in report
        assert "- beta" in report
        assert "Pages missing from index.md" in report
        assert "Repair broken links" in report
        assert "Review index drift" in report
        assert "Review orphan pages" in report

    def test_curator_status_reads_existing_candidate_backlog(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(_page("alpha", "Links to [[iterable]]."))
        _curator_report(store, paths, "off", update_candidates=True, today=TODAY)

        report = _curator_report(store, paths, "off")

        assert "## Candidate Page Backlog" in report
        assert "iterable" in report
        assert "discovered" in report

    def test_curator_status_includes_latest_semantic_lint_summary(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(
            _page(
                "wiki-semantic-lint",
                "# Semantic Lint\n\n## Audit Scope\n\nAudited items: 1\n\n## Findings\n\nNone.",
                category="synthesis",
            )
        )

        report = _curator_report(store, paths, "off")

        assert "## Latest Semantic Lint" in report
        assert "Audited items: 1" in report
        assert "category: synthesis" not in report

    def test_curator_status_reports_evidence_registry_counts(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        (paths.raw_dir / "article.md").write_text("Source evidence.", encoding="utf-8")
        registry = EvidenceRegistry(
            registry_id="test-registry",
            source_texts=(source_text_from_text("article.md", "Source evidence."),),
            source_ranges=(
                SourceRange(
                    source_range_id="source-range-alpha",
                    page_id="alpha",
                    source_locator="article.md",
                    page_range=None,
                    line_range=(1, 1),
                    heading_path="Alpha",
                ),
            ),
            evidence_records=(
                EvidenceRecord(
                    evidence_id="evidence-alpha",
                    source_locator="article.md",
                    source_hash="hash",
                    source_range_id="source-range-alpha",
                    line_range=(1, 1),
                    excerpt="Source evidence.",
                    excerpt_digest="digest",
                    evidence_kind="source-claim",
                    source_claim_id="source-claim-alpha",
                ),
            ),
        )
        store.write_evidence_registry_artifact("article.md", registry_to_json(registry))
        store.write_page(
            _page(
                "alpha",
                '"Source evidence." (raw/article.md normalized:L1)',
                sources=("article.md",),
            )
        )

        report = _curator_report(store, paths, "warn")

        assert (
            "Evidence registry: 1 source text(s), 1 source range(s), 1 evidence record(s)."
            in report
        )

    def test_curator_status_reports_graph_missing_and_current(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(_page("alpha", "See [[beta]]."))
        store.write_page(_page("beta", "Back to [[alpha]]."))

        missing = _curator_report(store, paths, "off")
        store.write_graph_json(
            build_wiki_graph(store.page_texts(), generated_date=TODAY).to_json_text()
        )
        current = _curator_report(store, paths, "off")

        assert "Graph export: missing" in missing
        assert "Graph export: current" in current

    def test_curator_status_reports_ingest_route_plan_gaps(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        manifest_dir = paths.cache_dir / "deadbeef"
        manifest_dir.mkdir(parents=True)
        manifest = Manifest(
            source="book.pdf",
            sha256="deadbeef" * 8,
            chunks=(
                ChunkRecord(
                    chunk_id=1,
                    heading="Functions",
                    start_page=1,
                    end_page=10,
                    token_estimate=4000,
                    status="done",
                    route_plan_pages=2,
                    route_plan_gaps=1,
                    route_gap_summaries=("Minor syntax aside folded into chapter page.",),
                ),
            ),
        )
        (manifest_dir / "manifest.json").write_text(to_json(manifest), encoding="utf-8")

        report = _curator_report(store, paths, "off")

        assert "## Ingest Route Plans" in report
        assert "Planned pages recorded: 2" in report
        assert "Route gaps recorded: 1" in report
        assert "raw/book.pdf chunk 1: Minor syntax aside folded into chapter page." in report

    def test_curator_status_reports_markdown_ingest_route_plan_gaps(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        paths.route_plan_history_path.parent.mkdir(parents=True)
        record = IngestRoutePlanRecord(
            date=TODAY,
            run_id="run-1",
            source_locator="article.md",
            scope="source",
            chunk_id=None,
            profile_ids=(),
            planned_page_count=1,
            route_gap_count=1,
            route_gap_summaries=("Minor aside stayed inside the source page.",),
            planned_page_ids=("article",),
            page_writes=("article",),
        )
        paths.route_plan_history_path.write_text(record.to_json_line() + "\n", encoding="utf-8")

        report = _curator_report(store, paths, "off")

        assert "Planned pages recorded: 1" in report
        assert "Route gaps recorded: 1" in report
        assert "raw/article.md: Minor aside stayed inside the source page." in report

    def test_report_surfaces_citation_warnings(self, store: WikiStore, paths: WikiPaths) -> None:
        store.write_page(_page("alpha", "Claim cites a missing source. (raw/missing.md)"))

        report = _curator_report(store, paths, "warn")

        assert "Strict evidence mode: warn" in report
        assert "missing-source" in report
        assert "Citation findings: 1" in report

    def test_health_and_curator_status_are_not_reported_as_orphans(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(_page("alpha", "[[beta]]"))
        store.write_page(_page("beta", "[[alpha]]"))
        store.write_page(_page("wiki-health", "Old health report.", category="synthesis"))
        store.write_page(_page("wiki-curator-status", "Old status report.", category="synthesis"))

        report = _curator_report(store, paths, "off")

        assert "Orphan pages" not in report
        assert "wiki-health" not in report
        assert "wiki-curator-status" not in report

    def test_missing_navigation_files_are_reported(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        paths.index_path.unlink()
        paths.log_path.unlink()

        report = _curator_report(store, paths, "off")

        assert "index.md: missing" in report
        assert "log.md: missing" in report
        assert "wiki/index.md is missing" in report
        assert "wiki/log.md is missing" in report


class TestCuratorCli:
    async def test_curator_status_is_read_only_and_backend_free(
        self, paths: WikiPaths, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        def fail_backend(*args: object, **kwargs: object) -> NoReturn:
            raise AssertionError("status must not load backend config")

        monkeypatch.setattr("llmwiki.cli.load_backend_config", fail_backend)
        monkeypatch.setattr("llmwiki.cli.start_backend", fail_backend)
        before_log = paths.log_path.read_text(encoding="utf-8")
        args = _build_parser().parse_args(
            ["--root", str(paths.root), "--runtime", "not-needed", "curator-status"]
        )

        result = await _run(args)

        assert result.op == "curator-status"
        assert "# Curator Status" in result.output
        assert result.transcript_path is None
        assert before_log == paths.log_path.read_text(encoding="utf-8")
        assert not (paths.wiki_dir / "wiki-curator-status.md").exists()

    async def test_maintenance_files_report_and_log_without_backend(
        self, paths: WikiPaths, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        def fail_backend(*args: object, **kwargs: object) -> NoReturn:
            raise AssertionError("maintenance must not load backend config")

        monkeypatch.setattr("llmwiki.cli.load_backend_config", fail_backend)
        monkeypatch.setattr("llmwiki.cli.start_backend", fail_backend)
        args = _build_parser().parse_args(["--root", str(paths.root), "maintenance"])

        result = await _run(args)

        assert result.op == "maintenance"
        assert "# Curator Status" in result.output
        assert (paths.wiki_dir / "wiki-curator-status.md").exists()
        report_page = (paths.wiki_dir / "wiki-curator-status.md").read_text(encoding="utf-8")
        assert "Deterministic curator status" in report_page
        log_text = paths.log_path.read_text(encoding="utf-8")
        assert "## [" in log_text
        assert "maintenance | curator status" in log_text

    async def test_maintenance_updates_candidate_backlog_without_creating_pages(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(_page("alpha", "Links to [[iterable]]."))
        args = _build_parser().parse_args(["--root", str(paths.root), "maintenance"])

        result = await _run(args)

        assert "iterable" in result.output
        assert (paths.wiki_dir / "wiki-candidates.json").exists()
        assert not (paths.wiki_dir / "iterable.md").exists()
        assert "iterable.md" not in paths.index_path.read_text(encoding="utf-8")

    async def test_maintenance_keeps_rejected_candidate_rejected(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(_page("alpha", "Links to [[iterable]]."))
        reject_args = _build_parser().parse_args(
            ["--root", str(paths.root), "candidates", "reject", "iterable", "--reason", "too thin"]
        )
        await _run(reject_args)
        maintenance_args = _build_parser().parse_args(["--root", str(paths.root), "maintenance"])

        await _run(maintenance_args)

        text = (paths.wiki_dir / "wiki-candidates.json").read_text(encoding="utf-8")
        assert '"status": "rejected"' in text
        assert "too thin" in text

    async def test_candidates_reject_updates_backlog_and_log(self, paths: WikiPaths) -> None:
        args = _build_parser().parse_args(
            ["--root", str(paths.root), "candidates", "reject", "maybe-page", "--reason", "nope"]
        )

        result = await _run(args)

        assert result.op == "candidates"
        assert "Rejected candidate `maybe-page`: nope" in result.output
        assert "maybe-page" in (paths.wiki_dir / "wiki-candidates.json").read_text(encoding="utf-8")
        assert "candidates | maybe-page" in paths.log_path.read_text(encoding="utf-8")

    async def test_candidates_list_is_backend_free(
        self, paths: WikiPaths, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        def fail_backend(*args: object, **kwargs: object) -> NoReturn:
            raise AssertionError("candidate listing must not load backend config")

        monkeypatch.setattr("llmwiki.cli.load_backend_config", fail_backend)
        monkeypatch.setattr("llmwiki.cli.start_backend", fail_backend)
        args = _build_parser().parse_args(["--root", str(paths.root), "candidates"])

        result = await _run(args)

        assert result.op == "candidates"
        assert (
            "No active candidate pages from explicit missing double-bracket links" in result.output
        )

    async def test_graph_writes_artifact_and_log_without_backend(
        self, store: WikiStore, paths: WikiPaths, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        def fail_backend(*args: object, **kwargs: object) -> NoReturn:
            raise AssertionError("graph export must not load backend config")

        monkeypatch.setattr("llmwiki.cli.load_backend_config", fail_backend)
        monkeypatch.setattr("llmwiki.cli.start_backend", fail_backend)
        store.write_page(_page("alpha", "See [[ghost]]."))
        args = _build_parser().parse_args(["--root", str(paths.root), "graph"])

        result = await _run(args)

        assert result.op == "graph"
        assert "Graph export: current" in result.output
        assert "Unresolved edges: 1" in result.output
        assert (paths.wiki_dir / "wiki-graph.json").exists()
        assert "graph | wiki graph" in paths.log_path.read_text(encoding="utf-8")

    async def test_pages_delete_removes_page_without_backend(
        self, store: WikiStore, paths: WikiPaths, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        def fail_backend(*args: object, **kwargs: object) -> NoReturn:
            raise AssertionError("page deletion must not load backend config")

        monkeypatch.setattr("llmwiki.cli.load_backend_config", fail_backend)
        monkeypatch.setattr("llmwiki.cli.start_backend", fail_backend)
        store.write_page(_page("scratch", "Temporary."))
        store.write_page(_page("scratch-two", "Temporary."))
        args = _build_parser().parse_args(
            ["--root", str(paths.root), "pages", "delete", "scratch", "scratch-two"]
        )

        result = await _run(args)

        assert result.op == "pages"
        assert "Deleted [[scratch]]" in result.output
        assert not (paths.wiki_dir / "scratch.md").exists()
        assert not (paths.wiki_dir / "scratch-two.md").exists()
        assert "[[scratch]]" not in paths.index_path.read_text(encoding="utf-8")
        assert "[[scratch-two]]" not in paths.index_path.read_text(encoding="utf-8")

    async def test_graph_check_detects_stale_artifact(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(_page("alpha", "See [[beta]]."))
        write_args = _build_parser().parse_args(["--root", str(paths.root), "graph"])
        await _run(write_args)
        store.write_page(_page("beta", "New page."))
        check_args = _build_parser().parse_args(["--root", str(paths.root), "graph", "--check"])

        with pytest.raises(ConfigError, match="stale"):
            await _run(check_args)

    async def test_maintenance_creates_missing_navigation_files(self, paths: WikiPaths) -> None:
        paths.index_path.unlink()
        paths.log_path.unlink()
        (paths.wiki_dir / "alpha.md").write_text(
            render_page(_page("alpha", "Standalone page.")),
            encoding="utf-8",
        )
        args = _build_parser().parse_args(["--root", str(paths.root), "maintenance"])

        result = await _run(args)

        assert "index.md: missing" in result.output
        assert paths.index_path.exists()
        assert paths.log_path.exists()
        assert "[[wiki-curator-status]]" in paths.index_path.read_text(encoding="utf-8")

    async def test_empty_contradiction_audit_does_not_start_backend(
        self, paths: WikiPaths, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        def fail_backend(*args: object, **kwargs: object) -> NoReturn:
            raise AssertionError("empty contradiction audit must not load backend config")

        monkeypatch.setattr("llmwiki.cli.load_backend_config", fail_backend)
        monkeypatch.setattr("llmwiki.cli.start_backend", fail_backend)
        args = _build_parser().parse_args(
            ["--root", str(paths.root), "--runtime", "not-needed", "contradictions"]
        )

        result = await _run(args)

        assert result.op == "contradictions"
        assert "Candidate pairs discovered: 0" in result.output
        assert (paths.wiki_dir / "wiki-contradictions.md").exists()

    async def test_empty_semantic_lint_does_not_start_backend(
        self, paths: WikiPaths, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        def fail_backend(*args: object, **kwargs: object) -> NoReturn:
            raise AssertionError("empty semantic lint must not load backend config")

        monkeypatch.setattr("llmwiki.cli.load_backend_config", fail_backend)
        monkeypatch.setattr("llmwiki.cli.start_backend", fail_backend)
        args = _build_parser().parse_args(
            ["--root", str(paths.root), "--runtime", "not-needed", "semantic-lint"]
        )

        result = await _run(args)

        assert result.op == "semantic-lint"
        assert "Candidate items discovered: 0" in result.output
        assert (paths.wiki_dir / "wiki-semantic-lint.md").exists()

    async def test_contradictions_rejects_non_positive_max_pairs(self, paths: WikiPaths) -> None:
        args = _build_parser().parse_args(
            ["--root", str(paths.root), "contradictions", "--max-pairs", "0"]
        )

        with pytest.raises(ConfigError, match="max-pairs"):
            await _run(args)

    async def test_semantic_lint_rejects_non_positive_max_items(self, paths: WikiPaths) -> None:
        args = _build_parser().parse_args(
            ["--root", str(paths.root), "semantic-lint", "--max-items", "0"]
        )

        with pytest.raises(ConfigError, match="max-items"):
            await _run(args)
