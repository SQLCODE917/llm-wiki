"""Chat e2e: read-only workflow, seeded turns, and the REPL's dispatch logic
— real WorkflowRunner + stores, fake LLM, no terminal."""

from fakes import FakeClient
from forge.context import ContextManager, NoCompact
from forge.core.workflow import ToolCall

from llmwiki.config import WikiPaths
from llmwiki.domain.chatwindow import QAPair
from llmwiki.domain.pages import WikiPage
from llmwiki.runtime.chat_repl import ChatRepl
from llmwiki.runtime.session import Session
from llmwiki.store import WikiStore
from llmwiki.store.chat_store import ChatStore
from llmwiki.workflows import build_chat_workflow

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
        WikiPage(
            name="closure",
            category="concept",
            summary="Functions capturing scope.",
            body="A closure captures its defining environment.",
            updated=TODAY,
        )
    )


class TestChatWorkflow:
    def test_read_only_by_construction(self, store: WikiStore) -> None:
        workflow = build_chat_workflow(store)
        assert "write_page" not in workflow.tools
        assert set(workflow.tools) == {"search_wiki", "read_index", "read_page", "respond"}

    def test_no_required_steps_grounding_is_provisioned(self, store: WikiStore) -> None:
        # A required-search step was removed on live evidence: it interrupted
        # a correct index-first flow and the forced junk search won by recency.
        assert build_chat_workflow(store).required_steps == []

    async def test_grounded_turn_carries_index_so_coverage_answers_work(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        # The measured failure: "what is this wiki about?" — the catalog is
        # now provisioned with the first message; the model can answer
        # directly from it.
        _seed_wiki(store)
        script = [
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
        await session.chat_turn("shorter please", window=(), grounded=False, tag="chat-f")
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
            [ToolCall(tool="respond", args={"message": "See [[closure]]."})],
        ]
        session = _session(store, script, paths)
        answer, transcript = await session.chat_turn(
            "what is a closure?", window=(), grounded=True, tag="chat-t1"
        )
        assert answer == "See [[closure]]."
        assert transcript is not None and transcript.exists()

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
            [ToolCall(tool="respond", args={"message": "Answer one."})],
        ]
        repl, emitted = self._repl(store, paths, script)
        repl.start(resume=None)
        first_id = repl.active_id

        assert await repl.handle("what is a closure?") is True
        assert "Answer one." in emitted
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

    async def test_unknown_command_hint(self, store: WikiStore, paths: WikiPaths) -> None:
        repl, emitted = self._repl(store, paths, script=[])
        repl.start(resume=None)
        await repl.handle("/wat")
        assert any("unknown command" in line for line in emitted)
