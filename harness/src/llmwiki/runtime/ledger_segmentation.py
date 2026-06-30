"""Segment ingest chunks into source segments for the claim ledger.

Chunks (page-range markdown) are split into finer segments — headings, fenced
code blocks, tabular blocks, lists, and paragraphs — by reusable structural
signals only. Each segment is profiled and (for prose) gets claim records from
the shared claim classifier, so the ledger's ExtractedUnits are fine enough for
one disposition each and for code/table blocks to become their own atoms.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.evidence_locator_index import EvidenceIdentity
from llmwiki.domain.ledger.builder import SegmentInput
from llmwiki.domain.ledger.extraction import ExtractedUnitProfile
from llmwiki.domain.ledger.features import profile_unit
from llmwiki.domain.ledger.segments import SegmentClaim, SourceSegment
from llmwiki.domain.objects import Schema
from llmwiki.domain.planning import derive_segment_claims
from llmwiki.domain.prose_flow import merge_prose_blocks
from llmwiki.domain.source_summary import SourceClaim

_HEADING = re.compile(r"^\s{0,3}#{1,6}\s")
_FENCE = re.compile(r"^\s*(```|~~~)")
_ENUMERATED = re.compile(r"^\s*(?:[-*]\s*)?\d+[.)\s]")
_LIST = re.compile(r"^\s*[-*]\s")
_PIPE = re.compile(r"\|.*\|")
_PROSE_KINDS = ("paragraph", "list")
_MAX_ANALYSIS_TEXT_CHARS = 80_000


@dataclass(frozen=True)
class ChunkText:
    unit_id: str
    page_locator: str
    heading_path: str
    text: str


def segment_chunks(
    chunks: tuple[ChunkText, ...],
    *,
    source_locator: str,
    source_hash: str,
    schema: Schema,
) -> tuple[tuple[SegmentInput, ...], dict[str, ExtractedUnitProfile]]:
    inputs: list[SegmentInput] = []
    profiles: dict[str, ExtractedUnitProfile] = {}
    order = 0
    for chunk in chunks:
        for kind, text in _blocks(chunk.text):
            order += 1
            range_id = f"source-range-{source_hash[:8]}-{order:05d}"
            analysis_text = _analysis_text(text)
            evidence_id = EvidenceIdentity.from_excerpt(
                source_locator, source_hash, chunk.page_locator, analysis_text
            ).evidence_id
            segment = SourceSegment(
                segment_id=f"segment-{order:05d}",
                source_range_id=range_id,
                source_locator=source_locator,
                source_hash=source_hash,
                heading_path=chunk.heading_path,
                structure_node_id="",
                source_order=order,
                text=text,
                segment_kind=kind,
                evidence_ids=(evidence_id,),
            )
            claims = _claims(kind, analysis_text, (evidence_id,), schema)
            inputs.append(SegmentInput(segment=segment, claims=claims))
            profiles[segment.segment_id] = profile_unit(
                extracted_unit_id=segment.segment_id,
                source_range_id=range_id,
                text=analysis_text,
                evidence_ids=(evidence_id,),
            )
    return tuple(inputs), profiles


def segment_page_plan_claim_chunks(
    chunks: tuple[ChunkText, ...],
    source_claims: tuple[SourceClaim, ...],
    *,
    source_locator: str,
    source_hash: str,
) -> tuple[tuple[SegmentInput, ...], dict[str, ExtractedUnitProfile]]:
    claims_by_unit: dict[str, list[SourceClaim]] = {}
    for claim in source_claims:
        claims_by_unit.setdefault(claim.extracted_unit_id, []).append(claim)
    inputs: list[SegmentInput] = []
    profiles: dict[str, ExtractedUnitProfile] = {}
    for order, chunk in enumerate(chunks, start=1):
        range_id = f"source-range-{source_hash[:8]}-{order:05d}"
        analysis_text = _analysis_text(chunk.text)
        evidence_id = EvidenceIdentity.from_excerpt(
            source_locator, source_hash, chunk.page_locator, analysis_text
        ).evidence_id
        segment = SourceSegment(
            segment_id=f"segment-{order:05d}",
            source_range_id=range_id,
            source_locator=source_locator,
            source_hash=source_hash,
            heading_path=chunk.heading_path,
            structure_node_id="",
            source_order=order,
            text=chunk.text,
            segment_kind="paragraph",
            evidence_ids=(evidence_id,),
        )
        segment_claims: list[SegmentClaim] = []
        for claim in claims_by_unit.get(chunk.unit_id, ()):
            segment_claims.append(
                SegmentClaim(
                    claim_id=claim.source_claim_id,
                    statement=claim.statement,
                    role_tags=claim.claim_role_tags,
                    eligibility=claim.claim_eligibility,
                    certainty=claim.claim_certainty,
                    evidence_ids=(evidence_id,),
                )
            )
        inputs.append(SegmentInput(segment=segment, claims=tuple(segment_claims)))
        profiles[segment.segment_id] = profile_unit(
            extracted_unit_id=segment.segment_id,
            source_range_id=range_id,
            text=analysis_text,
            evidence_ids=(evidence_id,),
        )
    return tuple(inputs), profiles


def _analysis_text(text: str) -> str:
    return text[:_MAX_ANALYSIS_TEXT_CHARS]


def _claims(
    kind: str, text: str, evidence_ids: tuple[str, ...], schema: Schema
) -> tuple[SegmentClaim, ...]:
    if kind not in _PROSE_KINDS:
        return ()
    records = derive_segment_claims(text, schema)
    return tuple(
        SegmentClaim(
            claim_id=f"segment-claim-{index:03d}-{evidence_ids[0]}",
            statement=record.statement,
            role_tags=record.role_tags,
            eligibility=record.eligibility,
            certainty=record.certainty,
            evidence_ids=evidence_ids,
        )
        for index, record in enumerate(records, start=1)
    )


def _blocks(text: str) -> list[tuple[str, str]]:
    lines = text.split("\n")
    blocks: list[tuple[str, str]] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if _HEADING.match(line):
            blocks.append(("heading", re.sub(r"[ \t]+", " ", line).strip()))
            index += 1
        elif _FENCE.match(line):
            index = _consume_fence(lines, index, blocks)
        elif not line.strip():
            index += 1
        else:
            index = _consume_paragraph(lines, index, blocks)
    return list(merge_prose_blocks(blocks, prose_kinds=("paragraph",)))


def _consume_fence(lines: list[str], start: int, blocks: list[tuple[str, str]]) -> int:
    index = start + 1
    while index < len(lines) and not _FENCE.match(lines[index]):
        index += 1
    end = min(index, len(lines) - 1)
    block = "\n".join(lines[start : end + 1])
    blocks.append(("code-fence", block))
    return index + 1


def _consume_paragraph(lines: list[str], start: int, blocks: list[tuple[str, str]]) -> int:
    index = start
    collected: list[str] = []
    while index < len(lines):
        line = lines[index]
        if not line.strip() or _HEADING.match(line) or _FENCE.match(line):
            break
        collected.append(line)
        index += 1
    kind = _classify(collected)
    if kind in _PROSE_KINDS:
        # Tabs are layout whitespace in this extractor; collapse them so prose
        # reads as sentences. Tables/code keep their raw text for fidelity.
        block = "\n".join(_collapse_layout_spaces(line).strip() for line in collected)
    else:
        block = "\n".join(collected)
    blocks.append((kind, block))
    return index


def _collapse_layout_spaces(line: str) -> str:
    chars: list[str] = []
    previous_layout_space = False
    for char in line:
        if char in {" ", "\t"}:
            if not previous_layout_space:
                chars.append(" ")
            previous_layout_space = True
            continue
        chars.append(char)
        previous_layout_space = False
    return "".join(chars)


def _classify(lines: list[str]) -> str:
    if not lines:
        return "paragraph"
    tabular = sum(1 for line in lines if _PIPE.search(line) or _ENUMERATED.match(line))
    if tabular >= max(2, len(lines) // 2):
        return "table-block"
    if sum(1 for line in lines if _LIST.match(line)) >= max(2, len(lines) // 2):
        return "list"
    return "paragraph"
