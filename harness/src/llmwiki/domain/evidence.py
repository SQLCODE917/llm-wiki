"""Strict-evidence policy over deterministic citation findings."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import cast

from llmwiki.config import StrictEvidenceMode
from llmwiki.domain.citations import (
    CitationFinding,
    FindingCode,
    FindingSeverity,
    SourceInventory,
    inspect_citations,
)
from llmwiki.domain.evidence_locator_index import EvidenceLocatorFinding, EvidenceLocatorIndex
from llmwiki.domain.evidence_locators import (
    locator_match_for_citation,
    source_range_finding,
)
from llmwiki.domain.evidence_registry import EvidenceRegistry
from llmwiki.domain.evidence_resolver import SourceTextResolver, resolve_normalized_evidence


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
    registry: EvidenceRegistry | None = None
    locator_index: EvidenceLocatorIndex | None = None

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
        if self.registry is not None:
            summary += (
                "\nEvidence registry: "
                f"{len(self.registry.source_texts)} source text(s), "
                f"{len(self.registry.source_ranges)} source range(s), "
                f"{len(self.registry.evidence_records)} evidence record(s)."
            )
        if self.locator_index is not None:
            summary += (
                "\nEvidence locator index: "
                f"{len(self.locator_index.locators)} locator(s), "
                f"{len(self.locator_index.findings)} finding(s)."
            )
        if not self.findings:
            return summary + "\nNo deterministic citation evidence findings."
        return summary + "\n" + _render_findings(self.findings)


@dataclass(frozen=True)
class EvidencePolicy:
    mode: StrictEvidenceMode = "off"
    registry: EvidenceRegistry | None = None
    locator_index: EvidenceLocatorIndex | None = None

    @property
    def enabled(self) -> bool:
        return self.mode != "off"

    def check_page(
        self,
        page_name: str,
        body: str,
        inventory: SourceInventory | None,
        source_resolver: SourceTextResolver | None = None,
    ) -> EvidencePolicyResult:
        if self.mode == "off":
            return EvidencePolicyResult(mode=self.mode)
        if inventory is None:
            raise ValueError("Source inventory is required when strict evidence is enabled.")
        report = inspect_citations(page_name, body, inventory)
        findings = list(report.findings)
        if self.registry is not None:
            for citation in report.citations:
                range_finding = source_range_finding(citation, self.registry)
                if range_finding is not None:
                    findings.append(range_finding)
                _, finding = locator_match_for_citation(citation, self.registry)
                if finding is not None:
                    findings.append(finding)
        elif source_resolver is not None:
            for citation in report.citations:
                _, finding = resolve_normalized_evidence(citation, source_resolver)
                if finding is not None:
                    findings.append(finding)
        return EvidencePolicyResult(mode=self.mode, findings=tuple(findings))

    def lint_pages(
        self,
        pages: Mapping[str, str],
        inventory: SourceInventory | None,
        source_resolver: SourceTextResolver | None = None,
        registry: EvidenceRegistry | None = None,
        locator_index: EvidenceLocatorIndex | None = None,
    ) -> EvidenceLintReport:
        if self.mode == "off":
            return EvidenceLintReport(mode=self.mode)
        if inventory is None:
            raise ValueError("Source inventory is required when strict evidence is enabled.")
        findings: list[CitationFinding] = []
        active_policy = EvidencePolicy(
            mode=self.mode,
            registry=registry or self.registry,
            locator_index=locator_index or self.locator_index,
        )
        for page_name in sorted(pages):
            result = active_policy.check_page(
                page_name, pages[page_name], inventory, source_resolver
            )
            findings.extend(result.findings)
        active_locator_index = locator_index or self.locator_index
        if active_locator_index is not None:
            findings.extend(_locator_index_findings(active_locator_index))
        return EvidenceLintReport(
            mode=self.mode,
            findings=tuple(findings),
            registry=registry,
            locator_index=active_locator_index,
        )


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


def _locator_index_findings(index: EvidenceLocatorIndex) -> tuple[CitationFinding, ...]:
    return tuple(_locator_index_finding(finding) for finding in index.findings)


def _locator_index_finding(finding: EvidenceLocatorFinding) -> CitationFinding:
    severity = "fail" if finding.severity == "blocker" else "warn"
    code = "locator-out-of-range" if finding.category == "invalid-range" else "missing-source"
    return CitationFinding(
        page_name=finding.page_id or index_page_name(finding.source_locator),
        severity=cast(FindingSeverity, severity),
        citation_text=finding.locator_id,
        code=cast(FindingCode, code),
        message=f"{finding.category}: {finding.message}",
    )


def index_page_name(source_locator: str) -> str:
    return source_locator.rsplit("/", 1)[-1].rsplit(".", 1)[0]
