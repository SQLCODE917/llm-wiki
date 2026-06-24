"""JSON persistence for TechnicalAtomCatalog artifacts."""

from __future__ import annotations

import json

from llmwiki.domain.technical_atom_detection import SupportStatus, TechnicalAtomKind
from llmwiki.domain.technical_atoms import TechnicalAtom, TechnicalAtomCatalog
from llmwiki.domain.technical_tables import TechnicalTable, TechnicalTableBlock


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
        "technical_tables": [
            {
                "technical_table_id": table.technical_table_id,
                "source_locator": table.source_locator,
                "page_id": table.page_id,
                "title": table.title,
                "blocks": [
                    {
                        "technical_table_block_id": block.technical_table_block_id,
                        "block_index": block.block_index,
                        "source_citation": block.source_citation,
                        "page_range": list(block.page_range) if block.page_range else None,
                        "line_range": list(block.line_range) if block.line_range else None,
                        "markdown": block.markdown,
                        "row_count": block.row_count,
                        "column_count": block.column_count,
                    }
                    for block in table.blocks
                ],
                "source_claim_ids": list(table.source_claim_ids),
                "evidence_ids": list(table.evidence_ids),
            }
            for table in catalog.technical_tables
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
        technical_tables=tuple(
            _table_from_payload(item) for item in payload.get("technical_tables", ())
        ),
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
        "table",
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


def _table_from_payload(payload: object) -> TechnicalTable:
    if not isinstance(payload, dict):
        raise ValueError("TechnicalTable JSON item must be an object.")
    return TechnicalTable(
        technical_table_id=str(payload["technical_table_id"]),
        source_locator=str(payload["source_locator"]),
        page_id=str(payload["page_id"]),
        title=str(payload["title"]),
        blocks=tuple(_block_from_payload(item) for item in payload["blocks"]),
        source_claim_ids=tuple(str(item) for item in payload["source_claim_ids"]),
        evidence_ids=tuple(str(item) for item in payload["evidence_ids"]),
    )


def _block_from_payload(payload: object) -> TechnicalTableBlock:
    if not isinstance(payload, dict):
        raise ValueError("TechnicalTableBlock JSON item must be an object.")
    return TechnicalTableBlock(
        technical_table_block_id=str(payload["technical_table_block_id"]),
        block_index=int(payload["block_index"]),
        source_citation=str(payload["source_citation"]),
        page_range=_optional_range(payload.get("page_range")),
        line_range=_optional_range(payload.get("line_range")),
        markdown=str(payload["markdown"]),
        row_count=int(payload["row_count"]),
        column_count=int(payload["column_count"]),
    )


def _optional_range(value: object) -> tuple[int, int] | None:
    if value is None:
        return None
    if not isinstance(value, list | tuple) or len(value) != 2:
        raise ValueError("TechnicalTableBlock ranges must be pairs.")
    return (int(value[0]), int(value[1]))
