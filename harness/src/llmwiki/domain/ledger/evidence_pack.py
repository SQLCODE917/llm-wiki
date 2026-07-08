"""Evidence packs for source-backed article writing."""

from __future__ import annotations

from dataclasses import dataclass, replace

from llmwiki.domain.ledger.canonical import artifact_fingerprint, deterministic_id
from llmwiki.domain.ledger.page_publication import PageCandidate, PagePublicationPlan
from llmwiki.domain.source_map import NormalizedSourceMap, SourceAnchor, SourceBlock
from llmwiki.domain.typed_evidence import EvidenceRecordSet, TypedEvidenceRecord

_PREFERRED_PACK_ITEMS = 12
_HARD_PACK_ITEMS = 16
_MIN_PACK_ITEMS = 4


@dataclass(frozen=True)
class SupportRef:
    support_kind: str
    support_id: str

    @property
    def code(self) -> str:
        return f"{self.support_kind}:{self.support_id}"


@dataclass(frozen=True)
class EvidencePackItem:
    support_ref: SupportRef
    typed_evidence_record_id: str
    evidence_record_type: str
    source_anchors: tuple[SourceAnchor, ...]
    source_block_ids: tuple[str, ...]
    source_text: str
    payload_text: str
    citation_label: str
    section_path: str


@dataclass(frozen=True)
class EvidencePackCoverage:
    page_id: str
    page_family: str
    page_purpose: str
    support_ref: SupportRef
    coverage_kind: str
    coverage_status: str


@dataclass(frozen=True)
class EvidencePackFinding:
    severity: str
    finding_code: str
    page_id: str
    message: str
    support_ref: str = ""


@dataclass(frozen=True)
class EvidencePack:
    page_id: str
    source_id: str
    source_hash: str
    source_profile_kind: str
    page_kind: str
    page_family: str
    title: str
    items: tuple[EvidencePackItem, ...]
    coverage: tuple[EvidencePackCoverage, ...]
    findings: tuple[EvidencePackFinding, ...] = ()

    @property
    def support_ref_codes(self) -> frozenset[str]:
        return frozenset(item.support_ref.code for item in self.items)


@dataclass(frozen=True)
class EvidencePackSet:
    evidence_pack_set_id: str
    evidence_pack_set_fingerprint: str
    source_id: str
    source_hash: str
    source_profile_kind: str
    packs: tuple[EvidencePack, ...]
    findings: tuple[EvidencePackFinding, ...]

    @property
    def valid_page_ids(self) -> tuple[str, ...]:
        return tuple(pack.page_id for pack in self.packs)

    @property
    def missing_pack_count(self) -> int:
        packed = {pack.page_id for pack in self.packs}
        return len({finding.page_id for finding in self.findings if finding.page_id not in packed})


def typed_evidence_support_ref(record_id: str) -> SupportRef:
    return SupportRef("typed-evidence-record", record_id)


def build_evidence_pack_set(
    *,
    publication_plan: PagePublicationPlan,
    evidence_record_set: EvidenceRecordSet | None,
    source_map: NormalizedSourceMap | None,
) -> EvidencePackSet:
    findings: list[EvidencePackFinding] = []
    packs: list[EvidencePack] = []
    for candidate in sorted(
        publication_plan.accepted_candidates,
        key=lambda item: (-item.rank_score, item.source_order, item.page_id),
    ):
        if source_map is None:
            findings.append(_finding(candidate, "source-map-missing", "source map is missing"))
            continue
        if evidence_record_set is None:
            findings.append(
                _finding(candidate, "evidence-record-set-missing", "typed evidence is missing")
            )
            continue
        pack = _pack_for_candidate(candidate, evidence_record_set, source_map)
        findings.extend(pack.findings)
        if pack.items:
            packs.append(pack)
        else:
            findings.append(
                _finding(
                    candidate,
                    "no-valid-evidence-pack-items",
                    "candidate has no valid support",
                )
            )
    draft = EvidencePackSet(
        evidence_pack_set_id=deterministic_id(
            "evidence-pack-set", publication_plan.source_hash, publication_plan.source_id
        ),
        evidence_pack_set_fingerprint="",
        source_id=publication_plan.source_id,
        source_hash=publication_plan.source_hash,
        source_profile_kind=publication_plan.source_profile_kind,
        packs=tuple(packs),
        findings=tuple(findings),
    )
    fingerprint = artifact_fingerprint(draft, exclude=("evidence_pack_set_fingerprint",))
    return replace(draft, evidence_pack_set_fingerprint=fingerprint)


def empty_evidence_pack_set(
    *, source_id: str, source_hash: str, source_profile_kind: str
) -> EvidencePackSet:
    draft = EvidencePackSet(
        evidence_pack_set_id=deterministic_id("evidence-pack-set", source_hash, source_id),
        evidence_pack_set_fingerprint="",
        source_id=source_id,
        source_hash=source_hash,
        source_profile_kind=source_profile_kind,
        packs=(),
        findings=(),
    )
    fingerprint = artifact_fingerprint(draft, exclude=("evidence_pack_set_fingerprint",))
    return replace(draft, evidence_pack_set_fingerprint=fingerprint)


def validate_support_refs(
    pack: EvidencePack, support_refs: tuple[SupportRef, ...]
) -> tuple[EvidencePackFinding, ...]:
    selected = pack.support_ref_codes
    return tuple(
        EvidencePackFinding(
            severity="blocker",
            finding_code="unknown-support-ref",
            page_id=pack.page_id,
            support_ref=ref.code,
            message="article claim references support outside the evidence pack",
        )
        for ref in support_refs
        if ref.code not in selected
    )


def _pack_for_candidate(
    candidate: PageCandidate,
    evidence_record_set: EvidenceRecordSet,
    source_map: NormalizedSourceMap,
) -> EvidencePack:
    record_by_id = {
        record.typed_evidence_record_id: record for record in evidence_record_set.records
    }
    block_by_id = source_map.source_blocks_by_id
    items: list[EvidencePackItem] = []
    findings: list[EvidencePackFinding] = []
    for record_id in candidate.supporting_evidence_record_ids:
        record = record_by_id.get(record_id)
        support_ref = typed_evidence_support_ref(record_id)
        if record is None:
            findings.append(
                _finding(candidate, "unknown-support-ref", "support ref is unknown", support_ref)
            )
            continue
        if record.status != "accepted":
            findings.append(
                _finding(
                    candidate,
                    "typed-evidence-not-accepted",
                    "typed evidence is not accepted",
                    support_ref,
                )
            )
            continue
        item = _item_for_record(record, block_by_id)
        if not item.source_text.strip() and not item.payload_text.strip():
            findings.append(
                _finding(
                    candidate,
                    "missing-support-text",
                    "support has no full source text or payload",
                    support_ref,
                )
            )
            continue
        items.append(item)
    shaped_items, shape_findings = _shape_pack_items(candidate, tuple(items))
    findings.extend(shape_findings)
    coverage = tuple(
        EvidencePackCoverage(
            page_id=candidate.page_id,
            page_family=candidate.page_family,
            page_purpose=candidate.page_family,
            support_ref=item.support_ref,
            coverage_kind="page-purpose-support",
            coverage_status="covered",
        )
        for item in shaped_items
    )
    return EvidencePack(
        page_id=candidate.page_id,
        source_id=candidate.source_id,
        source_hash=candidate.source_hash,
        source_profile_kind=candidate.source_profile_kind,
        page_kind=candidate.page_kind,
        page_family=candidate.page_family,
        title=candidate.title,
        items=shaped_items,
        coverage=coverage,
        findings=tuple(findings),
    )


def _item_for_record(
    record: TypedEvidenceRecord, block_by_id: dict[str, SourceBlock]
) -> EvidencePackItem:
    blocks = tuple(
        sorted(
            (block for block_id in record.source_block_ids if (block := block_by_id.get(block_id))),
            key=lambda item: item.source_order,
        )
    )
    source_text = "\n\n".join(
        block.source_text.strip() for block in blocks if block.source_text.strip()
    )
    section_path = next((block.section_path for block in blocks if block.section_path), "")
    return EvidencePackItem(
        support_ref=typed_evidence_support_ref(record.typed_evidence_record_id),
        typed_evidence_record_id=record.typed_evidence_record_id,
        evidence_record_type=record.evidence_record_type,
        source_anchors=record.source_anchors,
        source_block_ids=record.source_block_ids,
        source_text=source_text,
        payload_text=record.payload_text,
        citation_label=_citation_label(record, blocks),
        section_path=section_path,
    )


def _shape_pack_items(
    candidate: PageCandidate, items: tuple[EvidencePackItem, ...]
) -> tuple[tuple[EvidencePackItem, ...], tuple[EvidencePackFinding, ...]]:
    unique = _dedupe_items(items)
    if not unique:
        return (), ()
    if candidate.page_family == "recipe-pattern":
        selected, unbalanced = _shape_recipe_items(unique)
    elif candidate.page_family == "procedure-guide":
        selected, unbalanced = _shape_procedure_items(unique)
    elif candidate.page_family == "topic-concept":
        selected, unbalanced = _shape_topic_items(unique)
    else:
        selected, unbalanced = (unique[:_PREFERRED_PACK_ITEMS], False)
    selected = selected[:_HARD_PACK_ITEMS]
    findings: list[EvidencePackFinding] = []
    if len(unique) > len(selected):
        findings.append(
            _finding(
                candidate,
                "evidence-pack-trimmed",
                f"evidence pack trimmed from {len(unique)} to {len(selected)} item(s)",
                severity="warning",
            )
        )
    if unbalanced:
        findings.append(
            _finding(
                candidate,
                "evidence-pack-unbalanced",
                "evidence pack is missing expected record-type balance for its page family",
                severity="warning",
            )
        )
    if 0 < len(selected) < _MIN_PACK_ITEMS:
        findings.append(
            _finding(
                candidate,
                "evidence-pack-under-supported",
                f"evidence pack has {len(selected)} item(s); {_MIN_PACK_ITEMS} preferred",
                severity="warning",
            )
        )
    return selected, tuple(findings)


def _shape_recipe_items(
    items: tuple[EvidencePackItem, ...],
) -> tuple[tuple[EvidencePackItem, ...], bool]:
    code = _items_of_type(items, {"code_example"})
    context = _items_of_type(items, {"argument", "definition", "procedure_step"})
    selected = (*code[:4], *context[: _PREFERRED_PACK_ITEMS - min(len(code), 4)])
    return _ordered_unique(selected), not code or not context


def _shape_procedure_items(
    items: tuple[EvidencePackItem, ...],
) -> tuple[tuple[EvidencePackItem, ...], bool]:
    steps = _items_of_type(items, {"procedure_step"})
    closure = _items_of_type(items, {"rule", "formula", "table_fact"})
    context = _items_of_type(items, {"definition", "entity_fact"})
    selected = (*steps[:8], *closure[:4], *context[:2])
    return _ordered_unique(selected[:_PREFERRED_PACK_ITEMS]), not steps or not closure


def _shape_topic_items(
    items: tuple[EvidencePackItem, ...],
) -> tuple[tuple[EvidencePackItem, ...], bool]:
    definitions = _items_of_type(items, {"definition"})
    support = _items_of_type(items, {"rule", "code_example", "table_fact", "formula"})
    context = _items_of_type(items, {"argument", "entity_fact"})
    selected = (*definitions[:3], *support[:6], *context[:5])
    return _ordered_unique(selected[:_PREFERRED_PACK_ITEMS]), not (definitions or support)


def _items_of_type(
    items: tuple[EvidencePackItem, ...], record_types: set[str]
) -> tuple[EvidencePackItem, ...]:
    return tuple(item for item in items if item.evidence_record_type in record_types)


def _ordered_unique(items: tuple[EvidencePackItem, ...]) -> tuple[EvidencePackItem, ...]:
    return tuple(dict.fromkeys(items))


def _dedupe_items(items: tuple[EvidencePackItem, ...]) -> tuple[EvidencePackItem, ...]:
    seen: set[str] = set()
    unique: list[EvidencePackItem] = []
    for item in items:
        key = " ".join((item.payload_text or item.source_text).casefold().split())[:160]
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return tuple(unique)


def _citation_label(record: TypedEvidenceRecord, blocks: tuple[SourceBlock, ...]) -> str:
    anchors = record.source_anchors
    if anchors:
        start = min(anchor.page_span[0] for anchor in anchors)
        end = max(anchor.page_span[1] for anchor in anchors)
        page_label = f"p. {start}" if start == end else f"pp. {start}-{end}"
        return f"raw/{record.source_locator} ({page_label})"
    if blocks:
        block_ids = ", ".join(block.source_block_id for block in blocks)
        return f"raw/{record.source_locator} ({block_ids})"
    return f"raw/{record.source_locator}"


def _finding(
    candidate: PageCandidate,
    code: str,
    message: str,
    support_ref: SupportRef | None = None,
    *,
    severity: str = "blocker",
) -> EvidencePackFinding:
    return EvidencePackFinding(
        severity=severity,
        finding_code=code,
        page_id=candidate.page_id,
        support_ref=support_ref.code if support_ref is not None else "",
        message=message,
    )
