"""Locator stability gate for ingest confidence reports."""

from __future__ import annotations

from llmwiki.domain.evidence_locator_index import EvidenceLocatorIndex
from llmwiki.domain.ingest_confidence import ValidationFinding, validation_finding


def locator_stability_findings(
    source_locator: str,
    previous: EvidenceLocatorIndex | None,
    current: EvidenceLocatorIndex | None,
) -> tuple[ValidationFinding, ...]:
    if current is None:
        return (
            validation_finding(
                severity="blocker",
                category="locator",
                source_locator=source_locator,
                message="EvidenceLocatorIndex is missing.",
            ),
        )
    findings = [
        validation_finding(
            severity="blocker" if finding.severity == "blocker" else "warning",
            category="locator",
            source_locator=source_locator,
            page_id=finding.page_id,
            message=f"{finding.category}: {finding.message}",
            fingerprint=current.locator_artifact_fingerprint,
        )
        for finding in current.findings
    ]
    if previous is not None:
        old_ids = {locator.locator_id for locator in previous.locators}
        new_ids = {locator.locator_id for locator in current.locators}
        drift_count = len(old_ids.symmetric_difference(new_ids))
        if drift_count:
            findings.append(
                validation_finding(
                    severity="warning",
                    category="locator",
                    source_locator=source_locator,
                    message=f"Locator ids drifted. Drift count: {drift_count}.",
                    fingerprint=current.locator_artifact_fingerprint,
                )
            )
    return tuple(findings)


def locator_stability_detail(
    previous: EvidenceLocatorIndex | None, current: EvidenceLocatorIndex | None
) -> str:
    if current is None:
        return "No EvidenceLocatorIndex available."
    old_ids = {locator.locator_id for locator in previous.locators} if previous else set()
    new_ids = {locator.locator_id for locator in current.locators}
    stable = len(old_ids.intersection(new_ids)) if previous else len(new_ids)
    drift = len(old_ids.symmetric_difference(new_ids)) if previous else 0
    return (
        f"Locators: {len(current.locators)}\n"
        f"Stable locators: {stable}\n"
        f"Locator drift: {drift}\n"
        f"Invalid locators: {current.invalid_count}"
    )
