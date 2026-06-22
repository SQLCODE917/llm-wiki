"""Report-only claim support audit over generated wiki claims."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

DEFAULT_MAX_CLAIM_SUPPORT_CLAIMS = 5
ClaimSupportSampleStrategy = Literal["ordered", "stratified"]
DEFAULT_CLAIM_SUPPORT_SAMPLE_STRATEGY: ClaimSupportSampleStrategy = "stratified"
ClaimSupportVerdictLabel = Literal["supported", "too_broad", "not_supported", "unclear"]
ClaimSupportSeverity = Literal["blocker", "warning", "info"]
ClaimSupportCategory = Literal[
    "missing-evidence",
    "locator-mismatch",
    "source-range",
    "copied-evidence",
    "support-verdict",
]

MAX_RENDERED_EVIDENCE_IDS = 8


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
    risk_tags: tuple[str, ...] = ()

    def render(self, index: int) -> str:
        citations = ", ".join(self.citation_texts) or "None."
        claims = ", ".join(self.source_claim_ids) or "None."
        excerpts = "\n".join(f"- {excerpt}" for excerpt in self.evidence_excerpts) or "None."
        risk_tags = ", ".join(self.risk_tags) or "None."
        return (
            f"### Candidate {index}: {self.candidate_id}\n"
            f"Page: [[{self.page_id}]]\n"
            f"Kind: {self.candidate_kind}\n"
            f"Risk tags: {risk_tags}\n"
            f"Claim: {self.claim_text}\n"
            f"Local context: {self.page_context}\n"
            f"Citations: {citations}\n"
            f"SourceClaim ids: {claims}\n"
            f"{self._render_evidence_id_summary()}\n"
            f"Evidence excerpts:\n{excerpts}"
        )

    def _render_evidence_id_summary(self) -> str:
        excerpt_ids = _evidence_ids_from_excerpts(self.evidence_excerpts)
        if excerpt_ids:
            return "Evidence excerpt ids: " + ", ".join(excerpt_ids)
        if not self.evidence_ids:
            return "Evidence excerpt ids: None."
        rendered = ", ".join(self.evidence_ids[:MAX_RENDERED_EVIDENCE_IDS])
        omitted = len(self.evidence_ids) - MAX_RENDERED_EVIDENCE_IDS
        if omitted > 0:
            rendered = f"{rendered} ({omitted} more not shown)"
        return "Evidence excerpt ids: " + rendered


@dataclass(frozen=True)
class ClaimSupportCoverageCount:
    label: str
    available: int
    sampled: int

    def render(self) -> str:
        return f"- {self.label}: {self.sampled}/{self.available}"


@dataclass(frozen=True)
class ClaimSupportSampleCoverage:
    sample_strategy: ClaimSupportSampleStrategy
    available_candidates: int
    sampled_candidates: int
    available_pages: int
    sampled_pages: int
    available_source_buckets: int
    sampled_source_buckets: int
    candidate_kind_counts: tuple[ClaimSupportCoverageCount, ...]
    risk_tag_counts: tuple[ClaimSupportCoverageCount, ...]

    def render(self) -> str:
        return "\n".join(
            (
                f"Sample strategy: {self.sample_strategy}",
                f"Sampled candidates: {self.sampled_candidates}/{self.available_candidates}",
                f"Page coverage: {self.sampled_pages}/{self.available_pages}",
                (
                    "Source-bucket coverage: "
                    f"{self.sampled_source_buckets}/{self.available_source_buckets}"
                ),
                "Candidate kinds:",
                _render_counts(self.candidate_kind_counts),
                "Risk tags:",
                _render_counts(self.risk_tag_counts),
            )
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
    sample_strategy: ClaimSupportSampleStrategy = DEFAULT_CLAIM_SUPPORT_SAMPLE_STRATEGY
    sample_coverage: ClaimSupportSampleCoverage | None = None

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

    @property
    def missing_verdict_candidate_ids(self) -> tuple[str, ...]:
        recorded = {verdict.candidate_id for verdict in self.verdicts}
        return tuple(
            candidate.candidate_id
            for candidate in self.selection.candidates
            if candidate.candidate_id not in recorded
        )

    def render(self) -> str:
        return "\n\n".join(
            [
                "# Claim Support Audit",
                "## Audit Scope\n\n" + self._scope(),
                "## Sample Coverage\n\n" + self._sample_coverage(),
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

    def _sample_coverage(self) -> str:
        if self.selection.sample_coverage is None:
            return "No sample coverage report."
        return self.selection.sample_coverage.render()

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


def _render_counts(counts: tuple[ClaimSupportCoverageCount, ...]) -> str:
    if not counts:
        return "- None."
    return "\n".join(count.render() for count in counts)


def _evidence_ids_from_excerpts(excerpts: tuple[str, ...]) -> tuple[str, ...]:
    evidence_ids: list[str] = []
    for excerpt in excerpts:
        evidence_id, separator, _text = excerpt.partition(":")
        if separator and evidence_id.startswith("evidence-"):
            evidence_ids.append(evidence_id)
    return tuple(evidence_ids)
