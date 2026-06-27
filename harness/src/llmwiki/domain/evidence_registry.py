"""Generated source evidence registry for deterministic audits."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from typing import Literal

from llmwiki.domain.citations import Citation
from llmwiki.domain.evidence_locator_index import EvidenceIdentity
from llmwiki.domain.objects import ExtractedUnit, PagePlan

SourceTextKind = Literal["markdown", "pdf-cache", "page-plan-cache"]
EvidenceKind = Literal["source-claim", "citation", "table-cell"]


@dataclass(frozen=True)
class SourceText:
    source_locator: str
    source_hash: str
    source_text_kind: SourceTextKind
    lines: tuple[str, ...]

    @property
    def line_count(self) -> int:
        return len(self.lines)

    @property
    def source_path(self) -> str:
        return _source_path(self.source_locator)


@dataclass(frozen=True)
class SourceRange:
    source_range_id: str
    page_id: str
    source_locator: str
    page_range: tuple[int, int] | None
    line_range: tuple[int, int] | None
    heading_path: str

    @property
    def source_path(self) -> str:
        return _source_path(self.source_locator)

    def contains(self, citation: Citation) -> bool:
        if citation.source_path != self.source_path:
            return False
        if citation.line_range is not None and self.line_range is not None:
            return _contains_range(self.line_range, citation.line_range)
        if citation.page_range is not None and self.page_range is not None:
            return _contains_range(self.page_range, citation.page_range)
        return True


@dataclass(frozen=True)
class EvidenceRecord:
    evidence_id: str
    source_locator: str
    source_hash: str
    source_range_id: str
    line_range: tuple[int, int] | None
    excerpt: str
    excerpt_digest: str
    evidence_kind: EvidenceKind
    evidence_identity_id: str = ""
    source_claim_id: str = ""


@dataclass(frozen=True)
class EvidenceBank:
    source_range_id: str
    evidence_ids: tuple[str, ...]
    snippets: tuple[str, ...]
    token_estimate: int


@dataclass(frozen=True)
class EvidenceRegistry:
    registry_id: str
    source_texts: tuple[SourceText, ...]
    source_ranges: tuple[SourceRange, ...]
    evidence_records: tuple[EvidenceRecord, ...]

    def source_lines(self, source_path: str) -> tuple[str, ...] | None:
        for source_text in self.source_texts:
            if source_text.source_path == source_path:
                return source_text.lines
        return None

    def ranges_for_page(self, page_id: str, source_path: str) -> tuple[SourceRange, ...]:
        return tuple(
            source_range
            for source_range in self.source_ranges
            if source_range.page_id == page_id and source_range.source_path == source_path
        )

    @property
    def evidence_banks(self) -> tuple[EvidenceBank, ...]:
        records_by_range: dict[str, list[EvidenceRecord]] = {}
        for record in self.evidence_records:
            records_by_range.setdefault(record.source_range_id, []).append(record)
        banks: list[EvidenceBank] = []
        for source_range_id, records in sorted(records_by_range.items()):
            snippets = tuple(
                _snippet(record.excerpt) for record in records if record.excerpt.strip()
            )
            banks.append(
                EvidenceBank(
                    source_range_id=source_range_id,
                    evidence_ids=tuple(record.evidence_id for record in records),
                    snippets=snippets,
                    token_estimate=sum(len(snippet.split()) for snippet in snippets),
                )
            )
        return tuple(banks)


def build_evidence_registry(
    plan: PagePlan, source_texts: tuple[SourceText, ...]
) -> EvidenceRegistry:
    source_ranges = _source_ranges(plan, source_texts)
    evidence_records = _evidence_records(plan, source_texts, source_ranges)
    source_key = "|".join(
        f"{source_text.source_locator}:{source_text.source_hash}" for source_text in source_texts
    )
    registry_id = _digest(f"{plan.plan_id}|{source_key}")[:16]
    return EvidenceRegistry(
        registry_id=f"evidence-registry-{registry_id}",
        source_texts=source_texts,
        source_ranges=source_ranges,
        evidence_records=evidence_records,
    )


def source_text_from_text(
    source_locator: str, text: str, source_text_kind: SourceTextKind = "markdown"
) -> SourceText:
    return SourceText(
        source_locator=source_locator,
        source_hash=_digest(text),
        source_text_kind=source_text_kind,
        lines=tuple(text.splitlines()),
    )


def _source_ranges(plan: PagePlan, source_texts: tuple[SourceText, ...]) -> tuple[SourceRange, ...]:
    source_text_by_locator = {
        source_text.source_locator: source_text for source_text in source_texts
    }
    ranges: list[SourceRange] = []
    units_by_id = {unit.unit_id: unit for unit in plan.extracted_units}
    for write in plan.planned_writes:
        units = tuple(
            units_by_id[unit_id] for unit_id in write.extracted_units if unit_id in units_by_id
        )
        if not units:
            continue
        source_locator = units[0].raw_source.source_locator
        source_text = source_text_by_locator.get(source_locator)
        page_range = _combined_page_range(tuple(unit.locator for unit in units))
        line_range = (1, source_text.line_count) if source_text is not None else None
        ranges.append(
            SourceRange(
                source_range_id=f"source-range-{write.page_metadata.page_id}",
                page_id=write.page_metadata.page_id,
                source_locator=source_locator,
                page_range=page_range,
                line_range=line_range,
                heading_path=_heading_path(units),
            )
        )
    return tuple(ranges)


def _evidence_records(
    plan: PagePlan,
    source_texts: tuple[SourceText, ...],
    source_ranges: tuple[SourceRange, ...],
) -> tuple[EvidenceRecord, ...]:
    source_hashes = {
        source_text.source_locator: source_text.source_hash for source_text in source_texts
    }
    range_by_unit = _source_range_by_unit(plan, source_ranges)
    records: list[EvidenceRecord] = []
    for claim in plan.source_claims:
        source_range = range_by_unit.get(claim.extracted_unit_id)
        if source_range is None:
            continue
        source_hash = source_hashes.get(claim.evidence.raw_source.source_locator, "")
        excerpt = claim.statement.strip()
        excerpt_digest = _digest(excerpt)
        locator_text = _identity_locator_text(source_range, source_texts)
        identity = EvidenceIdentity.from_excerpt(
            claim.evidence.raw_source.source_locator,
            source_hash,
            locator_text,
            excerpt,
        )
        records.append(
            EvidenceRecord(
                evidence_id=identity.evidence_id,
                source_locator=claim.evidence.raw_source.source_locator,
                source_hash=source_hash,
                source_range_id=source_range.source_range_id,
                line_range=source_range.line_range,
                excerpt=excerpt,
                excerpt_digest=excerpt_digest,
                evidence_kind="source-claim",
                evidence_identity_id=identity.evidence_identity_id,
                source_claim_id=claim.source_claim_id,
            )
        )
    return tuple(records)


def _source_range_by_unit(
    plan: PagePlan, source_ranges: tuple[SourceRange, ...]
) -> dict[str, SourceRange]:
    ranges_by_page = {source_range.page_id: source_range for source_range in source_ranges}
    result: dict[str, SourceRange] = {}
    for write in plan.planned_writes:
        source_range = ranges_by_page.get(write.page_metadata.page_id)
        if source_range is None:
            continue
        for unit_id in write.extracted_units:
            result.setdefault(unit_id, source_range)
    return result


def _combined_page_range(locators: tuple[str, ...]) -> tuple[int, int] | None:
    ranges = tuple(_page_range(locator) for locator in locators)
    present = tuple(item for item in ranges if item is not None)
    if not present:
        return None
    return min(start for start, _ in present), max(end for _, end in present)


def _page_range(locator: str) -> tuple[int, int] | None:
    match = re.search(r"\bp\.(?P<start>\d+)(?:-(?P<end>\d+))?", locator)
    if match is None:
        return None
    start = int(match.group("start"))
    end = int(match.group("end") or start)
    if end < start:
        return None
    return start, end


def _heading_path(units: tuple[ExtractedUnit, ...]) -> str:
    first = units[0].heading_path
    last = units[-1].heading_path
    return first if first == last else f"{first} through {last}"


def _source_path(source_locator: str) -> str:
    return source_locator if source_locator.startswith("raw/") else f"raw/{source_locator}"


def _contains_range(container: tuple[int, int], item: tuple[int, int]) -> bool:
    return container[0] <= item[0] and item[1] <= container[1]


def _identity_locator_text(source_range: SourceRange, source_texts: tuple[SourceText, ...]) -> str:
    if source_range.page_range is not None:
        start, end = source_range.page_range
        return f"p.{start}" if start == end else f"p.{start}-{end}"
    if source_range.line_range is not None:
        return _normalized_locator(*source_range.line_range)
    for source_text in source_texts:
        if source_text.source_locator == source_range.source_locator and source_text.line_count:
            return _normalized_locator(1, source_text.line_count)
    return "source:unresolved"


def _normalized_locator(start: int, end: int) -> str:
    return f"normalized:L{start}" if start == end else f"normalized:L{start}-L{end}"


def _snippet(text: str, limit: int = 220) -> str:
    normalized = " ".join(text.split())
    return normalized if len(normalized) <= limit else normalized[: limit - 3].rstrip() + "..."


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
