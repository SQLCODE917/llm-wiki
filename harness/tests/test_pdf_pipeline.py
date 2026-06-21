"""Extraction pipeline tests against a synthetic PDF."""

from pathlib import Path

import pymupdf  # type: ignore[import-untyped]
import pytest

from llmwiki.pdf import ScannedPdfError
from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.pipeline import chunk_file, ensure_extracted, save_manifest
from llmwiki.pdf.recognizer import NullRecognizer

_PAGE_PROSE = "Functions are first-class values. " * 40


def _make_pdf(path: Path, n_pages: int = 6) -> None:
    doc = pymupdf.open()
    for i in range(n_pages):
        page = doc.new_page()
        page.insert_text((72, 72), f"Chapter text page {i + 1}.")
        page.insert_textbox(pymupdf.Rect(72, 100, 540, 400), _PAGE_PROSE)
    doc.set_toc([[1, "One", 1], [1, "Two", 3], [1, "Three", 5]])
    doc.save(str(path))
    doc.close()


def _make_scanned_pdf(path: Path, n_pages: int = 4) -> None:
    doc = pymupdf.open()
    for _ in range(n_pages):
        doc.new_page()
    doc.save(str(path))
    doc.close()


class FakeDocumentExtractor:
    def __init__(self, heading: str = "Functions", text: str = "Functions are values.") -> None:
        self.calls = 0
        self.heading = heading
        self.text = text

    def __call__(self, pdf_path: Path, source_rel: str, source_hash: str) -> DocumentModel:
        self.calls += 1
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
                    page_end=6,
                    text=self.text,
                    markdown=self.text,
                ),
            ),
        )


class TestEnsureExtracted:
    def test_extracts_chunks_and_manifest(self, tmp_path: Path) -> None:
        pdf = tmp_path / "book.pdf"
        _make_pdf(pdf)
        document_extractor = FakeDocumentExtractor()
        result = ensure_extracted(
            pdf,
            "book.pdf",
            tmp_path / "cache",
            NullRecognizer(),
            document_extractor=document_extractor,
        )

        manifest = result.manifest
        assert manifest.source == "book.pdf"
        assert manifest.extractor_name == "docling"
        assert len(manifest.chunks) == 1
        assert manifest.pending == manifest.chunks
        first = manifest.chunks[0]
        text = chunk_file(result.cache_dir, first.chunk_id).read_text(encoding="utf-8")
        assert "Functions are values" in text
        assert (first.start_page, manifest.chunks[-1].end_page) == (1, 6)
        assert (result.cache_dir / "document_model.json").is_file()
        assert (result.cache_dir / "source_sections.json").is_file()
        assert document_extractor.calls == 1

    def test_cache_hit_skips_reextraction(self, tmp_path: Path) -> None:
        pdf = tmp_path / "book.pdf"
        _make_pdf(pdf)
        document_extractor = FakeDocumentExtractor()
        first = ensure_extracted(
            pdf,
            "book.pdf",
            tmp_path / "cache",
            NullRecognizer(),
            document_extractor=document_extractor,
        )
        marked = first.manifest.mark_done(1, "notes")
        save_manifest(type(first)(manifest=marked, cache_dir=first.cache_dir))

        again = ensure_extracted(
            pdf,
            "book.pdf",
            tmp_path / "cache",
            NullRecognizer(),
            document_extractor=document_extractor,
        )
        assert again.manifest.chunks[0].status == "done"
        assert document_extractor.calls == 1

    def test_reextract_rebuilds_pending_manifest(self, tmp_path: Path) -> None:
        pdf = tmp_path / "book.pdf"
        _make_pdf(pdf)
        document_extractor = FakeDocumentExtractor()
        first = ensure_extracted(
            pdf,
            "book.pdf",
            tmp_path / "cache",
            NullRecognizer(),
            document_extractor=document_extractor,
        )
        save_manifest(
            type(first)(manifest=first.manifest.mark_done(1, "n"), cache_dir=first.cache_dir)
        )
        redone = ensure_extracted(
            pdf,
            "book.pdf",
            tmp_path / "cache",
            NullRecognizer(),
            reextract=True,
            document_extractor=document_extractor,
        )
        assert redone.manifest.pending == redone.manifest.chunks
        assert document_extractor.calls == 2

    def test_scanned_pdf_is_refused_cleanly(self, tmp_path: Path) -> None:
        pdf = tmp_path / "scan.pdf"
        _make_scanned_pdf(pdf)
        with pytest.raises(ScannedPdfError, match="scanned"):
            ensure_extracted(
                pdf,
                "scan.pdf",
                tmp_path / "cache",
                NullRecognizer(),
                document_extractor=FakeDocumentExtractor(),
            )
