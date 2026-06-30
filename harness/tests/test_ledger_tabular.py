"""Source-neutral tabular row detector tests."""

from __future__ import annotations

from llmwiki.domain.ledger.tabular import range_value_entries, row_marker_count


def test_row_marker_count_bounds_large_flattened_text() -> None:
    text = ("ordinary prose " * 100_000) + "\n1 Alpha\n2 Beta\n3 Gamma"

    assert row_marker_count(text) == 3


def test_range_value_entries_scans_large_input_in_windows() -> None:
    text = ("ordinary prose " * 20_000) + " 1-2 +3" + (" filler " * 8_000) + " 3-4 +2 5-6 +1"

    assert range_value_entries(text) == (("1-2", "+3"), ("3-4", "+2"), ("5-6", "+1"))
