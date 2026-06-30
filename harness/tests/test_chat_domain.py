"""Window builder: deterministic, budget-bound, seed-only clipping."""

from llmwiki.domain.chat_grounding import (
    ChatEvidenceMode,
    ChatEvidenceScope,
    ChatResponseCitationPolicy,
    ChatTaskMode,
    plan_chat_grounding,
    render_grounded_user_message,
)
from llmwiki.domain.chatwindow import (
    SEED_ANSWER_CAP_CHARS,
    QAPair,
    build_window,
    estimate_tokens,
)
from llmwiki.domain.pages import parse_page
from llmwiki.domain.search import SearchHit


def _pair(i: int, answer_chars: int = 400) -> QAPair:
    return QAPair(question=f"question {i}?", answer=f"answer {i} " + "x" * answer_chars)


def _page(page_id: str, page_family: str) -> str:
    family = f"page_family: {page_family}\n" if page_family else ""
    return (
        "---\n"
        f"page_id: {page_id}\n"
        "page_kind: source\n"
        f"{family}"
        f"summary: {page_id} summary.\n"
        "---\n\n"
        f"# {page_id}\n"
    )


class TestBuildWindow:
    def test_keeps_most_recent_that_fit_in_order(self) -> None:
        history = [_pair(i) for i in range(10)]  # ~100 tokens each
        window = build_window(history, budget_tokens=350)
        assert [p.question for p in window] == ["question 7?", "question 8?", "question 9?"]

    def test_everything_fits_when_budget_allows(self) -> None:
        history = [_pair(i) for i in range(3)]
        assert build_window(history, budget_tokens=10_000) == tuple(history)

    def test_empty_history(self) -> None:
        assert build_window([]) == ()

    def test_oversized_answer_clipped_in_seed_only(self) -> None:
        original = _pair(1, answer_chars=SEED_ANSWER_CAP_CHARS * 3)
        history = [original]
        window = build_window(history, budget_tokens=10_000)
        assert len(window[0].answer) == SEED_ANSWER_CAP_CHARS
        assert window[0].answer.endswith("…")
        # The stored object is untouched (preservation guarantee).
        assert len(original.answer) > SEED_ANSWER_CAP_CHARS

    def test_window_is_contiguous_no_gaps(self) -> None:
        # One huge old answer must stop the walk, not be skipped over.
        history = [_pair(0), _pair(1, answer_chars=8_000), _pair(2), _pair(3)]
        window = build_window(history, budget_tokens=300)
        assert [p.question for p in window] == ["question 2?", "question 3?"]

    def test_token_estimate_sanity(self) -> None:
        assert estimate_tokens("x" * 400) == 100


class TestChatGrounding:
    def test_catalog_question_uses_index(self) -> None:
        plan = plan_chat_grounding("What does this wiki cover?", grounded=False, has_window=True)

        assert plan.evidence_mode is ChatEvidenceMode.CATALOG_OR_PAGE
        assert plan.include_index
        assert not plan.include_search_results

    def test_style_followup_uses_conversation_window(self) -> None:
        plan = plan_chat_grounding("shorter please", grounded=False, has_window=True)

        assert plan.evidence_mode is ChatEvidenceMode.CONVERSATION
        assert not plan.require_wiki_read
        assert not plan.include_search_results

    def test_resumed_fresh_lookup_uses_page_grounding(self) -> None:
        plan = plan_chat_grounding("fresh topic label", grounded=False, has_window=True)

        assert plan.evidence_mode is ChatEvidenceMode.PAGE
        assert plan.require_wiki_read
        assert plan.include_search_results

    def test_how_to_question_explains_procedure(self) -> None:
        plan = plan_chat_grounding(
            "how do I create a Sword World RPG character?", grounded=False, has_window=False
        )

        assert plan.task_mode is ChatTaskMode.EXPLAIN_PROCEDURE
        message = render_grounded_user_message(
            "how do I create a Sword World RPG character?",
            plan,
            search_results="[[book-procedure-create-character]]",
        )
        assert "Task intent: explain the relevant procedure" in message
        assert "Prefer procedure pages" in message

    def test_creation_request_executes_procedure(self) -> None:
        plan = plan_chat_grounding(
            "actually create a Sword World RPG character", grounded=False, has_window=True
        )

        assert plan.task_mode is ChatTaskMode.EXECUTE_PROCEDURE
        message = render_grounded_user_message(
            "actually create a Sword World RPG character",
            plan,
            search_results="[[book-procedure-create-character]]",
        )
        assert "Task intent: execute the relevant procedure" in message
        assert "not merely summarize it" in message
        assert "make explicit assumptions" in message
        assert "not a future-tense plan" in message
        assert "one concrete result or explicit unresolved note" in message

    def test_source_material_comparison_uses_page_grounding(self) -> None:
        plan = plan_chat_grounding(
            "compare that character with the source material", grounded=False, has_window=True
        )

        assert plan.evidence_mode is ChatEvidenceMode.PAGE
        assert plan.include_search_results
        assert plan.task_mode is ChatTaskMode.SOURCE_AUDIT
        message = render_grounded_user_message(
            "compare that character with the source material",
            plan,
            search_results="[[book-procedure-create-character]]",
        )
        assert "Task intent: audit a previous answer against source material" in message
        assert "Report matches, mismatches, unsupported fields, and corrections" in message


class TestChatEvidenceScope:
    def test_rejects_aggregate_page_when_focused_candidate_is_stronger(self) -> None:
        pages = {
            "book": _page("book", "source-manifest"),
            "book-section": _page("book-section", "section-reference"),
        }
        scope = ChatEvidenceScope.from_search_hits(
            pages,
            (
                SearchHit("book-section", 247, "focused"),
                SearchHit("book", 227, "aggregate"),
            ),
        )
        metadata = parse_page(pages["book"]).page_metadata

        decision = scope.read_decision(metadata)

        assert not decision.allowed
        assert "[[book-section]]" in decision.message
        assert "source-manifest" in decision.message

    def test_allows_aggregate_page_when_it_is_the_strongest_candidate(self) -> None:
        pages = {
            "book": _page("book", "source-manifest"),
            "book-section": _page("book-section", "section-reference"),
        }
        scope = ChatEvidenceScope.from_search_hits(
            pages,
            (
                SearchHit("book", 500, "aggregate"),
                SearchHit("book-section", 247, "focused"),
            ),
        )
        metadata = parse_page(pages["book"]).page_metadata

        decision = scope.read_decision(metadata)

        assert decision.allowed

    def test_allows_aggregate_page_when_no_focused_candidate_exists(self) -> None:
        pages = {"book": _page("book", "source-manifest")}
        scope = ChatEvidenceScope.from_search_hits(
            pages,
            (SearchHit("book", 227, "aggregate"),),
        )
        metadata = parse_page(pages["book"]).page_metadata

        decision = scope.read_decision(metadata)

        assert decision.allowed


class TestChatResponseCitationPolicy:
    def test_accepts_link_to_read_page(self) -> None:
        policy = ChatResponseCitationPolicy(frozenset({"book-section"}))

        decision = policy.response_decision(
            "The answer is grounded in [[book-section]] (raw/book.pdf)."
        )

        assert decision.allowed

    def test_rejects_raw_source_without_wiki_page_link(self) -> None:
        policy = ChatResponseCitationPolicy(frozenset({"book-section"}))

        decision = policy.response_decision("The answer only cites (raw/book.pdf).")

        assert not decision.allowed
        assert "[[book-section]]" in decision.message
        assert "Raw source citations alone are not enough" in decision.message

    def test_rejects_link_to_unread_page(self) -> None:
        policy = ChatResponseCitationPolicy(frozenset({"book-section"}))

        decision = policy.response_decision("The answer cites [[other-section]].")

        assert not decision.allowed
