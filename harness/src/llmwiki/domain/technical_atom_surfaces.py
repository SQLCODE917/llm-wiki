"""Source-agnostic surfacing of related technical atoms."""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.technical_atom_detection import normalize_payload
from llmwiki.domain.technical_atoms import (
    TechnicalAtom,
    TechnicalAtomCatalog,
    render_technical_details_section,
    render_technical_table,
)


@dataclass(frozen=True)
class RelatedTechnicalAtomSurface:
    page_id: str
    related_page_id: str
    technical_atom: TechnicalAtom
    score: int
    matched_terms: tuple[str, ...]
    relation_reason: str


_KIND_PRIORITY = {
    "code": 0,
    "formula": 1,
    "procedure": 2,
    "requirement": 3,
    "exception": 4,
    "worked-example": 5,
    "table": 6,
    "table-row": 7,
}
_KIND_SCORE = {
    "code": 18,
    "formula": 16,
    "procedure": 14,
    "requirement": 10,
    "exception": 8,
    "worked-example": 6,
    "table": 4,
    "table-row": 2,
}
_TERM_RE = re.compile(r"[a-z][a-z0-9-]{2,}", re.IGNORECASE)
_STOP_TERMS = frozenset(
    [
        "and",
        "are",
        "book",
        "chapter",
        "complete",
        "details",
        "edition",
        "for",
        "from",
        "into",
        "part",
        "pdf",
        "raw",
        "section",
        "source",
        "technical",
        "that",
        "the",
        "this",
        "through",
        "with",
        "world",
    ]
)
_BROAD_TECHNICAL_TERMS = frozenset(
    [
        "bonus",
        "check",
        "checks",
        "damage",
        "formula",
        "hit",
        "level",
        "points",
        "power",
        "requirement",
        "roll",
        "rules",
        "skill",
        "target",
    ]
)
_MAX_RELATED_PAGE_DISTANCE = 4
_RELATED_SCORE_FLOOR = 40


def render_technical_details_sections(
    catalog: TechnicalAtomCatalog,
    page_id: str,
    page_context_text: str,
    *,
    related_page_ids: tuple[str, ...] = (),
    max_related_atoms: int = 4,
) -> str:
    sections = tuple(
        section
        for section in (
            render_technical_details_section(catalog, page_id),
            render_related_technical_details_section(
                catalog,
                page_id,
                page_context_text,
                related_page_ids=related_page_ids,
                max_atoms=max_related_atoms,
            ),
        )
        if section
    )
    return "\n\n".join(sections)


def render_related_technical_details_section(
    catalog: TechnicalAtomCatalog,
    page_id: str,
    page_context_text: str,
    *,
    related_page_ids: tuple[str, ...] = (),
    max_atoms: int = 4,
) -> str:
    surfaces = select_related_technical_atom_surfaces(
        catalog,
        page_id,
        page_context_text,
        related_page_ids=related_page_ids,
        max_atoms=max_atoms,
    )
    if not surfaces:
        return ""
    rendered = tuple(_render_related_surface(catalog, surface) for surface in surfaces)
    return "\n\n".join(("## Related technical details", *rendered))


def select_related_technical_atom_surfaces(
    catalog: TechnicalAtomCatalog,
    page_id: str,
    page_context_text: str,
    *,
    related_page_ids: tuple[str, ...] = (),
    max_atoms: int = 4,
) -> tuple[RelatedTechnicalAtomSurface, ...]:
    context_terms = _technical_terms(page_context_text)
    if not context_terms:
        return ()
    ignored_terms = _ignored_catalog_terms(catalog)
    context_terms = context_terms - ignored_terms
    context_phrases = _technical_phrases(page_context_text, ignored_terms)
    page_order = _page_order(catalog)
    source_index = page_order.get(page_id)
    explicit_pages = frozenset(related_page_ids)
    owned_payloads = {
        normalize_payload(atom.technical_payload) for atom in catalog.atoms_for_page(page_id)
    }
    surfaces = tuple(
        surface
        for atom in catalog.technical_atoms
        if atom.page_id != page_id
        and normalize_payload(atom.technical_payload) not in owned_payloads
        if (
            surface := _related_surface(
                page_id,
                atom,
                context_terms,
                page_order,
                source_index,
                explicit_pages,
                context_phrases,
                ignored_terms,
            )
        )
        is not None
    )
    ordered = sorted(
        enumerate(surfaces),
        key=lambda item: (
            -item[1].score,
            _KIND_PRIORITY.get(item[1].technical_atom.atom_kind, 99),
            page_order.get(item[1].related_page_id, 999_999),
            item[0],
        ),
    )
    return tuple(surface for _index, surface in ordered[:max_atoms])


def _render_related_surface(
    catalog: TechnicalAtomCatalog, surface: RelatedTechnicalAtomSurface
) -> str:
    atom = surface.technical_atom
    header = f"### From [[{surface.related_page_id}]]: `{atom.technical_atom_id}` {atom.atom_kind}"
    terms = ", ".join(f"`{term}`" for term in surface.matched_terms[:6])
    reason = f"Relation: {surface.relation_reason}"
    if terms:
        reason = f"{reason}; matched terms {terms}"
    citation = f"Citation: ({atom.source_citation})"
    if atom.atom_kind == "code":
        language = dict(atom.normalized_fields).get("language", "")
        return f"{header}\n\n{reason}\n\n{citation}\n\n```{language}\n{atom.technical_payload}\n```"
    if atom.atom_kind == "table":
        table = catalog.table_for_atom(atom)
        if table is not None:
            return f"{header}\n\n{reason}\n\n{render_technical_table(table)}"
    return f"{header}\n\n{reason}\n\n{citation}\n\n{atom.technical_payload}"


def _related_surface(
    page_id: str,
    atom: TechnicalAtom,
    context_terms: frozenset[str],
    page_order: dict[str, int],
    source_index: int | None,
    explicit_pages: frozenset[str],
    context_phrases: frozenset[str],
    ignored_terms: frozenset[str],
) -> RelatedTechnicalAtomSurface | None:
    atom_terms = _atom_terms(atom, ignored_terms)
    matched_terms = tuple(sorted(context_terms & atom_terms))
    matched_phrases = tuple(sorted(context_phrases & _atom_phrases(atom, ignored_terms)))
    is_explicit = atom.page_id in explicit_pages
    distance = _page_distance(source_index, page_order.get(atom.page_id))
    if not _passes_related_gate(matched_terms, matched_phrases, is_explicit, distance):
        return None
    proximity_score = 0 if distance is None else max(0, 48 - distance * 8)
    explicit_score = 40 if is_explicit else 0
    specific_terms = _specific_terms(matched_terms)
    broad_terms = tuple(term for term in matched_terms if term not in specific_terms)
    score = len(matched_phrases) * 50 + len(specific_terms) * 15 + len(broad_terms) * 4
    score += proximity_score + explicit_score
    score += _KIND_SCORE.get(atom.atom_kind, 0)
    if score < _RELATED_SCORE_FLOOR:
        return None
    return RelatedTechnicalAtomSurface(
        page_id, atom.page_id, atom, score, matched_terms, _relation_reason(is_explicit, distance)
    )


def _passes_related_gate(
    matched_terms: tuple[str, ...],
    matched_phrases: tuple[str, ...],
    is_explicit: bool,
    distance: int | None,
) -> bool:
    if is_explicit and (matched_phrases or _specific_terms(matched_terms)):
        return True
    if distance is None or distance > _MAX_RELATED_PAGE_DISTANCE:
        return False
    return bool(matched_phrases) or len(_specific_terms(matched_terms)) >= 3


def _relation_reason(is_explicit: bool, distance: int | None) -> str:
    reasons = []
    if is_explicit:
        reasons.append("linked page")
    if distance is not None:
        reasons.append("nearby source page" if distance else "same source page group")
    return ", ".join(reasons) or "shared source terms"


def _page_order(catalog: TechnicalAtomCatalog) -> dict[str, int]:
    order: dict[str, int] = {}
    for atom in catalog.technical_atoms:
        order.setdefault(atom.page_id, len(order))
    return order


def _page_distance(source_index: int | None, target_index: int | None) -> int | None:
    if source_index is None or target_index is None:
        return None
    return abs(source_index - target_index)


def _atom_terms(atom: TechnicalAtom, ignored_terms: frozenset[str]) -> frozenset[str]:
    text = " ".join((atom.page_id.replace("-", " "), atom.title, atom.technical_payload))
    return _technical_terms(text) - ignored_terms


def _atom_phrases(atom: TechnicalAtom, ignored_terms: frozenset[str]) -> frozenset[str]:
    text = " ".join((atom.title, atom.technical_payload))
    return _technical_phrases(text, ignored_terms)


def _technical_terms(text: str) -> frozenset[str]:
    return frozenset(_ordered_terms(text))


def _technical_phrases(text: str, ignored_terms: frozenset[str]) -> frozenset[str]:
    terms = tuple(_ordered_terms(text, ignored_terms))
    return frozenset(f"{left} {right}" for left, right in zip(terms, terms[1:], strict=False))


def _specific_terms(terms: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(term for term in terms if term not in _BROAD_TECHNICAL_TERMS)


def _ignored_catalog_terms(catalog: TechnicalAtomCatalog) -> frozenset[str]:
    page_ids = tuple(dict.fromkeys(atom.page_id for atom in catalog.technical_atoms))
    if not page_ids:
        return _technical_terms(catalog.source_locator)
    threshold = max(2, int(len(page_ids) * 0.6))
    counts: dict[str, int] = {}
    for page_id in page_ids:
        for term in _technical_terms(page_id.replace("-", " ")):
            counts[term] = counts.get(term, 0) + 1
    common_page_terms = {term for term, count in counts.items() if count >= threshold}
    return frozenset((*_technical_terms(catalog.source_locator), *common_page_terms))


def _ordered_terms(text: str, ignored_terms: frozenset[str] = frozenset()) -> tuple[str, ...]:
    return tuple(
        term
        for term in _TERM_RE.findall(text.replace("_", " ").lower())
        if term not in _STOP_TERMS and term not in ignored_terms
    )
