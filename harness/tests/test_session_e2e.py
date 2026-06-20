"""End-to-end operation tests: real WorkflowRunner + real store, fake LLM.

These map to the design doc's key interactions — ingest, query, lint —
and exercise the guardrail wiring (required steps, prerequisites) that the
harness declares on each workflow.
"""

import pytest
from fakes import FakeClient
from forge.context import ContextManager, NoCompact
from forge.core.workflow import TextResponse, ToolCall
from helpers import wiki_page

from llmwiki.config import WikiPaths
from llmwiki.domain.contradictions import select_contradiction_candidates
from llmwiki.domain.evidence import EvidencePolicy
from llmwiki.domain.grounding import GroundingSelection, select_grounding_claims
from llmwiki.domain.ingest_route_history import ingest_route_plan_records_from_jsonl
from llmwiki.domain.ingest_route_plan import (
    IngestRouteContext,
    IngestRoutePlan,
    IngestRoutePlanState,
    PlannedPage,
)
from llmwiki.domain.semantic_lint import SemanticLintSelection, select_semantic_lint_candidates
from llmwiki.runtime.session import Session
from llmwiki.store import PageNotFoundError, WikiStore, WikiStoreError
from llmwiki.workflows.tools import write_page_tool

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


def _plan_page_call(
    name: str,
    *,
    category: str = "source",
    summary: str = "Lunar notes.",
    action: str = "create",
    source_scope: str = "moon.md",
    sources: tuple[str, ...] = ("moon.md",),
    gaps: list[dict[str, str]] | None = None,
) -> ToolCall:
    return ToolCall(
        tool="plan_pages",
        args={
            "planned_pages": [
                {
                    "metadata": {
                        "page_id": name,
                        "page_kind": category,
                        "summary": summary,
                        "sources": list(sources),
                    },
                    "role": "primary page for this source",
                    "action": action,
                    "source_scope": source_scope,
                    "confidence": "high",
                    "rationale": f"{name} is the durable wiki target for this ingest.",
                }
            ],
            "gaps": gaps or [],
        },
    )


def _source_summary_write_args(
    *,
    page_id: str = "moon",
    summary: str = "Lunar notes.",
    source_locator: str = "moon.md",
    source_claim_id: str = "source-claim-unit-0001-0001",
    record_text: str = "Source record for [[moon]].",
    claim_text: str = "The source supports a lunar formation claim.",
) -> dict[str, object]:
    citation = f"raw/{source_locator}"
    return {
        "page_id": page_id,
        "page_kind": "source",
        "summary": summary,
        "source_record_text": f"{record_text} ({citation})",
        "claim_bullets": [
            {
                "bullet_text": f"{claim_text} ({citation})",
                "covered_source_claims": [source_claim_id],
            },
            {
                "bullet_text": f"The same source claim is restated compactly. ({citation})",
                "covered_source_claims": [source_claim_id],
            },
            {
                "bullet_text": f"The summary preserves the source coverage target. ({citation})",
                "covered_source_claims": [source_claim_id],
            },
        ],
        "sources": [source_locator],
    }


class TestIngest:
    def test_ingest_run_uses_raw_source_boundary(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        ingest_run = _session(store, [], paths)._ingest_run(source)

        assert ingest_run.source_bundle.raw_sources[0].source_locator == "moon.md"
        assert ingest_run.source_bundle.raw_sources[0].source_format == "markdown"
        assert ingest_run.wiki_structure.structure_id == "local-flat"

    async def test_happy_path_updates_all_layers(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        script = [
            [ToolCall(tool="read_source", args={"source_locator": "moon.md"})],
            [ToolCall(tool="search_wiki", args={"query": "moon lunar formation"})],
            [_plan_page_call("moon", summary="Notes on lunar formation.")],
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_write_args(
                        summary="Notes on lunar formation.",
                        claim_text="The Moon source supports a giant impact origin claim.",
                    ),
                )
            ],
            [ToolCall(tool="finish_ingest", args={"report": "Wrote [[moon]]."})],
        ]
        result = await _session(store, script, paths).ingest(source)

        assert result.output == "Wrote [[moon]]."
        assert "giant impact origin" in store.read_page("moon")
        assert "- [[moon]] — Notes on lunar formation." in store.read_index()
        log = paths.log_path.read_text(encoding="utf-8")
        assert f"## [{TODAY}] ingest | moon.md" in log
        assert result.transcript_path is not None and result.transcript_path.exists()
        route_records = ingest_route_plan_records_from_jsonl(
            paths.route_plan_history_path.read_text(encoding="utf-8")
        )
        assert len(route_records) == 1
        assert route_records[0].source_locator == "moon.md"
        assert route_records[0].planned_page_ids == ("moon",)
        assert route_records[0].page_writes == ("moon",)
        assert route_records[0].route_gap_count == 0
        draft_path = (
            store.page_plan_artifact_dir("moon.md")
            / "accepted-source-summaries"
            / "write-moon.json"
        )
        assert draft_path.exists()
        assert "source-claim-unit-0001-0001" in draft_path.read_text(encoding="utf-8")
        assert "source-claim-unit" not in store.read_page("moon")

    async def test_markdown_route_plan_gaps_are_persisted(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        gaps = [
            {
                "reason": "too-granular",
                "source_scope": "moon.md",
                "summary": "Minor aside stayed inside the source page.",
            }
        ]
        script = [
            [ToolCall(tool="read_source", args={"source_locator": "moon.md"})],
            [ToolCall(tool="search_wiki", args={"query": "moon"})],
            [_plan_page_call("moon", gaps=gaps)],
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_write_args(),
                )
            ],
            [ToolCall(tool="finish_ingest", args={"report": "ok"})],
        ]

        await _session(store, script, paths).ingest(source)

        route_records = ingest_route_plan_records_from_jsonl(
            paths.route_plan_history_path.read_text(encoding="utf-8")
        )
        assert route_records[0].route_gap_count == 1
        assert route_records[0].route_gap_summaries == (
            "Minor aside stayed inside the source page.",
        )

    async def test_premature_finish_is_blocked_then_recovers(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        # Turn 1 tries to finish before reading/writing: StepEnforcer must
        # block it (tool-error nudge), and the workflow still completes.
        script = [
            [ToolCall(tool="finish_ingest", args={"report": "done!"})],
            [ToolCall(tool="read_source", args={"source_locator": "moon.md"})],
            [ToolCall(tool="search_wiki", args={"query": "moon"})],
            [_plan_page_call("moon")],
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_write_args(),
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
                        "page_id": "moon",
                        "page_kind": "source",
                        "summary": "Lunar notes.",
                        "page_body": "Body.",
                    },
                )
            ],
            [ToolCall(tool="read_source", args={"source_locator": "moon.md"})],
            [ToolCall(tool="search_wiki", args={"query": "moon"})],
            [_plan_page_call("moon")],
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_write_args(),
                )
            ],
            [ToolCall(tool="finish_ingest", args={"report": "ok"})],
        ]
        await _session(store, script, paths).ingest(source)
        # The blocked first write must not have touched the wiki layer.
        assert store.read_index().count("[[moon]]") == 1

    async def test_write_page_requires_prior_search_wiki(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        # Ingest must consult the existing wiki before it writes. A source
        # read alone is not enough for compounding wiki maintenance.
        script = [
            [ToolCall(tool="read_source", args={"source_locator": "moon.md"})],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "page_id": "moon",
                        "page_kind": "source",
                        "summary": "Lunar notes.",
                        "page_body": "Body.",
                    },
                )
            ],
            [ToolCall(tool="search_wiki", args={"query": "moon"})],
            [_plan_page_call("moon")],
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_write_args(),
                )
            ],
            [ToolCall(tool="finish_ingest", args={"report": "ok"})],
        ]
        await _session(store, script, paths).ingest(source)

        assert store.read_index().count("[[moon]]") == 1

    async def test_write_page_must_match_active_ingest_route_plan(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        script = [
            [ToolCall(tool="read_source", args={"source_locator": "moon.md"})],
            [ToolCall(tool="search_wiki", args={"query": "moon"})],
            [_plan_page_call("moon-summary")],
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_write_args(),
                )
            ],
            [_plan_page_call("moon")],
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_write_args(),
                )
            ],
            [ToolCall(tool="finish_ingest", args={"report": "ok"})],
        ]

        await _session(store, script, paths).ingest(source)

        assert store.list_pages() == ["moon"]
        assert "moon-summary" not in store.read_index()

    async def test_bad_tool_args_fed_back_for_self_correction(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        script = [
            [ToolCall(tool="read_source", args={"source_locator": "moon.md"})],
            [ToolCall(tool="search_wiki", args={"query": "moon"})],
            [_plan_page_call("moon")],
            [
                ToolCall(  # invalid category — tool error, model retries
                    tool="write_page",
                    args={
                        "page_id": "moon",
                        "page_kind": "article",
                        "summary": "s",
                        "page_body": "b",
                    },
                )
            ],
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_write_args(summary="s"),
                )
            ],
            [ToolCall(tool="finish_ingest", args={"report": "ok"})],
        ]
        result = await _session(store, script, paths).ingest(source)
        assert result.output == "ok"
        assert store.list_pages() == ["moon"]

    async def test_source_summary_validation_error_recovers(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        script = [
            [ToolCall(tool="read_source", args={"source_locator": "moon.md"})],
            [ToolCall(tool="search_wiki", args={"query": "moon"})],
            [_plan_page_call("moon")],
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_write_args(
                        claim_text="The Moon formed 4.5 billion years ago from a giant impact."
                    ),
                )
            ],
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_write_args(
                        claim_text="A compact lunar-origin note keeps the impact claim."
                    ),
                )
            ],
            [ToolCall(tool="finish_ingest", args={"report": "ok"})],
        ]
        result = await _session(store, script, paths).ingest(source)

        assert result.output == "ok"
        assert store.list_pages() == ["moon"]
        assert "source-claim-unit" not in store.read_page("moon")

    async def test_markdown_ingest_without_successful_write_is_not_logged(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        script = [
            [ToolCall(tool="read_source", args={"source_locator": "moon.md"})],
            [ToolCall(tool="search_wiki", args={"query": "moon"})],
            [_plan_page_call("moon")],
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_write_args(
                        claim_text="The Moon formed 4.5 billion years ago from a giant impact."
                    ),
                )
            ],
            [ToolCall(tool="finish_ingest", args={"report": "claimed done"})],
        ]

        with pytest.raises(RuntimeError, match="successful page writes"):
            await _session(store, script, paths).ingest(source)

        assert store.list_pages() == []
        assert "claimed done" not in paths.log_path.read_text(encoding="utf-8")

    async def test_rewrite_without_read_is_blocked_then_recovers(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        # write_page replaces the whole page; rewriting one the model never
        # read this run must fail with a corrective error (open question #10),
        # and succeed after read_page.
        store.write_page(
            wiki_page(
                name="moon",
                category="source",
                summary="Original.",
                body="Original rich body with [[links]].",
                updated=TODAY,
            )
        )
        script = [
            [ToolCall(tool="read_source", args={"source_locator": "moon.md"})],
            [ToolCall(tool="search_wiki", args={"query": "moon"})],
            [_plan_page_call("moon", action="enrich")],
            [
                ToolCall(  # blind rewrite — must be rejected
                    tool="write_page",
                    args={
                        "page_id": "moon",
                        "page_kind": "source",
                        "summary": "thin",
                        "page_body": "x",
                    },
                )
            ],
            [ToolCall(tool="read_page", args={"page_id": "moon"})],
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_write_args(
                        summary="Updated.",
                        record_text="Source record for [[moon]]. Plus new facts.",
                        claim_text="Plus new facts are filed through the source summary.",
                    ),
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
            [ToolCall(tool="read_source", args={"source_locator": "moon.md"})],
            [ToolCall(tool="search_wiki", args={"query": "moon"})],
            [_plan_page_call("moon")],
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_write_args(
                        record_text="Real claim.\n\n"
                        "[figure text (OCR, unverified): NOISE ON A MUG]\n\n"
                        "Another claim."
                    ),
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
            [ToolCall(tool="read_source", args={"source_locator": "moon.md"})],
            [ToolCall(tool="search_wiki", args={"query": "moon"})],
            [_plan_page_call("moon", summary="s")],
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_write_args(summary="s"),
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


class TestStrictEvidenceWrites:
    def test_write_guard_accepts_non_tool_ingest_route_plan(self, store: WikiStore) -> None:
        state = IngestRoutePlanState(IngestRouteContext(source_locator="moon.md", scope="source"))
        state.accept(
            IngestRoutePlan(
                source_locator="moon.md",
                scope="source",
                profile_ids=(),
                planned_pages=(
                    PlannedPage(
                        metadata=wiki_page(
                            name="moon",
                            category="source",
                            summary="Lunar notes.",
                            body="",
                        ).page_metadata,
                        role="primary source page",
                        action="create",
                        source_scope="moon.md",
                        confidence="high",
                        rationale="The source is about the Moon.",
                    ),
                ),
            )
        )
        tool = write_page_tool(store, TODAY, ingest_route_plan_state=state)

        result = tool.callable(
            page_id="moon",
            page_kind="source",
            summary="Lunar notes.",
            page_body="Claim. (raw/moon.md)",
            sources=[],
        )

        assert "Wrote wiki/moon.md" in result
        assert "moon" in store.list_pages()

    def test_off_mode_skips_validation(self, store: WikiStore) -> None:
        tool = write_page_tool(store, TODAY, evidence_policy=EvidencePolicy(mode="off"))
        result = tool.callable(
            page_id="moon",
            page_kind="source",
            summary="Lunar notes.",
            page_body="Claim cites a missing source. (raw/missing.md)",
            sources=[],
        )
        assert "Wrote wiki/moon.md" in result
        assert "missing-source" not in result
        assert "moon" in store.list_pages()

    def test_warn_mode_permits_write_and_returns_findings(self, store: WikiStore) -> None:
        tool = write_page_tool(store, TODAY, evidence_policy=EvidencePolicy(mode="warn"))
        result = tool.callable(
            page_id="moon",
            page_kind="source",
            summary="Lunar notes.",
            page_body="Claim cites a missing source. (raw/missing.md)",
            sources=[],
        )
        assert "Wrote wiki/moon.md" in result
        assert "Strict evidence findings" in result
        assert "missing-source" in result
        assert "moon" in store.list_pages()

    def test_fail_mode_rejects_and_leaves_index_unchanged(self, store: WikiStore) -> None:
        before_index = store.read_index()
        tool = write_page_tool(store, TODAY, evidence_policy=EvidencePolicy(mode="fail"))
        with pytest.raises(WikiStoreError, match="missing-source"):
            tool.callable(
                page_id="moon",
                page_kind="source",
                summary="Lunar notes.",
                page_body="Claim cites a missing source. (raw/missing.md)",
                sources=[],
            )
        assert store.read_index() == before_index
        assert "moon" not in store.list_pages()
        with pytest.raises(PageNotFoundError):
            store.read_page("moon")

    def test_fail_mode_rejects_fabricated_normalized_evidence(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        (paths.raw_dir / "article.md").write_text("Actual source line.", encoding="utf-8")
        before_index = store.read_index()
        tool = write_page_tool(store, TODAY, evidence_policy=EvidencePolicy(mode="fail"))

        with pytest.raises(WikiStoreError, match="evidence-not-found"):
            tool.callable(
                page_id="moon",
                page_kind="source",
                summary="Lunar notes.",
                page_body='"Fabricated source line." (raw/article.md normalized:L1)',
                sources=[],
            )

        assert store.read_index() == before_index
        assert "moon" not in store.list_pages()


class TestQuery:
    async def test_search_then_respond_and_logged(self, store: WikiStore, paths: WikiPaths) -> None:
        store.write_page(
            wiki_page(
                name="moon",
                category="source",
                summary="Lunar notes.",
                body="Giant impact formed the Moon.",
                updated=TODAY,
            )
        )
        script = [
            [ToolCall(tool="search_wiki", args={"query": "moon formation"})],
            [ToolCall(tool="read_page", args={"page_id": "moon"})],
            [ToolCall(tool="respond", args={"message": "A giant impact — see [[moon]]."})],
        ]
        result = await _session(store, script, paths).query("How did the Moon form?")
        assert result.output == "A giant impact — see [[moon]]."
        assert f"## [{TODAY}] query | How did the Moon form?" in paths.log_path.read_text()

    async def test_respond_requires_prior_page_or_index_read(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(
            wiki_page(
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
            [ToolCall(tool="read_page", args={"page_id": "moon"})],
            [ToolCall(tool="respond", args={"message": "A giant impact — see [[moon]]."})],
        ]
        result = await _session(store, script, paths).query("How did the Moon form?")
        assert result.output == "A giant impact — see [[moon]]."

    async def test_respond_allows_index_read_for_coverage_question(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(
            wiki_page(
                name="moon",
                category="source",
                summary="Lunar notes.",
                body="Giant impact formed the Moon.",
                updated=TODAY,
            )
        )
        script = [
            [ToolCall(tool="read_index", args={})],
            [
                ToolCall(
                    tool="respond",
                    args={"message": "The wiki currently covers lunar notes via [[moon]]."},
                )
            ],
        ]
        result = await _session(store, script, paths).query("What does this wiki cover?")
        assert result.output == "The wiki currently covers lunar notes via [[moon]]."


class TestLint:
    async def test_empty_wiki_short_circuits_without_llm(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        result = await _session(store, [], paths).lint()
        assert "empty" in result.output.lower()
        assert f"## [{TODAY}] lint | empty wiki" in paths.log_path.read_text()

    async def test_lint_files_report_page_and_log(self, store: WikiStore, paths: WikiPaths) -> None:
        store.write_page(
            wiki_page(
                name="alpha",
                category="concept",
                summary="A.",
                body="Links to [[ghost]].",
                updated=TODAY,
            )
        )
        script = [
            [ToolCall(tool="read_page", args={"page_id": "alpha"})],
            [ToolCall(tool="finish_lint", args={"report": "ghost link is broken."})],
        ]
        session = _session(store, script, paths)
        result = await session.lint()
        assert "## Model report" in result.output
        assert "ghost link is broken." in result.output
        assert "## Deterministic verification" in result.output
        assert "### Delta" in result.output
        assert "### Before model pass" in result.output
        assert "### After model pass" in result.output
        assert "wiki-health" in store.list_pages()
        assert "Deterministic verification" in store.read_page("wiki-health")
        assert f"## [{TODAY}] lint | wiki health" in paths.log_path.read_text()
        # The deterministic findings reached the model in the user message.
        fake: FakeClient = session.client
        first_turn = fake.sent[0]
        user_msgs = [m["content"] for m in first_turn if m.get("role") == "user"]
        assert any("ghost" in content for content in user_msgs)

    async def test_lint_output_does_not_trust_model_success_claim(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(
            wiki_page(
                name="alpha",
                category="concept",
                summary="A.",
                body="No links.",
                updated=TODAY,
            )
        )
        store.write_page(
            wiki_page(
                name="beta",
                category="concept",
                summary="B.",
                body="No links.",
                updated=TODAY,
            )
        )
        script = [
            [ToolCall(tool="read_page", args={"page_id": "alpha"})],
            [ToolCall(tool="finish_lint", args={"report": "All orphan pages fixed."})],
        ]
        result = await _session(store, script, paths).lint()

        assert "All orphan pages fixed." in result.output
        delta = result.output.split("### Delta", maxsplit=1)[1].split(
            "### Before model pass", maxsplit=1
        )[0]
        assert "Resolved orphan pages: None." in delta
        assert "Remaining orphan pages" in delta
        assert "- alpha" in delta
        assert "- beta" in delta
        after = result.output.split("### After model pass", maxsplit=1)[1]
        assert "Orphan pages" in after
        assert "- alpha" in after
        assert "- beta" in after

    async def test_lint_can_fix_orphan_with_deterministic_link_tool(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(
            wiki_page(
                name="alpha",
                category="concept",
                summary="A.",
                body="Related source page: [[gamma]].",
                updated=TODAY,
            )
        )
        store.write_page(
            wiki_page(
                name="beta",
                category="concept",
                summary="B.",
                body="Initially orphaned.",
                updated=TODAY,
            )
        )
        store.write_page(
            wiki_page(
                name="gamma",
                category="source",
                summary="G.",
                body="Backlink to [[alpha]].",
                updated=TODAY,
            )
        )
        script = [
            [ToolCall(tool="read_page", args={"page_id": "alpha"})],
            [ToolCall(tool="link_orphan", args={"from_page": "alpha", "orphan_page": "beta"})],
            [ToolCall(tool="finish_lint", args={"report": "Linked beta from alpha."})],
        ]
        result = await _session(store, script, paths).lint()

        assert "[[beta]]" in store.read_page("alpha")
        assert "Linked beta from alpha." in result.output
        delta = result.output.split("### Delta", maxsplit=1)[1].split(
            "### Before model pass", maxsplit=1
        )[0]
        assert "Resolved orphan pages:\n- beta" in delta
        assert "Remaining orphan pages: None." in delta
        after = result.output.split("### After model pass", maxsplit=1)[1]
        assert "No deterministic issues found" in after
        assert "- beta" not in after

    async def test_link_orphan_rejects_non_orphan_target(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(
            wiki_page(
                name="alpha",
                category="concept",
                summary="A.",
                body="[[beta]]",
                updated=TODAY,
            )
        )
        store.write_page(
            wiki_page(
                name="beta",
                category="concept",
                summary="B.",
                body="[[alpha]]",
                updated=TODAY,
            )
        )
        store.write_page(
            wiki_page(
                name="gamma",
                category="concept",
                summary="G.",
                body="[[alpha]]",
                updated=TODAY,
            )
        )
        script = [
            [ToolCall(tool="read_page", args={"page_id": "gamma"})],
            [ToolCall(tool="link_orphan", args={"from_page": "gamma", "orphan_page": "beta"})],
            [ToolCall(tool="finish_lint", args={"report": "beta was not an orphan."})],
        ]
        result = await _session(store, script, paths).lint()

        assert "beta was not an orphan." in result.output
        assert store.read_page("gamma").count("[[beta]]") == 0

    async def test_lint_prompt_includes_evidence_findings(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(
            wiki_page(
                name="alpha",
                category="concept",
                summary="A.",
                body="Claim cites a missing source. (raw/missing.md)",
                updated=TODAY,
            )
        )
        script = [
            [ToolCall(tool="read_page", args={"page_id": "alpha"})],
            [ToolCall(tool="finish_lint", args={"report": "missing source citation found."})],
        ]
        session = _session(store, script, paths)
        session = Session(
            store=session.store,
            client=session.client,
            context_manager=session.context_manager,
            today=session.today,
            runs_dir=session.runs_dir,
            run_id=session.run_id,
            strict_evidence="warn",
        )
        await session.lint()
        fake: FakeClient = session.client
        user_msgs = [m["content"] for m in fake.sent[0] if m.get("role") == "user"]
        assert any("Citation evidence findings" in content for content in user_msgs)
        assert any("missing-source" in content for content in user_msgs)
        assert any("Strict evidence mode: warn" in content for content in user_msgs)

    async def test_lint_prompt_includes_normalized_resolver_findings(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        (paths.raw_dir / "article.md").write_text("Actual source line.", encoding="utf-8")
        store.write_page(
            wiki_page(
                name="alpha",
                category="concept",
                summary="A.",
                body='"Fabricated source line." (raw/article.md normalized:L1)',
                updated=TODAY,
            )
        )
        script = [
            [ToolCall(tool="read_page", args={"page_id": "alpha"})],
            [ToolCall(tool="finish_lint", args={"report": "fabricated evidence found."})],
        ]
        session = _session(store, script, paths)
        session = Session(
            store=session.store,
            client=session.client,
            context_manager=session.context_manager,
            today=session.today,
            runs_dir=session.runs_dir,
            run_id=session.run_id,
            strict_evidence="warn",
        )

        result = await session.lint()

        assert "evidence-not-found" in result.output
        fake: FakeClient = session.client
        user_msgs = [m["content"] for m in fake.sent[0] if m.get("role") == "user"]
        assert any("evidence-not-found" in content for content in user_msgs)

    async def test_health_page_is_not_reported_as_orphan(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        # A prior lint filed wiki-health; the next lint must not flag it.
        store.write_page(
            wiki_page(
                name="alpha",
                category="concept",
                summary="A.",
                body="[[beta]]",
                updated=TODAY,
            )
        )
        store.write_page(
            wiki_page(
                name="beta",
                category="concept",
                summary="B.",
                body="[[alpha]]",
                updated=TODAY,
            )
        )
        store.write_page(
            wiki_page(
                name="wiki-health",
                category="synthesis",
                summary="Old report.",
                body="All clean.",
                updated=TODAY,
            )
        )
        script = [
            [ToolCall(tool="read_page", args={"page_id": "alpha"})],
            [ToolCall(tool="finish_lint", args={"report": "Still clean."})],
        ]
        session = _session(store, script, paths)
        await session.lint()
        fake: FakeClient = session.client
        user_msgs = [m["content"] for m in fake.sent[0] if m.get("role") == "user"]
        assert not any("Orphan" in content for content in user_msgs)


class TestContradictions:
    async def test_records_findings_without_rewriting_content_pages(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(
            wiki_page(
                name="alpha",
                category="concept",
                summary="A.",
                body="The feature was introduced in ES2015. See [[beta]].",
                updated=TODAY,
            )
        )
        store.write_page(
            wiki_page(
                name="beta",
                category="concept",
                summary="B.",
                body="The feature was introduced in ES2019. See [[alpha]].",
                updated=TODAY,
            )
        )
        before_alpha = store.read_page("alpha")
        before_beta = store.read_page("beta")
        selection = select_contradiction_candidates(store.page_texts(), max_pairs=5)
        script = [
            [ToolCall(tool="read_page", args={"page_id": "alpha"})],
            [ToolCall(tool="read_page", args={"page_id": "beta"})],
            [
                ToolCall(
                    tool="record_contradiction",
                    args={
                        "page_a": "alpha",
                        "claim_a": "The feature was introduced in ES2015.",
                        "page_b": "beta",
                        "claim_b": "The feature was introduced in ES2019.",
                        "severity": "medium",
                        "rationale": "The introduction years conflict.",
                        "recommended_action": "Inspect the cited sources and qualify the date.",
                    },
                )
            ],
            [ToolCall(tool="finish_contradictions", args={"report": "Recorded one conflict."})],
        ]
        session = _session(store, script, paths)

        result = await session.contradictions(selection)

        assert result.op == "contradictions"
        assert "Candidate pairs discovered:" in result.output
        assert "Finding 1: MEDIUM" in result.output
        assert "wiki-contradictions" in store.list_pages()
        assert "Contradiction Audit" in store.read_page("wiki-contradictions")
        assert f"## [{TODAY}] contradiction | contradiction audit" in paths.log_path.read_text()
        assert store.read_page("alpha") == before_alpha
        assert store.read_page("beta") == before_beta
        fake: FakeClient = session.client
        user_msgs = [m["content"] for m in fake.sent[0] if m.get("role") == "user"]
        assert any(
            "Pair 1" in content and "Candidate pairs discovered" in content for content in user_msgs
        )

    async def test_no_candidate_audit_short_circuits_without_llm(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        selection = select_contradiction_candidates(store.page_texts())
        result = await _session(store, [], paths).contradictions(selection)

        assert result.transcript_path is None
        assert "Candidate pairs discovered: 0" in result.output
        assert "not proof that the wiki has no contradictions" in result.output
        assert "wiki-contradictions" in store.list_pages()

    async def test_record_contradiction_rejects_missing_page(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(
            wiki_page(name="alpha", category="concept", summary="A.", body="Claim.", updated=TODAY)
        )
        selection = select_contradiction_candidates(
            {
                "alpha": "---\ncategory: concept\nsummary: A.\n---\n\nSee [[beta]].",
                "beta": "---\ncategory: concept\nsummary: B.\n---\n\nClaim.",
            }
        )
        script = [
            [ToolCall(tool="read_page", args={"page_id": "alpha"})],
            [
                ToolCall(
                    tool="record_contradiction",
                    args={
                        "page_a": "alpha",
                        "claim_a": "A claim.",
                        "page_b": "missing",
                        "claim_b": "Missing claim.",
                        "severity": "high",
                        "rationale": "Would conflict.",
                        "recommended_action": "No action.",
                    },
                )
            ],
            [ToolCall(tool="finish_contradictions", args={"report": "No valid findings."})],
        ]
        result = await _session(store, script, paths).contradictions(selection)

        assert "No valid findings." in result.output
        assert "No contradictions were recorded" in result.output


class TestGrounding:
    async def test_records_verdicts_without_rewriting_content_pages(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        (paths.raw_dir / "article.md").write_text(
            "Array destructuring binds positions to names.", encoding="utf-8"
        )
        store.write_page(
            wiki_page(
                name="arrays",
                category="concept",
                summary="Array notes.",
                body="Array destructuring binds positions to names. (raw/article.md normalized:L1)",
                updated=TODAY,
            )
        )
        before = store.read_page("arrays")
        selection = select_grounding_claims(
            store.page_texts(),
            store.source_inventory(),
            store.source_resolver(),
            max_claims=1,
        )
        script = [
            [
                ToolCall(
                    tool="record_grounding_verdict",
                    args={
                        "page_name": "arrays",
                        "claim_text": "Array destructuring binds positions to names.",
                        "verdict": "supported",
                        "rationale": "The resolved excerpt states the same claim.",
                        "recommended_action": "No page change needed.",
                    },
                )
            ],
            [ToolCall(tool="finish_grounding", args={"report": "One claim supported."})],
        ]

        result = await _session(store, script, paths).grounding(selection)

        assert result.op == "grounding"
        assert "Claim candidates discovered: 1" in result.output
        assert "Verdict 1: INFO - supported" in result.output
        assert "wiki-grounding" in store.list_pages()
        assert "Grounding Audit" in store.read_page("wiki-grounding")
        assert f"## [{TODAY}] grounding | grounding audit" in paths.log_path.read_text()
        assert store.read_page("arrays") == before

    async def test_no_candidate_audit_short_circuits_without_llm(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        selection = GroundingSelection(
            candidates=(),
            deterministic_findings=(),
            candidate_count=0,
            max_claims=5,
        )

        result = await _session(store, [], paths).grounding(selection)

        assert result.transcript_path is None
        assert "Claim candidates discovered: 0" in result.output
        assert "No model grounding verdicts were recorded" in result.output
        assert "wiki-grounding" in store.list_pages()

    async def test_invalid_verdict_label_is_rejected_then_recovers(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        (paths.raw_dir / "article.md").write_text("A supported fact.", encoding="utf-8")
        store.write_page(
            wiki_page(
                name="alpha",
                category="concept",
                summary="A.",
                body="A supported fact. (raw/article.md normalized:L1)",
                updated=TODAY,
            )
        )
        selection = select_grounding_claims(
            store.page_texts(),
            store.source_inventory(),
            store.source_resolver(),
            max_claims=1,
        )
        script = [
            [
                ToolCall(
                    tool="record_grounding_verdict",
                    args={
                        "page_name": "alpha",
                        "claim_text": "A supported fact.",
                        "verdict": "maybe",
                        "rationale": "Invalid label.",
                        "recommended_action": "No action.",
                    },
                )
            ],
            [
                ToolCall(
                    tool="record_grounding_verdict",
                    args={
                        "page_name": "alpha",
                        "claim_text": "A supported fact.",
                        "verdict": "supported",
                        "rationale": "The excerpt directly supports the claim.",
                        "recommended_action": "No action.",
                    },
                )
            ],
            [ToolCall(tool="finish_grounding", args={"report": "Recovered."})],
        ]

        result = await _session(store, script, paths).grounding(selection)

        assert "Invalid label" not in result.output
        assert result.output.count("Verdict 1: INFO - supported") == 1

    async def test_non_unclear_verdict_without_evidence_excerpt_is_rejected(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        (paths.raw_dir / "article.md").write_text("A supported fact.", encoding="utf-8")
        store.write_page(
            wiki_page(
                name="alpha",
                category="concept",
                summary="A.",
                body="A supported fact. (raw/article.md)",
                updated=TODAY,
            )
        )
        selection = select_grounding_claims(
            store.page_texts(),
            store.source_inventory(),
            store.source_resolver(),
            max_claims=1,
        )
        script = [
            [
                ToolCall(
                    tool="record_grounding_verdict",
                    args={
                        "page_name": "alpha",
                        "claim_text": "A supported fact.",
                        "verdict": "supported",
                        "rationale": "The citation exists.",
                        "recommended_action": "No action.",
                    },
                )
            ],
            [
                ToolCall(
                    tool="record_grounding_verdict",
                    args={
                        "page_name": "alpha",
                        "claim_text": "A supported fact.",
                        "verdict": "unclear",
                        "rationale": "No normalized evidence excerpt was available.",
                        "recommended_action": "Review the raw source or add a locator.",
                    },
                )
            ],
            [ToolCall(tool="finish_grounding", args={"report": "Recovered."})],
        ]

        result = await _session(store, script, paths).grounding(selection)

        assert "Verdict 1: WARN - unclear" in result.output
        assert "INFO - supported" not in result.output

    async def test_deterministic_failures_skip_model_judgment(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        (paths.raw_dir / "article.md").write_text("Actual source line.", encoding="utf-8")
        store.write_page(
            wiki_page(
                name="alpha",
                category="concept",
                summary="A.",
                body='"Fabricated source line." (raw/article.md normalized:L1)',
                updated=TODAY,
            )
        )
        selection = select_grounding_claims(
            store.page_texts(),
            store.source_inventory(),
            store.source_resolver(),
            max_claims=5,
        )

        result = await _session(store, [], paths).grounding(selection)

        assert result.transcript_path is None
        assert "evidence-not-found" in result.output
        assert "No model grounding verdicts were recorded" in result.output


class TestSemanticLint:
    async def test_records_findings_without_rewriting_content_pages(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(
            wiki_page(
                name="alpha",
                category="concept",
                summary="A.",
                body="Feature arrived in ES2015. See [[beta]]. (raw/book.md)",
                sources=("book.md",),
                updated=TODAY,
            )
        )
        store.write_page(
            wiki_page(
                name="beta",
                category="concept",
                summary="B.",
                body="Feature details changed later. See [[alpha]]. (raw/book.md)",
                sources=("book.md",),
                updated=TODAY,
            )
        )
        before_alpha = store.read_page("alpha")
        selection = select_semantic_lint_candidates(
            store.page_texts(),
            store.read_candidate_backlog(),
            max_items=3,
        )
        script = [
            [ToolCall(tool="read_page", args={"page_id": "alpha"})],
            [ToolCall(tool="read_page", args={"page_id": "beta"})],
            [
                ToolCall(
                    tool="record_semantic_finding",
                    args={
                        "kind": "possible_supersession",
                        "affected_pages": ["alpha", "beta"],
                        "rationale": "The newer page may change the context of alpha.",
                        "evidence_consulted": "[[alpha]] and [[beta]]",
                        "recommended_action": "Review source dates and qualify the claim.",
                    },
                )
            ],
            [ToolCall(tool="finish_semantic_lint", args={"report": "Recorded one lead."})],
        ]

        result = await _session(store, script, paths).semantic_lint(selection)

        assert result.op == "semantic-lint"
        assert "Finding 1: possible_supersession" in result.output
        assert "wiki-semantic-lint" in store.list_pages()
        assert "Semantic Lint" in store.read_page("wiki-semantic-lint")
        assert f"## [{TODAY}] semantic-lint | semantic audit" in paths.log_path.read_text()
        assert store.read_page("alpha") == before_alpha

    async def test_no_candidate_audit_short_circuits_without_llm(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        selection = SemanticLintSelection(candidates=(), candidate_count=0, max_items=5)

        result = await _session(store, [], paths).semantic_lint(selection)

        assert result.transcript_path is None
        assert "Candidate items discovered: 0" in result.output
        assert "No semantic lint findings were recorded" in result.output
        assert "wiki-semantic-lint" in store.list_pages()

    async def test_record_semantic_finding_rejects_missing_page_then_recovers(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(
            wiki_page(
                name="alpha",
                category="concept",
                summary="A.",
                body="Feature arrived in ES2015. (raw/book.md)",
                sources=("book.md",),
                updated=TODAY,
            )
        )
        store.write_page(
            wiki_page(
                name="beta",
                category="concept",
                summary="B.",
                body="Feature details changed later. [[alpha]] (raw/book.md)",
                sources=("book.md",),
                updated=TODAY,
            )
        )
        selection = select_semantic_lint_candidates(
            store.page_texts(),
            store.read_candidate_backlog(),
            max_items=3,
        )
        script = [
            [ToolCall(tool="read_page", args={"page_id": "alpha"})],
            [
                ToolCall(
                    tool="record_semantic_finding",
                    args={
                        "kind": "data_gap",
                        "affected_pages": ["missing"],
                        "rationale": "Bad page.",
                        "evidence_consulted": "No valid page.",
                        "recommended_action": "Retry.",
                    },
                )
            ],
            [
                ToolCall(
                    tool="record_semantic_finding",
                    args={
                        "kind": "data_gap",
                        "affected_pages": ["alpha"],
                        "rationale": "Coverage needs review.",
                        "evidence_consulted": "[[alpha]]",
                        "recommended_action": "Consider a source search.",
                    },
                )
            ],
            [ToolCall(tool="finish_semantic_lint", args={"report": "Recovered."})],
        ]

        result = await _session(store, script, paths).semantic_lint(selection)

        assert "Finding 1: data_gap" in result.output
        assert "missing" not in result.output
