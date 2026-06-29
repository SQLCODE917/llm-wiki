from llmwiki.domain.evidence_registry import SourceRange, SourceText
from llmwiki.domain.technical_table_detection import detect_technical_tables


def test_detected_table_ignores_non_positive_page_markers() -> None:
    source_text = SourceText(
        source_locator="book.pdf",
        source_hash="hash",
        source_text_kind="pdf-cache",
        lines=(
            "0",
            "| Item | Value |",
            "| --- | --- |",
            "| Alpha | 1 |",
        ),
    )
    source_range = SourceRange(
        source_range_id="range-1",
        page_id="page-1",
        source_locator="book.pdf",
        page_range=(0, 0),
        line_range=(2, 4),
        heading_path="Tables",
    )

    tables = detect_technical_tables(
        unit_text="| Item | Value |\n| --- | --- |\n| Alpha | 1 |",
        source_text=source_text,
        source_range=source_range,
    )

    assert len(tables) == 1
    block = tables[0].blocks[0]
    assert block.page_range is None
    assert block.line_range == (2, 4)
