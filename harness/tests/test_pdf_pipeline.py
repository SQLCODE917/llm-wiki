"""Extraction pipeline tests against a synthetic PDF (built with pymupdf).

Covers the design's standing integration contract: decorative images flow
through with empty OCR, silently — full extraction, zero figure text,
zero errors.
"""

from pathlib import Path

import pymupdf  # type: ignore[import-untyped]
import pytest

from llmwiki.pdf import ScannedPdfError
from llmwiki.pdf.pipeline import chunk_file, ensure_extracted, save_manifest
from llmwiki.pdf.recognizer import NullRecognizer, TextSpan

_PAGE_PROSE = "Functions are first-class values. " * 40  # ~1.4K chars/page: classifies TEXT


class CountingRecognizer:
    """Engine double: decorative everywhere, counts invocations."""

    def __init__(self, spans: list[TextSpan] | None = None) -> None:
        self.calls = 0
        self._spans = spans or []

    def recognize(self, image_path: Path) -> list[TextSpan]:
        self.calls += 1
        return self._spans


def _make_pdf(path: Path, n_pages: int = 6, with_image: bool = True) -> None:
    doc = pymupdf.open()
    for i in range(n_pages):
        page = doc.new_page()
        page.insert_text((72, 72), f"Chapter text page {i + 1}.")
        page.insert_textbox(pymupdf.Rect(72, 100, 540, 400), _PAGE_PROSE)
    if with_image:
        # A textured "photo" placed clear of the text — the layout engine
        # silently drops featureless rectangles and overlapped images.
        width, height = 240, 180
        pixmap = pymupdf.Pixmap(pymupdf.csRGB, pymupdf.IRect(0, 0, width, height), False)
        for y in range(0, height, 4):
            for x in range(0, width, 4):
                pixmap.set_pixel(x, y, (x % 256, y % 256, (x * y) % 256))
        doc[0].insert_image(pymupdf.Rect(150, 450, 390, 630), pixmap=pixmap)
    toc = [[1, "One", 1], [1, "Two", 3], [1, "Three", 5]]
    doc.set_toc(toc)
    doc.save(str(path))
    doc.close()


def _make_scanned_pdf(path: Path, n_pages: int = 4) -> None:
    doc = pymupdf.open()
    for _ in range(n_pages):
        doc.new_page()  # no text layer at all
    doc.save(str(path))
    doc.close()


class TestEnsureExtracted:
    def test_extracts_chunks_and_manifest(self, tmp_path: Path) -> None:
        pdf = tmp_path / "book.pdf"
        _make_pdf(pdf)
        result = ensure_extracted(pdf, "book.pdf", tmp_path / "cache", NullRecognizer())

        manifest = result.manifest
        assert manifest.source == "book.pdf"
        assert len(manifest.chunks) >= 1
        assert manifest.pending == manifest.chunks
        first = manifest.chunks[0]
        text = chunk_file(result.cache_dir, first.chunk_id).read_text(encoding="utf-8")
        assert "Chapter text page 1" in text
        assert (first.start_page, manifest.chunks[-1].end_page) == (1, 6)

    def test_decorative_images_extract_silently_with_empty_ocr(self, tmp_path: Path) -> None:
        # The standing integration test from the design: empty OCR is normal.
        pdf = tmp_path / "book.pdf"
        _make_pdf(pdf, with_image=True)
        recognizer = CountingRecognizer()
        result = ensure_extracted(pdf, "book.pdf", tmp_path / "cache", recognizer)

        images = list((result.cache_dir / "images").iterdir())
        assert images, "the decorative image must be extracted to disk"
        assert recognizer.calls == len(images)
        all_chunks = "".join(
            chunk_file(result.cache_dir, c.chunk_id).read_text(encoding="utf-8")
            for c in result.manifest.chunks
        )
        assert "OCR" not in all_chunks  # no folded figure text, no markers

    def test_figure_text_is_folded_under_ref(self, tmp_path: Path) -> None:
        pdf = tmp_path / "book.pdf"
        _make_pdf(pdf, with_image=True)
        recognizer = CountingRecognizer([TextSpan("Figure 1: function composition", 0.95)])
        result = ensure_extracted(pdf, "book.pdf", tmp_path / "cache", recognizer)
        all_chunks = "".join(
            chunk_file(result.cache_dir, c.chunk_id).read_text(encoding="utf-8")
            for c in result.manifest.chunks
        )
        assert "[figure text (OCR, unverified): Figure 1: function composition]" in all_chunks

    def test_cache_hit_skips_reextraction_and_ocr(self, tmp_path: Path) -> None:
        pdf = tmp_path / "book.pdf"
        _make_pdf(pdf)
        recognizer = CountingRecognizer()
        first = ensure_extracted(pdf, "book.pdf", tmp_path / "cache", recognizer)
        marked = first.manifest.mark_done(1, "notes")
        save_manifest(type(first)(manifest=marked, cache_dir=first.cache_dir))

        again = ensure_extracted(pdf, "book.pdf", tmp_path / "cache", recognizer)
        assert again.manifest.chunks[0].status == "done"  # resume state survived
        assert recognizer.calls == len(list((first.cache_dir / "images").iterdir()))

    def test_reextract_rebuilds_pending_manifest(self, tmp_path: Path) -> None:
        pdf = tmp_path / "book.pdf"
        _make_pdf(pdf)
        first = ensure_extracted(pdf, "book.pdf", tmp_path / "cache", NullRecognizer())
        save_manifest(
            type(first)(manifest=first.manifest.mark_done(1, "n"), cache_dir=first.cache_dir)
        )
        redone = ensure_extracted(
            pdf, "book.pdf", tmp_path / "cache", NullRecognizer(), reextract=True
        )
        assert redone.manifest.pending == redone.manifest.chunks

    def test_scanned_pdf_is_refused_cleanly(self, tmp_path: Path) -> None:
        pdf = tmp_path / "scan.pdf"
        _make_scanned_pdf(pdf)
        with pytest.raises(ScannedPdfError, match="scanned"):
            ensure_extracted(pdf, "scan.pdf", tmp_path / "cache", NullRecognizer())
