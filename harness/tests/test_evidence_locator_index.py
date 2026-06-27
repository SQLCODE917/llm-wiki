"""Tests for stable evidence locator domain objects."""

from __future__ import annotations

from pathlib import Path

from llmwiki.domain.citations import SourceInventory, inspect_citations
from llmwiki.domain.evidence import EvidencePolicy
from llmwiki.domain.evidence_locator_builder import (
    build_evidence_locator_index,
    validate_evidence_locator_index,
)
from llmwiki.domain.evidence_locator_index import (
    EvidenceLocator,
    EvidenceLocatorIndex,
    canonicalize_evidence_text,
)
from llmwiki.domain.evidence_locator_index_io import (
    evidence_locator_index_from_json,
    evidence_locator_index_to_json,
)
from llmwiki.domain.evidence_registry import build_evidence_registry, source_text_from_text
from llmwiki.domain.objects import RawSource, SourceBundle
from llmwiki.domain.pages import LOCAL_FLAT_STRUCTURE
from llmwiki.domain.planning import build_page_plan
from llmwiki.domain.planning_analysis import build_extracted_unit

TODAY = "2026-06-22"


def test_evidence_record_identity_survives_page_id_changes() -> None:
    claim = "The mechanism predicts solar eclipses."
    source = source_text_from_text("article.md", claim)
    first = build_evidence_registry(_plan("alpha", claim), (source,))
    second = build_evidence_registry(_plan("beta", claim), (source,))

    assert first.source_ranges[0].source_range_id != second.source_ranges[0].source_range_id
    assert first.evidence_records[0].evidence_id == second.evidence_records[0].evidence_id
    assert (
        first.evidence_records[0].evidence_identity_id
        == second.evidence_records[0].evidence_identity_id
    )


def test_evidence_record_identity_changes_when_canonical_excerpt_changes() -> None:
    first_claim = "The mechanism predicts solar eclipses."
    second_claim = "The mechanism predicts lunar eclipses."
    source = source_text_from_text("article.md", f"{first_claim}\n{second_claim}")
    first = build_evidence_registry(_plan("alpha", first_claim), (source,))
    second = build_evidence_registry(_plan("alpha", second_claim), (source,))

    assert first.evidence_records[0].evidence_id != second.evidence_records[0].evidence_id


def test_canonicalize_evidence_text_bounds_pathological_excerpts() -> None:
    text = "Page 12 " + ("very-long-word " * 50_000)

    canonical = canonicalize_evidence_text(text)

    assert canonical.startswith("very-long-word")
    assert len(canonical) < len(text)


def test_evidence_locator_index_validates_normalized_line_ranges() -> None:
    source = source_text_from_text("article.md", "one\ntwo\nthree\nfour\nfive")
    valid = EvidenceLocator.from_excerpt(
        source_locator="article.md",
        source_hash=source.source_hash,
        locator_text="normalized:L2-L3",
        locator_kind="normalized-line",
        range_start=2,
        range_end=3,
        excerpt="two three",
    )
    invalid = EvidenceLocator.from_excerpt(
        source_locator="article.md",
        source_hash=source.source_hash,
        locator_text="normalized:L6",
        locator_kind="normalized-line",
        range_start=6,
        range_end=6,
        excerpt="missing",
    )

    assert (
        validate_evidence_locator_index(
            EvidenceLocatorIndex.from_locators("article.md", source.source_hash, (valid,)),
            (source,),
        )
        == ()
    )
    findings = validate_evidence_locator_index(
        EvidenceLocatorIndex.from_locators("article.md", source.source_hash, (invalid,)),
        (source,),
    )
    assert [finding.category for finding in findings] == ["invalid-range"]


def test_evidence_locator_index_validates_page_ranges() -> None:
    source = source_text_from_text("book.pdf", "page text", "pdf-cache")
    invalid = EvidenceLocator.from_excerpt(
        source_locator="book.pdf",
        source_hash=source.source_hash,
        locator_text="p.8-2",
        locator_kind="page-range",
        range_start=8,
        range_end=2,
        excerpt="page text",
    )

    findings = validate_evidence_locator_index(
        EvidenceLocatorIndex.from_locators("book.pdf", source.source_hash, (invalid,)),
        (source,),
    )

    assert [finding.category for finding in findings] == ["invalid-range"]


def test_evidence_locator_index_round_trips_json() -> None:
    claim = "The mechanism predicts solar eclipses."
    source = source_text_from_text("article.md", claim)
    registry = build_evidence_registry(_plan("alpha", claim), (source,))
    index = build_evidence_locator_index(registry)

    assert evidence_locator_index_from_json(evidence_locator_index_to_json(index)) == index


def test_builder_prefers_page_range_for_page_scoped_records() -> None:
    claim = "The mechanism predicts solar eclipses."
    source = source_text_from_text("article.md", claim)
    registry = build_evidence_registry(_plan("alpha", claim), (source,))

    index = build_evidence_locator_index(registry)

    assert {locator.locator_text for locator in index.locators} == {"p.1"}
    assert {locator.locator_kind for locator in index.locators} == {"page-range"}


def test_builder_includes_resolved_citation_locators() -> None:
    source = source_text_from_text("article.md", "Stable evidence.")
    registry = build_evidence_registry(_plan("alpha", "Stable evidence."), (source,))
    report = inspect_citations(
        "alpha",
        '"Stable evidence." (raw/article.md normalized:L1)',
        SourceInventory.from_raw_relative_paths(["article.md"]),
    )

    index = build_evidence_locator_index(registry, report.citations)

    assert any(locator.locator_text == "normalized:L1" for locator in index.locators)


def test_evidence_policy_reports_locator_index_findings() -> None:
    source = source_text_from_text("article.md", "one")
    locator = EvidenceLocator.from_excerpt(
        source_locator="article.md",
        source_hash=source.source_hash,
        locator_text="normalized:L2",
        locator_kind="normalized-line",
        range_start=2,
        range_end=2,
        excerpt="missing",
    )
    index = EvidenceLocatorIndex.from_locators(
        "article.md",
        source.source_hash,
        (locator,),
        validate_evidence_locator_index(
            EvidenceLocatorIndex.from_locators("article.md", source.source_hash, (locator,)),
            (source,),
        ),
    )

    report = EvidencePolicy(mode="fail", locator_index=index).lint_pages(
        {"alpha": '"missing" (raw/article.md normalized:L2)'},
        SourceInventory.from_raw_relative_paths(["article.md"]),
    )

    assert [finding.code for finding in report.findings] == ["locator-out-of-range"]
    assert report.fail_count == 1


def test_domain_vocabulary_records_locator_terms() -> None:
    text = Path("docs/domain-vocabulary.md").read_text(encoding="utf-8")

    for row in (
        "| `EvidenceLocator` | `evidence_locator` |",
        "| `EvidenceIdentity` | `evidence_identity` |",
        "| `EvidenceLocatorIndex` | `evidence_locator_index` |",
        "| `EvidenceLocatorFinding` | `evidence_locator_finding` |",
    ):
        assert row in text


def _plan(prefix: str, unit_text: str):
    raw_source = RawSource.from_locator("article.md")
    unit = build_extracted_unit(
        unit_id="unit-0001",
        raw_source=raw_source,
        locator="p.1",
        heading_path="Alpha",
        text=unit_text,
    )
    return build_page_plan(
        plan_id=f"plan-{prefix}",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=(unit,),
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
        new_page_prefix=prefix,
    )
