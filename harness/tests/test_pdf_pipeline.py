"""Extraction pipeline tests against a synthetic PDF."""

# mypy: disable-error-code="no-untyped-call"

import sys
from pathlib import Path

import pymupdf
import pytest

from llmwiki.pdf import ScannedPdfError
from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.manifest import ChunkRecord, Manifest, to_json
from llmwiki.pdf.pipeline import (
    ExtractionResult,
    chunk_file,
    document_extractor_by_name,
    ensure_extracted,
    save_manifest,
)
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


def _make_captioned_table_pdf(path: Path) -> None:
    doc = pymupdf.open()
    page = doc.new_page()
    page.insert_text((72, 72), "Chapter text page 1.")
    page.insert_textbox(pymupdf.Rect(72, 100, 540, 400), _PAGE_PROSE)
    rows = (
        ("Table- Sample Matrix",),
        ("Label", "Score", "Note"),
        ("Alpha", "10", "Stable"),
        ("Beta", "20", "Review"),
        ("Gamma", "30", "Complete"),
    )
    y = 500
    for row in rows:
        if len(row) == 1:
            page.insert_text((72, y), row[0])
        else:
            for x, value in zip((72, 190, 310), row, strict=True):
                page.insert_text((x, y), value)
        y += 18
    page.insert_text((72, y + 20), "Next Section")
    page.insert_text((72, y + 38), "Ordinary prose follows the table.")
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
        )
        assert again.manifest.chunks[0].status == "done"
        assert document_extractor.calls == 1

    def test_cache_hit_rebuilds_nonlexical_unintegrated_chunks_from_document_model(
        self, tmp_path: Path
    ) -> None:
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
        bad_manifest = Manifest(
            source="book.pdf",
            sha256=first.manifest.sha256,
            extractor_name=first.manifest.extractor_name,
            chunks=(ChunkRecord(1, "[", 1, 1, 0),),
            integrated=False,
        )
        save_manifest(ExtractionResult(manifest=bad_manifest, cache_dir=first.cache_dir))
        chunk_file(first.cache_dir, 1).write_text("# [", encoding="utf-8")

        repaired = ensure_extracted(
            pdf,
            "book.pdf",
            tmp_path / "cache",
            NullRecognizer(),
            document_extractor=document_extractor,
        )

        assert document_extractor.calls == 1
        assert [chunk.heading for chunk in repaired.manifest.chunks] == ["Functions"]
        assert "Functions are values" in chunk_file(repaired.cache_dir, 1).read_text(
            encoding="utf-8"
        )

    def test_integrated_cache_hit_skips_nonlexical_rebuild(self, tmp_path: Path) -> None:
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
        bad_manifest = Manifest(
            source="book.pdf",
            sha256=first.manifest.sha256,
            extractor_name=first.manifest.extractor_name,
            chunks=(ChunkRecord(1, "[", 1, 1, 0),),
            integrated=True,
        )
        save_manifest(ExtractionResult(manifest=bad_manifest, cache_dir=first.cache_dir))
        chunk_file(first.cache_dir, 1).write_text("# [", encoding="utf-8")

        reused = ensure_extracted(
            pdf,
            "book.pdf",
            tmp_path / "cache",
            NullRecognizer(),
            document_extractor=document_extractor,
        )

        assert document_extractor.calls == 1
        assert [chunk.heading for chunk in reused.manifest.chunks] == ["["]
        assert chunk_file(reused.cache_dir, 1).read_text(encoding="utf-8") == "# ["

    def test_cache_hit_skips_extractor_module_import(self, tmp_path: Path) -> None:
        pdf = tmp_path / "cached.pdf"
        pdf.write_bytes(b"cached pdf placeholder")
        source_hash = "fcd34992e16d9238e0d4bd0017fc8877ec456828ae79b99ad807bb3ba383abe6"
        cache_dir = tmp_path / "cache" / source_hash[:16]
        cache_dir.mkdir(parents=True)
        manifest = Manifest(
            source="cached.pdf",
            sha256=source_hash,
            chunks=(ChunkRecord(1, "Cached", 1, 1, 10, status="done"),),
            extractor_name="test",
        )
        (cache_dir / "manifest.json").write_text(to_json(manifest), encoding="utf-8")
        (cache_dir / "document_model.json").write_text("{}", encoding="utf-8")
        (cache_dir / "source_sections.json").write_text("[]", encoding="utf-8")
        sys.modules.pop("llmwiki.pdf.extractor", None)
        sys.modules.pop("llmwiki.pdf.pymupdf_document_extractor", None)

        result = ensure_extracted(
            pdf,
            "cached.pdf",
            tmp_path / "cache",
            NullRecognizer(),
            document_extractor_name="pymupdf",
        )

        assert result.manifest.extractor_name == "test"
        assert "llmwiki.pdf.extractor" not in sys.modules
        assert "llmwiki.pdf.pymupdf_document_extractor" not in sys.modules

    def test_manifest_only_cache_reextracts_current_artifacts(self, tmp_path: Path) -> None:
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
        (first.cache_dir / "document_model.json").unlink()
        (first.cache_dir / "source_sections.json").unlink()

        again = ensure_extracted(
            pdf,
            "book.pdf",
            tmp_path / "cache",
            NullRecognizer(),
            document_extractor=document_extractor,
        )

        assert again.cache_dir == first.cache_dir
        assert (again.cache_dir / "document_model.json").is_file()
        assert (again.cache_dir / "source_sections.json").is_file()
        assert document_extractor.calls == 2

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

    def test_recovers_captioned_layout_table_when_primary_extractor_misses_it(
        self, tmp_path: Path
    ) -> None:
        pdf = tmp_path / "book.pdf"
        _make_captioned_table_pdf(pdf)
        document_extractor = FakeDocumentExtractor(
            heading="Measurements",
            text="Table- Sample Matrix\n\n20",
        )

        result = ensure_extracted(
            pdf,
            "book.pdf",
            tmp_path / "cache",
            NullRecognizer(),
            document_extractor=document_extractor,
        )

        model = (result.cache_dir / "document_model.json").read_text(encoding="utf-8")
        chunk = "\n\n".join(
            chunk_file(result.cache_dir, chunk_record.chunk_id).read_text(encoding="utf-8")
            for chunk_record in result.manifest.chunks
        )
        assert '"element_kind": "table"' in model
        assert model.count('"element_kind": "table"') == 1
        assert chunk.count("Table- Sample Matrix") == 1
        assert "Label" in chunk
        assert "Alpha" in chunk
        assert "Gamma" in chunk
        assert "Next Section" not in chunk


class TestDocumentExtractorSelection:
    def test_unknown_extractor_is_rejected(self) -> None:
        with pytest.raises(ValueError, match="Unknown PDF extractor"):
            document_extractor_by_name("unknown")

    def test_pymupdf_extractor_builds_document_model(self, tmp_path: Path) -> None:
        pdf = tmp_path / "book.pdf"
        _make_pdf(pdf)

        model = document_extractor_by_name("pymupdf")(pdf, "book.pdf", "source-hash")

        assert model.extractor_name == "pymupdf4llm"
        assert model.source_locator == "book.pdf"
        assert any(element.element_kind == "heading" for element in model.elements)
        assert any("Chapter text page 1" in element.markdown for element in model.elements)
