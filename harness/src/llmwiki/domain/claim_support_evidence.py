"""Evidence lookup service for claim-support audits."""

from __future__ import annotations

import re
from collections.abc import Sequence

from llmwiki.domain.citations import Citation
from llmwiki.domain.evidence_registry import EvidenceRecord, EvidenceRegistry, SourceRange

_TERM_RE = re.compile(r"[a-z][a-z0-9-]{2,}")


class ClaimSupportEvidenceIndex:
    def __init__(self, registries: Sequence[EvidenceRegistry]) -> None:
        self.registries = registries
        self.records = _records_by_id(registries)
        self.records_by_claim = _records_by_claim(registries)
        self.ranges = _ranges_by_id(registries)
        self.registries_by_source = {
            registry.source_texts[0].source_path: registry
            for registry in registries
            if registry.source_texts
        }

    def registry_for_source(self, source_path: str) -> EvidenceRegistry | None:
        return self.registries_by_source.get(source_path)

    def evidence_ids_for_claims(self, claim_ids: Sequence[str]) -> tuple[str, ...]:
        ids: list[str] = []
        for claim_id in claim_ids:
            ids.extend(record.evidence_id for record in self.records_by_claim.get(claim_id, ()))
        return tuple(dict.fromkeys(ids))

    def evidence_ids_for_citations(
        self, page_id: str, citations: Sequence[Citation]
    ) -> tuple[str, ...]:
        ids: list[str] = []
        for citation in citations:
            registry = self.registry_for_source(citation.source_path)
            if registry is None:
                continue
            for source_range in registry.ranges_for_page(page_id, citation.source_path):
                if source_range.contains(citation):
                    ids.extend(
                        record.evidence_id
                        for record in registry.evidence_records
                        if record.source_range_id == source_range.source_range_id
                    )
        return tuple(dict.fromkeys(ids))

    def page_id_for_evidence(self, evidence_ids: Sequence[str]) -> str:
        for evidence_id in evidence_ids:
            record = self.records.get(evidence_id)
            if record is None:
                continue
            source_range = self.ranges.get(record.source_range_id)
            if source_range is not None:
                return source_range.page_id
        return ""

    def excerpts(self, evidence_ids: Sequence[str], limit: int = 3) -> tuple[str, ...]:
        excerpts: list[str] = []
        for evidence_id in evidence_ids[:limit]:
            record = self.records.get(evidence_id)
            if record is not None:
                excerpts.append(f"{evidence_id}: {record.excerpt}")
        return tuple(excerpts)

    def excerpts_for_claim(
        self, evidence_ids: Sequence[str], claim_text: str, limit: int = 3
    ) -> tuple[str, ...]:
        query_terms = _terms(claim_text)
        ranked: list[tuple[int, int, int, str, str]] = []
        for position, evidence_id in enumerate(dict.fromkeys(evidence_ids)):
            record = self.records.get(evidence_id)
            if record is None:
                continue
            overlap = len(query_terms & _terms(record.excerpt)) if query_terms else 0
            source_claim_bonus = 1 if record.source_claim_id else 0
            ranked.append((overlap, source_claim_bonus, -position, evidence_id, record.excerpt))
        ranked.sort(reverse=True)
        return tuple(
            f"{evidence_id}: {excerpt}"
            for _, _, _, evidence_id, excerpt in ranked[:limit]
        )


def _records_by_id(registries: Sequence[EvidenceRegistry]) -> dict[str, EvidenceRecord]:
    return {
        record.evidence_id: record
        for registry in registries
        for record in registry.evidence_records
    }


def _records_by_claim(
    registries: Sequence[EvidenceRegistry],
) -> dict[str, tuple[EvidenceRecord, ...]]:
    result: dict[str, list[EvidenceRecord]] = {}
    for registry in registries:
        for record in registry.evidence_records:
            if record.source_claim_id:
                result.setdefault(record.source_claim_id, []).append(record)
    return {claim_id: tuple(records) for claim_id, records in result.items()}


def _ranges_by_id(registries: Sequence[EvidenceRegistry]) -> dict[str, SourceRange]:
    return {
        source_range.source_range_id: source_range
        for registry in registries
        for source_range in registry.source_ranges
    }


def _terms(text: str) -> frozenset[str]:
    return frozenset(_TERM_RE.findall(text.lower()))
