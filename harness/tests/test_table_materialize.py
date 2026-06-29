"""Table materialization regression tests."""

from __future__ import annotations

from llmwiki.domain.ledger.atoms import TablePayload
from llmwiki.domain.ledger.segments import SourceSegment
from llmwiki.domain.ledger.table_materialize import materialize_table


def test_enumerated_table_recovers_isolated_marker_row_without_absorbing_next_prefix() -> None:
    payload, reason = materialize_table(
        _segment(
            "1 First complete row.\n"
            "A prefix for the second row\n"
            "2\n"
            "continues after the marker.\n"
            "(petty)\n"
            "and then finishes.\n"
            "lowercase continuation before the next marker\n"
            "A prefix for the third row\n"
            "3 Third row starts here."
        )
    )

    assert reason is not None
    assert isinstance(payload, TablePayload)
    values = [cell.value for cell in payload.cells if cell.column_index == 1]
    assert values == [
        "First complete row.",
        "A prefix for the second row continues after the marker. (petty) and then finishes. "
        "lowercase continuation before the next marker",
        "A prefix for the third row Third row starts here.",
    ]


def _segment(text: str) -> SourceSegment:
    return SourceSegment(
        segment_id="seg-001",
        source_range_id="sr-001",
        source_locator="src.pdf",
        source_hash="0123456789abcdef",
        heading_path="H",
        structure_node_id="",
        source_order=1,
        text=text,
        segment_kind="table-block",
        evidence_ids=("ev-001",),
        source_element_ids=("el-001",),
    )
