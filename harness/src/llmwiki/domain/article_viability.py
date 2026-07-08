"""Article-viability selection for compiler page candidates."""

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass, replace

from llmwiki.domain.ledger.page_publication import (
    PAGE_FAMILY_BROAD_TOPIC,
    PAGE_FAMILY_COLLECTION_PAGE,
    PAGE_FAMILY_PROCEDURE_GUIDE,
    PAGE_FAMILY_RECIPE_PATTERN,
    PAGE_FAMILY_SECTION_REFERENCE,
    PAGE_FAMILY_TOPIC_CONCEPT,
    PageCandidate,
)
from llmwiki.domain.typed_evidence import EvidenceRecordSet, TypedEvidenceRecord

_WORD = re.compile(r"[a-z0-9]+")
_NON_READER_TITLES = {
    "copyright notice",
    "document",
    "about the sample pdf",
    "cover",
    "contents",
    "index",
    "summary",
    "table of contents",
}
_CONNECTIVE_TITLES = {"and also", "or even"}
_LOW_VALUE_TITLE_PARTS = ("copyright", "license", "all rights reserved")
_RISKY_TITLE_PARTS = ("caveat", "history lesson", "preface")
_TRAILING_NUMBER_RE = re.compile(r"\b\d+\s*$")
_FAMILY_PREFERENCE = {
    PAGE_FAMILY_RECIPE_PATTERN: 0,
    PAGE_FAMILY_PROCEDURE_GUIDE: 1,
    PAGE_FAMILY_TOPIC_CONCEPT: 2,
    PAGE_FAMILY_BROAD_TOPIC: 3,
    PAGE_FAMILY_COLLECTION_PAGE: 4,
    PAGE_FAMILY_SECTION_REFERENCE: 9,
}
_FAMILY_BASE = {
    PAGE_FAMILY_RECIPE_PATTERN: 70.0,
    PAGE_FAMILY_PROCEDURE_GUIDE: 64.0,
    PAGE_FAMILY_TOPIC_CONCEPT: 55.0,
    PAGE_FAMILY_BROAD_TOPIC: 35.0,
    PAGE_FAMILY_COLLECTION_PAGE: 18.0,
    PAGE_FAMILY_SECTION_REFERENCE: 0.0,
}
_TARGET_SUPPORT = 8


@dataclass(frozen=True)
class ArticleViabilityFinding:
    severity: str
    finding_code: str
    page_id: str
    title: str
    page_family: str
    message: str


@dataclass(frozen=True)
class ArticleViabilityReport:
    source_id: str
    source_hash: str
    accepted_candidate_ids: tuple[str, ...]
    rejected_candidate_ids: tuple[str, ...]
    findings: tuple[ArticleViabilityFinding, ...]


@dataclass(frozen=True)
class ArticleViabilityResult:
    candidates: tuple[PageCandidate, ...]
    report: ArticleViabilityReport


def select_article_viable_candidates(
    *,
    source_id: str,
    source_hash: str,
    candidates: tuple[PageCandidate, ...],
    record_set: EvidenceRecordSet,
) -> ArticleViabilityResult:
    records = {record.typed_evidence_record_id: record for record in record_set.accepted_records}
    rejected: list[ArticleViabilityFinding] = []
    scored: list[PageCandidate] = []
    for candidate in candidates:
        finding = _candidate_rejection(candidate)
        if finding is not None:
            rejected.append(finding)
            continue
        scored.append(_with_viability_score(candidate, records))
    selected, duplicate_findings = _suppress_duplicate_titles(scored)
    rejected.extend(duplicate_findings)
    report = ArticleViabilityReport(
        source_id=source_id,
        source_hash=source_hash,
        accepted_candidate_ids=tuple(candidate.page_candidate_id for candidate in selected),
        rejected_candidate_ids=tuple(finding.page_id for finding in rejected),
        findings=tuple(rejected),
    )
    return ArticleViabilityResult(tuple(selected), report)


def _candidate_rejection(candidate: PageCandidate) -> ArticleViabilityFinding | None:
    title_key = _normalized_title(candidate.title)
    source_key = _normalized_title(candidate.source_id)
    source_stub = candidate.page_family == PAGE_FAMILY_BROAD_TOPIC and source_key in {
        title_key,
        title_key.removesuffix("overview").strip(),
    }
    source_rulebook_stub = (
        candidate.page_family == PAGE_FAMILY_TOPIC_CONCEPT
        and title_key.endswith("rulebook")
        and source_key == title_key.removesuffix("rulebook").strip()
    )
    if title_key in _NON_READER_TITLES or source_stub or source_rulebook_stub:
        return _finding(
            candidate,
            "non-reader-article-candidate",
            "candidate title is source furniture or not a reader-useful article",
        )
    if title_key in _CONNECTIVE_TITLES or (
        candidate.title.strip().endswith(":") and ">" not in candidate.title
    ):
        return _finding(
            candidate,
            "weak-reader-title",
            "candidate title is a standalone connective heading, not a reader-useful article",
        )
    if any(part in title_key for part in _LOW_VALUE_TITLE_PARTS):
        return _finding(
            candidate,
            "low-value-article-candidate",
            "candidate is legal/source metadata rather than reader-facing content",
        )
    return None


def _with_viability_score(
    candidate: PageCandidate, records_by_id: dict[str, TypedEvidenceRecord]
) -> PageCandidate:
    records = tuple(
        record
        for record_id in candidate.supporting_evidence_record_ids
        if (record := records_by_id.get(record_id)) is not None
    )
    support_count = len(records)
    record_types = {record.evidence_record_type for record in records}
    balance = min(len(record_types) * 5.0, 20.0)
    support_fit = max(0.0, 22.0 - abs(support_count - _TARGET_SUPPORT) * 1.5)
    closure = _closure_bonus(candidate.page_family, record_types)
    title_bonus = _title_bonus(candidate.title)
    oversize_penalty = max(0.0, support_count - 16) * 1.25
    risk_penalty = _article_risk_penalty(candidate.title, records)
    score = (
        _FAMILY_BASE.get(candidate.page_family, 0.0)
        + balance
        + support_fit
        + closure
        + title_bonus
        - oversize_penalty
        - risk_penalty
    )
    return replace(candidate, rank_score=round(score, 4))


def _closure_bonus(page_family: str, record_types: set[str]) -> float:
    if page_family == PAGE_FAMILY_RECIPE_PATTERN:
        return 22.0 if "code_example" in record_types and len(record_types) >= 2 else -30.0
    if page_family == PAGE_FAMILY_PROCEDURE_GUIDE:
        has_steps = "procedure_step" in record_types
        has_closure = bool(record_types & {"rule", "formula", "table_fact"})
        return 18.0 if has_steps and has_closure else -18.0
    if page_family == PAGE_FAMILY_TOPIC_CONCEPT:
        return 12.0 if record_types & {"definition", "rule", "code_example"} else 0.0
    return 0.0


def _title_bonus(title: str) -> float:
    words = _WORD.findall(title.casefold())
    if 1 <= len(words) <= 6:
        return 8.0
    if len(words) <= 10:
        return 3.0
    return -6.0


def _article_risk_penalty(title: str, records: tuple[TypedEvidenceRecord, ...]) -> float:
    title_key = title.casefold()
    penalty = 0.0
    if _TRAILING_NUMBER_RE.search(title_key):
        penalty += 16.0
    if any(part in title_key for part in _RISKY_TITLE_PARTS):
        penalty += 8.0
    penalty += min(30.0, sum(_record_risk_penalty(record) for record in records))
    return penalty


def _record_risk_penalty(record: TypedEvidenceRecord) -> float:
    text = " ".join((record.payload_text, record.canonical_text, record.support_text)).strip()
    if not text:
        return 8.0
    stripped = text.strip()
    penalty = 0.0
    if "..." in stripped or "\\\n" in stripped:
        penalty += 8.0
    if stripped.endswith((':', ';')) or stripped.casefold().endswith(("and;", "and")):
        penalty += 5.0
    if stripped.startswith("-"):
        penalty += 3.0
    if len(_WORD.findall(stripped)) < 4:
        penalty += 6.0
    if record.evidence_record_type == "code_example" and "?" in stripped:
        penalty += 5.0
    return penalty


def _suppress_duplicate_titles(
    candidates: list[PageCandidate],
) -> tuple[list[PageCandidate], tuple[ArticleViabilityFinding, ...]]:
    grouped: dict[str, list[PageCandidate]] = defaultdict(list)
    for candidate in candidates:
        grouped[_normalized_title(candidate.title)].append(candidate)
    selected: list[PageCandidate] = []
    findings: list[ArticleViabilityFinding] = []
    for group in grouped.values():
        winner = min(
            group,
            key=lambda candidate: (
                _FAMILY_PREFERENCE.get(candidate.page_family, 50),
                -candidate.rank_score,
                candidate.source_order,
                candidate.page_id,
            ),
        )
        selected.append(winner)
        for candidate in group:
            if candidate is winner:
                continue
            findings.append(
                _finding(
                    candidate,
                    "duplicate-article-candidate",
                    f"duplicate title suppressed in favor of {winner.page_id}",
                )
            )
    selected = sorted(selected, key=lambda candidate: (candidate.source_order, candidate.page_id))
    return selected, tuple(findings)


def _normalized_title(value: str) -> str:
    return " ".join(_WORD.findall(value.casefold()))


def _finding(candidate: PageCandidate, code: str, message: str) -> ArticleViabilityFinding:
    return ArticleViabilityFinding(
        "blocking",
        code,
        candidate.page_id,
        candidate.title,
        candidate.page_family,
        message,
    )
