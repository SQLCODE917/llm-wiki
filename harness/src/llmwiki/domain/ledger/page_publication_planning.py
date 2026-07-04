"""Pure publication-planning operations."""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import replace

from llmwiki.domain.ledger.canonical import artifact_fingerprint, deterministic_id
from llmwiki.domain.ledger.page_publication import (
    FAMILY_PRIORITY,
    FAMILY_RECORD_TYPES,
    PAGE_FAMILY_SECTION_REFERENCE,
    PageCandidate,
    PagePublicationPlan,
    PublicationBudget,
    PublicationWalkabilityReport,
    RejectedPageCandidate,
    conservative_publication_budget,
)
from llmwiki.domain.typed_evidence import EvidenceRecordSet, TypedEvidenceRecord

_STOP_WORDS = {
    "and",
    "for",
    "from",
    "into",
    "page",
    "procedure",
    "recipe",
    "section",
    "source",
    "the",
    "this",
    "with",
}
_WORD = re.compile(r"[a-z0-9]+")


def attach_typed_evidence_support(
    candidates: tuple[PageCandidate, ...], record_set: EvidenceRecordSet | None
) -> tuple[PageCandidate, ...]:
    if record_set is None:
        return candidates
    accepted = record_set.accepted_records
    return tuple(_with_support(candidate, accepted) for candidate in candidates)


def plan_publication(
    *,
    source_id: str,
    source_hash: str,
    source_profile_kind: str,
    budget: PublicationBudget,
    candidates: tuple[PageCandidate, ...],
) -> PagePublicationPlan:
    immediate_rejections: list[RejectedPageCandidate] = []
    eligible: list[PageCandidate] = []
    explicit_sections = set(budget.explicit_section_page_ids)
    minimums = budget.support_minimums
    for candidate in candidates:
        rejection = _immediate_rejection(candidate, minimums, explicit_sections)
        if rejection is None:
            eligible.append(candidate)
        else:
            immediate_rejections.append(rejection)

    accepted: list[PageCandidate] = []
    budget_rejections: list[RejectedPageCandidate] = []
    family_counts: Counter[str] = Counter()
    caps = budget.family_caps
    for candidate in sorted(eligible, key=_candidate_rank):
        family_cap = caps.get(candidate.page_family, 0)
        family_full = family_counts[candidate.page_family] >= family_cap
        if len(accepted) >= budget.max_public_pages or family_full:
            budget_rejections.append(
                _rejected(
                    candidate,
                    "publication-budget-exceeded",
                    "candidate exceeded the source-profile publication budget",
                )
            )
            continue
        accepted.append(candidate)
        family_counts[candidate.page_family] += 1

    rejected = tuple(
        sorted(
            (*immediate_rejections, *budget_rejections),
            key=lambda item: (item.page_family, item.page_id, item.rejection_code),
        )
    )
    draft = PagePublicationPlan(
        page_publication_plan_id=deterministic_id("page-publication-plan", source_hash, source_id),
        page_publication_plan_fingerprint="",
        source_id=source_id,
        source_hash=source_hash,
        source_profile_kind=source_profile_kind,
        publication_budget_id=budget.publication_budget_id,
        accepted_candidates=tuple(accepted),
        rejected_candidates=rejected,
        public_counts=tuple(sorted(family_counts.items())),
    )
    fingerprint = artifact_fingerprint(draft, exclude=("page_publication_plan_fingerprint",))
    return replace(draft, page_publication_plan_fingerprint=fingerprint)


def empty_publication_plan(
    *, source_id: str, source_hash: str, source_profile_kind: str
) -> PagePublicationPlan:
    budget = conservative_publication_budget(source_profile_kind)
    return plan_publication(
        source_id=source_id,
        source_hash=source_hash,
        source_profile_kind=budget.source_profile_kind,
        budget=budget,
        candidates=(),
    )


def publication_walkability_report(plan: PagePublicationPlan) -> PublicationWalkabilityReport:
    rejected_families = Counter(item.page_family for item in plan.rejected_candidates)
    families = Counter(dict(plan.public_counts))
    for family in rejected_families:
        families.setdefault(family, 0)
    return PublicationWalkabilityReport(
        source_id=plan.source_id,
        source_profile_kind=plan.source_profile_kind,
        accepted_count=len(plan.accepted_candidates),
        rejected_count=len(plan.rejected_candidates),
        family_counts=tuple(sorted(families.items())),
        budget_rejection_count=sum(
            1
            for candidate in plan.rejected_candidates
            if candidate.rejection_code == "publication-budget-exceeded"
        ),
    )


def render_publication_walkability_report(report: PublicationWalkabilityReport) -> str:
    lines = [
        "# Publication Walkability Report",
        "",
        f"- Source: `{report.source_id}`",
        f"- Source profile: `{report.source_profile_kind}`",
        f"- Accepted candidates: {report.accepted_count}",
        f"- Rejected candidates: {report.rejected_count}",
        f"- Budget rejections: {report.budget_rejection_count}",
        "",
        "## Family Counts",
        "",
    ]
    for family, count in report.family_counts:
        lines.append(f"- {family}: {count} accepted")
    return "\n".join(lines).strip() + "\n"


def _with_support(
    candidate: PageCandidate, accepted_records: tuple[TypedEvidenceRecord, ...]
) -> PageCandidate:
    candidate_terms = _terms(f"{candidate.title} {candidate.page_id.replace('-', ' ')}")
    compatible = FAMILY_RECORD_TYPES.get(candidate.page_family, set())
    support_ids: list[str] = []
    for record in accepted_records:
        if record.evidence_record_type not in compatible:
            continue
        if candidate_terms.intersection(_record_terms(record)):
            support_ids.append(record.typed_evidence_record_id)
    return replace(candidate, supporting_evidence_record_ids=tuple(dict.fromkeys(support_ids)))


def _record_terms(record: TypedEvidenceRecord) -> set[str]:
    return _terms(f"{record.canonical_text} {record.support_text}")


def _terms(text: str) -> set[str]:
    return {
        term
        for term in _WORD.findall(text.casefold())
        if len(term) >= 2 and term not in _STOP_WORDS
    }


def _immediate_rejection(
    candidate: PageCandidate, minimums: dict[str, int], explicit_sections: set[str]
) -> RejectedPageCandidate | None:
    if candidate.title_findings:
        codes = ", ".join(finding.finding_code for finding in candidate.title_findings)
        return _rejected(candidate, "title-lint-failed", f"title lint failed: {codes}")
    if (
        candidate.page_family == PAGE_FAMILY_SECTION_REFERENCE
        and candidate.page_id not in explicit_sections
    ):
        return _rejected(
            candidate,
            "section-reference-not-explicitly-accepted",
            "section-reference pages require explicit publication-plan acceptance",
        )
    minimum = minimums.get(candidate.page_family, 1)
    if len(candidate.supporting_evidence_record_ids) < minimum:
        support_count = len(candidate.supporting_evidence_record_ids)
        return _rejected(
            candidate,
            "insufficient-typed-evidence",
            f"candidate has {support_count} typed evidence support(s); {minimum} required",
        )
    return None


def _candidate_rank(candidate: PageCandidate) -> tuple[int, float, int, int, str]:
    return (
        FAMILY_PRIORITY.get(candidate.page_family, 50),
        -candidate.rank_score,
        -len(candidate.supporting_evidence_record_ids),
        candidate.source_order,
        candidate.page_id,
    )


def _rejected(candidate: PageCandidate, code: str, message: str) -> RejectedPageCandidate:
    return RejectedPageCandidate(
        candidate_id=candidate.page_candidate_id,
        source_id=candidate.source_id,
        page_id=candidate.page_id,
        title=candidate.title,
        page_family=candidate.page_family,
        rejection_code=code,
        supporting_evidence_record_ids=candidate.supporting_evidence_record_ids,
        message=message,
    )
