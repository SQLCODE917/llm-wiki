"""Generated artifact preparation for ingest confidence reports."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from llmwiki.domain.evidence_locator_index import EvidenceLocatorIndex
from llmwiki.domain.evidence_registry import EvidenceRegistry
from llmwiki.domain.ingest_confidence import (
    ArtifactFingerprint,
    ArtifactReuseDecision,
    ValidationFinding,
    decide_artifact_reuse,
    validation_finding,
)
from llmwiki.domain.ingest_profiles import IngestProfile
from llmwiki.domain.objects import PagePlan, Schema
from llmwiki.domain.technical_atom_builder import build_technical_atom_catalog
from llmwiki.domain.technical_atoms import TechnicalAtomCatalog
from llmwiki.runtime.ingest_confidence_artifact_store import (
    read_cached_artifacts,
    write_generated_artifacts,
)
from llmwiki.runtime.ingest_confidence_locator_artifacts import (
    build_current_locator_index,
    read_locator_index,
)
from llmwiki.runtime.ingest_confidence_page_plan_artifacts import (
    build_current_page_plan,
    build_current_registry,
)
from llmwiki.runtime.ingest_confidence_pdf_cache import (
    PdfExtractFn,
    pdf_extraction_artifact,
    raw_source_hash,
    runtime_finding,
)
from llmwiki.runtime.ingest_confidence_persisted_artifacts import (
    parsed_persisted_decision,
    read_persisted_locator_index,
    read_persisted_page_plan,
    read_persisted_registry,
)
from llmwiki.store import WikiStore

FINGERPRINT_FILE = "artifact-fingerprint.json"


@dataclass(frozen=True)
class PreparedIngestArtifacts:
    decisions: tuple[ArtifactReuseDecision, ...]
    page_plan: PagePlan | None
    evidence_registry: EvidenceRegistry | None
    evidence_locator_index: EvidenceLocatorIndex | None
    technical_atom_catalog: TechnicalAtomCatalog | None
    previous_evidence_locator_index: EvidenceLocatorIndex | None
    findings: tuple[ValidationFinding, ...]


def prepare_ingest_confidence_artifacts(
    *,
    store: WikiStore,
    cache_dir: Path,
    source_locator: str,
    today: str,
    profiles: tuple[IngestProfile, ...] = (),
    fresh: bool = False,
    extract_pdf: PdfExtractFn | None = None,
) -> PreparedIngestArtifacts:
    source_hash = raw_source_hash(store.raw_source_path(source_locator))
    fingerprint = ArtifactFingerprint.from_schema(
        source_locator=source_locator,
        source_hash=source_hash,
        schema=Schema(),
        profile_ids=tuple(profile.id for profile in profiles),
    )
    artifact_dir = store.page_plan_artifact_dir(source_locator)
    stored = _read_fingerprint(artifact_dir)
    plan_decision = _cache_decision(
        "page-plan", artifact_dir / "page-plan.json", fingerprint, stored, fresh
    )
    registry_decision = _cache_decision(
        "evidence-registry",
        artifact_dir / "evidence-registry.json",
        fingerprint,
        stored,
        fresh,
    )
    locator_decision = _cache_decision(
        "evidence-locators",
        artifact_dir / "evidence-locators.json",
        fingerprint,
        stored,
        fresh,
    )
    atom_decision = _cache_decision(
        "technical-atoms",
        artifact_dir / "technical-atoms.json",
        fingerprint,
        stored,
        fresh,
    )
    decisions: list[ArtifactReuseDecision] = []
    findings: list[ValidationFinding] = []
    previous_locator_index = read_locator_index(store, source_locator)
    cached = read_cached_artifacts(
        store,
        artifact_dir,
        source_locator,
        plan_decision,
        registry_decision,
        locator_decision,
        atom_decision,
    )
    if cached is not None:
        decisions.extend((plan_decision, registry_decision, locator_decision, atom_decision))
        return PreparedIngestArtifacts(
            tuple(decisions), cached[0], cached[1], cached[2], cached[3], cached[2], tuple(findings)
        )
    plan_decision_for_report = plan_decision
    registry_decision_for_report = registry_decision
    locator_decision_for_report = locator_decision
    plan = read_persisted_page_plan(artifact_dir, plan_decision, fresh, source_locator)
    registry = read_persisted_registry(store, source_locator, registry_decision, fresh, source_hash)
    locator_index = read_persisted_locator_index(
        store, source_locator, locator_decision, fresh, source_hash
    )
    if plan is not None:
        plan_decision_for_report = parsed_persisted_decision(
            "page-plan",
            artifact_dir / "page-plan.json",
            fingerprint,
            "parsed persisted PagePlan artifact",
        )
    if registry is not None:
        registry_decision_for_report = parsed_persisted_decision(
            "evidence-registry",
            artifact_dir / "evidence-registry.json",
            fingerprint,
            "parsed persisted EvidenceRegistry artifact with matching source hash",
        )
    if locator_index is not None:
        locator_decision_for_report = parsed_persisted_decision(
            "evidence-locators",
            artifact_dir / "evidence-locators.json",
            fingerprint,
            "parsed persisted EvidenceLocatorIndex artifact with matching source hash",
        )
    if plan is not None and registry is not None:
        locator_index = locator_index or build_current_locator_index(
            store, source_locator, registry
        )
        atom_catalog: TechnicalAtomCatalog | None
        atom_catalog = build_technical_atom_catalog(
            source_locator=source_locator,
            page_plan=plan,
            evidence_registry=registry,
            artifact_fingerprint=fingerprint.digest,
        )
        decisions.extend(
            (
                plan_decision_for_report,
                registry_decision_for_report,
                locator_decision_for_report,
                atom_decision,
            )
        )
        write_generated_artifacts(
            store,
            source_locator,
            artifact_dir,
            fingerprint,
            plan,
            registry,
            locator_index,
            atom_catalog,
        )
        return PreparedIngestArtifacts(
            tuple(decisions),
            plan,
            registry,
            locator_index,
            atom_catalog,
            previous_locator_index,
            tuple(findings),
        )
    pdf_result, pdf_decision, pdf_findings = pdf_extraction_artifact(
        store, cache_dir, source_locator, source_hash, fresh=fresh, extract_pdf=extract_pdf
    )
    if pdf_decision is not None:
        decisions.append(pdf_decision)
    findings.extend(pdf_findings)
    if plan is None:
        plan = build_current_page_plan(store, source_locator, today, profiles, pdf_result)
    if plan is None:
        findings.append(runtime_finding(source_locator, "Could not build a current PagePlan."))
        return PreparedIngestArtifacts(
            tuple(decisions), None, None, None, None, previous_locator_index, tuple(findings)
        )
    if registry is None:
        registry = build_current_registry(store, source_locator, plan, pdf_result)
    locator_index = locator_index or build_current_locator_index(store, source_locator, registry)
    atom_catalog = (
        build_technical_atom_catalog(
            source_locator=source_locator,
            page_plan=plan,
            evidence_registry=registry,
            artifact_fingerprint=fingerprint.digest,
        )
        if registry is not None
        else None
    )
    if registry is None:
        findings.append(
            validation_finding(
                severity="blocker",
                category="evidence",
                source_locator=source_locator,
                message="Could not build an EvidenceRegistry for this source.",
            )
        )
    decisions.extend(
        (
            plan_decision_for_report,
            registry_decision_for_report,
            locator_decision_for_report,
            atom_decision,
        )
    )
    write_generated_artifacts(
        store,
        source_locator,
        artifact_dir,
        fingerprint,
        plan,
        registry,
        locator_index,
        atom_catalog,
    )
    return PreparedIngestArtifacts(
        tuple(decisions),
        plan,
        registry,
        locator_index,
        atom_catalog,
        previous_locator_index,
        tuple(findings),
    )


def _cache_decision(
    artifact_kind: str,
    artifact_path: Path,
    fingerprint: ArtifactFingerprint,
    stored: ArtifactFingerprint | None,
    fresh: bool,
) -> ArtifactReuseDecision:
    return decide_artifact_reuse(
        artifact_kind=artifact_kind,
        artifact_path=str(artifact_path),
        current=fingerprint,
        stored=stored,
        artifact_exists=artifact_path.is_file(),
        fresh=fresh,
    )


def _read_fingerprint(artifact_dir: Path) -> ArtifactFingerprint | None:
    path = artifact_dir / FINGERPRINT_FILE
    if not path.is_file():
        return None
    try:
        return ArtifactFingerprint.from_json_text(path.read_text(encoding="utf-8"))
    except Exception:
        return None
