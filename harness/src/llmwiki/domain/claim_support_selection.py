"""Candidate selection and deterministic checks for claim-support audits."""

from __future__ import annotations

import hashlib
import re
from collections.abc import Mapping, Sequence

from llmwiki.domain.citations import SourceInventory, inspect_citations
from llmwiki.domain.claim_support import (
    DEFAULT_MAX_CLAIM_SUPPORT_CLAIMS,
    ClaimSupportCandidate,
    ClaimSupportCategory,
    ClaimSupportFinding,
    ClaimSupportSelection,
)
from llmwiki.domain.claim_support_evidence import ClaimSupportEvidenceIndex
from llmwiki.domain.evidence_locator_index import canonicalize_evidence_text
from llmwiki.domain.evidence_locators import (
    locator_match_for_citation,
    source_range_finding,
)
from llmwiki.domain.evidence_registry import EvidenceRegistry
from llmwiki.domain.pages import PageError, parse_page
from llmwiki.domain.source_summary import SourceSummaryDraftArtifact
from llmwiki.domain.system_pages import SYSTEM_PAGES


def select_claim_support_candidates(
    page_texts: Mapping[str, str],
    inventory: SourceInventory,
    registries: Sequence[EvidenceRegistry],
    source_summary_artifacts: Sequence[SourceSummaryDraftArtifact],
    *,
    max_claims: int = DEFAULT_MAX_CLAIM_SUPPORT_CLAIMS,
    source: str = "",
) -> ClaimSupportSelection:
    if max_claims < 1:
        raise ValueError("max_claims must be at least 1.")
    source_path = _source_path_filter(source)
    index = ClaimSupportEvidenceIndex(registries)
    summary_candidates = _source_summary_candidates(
        page_texts, inventory, source_summary_artifacts, index, source_path
    )
    summary_keys = {(candidate.page_id, candidate.claim_text) for candidate in summary_candidates}
    prose_candidates = _prose_candidates(page_texts, inventory, index, source_path, summary_keys)
    discovered = (*summary_candidates, *prose_candidates)
    selected: list[ClaimSupportCandidate] = []
    blocked: list[ClaimSupportCandidate] = []
    findings: list[ClaimSupportFinding] = []
    for candidate in discovered:
        if len(selected) >= max_claims:
            break
        candidate_findings = _deterministic_findings(candidate, inventory, index)
        findings.extend(candidate_findings)
        if candidate_findings:
            blocked.append(candidate)
        else:
            selected.append(candidate)
    return ClaimSupportSelection(
        candidates=tuple(selected),
        blocked_candidates=tuple(blocked),
        deterministic_findings=tuple(findings),
        candidate_count=len(discovered),
        max_claims=max_claims,
    )


def _source_summary_candidates(
    page_texts: Mapping[str, str],
    inventory: SourceInventory,
    artifacts: Sequence[SourceSummaryDraftArtifact],
    index: ClaimSupportEvidenceIndex,
    source_path: str,
) -> tuple[ClaimSupportCandidate, ...]:
    candidates: list[ClaimSupportCandidate] = []
    seen: set[tuple[str, str, tuple[str, ...]]] = set()
    page_counts: dict[str, int] = {}
    for artifact in artifacts:
        if source_path and _source_path(artifact.source_locator) != source_path:
            continue
        for bullet in artifact.draft.claim_bullets:
            evidence_ids = index.evidence_ids_for_claims(bullet.covered_source_claims)
            page_id = index.page_id_for_evidence(evidence_ids) or artifact.page_id_hint
            if page_id not in page_texts:
                continue
            report = inspect_citations(page_id, bullet.bullet_text, inventory)
            if (
                source_path
                and report.citations
                and not any(citation.source_path == source_path for citation in report.citations)
            ):
                continue
            citations = tuple(citation.raw_text for citation in report.citations)
            evidence_ids = tuple(
                dict.fromkeys(
                    (
                        *evidence_ids,
                        *index.evidence_ids_for_citations(page_id, report.citations),
                    )
                )
            )
            claim_text = _claim_text_from_citations(bullet.bullet_text, citations)
            if not _is_claim_like(claim_text):
                continue
            key = (page_id, claim_text, tuple(bullet.covered_source_claims))
            if key in seen:
                continue
            seen.add(key)
            page_counts[page_id] = page_counts.get(page_id, 0) + 1
            candidates.append(
                ClaimSupportCandidate(
                    candidate_id=f"claim-support-summary-{_slug(page_id)}-{page_counts[page_id]}",
                    page_id=page_id,
                    claim_text=claim_text,
                    page_context=bullet.bullet_text,
                    citation_texts=citations,
                    source_claim_ids=tuple(bullet.covered_source_claims),
                    evidence_ids=evidence_ids,
                    evidence_excerpts=index.excerpts_for_claim(
                        evidence_ids, claim_text, limit=5
                    ),
                    candidate_kind="source-summary",
                )
            )
    return tuple(candidates)


def _prose_candidates(
    page_texts: Mapping[str, str],
    inventory: SourceInventory,
    index: ClaimSupportEvidenceIndex,
    source_path: str,
    summary_keys: set[tuple[str, str]],
) -> tuple[ClaimSupportCandidate, ...]:
    candidates: list[ClaimSupportCandidate] = []
    for page_id in sorted(page_texts):
        if page_id in SYSTEM_PAGES:
            continue
        body = _body(page_id, page_texts[page_id])
        for line_number, line in enumerate(body.splitlines(), start=1):
            if "raw/" not in line or line.lstrip().startswith("#"):
                continue
            report = inspect_citations(page_id, line, inventory)
            if not report.citations:
                continue
            if source_path and not any(c.source_path == source_path for c in report.citations):
                continue
            citations = tuple(citation.raw_text for citation in report.citations)
            claim_text = _claim_text_from_citations(line, citations)
            if not _is_claim_like(claim_text) or (page_id, claim_text) in summary_keys:
                continue
            evidence_ids = index.evidence_ids_for_citations(page_id, report.citations)
            candidates.append(
                ClaimSupportCandidate(
                    candidate_id=f"claim-support-prose-{_slug(page_id)}-{line_number}",
                    page_id=page_id,
                    claim_text=claim_text,
                    page_context=line.strip(),
                    citation_texts=citations,
                    source_claim_ids=(),
                    evidence_ids=evidence_ids,
                    evidence_excerpts=index.excerpts_for_claim(
                        evidence_ids, claim_text, limit=5
                    ),
                )
            )
    return tuple(candidates)


def _deterministic_findings(
    candidate: ClaimSupportCandidate,
    inventory: SourceInventory,
    index: ClaimSupportEvidenceIndex,
) -> tuple[ClaimSupportFinding, ...]:
    findings: list[ClaimSupportFinding] = []
    report = inspect_citations(candidate.page_id, candidate.page_context, inventory)
    for citation_finding in report.findings:
        findings.append(
            _finding(
                candidate,
                "missing-evidence",
                f"{citation_finding.code}: {citation_finding.message}",
            )
        )
    if not candidate.evidence_ids:
        findings.append(_finding(candidate, "missing-evidence", "No EvidenceRecord matched."))
    for citation in report.citations:
        registry = index.registry_for_source(citation.source_path)
        if registry is None:
            continue
        range_finding = source_range_finding(citation, registry)
        if range_finding is not None:
            findings.append(_finding(candidate, "source-range", range_finding.message))
        _, locator_finding = locator_match_for_citation(citation, registry)
        if locator_finding is not None:
            findings.append(_finding(candidate, "locator-mismatch", locator_finding.message))
        if citation.evidence_text and citation.line_range is None:
            copied = canonicalize_evidence_text(citation.evidence_text)
            excerpts = " ".join(index.excerpts(candidate.evidence_ids))
            if copied and copied not in canonicalize_evidence_text(excerpts):
                findings.append(
                    _finding(
                        candidate,
                        "copied-evidence",
                        "Copied evidence text mismatches EvidenceRecord excerpts.",
                    )
                )
    return tuple(findings)


def _claim_text_from_citations(line: str, citation_texts: Sequence[str]) -> str:
    claim = line
    for citation_text in citation_texts:
        claim = claim.replace(f"({citation_text})", "").replace(citation_text, "")
    return re.sub(r"\s+", " ", claim).strip(" -|")


def _is_claim_like(claim_text: str) -> bool:
    text = claim_text.strip()
    if not text:
        return False
    label = text.lower().strip(" :")
    return not (
        label in {"citation", "citations", "cite", "source", "sources"}
        or label.startswith("cited in")
        or (label.startswith("see ") and " for " in label)
    )


def _body(page_id: str, text: str) -> str:
    try:
        return parse_page(text).page_body
    except PageError:
        return text


def _source_path_filter(source: str) -> str:
    if not source:
        return ""
    return _source_path(source.removeprefix("raw/"))


def _source_path(source_locator: str) -> str:
    return source_locator if source_locator.startswith("raw/") else f"raw/{source_locator}"


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "claim"


def _finding(
    candidate: ClaimSupportCandidate,
    category: ClaimSupportCategory,
    message: str,
    evidence_id: str = "",
) -> ClaimSupportFinding:
    seed = f"{candidate.candidate_id}:{category}:{message}:{evidence_id}"
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()[:16]
    return ClaimSupportFinding(
        finding_id=f"claim-support-finding-{digest}",
        candidate_id=candidate.candidate_id,
        page_id=candidate.page_id,
        severity="blocker",
        category=category,
        message=message,
        evidence_id=evidence_id,
    )
