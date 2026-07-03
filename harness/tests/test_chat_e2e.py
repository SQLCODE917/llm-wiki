"""Chat e2e: read-only workflow, seeded turns, and the REPL's dispatch logic
— real WorkflowRunner + stores, fake LLM, no terminal."""

import asyncio
import builtins

import pytest
from fakes import FakeClient
from forge.context import ContextManager, NoCompact
from forge.core.workflow import ToolCall
from helpers import wiki_page

from llmwiki.cli import _close_backend_safely, _run_chat
from llmwiki.config import WikiPaths
from llmwiki.domain.chat_grounding import ChatEvidenceScope, ChatTaskMode
from llmwiki.domain.chatwindow import QAPair
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.domain.search import SearchHit
from llmwiki.domain.task_evidence import build_task_evidence_pack
from llmwiki.runtime.chat_repl import ChatRepl
from llmwiki.runtime.session import Session
from llmwiki.store import WikiStore, WikiStoreError
from llmwiki.store.chat_store import ChatStore
from llmwiki.workflows import build_chat_file_workflow, build_chat_workflow

TODAY = "2026-06-12"


def _session(store: WikiStore, script: list, paths: WikiPaths) -> Session:
    return Session(
        store=store,
        client=FakeClient(script),
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        today=TODAY,
        runs_dir=paths.root / "runs",
        run_id="chat-test",
    )


def _seed_wiki(store: WikiStore) -> None:
    store.write_page(
        wiki_page(
            name="closure",
            category="concept",
            summary="Functions capturing scope.",
            body="A closure captures its defining environment.",
            updated=TODAY,
        )
    )


def _seed_procedure_wiki(store: WikiStore) -> None:
    store.write_page(
        WikiPage(
            page_metadata=PageMetadata(
                page_id="book-procedure-create-character",
                page_kind="procedure",
                page_family="procedure-guide",
                summary="Create Character.",
            ),
            page_body=(
                "# Create Character\n\n"
                "## Procedure Steps\n\n"
                "1. **Choose Race** (`choose`) - evidence section [[book-choose-race]].\n"
                "2. **Record Name** (`record`) - evidence section [[book-record-name]].\n"
            ),
        )
    )
    store.write_page(
        WikiPage(
            page_metadata=PageMetadata(
                page_id="book-choose-race",
                page_kind="source",
                page_family="section-reference",
                summary="Race choices.",
            ),
            page_body="# Choose Race\n\nThe race chosen in the worked example is human.",
        )
    )
    store.write_page(
        WikiPage(
            page_metadata=PageMetadata(
                page_id="book-record-name",
                page_kind="source",
                page_family="section-reference",
                summary="Name choice.",
            ),
            page_body="# Record Name\n\nNames are a free character choice.",
        )
    )


class TestChatWorkflow:
    def test_read_only_by_construction(self, store: WikiStore) -> None:
        workflow = build_chat_workflow(store)
        assert "write_page" not in workflow.tools
        assert set(workflow.tools) == {
            "inspect_page",
            "read_index",
            "read_page",
            "respond",
            "search_wiki",
        }

    def test_no_required_steps_grounding_is_provisioned(self, store: WikiStore) -> None:
        # The respond tool performs the evidence gate, so StepEnforcer still
        # does not force a fixed navigation sequence.
        assert build_chat_workflow(store).required_steps == []

    def test_content_chat_requires_page_read_before_response(self, store: WikiStore) -> None:
        _seed_wiki(store)
        workflow = build_chat_workflow(store, allow_index_response=False)
        workflow.tools["read_index"].callable()
        with pytest.raises(WikiStoreError, match="read_page"):
            workflow.tools["respond"].callable(message="The index did not mention it.")

    def test_content_chat_requires_citation_to_read_page(self, store: WikiStore) -> None:
        _seed_wiki(store)
        workflow = build_chat_workflow(store, allow_index_response=False)
        workflow.tools["read_page"].callable(page_id="closure")

        with pytest.raises(WikiStoreError, match=r"\[\[closure\]\]"):
            workflow.tools["respond"].callable(
                message="A closure captures its defining environment. (raw/book.pdf)"
            )

        answer = workflow.tools["respond"].callable(
            message="A closure captures its defining environment. [[closure]] (raw/book.pdf)"
        )
        assert "[[closure]]" in answer

    def test_focused_chat_scope_rejects_lower_ranked_aggregate_read(self, store: WikiStore) -> None:
        store.write_page(
            WikiPage(
                page_metadata=PageMetadata(
                    page_id="book",
                    page_kind="source",
                    page_family="source-manifest",
                    summary="Whole source manifest.",
                ),
                page_body="### Disposition counts\n\n- non-claim: 5206\n",
            )
        )
        store.write_page(
            WikiPage(
                page_metadata=PageMetadata(
                    page_id="book-section",
                    page_kind="source",
                    page_family="section-reference",
                    summary="Focused section.",
                ),
                page_body="A precise term is explained here.",
            )
        )
        scope = ChatEvidenceScope.from_search_hits(
            store.page_texts(),
            (
                SearchHit("book-section", 247, "focused"),
                SearchHit("book", 227, "aggregate"),
            ),
        )
        workflow = build_chat_workflow(
            store,
            allow_index_response=False,
            evidence_scope=scope,
        )

        assert "precise term" in workflow.tools["read_page"].callable(page_id="book-section")
        with pytest.raises(WikiStoreError) as exc:
            workflow.tools["read_page"].callable(page_id="book")

        assert "source-manifest" in str(exc.value)
        assert "non-claim" not in str(exc.value)

    def test_chat_file_workflow_is_explicit_write_path(self, store: WikiStore) -> None:
        workflow = build_chat_file_workflow(store, TODAY)
        assert "write_page" in workflow.tools
        assert "finish_chat_file" in workflow.tools
        assert workflow.required_steps == ["read_page"]

    def test_procedure_execution_requires_valid_submit_before_response(
        self, store: WikiStore
    ) -> None:
        _seed_procedure_wiki(store)
        pack = build_task_evidence_pack(
            store.page_texts(),
            (SearchHit("book-procedure-create-character", 500, "procedure"),),
            task_mode=ChatTaskMode.EXECUTE_PROCEDURE,
        )
        assert pack is not None
        workflow = build_chat_workflow(
            store,
            allow_index_response=False,
            task_evidence_pack=pack,
            require_procedure_execution=True,
        )

        assert "submit_procedure_execution" in workflow.tools
        assert set(workflow.tools) == {"submit_procedure_execution", "respond"}
        assert workflow.required_steps == ["submit_procedure_execution"]
        with pytest.raises(WikiStoreError, match="submit_procedure_execution"):
            workflow.tools["respond"].callable(message="Created [[book-choose-race]].")

        workflow.tools["submit_procedure_execution"].callable(
            procedure_id="book-procedure-create-character",
            assumptions=["Aldis is the chosen character name."],
            step_results=[
                {
                    "sequence": 1,
                    "title": "Choose Race",
                    "status": "completed",
                    "outputs": [
                        {
                            "name": "race",
                            "value": "human",
                            "support": "evidence",
                            "evidence_page_ids": ["book-choose-race"],
                        }
                    ],
                },
                {
                    "sequence": 2,
                    "title": "Record Name",
                    "status": "completed",
                    "outputs": [
                        {
                            "name": "name",
                            "value": "Aldis",
                            "support": "assumption",
                        }
                    ],
                },
            ],
        )
        answer = workflow.tools["respond"].callable(
            message="Created a human named Aldis. [[book-choose-race]]"
        )
        assert "human named Aldis" in answer

    async def test_grounded_turn_carries_index_so_coverage_answers_work(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        # The measured failure: "what is this wiki about?" — the catalog is
        # now provisioned with the first message; the model can answer
        # directly from it.
        _seed_wiki(store)
        script = [
            [ToolCall(tool="read_index", args={})],
            [ToolCall(tool="respond", args={"message": "It covers [[closure]] and more."})],
        ]
        session = _session(store, script, paths)
        answer, _ = await session.chat_turn(
            "What is this wiki about?", window=(), grounded=True, tag="chat-meta"
        )
        assert answer == "It covers [[closure]] and more."
        fake: FakeClient = session.client
        first_user = next(m for m in fake.sent[0] if m["role"] == "user")
        assert "[[closure]] — Functions capturing scope." in first_user["content"]
        assert "What is this wiki about?" in first_user["content"]

    async def test_follow_up_turns_do_not_carry_the_index(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        _seed_wiki(store)
        script = [[ToolCall(tool="respond", args={"message": "ok"})]]
        session = _session(store, script, paths)
        await session.chat_turn(
            "shorter please",
            window=(QAPair(question="what is a closure?", answer="See [[closure]]."),),
            grounded=False,
            tag="chat-f",
        )
        fake: FakeClient = session.client
        user_contents = [m["content"] for m in fake.sent[0] if m["role"] == "user"]
        assert not any("[[closure]] — Functions capturing scope." in c for c in user_contents)


class TestChatTurn:
    async def test_grounded_first_turn_searches_then_responds(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        _seed_wiki(store)
        script = [
            [ToolCall(tool="search_wiki", args={"query": "closure"})],
            [ToolCall(tool="read_page", args={"page_id": "closure"})],
            [ToolCall(tool="respond", args={"message": "See [[closure]]."})],
        ]
        session = _session(store, script, paths)
        answer, transcript = await session.chat_turn(
            "what is a closure?", window=(), grounded=True, tag="chat-t1"
        )
        assert answer == "See [[closure]]."
        assert transcript is not None and transcript.exists()
        fake: FakeClient = session.client
        first_user = next(m for m in fake.sent[0] if m["role"] == "user")
        assert "Initial wiki search results for the question." in first_user["content"]
        assert "[[closure]]" in first_user["content"]
        assert "/no_think" not in first_user["content"]

    async def test_follow_up_sees_window_and_skips_search(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        _seed_wiki(store)
        # Relaxed follow-up: respond directly, no required search.
        script = [[ToolCall(tool="respond", args={"message": "Shorter: scope capture."})]]
        session = _session(store, script, paths)
        window = (QAPair(question="what is a closure?", answer="See [[closure]]."),)
        answer, _ = await session.chat_turn(
            "say that shorter", window=window, grounded=False, tag="chat-t2"
        )
        assert answer == "Shorter: scope capture."
        fake: FakeClient = session.client
        sent = fake.sent[0]
        contents = [m["content"] for m in sent]
        # Past Q/A pair seeded; system prompt first; new question last.
        assert any("what is a closure?" in c for c in contents)
        assert any("See [[closure]]." in c for c in contents)
        assert sent[0]["role"] == "system"
        assert "say that shorter" in sent[-1]["content"]

    async def test_resumed_fresh_lookup_gets_search_hints_and_requires_page_read(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        _seed_wiki(store)
        script = [
            [ToolCall(tool="read_page", args={"page_id": "closure"})],
            [ToolCall(tool="respond", args={"message": "See [[closure]]."})],
        ]
        session = _session(store, script, paths)
        window = (
            QAPair(
                question="previous topic",
                answer="Prior answer about a different topic.",
            ),
        )

        answer, _ = await session.chat_turn(
            "closure", window=window, grounded=False, tag="chat-new-topic"
        )

        assert answer == "See [[closure]]."
        fake: FakeClient = session.client
        current_user = [m for m in fake.sent[0] if m["role"] == "user"][-1]
        assert "Initial wiki search results for the question." in current_user["content"]
        assert "[[closure]]" in current_user["content"]

    async def test_execution_turn_carries_pack_and_accepts_typed_execution(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        _seed_procedure_wiki(store)
        script = [
            [
                ToolCall(
                    tool="submit_procedure_execution",
                    args={
                        "procedure_id": "book-procedure-create-character",
                        "assumptions": ["Aldis is the chosen character name."],
                        "step_results": [
                            {
                                "sequence": 1,
                                "title": "Choose Race",
                                "status": "completed",
                                "outputs": [
                                    {
                                        "name": "race",
                                        "value": "human",
                                        "support": "evidence",
                                        "evidence_page_ids": ["book-choose-race"],
                                    }
                                ],
                            },
                            {
                                "sequence": 2,
                                "title": "Record Name",
                                "status": "completed",
                                "outputs": [
                                    {
                                        "name": "name",
                                        "value": "Aldis",
                                        "support": "assumption",
                                    }
                                ],
                            },
                        ],
                    },
                )
            ],
            [
                ToolCall(
                    tool="respond",
                    args={
                        "message": (
                            "Created a human named Aldis from the procedure. [[book-choose-race]]"
                        )
                    },
                )
            ],
        ]
        session = _session(store, script, paths)

        answer, _ = await session.chat_turn(
            "actually create a character", window=(), grounded=True, tag="chat-execute"
        )

        assert "human named Aldis" in answer
        fake: FakeClient = session.client
        first_user = next(m for m in fake.sent[0] if m["role"] == "user")
        assert "Deterministic task evidence pack" in first_user["content"]
        assert "submit_procedure_execution" in first_user["content"]


class TestChatFile:
    async def test_files_latest_answer_as_synthesis(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        _seed_wiki(store)
        script = [
            [ToolCall(tool="search_wiki", args={"query": "closure"})],
            [ToolCall(tool="read_page", args={"page_id": "closure"})],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "page_id": "closure-summary",
                        "page_kind": "synthesis",
                        "summary": "Durable chat synthesis about closures.",
                        "page_body": "Closures preserve scope; see [[closure]].",
                        "sources": [],
                    },
                )
            ],
            [ToolCall(tool="finish_chat_file", args={"report": "Filed [[closure-summary]]."})],
        ]
        session = _session(store, script, paths)
        result = await session.file_chat_synthesis(
            page_id="closure-summary",
            question="explain closures",
            answer="Closures preserve scope.",
            scope="short durable note",
        )

        assert result.output == "Filed [[closure-summary]]."
        assert "Closures preserve scope" in store.read_page("closure-summary")
        assert "[[closure-summary]] — Durable chat synthesis about closures." in store.read_index()
        assert f"## [{TODAY}] chat-file | closure-summary" in paths.log_path.read_text()

    async def test_existing_page_filing_requires_read_before_rewrite(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(
            wiki_page(
                name="closure-summary",
                category="synthesis",
                summary="Original.",
                body="Old sentence.",
                updated=TODAY,
            )
        )
        script = [
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "page_id": "closure-summary",
                        "page_kind": "synthesis",
                        "summary": "Blind.",
                        "page_body": "Blind rewrite [[closure]].",
                        "sources": [],
                    },
                )
            ],
            [ToolCall(tool="read_page", args={"page_id": "closure-summary"})],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "page_id": "closure-summary",
                        "page_kind": "synthesis",
                        "summary": "Updated.",
                        "page_body": "Old sentence.\n\nNew closure synthesis links [[closure]].",
                        "sources": [],
                    },
                )
            ],
            [ToolCall(tool="finish_chat_file", args={"report": "Updated page."})],
        ]
        await _session(store, script, paths).file_chat_synthesis(
            page_id="closure-summary",
            question="make this durable",
            answer="New closure synthesis",
        )

        page = store.read_page("closure-summary")
        assert "Old sentence." in page
        assert "New closure synthesis" in page
        assert "Blind rewrite" not in page

    async def test_chat_history_is_not_accepted_as_evidence(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        _seed_wiki(store)
        script = [
            [ToolCall(tool="read_page", args={"page_id": "closure"})],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "page_id": "chat-only-claim",
                        "page_kind": "synthesis",
                        "summary": "Invalid chat-only claim.",
                        "page_body": "The prior answer said this was important. (chat history)",
                        "sources": ["chat history"],
                    },
                )
            ],
            [
                ToolCall(
                    tool="finish_chat_file",
                    args={"report": "Declined: chat history is not source evidence."},
                )
            ],
        ]
        result = await _session(store, script, paths).file_chat_synthesis(
            page_id="chat-only-claim",
            question="remember that",
            answer="This was important.",
        )

        assert "Declined" in result.output
        assert "chat-only-claim" not in store.list_pages()

    async def test_wiki_page_names_are_not_accepted_as_sources(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        _seed_wiki(store)
        script = [
            [ToolCall(tool="read_page", args={"page_id": "closure"})],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "page_id": "bad-sources",
                        "page_kind": "synthesis",
                        "summary": "Invalid source metadata.",
                        "page_body": "This cites the current wiki page [[closure]].",
                        "sources": ["closure"],
                    },
                )
            ],
            [
                ToolCall(
                    tool="finish_chat_file",
                    args={"report": "Declined: sources must be raw files."},
                )
            ],
        ]
        result = await _session(store, script, paths).file_chat_synthesis(
            page_id="bad-sources",
            question="file this",
            answer="Closure note.",
        )

        assert "Declined" in result.output
        assert "bad-sources" not in store.list_pages()


class TestChatRepl:
    def _repl(self, store: WikiStore, paths: WikiPaths, script: list) -> tuple[ChatRepl, list[str]]:
        emitted: list[str] = []
        repl = ChatRepl(
            session=_session(store, script, paths),
            chat_store=ChatStore(paths.root / "chat.db"),
            emit=emitted.append,
        )
        return repl, emitted

    async def test_full_flow_new_turn_switch_list_finish(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        _seed_wiki(store)
        script = [
            [ToolCall(tool="search_wiki", args={"query": "closure"})],
            [ToolCall(tool="read_page", args={"page_id": "closure"})],
            [ToolCall(tool="respond", args={"message": "Answer one from [[closure]]."})],
        ]
        repl, emitted = self._repl(store, paths, script)
        repl.start(resume=None)
        first_id = repl.active_id

        assert await repl.handle("what is a closure?") is True
        assert "Answer one from [[closure]]." in emitted
        assert repl.chat_store.turn_count(first_id) == 1

        assert await repl.handle("/new") is True
        second_id = repl.active_id
        assert second_id != first_id

        await repl.handle("/sessions")
        listing = "\n".join(emitted)
        assert first_id in listing and "what is a closure?" in listing

        await repl.handle(f"/switch {first_id}")
        assert repl.active_id == first_id

        assert await repl.handle("/exit") is False
        repl.finish()
        log = paths.log_path.read_text(encoding="utf-8")
        assert "chat | 1 turns across 1 conversation" in log

    async def test_file_command_files_latest_turn(self, store: WikiStore, paths: WikiPaths) -> None:
        _seed_wiki(store)
        script = [
            [ToolCall(tool="read_page", args={"page_id": "closure"})],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "page_id": "closure-note",
                        "page_kind": "synthesis",
                        "summary": "Filed closure note.",
                        "page_body": "A durable note linked to [[closure]].",
                        "sources": [],
                    },
                )
            ],
            [ToolCall(tool="finish_chat_file", args={"report": "Filed [[closure-note]]."})],
        ]
        repl, emitted = self._repl(store, paths, script)
        repl.start(resume=None)
        repl.chat_store.append_turn(
            repl.active_id,
            "what is a closure?",
            "A closure captures scope.",
            "",
            10,
            "2026-06-12T12:00:00",
        )

        assert await repl.handle("/file closure-note keep it short") is True

        assert "Filed [[closure-note]]." in emitted
        assert "A durable note linked to [[closure]]." in store.read_page("closure-note")

    async def test_file_command_requires_prior_turn(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        repl, emitted = self._repl(store, paths, script=[])
        repl.start(resume=None)

        assert await repl.handle("/file empty-note") is True

        assert any("nothing to file yet" in line for line in emitted)

    async def test_failed_turn_persists_nothing_and_continues(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        repl, emitted = self._repl(store, paths, script=[])  # script exhausted -> error
        repl.start(resume=None)
        assert await repl.handle("anything?") is True
        assert any("turn failed" in line for line in emitted)
        assert repl.chat_store.turn_count(repl.active_id) == 0
        repl.finish()  # zero turns -> no log entry
        assert "chat |" not in paths.log_path.read_text(encoding="utf-8")

    async def test_resume_latest_and_unknown_switch(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        chat_store = ChatStore(paths.root / "chat.db")
        chat_store.create_session("old-1", "2026-06-11T09:00:00")
        repl = ChatRepl(
            session=_session(store, [], paths), chat_store=chat_store, emit=lambda _: None
        )
        repl.start(resume="latest")
        assert repl.active_id == "old-1"
        emitted: list[str] = []
        repl.emit = emitted.append
        await repl.handle("/switch ghost")
        assert repl.active_id == "old-1"
        assert any("no conversation 'ghost'" in line for line in emitted)

    def test_interrupt_message_prints_runtime_resume_command(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        repl, emitted = self._repl(store, paths, script=[])
        repl.start(resume=None)
        session_id = repl.active_id

        repl.interrupt("local-4090")

        assert f"conversation {session_id} is still resumable" in "\n".join(emitted)
        assert (
            f"resume with: uv run llmwiki --runtime local-4090 chat --resume {session_id}"
            in emitted
        )

    async def test_cli_ctrl_c_prints_resume_command(
        self,
        monkeypatch: pytest.MonkeyPatch,
        store: WikiStore,
        paths: WikiPaths,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        def interrupting_input(_prompt: str) -> str:
            raise KeyboardInterrupt

        monkeypatch.setattr(builtins, "input", interrupting_input)

        result = await _run_chat(
            _session(store, [], paths),
            paths,
            resume=None,
            runtime_name="local-4090",
        )

        output = capsys.readouterr().out
        assert "resume with: uv run llmwiki --runtime local-4090 chat --resume" in output
        assert result.output.startswith("chat interrupted:")

    async def test_backend_cleanup_suppresses_late_interrupt(self) -> None:
        class InterruptingBackend:
            async def aclose(self) -> None:
                raise KeyboardInterrupt

        await _close_backend_safely(InterruptingBackend())

    async def test_backend_cleanup_suppresses_late_cancellation(self) -> None:
        class CancellingBackend:
            async def aclose(self) -> None:
                raise asyncio.CancelledError

        await _close_backend_safely(CancellingBackend())

    async def test_unknown_command_hint(self, store: WikiStore, paths: WikiPaths) -> None:
        repl, emitted = self._repl(store, paths, script=[])
        repl.start(resume=None)
        await repl.handle("/wat")
        assert any("unknown command" in line for line in emitted)
