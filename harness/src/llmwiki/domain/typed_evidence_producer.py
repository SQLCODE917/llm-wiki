"""Typed evidence producers for normalized source maps."""

from __future__ import annotations

import re
from typing import Protocol

from llmwiki.domain.source_claim_sentences import claim_sentences
from llmwiki.domain.source_map import NormalizedSourceMap, SourceBlock
from llmwiki.domain.source_profiles import EvidenceExtractionPlan, SourceProfileArtifact
from llmwiki.domain.technical_atom_detection import (
    fenced_code_blocks,
    is_formula,
    ordered_step_groups,
)
from llmwiki.domain.typed_evidence import (
    EvidenceRecordSet,
    StructuredEvidencePayload,
    TypedEvidenceRecord,
    evidence_record_set,
    stable_id,
    validate_typed_evidence_record,
)

_DEONTIC_RE = re.compile(
    r"\b(?:must|shall|should|may|can(?:not)?|can't|cannot|always|never|if|unless|when)\b",
    re.IGNORECASE,
)
_DEFINITION_RE = re.compile(
    r"\b(?:is|are|means|refers to|is called|are called|is defined as)\b",
    re.IGNORECASE,
)
_ORDERED_LINE_RE = re.compile(r"^\s*(?:\d+[.)]|[-*])\s+(?P<step>\S.+)")
_TABLE_ROW_RE = re.compile(r"\S+\s+\|\s+\S+")


class TypedEvidenceProducer(Protocol):
    def build_record_set(
        self,
        source_map: NormalizedSourceMap,
        source_profile_artifact: SourceProfileArtifact,
        plan: EvidenceExtractionPlan,
    ) -> EvidenceRecordSet:
        """Build typed source evidence from a normalized source map."""


class DeterministicTypedEvidenceProducer:
    """Conservative source-map extractor used before model-backed evidence."""

    def build_record_set(
        self,
        source_map: NormalizedSourceMap,
        source_profile_artifact: SourceProfileArtifact,
        plan: EvidenceExtractionPlan,
    ) -> EvidenceRecordSet:
        records: list[TypedEvidenceRecord] = []
        selected = set(plan.source_block_ids)
        allowed = {str(item) for item in plan.allowed_record_types}
        profile_id = source_profile_artifact.source_profile.profile_id
        for block in sorted(source_map.source_blocks, key=lambda item: item.source_order):
            if block.source_block_id not in selected:
                continue
            for record in _records_for_block(source_map, block, allowed, profile_id):
                records.append(validate_typed_evidence_record(record, plan))
        return evidence_record_set(
            source_id=source_map.source_id,
            source_locator=source_map.source_locator,
            source_hash=source_map.source_hash,
            source_profile_id=source_profile_artifact.source_profile.source_profile_id,
            evidence_extraction_plan_id=plan.evidence_extraction_plan_id,
            records=tuple(records),
        )


def _records_for_block(
    source_map: NormalizedSourceMap,
    block: SourceBlock,
    allowed: set[str],
    profile_id: str,
) -> tuple[TypedEvidenceRecord, ...]:
    if block.block_type == "heading":
        return ()
    text = block.source_text.strip()
    if not text:
        return ()
    if block.block_type == "code":
        return _single_record(source_map, block, allowed, "code_example", text, "code")
    if block.block_type == "table":
        return _single_record(source_map, block, allowed, "table_fact", text, "table")
    records: list[TypedEvidenceRecord] = []
    for step in _procedure_steps(text):
        records.extend(_single_record(source_map, block, allowed, "procedure_step", step, "text"))
    for statement in claim_sentences(text):
        record_type = _record_type_for_statement(statement, profile_id, allowed)
        if record_type is None:
            continue
        records.extend(_single_record(source_map, block, allowed, record_type, statement, "text"))
    return tuple(records)


def _single_record(
    source_map: NormalizedSourceMap,
    block: SourceBlock,
    allowed: set[str],
    record_type: str,
    text: str,
    payload_kind: str,
) -> tuple[TypedEvidenceRecord, ...]:
    if record_type not in allowed:
        return ()
    payload_text = _payload_text(record_type, text)
    canonical_text = _canonical_text(record_type, payload_text)
    identity_text = f"{block.source_block_id}|{record_type}|{payload_text}"
    return (
        TypedEvidenceRecord(
            typed_evidence_record_id=stable_id(
                "typed-evidence-record",
                source_map.source_hash,
                identity_text,
            ),
            source_id=source_map.source_id,
            source_locator=source_map.source_locator,
            source_hash=source_map.source_hash,
            evidence_record_type=record_type,
            status="accepted",
            canonical_text=canonical_text,
            structured_payload=StructuredEvidencePayload(
                payload_kind=payload_kind,
                payload_text=payload_text,
                normalized_fields=_normalized_fields(record_type, payload_text),
            ),
            source_anchors=(block.source_anchor,),
            source_block_ids=(block.source_block_id,),
            confidence=block.confidence,
        ),
    )


def _payload_text(record_type: str, text: str) -> str:
    if record_type != "code_example":
        return text.strip()
    blocks = fenced_code_blocks(text)
    if blocks:
        return blocks[0][1]
    return text.strip().strip("`").strip()


def _canonical_text(record_type: str, payload_text: str) -> str:
    if record_type == "code_example":
        return f"Code example: {_single_line(payload_text)}"
    if record_type == "table_fact":
        return f"Table fact: {_single_line(payload_text)}"
    return payload_text.strip()


def _record_type_for_statement(
    statement: str,
    profile_id: str,
    allowed: set[str],
) -> str | None:
    if "formula" in allowed and is_formula(statement):
        return "formula"
    if "table_fact" in allowed and _TABLE_ROW_RE.search(statement):
        return "table_fact"
    if "rule" in allowed and _DEONTIC_RE.search(statement):
        return "rule"
    if "definition" in allowed and _DEFINITION_RE.search(statement):
        return "definition"
    if profile_id == "programming-prose" and "argument" in allowed:
        return "argument"
    if "argument" in allowed and len(statement.split()) >= 7:
        return "argument"
    if "entity_fact" in allowed:
        return "entity_fact"
    return None


def _procedure_steps(text: str) -> tuple[str, ...]:
    grouped = ordered_step_groups(text)
    if grouped:
        return tuple(step for group in grouped for step in group)
    steps: list[str] = []
    for line in text.splitlines():
        match = _ORDERED_LINE_RE.match(line)
        if match is not None:
            steps.append(match.group("step").strip())
    return tuple(steps)


def _normalized_fields(record_type: str, payload_text: str) -> tuple[tuple[str, str], ...]:
    if record_type == "formula":
        return (("expression", payload_text),)
    if record_type == "code_example":
        return (("code", payload_text),)
    if record_type == "table_fact":
        return (("table_text", payload_text),)
    if record_type == "procedure_step":
        return (("step_text", payload_text),)
    return (("statement", payload_text),)


def _single_line(text: str) -> str:
    cleaned = " ".join(text.split())
    return cleaned if len(cleaned) <= 180 else f"{cleaned[:177].rstrip()}..."
