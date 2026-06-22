"""Domain objects for source-level ingest confidence reports."""

from __future__ import annotations

import hashlib
import json
from collections.abc import Sequence
from dataclasses import asdict, dataclass
from typing import Literal

from llmwiki.domain.objects import Schema

FindingSeverity = Literal["blocker", "warning", "info"]
FindingCategory = Literal[
    "planning",
    "source-summary",
    "citation",
    "evidence",
    "source-range",
    "claim-support",
    "graph",
    "index",
    "runtime",
]
GateKind = Literal["deterministic", "model-assisted"]
GateStatus = Literal["pass", "fail", "skipped"]
ArtifactDecision = Literal["reuse", "rebuild", "missing"]


@dataclass(frozen=True)
class ArtifactFingerprint:
    source_locator: str
    source_hash: str
    schema_id: str
    page_body_contract_digest: str
    profile_ids: tuple[str, ...]
    artifact_version: int = 1

    @classmethod
    def from_schema(
        cls,
        *,
        source_locator: str,
        source_hash: str,
        schema: Schema,
        profile_ids: Sequence[str] = (),
    ) -> ArtifactFingerprint:
        contract_payload = {
            "page_body_contracts": [asdict(contract) for contract in schema.page_body_contracts],
            "page_body_contract_by_page_kind": list(schema.page_body_contract_by_page_kind),
        }
        return cls(
            source_locator=source_locator,
            source_hash=source_hash,
            schema_id=schema.schema_id,
            page_body_contract_digest=_digest_json(contract_payload),
            profile_ids=tuple(profile_ids),
        )

    @property
    def digest(self) -> str:
        return _digest_json(self.to_payload())[:16]

    def to_payload(self) -> dict[str, object]:
        return {
            "artifact_version": self.artifact_version,
            "source_locator": self.source_locator,
            "source_hash": self.source_hash,
            "schema_id": self.schema_id,
            "page_body_contract_digest": self.page_body_contract_digest,
            "profile_ids": list(self.profile_ids),
        }

    def to_json_text(self) -> str:
        return json.dumps(self.to_payload(), indent=2, sort_keys=True) + "\n"

    @classmethod
    def from_json_text(cls, text: str) -> ArtifactFingerprint:
        data = json.loads(text)
        return cls(
            source_locator=str(data["source_locator"]),
            source_hash=str(data["source_hash"]),
            schema_id=str(data["schema_id"]),
            page_body_contract_digest=str(data["page_body_contract_digest"]),
            profile_ids=tuple(str(item) for item in data.get("profile_ids", ())),
            artifact_version=int(data.get("artifact_version", 1)),
        )


@dataclass(frozen=True)
class ArtifactReuseDecision:
    artifact_kind: str
    artifact_path: str
    decision: ArtifactDecision
    reason: str
    fingerprint: str

    def render(self) -> str:
        return (
            f"- {self.artifact_kind}: {self.decision} `{self.artifact_path}` "
            f"({self.reason}; fingerprint {self.fingerprint})"
        )


def decide_artifact_reuse(
    *,
    artifact_kind: str,
    artifact_path: str,
    current: ArtifactFingerprint,
    stored: ArtifactFingerprint | None,
    artifact_exists: bool,
    fresh: bool = False,
) -> ArtifactReuseDecision:
    if not artifact_exists:
        decision: ArtifactDecision = "missing"
        reason = "artifact is missing"
    elif fresh:
        decision = "rebuild"
        reason = "--fresh requested"
    elif stored is None:
        decision = "rebuild"
        reason = "fingerprint is missing or invalid"
    elif stored != current:
        decision = "rebuild"
        reason = "fingerprint differs"
    else:
        decision = "reuse"
        reason = "fingerprint matches"
    return ArtifactReuseDecision(
        artifact_kind=artifact_kind,
        artifact_path=artifact_path,
        decision=decision,
        reason=reason,
        fingerprint=current.digest,
    )


@dataclass(frozen=True)
class ValidationFinding:
    finding_id: str
    severity: FindingSeverity
    category: FindingCategory
    source_locator: str
    page_id: str
    message: str
    fingerprint: str = ""

    def render(self) -> str:
        page = f" {self.page_id}" if self.page_id else ""
        fingerprint = f" fingerprint={self.fingerprint}" if self.fingerprint else ""
        return f"- {self.severity.upper()} {self.category}{page}: {self.message}{fingerprint}"


@dataclass(frozen=True)
class IngestConfidenceGate:
    gate_id: str
    gate_kind: GateKind
    scope: str
    status: GateStatus
    finding_ids: tuple[str, ...] = ()
    detail: str = ""

    def render(self) -> str:
        findings = ", ".join(self.finding_ids) or "none"
        parts = [
            f"### {self.gate_id}",
            f"- Kind: {self.gate_kind}",
            f"- Scope: {self.scope}",
            f"- Status: {self.status}",
            f"- Findings: {findings}",
        ]
        if self.detail.strip():
            parts.append(self.detail.strip())
        return "\n".join(parts)


@dataclass(frozen=True)
class IngestConfidenceReport:
    run_id: str
    source_locator: str
    artifact_decisions: tuple[ArtifactReuseDecision, ...]
    gates: tuple[IngestConfidenceGate, ...]
    findings: tuple[ValidationFinding, ...]
    summary: str = ""

    def render(self) -> str:
        return "\n\n".join(
            [
                "# Ingest Confidence Report",
                "## Summary\n\n" + (self.summary or self.computed_summary),
                "## Artifact Reuse\n\n" + self._artifact_decisions(),
                "## Gates\n\n" + self._gates(),
                "## Findings\n\n" + self._findings(),
                "## Caveat\n\n"
                "This is a bounded post-ingest confidence report, not proof that "
                "every wiki claim is correct.",
            ]
        )

    @property
    def computed_summary(self) -> str:
        blockers = sum(1 for finding in self.findings if finding.severity == "blocker")
        warnings = sum(1 for finding in self.findings if finding.severity == "warning")
        if blockers:
            status = "failed"
        elif warnings:
            status = "passed with warnings"
        else:
            status = "passed"
        return (
            f"Run id: {self.run_id}\n"
            f"Source: raw/{self.source_locator}\n"
            f"Confidence status: {status}\n"
            f"Blockers: {blockers}\n"
            f"Warnings: {warnings}\n"
            f"Gates: {len(self.gates)}"
        )

    def _artifact_decisions(self) -> str:
        if not self.artifact_decisions:
            return "No generated ingest artifacts were checked."
        return "\n".join(decision.render() for decision in self.artifact_decisions)

    def _gates(self) -> str:
        if not self.gates:
            return "No confidence gates were run."
        return "\n\n".join(gate.render() for gate in self.gates)

    def _findings(self) -> str:
        if not self.findings:
            return "No validation findings."
        return "\n".join(finding.render() for finding in self.findings)


def validation_finding(
    *,
    severity: FindingSeverity,
    category: FindingCategory,
    source_locator: str,
    message: str,
    page_id: str = "",
    fingerprint: str = "",
) -> ValidationFinding:
    seed = f"{severity}:{category}:{source_locator}:{page_id}:{message}:{fingerprint}"
    return ValidationFinding(
        finding_id=f"validation-finding-{hashlib.sha256(seed.encode()).hexdigest()[:16]}",
        severity=severity,
        category=category,
        source_locator=source_locator,
        page_id=page_id,
        message=message,
        fingerprint=fingerprint,
    )


def gate_status(findings: Sequence[ValidationFinding]) -> GateStatus:
    return (
        "fail"
        if any(finding.severity in {"blocker", "warning"} for finding in findings)
        else "pass"
    )


def _digest_json(payload: object) -> str:
    text = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
