"""Report-only claim support audit over generated wiki claims."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

DEFAULT_MAX_CLAIM_SUPPORT_CLAIMS = 5
ClaimSupportVerdictLabel = Literal["supported", "too_broad", "not_supported", "unclear"]
ClaimSupportSeverity = Literal["blocker", "warning", "info"]
ClaimSupportCategory = Literal[
    "missing-evidence",
    "locator-mismatch",
    "source-range",
    "copied-evidence",
    "support-verdict",
]


@dataclass(frozen=True)
class ClaimSupportCandidate:
    candidate_id: str
    page_id: str
    claim_text: str
    page_context: str
    citation_texts: tuple[str, ...]
    source_claim_ids: tuple[str, ...]
    evidence_ids: tuple[str, ...]
    evidence_excerpts: tuple[str, ...] = ()
    candidate_kind: str = "prose-line"

    def render(self, index: int) -> str:
        citations = ", ".join(self.citation_texts) or "None."
        claims = ", ".join(self.source_claim_ids) or "None."
        evidence_ids = ", ".join(self.evidence_ids) or "None."
        excerpts = "\n".join(f"- {excerpt}" for excerpt in self.evidence_excerpts) or "None."
        return (
            f"### Candidate {index}: {self.candidate_id}\n"
            f"Page: [[{self.page_id}]]\n"
            f"Kind: {self.candidate_kind}\n"
            f"Claim: {self.claim_text}\n"
            f"Local context: {self.page_context}\n"
            f"Citations: {citations}\n"
            f"SourceClaim ids: {claims}\n"
            f"Evidence ids: {evidence_ids}\n"
            f"Evidence excerpts:\n{excerpts}"
        )


@dataclass(frozen=True)
class ClaimSupportFinding:
    finding_id: str
    candidate_id: str
    page_id: str
    severity: ClaimSupportSeverity
    category: ClaimSupportCategory
    message: str
    evidence_id: str = ""

    def render(self) -> str:
        evidence = f" evidence_id={self.evidence_id}" if self.evidence_id else ""
        return (
            f"- {self.severity.upper()} {self.page_id} {self.candidate_id}: "
            f"{self.category}: {self.message}{evidence}"
        )


@dataclass(frozen=True)
class ClaimSupportVerdict:
    candidate_id: str
    verdict: ClaimSupportVerdictLabel
    rationale: str
    recommended_action: str

    @property
    def severity(self) -> ClaimSupportSeverity:
        if self.verdict == "supported":
            return "info"
        if self.verdict == "not_supported":
            return "blocker"
        return "warning"

    def render(self, index: int) -> str:
        return (
            f"### Verdict {index}: {self.severity.upper()} - {self.verdict} "
            f"on {self.candidate_id}\n\n"
            f"- Rationale: {self.rationale}\n"
            f"- Recommended action: {self.recommended_action}"
        )


@dataclass(frozen=True)
class ClaimSupportSelection:
    candidates: tuple[ClaimSupportCandidate, ...]
    blocked_candidates: tuple[ClaimSupportCandidate, ...]
    deterministic_findings: tuple[ClaimSupportFinding, ...]
    candidate_count: int
    max_claims: int

    @property
    def audited_count(self) -> int:
        return len(self.candidates) + len(self.blocked_candidates)

    @property
    def selected_count(self) -> int:
        return len(self.candidates)

    @property
    def deterministic_skipped_count(self) -> int:
        return len(self.blocked_candidates)

    @property
    def skipped_count(self) -> int:
        return max(0, self.candidate_count - self.audited_count)

    def render_for_prompt(self) -> str:
        if not self.candidates:
            return "No claim support candidates were selected for model judgment."
        return "\n\n".join(
            candidate.render(index) for index, candidate in enumerate(self.candidates, 1)
        )


@dataclass(frozen=True)
class ClaimSupportAuditReport:
    run_id: str
    selection: ClaimSupportSelection
    verdicts: tuple[ClaimSupportVerdict, ...]
    model_report: str

    def render(self) -> str:
        return "\n\n".join(
            [
                "# Claim Support Audit",
                "## Audit Scope\n\n" + self._scope(),
                "## Deterministic Findings\n\n" + self._findings(),
                "## Verdict Totals\n\n" + self._verdict_totals(),
                "## Model Verdicts\n\n" + self._verdicts(),
                "## Model Report\n\n" + self._model_report(),
                "## Caveat\n\n"
                "This is a bounded claim-support audit over selected generated "
                "claims, not proof that every wiki claim is supported.",
            ]
        )

    def _scope(self) -> str:
        return (
            f"Run id: {self.run_id}\n"
            f"Claim candidates discovered: {self.selection.candidate_count}\n"
            f"Audited candidates: {self.selection.audited_count}\n"
            f"Selected for model judgment: {self.selection.selected_count}\n"
            f"Skipped by deterministic findings: "
            f"{self.selection.deterministic_skipped_count}\n"
            f"Skipped by cap: {self.selection.skipped_count}\n"
            f"Max claims: {self.selection.max_claims}"
        )

    def _findings(self) -> str:
        if not self.selection.deterministic_findings:
            return "No deterministic claim-support findings in selected scope."
        return "\n".join(finding.render() for finding in self.selection.deterministic_findings)

    def _verdict_totals(self) -> str:
        counts = {"supported": 0, "too_broad": 0, "not_supported": 0, "unclear": 0}
        for verdict in self.verdicts:
            counts[verdict.verdict] += 1
        return "\n".join(f"- {label}: {count}" for label, count in counts.items())

    def _verdicts(self) -> str:
        if not self.verdicts:
            return "No model claim-support verdicts were recorded."
        return "\n\n".join(verdict.render(index) for index, verdict in enumerate(self.verdicts, 1))

    def _model_report(self) -> str:
        if self.verdicts:
            return (
                "Per-candidate verdict rationale and recommended action are recorded "
                "above. The free-form finish note is omitted so structured tool-call "
                "verdicts remain authoritative."
            )
        note = self.model_report.strip() or "No model report."
        return "Free-form model notes; verdict totals above are harness-computed.\n\n" + note
