"""Technical-atom matching helpers for topic projection."""

from __future__ import annotations

import re

from llmwiki.domain.ledger.atom_projection import atom_is_topic_projectable
from llmwiki.domain.ledger.atoms import TablePayload
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.table_identity import table_identity_names_by_atom_id
from llmwiki.domain.ledger.topic_terms import topic_field_matches


def atom_ids_matching_table_payload(
    ledger: ClaimLedger,
    matcher: re.Pattern[str],
    terms: tuple[str, ...],
    required_terms: tuple[str, ...] | None = None,
    structure: DocumentStructure | None = None,
) -> tuple[str, ...]:
    ids: list[str] = []
    names_by_atom = table_identity_names_by_atom_id(ledger, structure)
    for atom in ledger.technical_atoms:
        if not atom_is_topic_projectable(atom, ledger.source_profile):
            continue
        if not isinstance(atom.payload, TablePayload):
            continue
        searchable = "\n".join(
            (
                atom.payload.caption,
                *_first_lines(atom.payload.raw_table_text),
                *names_by_atom.get(atom.technical_atom_id, ()),
            )
        )
        if topic_field_matches(searchable, matcher, terms, required_terms):
            ids.append(atom.technical_atom_id)
    return tuple(dict.fromkeys(ids))


def _first_lines(text: str) -> tuple[str, ...]:
    return tuple(line for line in text.splitlines()[:3] if line.strip())
