"""JSON persistence for TechnicalAtomCatalog artifacts."""

from __future__ import annotations

import json

from llmwiki.domain.technical_atom_detection import SupportStatus, TechnicalAtomKind
from llmwiki.domain.technical_atoms import TechnicalAtom, TechnicalAtomCatalog


def technical_atom_catalog_to_json(catalog: TechnicalAtomCatalog) -> str:
    payload = {
        "catalog_id": catalog.catalog_id,
        "source_locator": catalog.source_locator,
        "artifact_fingerprint": catalog.artifact_fingerprint,
        "technical_atoms": [
            {
                "technical_atom_id": atom.technical_atom_id,
                "source_locator": atom.source_locator,
                "page_id": atom.page_id,
                "atom_kind": atom.atom_kind,
                "title": atom.title,
                "technical_payload": atom.technical_payload,
                "normalized_fields": list(atom.normalized_fields),
                "source_claim_ids": list(atom.source_claim_ids),
                "evidence_ids": list(atom.evidence_ids),
                "source_range_id": atom.source_range_id,
                "support_status": atom.support_status,
            }
            for atom in catalog.technical_atoms
        ],
    }
    return json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def technical_atom_catalog_from_json(text: str) -> TechnicalAtomCatalog:
    payload = json.loads(text)
    return TechnicalAtomCatalog(
        catalog_id=str(payload["catalog_id"]),
        source_locator=str(payload["source_locator"]),
        artifact_fingerprint=str(payload["artifact_fingerprint"]),
        technical_atoms=tuple(_atom_from_payload(item) for item in payload["technical_atoms"]),
    )


def _atom_from_payload(payload: object) -> TechnicalAtom:
    if not isinstance(payload, dict):
        raise ValueError("TechnicalAtom JSON item must be an object.")
    fields = payload.get("normalized_fields", ())
    return TechnicalAtom(
        technical_atom_id=str(payload["technical_atom_id"]),
        source_locator=str(payload["source_locator"]),
        page_id=str(payload["page_id"]),
        atom_kind=_atom_kind(str(payload["atom_kind"])),
        title=str(payload["title"]),
        technical_payload=str(payload["technical_payload"]),
        normalized_fields=_normalized_fields(fields),
        source_claim_ids=tuple(str(item) for item in payload["source_claim_ids"]),
        evidence_ids=tuple(str(item) for item in payload["evidence_ids"]),
        source_range_id=str(payload["source_range_id"]),
        support_status=_support_status(str(payload.get("support_status", "supported"))),
    )


def _atom_kind(value: str) -> TechnicalAtomKind:
    if value not in {
        "code",
        "formula",
        "procedure",
        "table-row",
        "requirement",
        "exception",
        "worked-example",
    }:
        raise ValueError(f"Unknown TechnicalAtomKind: {value!r}.")
    return value  # type: ignore[return-value]


def _normalized_fields(value: object) -> tuple[tuple[str, str], ...]:
    if isinstance(value, dict):
        return tuple((str(key), str(item)) for key, item in value.items())
    if not isinstance(value, list):
        raise ValueError("TechnicalAtom normalized_fields must be a list or object.")
    fields: list[tuple[str, str]] = []
    for item in value:
        if not isinstance(item, list | tuple) or len(item) != 2:
            raise ValueError("TechnicalAtom normalized_fields entries must be pairs.")
        fields.append((str(item[0]), str(item[1])))
    return tuple(fields)


def _support_status(value: str) -> SupportStatus:
    if value not in {"supported", "too_broad", "not_supported", "unclear"}:
        raise ValueError(f"Unknown support_status: {value!r}.")
    return value  # type: ignore[return-value]
