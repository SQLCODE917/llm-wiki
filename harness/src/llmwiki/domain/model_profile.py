"""Model capabilities and derived source-processing budgets."""

from __future__ import annotations

from dataclasses import dataclass

BASELINE_CONTEXT_TOKENS = 16_384
DEFAULT_MODEL_ID = "qwen3-coder:30b"


@dataclass(frozen=True)
class ModelProfile:
    model_id: str
    context_window_tokens: int
    chars_per_token_estimate: int = 4

    def estimate_tokens(self, text: str) -> int:
        return max(1, len(text) // self.chars_per_token_estimate) if text else 0

    def chars_for_tokens(self, tokens: int) -> int:
        return tokens * self.chars_per_token_estimate

    @property
    def source_chunk_tokens(self) -> int:
        return self._scaled_tokens(6_000, minimum=512)

    @property
    def source_write_group_tokens(self) -> int:
        return self._scaled_tokens(2_200, minimum=256)

    @property
    def raw_source_read_chars(self) -> int:
        return self._scaled_chars(24_000, minimum=4_000)

    @property
    def read_page_default_chars(self) -> int:
        return self._scaled_chars(3_000, minimum=800)

    @property
    def read_page_max_chars(self) -> int:
        return max(self.read_page_default_chars, self._scaled_chars(5_000, minimum=1_200))

    @property
    def evidence_pack_prompt_tokens(self) -> int:
        return self._scaled_tokens(8_000, minimum=1_500)

    def _scaled_tokens(self, baseline_tokens: int, *, minimum: int) -> int:
        scaled = round(baseline_tokens * self.context_window_tokens / BASELINE_CONTEXT_TOKENS)
        return max(minimum, scaled)

    def _scaled_chars(self, baseline_chars: int, *, minimum: int) -> int:
        scaled = round(baseline_chars * self.context_window_tokens / BASELINE_CONTEXT_TOKENS)
        return max(minimum, scaled)


def qwen3_coder_30b_profile(
    context_window_tokens: int = BASELINE_CONTEXT_TOKENS,
) -> ModelProfile:
    return ModelProfile(DEFAULT_MODEL_ID, context_window_tokens)


DEFAULT_MODEL_PROFILE = qwen3_coder_30b_profile()
