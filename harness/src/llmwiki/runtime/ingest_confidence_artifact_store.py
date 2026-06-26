"""Read and write generated confidence artifacts."""

from __future__ import annotations

from pathlib import Path

from llmwiki.domain.evidence_locator_index import EvidenceLocatorIndex
from llmwiki.domain.evidence_locator_index_io import evidence_locator_index_to_json
from llmwiki.domain.evidence_registry import EvidenceRegistry
from llmwiki.domain.evidence_registry_io import registry_to_json
from llmwiki.domain.ingest_confidence import ArtifactFingerprint, ArtifactReuseDecision
from llmwiki.domain.ledger.current_artifacts import build_current_ledger_artifacts
from llmwiki.domain.objects import PagePlan
from llmwiki.domain.planning import observation_report, page_plan_from_json, page_plan_to_json
from llmwiki.domain.technical_atom_io import technical_atom_catalog_to_json
from llmwiki.domain.technical_atoms import TechnicalAtomCatalog
from llmwiki.store import WikiStore


def read_cached_artifacts(
    store: WikiStore,
    artifact_dir: Path,
    source_locator: str,
    plan_decision: ArtifactReuseDecision,
    registry_decision: ArtifactReuseDecision,
    locator_decision: ArtifactReuseDecision,
    atom_decision: ArtifactReuseDecision,
) -> tuple[PagePlan, EvidenceRegistry, EvidenceLocatorIndex, TechnicalAtomCatalog] | None:
    if (
        plan_decision.decision != "reuse"
        or registry_decision.decision != "reuse"
        or locator_decision.decision != "reuse"
        or atom_decision.decision != "reuse"
    ):
        return None
    plan_path = artifact_dir / "page-plan.json"
    try:
        plan = page_plan_from_json(plan_path.read_text(encoding="utf-8"))
        registry = store.read_evidence_registry_artifact(source_locator)
        locator_index = store.read_evidence_locator_index_artifact(source_locator)
        atom_catalog = store.read_technical_atom_catalog_artifact(source_locator)
        ledger = store.read_claim_ledger_artifact(source_locator)
    except Exception:
        return None
    if registry is None or locator_index is None or atom_catalog is None or ledger is None:
        return None
    return plan, registry, locator_index, atom_catalog


def write_generated_artifacts(
    store: WikiStore,
    source_locator: str,
    artifact_dir: Path,
    fingerprint: ArtifactFingerprint,
    plan: PagePlan,
    registry: EvidenceRegistry | None,
    locator_index: EvidenceLocatorIndex | None,
    atom_catalog: TechnicalAtomCatalog | None,
) -> None:
    store.write_page_plan_artifacts(
        source_locator, page_plan_to_json(plan), observation_report(plan)
    )
    if registry is not None:
        store.write_evidence_registry_artifact(source_locator, registry_to_json(registry))
    if locator_index is not None:
        store.write_evidence_locator_index_artifact(
            source_locator, evidence_locator_index_to_json(locator_index)
        )
    if atom_catalog is not None:
        store.write_technical_atom_catalog_artifact(
            source_locator, technical_atom_catalog_to_json(atom_catalog)
        )
    if registry is not None and atom_catalog is not None:
        ledger_artifacts = build_current_ledger_artifacts(
            source_locator=source_locator,
            page_plan=plan,
            evidence_registry=registry,
            technical_atom_catalog=atom_catalog,
        )
        store.write_claim_ledger_artifacts(source_locator, ledger_artifacts.artifact_files)
    artifact_dir.mkdir(parents=True, exist_ok=True)
    (artifact_dir / "artifact-fingerprint.json").write_text(
        fingerprint.to_json_text(), encoding="utf-8"
    )
