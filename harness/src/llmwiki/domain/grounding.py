"""Deterministic scaffolding for model-assisted grounding audits."""

from __future__ import annotations

import re
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Literal

from llmwiki.domain.citations import Citation, CitationFinding, SourceInventory, inspect_citations
from llmwiki.domain.evidence import EvidencePolicy
from llmwiki.domain.evidence_resolver import SourceTextResolver, resolve_normalized_evidence
from llmwiki.domain.pages import PageError, parse_page
from llmwiki.domain.system_pages import SYSTEM_PAGES

DEFAULT_MAX_CLAIMS = 5
GroundingVerdictLabel = Literal["supported", "too_broad", "not_supported", "unclear"]


@dataclass(frozen=True)
class ClaimCandidate:
    page_name: str
    claim_text: str
    local_context: str
    citation_text: str
    evidence_excerpt: str

    def render(self, index: int) -> str:
        return (
            f"### Claim {index}: [[{self.page_name}]]\n"
            f"Claim: {self.claim_text}\n"
            f"Citation: {self.citation_text}\n"
            f"Local context: {self.local_context}\n"
            f"Evidence excerpt:\n{self.evidence_excerpt}"
        )


@dataclass(frozen=True)
class GroundingSelection:
    candidates: tuple[ClaimCandidate, ...]
    deterministic_findings: tuple[CitationFinding, ...]
    candidate_count: int
    max_claims: int

    @property
    def audited_count(self) -> int:
        return len(self.candidates)

    @property
    def skipped_count(self) -> int:
        return max(0, self.candidate_count - self.audited_count)

    def render_for_prompt(self) -> str:
        if not self.candidates:
            return "No claim candidates were selected for model judgment."
        return "\n\n".join(
            candidate.render(index) for index, candidate in enumerate(self.candidates, 1)
        )


@dataclass(frozen=True)
class GroundingVerdict:
    page_name: str
    claim_text: str
    verdict: GroundingVerdictLabel
    rationale: str
    recommended_action: str

    @property
    def severity(self) -> str:
        return {
            "supported": "info",
            "too_broad": "warn",
            "not_supported": "fail",
            "unclear": "warn",
        }[self.verdict]

    def render(self, index: int) -> str:
        return (
            f"### Verdict {index}: {self.severity.upper()} - {self.verdict} "
            f"on [[{self.page_name}]]\n\n"
            f"- Claim: {self.claim_text}\n"
            f"- Rationale: {self.rationale}\n"
            f"- Recommended action: {self.recommended_action}"
        )


@dataclass(frozen=True)
class GroundingAuditReport:
    selection: GroundingSelection
    verdicts: tuple[GroundingVerdict, ...]
    model_report: str

    def render(self) -> str:
        return "\n\n".join(
            [
                "# Grounding Audit",
                "## Audit Scope\n\n" + self._scope(),
                "## Deterministic Evidence Findings\n\n" + self._deterministic_findings(),
                "## Model Verdicts\n\n" + self._verdicts(),
                "## Model Report\n\n" + (self.model_report.strip() or "No model report."),
                "## Caveat\n\n"
                "This is a bounded grounding audit over selected claims, not proof "
                "that every wiki claim is supported.",
            ]
        )

    def _scope(self) -> str:
        return (
            f"Claim candidates discovered: {self.selection.candidate_count}\n"
            f"Audited claims: {self.selection.audited_count}\n"
            f"Skipped by cap: {self.selection.skipped_count}\n"
            f"Max claims: {self.selection.max_claims}"
        )

    def _deterministic_findings(self) -> str:
        if not self.selection.deterministic_findings:
            return "No fatal deterministic citation evidence findings in selected scope."
        return "\n".join(
            f"- {finding.severity.upper()} {finding.page_name}: {finding.code}: "
            f"{finding.citation_text} -- {finding.message}"
            for finding in self.selection.deterministic_findings
        )

    def _verdicts(self) -> str:
        if not self.verdicts:
            return "No model grounding verdicts were recorded."
        return "\n\n".join(verdict.render(index) for index, verdict in enumerate(self.verdicts, 1))


def select_grounding_claims(
    page_texts: Mapping[str, str],
    inventory: SourceInventory,
    source_resolver: SourceTextResolver,
    *,
    max_claims: int = DEFAULT_MAX_CLAIMS,
) -> GroundingSelection:
    if max_claims < 1:
        raise ValueError("max_claims must be at least 1.")
    policy = EvidencePolicy(mode="warn")
    deterministic: list[CitationFinding] = []
    candidates: list[ClaimCandidate] = []
    discovered = 0
    for page_name in sorted(page_texts):
        if page_name in SYSTEM_PAGES:
            continue
        body = _body(page_name, page_texts[page_name])
        result = policy.check_page(page_name, body, inventory, source_resolver)
        fatal = tuple(finding for finding in result.findings if finding.severity == "fail")
        if fatal:
            deterministic.extend(fatal)
            continue
        report = inspect_citations(page_name, body, inventory)
        for candidate in _claim_candidates(page_name, body, report.citations, source_resolver):
            discovered += 1
            if len(candidates) < max_claims:
                candidates.append(candidate)
    return GroundingSelection(
        candidates=tuple(candidates),
        deterministic_findings=tuple(deterministic),
        candidate_count=discovered,
        max_claims=max_claims,
    )


def _claim_candidates(
    page_name: str, body: str, citations: Sequence[Citation], source_resolver: SourceTextResolver
) -> tuple[ClaimCandidate, ...]:
    selected: list[ClaimCandidate] = []
    for line in body.splitlines():
        if "raw/" not in line or line.lstrip().startswith("#"):
            continue
        matching = [citation for citation in citations if citation.raw_text in line]
        if not matching:
            continue
        citation = matching[0]
        _, finding = resolve_normalized_evidence(citation, source_resolver)
        if finding is not None and finding.severity == "fail":
            continue
        claim_text = _claim_text(line, citation.raw_text)
        if not _is_claim_like(claim_text):
            continue
        selected.append(
            ClaimCandidate(
                page_name=page_name,
                claim_text=claim_text,
                local_context=line.strip(),
                citation_text=citation.raw_text,
                evidence_excerpt=_evidence_excerpt(citation, source_resolver),
            )
        )
    return tuple(selected)


def _body(page_name: str, text: str) -> str:
    try:
        return parse_page(text).page_body
    except PageError:
        return text


def _claim_text(line: str, citation_text: str) -> str:
    claim = line.replace(f"({citation_text})", "").replace(citation_text, "")
    claim = re.sub(r"\s+", " ", claim).strip(" -|")
    return claim


def _is_claim_like(claim_text: str) -> bool:
    text = claim_text.strip()
    if not text:
        return False
    label = text.lower().strip(" :")
    if label in {"citation", "citations", "cite", "source", "sources"}:
        return False
    if label.startswith("cited in"):
        return False
    if label.startswith("see ") and " for " in label:
        return False
    return bool(re.search(r"[A-Za-z]", text))


def _evidence_excerpt(citation: Citation, source_resolver: SourceTextResolver) -> str:
    resolved, _ = resolve_normalized_evidence(citation, source_resolver)
    if resolved is not None:
        return resolved.text
    return "No normalized evidence excerpt is available; judge conservatively from the citation."
