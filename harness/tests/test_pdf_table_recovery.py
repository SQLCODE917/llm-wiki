"""PDF table recovery tests against source-neutral layout patterns."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pymupdf  # type: ignore[import-untyped]

from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.pipeline import chunk_file, ensure_extracted
from llmwiki.pdf.recognizer import NullRecognizer
from llmwiki.pdf.table_geometry_repair import geometry_table_rows, preface_numbered_table_text

_PAGE_PROSE = "Functions are first-class values. " * 40


def _make_forward_cue_table_pdf(path: Path) -> None:
    doc = pymupdf.open()
    page = doc.new_page()
    page.insert_text((72, 72), "Sample Outcomes")
    page.insert_text((72, 100), "Roll on the table below.")
    page.insert_text((230, 130), "Alpha result keeps separate words.")
    page.insert_text((90, 136), "1 Trial")
    page.insert_text((230, 160), "Beta result keeps spaces.")
    page.insert_text((90, 166), "2 Review")
    page.insert_text((72, 210), "Follow-up Notes")
    page.insert_textbox(pymupdf.Rect(72, 260, 540, 520), _PAGE_PROSE)
    doc.save(str(path))
    doc.close()


def _make_forward_cue_without_table_pdf(path: Path) -> None:
    doc = pymupdf.open()
    page = doc.new_page()
    page.insert_text((72, 72), "Sample Outcomes")
    page.insert_text((72, 100), "See the table below for details.")
    page.insert_text((72, 130), "Ordinary prose continues without numbered rows.")
    page.insert_text((72, 160), "Another sentence still belongs to the paragraph.")
    page.insert_textbox(pymupdf.Rect(72, 220, 540, 520), _PAGE_PROSE)
    doc.save(str(path))
    doc.close()


def _make_sentence_fragment_caption_false_positive_pdf(path: Path) -> None:
    doc = pymupdf.open()
    page = doc.new_page()
    page.insert_text((72, 72), "Attack Modifiers")
    page.insert_text((72, 110), "table to see how they are uniquely impacted.")
    page.insert_text((72, 140), "If fighting from a position of weakness, the attack is impaired.")
    page.insert_textbox(pymupdf.Rect(72, 220, 540, 520), _PAGE_PROSE)
    doc.save(str(path))
    doc.close()


class FakeDocumentExtractor:
    def __init__(self, heading: str = "Functions", text: str = "Functions are values.") -> None:
        self.heading = heading
        self.text = text

    def __call__(self, pdf_path: Path, source_rel: str, source_hash: str) -> DocumentModel:
        return DocumentModel(
            source_locator=source_rel,
            source_hash=source_hash,
            extractor_name="docling",
            extractor_version="test",
            elements=(
                DocumentElement(
                    element_id="element-000001",
                    element_kind="heading",
                    body_state="body",
                    heading_path=self.heading,
                    page_start=1,
                    page_end=1,
                    text=self.heading,
                    markdown=f"# {self.heading}",
                ),
                DocumentElement(
                    element_id="element-000002",
                    element_kind="paragraph",
                    body_state="body",
                    heading_path=self.heading,
                    page_start=1,
                    page_end=1,
                    text=self.text,
                    markdown=self.text,
                ),
            ),
        )


class ForwardCueDocumentExtractor:
    def __call__(self, pdf_path: Path, source_rel: str, source_hash: str) -> DocumentModel:
        return DocumentModel(
            source_locator=source_rel,
            source_hash=source_hash,
            extractor_name="docling",
            extractor_version="test",
            elements=(
                DocumentElement(
                    element_id="element-000001",
                    element_kind="heading",
                    body_state="body",
                    heading_path="Sample Outcomes",
                    page_start=1,
                    page_end=1,
                    text="Sample Outcomes",
                    markdown="# Sample Outcomes",
                ),
                DocumentElement(
                    element_id="element-000002",
                    element_kind="heading",
                    body_state="body",
                    heading_path="Roll on the table below.",
                    page_start=1,
                    page_end=1,
                    text="Roll on the table below.",
                    markdown="# Roll on the table below.",
                ),
                DocumentElement(
                    element_id="element-000003",
                    element_kind="heading",
                    body_state="body",
                    heading_path="Follow-up Notes",
                    page_start=1,
                    page_end=1,
                    text="Follow-up Notes",
                    markdown="# Follow-up Notes",
                ),
            ),
        )


@dataclass(frozen=True)
class FakeRow:
    cells: tuple[tuple[float, float, float, float], ...]


@dataclass(frozen=True)
class FakeTable:
    bbox: tuple[float, float, float, float]
    rows: tuple[FakeRow, ...]


class FakePage:
    def get_text(self, mode: str, sort: bool = True) -> tuple[tuple[Any, ...], ...]:
        assert mode == "words"
        return (
            (10, 10, 18, 20, "1", 0, 0, 0),
            (25, 10, 62, 20, "Encounter", 0, 0, 1),
            (80, 10, 100, 20, "Roll", 0, 0, 2),
            (103, 10, 113, 20, "on", 0, 0, 3),
            (116, 10, 130, 20, "an", 0, 0, 4),
            (80, 22, 128, 32, "encounter", 0, 1, 0),
            (132, 22, 154, 32, "table.", 0, 1, 1),
        )


class NumberedPrefacePage:
    def get_text(self, mode: str, sort: bool = True) -> tuple[tuple[Any, ...], ...]:
        assert mode == "words"
        return (
            (80, 10, 100, 20, "Roll", 0, 0, 0),
            (103, 10, 113, 20, "on", 0, 0, 1),
            (116, 10, 130, 20, "the", 0, 0, 2),
            (134, 10, 160, 20, "table.", 0, 0, 3),
            (10, 28, 18, 38, "1", 0, 1, 0),
            (25, 28, 62, 38, "Encounter", 0, 1, 1),
            (80, 28, 100, 38, "First", 0, 1, 2),
            (104, 28, 126, 38, "event.", 0, 1, 3),
            (80, 52, 105, 62, "Second", 0, 2, 0),
            (109, 52, 120, 62, "row", 0, 2, 1),
            (10, 64, 18, 74, "2", 0, 3, 0),
            (25, 64, 45, 74, "Sign", 0, 3, 1),
            (80, 64, 120, 74, "continues.", 0, 3, 2),
        )


def test_geometry_table_rows_render_cell_words_with_spaces() -> None:
    rows = geometry_table_rows(
        FakePage(),
        FakeTable(
            bbox=(0, 8, 170, 34),
            rows=(FakeRow(cells=((0, 8, 22, 22), (22, 8, 76, 22), (76, 8, 170, 34))),),
        ),
    )

    assert rows == (("1", "Encounter", "Roll on an encounter table."),)


def test_preface_numbered_table_rebuilds_rows_from_marker_bands() -> None:
    text = preface_numbered_table_text(
        NumberedPrefacePage(),
        FakeTable(
            bbox=(0, 8, 170, 78),
            rows=(
                FakeRow(cells=((0, 8, 22, 24), (22, 8, 76, 24), (76, 8, 170, 24))),
                FakeRow(cells=((0, 24, 22, 42), (22, 24, 76, 42), (76, 24, 170, 42))),
                FakeRow(cells=((0, 42, 22, 60), (22, 42, 76, 60), (76, 42, 170, 60))),
                FakeRow(cells=((0, 60, 22, 78), (22, 60, 76, 78), (76, 60, 170, 78))),
            ),
        ),
        (
            ("", "", "Roll on the table."),
            ("1", "Encounter", "First event."),
            ("", "", "Second row"),
            ("2", "Sign", "continues."),
        ),
    )

    assert text == "Roll on the table.\n1 Encounter First event.\n2 Sign Second row continues."


def test_recovers_forward_cue_numbered_table_with_readable_cells(tmp_path: Path) -> None:
    pdf = tmp_path / "book.pdf"
    _make_forward_cue_table_pdf(pdf)

    result = ensure_extracted(
        pdf,
        "book.pdf",
        tmp_path / "cache",
        NullRecognizer(),
        document_extractor=ForwardCueDocumentExtractor(),
    )

    model = (result.cache_dir / "document_model.json").read_text(encoding="utf-8")
    chunk = "\n\n".join(
        chunk_file(result.cache_dir, chunk_record.chunk_id).read_text(encoding="utf-8")
        for chunk_record in result.manifest.chunks
    )
    assert '"element_kind": "table"' in model
    assert "1 Trial Alpha result keeps separate words." in chunk
    assert "2 Review Beta result keeps spaces." in chunk
    assert "Alpharesult" not in chunk
    assert chunk.index("Roll on the table below.") < chunk.index("1 Trial")
    assert chunk.index("2 Review") < chunk.index("Follow-up Notes")


def test_forward_cue_without_numbered_rows_does_not_create_table(tmp_path: Path) -> None:
    pdf = tmp_path / "book.pdf"
    _make_forward_cue_without_table_pdf(pdf)

    result = ensure_extracted(
        pdf,
        "book.pdf",
        tmp_path / "cache",
        NullRecognizer(),
        document_extractor=ForwardCueDocumentExtractor(),
    )

    model = (result.cache_dir / "document_model.json").read_text(encoding="utf-8")
    assert '"element_kind": "table"' not in model


def test_sentence_fragment_starting_with_table_is_not_caption(tmp_path: Path) -> None:
    pdf = tmp_path / "book.pdf"
    _make_sentence_fragment_caption_false_positive_pdf(pdf)

    result = ensure_extracted(
        pdf,
        "book.pdf",
        tmp_path / "cache",
        NullRecognizer(),
        document_extractor=FakeDocumentExtractor(
            heading="Attack Modifiers",
            text="Attack modifiers use ordinary prose.",
        ),
    )

    model = (result.cache_dir / "document_model.json").read_text(encoding="utf-8")
    assert '"element_kind": "table"' not in model
