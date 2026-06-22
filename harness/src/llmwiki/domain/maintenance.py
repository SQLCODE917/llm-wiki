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
from llmwiki.domain.links import compute_findings
from llmwiki.domain.objects import LintRun
from llmwiki.domain.pages import PageError, parse_page
from llmwiki.domain.salience import SalienceReport
from llmwiki.domain.schema import PAGE_KINDS
from llmwiki.domain.system_pages import ORPHAN_EXEMPT_PAGES

_LOG_HEADING_RE = re.compile(r"^## \[[^\]]+\] .+")


@dataclass(frozen=True)
class WikiShapeSummary:
    page_count: int
    page_counts_by_page_kind: tuple[tuple[str, int], ...]
    source_page_count: int
    raw_source_count: int
    index_exists: bool
    log_exists: bool
    invalid_page_count: int

    def render(self) -> str:
        page_kind_lines = "\n".join(
            f"- {page_kind}: {count}" for page_kind, count in self.page_counts_by_page_kind
        )
        return (
            f"Total wiki pages: {self.page_count}\n"
            f"Raw source files: {self.raw_source_count}\n"
            f"Source pages: {self.source_page_count}\n"
            f"index.md: {_present(self.index_exists)}\n"
            f"log.md: {_present(self.log_exists)}\n"
            f"Pages with invalid frontmatter: {self.invalid_page_count}\n\n"
            "Pages by page kind:\n"
            f"{page_kind_lines}"
        )


@dataclass(frozen=True)
class RecommendedAction:
    label: str
    reason: str
    command: str

    def render(self) -> str:
        return f"- {self.label}: {self.reason} Suggested command: `{self.command}`."


@dataclass(frozen=True)
class RoutePlanStatus:
    total_planned_pages: int = 0
    total_route_gaps: int = 0
    recent_route_gaps: tuple[str, ...] = ()

    def render(self) -> str:
        lines = [
            f"Planned pages recorded: {self.total_planned_pages}",
            f"Route gaps recorded: {self.total_route_gaps}",
        ]
        if self.recent_route_gaps:
            lines.append("Recent route gaps:")
            lines.extend(f"- {gap}" for gap in self.recent_route_gaps)
        else:
            lines.append("Recent route gaps: None.")
        return "\n".join(lines)


@dataclass(frozen=True)
class CuratorStatus:
    strict_evidence: StrictEvidenceMode
    shape: WikiShapeSummary
    lint_run: LintRun
    evidence_report: EvidenceLintReport
    salience_report: SalienceReport
    candidate_backlog: CandidateBacklog
    claim_support_summary: str
    semantic_lint_summary: str
    ingest_confidence_summary: str
    route_plan_status: RoutePlanStatus
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
                "## Deterministic Findings\n\n" + self.lint_run.render(),
                "## Citation Evidence\n\n" + self.evidence_report.render(),
                "## Salience\n\n" + (self.salience_report.render() or "No salience entries."),
                "## Candidate Page Backlog\n\n" + self.candidate_backlog.render(),
                "## Ingest Route Plans\n\n" + self.route_plan_status.render(),
                "## Latest Ingest Confidence\n\n"
                + (self.ingest_confidence_summary or "No ingest confidence report."),
                "## Latest Claim Support Audit\n\n"
                + (self.claim_support_summary or "No claim support audit report."),
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
    index_page_ids: set[str],
    raw_source_count: int,
    index_exists: bool,
    log_exists: bool,
    recent_log_entries: Sequence[str],
    evidence_report: EvidenceLintReport,
    salience_report: SalienceReport,
    candidate_backlog: CandidateBacklog,
    strict_evidence: StrictEvidenceMode,
    claim_support_summary: str = "",
    semantic_lint_summary: str = "",
    ingest_confidence_summary: str = "",
    route_plan_status: RoutePlanStatus | None = None,
    graph_status: GraphStatus | None = None,
    lint_run: LintRun | None = None,
) -> CuratorStatus:
    if lint_run is None:
        lint_run = compute_findings(
            page_texts,
            index_page_ids,
            exempt_from_orphans=ORPHAN_EXEMPT_PAGES,
        )
    invalid_pages, page_kind_counts = _page_kind_counts(page_texts)
    shape = WikiShapeSummary(
        page_count=len(page_texts),
        page_counts_by_page_kind=tuple(
            (page_kind, page_kind_counts[page_kind]) for page_kind in PAGE_KINDS
        ),
        source_page_count=page_kind_counts["source"],
        raw_source_count=raw_source_count,
        index_exists=index_exists,
        log_exists=log_exists,
        invalid_page_count=invalid_pages,
    )
    navigation_warnings = _navigation_warnings(index_exists, log_exists)
    return CuratorStatus(
        strict_evidence=strict_evidence,
        shape=shape,
        lint_run=lint_run,
        evidence_report=evidence_report,
        salience_report=salience_report,
        candidate_backlog=candidate_backlog,
        claim_support_summary=claim_support_summary,
        semantic_lint_summary=semantic_lint_summary,
        ingest_confidence_summary=ingest_confidence_summary,
        route_plan_status=route_plan_status or RoutePlanStatus(),
        graph_status=graph_status,
        recent_log_entries=tuple(recent_log_entries),
        navigation_warnings=navigation_warnings,
        recommended_actions=_recommended_actions(
            shape, lint_run, evidence_report, candidate_backlog
        ),
    )


def recent_log_entries(log_text: str, limit: int = 5) -> tuple[str, ...]:
    entries = [line.strip() for line in log_text.splitlines() if _LOG_HEADING_RE.match(line)]
    return tuple(entries[-limit:])


def _page_kind_counts(page_texts: dict[str, str]) -> tuple[int, Counter[str]]:
    invalid = 0
    counts: Counter[str] = Counter({page_kind: 0 for page_kind in PAGE_KINDS})
    for text in page_texts.values():
        try:
            page = parse_page(text)
        except PageError:
            invalid += 1
            continue
        counts[page.page_kind] += 1
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
    findings: LintRun,
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
