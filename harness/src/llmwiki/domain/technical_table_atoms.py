"""Build TechnicalTable records and their table TechnicalAtom."""

from __future__ import annotations

import hashlib

from llmwiki.domain.evidence_registry import EvidenceRecord, SourceRange
from llmwiki.domain.technical_atom_detection import (
    best_evidence_ids,
    bounded_payload,
    normalize_payload,
    title_for_payload,
)
from llmwiki.domain.technical_atom_evidence import (
    records_for_evidence_ids,
    selected_source_claim_ids,
)
from llmwiki.domain.technical_atoms import TechnicalAtom
from llmwiki.domain.technical_table_detection import DetectedTable, DetectedTableBlock
from llmwiki.domain.technical_tables import TechnicalTable, TechnicalTableBlock


def build_technical_table_atom(
    *,
    detected: DetectedTable,
    source_locator: str,
    page_id: str,
    source_range: SourceRange,
    records: tuple[EvidenceRecord, ...],
    seen: set[tuple[str, str, str]],
) -> tuple[TechnicalTable | None, TechnicalAtom | None]:
    evidence_ids = tuple(
        dict.fromkeys(
            evidence_id
            for block in detected.blocks
            for evidence_id in best_evidence_ids(records, block.markdown)
        )
    )
    if not evidence_ids:
        return None, None
    bounded = bounded_payload(detected.title)
    if bounded is None:
        return None, None
    key = (page_id, "table", normalize_payload(bounded))
    if key in seen:
        return None, None
    evidence_records = records_for_evidence_ids(records, evidence_ids)
    source_claim_ids = selected_source_claim_ids((), evidence_records)
    table_id = _table_id(page_id, detected)
    table = TechnicalTable(
        technical_table_id=table_id,
        source_locator=source_locator,
        page_id=page_id,
        title=detected.title,
        blocks=tuple(_table_block(table_id, block) for block in detected.blocks),
        source_claim_ids=source_claim_ids,
        evidence_ids=evidence_ids,
    )
    seen.add(key)
    atom_id = f"technical-atom-{_digest(':'.join((*key, *evidence_ids)))[:16]}"
    atom = TechnicalAtom(
        technical_atom_id=atom_id,
        source_locator=source_locator,
        page_id=page_id,
        atom_kind="table",
        title=title_for_payload("table", bounded),
        technical_payload=bounded,
        normalized_fields=(
            ("technical_table_id", table_id),
            ("source_citation", table.source_citation),
        ),
        source_claim_ids=source_claim_ids,
        evidence_ids=evidence_ids,
        source_range_id=source_range.source_range_id,
    )
    return table, atom


def _table_block(table_id: str, block: DetectedTableBlock) -> TechnicalTableBlock:
    return TechnicalTableBlock(
        technical_table_block_id=f"{table_id}-block-{block.block_index}",
        block_index=block.block_index,
        source_citation=block.source_citation,
        page_range=block.page_range,
        line_range=block.line_range,
        markdown=block.markdown,
        row_count=block.row_count,
        column_count=block.column_count,
    )


def _table_id(page_id: str, detected: DetectedTable) -> str:
    seed = page_id + detected.title + detected.blocks[0].markdown
    return f"technical-table-{_digest(seed)[:16]}"


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
