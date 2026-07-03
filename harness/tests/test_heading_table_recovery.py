"""Heading-led numbered table recovery tests."""

from __future__ import annotations

from pathlib import Path

import pymupdf  # type: ignore[import-untyped]

from llmwiki.domain.ledger.atoms import TablePayload
from llmwiki.domain.ledger.segments import SourceSegment
from llmwiki.domain.ledger.table_materialize import materialize_table
from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.heading_table_recovery import heading_numbered_table_candidates
from llmwiki.pdf.layout_lines import page_lines
from llmwiki.pdf.table_candidate_model import TableCandidate
from llmwiki.pdf.table_extractor import (
    _degraded_fragment_ids,
    _enrich_document_model_with_tables_in_process,
    _norm,
)


def test_heading_numbered_table_uses_reading_order_and_normalizes_cells(tmp_path: Path) -> None:
    pdf = tmp_path / "numbered.pdf"
    _make_heading_numbered_pdf(pdf)

    with pymupdf.open(pdf) as doc:  # type: ignore[no-untyped-call]
        lines = tuple(page_lines(page, page_index) for page_index, page in enumerate(doc))
        candidate = heading_numbered_table_candidates(doc, lines)[0]

    payload, reason = materialize_table(_segment(candidate.raw_text))

    assert reason is not None
    assert isinstance(payload, TablePayload)
    values = [cell.value for cell in payload.cells if cell.column_index == 1]
    assert values == [
        "Alpha (small) value.",
        "Beta closes.",
        "Gamma starts before break. continues (small) value.",
    ]


def test_clean_heading_candidate_replaces_degraded_existing_table(tmp_path: Path) -> None:
    pdf = tmp_path / "numbered.pdf"
    _make_heading_numbered_pdf(pdf)
    bad = "Outcomes\nD20 Result\n1 Alpha ( small ) value .\n(\nsmall\n)\n3 bad"
    model = DocumentModel(
        source_locator="numbered.pdf",
        source_hash="abc",
        extractor_name="test",
        extractor_version="test",
        elements=(
            DocumentElement(
                "heading", "heading", "body", "Outcomes", 1, 1, "Outcomes", "# Outcomes"
            ),
            DocumentElement("bad-table", "table", "body", "Outcomes", 1, 2, bad, bad),
        ),
    )

    enriched = _enrich_document_model_with_tables_in_process(pdf, model)

    tables = [element for element in enriched.elements if element.element_kind == "table"]
    assert len(tables) == 1
    assert tables[0].element_id.startswith("fallback-table-")
    assert "Gamma starts before break." in tables[0].text


def test_captionless_forward_table_preserves_source_heading(tmp_path: Path) -> None:
    pdf = tmp_path / "forward.pdf"
    _make_forward_cue_pdf(pdf)
    model = DocumentModel(
        source_locator="forward.pdf",
        source_hash="abc",
        extractor_name="test",
        extractor_version="test",
        elements=(
            DocumentElement("heading", "heading", "body", "Events", 1, 1, "Events", "# Events"),
            DocumentElement(
                "cue",
                "paragraph",
                "body",
                "Events",
                1,
                1,
                "Roll on the table below.",
                "Roll on the table below.",
                layout_y0=104.0,
            ),
            DocumentElement(
                "degraded-row-1",
                "paragraph",
                "body",
                "Events",
                1,
                1,
                "1 Change First event.",
                "1 Change First event.",
                layout_y0=132.0,
            ),
            DocumentElement(
                "degraded-row-2",
                "paragraph",
                "body",
                "Events",
                1,
                1,
                "2 Delay Second event.",
                "2 Delay Second event.",
                layout_y0=164.0,
            ),
        ),
    )

    enriched = _enrich_document_model_with_tables_in_process(pdf, model)

    tables = [element for element in enriched.elements if element.element_kind == "table"]
    element_ids = {element.element_id for element in enriched.elements}
    assert len(tables) == 1
    assert tables[0].text.splitlines()[:3] == [
        "Events",
        "1 Change First event.",
        "2 Delay Second event.",
    ]
    assert "degraded-row-1" not in element_ids
    assert "degraded-row-2" not in element_ids


def test_degraded_fragment_matching_normalizes_ocr_ligatures() -> None:
    assert _norm("Dex modiﬁer") == _norm("Dex modifier")
    assert _norm("Whistle ( petty ) .") == _norm("Whistle (petty).")


def test_degraded_fragment_cleanup_bridges_split_cell_fragments() -> None:
    raw_text = "\n".join(
        [
            "Items",
            "D20",
            "Result",
            "1",
            "Take a Token (small) woven from thread.",
            "2",
            "Use the second result.",
        ]
    )
    candidate = TableCandidate(
        caption="",
        page_start=1,
        page_end=1,
        y0=100.0,
        raw_text=raw_text,
        extractor_stage="heading-numbered-layout",
    )
    elements = [
        _element("heading", "heading", "Items"),
        _element("row-start", "paragraph", "1 Take a Token"),
        _element("split-cell", "paragraph", "small Token"),
        _element("split-paren", "paragraph", ") woven from thread."),
        _element("row-two", "list_item", "2 Use the second result."),
        _element("after-table", "paragraph", "brief note"),
    ]

    skipped = _degraded_fragment_ids(elements, 1, candidate, raw_text)

    assert skipped == {"row-start", "split-cell", "split-paren", "row-two"}


def _make_heading_numbered_pdf(path: Path) -> None:
    doc = pymupdf.open()
    page = doc.new_page()
    page.insert_text((72, 72), "Outcomes")
    page.insert_text((72, 104), "D20")
    page.insert_text((112, 104), "Result")
    page.insert_text((72, 132), "1")
    page.insert_text((112, 132), "Alpha ( small ) value .")
    page.insert_text((72, 164), "2")
    page.insert_text((112, 164), "Beta closes.")
    page.insert_text((112, 760), "Gamma starts before break.")
    page = doc.new_page()
    page.insert_text((72, 72), "3")
    page.insert_text((112, 72), "continues ( small ) value .")
    page.insert_text((72, 120), "Next Section")
    doc.save(str(path))
    doc.close()


def _make_forward_cue_pdf(path: Path) -> None:
    doc = pymupdf.open()
    page = doc.new_page()
    page.insert_text((72, 72), "Events")
    page.insert_text((72, 104), "Roll on the table below.")
    page.insert_text((72, 132), "1")
    page.insert_text((112, 132), "Change")
    page.insert_text((172, 132), "First event.")
    page.insert_text((72, 164), "2")
    page.insert_text((112, 164), "Delay")
    page.insert_text((172, 164), "Second event.")
    doc.save(str(path))
    doc.close()


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


def _element(element_id: str, kind: str, text: str) -> DocumentElement:
    return DocumentElement(
        element_id=element_id,
        element_kind=kind,
        body_state="body",
        heading_path="Items",
        page_start=1,
        page_end=1,
        text=text,
        markdown=text,
    )
