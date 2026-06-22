"""Small bounded text iterators for deterministic analysis."""

from __future__ import annotations

from collections.abc import Iterable, Iterator

_SENTENCE_ENDINGS = frozenset(".!?")


def paragraphs(text: str, max_chars: int) -> Iterator[str]:
    current_lines: list[str] = []
    current_chars = 0
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            yield from _flush_paragraph(current_lines)
            current_lines = []
            current_chars = 0
            continue
        for segment in text_windows(stripped, max_chars):
            segment_length = len(segment)
            if current_lines and current_chars + segment_length + 1 > max_chars:
                yield from _flush_paragraph(current_lines)
                current_lines = []
                current_chars = 0
            current_lines.append(segment)
            current_chars += segment_length + 1
    yield from _flush_paragraph(current_lines)


def sentence_fragments(paragraph: str) -> Iterator[str]:
    start = 0
    index = 0
    while index < len(paragraph):
        if (
            paragraph[index] in _SENTENCE_ENDINGS
            and (index + 1 == len(paragraph) or paragraph[index + 1].isspace())
        ):
            yield paragraph[start : index + 1]
            start = index + 1
        index += 1
    if start < len(paragraph):
        yield paragraph[start:]


def text_windows(text: str, max_chars: int) -> Iterator[str]:
    start = 0
    text_length = len(text)
    while start < text_length:
        end = min(start + max_chars, text_length)
        if end < text_length:
            split = text.rfind(" ", start, end)
            if split <= start:
                split = end
        else:
            split = end
        segment = text[start:split].strip()
        if segment:
            yield segment
        start = split
        while start < text_length and text[start].isspace():
            start += 1


def _flush_paragraph(lines: list[str]) -> Iterable[str]:
    if lines:
        yield " ".join(lines)
