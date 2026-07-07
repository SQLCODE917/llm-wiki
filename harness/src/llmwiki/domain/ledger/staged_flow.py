"""Pure staged-ingest flow domain objects."""

from __future__ import annotations

import re
from dataclasses import replace

from llmwiki.domain.ledger.canonical import artifact_fingerprint, deterministic_id
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.projection_navigation_closure import (
    generated_page_navigation_findings,
)
from llmwiki.domain.ledger.staged_contracts import (
    ARTIFACT_FORMAT,
    LedgerExtractionResult,
    ProjectionLintFinding,
    ProjectionLintRun,
    PublishRun,
    SourcePlan,
    StagedWikiPage,
    StagedWikiPageSet,
)
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.vocab import EXTRACTOR_CAPABILITY_IDS, TECHNICAL_ATOM_KINDS
from llmwiki.domain.pages import WikiPage
from llmwiki.domain.schema import PAGE_FAMILIES, PAGE_KINDS

_RELATED_LINE = re.compile(r"^\s*-\s+\[\[[a-z0-9-]+]]")


def build_source_plan(
    *, source_locator: str, source_hash: str, source_page_id: str
) -> SourcePlan:
    draft = SourcePlan(
        source_plan_id=deterministic_id("source-plan", source_hash, source_locator),
        source_plan_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        source_locator=source_locator,
        source_hash=source_hash,
        source_page_id=source_page_id,
        allowed_page_kinds=tuple(PAGE_KINDS),
        allowed_page_families=tuple(PAGE_FAMILIES),
        allowed_extractor_capability_ids=tuple(EXTRACTOR_CAPABILITY_IDS),
        allowed_technical_atom_kinds=tuple(TECHNICAL_ATOM_KINDS),
    )
    fingerprint = artifact_fingerprint(draft, exclude=("source_plan_fingerprint",))
    return replace(draft, source_plan_fingerprint=fingerprint)


def build_extraction_result(
    *,
    source_plan: SourcePlan,
    ledger: ClaimLedger,
    structure: DocumentStructure,
    document_structure_artifact_id: str,
    claim_ledger_id: str,
) -> LedgerExtractionResult:
    draft = LedgerExtractionResult(
        extraction_result_id=deterministic_id(
            "extraction-result", source_plan.source_plan_id, claim_ledger_id
        ),
        extraction_result_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        source_plan_id=source_plan.source_plan_id,
        source_locator=source_plan.source_locator,
        source_hash=source_plan.source_hash,
        document_structure_artifact_id=document_structure_artifact_id,
        claim_ledger_id=claim_ledger_id,
        source_statement_ids=tuple(
            statement.source_statement_id for statement in ledger.source_statements
        ),
        accepted_entry_ids=tuple(entry.ledger_entry_id for entry in ledger.usable_entries),
        needs_review_entry_ids=tuple(
            entry.ledger_entry_id for entry in ledger.needs_review_entries
        ),
        rejected_entry_ids=tuple(
            entry.ledger_entry_id
            for entry in ledger.entries
            if entry.ledger_entry_status == "rejected"
        ),
        technical_atom_ids=tuple(atom.technical_atom_id for atom in ledger.technical_atoms),
        extractor_decision_count=len(ledger.extractor_decisions),
        rejected_candidate_count=len(ledger.rejected_candidates),
    )
    fingerprint = artifact_fingerprint(draft, exclude=("extraction_result_fingerprint",))
    return replace(draft, extraction_result_fingerprint=fingerprint)


def build_staged_page_set(
    source_plan: SourcePlan, pages: tuple[WikiPage, ...]
) -> StagedWikiPageSet:
    staged = tuple(_staged_page(source_plan, page) for page in pages)
    draft = StagedWikiPageSet(
        staged_page_set_id=deterministic_id(
            "staged-page-set", source_plan.source_plan_id, "|".join(p.page_id for p in staged)
        ),
        staged_page_set_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        source_plan_id=source_plan.source_plan_id,
        pages=staged,
    )
    fingerprint = artifact_fingerprint(draft, exclude=("staged_page_set_fingerprint",))
    return replace(draft, staged_page_set_fingerprint=fingerprint)


def build_lint_run(
    *,
    source_plan: SourcePlan,
    staged_page_set: StagedWikiPageSet,
    upstream_write_decision: str,
) -> ProjectionLintRun:
    findings = _lint_findings(source_plan, staged_page_set, upstream_write_decision)
    page_ids = tuple(page.page_id for page in staged_page_set.pages)
    blocking_page_ids = {
        finding.page_id
        for finding in findings
        if finding.severity == "blocking" and finding.page_id
    }
    global_blocking = any(
        finding.severity == "blocking" and not finding.page_id for finding in findings
    )
    accepted = (
        ()
        if global_blocking
        else tuple(page_id for page_id in page_ids if page_id not in blocking_page_ids)
    )
    rejected = (
        page_ids
        if global_blocking
        else tuple(page_id for page_id in page_ids if page_id in blocking_page_ids)
    )
    status = _lint_status(findings, accepted, rejected, global_blocking)
    draft = ProjectionLintRun(
        lint_run_id=deterministic_id(
            "projection-lint-run", source_plan.source_plan_id, upstream_write_decision
        ),
        lint_run_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        source_plan_id=source_plan.source_plan_id,
        upstream_write_decision=upstream_write_decision,
        status=status,
        accepted_page_ids=accepted,
        rejected_page_ids=rejected,
        findings=tuple(findings),
    )
    fingerprint = artifact_fingerprint(draft, exclude=("lint_run_fingerprint",))
    return replace(draft, lint_run_fingerprint=fingerprint)


def build_publish_run(
    source_plan: SourcePlan,
    staged_page_set: StagedWikiPageSet,
    lint_run: ProjectionLintRun,
) -> PublishRun:
    accepted = tuple(
        page.page_id
        for page in staged_page_set.pages
        if page.page_id in set(lint_run.accepted_page_ids)
    )
    status = "published" if accepted else "blocked"
    draft = PublishRun(
        publish_run_id=deterministic_id(
            "publish-run", source_plan.source_plan_id, lint_run.lint_run_id
        ),
        publish_run_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        source_plan_id=source_plan.source_plan_id,
        status=status,
        accepted_page_ids=accepted,
        rejected_page_ids=lint_run.rejected_page_ids,
        blocked_reason=_blocked_reason(lint_run),
    )
    fingerprint = artifact_fingerprint(draft, exclude=("publish_run_fingerprint",))
    return replace(draft, publish_run_fingerprint=fingerprint)


def accepted_pages(
    staged_page_set: StagedWikiPageSet, publish_run: PublishRun
) -> tuple[WikiPage, ...]:
    accepted = set(publish_run.accepted_page_ids)
    return tuple(page.page for page in staged_page_set.pages if page.page_id in accepted)


def _staged_page(source_plan: SourcePlan, page: WikiPage) -> StagedWikiPage:
    draft = StagedWikiPage(
        staged_page_id=deterministic_id("staged-page", source_plan.source_plan_id, page.page_id),
        staged_page_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        source_plan_id=source_plan.source_plan_id,
        page_id=page.page_id,
        page_kind=page.page_kind,
        page_family=page.page_metadata.page_family,
        source_locator=source_plan.source_locator,
        page_body_hash=artifact_fingerprint({"page_body": page.page_body}),
        projection_coverage_pointer=page.page_metadata.projection_coverage_pointer,
        page=page,
    )
    fingerprint = artifact_fingerprint(draft, exclude=("staged_page_fingerprint",))
    return replace(draft, staged_page_fingerprint=fingerprint)


def _lint_findings(
    source_plan: SourcePlan, staged_page_set: StagedWikiPageSet, upstream_write_decision: str
) -> list[ProjectionLintFinding]:
    findings: list[ProjectionLintFinding] = []
    if upstream_write_decision == "block-authoritative-write":
        findings.append(
            _finding(
                "blocking",
                "upstream-write-blocked",
                "",
                "quality reports blocked the write",
            )
        )
    if upstream_write_decision == "write-with-review-work":
        findings.append(
            _finding(
                "warning",
                "upstream-review-work",
                "",
                "quality reports allow the write with review work",
            )
        )
    if not staged_page_set.pages and upstream_write_decision != "block-authoritative-write":
        findings.append(
            _finding("blocking", "no-staged-pages", "", "no staged pages were produced")
        )
    seen: set[str] = set()
    for page in staged_page_set.pages:
        findings.extend(_page_findings(source_plan, page, seen))
        seen.add(page.page_id)
    findings.extend(_navigation_closure_findings(source_plan, staged_page_set))
    return findings


def _page_findings(
    source_plan: SourcePlan, page: StagedWikiPage, seen: set[str]
) -> tuple[ProjectionLintFinding, ...]:
    findings: list[ProjectionLintFinding] = []
    if page.page_id in seen:
        findings.append(
            _finding("blocking", "duplicate-page-id", page.page_id, "duplicate staged page id")
        )
    if page.page_kind not in source_plan.allowed_page_kinds:
        findings.append(
            _finding("blocking", "page-kind-not-planned", page.page_id, page.page_kind)
        )
    if page.page_family not in source_plan.allowed_page_families:
        findings.append(
            _finding("blocking", "page-family-not-planned", page.page_id, page.page_family)
        )
    if f"raw/{source_plan.source_locator}" not in page.page.page_metadata.sources:
        findings.append(
            _finding("blocking", "source-support-missing", page.page_id, "raw source missing")
        )
    if not page.page.page_body.strip():
        findings.append(_finding("blocking", "empty-page-body", page.page_id, "page body is empty"))
    if not page.projection_coverage_pointer:
        findings.append(
            _finding(
                "warning",
                "projection-coverage-missing",
                page.page_id,
                "missing coverage pointer",
            )
        )
    findings.extend(_body_contract_findings(page))
    return tuple(findings)


def _navigation_closure_findings(
    source_plan: SourcePlan, staged_page_set: StagedWikiPageSet
) -> tuple[ProjectionLintFinding, ...]:
    page_bodies = {page.page_id: page.page.page_body for page in staged_page_set.pages}
    page_families = {page.page_id: page.page_family for page in staged_page_set.pages}
    return tuple(
        _finding("blocking", finding.finding_type, finding.page_id, finding.message)
        for finding in generated_page_navigation_findings(
            source_page_id=source_plan.source_page_id,
            page_bodies=page_bodies,
            page_families=page_families,
        )
    )


def _body_contract_findings(page: StagedWikiPage) -> tuple[ProjectionLintFinding, ...]:
    findings: list[ProjectionLintFinding] = []
    in_related = False
    lines = page.page.page_body.splitlines()
    for line in lines:
        if line == "## Related pages":
            in_related = True
            continue
        if line.startswith("## ") and in_related:
            in_related = False
        if in_related and _RELATED_LINE.match(line) and " - " not in line:
            findings.append(
                _finding(
                    "blocking",
                    "related-link-reason-missing",
                    page.page_id,
                    "visible related link has no reason",
                )
            )
    if "**Atom:**" in page.page.page_body and '<a id="atom-' not in page.page.page_body:
        findings.append(
            _finding(
                "blocking",
                "technical-atom-anchor-missing",
                page.page_id,
                "rendered technical atom has no stable anchor",
            )
        )
    return tuple(findings)


def _accepted_status(
    findings: tuple[ProjectionLintFinding, ...] | list[ProjectionLintFinding],
) -> str:
    if any(f.severity == "warning" for f in findings):
        return "accepted-with-warnings"
    return "accepted"


def _lint_status(
    findings: tuple[ProjectionLintFinding, ...] | list[ProjectionLintFinding],
    accepted_page_ids: tuple[str, ...],
    rejected_page_ids: tuple[str, ...],
    global_blocking: bool,
) -> str:
    if global_blocking or (rejected_page_ids and not accepted_page_ids):
        return "blocked"
    if rejected_page_ids:
        return "accepted-with-rejections"
    return _accepted_status(findings)


def _blocked_reason(lint_run: ProjectionLintRun) -> str:
    if lint_run.status != "blocked":
        return ""
    return "; ".join(f"{finding.finding_type}:{finding.page_id}" for finding in lint_run.findings)


def _finding(severity: str, finding_type: str, page_id: str, message: str) -> ProjectionLintFinding:
    return ProjectionLintFinding(severity, finding_type, page_id, message)
