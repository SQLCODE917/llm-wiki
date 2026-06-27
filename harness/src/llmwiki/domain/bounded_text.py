"""Small bounded text iterators for deterministic analysis."""

from __future__ import annotations

_SENTENCE_ENDINGS = frozenset(".!?")


def paragraphs(text: str, max_chars: int) -> tuple[str, ...]:
    result: list[str] = []
    current_lines: list[str] = []
    current_chars = 0
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            _append_paragraph(result, current_lines)
            current_lines = []
            current_chars = 0
            continue
        for segment in text_windows(stripped, max_chars):
            segment_length = len(segment)
            if current_lines and current_chars + segment_length + 1 > max_chars:
                _append_paragraph(result, current_lines)
                current_lines = []
                current_chars = 0
            current_lines.append(segment)
            current_chars += segment_length + 1
    _append_paragraph(result, current_lines)
    return tuple(result)


def sentence_fragments(paragraph: str) -> tuple[str, ...]:
    result: list[str] = []
    start = 0
    paragraph_length = len(paragraph)
    for index, character in enumerate(paragraph):
        if character in _SENTENCE_ENDINGS and (
            index + 1 >= paragraph_length or paragraph[index + 1].isspace()
        ):
            result.append(paragraph[start : index + 1])
            start = index + 1
    if start < paragraph_length:
        result.append(paragraph[start:])
    return tuple(result)


def text_windows(text: str, max_chars: int) -> tuple[str, ...]:
    if max_chars <= 0:
        return ()
    result: list[str] = []
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
            result.append(segment)
        start = split
        while start < text_length and text[start].isspace():
            start += 1
    return tuple(result)


def _append_paragraph(result: list[str], lines: list[str]) -> None:
    if lines:
        result.append(" ".join(lines))
