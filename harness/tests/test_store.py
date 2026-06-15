"""WikiStore boundary tests: confinement, immutability, index coupling."""

import json

import pytest

from llmwiki.config import SOURCE_READ_BUDGET_CHARS, WikiPaths
from llmwiki.domain.pages import WikiPage
from llmwiki.store import PageNotFoundError, SourceNotFoundError, WikiStore, WikiStoreError


def _page(name: str = "hittites", category: str = "entity") -> WikiPage:
    return WikiPage(
        name=name,
        category=category,
        summary=f"About {name}.",
        body=f"The {name} page. See [[other]].",
        sources=("article.md",),
        updated="2026-06-10",
    )


class TestRawLayer:
    def test_read_source(self, paths: WikiPaths, store: WikiStore) -> None:
        (paths.raw_dir / "article.md").write_text("Source text.", encoding="utf-8")
        assert store.read_source("article.md") == "Source text."

    def test_traversal_outside_raw_rejected(self, paths: WikiPaths, store: WikiStore) -> None:
        (paths.root / "secret.md").write_text("nope", encoding="utf-8")
        with pytest.raises(SourceNotFoundError):
            store.read_source("../secret.md")

    def test_missing_source_lists_available(self, paths: WikiPaths, store: WikiStore) -> None:
        (paths.raw_dir / "exists.md").write_text("x", encoding="utf-8")
        with pytest.raises(SourceNotFoundError, match="exists.md"):
            store.read_source("missing.md")

    def test_source_inventory_lists_raw_citation_paths(
        self, paths: WikiPaths, store: WikiStore
    ) -> None:
        (paths.raw_dir / "exists.md").write_text("x", encoding="utf-8")
        (paths.raw_dir / "nested").mkdir()
        (paths.raw_dir / "nested" / "book.pdf").write_bytes(b"%PDF")
        inventory = store.source_inventory()
        assert inventory.source_paths == frozenset({"raw/exists.md", "raw/nested/book.pdf"})

    def test_oversized_source_truncated_with_marker(
        self, paths: WikiPaths, store: WikiStore
    ) -> None:
        (paths.raw_dir / "big.md").write_text("x" * (SOURCE_READ_BUDGET_CHARS + 100))
        text = store.read_source("big.md")
        assert "[TRUNCATED" in text
        assert len(text) < SOURCE_READ_BUDGET_CHARS + 200

    def test_source_resolver_reads_cached_pdf_chunks(
        self, paths: WikiPaths, store: WikiStore
    ) -> None:
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF")
        cache_dir = paths.cache_dir / "abc123"
        chunks_dir = cache_dir / "chunks"
        chunks_dir.mkdir(parents=True)
        (cache_dir / "manifest.json").write_text(
            json.dumps({"source": "book.pdf"}),
            encoding="utf-8",
        )
        (chunks_dir / "0001.md").write_text("Line one.\nLine two.", encoding="utf-8")

        assert store.source_resolver().source_lines("raw/book.pdf") == (
            "Line one.",
            "Line two.",
        )


class TestWikiLayer:
    def test_write_page_creates_file_and_index_entry(
        self, paths: WikiPaths, store: WikiStore
    ) -> None:
        store.write_page(_page())
        assert (paths.wiki_dir / "hittites.md").exists()
        assert "- [[hittites]] — About hittites." in store.read_index()
        assert store.list_pages() == ["hittites"]

    def test_rewrite_updates_in_place(self, store: WikiStore) -> None:
        store.write_page(_page())
        store.write_page(
            WikiPage(
                name="hittites",
                category="entity",
                summary="Updated summary.",
                body="New body.",
                updated="2026-06-11",
            )
        )
        assert store.read_index().count("[[hittites]]") == 1
        assert "Updated summary." in store.read_index()
        assert "New body." in store.read_page("hittites")

    def test_reserved_names_rejected(self, store: WikiStore) -> None:
        with pytest.raises(WikiStoreError, match="reserved"):
            store.write_page(_page(name="index", category="concept"))

    def test_read_missing_page(self, store: WikiStore) -> None:
        with pytest.raises(PageNotFoundError):
            store.read_page("nope")

    def test_index_and_log_not_listed_as_pages(self, store: WikiStore) -> None:
        assert store.list_pages() == []


class TestLog:
    def test_append_log_is_append_only(self, store: WikiStore, paths: WikiPaths) -> None:
        before = paths.log_path.read_text(encoding="utf-8")
        store.append_log("2026-06-10", "ingest", "article.md", "Wrote pages.")
        after = paths.log_path.read_text(encoding="utf-8")
        assert after.startswith(before)
        assert "## [2026-06-10] ingest | article.md" in after
