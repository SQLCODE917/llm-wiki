"""Citation matching rules for source-summary bullets."""

from __future__ import annotations

from llmwiki.domain.citations import Citation, parse_citations

_CITATION_TRANSLATION = str.maketrans(
    {
        "\u00a0": " ",
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
    }
)


def normalized_citation_text(text: str) -> str:
    return " ".join(text.translate(_CITATION_TRANSLATION).split())


def source_summary_bullet_cites_required_locator(
    bullet_text: str, required_citations: tuple[str, ...]
) -> bool:
    normalized_bullet = normalized_citation_text(bullet_text)
    normalized_required = tuple(
        normalized_citation_text(citation) for citation in required_citations
    )
    if any(citation in normalized_bullet for citation in normalized_required):
        return True

    bullet_citations = parse_citations("source-summary-bullet", bullet_text).citations
    required_parsed = tuple(
        citation
        for required in required_citations
        for citation in parse_citations("source-summary-requirement", required).citations
    )
    return any(
        _candidate_satisfies_required(candidate, required)
        for candidate in bullet_citations
        for required in required_parsed
    )


def _candidate_satisfies_required(candidate: Citation, required: Citation) -> bool:
    if candidate.source_path != required.source_path:
        return False
    if required.page_range is not None:
        return candidate.page_range is not None and _contains(
            required.page_range, candidate.page_range
        )
    if required.line_range is not None:
        return candidate.line_range is not None and _contains(
            required.line_range, candidate.line_range
        )
    return True


def _contains(required_range: tuple[int, int], candidate_range: tuple[int, int]) -> bool:
    required_start, required_end = required_range
    candidate_start, candidate_end = candidate_range
    return required_start <= candidate_start <= candidate_end <= required_end
