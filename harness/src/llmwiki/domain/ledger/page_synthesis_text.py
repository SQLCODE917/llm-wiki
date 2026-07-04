"""Text helpers shared by page synthesis validators."""

from __future__ import annotations

import re

from llmwiki.domain.ledger.page_synthesis import DraftBlock

WORD_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)?", re.IGNORECASE)
SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s+")


def factual_sentences(block: DraftBlock) -> tuple[str, ...]:
    if block.block_kind not in {"paragraph", "bullet-list", "numbered-list"}:
        return ()
    return tuple(
        sentence
        for text in block_texts(block)
        for sentence in split_sentences(text)
        if sentence.strip()
    )


def block_texts(block: DraftBlock) -> tuple[str, ...]:
    if block.block_kind == "table":
        return tuple(cell for row in block.table_rows for cell in row)
    if block.items:
        return block.items
    if block.text:
        return (block.text,)
    return ()


def split_sentences(text: str) -> tuple[str, ...]:
    cleaned = " ".join(text.split()).strip()
    if not cleaned:
        return ()
    sentences = tuple(part.strip() for part in SENTENCE_END_RE.split(cleaned) if part.strip())
    return sentences or (cleaned,)


def words(text: str) -> tuple[str, ...]:
    return tuple(match.group(0).lower() for match in WORD_RE.finditer(text))


def canonical_text(text: str) -> str:
    return " ".join(words(text))


def ngrams(words_: tuple[str, ...], size: int) -> tuple[tuple[str, ...], ...]:
    if len(words_) < size:
        return ()
    return tuple(tuple(words_[index : index + size]) for index in range(len(words_) - size + 1))
