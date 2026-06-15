"""Deterministic curator-status report for routine wiki maintenance."""

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Sequence
from dataclasses import dataclass

from llmwiki.config import StrictEvidenceMode
from llmwiki.domain.candidates import CandidateBacklog
from llmwiki.domain.evidence import EvidenceLintReport
from llmwiki.domain.graph import GraphStatus
from llmwiki.domain.links import LintFindings, compute_findings
from llmwiki.domain.pages import PAGE_CATEGORIES, PageError, parse_page
from llmwiki.domain.salience import SalienceReport
from llmwiki.domain.system_pages import ORPHAN_EXEMPT_PAGES

_LOG_HEADING_RE = re.compile(r"^## \[[^\]]+\] .+")


@dataclass(frozen=True)
class WikiShapeSummary:
    page_count: int
    page_counts_by_category: tuple[tuple[str, int], ...]
    source_page_count: int
    raw_source_count: int
    index_exists: bool
    log_exists: bool
    invalid_page_count: int

    def render(self) -> str:
        category_lines = "\n".join(
            f"- {category}: {count}" for category, count in self.page_counts_by_category
        )
        return (
            f"Total wiki pages: {self.page_count}\n"
            f"Raw source files: {self.raw_source_count}\n"
            f"Source pages: {self.source_page_count}\n"
            f"index.md: {_present(self.index_exists)}\n"
            f"log.md: {_present(self.log_exists)}\n"
            f"Pages with invalid frontmatter: {self.invalid_page_count}\n\n"
            "Pages by category:\n"
            f"{category_lines}"
        )


@dataclass(frozen=True)
class RecommendedAction:
    label: str
    reason: str
    command: str

    def render(self) -> str:
        return f"- {self.label}: {self.reason} Suggested command: `{self.command}`."


@dataclass(frozen=True)
class CuratorStatus:
    strict_evidence: StrictEvidenceMode
    shape: WikiShapeSummary
    link_findings: LintFindings
    evidence_report: EvidenceLintReport
    salience_report: SalienceReport
    candidate_backlog: CandidateBacklog
    semantic_lint_summary: str
    graph_status: GraphStatus | None
    recent_log_entries: tuple[str, ...]
    navigation_warnings: tuple[str, ...]
    recommended_actions: tuple[RecommendedAction, ...]

    def render(self) -> str:
        return "\n\n".join(
            [
                "# Curator Status",
                f"Strict evidence mode: {self.strict_evidence}",
                "## Wiki Shape\n\n" + self.shape.render(),
                "## Deterministic Findings\n\n" + self.link_findings.render(),
                "## Citation Evidence\n\n" + self.evidence_report.render(),
                "## Salience\n\n" + (self.salience_report.render() or "No salience entries."),
                "## Candidate Page Backlog\n\n" + self.candidate_backlog.render(),
                "## Latest Semantic Lint\n\n"
                + (self.semantic_lint_summary or "No semantic lint report."),
                "## Graph Export\n\n" + _render_graph_status(self.graph_status),
                "## Recent Log Entries\n\n" + _render_lines(self.recent_log_entries),
                "## Navigation Warnings\n\n" + _render_lines(self.navigation_warnings),
                "## Recommended Next Actions\n\n"
                + "\n".join(action.render() for action in self.recommended_actions),
            ]
        )


def build_curator_status(
    *,
    page_texts: dict[str, str],
    index_names: set[str],
    raw_source_count: int,
    index_exists: bool,
    log_exists: bool,
    recent_log_entries: Sequence[str],
    evidence_report: EvidenceLintReport,
    salience_report: SalienceReport,
    candidate_backlog: CandidateBacklog,
    strict_evidence: StrictEvidenceMode,
    semantic_lint_summary: str = "",
    graph_status: GraphStatus | None = None,
    link_findings: LintFindings | None = None,
) -> CuratorStatus:
    if link_findings is None:
        link_findings = compute_findings(
            page_texts,
            index_names,
            exempt_from_orphans=ORPHAN_EXEMPT_PAGES,
        )
    invalid_pages, category_counts = _category_counts(page_texts)
    shape = WikiShapeSummary(
        page_count=len(page_texts),
        page_counts_by_category=tuple(
            (category, category_counts[category]) for category in PAGE_CATEGORIES
        ),
        source_page_count=category_counts["source"],
        raw_source_count=raw_source_count,
        index_exists=index_exists,
        log_exists=log_exists,
        invalid_page_count=invalid_pages,
    )
    navigation_warnings = _navigation_warnings(index_exists, log_exists)
    return CuratorStatus(
        strict_evidence=strict_evidence,
        shape=shape,
        link_findings=link_findings,
        evidence_report=evidence_report,
        salience_report=salience_report,
        candidate_backlog=candidate_backlog,
        semantic_lint_summary=semantic_lint_summary,
        graph_status=graph_status,
        recent_log_entries=tuple(recent_log_entries),
        navigation_warnings=navigation_warnings,
        recommended_actions=_recommended_actions(
            shape, link_findings, evidence_report, candidate_backlog
        ),
    )


def recent_log_entries(log_text: str, limit: int = 5) -> tuple[str, ...]:
    entries = [line.strip() for line in log_text.splitlines() if _LOG_HEADING_RE.match(line)]
    return tuple(entries[-limit:])


def _category_counts(page_texts: dict[str, str]) -> tuple[int, Counter[str]]:
    invalid = 0
    counts: Counter[str] = Counter({category: 0 for category in PAGE_CATEGORIES})
    for name, text in page_texts.items():
        try:
            page = parse_page(name, text)
        except PageError:
            invalid += 1
            continue
        counts[page.category] += 1
    return invalid, counts


def _navigation_warnings(index_exists: bool, log_exists: bool) -> tuple[str, ...]:
    warnings: list[str] = []
    if not index_exists:
        warnings.append("wiki/index.md is missing.")
    if not log_exists:
        warnings.append("wiki/log.md is missing.")
    return tuple(warnings)


def _recommended_actions(
    shape: WikiShapeSummary,
    findings: LintFindings,
    evidence_report: EvidenceLintReport,
    candidate_backlog: CandidateBacklog,
) -> tuple[RecommendedAction, ...]:
    actions: list[RecommendedAction] = []
    if shape.page_count == 0:
        actions.append(
            RecommendedAction(
                "Ingest a source",
                "The wiki has no content pages.",
                "uv run llmwiki ingest <source>",
            )
        )
    if evidence_report.fail_count:
        actions.append(
            RecommendedAction(
                "Fix fatal citation evidence",
                f"{evidence_report.fail_count} citation finding(s) are fatal in strict mode.",
                "uv run llmwiki lint --strict-evidence fail",
            )
        )
    if findings.broken_links:
        actions.append(
            RecommendedAction(
                "Repair broken links",
                f"{sum(len(v) for v in findings.broken_links.values())} broken link(s) found.",
                "uv run llmwiki lint",
            )
        )
    if findings.missing_from_index or findings.stale_index_entries:
        actions.append(
            RecommendedAction(
                "Review index drift",
                "The page files and index.md disagree.",
                "uv run llmwiki lint",
            )
        )
    if findings.orphan_pages:
        actions.append(
            RecommendedAction(
                "Review orphan pages",
                f"{len(findings.orphan_pages)} page(s) have no inbound links.",
                "uv run llmwiki lint",
            )
        )
    queued = [record for record in candidate_backlog.records if record.status == "queued"]
    if queued:
        actions.append(
            RecommendedAction(
                "Review candidate pages",
                f"{len(queued)} candidate page(s) are queued for curator review.",
                "uv run llmwiki candidates",
            )
        )
    if shape.page_count and not actions:
        actions.append(
            RecommendedAction(
                "No deterministic maintenance actions",
                "Measured link, index, orphan, and citation checks are clean.",
                "uv run llmwiki curator-status",
            )
        )
    return tuple(actions)


def _render_lines(lines: Sequence[str]) -> str:
    if not lines:
        return "None."
    return "\n".join(f"- {line}" for line in lines)


def _render_graph_status(status: GraphStatus | None) -> str:
    if status is None:
        return "Graph status not computed."
    return status.render()


def _present(value: bool) -> str:
    return "present" if value else "missing"
