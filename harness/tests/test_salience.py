"""Deterministic salience v2: scoping, hub exclusion, mentions, ranking,
and harness-owned key-list reconciliation."""

from llmwiki.domain.pages import PageMetadata, WikiPage, render_page
from llmwiki.domain.salience import compute_salience, reconcile_key_lists


def _page(name: str, category: str, body: str, sources: tuple[str, ...] = ()) -> str:
    return render_page(
        WikiPage(
            page_metadata=PageMetadata(
                page_id=name,
                page_kind=category,
                summary=f"About {name}.",
                sources=sources,
            ),
            page_body=body,
        )
    )


BOOK = ("iterable protocol " * 60) + ("generator " * 20) + "by matthew knox. leanpub edition."
SRC = ("raw/book.pdf",)


def _measured_failure_wiki() -> dict[str, str]:
    """The hub-review #2 shape: foreword people + platform vs the book's
    center of mass, plus a hub that links everything (open question #12)."""
    return {
        "book": _page(
            "book",
            "source",
            "Hub linking [[matthew-knox]], [[leanpub]], [[iterable]], [[generator]].",
            SRC,
        ),
        "matthew-knox": _page("matthew-knox", "entity", "Foreword author.", SRC),
        "leanpub": _page("leanpub", "concept", "A publishing platform.", SRC),
        "iterable": _page("iterable", "concept", "Core protocol.", SRC),
        "generator": _page("generator", "entity", "Produces [[iterable]]s lazily.", SRC),
        "antikythera": _page("antikythera", "entity", "Other source entity.", ("raw/other.md",)),
        "wiki-health": _page("wiki-health", "synthesis", "Report citing [[leanpub]].", SRC),
    }


class TestMetricV2:
    def _report(self):  # noqa: ANN202
        return compute_salience(
            _measured_failure_wiki(),
            write_counts={"matthew-knox": 1, "leanpub": 2, "iterable": 2, "generator": 1},
            source_text=BOOK,
            scope_source="book.pdf",
            exclude_inbound_from=frozenset({"book"}),
        )

    def test_mentions_outrank_foreword_trivia(self) -> None:
        report = self._report()
        assert [e.name for e in report.top("concept")] == ["iterable", "leanpub"]
        iterable = report.top("concept")[0]
        assert iterable.source_mentions == 60
        # leanpub: 1 mention, hub link excluded -> low score despite 2 writes
        assert report.top("concept")[1].score < iterable.score / 2

    def test_hub_links_do_not_feed_the_ranking(self) -> None:
        report = self._report()
        knox = next(e for e in report.entries if e.name == "matthew-knox")
        assert knox.inbound_links == 0  # only the excluded hub links him
        generator = next(e for e in report.entries if e.name == "generator")
        assert [e.name for e in report.top("entity")] == ["generator", "matthew-knox"]
        assert generator.score > knox.score

    def test_harness_report_links_do_not_feed_the_ranking(self) -> None:
        report = self._report()
        leanpub = next(e for e in report.entries if e.name == "leanpub")
        assert leanpub.inbound_links == 0  # wiki-health is a report, not wiki evidence

    def test_scope_excludes_other_sources(self) -> None:
        ranked = {e.name for e in self._report().entries}
        assert "antikythera" not in ranked

    def test_unscoped_is_wiki_global(self) -> None:
        ranked = {e.name for e in compute_salience(_measured_failure_wiki()).entries}
        assert "antikythera" in ranked


class TestMentionCounting:
    def test_word_boundaries_prevent_substring_hits(self) -> None:
        pages = {"nan": _page("nan", "entity", "Not a number.", SRC)}
        report = compute_salience(
            pages, source_text="banana nanny nan banana", scope_source="book.pdf"
        )
        assert report.entries[0].source_mentions == 1

    def test_plural_slug_matches_singular_text(self) -> None:
        pages = {"linked-lists": _page("linked-lists", "concept", "x", SRC)}
        report = compute_salience(
            pages,
            source_text="a linked list, two linked lists, one linked-list",
            scope_source="book.pdf",
        )
        assert report.entries[0].source_mentions == 3

    def test_no_source_text_means_zero_mentions(self) -> None:
        pages = {"alpha": _page("alpha", "concept", "x", SRC)}
        assert compute_salience(pages).entries[0].source_mentions == 0


class TestRender:
    def test_render_shows_labeled_counts_in_rank_order(self) -> None:
        block = compute_salience(
            _measured_failure_wiki(),
            source_text=BOOK,
            scope_source="book.pdf",
            exclude_inbound_from=frozenset({"book"}),
        ).render()
        assert "[[iterable]] (links 1, writes 0, mentions 60)" in block
        assert block.index("[[iterable]]") < block.index("[[leanpub]]")
        assert "Concepts:" in block and "Entities:" in block

    def test_empty_wiki_renders_empty(self) -> None:
        assert compute_salience({}).render() == ""

    def test_top_n_caps_each_category(self) -> None:
        pages = {f"c-{i:02d}": _page(f"c-{i:02d}", "concept", "x") for i in range(12)}
        assert compute_salience(pages).render().count("[[") == 8

    def test_self_links_do_not_count(self) -> None:
        pages = {"navel": _page("navel", "concept", "See [[navel]].")}
        assert compute_salience(pages).entries[0].inbound_links == 0


class TestReconcileKeyLists:
    def _report(self):  # noqa: ANN202
        return compute_salience(
            _measured_failure_wiki(),
            source_text=BOOK,
            scope_source="book.pdf",
            exclude_inbound_from=frozenset({"book"}),
        )

    def test_model_written_lists_are_replaced_not_merged(self) -> None:
        body = (
            "Hub prose stays.\n\n"
            "**Key entities**: [[matthew-knox]], [[leanpub]].\n"
            "Key concepts: [[leanpub]], [[lexical-scoping]]\n"
        )
        out = reconcile_key_lists(body, self._report())
        assert "Hub prose stays." in out
        assert "[[matthew-knox]]" not in out  # 2 mentions: under the floor
        # Reader-facing labels only — no "computed from salience" plumbing.
        assert "**Key concepts:** [[iterable]]" in out
        # generator: 20 mentions, only entity above the floor
        assert "**Key entities:** [[generator]]" in out
        assert "salience" not in out
        assert out.count("ey entities") == 1 and out.count("ey concepts") == 1

    def test_idempotent(self) -> None:
        once = reconcile_key_lists("Prose.", self._report())
        assert reconcile_key_lists(once, self._report()) == once

    def test_mentions_floor_keeps_trivia_off_key_lists(self) -> None:
        report = self._report()
        keys = {e.name for c in ("concept", "entity") for e in report.key_pages(c)}
        assert keys == {"iterable", "generator"}  # leanpub (1 mention) is out
        # ...even though leanpub still appears in the report shown to the model
        assert any(e.name == "leanpub" for e in report.top("concept"))

    def test_empty_report_strips_and_adds_nothing(self) -> None:
        body = "Prose.\n**Key entities**: [[stale]]."
        out = reconcile_key_lists(body, compute_salience({}))
        assert out == "Prose."
