"""Build rebuildable TechnicalAtomCatalog records from ingest artifacts."""

from __future__ import annotations

import hashlib
from collections import Counter

from llmwiki.domain.evidence_registry import EvidenceRecord, EvidenceRegistry, SourceRange
from llmwiki.domain.objects import ExtractedUnit, PagePlan, SourceClaim
from llmwiki.domain.technical_atom_detection import (
    MAX_RENDERED_ATOMS_PER_PAGE,
    TechnicalAtomKind,
    best_evidence_ids,
    bounded_payload,
    claim_kind,
    fenced_code_blocks,
    fields_for_claim,
    inline_fenced_code_blocks,
    is_formula,
    normalize_payload,
    ordered_step_groups,
    table_row,
    text_without_fenced_code,
    title_for_payload,
)
from llmwiki.domain.technical_atoms import TechnicalAtom, TechnicalAtomCatalog


def build_technical_atom_catalog(
    *,
    source_locator: str,
    page_plan: PagePlan,
    evidence_registry: EvidenceRegistry,
    artifact_fingerprint: str,
) -> TechnicalAtomCatalog:
    source_text = next(
        (text for text in evidence_registry.source_texts if text.source_locator == source_locator),
        None,
    )
    source_hash = source_text.source_hash if source_text is not None else ""
    builder = TechnicalAtomBuilder(page_plan, evidence_registry, source_locator)
    atoms = builder.build()
    seed = f"{source_locator}:{source_hash}:{artifact_fingerprint}:{len(atoms)}"
    return TechnicalAtomCatalog(
        catalog_id=f"technical-atom-catalog-{_digest(seed)[:16]}",
        source_locator=source_locator,
        artifact_fingerprint=artifact_fingerprint,
        technical_atoms=atoms,
    )


class TechnicalAtomBuilder:
    def __init__(
        self, page_plan: PagePlan, evidence_registry: EvidenceRegistry, source_locator: str
    ) -> None:
        self.page_plan = page_plan
        self.registry = evidence_registry
        self.source_locator = source_locator
        self.records_by_claim = _records_by_claim(evidence_registry.evidence_records)
        self.records_by_range = _records_by_range(evidence_registry.evidence_records)
        self.ranges_by_page = {
            source_range.page_id: source_range for source_range in evidence_registry.source_ranges
        }

    def build(self) -> tuple[TechnicalAtom, ...]:
        atoms: list[TechnicalAtom] = []
        seen: set[tuple[str, str, str]] = set()
        for unit, page_id, source_range in self._units():
            atoms.extend(self._structural_atoms(unit, page_id, source_range, seen))
        for claim in self.page_plan.source_claims:
            atoms.extend(self._claim_atoms(claim, seen))
        return tuple(_limit_atoms_per_page(atoms))

    def _units(self) -> tuple[tuple[ExtractedUnit, str, SourceRange], ...]:
        units_by_id = {unit.unit_id: unit for unit in self.page_plan.extracted_units}
        rows: list[tuple[ExtractedUnit, str, SourceRange]] = []
        for write in self.page_plan.planned_writes:
            source_range = self.ranges_by_page.get(write.page_metadata.page_id)
            if source_range is None:
                continue
            for unit_id in write.extracted_units:
                unit = units_by_id.get(unit_id)
                if unit is not None:
                    rows.append((unit, write.page_metadata.page_id, source_range))
        return tuple(rows)

    def _structural_atoms(
        self,
        unit: ExtractedUnit,
        page_id: str,
        source_range: SourceRange,
        seen: set[tuple[str, str, str]],
    ) -> tuple[TechnicalAtom, ...]:
        atoms: list[TechnicalAtom] = []
        for language, code in fenced_code_blocks(unit.text):
            atom = self._make_atom(
                "code", page_id, source_range, code, (("language", language),), seen
            )
            if atom is not None:
                atoms.append(atom)
        prose_text = text_without_fenced_code(unit.text)
        for line in prose_text.splitlines():
            atoms.extend(self._line_atoms(line, page_id, source_range, seen))
        for steps in ordered_step_groups(prose_text):
            payload = "\n".join(f"{index}. {step}" for index, step in enumerate(steps, 1))
            atom = self._make_atom(
                "procedure",
                page_id,
                source_range,
                payload,
                (("ordered_steps", payload),),
                seen,
            )
            if atom is not None:
                atoms.append(atom)
        return tuple(atoms)

    def _line_atoms(
        self,
        line: str,
        page_id: str,
        source_range: SourceRange,
        seen: set[tuple[str, str, str]],
    ) -> tuple[TechnicalAtom, ...]:
        atoms: list[TechnicalAtom] = []
        row = table_row(line)
        if row is not None:
            atom = self._make_atom(
                "table-row",
                page_id,
                source_range,
                line.strip(),
                (("cells", " | ".join(row)),),
                seen,
            )
            if atom is not None:
                atoms.append(atom)
        if is_formula(line):
            atom = self._make_atom(
                "formula",
                page_id,
                source_range,
                line.strip(),
                (("expression", line.strip()),),
                seen,
            )
            if atom is not None:
                atoms.append(atom)
        return tuple(atoms)

    def _claim_atoms(
        self, claim: SourceClaim, seen: set[tuple[str, str, str]]
    ) -> tuple[TechnicalAtom, ...]:
        records = self.records_by_claim.get(claim.source_claim_id, ())
        if not records:
            return ()
        source_range = self._range_for_record(records[0])
        if source_range is None:
            return ()
        kind = claim_kind(claim)
        if kind is None:
            return ()
        evidence_ids = tuple(record.evidence_id for record in records)
        if "```" in claim.statement and kind != "code":
            return ()
        if kind == "code":
            atoms = tuple(
                atom
                for language, payload in inline_fenced_code_blocks(claim.statement)
                if (
                    atom := self._make_atom(
                        "code",
                        source_range.page_id,
                        source_range,
                        payload,
                        (("language", language),),
                        seen,
                        source_claim_ids=(claim.source_claim_id,),
                        evidence_ids=evidence_ids,
                    )
                )
                is not None
            )
            if atoms or "```" in claim.statement:
                return atoms
        return _maybe_tuple(
            self._make_atom(
                kind,
                source_range.page_id,
                source_range,
                claim.statement,
                fields_for_claim(kind, claim.statement),
                seen,
                source_claim_ids=(claim.source_claim_id,),
                evidence_ids=evidence_ids,
            )
        )

    def _make_atom(
        self,
        atom_kind: TechnicalAtomKind,
        page_id: str,
        source_range: SourceRange,
        payload: str,
        fields: tuple[tuple[str, str], ...],
        seen: set[tuple[str, str, str]],
        *,
        source_claim_ids: tuple[str, ...] = (),
        evidence_ids: tuple[str, ...] = (),
    ) -> TechnicalAtom | None:
        bounded = bounded_payload(payload)
        if bounded is None:
            return None
        key = (page_id, atom_kind, normalize_payload(bounded))
        if key in seen:
            return None
        records = self.records_by_range.get(source_range.source_range_id, ())
        evidence_ids = evidence_ids or best_evidence_ids(records, bounded)
        if not evidence_ids:
            return None
        seen.add(key)
        atom_id = f"technical-atom-{_digest(':'.join((*key, *evidence_ids)))[:16]}"
        return TechnicalAtom(
            technical_atom_id=atom_id,
            source_locator=self.source_locator,
            page_id=page_id,
            atom_kind=atom_kind,
            title=title_for_payload(atom_kind, bounded),
            technical_payload=bounded,
            normalized_fields=(*fields, ("source_citation", _citation_for_range(source_range))),
            source_claim_ids=_source_claim_ids(source_claim_ids, records),
            evidence_ids=tuple(dict.fromkeys(evidence_ids)),
            source_range_id=source_range.source_range_id,
        )

    def _range_for_record(self, record: EvidenceRecord) -> SourceRange | None:
        return next(
            (
                source_range
                for source_range in self.registry.source_ranges
                if source_range.source_range_id == record.source_range_id
            ),
            None,
        )


def _source_claim_ids(
    source_claim_ids: tuple[str, ...], records: tuple[EvidenceRecord, ...]
) -> tuple[str, ...]:
    if source_claim_ids:
        return tuple(dict.fromkeys(source_claim_ids))
    return tuple(
        dict.fromkeys(record.source_claim_id for record in records if record.source_claim_id)
    )[:3]


def _maybe_tuple(atom: TechnicalAtom | None) -> tuple[TechnicalAtom, ...]:
    return () if atom is None else (atom,)


def _records_by_claim(
    records: tuple[EvidenceRecord, ...],
) -> dict[str, tuple[EvidenceRecord, ...]]:
    grouped: dict[str, list[EvidenceRecord]] = {}
    for record in records:
        if record.source_claim_id:
            grouped.setdefault(record.source_claim_id, []).append(record)
    return {claim_id: tuple(items) for claim_id, items in grouped.items()}


def _records_by_range(
    records: tuple[EvidenceRecord, ...],
) -> dict[str, tuple[EvidenceRecord, ...]]:
    grouped: dict[str, list[EvidenceRecord]] = {}
    for record in records:
        grouped.setdefault(record.source_range_id, []).append(record)
    return {range_id: tuple(items) for range_id, items in grouped.items()}


def _limit_atoms_per_page(atoms: list[TechnicalAtom]) -> tuple[TechnicalAtom, ...]:
    counts: Counter[str] = Counter()
    result: list[TechnicalAtom] = []
    for atom in atoms:
        if counts[atom.page_id] >= MAX_RENDERED_ATOMS_PER_PAGE:
            continue
        result.append(atom)
        counts[atom.page_id] += 1
    return tuple(result)


def _citation_for_range(source_range: SourceRange) -> str:
    source = source_range.source_path
    if source_range.page_range is not None:
        start, end = source_range.page_range
        suffix = f"p.{start}" if start == end else f"p.{start}-{end}"
        return f"{source} {suffix}"
    if source_range.line_range is not None:
        start, end = source_range.line_range
        suffix = f"normalized:L{start}" if start == end else f"normalized:L{start}-L{end}"
        return f"{source} {suffix}"
    return source


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
