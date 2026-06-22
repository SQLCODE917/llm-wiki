"""Generated artifact preparation for ingest confidence reports."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from llmwiki.domain.evidence_locator_index import EvidenceLocatorIndex
from llmwiki.domain.evidence_locator_index_io import evidence_locator_index_to_json
from llmwiki.domain.evidence_registry import (
    EvidenceRegistry,
    SourceText,
    build_evidence_registry,
    source_text_from_text,
)
from llmwiki.domain.evidence_registry_io import registry_to_json
from llmwiki.domain.ingest_confidence import (
    ArtifactFingerprint,
    ArtifactReuseDecision,
    ValidationFinding,
    decide_artifact_reuse,
    validation_finding,
)
from llmwiki.domain.ingest_profiles import IngestProfile, required_new_page_prefix
from llmwiki.domain.objects import (
    ExtractedUnit,
    PagePlan,
    RawSource,
    Schema,
    SourceBundle,
    SourcePlan,
)
from llmwiki.domain.pages import slugify
from llmwiki.domain.planning import (
    build_markdown_page_plan,
    build_page_plan,
    observation_report,
    page_plan_from_json,
    page_plan_to_json,
)
from llmwiki.domain.planning_analysis import build_extracted_unit
from llmwiki.pdf.manifest import ChunkRecord
from llmwiki.pdf.pipeline import ExtractionResult, chunk_file, read_source_text
from llmwiki.runtime.ingest_confidence_locator_artifacts import (
    build_current_locator_index,
    read_locator_index,
)
from llmwiki.runtime.ingest_confidence_pdf_cache import (
    PdfExtractFn,
    pdf_extraction_artifact,
    raw_source_hash,
    runtime_finding,
)
from llmwiki.store import WikiStore

FINGERPRINT_FILE = "artifact-fingerprint.json"


@dataclass(frozen=True)
class PreparedIngestArtifacts:
    decisions: tuple[ArtifactReuseDecision, ...]
    page_plan: PagePlan | None
    evidence_registry: EvidenceRegistry | None
    evidence_locator_index: EvidenceLocatorIndex | None
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
    decisions: list[ArtifactReuseDecision] = []
    findings: list[ValidationFinding] = []
    previous_locator_index = read_locator_index(store, source_locator)
    pdf_result, pdf_decision, pdf_findings = pdf_extraction_artifact(
        store, cache_dir, source_locator, source_hash, fresh=fresh, extract_pdf=extract_pdf
    )
    if pdf_decision is not None:
        decisions.append(pdf_decision)
    findings.extend(pdf_findings)
    cached = _reused_artifacts(
        store, artifact_dir, source_locator, plan_decision, registry_decision, locator_decision
    )
    if cached is not None:
        decisions.extend((plan_decision, registry_decision, locator_decision))
        return PreparedIngestArtifacts(
            tuple(decisions), cached[0], cached[1], cached[2], cached[2], tuple(findings)
        )
    plan = _build_current_page_plan(store, source_locator, today, profiles, pdf_result)
    if plan is None:
        findings.append(runtime_finding(source_locator, "Could not build a current PagePlan."))
        return PreparedIngestArtifacts(
            tuple(decisions), None, None, None, previous_locator_index, tuple(findings)
        )
    registry = _build_current_registry(store, source_locator, plan, pdf_result)
    locator_index = build_current_locator_index(store, source_locator, registry)
    if registry is None:
        findings.append(
            validation_finding(
                severity="blocker",
                category="evidence",
                source_locator=source_locator,
                message="Could not build an EvidenceRegistry for this source.",
            )
        )
    decisions.extend((plan_decision, registry_decision, locator_decision))
    store.write_page_plan_artifacts(
        source_locator, page_plan_to_json(plan), observation_report(plan)
    )
    if registry is not None:
        store.write_evidence_registry_artifact(source_locator, registry_to_json(registry))
    if locator_index is not None:
        store.write_evidence_locator_index_artifact(
            source_locator, evidence_locator_index_to_json(locator_index)
        )
    _write_fingerprint(artifact_dir, fingerprint)
    return PreparedIngestArtifacts(
        tuple(decisions), plan, registry, locator_index, previous_locator_index, tuple(findings)
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


def _reused_artifacts(
    store: WikiStore,
    artifact_dir: Path,
    source_locator: str,
    plan_decision: ArtifactReuseDecision,
    registry_decision: ArtifactReuseDecision,
    locator_decision: ArtifactReuseDecision,
) -> tuple[PagePlan, EvidenceRegistry, EvidenceLocatorIndex] | None:
    if (
        plan_decision.decision != "reuse"
        or registry_decision.decision != "reuse"
        or locator_decision.decision != "reuse"
    ):
        return None
    plan_path = artifact_dir / "page-plan.json"
    try:
        plan = page_plan_from_json(plan_path.read_text(encoding="utf-8"))
        registry = store.read_evidence_registry_artifact(source_locator)
        locator_index = store.read_evidence_locator_index_artifact(source_locator)
    except Exception:
        return None
    if registry is None or locator_index is None:
        return None
    return plan, registry, locator_index


def _build_current_page_plan(
    store: WikiStore,
    source_locator: str,
    today: str,
    profiles: tuple[IngestProfile, ...],
    pdf_result: ExtractionResult | None,
) -> PagePlan | None:
    raw_source = store.raw_source(source_locator)
    source_plan = SourcePlan(raw_source, raw_source.source_format, "plan-pages")
    if source_locator.lower().endswith(".pdf"):
        if pdf_result is None:
            return None
        units = tuple(
            _unit_from_chunk(raw_source, pdf_result, chunk) for chunk in pdf_result.manifest.chunks
        )
        return build_page_plan(
            plan_id=f"{today}-confidence-pdf-{slugify(Path(source_locator).stem)}",
            source_bundle=SourceBundle.one(raw_source),
            raw_source=raw_source,
            extracted_units=units,
            existing_pages=store.page_texts(),
            wiki_structure=store.structure,
            today=today,
            source_plan=source_plan,
            new_page_prefix=required_new_page_prefix(profiles, source_locator)
            or slugify(Path(source_locator).stem),
        )
    return build_markdown_page_plan(
        plan_id=f"{today}-confidence-source-{slugify(Path(source_locator).stem)}",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        source_text=store.read_source(source_locator),
        existing_pages=store.page_texts(),
        wiki_structure=store.structure,
        today=today,
        source_plan=source_plan,
        new_page_prefix=required_new_page_prefix(profiles, source_locator),
    )


def _unit_from_chunk(
    raw_source: RawSource, result: ExtractionResult, chunk: ChunkRecord
) -> ExtractedUnit:
    return build_extracted_unit(
        unit_id=f"unit-{chunk.chunk_id:04d}",
        raw_source=raw_source,
        locator=f"p.{chunk.start_page}-{chunk.end_page}",
        heading_path=chunk.heading,
        text=chunk_file(result.cache_dir, chunk.chunk_id).read_text(encoding="utf-8"),
    )


def _build_current_registry(
    store: WikiStore,
    source_locator: str,
    plan: PagePlan,
    pdf_result: ExtractionResult | None,
) -> EvidenceRegistry | None:
    source_text = _source_text_for_registry(store, source_locator, pdf_result)
    if source_text is None:
        return None
    return build_evidence_registry(plan, (source_text,))


def _source_text_for_registry(
    store: WikiStore, source_locator: str, pdf_result: ExtractionResult | None
) -> SourceText | None:
    if source_locator.lower().endswith(".pdf") and pdf_result is not None:
        text = read_source_text(pdf_result.cache_dir)
        return source_text_from_text(source_locator, text, "pdf-cache")
    return store.source_resolver().source_text(source_locator)


def _read_fingerprint(artifact_dir: Path) -> ArtifactFingerprint | None:
    path = artifact_dir / FINGERPRINT_FILE
    if not path.is_file():
        return None
    try:
        return ArtifactFingerprint.from_json_text(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _write_fingerprint(artifact_dir: Path, fingerprint: ArtifactFingerprint) -> None:
    artifact_dir.mkdir(parents=True, exist_ok=True)
    (artifact_dir / FINGERPRINT_FILE).write_text(fingerprint.to_json_text(), encoding="utf-8")
