"""Build ledger entries from segment claims and accepted technical atoms.

A claim-like entry's ``normalized_text`` is the source-close statement itself,
never a broadened paraphrase — that is what makes a projected page faithful.
Fragmentary or undecomposable statements become needs-review entries rather
than asserted prose. Accepted atoms become technical-atom entries that keep
their exact payload.
"""

from __future__ import annotations

import re

from llmwiki.domain.ledger.atoms import TechnicalAtom, atom_raw_text
from llmwiki.domain.ledger.canonical import content_fingerprint, deterministic_id
from llmwiki.domain.ledger.common import ConfidenceBasis, ReviewReason
from llmwiki.domain.ledger.concepts import concept_facets_for_definition
from llmwiki.domain.ledger.confidence import ConfidencePolicy, ConfidenceSignals
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.propositions import decompose
from llmwiki.domain.ledger.segments import SegmentClaim, SourceSegment

_RELATIONSHIP_CUES: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(r"\b(because|therefore|thus|hence|caused|leads to|results in)\b", re.I), "causes"),
    (re.compile(r"\b(before|after|then|subsequently|prior to)\b", re.I), "precedes"),
    (re.compile(r"\b(defined as|means|refers to|is called)\b", re.I), "defines"),
    (re.compile(r"\b(for example|such as|e\.g\.|for instance)\b", re.I), "exemplifies"),
    (re.compile(r"\b(unlike|whereas|in contrast|compared)\b", re.I), "contrasts-with"),
    (re.compile(r"\b(within|located|inside|throughout)\b", re.I), "located-in"),
    (re.compile(r"\b(limit\w*|only|except|unless|constrain\w*)\b", re.I), "constrains"),
)


def build_claim_entry(
    *,
    segment: SourceSegment,
    claim: SegmentClaim,
    statement_id: str,
    structure_node_ids: tuple[str, ...],
    policy: ConfidencePolicy,
) -> LedgerEntry:
    prop = decompose(claim.statement)
    concept_facets = (
        concept_facets_for_definition(claim.statement, prop.subject)
        if "definition" in claim.role_tags
        else ()
    )
    kind = _claim_kind(claim, prop.temporal_scope is not None, concept_facets)
    anchors_ok = _anchors_resolved(prop)
    confidence, basis = policy.assess(
        ConfidenceSignals(
            evidence_resolved=bool(claim.evidence_ids),
            required_fields_complete=prop.complete,
            validation_passed=True,
            ambiguity_present=not prop.complete,
            anchors_resolved=anchors_ok,
        )
    )
    status = policy.status_for(confidence)
    review_reason: ReviewReason | None = None
    if not prop.complete:
        status, review_reason = (
            "needs-review",
            ReviewReason(
                "fragmentary", "no subject/predicate region recovered", claim.evidence_ids
            ),
        )
    fingerprint = content_fingerprint(
        (kind, claim.statement, prop.subject, prop.predicate, prop.object_value)
    )
    return LedgerEntry(
        ledger_entry_id=deterministic_id(
            "ledger-entry", segment.source_hash, segment.source_range_id, kind, fingerprint
        ),
        source_statement_id=statement_id,
        ledger_entry_kind=kind,
        ledger_entry_status=status,
        extraction_confidence=confidence,
        confidence_basis=basis,
        source_locator=segment.source_locator,
        source_hash=segment.source_hash,
        source_range_id=segment.source_range_id,
        evidence_ids=claim.evidence_ids,
        source_text=claim.statement,
        structure_node_ids=structure_node_ids,
        review_reason=review_reason,
        normalized_text=claim.statement,
        resolution_basis="source-close-statement",
        subject=prop.subject,
        predicate=prop.predicate,
        object_value=prop.object_value,
        polarity=prop.polarity,
        claim_force=prop.claim_force,
        condition_scope=prop.condition_scope,
        condition_text=prop.condition_text,
        exception_text=prop.exception_text,
        temporal_scope=prop.temporal_scope,
        spatial_scope=prop.spatial_scope,
        claim_role_tags=claim.role_tags,
        concept_facets=concept_facets if kind == "concept" else (),
    )


def build_relationship_entry(
    *,
    segment: SourceSegment,
    claim: SegmentClaim,
    primary_entry_id: str,
    statement_id: str,
    structure_node_ids: tuple[str, ...],
) -> LedgerEntry | None:
    relationship_kind = _relationship_kind(claim.statement)
    if relationship_kind is None:
        return None
    fingerprint = content_fingerprint(("relationship", relationship_kind, primary_entry_id))
    return LedgerEntry(
        ledger_entry_id=deterministic_id(
            "ledger-entry",
            segment.source_hash,
            segment.source_range_id,
            "relationship",
            fingerprint,
        ),
        source_statement_id=statement_id,
        ledger_entry_kind="relationship",
        ledger_entry_status="usable",
        extraction_confidence="medium",
        confidence_basis=ConfidenceBasis("relationship-connective-detected"),
        source_locator=segment.source_locator,
        source_hash=segment.source_hash,
        source_range_id=segment.source_range_id,
        evidence_ids=claim.evidence_ids,
        source_text=claim.statement,
        structure_node_ids=structure_node_ids,
        normalized_text=claim.statement,
        relationship_kind=relationship_kind,
        related_entry_ids=(primary_entry_id,),
    )


def build_atom_entry(
    *,
    segment: SourceSegment,
    atom: TechnicalAtom,
    statement_id: str,
    structure_node_ids: tuple[str, ...],
    policy: ConfidencePolicy,
) -> LedgerEntry:
    parsed_clean = atom.parse_status == "parsed"
    confidence, basis = policy.assess(
        ConfidenceSignals(
            evidence_resolved=bool(atom.evidence_ids),
            required_fields_complete=True,
            validation_passed=True,
            ambiguity_present=not parsed_clean,
            exact_payload_preserved=True,
        )
    )
    fingerprint = content_fingerprint(("technical-atom", atom.technical_atom_id))
    return LedgerEntry(
        ledger_entry_id=deterministic_id(
            "ledger-entry",
            segment.source_hash,
            segment.source_range_id,
            "technical-atom",
            fingerprint,
        ),
        source_statement_id=statement_id,
        ledger_entry_kind="technical-atom",
        ledger_entry_status="usable",
        extraction_confidence=confidence,
        confidence_basis=basis,
        source_locator=segment.source_locator,
        source_hash=segment.source_hash,
        source_range_id=segment.source_range_id,
        evidence_ids=atom.evidence_ids,
        source_text=atom_raw_text(atom.payload),
        structure_node_ids=structure_node_ids,
        review_reason=atom.review_reason,
        technical_atom_kind=atom.technical_atom_kind,
        technical_atom_id=atom.technical_atom_id,
    )


def build_source_note(
    *,
    segment: SourceSegment,
    statement_id: str,
    structure_node_ids: tuple[str, ...],
) -> LedgerEntry:
    """A needs-review note for a meaningful segment that yielded no structured entry."""
    fingerprint = content_fingerprint(("source-note", segment.text))
    return LedgerEntry(
        ledger_entry_id=deterministic_id(
            "ledger-entry", segment.source_hash, segment.source_range_id, "source-note", fingerprint
        ),
        source_statement_id=statement_id,
        ledger_entry_kind="source-note",
        ledger_entry_status="needs-review",
        extraction_confidence="low",
        confidence_basis=ConfidenceBasis("segment-not-decomposed"),
        source_locator=segment.source_locator,
        source_hash=segment.source_hash,
        source_range_id=segment.source_range_id,
        evidence_ids=segment.evidence_ids,
        source_text=segment.text,
        structure_node_ids=structure_node_ids,
        review_reason=ReviewReason(
            "unextracted", "segment carries subject matter but no structured claim was recovered"
        ),
        normalized_text="",
    )


def _claim_kind(claim: SegmentClaim, has_temporal: bool, concept_facets: tuple[str, ...]) -> str:
    if "definition" in claim.role_tags and concept_facets:
        return "concept"
    if has_temporal and ("temporal" in claim.role_tags or "provenance" in claim.role_tags):
        return "event"
    return "claim"


def _relationship_kind(statement: str) -> str | None:
    for pattern, kind in _RELATIONSHIP_CUES:
        if pattern.search(statement):
            return kind
    return None


def _anchors_resolved(prop: object) -> bool:
    for attr in ("temporal_scope", "spatial_scope"):
        scope = getattr(prop, attr, None)
        confidence = getattr(scope, f"{attr.split('_')[0]}_confidence", None) if scope else None
        if confidence == "unresolved":
            return False
    return True
