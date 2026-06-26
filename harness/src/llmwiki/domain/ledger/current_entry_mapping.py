"""Build ledger entries from current source-claim and technical-atom artifacts."""

from __future__ import annotations

from llmwiki.domain.evidence_registry import EvidenceRecord, EvidenceRegistry, SourceRange
from llmwiki.domain.ledger.atoms import TechnicalAtom as LedgerTechnicalAtom
from llmwiki.domain.ledger.atoms import atom_raw_text
from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.common import ConfidenceBasis, ReviewReason
from llmwiki.domain.ledger.current_atom_payloads import ledger_atom_kind, ledger_atom_payload
from llmwiki.domain.ledger.current_structure import source_hash_for_range
from llmwiki.domain.ledger.entries import LedgerEntry, SourceStatement
from llmwiki.domain.ledger.propositions import decompose
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.vocab import LEDGER_ENTRY_KINDS
from llmwiki.domain.objects import PagePlan, SourceClaim
from llmwiki.domain.technical_atoms import TechnicalAtomCatalog


def build_current_claim_entries(
    *,
    page_plan: PagePlan,
    evidence_registry: EvidenceRegistry,
    structure: DocumentStructure,
    range_by_unit: dict[str, SourceRange],
    node_by_page: dict[str, str],
) -> tuple[tuple[LedgerEntry, ...], tuple[SourceStatement, ...]]:
    evidence_by_claim = _evidence_by_claim(evidence_registry.evidence_records)
    entries: list[LedgerEntry] = []
    statements: list[SourceStatement] = []
    for claim in page_plan.source_claims:
        source_range = range_by_unit.get(claim.extracted_unit_id)
        if source_range is None:
            continue
        records = evidence_by_claim.get(claim.source_claim_id, ())
        entry = _claim_entry(
            claim, evidence_registry, source_range, records, structure, node_by_page
        )
        entries.append(entry)
        statements.append(
            SourceStatement(
                entry.source_statement_id,
                source_range.source_range_id,
                claim.statement,
                (entry.ledger_entry_id,),
            )
        )
    return tuple(entries), tuple(statements)


def build_current_atom_entries(
    *,
    source_locator: str,
    source_hash: str,
    evidence_registry: EvidenceRegistry,
    structure: DocumentStructure,
    node_by_page: dict[str, str],
    catalog: TechnicalAtomCatalog,
) -> tuple[tuple[LedgerTechnicalAtom, ...], tuple[LedgerEntry, ...], tuple[SourceStatement, ...]]:
    ranges = {
        source_range.source_range_id: source_range
        for source_range in evidence_registry.source_ranges
    }
    evidence_records = {record.evidence_id: record for record in evidence_registry.evidence_records}
    atoms: list[LedgerTechnicalAtom] = []
    entries: list[LedgerEntry] = []
    statements: list[SourceStatement] = []
    for current in catalog.technical_atoms:
        source_range = ranges.get(current.source_range_id)
        payload = ledger_atom_payload(catalog, current)
        atom_kind = ledger_atom_kind(current.atom_kind)
        atom_source_hash = _atom_source_hash(evidence_records, current.evidence_ids, source_hash)
        atom = LedgerTechnicalAtom(
            technical_atom_id=current.technical_atom_id,
            technical_atom_kind=atom_kind,
            payload=payload,
            source_locator=source_locator,
            source_range_id=current.source_range_id,
            evidence_ids=current.evidence_ids,
            parse_status=getattr(payload, "parse_status", "parsed"),
            review_reason=_atom_review_reason(current.support_status, current.evidence_ids),
        )
        entry = _atom_entry(
            source_locator,
            atom_source_hash,
            current.source_range_id,
            source_range.page_id if source_range is not None else current.page_id,
            structure,
            node_by_page,
            atom,
            current.support_status,
        )
        atoms.append(atom)
        entries.append(entry)
        statements.append(
            SourceStatement(
                entry.source_statement_id,
                current.source_range_id,
                entry.source_text,
                (entry.ledger_entry_id,),
            )
        )
    return tuple(atoms), tuple(entries), tuple(statements)


def ordered_entries(
    entries: tuple[LedgerEntry, ...], source_ranges: tuple[SourceRange, ...]
) -> tuple[LedgerEntry, ...]:
    range_order = {
        source_range.source_range_id: index for index, source_range in enumerate(source_ranges)
    }
    kind_order = {kind: index for index, kind in enumerate(LEDGER_ENTRY_KINDS)}
    return tuple(
        sorted(
            entries,
            key=lambda entry: (
                range_order.get(entry.source_range_id, 999999),
                kind_order.get(entry.ledger_entry_kind, 999),
                entry.ledger_entry_id,
            ),
        )
    )


def _claim_entry(
    claim: SourceClaim,
    registry: EvidenceRegistry,
    source_range: SourceRange,
    records: tuple[EvidenceRecord, ...],
    structure: DocumentStructure,
    node_by_page: dict[str, str],
) -> LedgerEntry:
    evidence_ids = tuple(record.evidence_id for record in records)
    prop = decompose(claim.statement)
    status, review = _claim_status(claim, prop.complete, evidence_ids)
    kind = _claim_kind(claim)
    source_hash = (
        records[0].source_hash if records else source_hash_for_range(registry, source_range)
    )
    statement_id = deterministic_id(
        "source-statement", source_hash, source_range.source_range_id, claim.source_claim_id
    )
    return LedgerEntry(
        ledger_entry_id=deterministic_id(
            "ledger-entry", source_hash, source_range.source_range_id, kind, claim.source_claim_id
        ),
        source_statement_id=statement_id,
        ledger_entry_kind=kind,
        ledger_entry_status=status,
        extraction_confidence=_claim_confidence(claim),
        confidence_basis=ConfidenceBasis("current-source-claim-artifact", claim.claim_role_tags),
        source_locator=source_range.source_locator,
        source_hash=source_hash,
        source_range_id=source_range.source_range_id,
        evidence_ids=evidence_ids,
        source_text=claim.statement,
        structure_node_ids=structure.ancestry(
            node_by_page.get(source_range.page_id, structure.root_node_id)
        ),
        review_reason=review,
        normalized_text=claim.statement,
        resolution_basis="current-source-claim-artifact",
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
        claim_role_tags=claim.claim_role_tags,
        concept_facets=claim.subject_terms if kind == "concept" else (),
    )


def _atom_entry(
    source_locator: str,
    source_hash: str,
    source_range_id: str,
    page_id: str,
    structure: DocumentStructure,
    node_by_page: dict[str, str],
    atom: LedgerTechnicalAtom,
    support_status: str,
) -> LedgerEntry:
    statement_id = deterministic_id(
        "source-statement", source_hash, source_range_id, atom.technical_atom_id
    )
    return LedgerEntry(
        ledger_entry_id=deterministic_id(
            "ledger-entry", source_hash, source_range_id, "technical-atom", atom.technical_atom_id
        ),
        source_statement_id=statement_id,
        ledger_entry_kind="technical-atom",
        ledger_entry_status="usable" if support_status == "supported" else "needs-review",
        extraction_confidence="high" if atom.evidence_ids else "low",
        confidence_basis=ConfidenceBasis("current-technical-atom-catalog"),
        source_locator=source_locator,
        source_hash=source_hash,
        source_range_id=source_range_id,
        evidence_ids=atom.evidence_ids,
        source_text=atom_raw_text(atom.payload),
        structure_node_ids=structure.ancestry(node_by_page.get(page_id, structure.root_node_id)),
        review_reason=atom.review_reason,
        technical_atom_kind=atom.technical_atom_kind,
        technical_atom_id=atom.technical_atom_id,
    )


def _claim_kind(claim: SourceClaim) -> str:
    if "definition" in claim.claim_role_tags:
        return "concept"
    if "temporal" in claim.claim_role_tags or "provenance" in claim.claim_role_tags:
        return "event"
    return "claim"


def _claim_status(
    claim: SourceClaim, complete: bool, evidence_ids: tuple[str, ...]
) -> tuple[str, ReviewReason | None]:
    if claim.claim_eligibility != "eligible":
        return "needs-review", ReviewReason(
            "ineligible-source-claim", claim.claim_eligibility, evidence_ids
        )
    if not evidence_ids:
        return "needs-review", ReviewReason("missing-evidence", "no evidence id", ())
    if not complete:
        return "needs-review", ReviewReason(
            "fragmentary", "no subject/predicate/object region recovered", evidence_ids
        )
    return "usable", None


def _claim_confidence(claim: SourceClaim) -> str:
    if claim.claim_certainty == "supported" and claim.claim_salience >= 0.4:
        return "high"
    if claim.claim_certainty in {"supported", "qualified"}:
        return "medium"
    return "low"


def _atom_review_reason(support_status: str, evidence_ids: tuple[str, ...]) -> ReviewReason | None:
    if support_status == "supported":
        return None
    return ReviewReason("technical-atom-support", support_status, evidence_ids)


def _evidence_by_claim(
    records: tuple[EvidenceRecord, ...],
) -> dict[str, tuple[EvidenceRecord, ...]]:
    grouped: dict[str, list[EvidenceRecord]] = {}
    for record in records:
        if record.source_claim_id:
            grouped.setdefault(record.source_claim_id, []).append(record)
    return {claim_id: tuple(items) for claim_id, items in grouped.items()}


def _atom_source_hash(
    evidence_records: dict[str, EvidenceRecord],
    evidence_ids: tuple[str, ...],
    fallback: str,
) -> str:
    for evidence_id in evidence_ids:
        record = evidence_records.get(evidence_id)
        if record is not None and record.source_hash:
            return record.source_hash
    return fallback
