"""Claim-support candidates derived from TechnicalAtomCatalog records."""

from __future__ import annotations

import re
from collections.abc import Mapping, Sequence

from llmwiki.domain.claim_support import ClaimSupportCandidate
from llmwiki.domain.claim_support_evidence import ClaimSupportEvidenceIndex
from llmwiki.domain.claim_support_sampling import claim_support_risk_tags
from llmwiki.domain.technical_atoms import TechnicalAtomCatalog


def technical_atom_claim_support_candidates(
    page_texts: Mapping[str, str],
    catalogs: Sequence[TechnicalAtomCatalog],
    index: ClaimSupportEvidenceIndex,
    source_path: str,
) -> tuple[ClaimSupportCandidate, ...]:
    candidates: list[ClaimSupportCandidate] = []
    page_counts: dict[str, int] = {}
    for catalog in catalogs:
        if source_path and _source_path(catalog.source_locator) != source_path:
            continue
        for atom in catalog.technical_atoms:
            if atom.page_id not in page_texts:
                continue
            page_counts[atom.page_id] = page_counts.get(atom.page_id, 0) + 1
            claim_text = f"{atom.atom_kind}: {atom.technical_payload}"
            citation = atom.source_citation or f"raw/{atom.source_locator}"
            candidates.append(
                ClaimSupportCandidate(
                    candidate_id=(
                        f"claim-support-technical-atom-"
                        f"{_slug(atom.page_id)}-{page_counts[atom.page_id]}"
                    ),
                    page_id=atom.page_id,
                    claim_text=claim_text,
                    page_context=f"{claim_text} ({citation})",
                    citation_texts=(citation,),
                    source_claim_ids=atom.source_claim_ids,
                    evidence_ids=atom.evidence_ids,
                    evidence_excerpts=index.excerpts_for_claim(
                        atom.evidence_ids, atom.technical_payload, limit=5
                    ),
                    candidate_kind="technical-atom",
                    risk_tags=claim_support_risk_tags(claim_text),
                )
            )
    return tuple(candidates)


def _source_path(source_locator: str) -> str:
    return source_locator if source_locator.startswith("raw/") else f"raw/{source_locator}"


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "claim"
