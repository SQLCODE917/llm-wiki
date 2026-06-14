"""Curator-status and maintenance tests: deterministic, model-free health checks."""

from typing import NoReturn

import pytest

from llmwiki.cli import _build_parser, _curator_report, _run
from llmwiki.config import WikiPaths
from llmwiki.domain.index import empty_index
from llmwiki.domain.pages import WikiPage, render_page
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
        name=name,
        category=category,
        summary=summary or f"{name} summary.",
        body=body,
        sources=sources,
        updated=TODAY,
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
