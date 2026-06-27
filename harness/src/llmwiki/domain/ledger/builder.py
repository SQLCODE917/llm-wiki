"""ClaimLedgerBuilder: the pure builder for one source's claim ledger.

It accounts for every segment with exactly one disposition, validates atom
candidates against the active atom schema set, turns accepted candidates and
eligible claims into ledger entries, retains extractor decisions and rejected
candidates for audit, and derives the source profile and family assignment.
It performs no I/O; given the same input it returns the same ledger.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.assembly import build_segment_entries, segment_disposition
from llmwiki.domain.ledger.atom_context import build_technical_atom_contexts
from llmwiki.domain.ledger.atoms import AtomCandidate, TechnicalAtom
from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.confidence import ConfidencePolicy
from llmwiki.domain.ledger.entries import LedgerEntry, SourceStatement
from llmwiki.domain.ledger.extraction import (
    ActiveExtractorCapabilitySet,
    ExtractedUnitProfile,
    ExtractorDecision,
)
from llmwiki.domain.ledger.extractors import extract_segment
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.profiles import assign_family, build_source_profile
from llmwiki.domain.ledger.schemas import (
    AbstainReasonPolicy,
    AtomSchemaSet,
    AtomValidator,
    CalibrationPolicy,
    FeatureSignalPolicy,
    default_active_extractor_capability_set,
    default_atom_schema_set,
    default_calibration_policy,
)
from llmwiki.domain.ledger.segments import SegmentClaim, SourceSegment
from llmwiki.domain.ledger.structure import (
    DocumentStructure,
    ExtractedUnitDispositionRecord,
)
from llmwiki.domain.ledger.structure_build import build_structure
from llmwiki.domain.ledger.vocab import LEDGER_ENTRY_KINDS


@dataclass(frozen=True)
class SegmentInput:
    segment: SourceSegment
    claims: tuple[SegmentClaim, ...] = ()


@dataclass(frozen=True)
class SchemaBundle:
    atom_schema_set: AtomSchemaSet
    capabilities: ActiveExtractorCapabilitySet
    calibration: CalibrationPolicy
    confidence_policy: ConfidencePolicy
    feature_policy: FeatureSignalPolicy
    abstain_policy: AbstainReasonPolicy


@dataclass(frozen=True)
class LedgerBuildResult:
    ledger: ClaimLedger
    document_structure: DocumentStructure


def default_schema_bundle() -> SchemaBundle:
    return SchemaBundle(
        atom_schema_set=default_atom_schema_set(),
        capabilities=default_active_extractor_capability_set(),
        calibration=default_calibration_policy(),
        confidence_policy=ConfidencePolicy(),
        feature_policy=FeatureSignalPolicy(),
        abstain_policy=AbstainReasonPolicy(),
    )


def build_claim_ledger(
    *,
    source_locator: str,
    source_hash: str,
    evidence_registry_hash: str,
    segments: tuple[SegmentInput, ...],
    profiles: dict[str, ExtractedUnitProfile],
    schema: SchemaBundle,
) -> LedgerBuildResult:
    validator = AtomValidator(schema.atom_schema_set)
    plan = build_structure(source_hash, source_locator, tuple(s.segment for s in segments))
    skeleton = DocumentStructure(plan.root_node_id, plan.nodes)

    entries: list[LedgerEntry] = []
    atoms: list[TechnicalAtom] = []
    decisions: list[ExtractorDecision] = []
    rejected: list[AtomCandidate] = []
    statements: list[SourceStatement] = []
    dispositions: list[ExtractedUnitDispositionRecord] = []

    for item in segments:
        seg = item.segment
        node_ids = skeleton.ancestry(plan.node_for_segment[seg.segment_id])
        statement_id = deterministic_id("source-statement", source_hash, seg.source_range_id)
        if seg.segment_kind == "blank":
            dispositions.append(_disposition(seg, "non-claim"))
            continue
        profile = profiles[seg.segment_id]
        extraction = extract_segment(
            seg,
            profile,
            capabilities=schema.capabilities,
            calibration=schema.calibration,
            validator=validator,
        )
        decisions.extend(extraction.decisions)
        if seg.segment_kind == "heading":
            dispositions.append(_disposition(seg, "structural"))
            continue
        produced = build_segment_entries(
            seg,
            item.claims,
            extraction.candidates,
            statement_id,
            node_ids,
            schema.confidence_policy,
            atoms,
            rejected,
        )
        entries.extend(produced)
        if produced:
            statements.append(
                SourceStatement(
                    statement_id,
                    seg.source_range_id,
                    seg.text,
                    tuple(entry.ledger_entry_id for entry in produced),
                )
            )
        dispositions.append(_disposition(seg, segment_disposition(produced, extraction.candidates)))

    ordered_entries = _ordered(entries, segments)
    technical_atom_contexts = build_technical_atom_contexts(
        source_hash=source_hash,
        segments=tuple(item.segment for item in segments),
        entries=ordered_entries,
        atoms=tuple(atoms),
    )
    source_profile = build_source_profile(
        source_locator=source_locator,
        unit_count=len(segments),
        entries=ordered_entries,
        atom_kind_counts=_atom_counts(atoms),
        feature_means=_feature_means(profiles),
    )
    ledger = ClaimLedger(
        claim_ledger_id=deterministic_id("claim-ledger", source_hash),
        source_locator=source_locator,
        source_hash=source_hash,
        evidence_registry_hash=evidence_registry_hash,
        source_profile=source_profile,
        source_family_assignment=assign_family(source_profile),
        entries=ordered_entries,
        technical_atoms=tuple(atoms),
        technical_atom_contexts=technical_atom_contexts,
        source_statements=tuple(statements),
        extractor_decisions=tuple(decisions),
        rejected_candidates=tuple(rejected),
    )
    structure = DocumentStructure(plan.root_node_id, plan.nodes, tuple(dispositions))
    return LedgerBuildResult(ledger, structure)


def _disposition(seg: SourceSegment, disposition: str) -> ExtractedUnitDispositionRecord:
    return ExtractedUnitDispositionRecord(
        seg.segment_id, seg.source_range_id, disposition, seg.source_order
    )


def _ordered(
    entries: list[LedgerEntry], segments: tuple[SegmentInput, ...]
) -> tuple[LedgerEntry, ...]:
    order_of = {s.segment.source_range_id: s.segment.source_order for s in segments}
    kind_rank = {kind: index for index, kind in enumerate(LEDGER_ENTRY_KINDS)}
    return tuple(
        sorted(
            entries,
            key=lambda e: (
                order_of.get(e.source_range_id, 0),
                kind_rank.get(e.ledger_entry_kind, len(kind_rank)),
                e.ledger_entry_id,
            ),
        )
    )


def _atom_counts(atoms: list[TechnicalAtom]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for atom in atoms:
        counts[atom.technical_atom_kind] = counts.get(atom.technical_atom_kind, 0) + 1
    return counts


def _feature_means(profiles: dict[str, ExtractedUnitProfile]) -> dict[str, float]:
    totals: dict[str, float] = {}
    count = 0
    for profile in profiles.values():
        count += 1
        for signal in profile.feature_signals:
            totals[signal.feature_signal_kind] = (
                totals.get(signal.feature_signal_kind, 0.0) + signal.feature_signal_value
            )
    if count == 0:
        return {}
    return {kind: value / count for kind, value in totals.items()}
