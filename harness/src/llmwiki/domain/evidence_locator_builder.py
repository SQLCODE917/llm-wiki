"""EvidenceLocatorBuilder domain service."""

from __future__ import annotations

import hashlib
from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from llmwiki.domain.citations import Citation
from llmwiki.domain.evidence_locator_index import (
    EvidenceLocator,
    EvidenceLocatorFinding,
    EvidenceLocatorIndex,
    LocatorCategory,
    LocatorKind,
)

if TYPE_CHECKING:
    from llmwiki.domain.evidence_registry import EvidenceRegistry, SourceText


def build_evidence_locator_index(
    registry: EvidenceRegistry, citations: Sequence[Citation] = ()
) -> EvidenceLocatorIndex:
    source_text = registry.source_texts[0]
    locators = [
        locator
        for record in registry.evidence_records
        if (locator := _locator_for_record(registry, record)) is not None
    ]
    locators.extend(
        locator
        for citation in citations
        if (locator := _locator_for_citation(citation, registry.source_texts)) is not None
    )
    base = EvidenceLocatorIndex.from_locators(
        source_text.source_locator, source_text.source_hash, locators
    )
    findings = validate_evidence_locator_index(base, registry.source_texts)
    return EvidenceLocatorIndex.from_locators(
        source_text.source_locator, source_text.source_hash, locators, findings
    )


def validate_evidence_locator_index(
    index: EvidenceLocatorIndex, source_texts: Sequence[SourceText]
) -> tuple[EvidenceLocatorFinding, ...]:
    source_text_by_locator = {source.source_locator: source for source in source_texts}
    findings: list[EvidenceLocatorFinding] = []
    for locator in index.locators:
        source_text = source_text_by_locator.get(locator.source_locator)
        if source_text is None:
            findings.append(_finding(locator, "missing-source-text", "SourceText is missing."))
            continue
        if locator.range_start < 1 or locator.range_end < locator.range_start:
            findings.append(_finding(locator, "invalid-range", "Locator range is invalid."))
        elif (
            locator.locator_kind == "normalized-line" and locator.range_end > source_text.line_count
        ):
            findings.append(
                _finding(
                    locator,
                    "invalid-range",
                    f"Locator {locator.locator_text} exceeds {source_text.line_count} lines.",
                )
            )
    return tuple(findings)


def _locator_for_record(registry: EvidenceRegistry, record: Any) -> EvidenceLocator | None:
    ranges = {source_range.source_range_id: source_range for source_range in registry.source_ranges}
    source_texts = {
        source_text.source_locator: source_text for source_text in registry.source_texts
    }
    source_range = ranges.get(record.source_range_id)
    source_text = source_texts.get(record.source_locator)
    line_range = None if source_range is not None and source_range.page_range else record.line_range
    locator = _range_locator(line_range, source_range, source_text)
    if locator is None:
        return None
    locator_text, locator_kind, start, end = locator
    return EvidenceLocator.from_excerpt(
        source_locator=record.source_locator,
        source_hash=record.source_hash,
        locator_text=locator_text,
        locator_kind=locator_kind,
        range_start=start,
        range_end=end,
        excerpt=record.excerpt,
    )


def _locator_for_citation(
    citation: Citation, source_texts: Sequence[SourceText]
) -> EvidenceLocator | None:
    source_locator = citation.source_path.removeprefix("raw/")
    source_text_by_locator = {source.source_locator: source for source in source_texts}
    source_text = source_text_by_locator.get(source_locator)
    if source_text is None or citation.evidence_text is None:
        return None
    if citation.line_range is not None:
        start, end = citation.line_range
        locator_text = _normalized_locator(start, end)
        locator_kind: LocatorKind = "normalized-line"
    elif citation.page_range is not None:
        start, end = citation.page_range
        locator_text = f"p.{start}" if start == end else f"p.{start}-{end}"
        locator_kind = "page-range"
    else:
        return None
    return EvidenceLocator.from_excerpt(
        source_locator=source_locator,
        source_hash=source_text.source_hash,
        locator_text=locator_text,
        locator_kind=locator_kind,
        range_start=start,
        range_end=end,
        excerpt=citation.evidence_text,
    )


def _range_locator(
    line_range: tuple[int, int] | None,
    source_range: Any,
    source_text: Any,
) -> tuple[str, LocatorKind, int, int] | None:
    if line_range is not None:
        start, end = line_range
        return (_normalized_locator(start, end), "normalized-line", start, end)
    if source_range is not None and source_range.page_range is not None:
        start, end = source_range.page_range
        page = f"p.{start}" if start == end else f"p.{start}-{end}"
        return (page, "page-range", start, end)
    if source_range is not None and source_range.line_range is not None:
        start, end = source_range.line_range
        return (_normalized_locator(start, end), "normalized-line", start, end)
    if source_text is not None and source_text.line_count:
        return (
            _normalized_locator(1, source_text.line_count),
            "normalized-line",
            1,
            source_text.line_count,
        )
    return None


def _normalized_locator(start: int, end: int) -> str:
    return f"normalized:L{start}" if start == end else f"normalized:L{start}-L{end}"


def _finding(
    locator: EvidenceLocator, category: LocatorCategory, message: str
) -> EvidenceLocatorFinding:
    seed = f"{locator.locator_id}:{category}:{message}"
    return EvidenceLocatorFinding(
        finding_id=f"evidence-locator-finding-{_digest(seed)[:16]}",
        severity="blocker",
        category=category,
        source_locator=locator.source_locator,
        page_id="",
        locator_id=locator.locator_id,
        message=message,
    )


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
