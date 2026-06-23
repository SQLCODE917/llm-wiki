"""Bounded sentence extraction for deterministic SourceClaim planning."""

from __future__ import annotations

from llmwiki.domain.bounded_text import paragraphs, sentence_fragments, text_windows
from llmwiki.domain.planning_analysis import tokens

_MAX_PARAGRAPH_CHARS = 12_000
_MAX_CLAIM_SENTENCE_CHARS = 1_800
_MAX_CLAIM_SENTENCES_PER_UNIT = 120


def claim_sentences(text: str) -> tuple[str, ...]:
    sentences: list[str] = []
    for paragraph in tuple(paragraphs(text, _MAX_PARAGRAPH_CHARS)):
        for sentence in tuple(sentence_fragments(paragraph)):
            for fragment in tuple(text_windows(sentence, _MAX_CLAIM_SENTENCE_CHARS)):
                normalized = " ".join(fragment.split()).strip()
                if len(tokens(normalized)) >= 3:
                    sentences.append(normalized)
                    if len(sentences) >= _MAX_CLAIM_SENTENCES_PER_UNIT:
                        return tuple(sentences)
    return tuple(sentences)
