"""Page text geometry helpers shared by PDF table recovery adapters."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class WordBox:
    x0: float
    y0: float
    x1: float
    y1: float
    text: str

    @property
    def cy(self) -> float:
        return (self.y0 + self.y1) / 2.0


@dataclass(frozen=True)
class TextLine:
    page_index: int
    y0: float
    y1: float
    words: tuple[WordBox, ...]

    @property
    def text(self) -> str:
        return " ".join(word.text for word in self.words)

    @property
    def cy(self) -> float:
        return (self.y0 + self.y1) / 2.0


def page_words(page: Any) -> tuple[WordBox, ...]:
    return tuple(
        WordBox(float(x0), float(y0), float(x1), float(y1), str(text))
        for x0, y0, x1, y1, text, *_rest in page.get_text("words", sort=True)
        if str(text).strip()
    )


def page_lines(page: Any, page_index: int) -> tuple[TextLine, ...]:
    words = page_words(page)
    lines: list[list[WordBox]] = []
    for word in words:
        if not lines or abs(lines[-1][0].y0 - word.y0) > 3.0:
            lines.append([word])
        else:
            lines[-1].append(word)
    return tuple(
        TextLine(
            page_index, min(word.y0 for word in line), max(word.y1 for word in line), tuple(line)
        )
        for line in lines
        if line
    )


def layout_text(lines: tuple[TextLine, ...]) -> str:
    words = tuple(word for line in lines for word in line.words)
    if not words:
        return ""
    left = min(word.x0 for word in words)
    scale = 5.0
    rendered: list[str] = []
    for line in lines:
        cursor = 0
        parts: list[str] = []
        for word in line.words:
            col = max(0, int((word.x0 - left) / scale))
            spaces = max(1, col - cursor)
            parts.append(" " * spaces + word.text)
            cursor = col + len(word.text)
        rendered.append("".join(parts).rstrip())
    return "\n".join(rendered).strip()


def join_words(words: tuple[WordBox, ...]) -> str:
    return " ".join(
        word.text for word in sorted(words, key=lambda item: (int(item.y0 / 3.0), item.x0))
    )
