"""Source-neutral stream table grid reconstruction tests."""

from __future__ import annotations

from llmwiki.pdf.layout_lines import TextLine, WordBox
from llmwiki.pdf.table_grid_reconstruction import reconstruct_table_grid


def test_stream_grid_reconstruction_merges_wrapped_cells_and_groups() -> None:
    lines = (
        _line(0, 10, [(100, "Table- Sample Loadout")]),
        _line(1, 20, [(100, "Item"), (160, "Cost"), (220, "Rating"), (300, "Flag")]),
        _line(2, 32, [(220, "(AC)")]),
        _line(3, 44, [(100, "Light")]),
        _line(4, 56, [(100, "Kit")]),
        _line(5, 68, [(220, "11"), (238, "+"), (252, "Dex")]),
        _line(6, 74, [(100, "Padded"), (160, "5"), (174, "gp"), (300, "Disadvantage")]),
        _line(7, 80, [(220, "modifier")]),
        _line(8, 94, [(100, "Studded"), (220, "12"), (238, "+"), (252, "Dex")]),
        _line(9, 100, [(160, "45"), (174, "gp"), (300, "-")]),
        _line(10, 106, [(100, "leather"), (220, "modifier")]),
    )

    grid = reconstruct_table_grid(lines)

    assert grid is not None
    assert "| Category | Item | Cost | Rating (AC) | Flag |" in grid.raw_text
    assert "| Light Kit | Padded | 5 gp | 11 + Dex modifier | Disadvantage |" in grid.raw_text
    assert "|  | Studded leather | 45 gp | 12 + Dex modifier | - |" in grid.raw_text


def _line(index: int, y0: float, words: list[tuple[float, str]]) -> TextLine:
    boxes = tuple(
        WordBox(x0, y0, x0 + max(6.0, len(text) * 5.0), y0 + 10.0, text) for x0, text in words
    )
    return TextLine(index, y0, y0 + 10.0, boxes)
