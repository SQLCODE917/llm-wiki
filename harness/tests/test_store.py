"""WikiStore boundary tests: confinement, immutability, index coupling."""

import json

import pytest

from llmwiki.config import SOURCE_READ_BUDGET_CHARS, WikiPaths
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.store import PageNotFoundError, SourceNotFoundError, WikiStore, WikiStoreError


def _page(
    name: str = "hittites",
    category: str = "entity",
    *,
    summary: str | None = None,
    body: str | None = None,
    sources: tuple[str, ...] = ("article.md",),
    updated: str = "2026-06-10",
) -> WikiPage:
    return WikiPage(
        page_metadata=PageMetadata(
            page_id=name,
            page_kind=category,
            summary=summary or f"About {name}.",
            sources=sources,
            updated=updated,
        ),
        page_body=body or f"The {name} page. See [[other]].",
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

    def test_raw_source_uses_source_locator(self, paths: WikiPaths, store: WikiStore) -> None:
        (paths.raw_dir / "article.md").write_text("Source text.", encoding="utf-8")

        raw_source = store.raw_source("article.md")

        assert raw_source.source_locator == "article.md"
        assert raw_source.source_format == "markdown"
        assert raw_source.immutable is True


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
                page_metadata=PageMetadata(
                    page_id="hittites",
                    page_kind="entity",
                    summary="Updated summary.",
                    updated="2026-06-11",
                ),
                page_body="New body.",
            )
        )
        assert store.read_index().count("[[hittites]]") == 1
        assert "Updated summary." in store.read_index()
        assert "New body." in store.read_page("hittites")
        assert "page_id: hittites" in store.read_page("hittites")
        assert "page_kind: entity" in store.read_page("hittites")
        assert "category:" not in store.read_page("hittites")

    def test_reserved_names_rejected(self, store: WikiStore) -> None:
        with pytest.raises(WikiStoreError, match="reserved"):
            store.write_page(_page(name="index", category="concept"))

    def test_read_missing_page(self, store: WikiStore) -> None:
        with pytest.raises(PageNotFoundError):
            store.read_page("nope")

    def test_index_and_log_not_listed_as_pages(self, store: WikiStore) -> None:
        assert store.list_pages() == []

    def test_rename_page_rewrites_inbound_links_and_index(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(_page(name="wraith"))
        store.write_page(
            _page(
                "hub",
                "source",
                summary="Hub.",
                body="See [[wraith]] and [[wraith|old label]].",
            )
        )

        store.rename_page("wraith", "wraith-form", summary="Spell effect.", today="2026-06-16")

        assert not (paths.wiki_dir / "wraith.md").exists()
        assert (paths.wiki_dir / "wraith-form.md").exists()
        assert "[[wraith-form]]" in store.read_index()
        assert "[[wraith]]" not in store.read_index()
        hub = store.read_page("hub")
        assert "[[wraith-form]]" in hub
        assert "[[wraith-form|old label]]" in hub

    def test_merge_page_removes_old_page_and_preserves_target(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(
            _page(
                "daemons",
                "entity",
                summary="Plural target.",
                body="Target body.",
                sources=("raw/book.pdf p.1",),
            )
        )
        store.write_page(
            _page(
                "daemon",
                "entity",
                summary="Duplicate drift.",
                body="Duplicate body.",
                sources=("raw/book.pdf p.2",),
                updated="2026-06-11",
            )
        )
        store.write_page(_page("hub", "source", summary="Hub.", body="See [[daemon]]."))

        store.merge_page("daemon", "daemons", summary="Merged daemon type.", today="2026-06-16")

        assert not (paths.wiki_dir / "daemon.md").exists()
        target = store.read_page("daemons")
        assert "Target body." in target
        assert "Duplicate body." not in target
        assert "raw/book.pdf p.1" in target
        assert "raw/book.pdf p.2" in target
        assert "[[daemons]]" in store.read_page("hub")

    def test_delete_page_removes_file_and_index_entry(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(_page("draft-page", "source", summary="Draft.", body="Temporary."))

        store.delete_page("draft-page")

        assert not (paths.wiki_dir / "draft-page.md").exists()
        assert "draft-page" not in store.list_pages()
        assert "[[draft-page]]" not in store.read_index()

    def test_delete_source_pages_not_in_removes_page_range_source_pages(
        self, store: WikiStore
    ) -> None:
        store.write_page(
            WikiPage.from_metadata(
                PageMetadata(
                    page_id="book-stale-range",
                    page_kind="source",
                    summary="Old chunk page.",
                    sources=("raw/book.pdf p.1-10",),
                    updated="2026-06-10",
                ),
                "Old chunk page.",
            )
        )
        store.write_page(
            WikiPage.from_metadata(
                PageMetadata(
                    page_id="book-stale-source-id",
                    page_kind="source",
                    summary="Old source page.",
                    sources=("raw/book.pdf p.11-20",),
                    updated="2026-06-10",
                    source_id="book.pdf",
                ),
                "Old source page.",
            )
        )
        store.write_page(
            WikiPage.from_metadata(
                PageMetadata(
                    page_id="book-keep",
                    page_kind="source",
                    summary="Current source page.",
                    sources=("raw/book.pdf",),
                    updated="2026-06-11",
                ),
                "Current source page.",
            )
        )
        store.write_page(
            WikiPage.from_metadata(
                PageMetadata(
                    page_id="book-cross-source",
                    page_kind="synthesis",
                    summary="Cross-source page.",
                    sources=("raw/book.pdf", "raw/other.pdf"),
                    updated="2026-06-11",
                ),
                "Cross-source page.",
            )
        )

        removed = store.delete_source_pages_not_in("book.pdf", {"book-keep"})

        assert removed == ("book-stale-range", "book-stale-source-id")
        assert store.list_pages() == ["book-cross-source", "book-keep"]
        assert "[[book-stale-range]]" not in store.read_index()
        assert "[[book-stale-source-id]]" not in store.read_index()

    def test_replace_page_link_preserves_alias_and_rewrites_index(self, store: WikiStore) -> None:
        store.write_page(_page(name="new-target"))
        store.write_page(
            _page(
                "hub",
                "source",
                summary="Hub.",
                body="See [[old-target]] and [[old-target|old label]].",
            )
        )

        store.replace_page_link("hub", "old-target", "new-target", today="2026-06-16")

        hub = store.read_page("hub")
        assert "[[new-target]]" in hub
        assert "[[new-target|old label]]" in hub
        assert "[[old-target]]" not in hub
        assert "updated: 2026-06-16" in hub

    def test_replace_page_link_can_add_alias(self, store: WikiStore) -> None:
        store.write_page(_page(name="new-target"))
        store.write_page(_page("hub", "source", summary="Hub.", body="See [[old-target]]."))

        store.replace_page_link("hub", "old-target", "new-target", alias="old label")

        assert "[[new-target|old label]]" in store.read_page("hub")


class TestLog:
    def test_append_log_is_append_only(self, store: WikiStore, paths: WikiPaths) -> None:
        before = paths.log_path.read_text(encoding="utf-8")
        store.append_log("2026-06-10", "ingest", "article.md", "Wrote pages.")
        after = paths.log_path.read_text(encoding="utf-8")
        assert after.startswith(before)
        assert "## [2026-06-10] ingest | article.md" in after
