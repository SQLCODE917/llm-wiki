"""Planner-facing page text stays bounded despite generated technical details."""

from llmwiki.domain.objects import ExtractedUnit, RawSource
from llmwiki.domain.page_match_text import PAGE_MATCH_TEXT_CHAR_LIMIT, page_match_text
from llmwiki.domain.planning_analysis import _WIKI_MATCHES_PER_UNIT_LIMIT, wiki_matches


def test_page_match_text_strips_generated_technical_sections() -> None:
    page = (
        "---\npage_id: book-functions\npage_kind: source\nsources: raw/book.pdf\n---\n\n"
        "## Source record\n\nFunctions are values.\n\n"
        "## Related technical details\n\n"
        + "const noisy = true;\n" * 10_000
    )

    bounded = page_match_text(page)

    assert "Functions are values." in bounded
    assert "const noisy" not in bounded
    assert len(bounded) < PAGE_MATCH_TEXT_CHAR_LIMIT


def test_wiki_matches_use_bounded_page_match_text_for_excerpts() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    unit = ExtractedUnit(
        unit_id="unit-0001",
        raw_source=raw_source,
        locator="p.1",
        heading_path="Functions",
        text="Functions are values and can be applied.",
        extraction_status="ok",
    )
    page = (
        "---\npage_id: book-functions\npage_kind: source\nsources: raw/book.pdf\n---\n\n"
        "## Source record\n\nFunctions are values.\n\n"
        "## Technical details\n\n"
        + "technical-noise " * 10_000
    )

    matches = wiki_matches((unit,), {"book-functions": page}, "book.pdf")

    assert matches
    assert "Functions are values." in matches[0].page_excerpt
    assert "technical-noise" not in matches[0].page_excerpt


def test_wiki_matches_cap_source_affine_pages_per_unit() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    unit = ExtractedUnit(
        unit_id="unit-0001",
        raw_source=raw_source,
        locator="p.10",
        heading_path="Target Procedure",
        text="Target procedure compares attack score with evasion score.",
        extraction_status="ok",
    )
    pages = {
        f"book-unrelated-{index:03d}": (
            "---\npage_kind: source\nsources: raw/book.pdf\n---\n\n"
            f"Unrelated source page {index} repeats only generic material."
        )
        for index in range(60)
    }
    pages["book-target-procedure"] = (
        "---\npage_kind: source\nsources: raw/book.pdf\n---\n\n"
        "Target procedure compares attack score with evasion score."
    )

    matches = wiki_matches((unit,), pages, "book.pdf")

    assert len(matches) <= _WIKI_MATCHES_PER_UNIT_LIMIT
    assert matches[0].page_id == "book-target-procedure"
