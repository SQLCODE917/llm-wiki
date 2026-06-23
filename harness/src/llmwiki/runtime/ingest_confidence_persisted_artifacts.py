"""Read current-enough persisted confidence artifacts."""

from __future__ import annotations

from pathlib import Path

from llmwiki.domain.evidence_locator_index import EvidenceLocatorIndex
from llmwiki.domain.evidence_registry import EvidenceRegistry
from llmwiki.domain.ingest_confidence import ArtifactFingerprint, ArtifactReuseDecision
from llmwiki.domain.objects import PagePlan
from llmwiki.domain.planning import page_plan_from_json
from llmwiki.store import WikiStore


def parsed_persisted_decision(
    artifact_kind: str,
    artifact_path: Path,
    fingerprint: ArtifactFingerprint,
    reason: str,
) -> ArtifactReuseDecision:
    return ArtifactReuseDecision(
        artifact_kind,
        str(artifact_path),
        "reuse",
        reason,
        fingerprint.digest,
    )


def read_persisted_page_plan(
    artifact_dir: Path, decision: ArtifactReuseDecision, fresh: bool, source_locator: str
) -> PagePlan | None:
    if fresh or decision.decision == "missing":
        return None
    path = artifact_dir / "page-plan.json"
    try:
        plan = page_plan_from_json(path.read_text(encoding="utf-8"))
    except Exception:
        return None
    return plan if _plan_source_matches(plan, source_locator) else None


def read_persisted_registry(
    store: WikiStore,
    source_locator: str,
    decision: ArtifactReuseDecision,
    fresh: bool,
    source_hash: str,
) -> EvidenceRegistry | None:
    if fresh or decision.decision == "missing":
        return None
    try:
        registry = store.read_evidence_registry_artifact(source_locator)
    except Exception:
        return None
    if registry is None:
        return None
    hashes = {
        text.source_hash for text in registry.source_texts if text.source_locator == source_locator
    }
    return registry if source_hash in hashes else None


def read_persisted_locator_index(
    store: WikiStore,
    source_locator: str,
    decision: ArtifactReuseDecision,
    fresh: bool,
    source_hash: str,
) -> EvidenceLocatorIndex | None:
    if fresh or decision.decision == "missing":
        return None
    try:
        index = store.read_evidence_locator_index_artifact(source_locator)
    except Exception:
        return None
    if index is None:
        return None
    return index if index.source_hash == source_hash else None


def _plan_source_matches(plan: PagePlan, source_locator: str) -> bool:
    return any(
        raw_source.source_locator == source_locator for raw_source in plan.source_bundle.raw_sources
    )
