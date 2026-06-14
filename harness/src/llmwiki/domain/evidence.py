"""Strict-evidence policy over deterministic citation findings."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

from llmwiki.config import StrictEvidenceMode
from llmwiki.domain.citations import CitationFinding, SourceInventory, inspect_citations


@dataclass(frozen=True)
class EvidencePolicyResult:
    mode: StrictEvidenceMode
    findings: tuple[CitationFinding, ...] = ()

    @property
    def fatal_findings(self) -> tuple[CitationFinding, ...]:
        if self.mode != "fail":
            return ()
        return tuple(finding for finding in self.findings if finding.severity == "fail")

    @property
    def allowed(self) -> bool:
        return not self.fatal_findings

    @property
    def has_warnings(self) -> bool:
        return bool(self.findings)

    def render_for_tool(self, page_name: str) -> str:
        if not self.findings:
            return ""
        heading = f"Strict evidence findings for page '{page_name}' (mode={self.mode}):"
        return heading + "\n" + _render_findings(self.findings)


@dataclass(frozen=True)
class EvidenceLintReport:
    mode: StrictEvidenceMode
    findings: tuple[CitationFinding, ...] = ()

    @property
    def fail_count(self) -> int:
        return sum(1 for finding in self.findings if finding.severity == "fail")

    @property
    def warn_count(self) -> int:
        return sum(1 for finding in self.findings if finding.severity == "warn")

    def render(self) -> str:
        if self.mode == "off":
            return "Strict evidence mode: off. Citation validation skipped."
        summary = (
            f"Strict evidence mode: {self.mode}. "
            f"Citation findings: {len(self.findings)} "
            f"({self.fail_count} fail, {self.warn_count} warn)."
        )
        if not self.findings:
            return summary + "\nNo deterministic citation evidence findings."
        return summary + "\n" + _render_findings(self.findings)


@dataclass(frozen=True)
class EvidencePolicy:
    mode: StrictEvidenceMode = "off"

    @property
    def enabled(self) -> bool:
        return self.mode != "off"

    def check_page(
        self, page_name: str, body: str, inventory: SourceInventory | None
    ) -> EvidencePolicyResult:
        if self.mode == "off":
            return EvidencePolicyResult(mode=self.mode)
        if inventory is None:
            raise ValueError("Source inventory is required when strict evidence is enabled.")
        report = inspect_citations(page_name, body, inventory)
        return EvidencePolicyResult(mode=self.mode, findings=report.findings)

    def lint_pages(
        self, pages: Mapping[str, str], inventory: SourceInventory | None
    ) -> EvidenceLintReport:
        if self.mode == "off":
            return EvidenceLintReport(mode=self.mode)
        if inventory is None:
            raise ValueError("Source inventory is required when strict evidence is enabled.")
        findings: list[CitationFinding] = []
        for page_name in sorted(pages):
            report = inspect_citations(page_name, pages[page_name], inventory)
            findings.extend(report.findings)
        return EvidenceLintReport(mode=self.mode, findings=tuple(findings))


def _render_findings(findings: tuple[CitationFinding, ...]) -> str:
    ordered = sorted(
        findings,
        key=lambda finding: (
            finding.page_name,
            finding.severity,
            finding.code,
            finding.citation_text,
        ),
    )
    return "\n".join(
        f"- {finding.severity.upper()} {finding.page_name}: "
        f"{finding.code}: {finding.citation_text} -- {finding.message}"
        for finding in ordered
    )
