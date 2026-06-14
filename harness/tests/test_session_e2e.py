"""End-to-end operation tests: real WorkflowRunner + real store, fake LLM.

These map to the design doc's key interactions — ingest, query, lint —
and exercise the guardrail wiring (required steps, prerequisites) that the
harness declares on each workflow.
"""

import pytest
from fakes import FakeClient
from forge.context import ContextManager, NoCompact
from forge.core.workflow import TextResponse, ToolCall

from llmwiki.config import WikiPaths
from llmwiki.domain.pages import WikiPage
from llmwiki.runtime.session import Session
from llmwiki.store import WikiStore

TODAY = "2026-06-10"


def _session(store: WikiStore, script: list, paths: WikiPaths) -> Session:
    return Session(
        store=store,
        client=FakeClient(script),
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        today=TODAY,
        runs_dir=paths.root / "runs",
        run_id="test-run",
    )


@pytest.fixture
def source(paths: WikiPaths) -> str:
    (paths.raw_dir / "moon.md").write_text(
        "The Moon formed ~4.5 billion years ago from a giant impact.", encoding="utf-8"
    )
    return "moon.md"


class TestIngest:
    async def test_happy_path_updates_all_layers(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        script = [
            [ToolCall(tool="read_source", args={"path": "moon.md"})],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "name": "moon",
                        "category": "source",
                        "summary": "Notes on lunar formation.",
                        "content": "Giant impact origin. See [[giant-impact]]. (raw/moon.md)",
                        "sources": ["moon.md"],
                    },
                )
            ],
            [ToolCall(tool="finish_ingest", args={"report": "Wrote [[moon]]."})],
        ]
        result = await _session(store, script, paths).ingest(source)

        assert result.output == "Wrote [[moon]]."
        assert "Giant impact origin" in store.read_page("moon")
        assert "- [[moon]] — Notes on lunar formation." in store.read_index()
        log = paths.log_path.read_text(encoding="utf-8")
        assert f"## [{TODAY}] ingest | moon.md" in log
        assert result.transcript_path is not None and result.transcript_path.exists()

    async def test_premature_finish_is_blocked_then_recovers(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        # Turn 1 tries to finish before reading/writing: StepEnforcer must
        # block it (tool-error nudge), and the workflow still completes.
        script = [
            [ToolCall(tool="finish_ingest", args={"report": "done!"})],
            [ToolCall(tool="read_source", args={"path": "moon.md"})],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "name": "moon",
                        "category": "source",
                        "summary": "Lunar notes.",
                        "content": "Body. (raw/moon.md)",
                    },
                )
            ],
            [ToolCall(tool="finish_ingest", args={"report": "Wrote [[moon]]."})],
        ]
        result = await _session(store, script, paths).ingest(source)
        assert result.output == "Wrote [[moon]]."
        assert "moon" in store.list_pages()

    async def test_write_page_requires_prior_read_source(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        # write_page before read_source violates the prerequisite; forge
        # nudges and the scripted model self-corrects.
        script = [
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "name": "moon",
                        "category": "source",
                        "summary": "Lunar notes.",
                        "content": "Body.",
                    },
                )
            ],
            [ToolCall(tool="read_source", args={"path": "moon.md"})],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "name": "moon",
                        "category": "source",
                        "summary": "Lunar notes.",
                        "content": "Body. (raw/moon.md)",
                    },
                )
            ],
            [ToolCall(tool="finish_ingest", args={"report": "ok"})],
        ]
        await _session(store, script, paths).ingest(source)
        # The blocked first write must not have touched the wiki layer.
        assert store.read_index().count("[[moon]]") == 1

    async def test_bad_tool_args_fed_back_for_self_correction(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        script = [
            [ToolCall(tool="read_source", args={"path": "moon.md"})],
            [
                ToolCall(  # invalid category — tool error, model retries
                    tool="write_page",
                    args={"name": "moon", "category": "article", "summary": "s", "content": "b"},
                )
            ],
            [
                ToolCall(
                    tool="write_page",
                    args={"name": "moon", "category": "source", "summary": "s", "content": "b"},
                )
            ],
            [ToolCall(tool="finish_ingest", args={"report": "ok"})],
        ]
        result = await _session(store, script, paths).ingest(source)
        assert result.output == "ok"
        assert store.list_pages() == ["moon"]

    async def test_rewrite_without_read_is_blocked_then_recovers(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        # write_page replaces the whole page; rewriting one the model never
        # read this run must fail with a corrective error (open question #10),
        # and succeed after read_page.
        store.write_page(
            WikiPage(
                name="moon",
                category="source",
                summary="Original.",
                body="Original rich body with [[links]].",
                updated=TODAY,
            )
        )
        script = [
            [ToolCall(tool="read_source", args={"path": "moon.md"})],
            [
                ToolCall(  # blind rewrite — must be rejected
                    tool="write_page",
                    args={"name": "moon", "category": "source", "summary": "thin", "content": "x"},
                )
            ],
            [ToolCall(tool="read_page", args={"name": "moon"})],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "name": "moon",
                        "category": "source",
                        "summary": "Updated.",
                        "content": "Original rich body with [[links]]. Plus new facts.",
                    },
                )
            ],
            [ToolCall(tool="finish_ingest", args={"report": "updated moon"})],
        ]
        result = await _session(store, script, paths).ingest(source)
        assert result.output == "updated moon"
        body = store.read_page("moon")
        assert "Plus new facts" in body
        # The blind rewrite never landed:
        assert "thin" not in store.read_index()

    async def test_pipeline_markers_stripped_from_written_pages(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        # The OCR caveat tag is extraction plumbing; observed quoted verbatim
        # into a wiki page despite the schema — stripped at the boundary now.
        script = [
            [ToolCall(tool="read_source", args={"path": "moon.md"})],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "name": "moon",
                        "category": "source",
                        "summary": "Lunar notes.",
                        "content": "Real claim.\n\n"
                        "[figure text (OCR, unverified): NOISE ON A MUG]\n\n"
                        "Another claim.",
                    },
                )
            ],
            [ToolCall(tool="finish_ingest", args={"report": "ok"})],
        ]
        await _session(store, script, paths).ingest(source)
        body = store.read_page("moon")
        assert "Real claim." in body and "Another claim." in body
        assert "OCR" not in body and "NOISE" not in body

    async def test_bare_text_after_work_nudged_to_terminal_tool(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        # The observed live failure mode: the model finishes its page writes,
        # then "reports" in bare text instead of calling finish_ingest. The
        # retry nudge must name the terminal tool and the run must recover.
        script = [
            [ToolCall(tool="read_source", args={"path": "moon.md"})],
            [
                ToolCall(
                    tool="write_page",
                    args={"name": "moon", "category": "source", "summary": "s", "content": "b"},
                )
            ],
            TextResponse(content="I have finished ingesting the source."),
            [ToolCall(tool="finish_ingest", args={"report": "Wrote [[moon]]."})],
        ]
        session = _session(store, script, paths)
        result = await session.ingest(source)
        assert result.output == "Wrote [[moon]]."
        fake: FakeClient = session.client
        # The turn after the bare text must carry the terminal-tool hint.
        last_turn = fake.sent[-1]
        nudges = [m["content"] for m in last_turn if m.get("role") == "user"]
        assert any("finish_ingest" in content for content in nudges)


class TestQuery:
    async def test_search_then_respond_and_logged(self, store: WikiStore, paths: WikiPaths) -> None:
        store.write_page(
            WikiPage(
                name="moon",
                category="source",
                summary="Lunar notes.",
                body="Giant impact formed the Moon.",
                updated=TODAY,
            )
        )
        script = [
            [ToolCall(tool="search_wiki", args={"query": "moon formation"})],
            [ToolCall(tool="respond", args={"message": "A giant impact — see [[moon]]."})],
        ]
        result = await _session(store, script, paths).query("How did the Moon form?")
        assert result.output == "A giant impact — see [[moon]]."
        assert f"## [{TODAY}] query | How did the Moon form?" in paths.log_path.read_text()


class TestLint:
    async def test_empty_wiki_short_circuits_without_llm(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        result = await _session(store, [], paths).lint()
        assert "empty" in result.output.lower()
        assert f"## [{TODAY}] lint | empty wiki" in paths.log_path.read_text()

    async def test_lint_files_report_page_and_log(self, store: WikiStore, paths: WikiPaths) -> None:
        store.write_page(
            WikiPage(
                name="alpha",
                category="concept",
                summary="A.",
                body="Links to [[ghost]].",
                updated=TODAY,
            )
        )
        script = [
            [ToolCall(tool="read_page", args={"name": "alpha"})],
            [ToolCall(tool="finish_lint", args={"report": "ghost link is broken."})],
        ]
        session = _session(store, script, paths)
        result = await session.lint()
        assert result.output == "ghost link is broken."
        assert "wiki-health" in store.list_pages()
        assert f"## [{TODAY}] lint | wiki health" in paths.log_path.read_text()
        # The deterministic findings reached the model in the user message.
        fake: FakeClient = session.client
        first_turn = fake.sent[0]
        user_msgs = [m["content"] for m in first_turn if m.get("role") == "user"]
        assert any("ghost" in content for content in user_msgs)

    async def test_health_page_is_not_reported_as_orphan(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        # A prior lint filed wiki-health; the next lint must not flag it.
        store.write_page(
            WikiPage(name="alpha", category="concept", summary="A.", body="[[beta]]", updated=TODAY)
        )
        store.write_page(
            WikiPage(name="beta", category="concept", summary="B.", body="[[alpha]]", updated=TODAY)
        )
        store.write_page(
            WikiPage(
                name="wiki-health",
                category="synthesis",
                summary="Old report.",
                body="All clean.",
                updated=TODAY,
            )
        )
        script = [
            [ToolCall(tool="read_page", args={"name": "alpha"})],
            [ToolCall(tool="finish_lint", args={"report": "Still clean."})],
        ]
        session = _session(store, script, paths)
        await session.lint()
        fake: FakeClient = session.client
        user_msgs = [m["content"] for m in fake.sent[0] if m.get("role") == "user"]
        assert not any("Orphan" in content for content in user_msgs)
