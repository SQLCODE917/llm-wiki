"""Data-in/data-out tests for the pure domain layer."""

import pytest

from llmwiki.domain.index import index_page_names, parse_index, upsert_index_entry
from llmwiki.domain.links import compute_findings, extract_links
from llmwiki.domain.log import format_log_entry
from llmwiki.domain.pages import PageError, WikiPage, parse_page, render_page
from llmwiki.domain.search import search_pages

INDEX = """# Index

## Sources

- [[alpha-source]] — about alpha

## Entities

## Concepts

- [[bravo]] — concept b
- [[delta]] — concept d

## Syntheses
"""


class TestPages:
    def test_render_parse_roundtrip(self) -> None:
        page = WikiPage(
            name="bronze-age",
            category="concept",
            summary="The Bronze Age collapse.",
            body="Linked to [[sea-peoples]].\n\nEvidence: (raw/article.md)",
            sources=("article.md",),
            updated="2026-06-10",
        )
        assert parse_page("bronze-age", render_page(page)) == page

    @pytest.mark.parametrize("name", ["Bad Name", "UPPER", "trailing-", "-leading", "a--b", ""])
    def test_invalid_names_rejected(self, name: str) -> None:
        with pytest.raises(PageError):
            WikiPage(name=name, category="entity", summary="s", body="b")

    def test_invalid_category_rejected(self) -> None:
        with pytest.raises(PageError):
            WikiPage(name="ok", category="article", summary="s", body="b")

    def test_summary_collapsed_to_one_line(self) -> None:
        with pytest.raises(PageError):
            WikiPage(name="ok", category="entity", summary="  \n ", body="b")


class TestIndex:
    def test_parse_extracts_entries_with_categories(self) -> None:
        entries = parse_index(INDEX)
        assert [(e.name, e.category) for e in entries] == [
            ("alpha-source", "source"),
            ("bravo", "concept"),
            ("delta", "concept"),
        ]

    def test_upsert_inserts_sorted_within_category(self) -> None:
        updated = upsert_index_entry(INDEX, "charlie", "concept", "concept c")
        names = [e.name for e in parse_index(updated) if e.category == "concept"]
        assert names == ["bravo", "charlie", "delta"]

    def test_upsert_replaces_existing_entry(self) -> None:
        updated = upsert_index_entry(INDEX, "bravo", "concept", "new summary")
        entries = {e.name: e.summary for e in parse_index(updated)}
        assert entries["bravo"] == "new summary"
        assert len([e for e in parse_index(updated) if e.name == "bravo"]) == 1

    def test_upsert_moves_page_between_categories(self) -> None:
        updated = upsert_index_entry(INDEX, "bravo", "synthesis", "now a synthesis")
        entries = {e.name: e.category for e in parse_index(updated)}
        assert entries["bravo"] == "synthesis"

    def test_upsert_into_empty_category(self) -> None:
        updated = upsert_index_entry(INDEX, "ada", "entity", "a person")
        assert ("ada", "entity") in [(e.name, e.category) for e in parse_index(updated)]

    def test_index_page_names(self) -> None:
        assert index_page_names(INDEX) == {"alpha-source", "bravo", "delta"}


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
        assert extract_links("See [[alpha]] and [[beta-2]]. Not [link].") == {"alpha", "beta-2"}

    def test_findings_detect_all_issue_kinds(self) -> None:
        pages = {
            "alpha": "links to [[beta]] and [[ghost]]",
            "beta": "no links here",
            "gamma": "links to [[alpha]]",
        }
        findings = compute_findings(pages, index_names={"alpha", "beta", "zombie"})
        assert findings.broken_links == {"alpha": ("ghost",)}
        assert findings.orphan_pages == ("gamma",)
        assert findings.missing_from_index == ("gamma",)
        assert findings.stale_index_entries == ("zombie",)
        assert not findings.is_clean
        assert "ghost" in findings.render()

    def test_clean_wiki_is_clean(self) -> None:
        pages = {"alpha": "see [[beta]]", "beta": "see [[alpha]]"}
        findings = compute_findings(pages, index_names={"alpha", "beta"})
        assert findings.is_clean

    def test_single_page_is_not_an_orphan(self) -> None:
        findings = compute_findings({"only": "text"}, index_names={"only"})
        assert findings.orphan_pages == ()


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

    def test_snippet_contains_context(self) -> None:
        hits = search_pages(self.PAGES, "hittites")
        assert "Hittites" in hits[0].snippet
