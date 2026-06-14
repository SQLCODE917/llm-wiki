"""Data-in/data-out tests for the PDF domain: classify, chunking, manifest, OCR fold."""

import pytest

from llmwiki.pdf.chunking import TocEntry, build_sections, pack_chunks
from llmwiki.pdf.classify import PdfKind, classify_pdf
from llmwiki.pdf.intermediate import fold_ocr_into_page, relativize_image_refs
from llmwiki.pdf.manifest import ChunkRecord, Manifest, from_json, to_json
from llmwiki.pdf.recognizer import TextSpan, usable_text


class TestClassify:
    def test_healthy_text_layer_is_text(self) -> None:
        assert classify_pdf([1100, 1200, 0, 950, 1300]) is PdfKind.TEXT

    def test_mostly_empty_pages_is_scanned(self) -> None:
        assert classify_pdf([0, 12, 0, 30, 0]) is PdfKind.SCANNED

    def test_empty_document_is_scanned(self) -> None:
        assert classify_pdf([]) is PdfKind.SCANNED


class TestSections:
    PAGES = [f"page {i} text" for i in range(1, 11)]  # 10 pages

    def test_toc_slices_into_page_spans(self) -> None:
        toc = [TocEntry(1, "Ch 1", 2), TocEntry(1, "Ch 2", 6)]
        sections = build_sections(toc, self.PAGES)
        assert [(s.heading, s.start_page, s.end_page) for s in sections] == [
            ("Front matter", 1, 1),
            ("Ch 1", 2, 5),
            ("Ch 2", 6, 10),
        ]
        assert "page 6 text" in sections[2].text

    def test_no_toc_yields_single_section(self) -> None:
        sections = build_sections([], self.PAGES)
        assert len(sections) == 1
        assert (sections[0].start_page, sections[0].end_page) == (1, 10)

    def test_same_page_entries_keep_page(self) -> None:
        toc = [TocEntry(1, "A", 3), TocEntry(1, "B", 3)]
        sections = build_sections(toc, self.PAGES)
        spans = [(s.heading, s.start_page, s.end_page) for s in sections]
        assert ("A", 3, 3) in spans
        assert ("B", 3, 10) in spans


class TestPackChunks:
    def test_packs_small_sections_together(self) -> None:
        toc = [TocEntry(1, f"S{i}", i + 1) for i in range(5)]
        pages = ["word " * 100] * 6  # ~125 tokens/page
        chunks = pack_chunks(build_sections(toc, pages), budget_tokens=300)
        assert len(chunks) >= 2
        assert all(c.token_estimate <= 300 for c in chunks)
        # Page coverage is continuous from first to last
        assert chunks[0].start_page == 1
        assert chunks[-1].end_page == 6

    def test_oversized_section_split_at_paragraphs(self) -> None:
        big = "\n\n".join(f"paragraph {i} " + "word " * 50 for i in range(10))
        chunks = pack_chunks(build_sections([], [big]), budget_tokens=200)
        assert len(chunks) > 1
        for chunk in chunks:
            assert chunk.token_estimate <= 200 or "\n\n" not in chunk.text
        # No paragraph was split in half
        rejoined = "\n\n".join(c.text for c in chunks)
        for i in range(10):
            assert f"paragraph {i} " in rejoined

    def test_ids_are_one_based_and_ordered(self) -> None:
        chunks = pack_chunks(build_sections([], ["text " * 50]), budget_tokens=100)
        assert [c.chunk_id for c in chunks] == list(range(1, len(chunks) + 1))


class TestManifest:
    def _manifest(self) -> Manifest:
        return Manifest(
            source="book.pdf",
            sha256="ab" * 32,
            chunks=(
                ChunkRecord(1, "Ch 1", 1, 5, 4000),
                ChunkRecord(2, "Ch 2", 6, 9, 3500),
            ),
        )

    def test_roundtrip(self) -> None:
        manifest = self._manifest().mark_done(1, "notes one")
        assert from_json(to_json(manifest)) == manifest

    def test_pending_and_resume_cursor(self) -> None:
        manifest = self._manifest()
        assert [c.chunk_id for c in manifest.pending] == [1, 2]
        manifest = manifest.mark_done(1, "n")
        assert [c.chunk_id for c in manifest.pending] == [2]
        assert not manifest.all_done
        manifest = manifest.mark_done(2, "n2")
        assert manifest.all_done

    def test_mark_done_unknown_chunk_raises(self) -> None:
        with pytest.raises(ValueError):
            self._manifest().mark_done(99, "n")

    def test_notes_are_capped(self) -> None:
        manifest = self._manifest().mark_done(1, "x" * 5000)
        assert len(manifest.chunks[0].notes) <= 1500

    def test_digest_carries_headings_and_pages(self) -> None:
        manifest = self._manifest().mark_done(1, "wrote [[functions]]")
        digest = manifest.digest()
        assert "Ch 1" in digest and "p.1-5" in digest and "[[functions]]" in digest
        assert "Ch 2" not in digest  # pending chunks contribute nothing

    def test_pages_written_roundtrip_and_digest_record(self) -> None:
        manifest = self._manifest().mark_done(1, "notes", pages_written=("functions", "scope"))
        assert from_json(to_json(manifest)) == manifest
        assert "Pages written (recorded): [[functions]], [[scope]]" in manifest.digest()
        assert manifest.write_counts() == {"functions": 1, "scope": 1}

    def test_legacy_manifest_without_pages_written_loads(self) -> None:
        import json

        data = json.loads(to_json(self._manifest()))
        for chunk in data["chunks"]:
            del chunk["pages_written"]  # manifests predating the salience design
        manifest = from_json(json.dumps(data))
        assert manifest.chunks[0].pages_written == ()

    def test_write_counts_accumulate_across_chunks(self) -> None:
        manifest = (
            self._manifest()
            .mark_done(1, "n1", pages_written=("iterable", "generator"))
            .mark_done(2, "n2", pages_written=("iterable",))
        )
        assert manifest.write_counts() == {"iterable": 2, "generator": 1}


class TestOcr:
    def test_usable_text_filters_confidence_and_length(self) -> None:
        spans = [TextSpan("EST. 1998", 0.3), TextSpan("ok", 0.9)]
        assert usable_text(spans) is None  # low conf dropped, rest too short

    def test_usable_text_keeps_real_text(self) -> None:
        spans = [TextSpan("const f = (x) => x * 2;", 0.94)]
        assert usable_text(spans) == "const f = (x) => x * 2;"

    def test_empty_spans_is_none_and_normal(self) -> None:
        assert usable_text([]) is None

    def test_fold_inserts_under_matching_ref_only(self) -> None:
        md = "intro\n\n![](images/book.pdf-0005-01.jpg)\n\n![](images/book.pdf-0007-01.jpg)\n\nend"
        folded = fold_ocr_into_page(md, {"book.pdf-0005-01.jpg": "diagram label"})
        assert "> [figure text (OCR, unverified): diagram label]" in folded
        lines = folded.splitlines()
        ref_idx = lines.index("![](images/book.pdf-0005-01.jpg)")
        assert "diagram label" in lines[ref_idx + 2]
        # Untouched decorative ref and surrounding text preserved
        assert "![](images/book.pdf-0007-01.jpg)" in folded
        assert folded.count("OCR") == 1

    def test_fold_with_no_results_is_identity(self) -> None:
        md = "text\n\n![](images/a.jpg)\n"
        assert fold_ocr_into_page(md, {}) == md

    def test_relativize_image_refs(self) -> None:
        md = "![](/abs/cache/images/a.jpg) and ![x](/abs/cache/images/b.jpg)"
        assert (
            relativize_image_refs(md, "/abs/cache/images")
            == "![](images/a.jpg) and ![x](images/b.jpg)"
        )
