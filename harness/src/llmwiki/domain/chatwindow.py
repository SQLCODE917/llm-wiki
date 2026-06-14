"""Deterministic chat context window (pure).

The design's memory rule (docs/2026-06-12-persistent-chat-design.md):
conversation = Q/A pairs, evidence is re-fetched, prior answers are not
evidence. The window is the most recent pairs that fit a token budget —
no model-curated summaries, no retrieval. Clipping happens only in the
seed copies produced here; stored turns stay verbatim (preservation
guarantee).
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, replace

# Seed budget from the design's 16K table: ~2.5K system + window + current
# question + tool headroom + generation. Awaiting tuning on real sessions.
WINDOW_TOKEN_BUDGET = 6000
# Per-answer clip in the SEED COPY only; stored answers are never truncated.
SEED_ANSWER_CAP_CHARS = 2000

_CHARS_PER_TOKEN = 4  # same rough estimate used across the harness


def estimate_tokens(text: str) -> int:
    return len(text) // _CHARS_PER_TOKEN


@dataclass(frozen=True)
class QAPair:
    """One conversation turn as seeded context: question and answer text only."""

    question: str
    answer: str

    @property
    def token_estimate(self) -> int:
        return estimate_tokens(self.question) + estimate_tokens(self.answer)


def _clip_for_seed(pair: QAPair) -> QAPair:
    if len(pair.answer) <= SEED_ANSWER_CAP_CHARS:
        return pair
    return replace(pair, answer=pair.answer[: SEED_ANSWER_CAP_CHARS - 1] + "…")


def build_window(
    history: Sequence[QAPair], budget_tokens: int = WINDOW_TOKEN_BUDGET
) -> tuple[QAPair, ...]:
    """Most recent pairs fitting the budget, in chronological order.

    Selection walks newest-first and stops at the first pair that would
    exceed the budget — a contiguous recent window, no gaps the model
    would misread as continuity.
    """
    window: list[QAPair] = []
    used = 0
    for pair in reversed(history):
        clipped = _clip_for_seed(pair)
        cost = clipped.token_estimate
        if used + cost > budget_tokens:
            break
        window.append(clipped)
        used += cost
    return tuple(reversed(window))
