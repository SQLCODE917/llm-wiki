"""ChatStore: verbatim persistence, derived navigation, never-closed sessions."""

from pathlib import Path

import pytest

from llmwiki.store.chat_store import SCHEMA_VERSION, ChatStore, ChatStoreError


@pytest.fixture
def chat_store(tmp_path: Path) -> ChatStore:
    return ChatStore(tmp_path / "chat.db")


class TestSessions:
    def test_create_list_latest(self, chat_store: ChatStore) -> None:
        chat_store.create_session("s-1", "2026-06-12T10:00:00")
        chat_store.create_session("s-2", "2026-06-12T11:00:00")
        assert chat_store.latest_session_id() == "s-2"
        listed = chat_store.list_sessions()
        assert [s.session_id for s in listed] == ["s-2", "s-1"]
        assert listed[0].turn_count == 0 and listed[0].first_question == ""

    def test_duplicate_id_rejected(self, chat_store: ChatStore) -> None:
        chat_store.create_session("s-1", "2026-06-12T10:00:00")
        with pytest.raises(ChatStoreError, match="already exists"):
            chat_store.create_session("s-1", "2026-06-12T10:01:00")

    def test_activity_reorders_latest(self, chat_store: ChatStore) -> None:
        chat_store.create_session("s-1", "2026-06-12T10:00:00")
        chat_store.create_session("s-2", "2026-06-12T11:00:00")
        chat_store.append_turn("s-1", "q", "a", "", 2, "2026-06-12T12:00:00")
        assert chat_store.latest_session_id() == "s-1"

    def test_schema_version_stamped(self, tmp_path: Path) -> None:
        store = ChatStore(tmp_path / "chat.db")
        version = store._conn.execute("PRAGMA user_version").fetchone()[0]
        assert version == SCHEMA_VERSION


class TestTurns:
    def test_append_and_history_ordered_verbatim(self, chat_store: ChatStore) -> None:
        chat_store.create_session("s-1", "2026-06-12T10:00:00")
        long_answer = "verbatim " * 1000  # way past any seed clip
        assert chat_store.append_turn("s-1", "q1", "a1", "t1.jsonl", 2, "2026-06-12T10:01:00") == 1
        assert (
            chat_store.append_turn("s-1", "q2", long_answer, "t2.jsonl", 9, "2026-06-12T10:02:00")
            == 2
        )
        history = chat_store.history("s-1")
        assert [p.question for p in history] == ["q1", "q2"]
        assert history[1].answer == long_answer  # never truncated in storage
        assert chat_store.turn_count("s-1") == 2

    def test_first_question_labels_listing(self, chat_store: ChatStore) -> None:
        chat_store.create_session("s-1", "2026-06-12T10:00:00")
        chat_store.append_turn("s-1", "what is a closure?", "a", "", 2, "2026-06-12T10:01:00")
        assert chat_store.list_sessions()[0].first_question == "what is a closure?"

    def test_turn_for_unknown_session_rejected(self, chat_store: ChatStore) -> None:
        with pytest.raises(ChatStoreError, match="no conversation"):
            chat_store.append_turn("ghost", "q", "a", "", 1, "2026-06-12T10:00:00")

    def test_histories_are_per_session(self, chat_store: ChatStore) -> None:
        chat_store.create_session("s-1", "2026-06-12T10:00:00")
        chat_store.create_session("s-2", "2026-06-12T10:00:01")
        chat_store.append_turn("s-1", "q-one", "a", "", 1, "2026-06-12T10:01:00")
        chat_store.append_turn("s-2", "q-two", "a", "", 1, "2026-06-12T10:02:00")
        assert [p.question for p in chat_store.history("s-1")] == ["q-one"]
        assert [p.question for p in chat_store.history("s-2")] == ["q-two"]
