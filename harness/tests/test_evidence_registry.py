"""Tests for generated source evidence registry objects."""

from __future__ import annotations

from llmwiki.config import WikiPaths
from llmwiki.domain.citations import SourceInventory
from llmwiki.domain.evidence import EvidencePolicy
from llmwiki.domain.evidence_registry import (
    EvidenceRegistry,
    SourceRange,
    build_evidence_registry,
    source_text_from_text,
)
from llmwiki.domain.evidence_registry_io import registry_from_json, registry_to_json
from llmwiki.domain.objects import RawSource, SourceBundle
from llmwiki.domain.pages import LOCAL_FLAT_STRUCTURE
from llmwiki.domain.planning import build_markdown_page_plan, build_page_plan
from llmwiki.domain.planning_analysis import build_extracted_unit
from llmwiki.store import WikiStore

TODAY = "2026-06-22"


def test_source_evidence_registry_builds_stable_records_for_markdown() -> None:
    raw_source = RawSource.from_locator("antikythera-mechanism.md")
    source_text = "# Device\n\nThe device may predict eclipses."
    plan = build_markdown_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        source_text=source_text,
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
    )
    source = source_text_from_text(raw_source.source_locator, source_text)

    first = build_evidence_registry(plan, (source,))
    second = build_evidence_registry(plan, (source,))

    assert first == second
    assert first.source_texts[0].source_text_kind == "markdown"
    assert first.source_texts[0].line_count == 3
    assert first.source_ranges[0].page_id == "antikythera-mechanism"
    assert first.evidence_records[0].source_claim_id == "source-claim-unit-0001-0001"
    assert first.evidence_banks[0].evidence_ids == (first.evidence_records[0].evidence_id,)
    assert registry_from_json(registry_to_json(first)) == first


def test_pdf_source_text_reads_extraction_cache(paths: WikiPaths) -> None:
    cache_dir = paths.cache_dir / "deadbeef"
    chunks_dir = cache_dir / "chunks"
    chunks_dir.mkdir(parents=True)
    (cache_dir / "manifest.json").write_text(
        '{"source": "book.pdf", "sha256": "abc123"}',
        encoding="utf-8",
    )
    (chunks_dir / "0001.md").write_text("Chunk one.", encoding="utf-8")
    (chunks_dir / "0002.md").write_text("Chunk two.", encoding="utf-8")

    source_text = WikiStore(paths).source_resolver().source_text("book.pdf")

    assert source_text is not None
    assert source_text.source_text_kind == "pdf-cache"
    assert source_text.lines == ("Chunk one.", "", "Chunk two.")


def test_page_plan_cache_is_explicit_source_text_kind() -> None:
    source_text = source_text_from_text("book.pdf", "Recovered cached text.", "page-plan-cache")

    assert source_text.source_text_kind == "page-plan-cache"


def test_locator_match_reports_local_window_and_global_suggestions() -> None:
    registry = EvidenceRegistry(
        registry_id="test-registry",
        source_texts=(
            source_text_from_text(
                "article.md", "Alpha.\nWindow evidence.\nBeta.\nGlobal evidence."
            ),
        ),
        source_ranges=(),
        evidence_records=(),
    )
    inventory = SourceInventory.from_raw_relative_paths(["article.md"])
    policy = EvidencePolicy(mode="warn", registry=registry)

    local = policy.check_page(
        "alpha",
        '"Window evidence." (raw/article.md normalized:L1)',
        inventory,
    )
    assert [finding.code for finding in local.findings] == ["evidence-outside-locator"]
    assert "Suggested locator: normalized:L1-L3" in local.findings[0].message

    global_result = policy.check_page(
        "alpha",
        '"Global evidence." (raw/article.md normalized:L1)',
        inventory,
    )
    assert [finding.code for finding in global_result.findings] == ["evidence-outside-locator"]
    assert "Suggested locator: normalized:L4" in global_result.findings[0].message


def test_source_range_violation_produces_finding() -> None:
    registry = EvidenceRegistry(
        registry_id="test-registry",
        source_texts=(source_text_from_text("book.pdf", "first\nsecond", "pdf-cache"),),
        source_ranges=(
            SourceRange(
                source_range_id="source-range-book-functions",
                page_id="book-functions",
                source_locator="book.pdf",
                page_range=(1, 2),
                line_range=None,
                heading_path="Functions",
            ),
        ),
        evidence_records=(),
    )
    inventory = SourceInventory.from_raw_relative_paths(["book.pdf"])
    result = EvidencePolicy(mode="warn", registry=registry).check_page(
        "book-functions",
        "Functions cite the wrong page. (raw/book.pdf p.9)",
        inventory,
    )

    assert [finding.code for finding in result.findings] == ["source-range-violation"]


def test_lint_uses_registry_argument_for_policy() -> None:
    registry = EvidenceRegistry(
        registry_id="test-registry",
        source_texts=(source_text_from_text("article.md", "Actual evidence."),),
        source_ranges=(),
        evidence_records=(),
    )
    inventory = SourceInventory.from_raw_relative_paths(["article.md"])

    report = EvidencePolicy(mode="warn").lint_pages(
        {"alpha": '"Actual evidence." (raw/article.md normalized:L1)'},
        inventory,
        registry=registry,
    )

    assert report.registry == registry
    assert report.findings == ()
    assert "Evidence registry: 1 source text(s)" in report.render()


def test_page_plan_registry_tracks_pdf_source_ranges() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    units = (
        build_extracted_unit(
            unit_id="unit-0001",
            raw_source=raw_source,
            locator="p.1-2",
            heading_path="Functions",
            text="Functions are values.",
        ),
        build_extracted_unit(
            unit_id="unit-0002",
            raw_source=raw_source,
            locator="p.3-4",
            heading_path="Closures",
            text="Closures capture scope.",
        ),
    )
    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=units,
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
        new_page_prefix="book",
    )
    registry = build_evidence_registry(
        plan,
        (
            source_text_from_text(
                "book.pdf", "Functions are values.\nClosures capture scope.", "pdf-cache"
            ),
        ),
    )

    ranges = {source_range.page_id: source_range for source_range in registry.source_ranges}
    assert ranges["book-functions"].page_range == (1, 2)
    assert ranges["book-closures"].page_range == (3, 4)


def test_locator_match_returns_no_match_for_fabricated_evidence() -> None:
    policy = EvidencePolicy(mode="fail", registry=_single_line_registry("Real evidence."))
    report = policy.check_page(
        "alpha",
        '"Fabricated evidence." (raw/article.md normalized:L1)',
        SourceInventory.from_raw_relative_paths(["article.md"]),
    )

    assert [finding.code for finding in report.findings] == ["evidence-not-found"]
    assert not report.allowed


def test_locator_match_helper_reports_exact_match() -> None:
    registry = _single_line_registry("Real evidence.")
    citation = EvidencePolicy(mode="warn", registry=registry).check_page(
        "alpha",
        '"Real evidence." (raw/article.md normalized:L1)',
        SourceInventory.from_raw_relative_paths(["article.md"]),
    )

    assert citation.findings == ()


def _single_line_registry(text: str) -> EvidenceRegistry:
    return EvidenceRegistry(
        registry_id="test-registry",
        source_texts=(source_text_from_text("article.md", text),),
        source_ranges=(),
        evidence_records=(),
    )
