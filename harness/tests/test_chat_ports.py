"""Contract tests for portable chat orchestration seams."""

from llmwiki.domain.chat_response_gate import (
    ChatResponseEvidenceState,
    ChatResponseGateConfig,
    decide_chat_response,
)
from llmwiki.domain.chat_turn_context import build_chat_turn_context
from llmwiki.domain.pages import PageMetadata, WikiPage, render_page


def _page(
    page_id: str,
    *,
    page_kind: str = "source",
    page_family: str = "section-reference",
    body: str = "Body.",
) -> str:
    return render_page(
        WikiPage.from_metadata(
            PageMetadata(
                page_id=page_id,
                page_kind=page_kind,
                page_family=page_family,
                summary=f"{page_id} summary.",
            ),
            body,
        )
    )


class TestChatTurnContext:
    def test_context_builds_task_pack_without_store_or_workflow_objects(self) -> None:
        pages = {
            "book-procedure-create-character": _page(
                "book-procedure-create-character",
                page_kind="procedure",
                page_family="procedure-guide",
                body=(
                    "# Create Character\n\n"
                    "1. **Choose Race** (`choose`) - evidence section [[book-race]].\n"
                    "2. **Record Name** (`record`) - evidence section [[book-name]].\n"
                ),
            ),
            "book-race": _page("book-race", body="# Race\n\nHuman is a race choice."),
            "book-name": _page("book-name", body="# Name\n\nRecord a name."),
        }

        context = build_chat_turn_context(
            "actually create a character",
            page_texts=pages,
            index_text="",
            grounded=False,
            has_window=False,
        )

        assert context.require_procedure_execution
        assert context.task_evidence_pack is not None
        assert context.task_evidence_pack.procedure_id == "book-procedure-create-character"
        assert "[[book-race]]" in context.task_evidence_pack_text

    def test_context_keeps_followup_turns_conversation_only(self) -> None:
        context = build_chat_turn_context(
            "shorter please",
            page_texts={"topic": _page("topic")},
            index_text="- [[topic]] - Topic.",
            grounded=False,
            has_window=True,
        )

        assert not context.require_wiki_read
        assert context.search_results == ""
        assert context.task_evidence_pack is None


class TestChatResponseGate:
    def test_gate_rejects_procedure_response_before_valid_execution(self) -> None:
        decision = decide_chat_response(
            "Done. [[book-procedure-create-character]]",
            config=ChatResponseGateConfig(require_procedure_execution=True),
            evidence=ChatResponseEvidenceState(
                read_page_ids=frozenset({"book-procedure-create-character"}),
                procedure_execution_satisfied=False,
            ),
        )

        assert not decision.allowed
        assert "submit_procedure_execution" in decision.message

    def test_gate_accepts_read_page_citation(self) -> None:
        decision = decide_chat_response(
            "The rule is here: [[book-race]].",
            config=ChatResponseGateConfig(
                require_wiki_read=True,
                require_read_page_citation=True,
            ),
            evidence=ChatResponseEvidenceState(read_page_ids=frozenset({"book-race"})),
        )

        assert decision.allowed

    def test_gate_rejects_missing_coverage_without_local_citation(self) -> None:
        decision = decide_chat_response(
            "The wiki does not have that procedure. Try another source?",
            config=ChatResponseGateConfig(require_wiki_read=False),
            evidence=ChatResponseEvidenceState(
                missing_focus_reports=frozenset({"raw/book.pdf::character creation"})
            ),
        )

        assert not decision.allowed
        assert "missing inspected wiki page citation" in decision.message
