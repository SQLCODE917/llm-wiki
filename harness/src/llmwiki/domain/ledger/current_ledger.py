"""Build a ClaimLedger aggregate from current ingest artifacts."""

from __future__ import annotations

from collections import Counter

from llmwiki.domain.evidence_registry import EvidenceRegistry
from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.current_entry_mapping import (
    build_current_atom_entries,
    build_current_claim_entries,
    ordered_entries,
)
from llmwiki.domain.ledger.current_structure import node_by_page, source_range_by_unit
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.profiles import assign_family, build_source_profile
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.objects import PagePlan
from llmwiki.domain.technical_atoms import TechnicalAtomCatalog


def build_current_claim_ledger(
    *,
    source_locator: str,
    source_hash: str,
    page_plan: PagePlan,
    evidence_registry: EvidenceRegistry,
    document_structure: DocumentStructure,
    technical_atom_catalog: TechnicalAtomCatalog,
) -> ClaimLedger:
    ranges_by_unit = source_range_by_unit(page_plan, evidence_registry.source_ranges)
    nodes_by_page = node_by_page(document_structure)
    claim_entries, claim_statements = build_current_claim_entries(
        page_plan=page_plan,
        evidence_registry=evidence_registry,
        structure=document_structure,
        range_by_unit=ranges_by_unit,
        node_by_page=nodes_by_page,
    )
    atoms, atom_entries, atom_statements = build_current_atom_entries(
        source_locator=source_locator,
        source_hash=source_hash,
        evidence_registry=evidence_registry,
        structure=document_structure,
        node_by_page=nodes_by_page,
        catalog=technical_atom_catalog,
    )
    entries = ordered_entries((*claim_entries, *atom_entries), evidence_registry.source_ranges)
    profile = build_source_profile(
        source_locator=source_locator,
        unit_count=len(page_plan.extracted_units),
        entries=entries,
        atom_kind_counts=dict(Counter(atom.technical_atom_kind for atom in atoms)),
        feature_means={},
    )
    return ClaimLedger(
        claim_ledger_id=deterministic_id("claim-ledger", source_hash),
        source_locator=source_locator,
        source_hash=source_hash,
        evidence_registry_hash=evidence_registry.registry_id,
        source_profile=profile,
        source_family_assignment=assign_family(profile),
        entries=entries,
        technical_atoms=atoms,
        source_statements=(*claim_statements, *atom_statements),
        extractor_decisions=(),
        rejected_candidates=(),
    )
