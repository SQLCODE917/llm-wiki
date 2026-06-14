"""Window builder: deterministic, budget-bound, seed-only clipping."""

from llmwiki.domain.chatwindow import (
    SEED_ANSWER_CAP_CHARS,
    QAPair,
    build_window,
    estimate_tokens,
)


def _pair(i: int, answer_chars: int = 400) -> QAPair:
    return QAPair(question=f"question {i}?", answer=f"answer {i} " + "x" * answer_chars)


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
