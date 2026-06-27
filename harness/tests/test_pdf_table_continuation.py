"""PDF table continuation tests for page-spanning numbered tables."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from llmwiki.pdf.table_geometry_repair import preface_numbered_table_text


@dataclass(frozen=True)
class FakeRect:
    height: float


@dataclass(frozen=True)
class FakeRow:
    cells: tuple[tuple[float, float, float, float], ...]


@dataclass(frozen=True)
class FakeTable:
    bbox: tuple[float, float, float, float]
    rows: tuple[FakeRow, ...]


class PageOne:
    rect = FakeRect(height=100)

    def get_text(self, mode: str, sort: bool = True) -> tuple[tuple[Any, ...], ...]:
        assert mode == "words"
        return (
            (80, 10, 100, 20, "Roll", 0, 0, 0),
            (104, 10, 116, 20, "on", 0, 0, 1),
            (10, 74, 18, 84, "1", 0, 1, 0),
            (25, 74, 60, 84, "Delay", 0, 1, 1),
            (80, 74, 122, 84, "Continue", 0, 1, 2),
            (126, 74, 138, 84, "to", 0, 1, 3),
        )


class PageTwo:
    rect = FakeRect(height=100)

    def get_text(self, mode: str, sort: bool = True) -> tuple[tuple[Any, ...], ...]:
        assert mode == "words"
        return (
            (80, 10, 125, 20, "resolve.", 0, 0, 0),
            (10, 28, 18, 38, "2", 0, 1, 0),
            (25, 28, 56, 38, "Prize", 0, 1, 1),
            (80, 28, 120, 38, "Recover.", 0, 1, 2),
            (80, 60, 130, 70, "Next Section", 0, 2, 0),
        )


def test_preface_numbered_table_reads_top_of_next_page_continuation() -> None:
    text = preface_numbered_table_text(
        PageOne(),
        FakeTable(
            bbox=(0, 8, 170, 96),
            rows=(
                FakeRow(cells=((0, 8, 22, 24), (22, 8, 76, 24), (76, 8, 170, 24))),
                FakeRow(cells=((0, 70, 22, 90), (22, 70, 76, 90), (76, 70, 170, 90))),
            ),
        ),
        (("", "", "Roll on"), ("1", "Delay", "Continue to")),
        PageTwo(),
    )

    assert text == "Roll on\n1 Delay Continue to resolve.\n2 Prize Recover."
