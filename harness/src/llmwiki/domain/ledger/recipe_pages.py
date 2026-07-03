"""Render reusable source-backed recipe pages."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.atoms import CodeBlockPayload, TechnicalAtom, atom_raw_text
from llmwiki.domain.ledger.canonical import short_digest
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.knowledge_shapes import KnowledgeShapeCatalog
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.section_navigation import section_page_id
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode
from llmwiki.domain.pages import PageMetadata, WikiPage, slugify

PAGE_FAMILY_RECIPE_PATTERN = "recipe-pattern"

_MAX_STATEMENTS = 6
_MAX_ATOMS = 6
_MAX_ATOM_CHARS = 1800


@dataclass(frozen=True)
class RecipePattern:
    recipe_id: str
    title: str
    source_node: StructureNode
    source_section_page_id: str
    claims: tuple[LedgerEntry, ...]
    technical_atoms: tuple[TechnicalAtom, ...]
    evidence_roles: tuple[str, ...]


def build_recipe_pages(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    *,
    source_page_id: str,
    source_locator: str,
    today: str,
    shape_catalog: KnowledgeShapeCatalog,
) -> tuple[WikiPage, ...]:
    pages: list[WikiPage] = []
    for pattern in plan_recipe_patterns(ledger, structure, source_page_id, shape_catalog):
        body = render_recipe_page(pattern, source_page_id)
        metadata = PageMetadata(
            page_id=pattern.recipe_id,
            page_kind="recipe",
            page_family=PAGE_FAMILY_RECIPE_PATTERN,
            summary=(
                f"{pattern.title}: reusable source-backed pattern with "
                f"{len(pattern.claims)} statement(s) and {len(pattern.technical_atoms)} "
                f"technical atom(s) from raw/{source_locator}."
            ),
            sources=(f"raw/{source_locator}",),
            updated=today,
            domain=source_page_id,
            category_path=f"recipes/{source_page_id}",
            source_id=source_locator,
            aliases=(slugify(pattern.title),),
            projection_coverage_pointer=f"recipe-{pattern.recipe_id}@{short_digest(body, 32)}",
        )
        pages.append(WikiPage.from_metadata(metadata, body))
    return tuple(pages)


def plan_recipe_patterns(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    source_page_id: str,
    shape_catalog: KnowledgeShapeCatalog,
) -> tuple[RecipePattern, ...]:
    patterns: list[RecipePattern] = []
    used_page_ids: set[str] = set()
    for candidate in shape_catalog.candidates_of_kind("recipe"):
        node = structure.node(candidate.structure_node_id)
        if node is None:
            continue
        recipe_id = _recipe_page_id(
            source_page_id,
            candidate.label,
            candidate.structure_node_id,
            used_page_ids,
        )
        claims = tuple(
            entry
            for entry_id in candidate.entry_ids
            if (entry := ledger.entry(entry_id)) is not None
        )
        atoms = tuple(
            atom for atom_id in candidate.atom_ids if (atom := ledger.atom(atom_id)) is not None
        )
        patterns.append(
            RecipePattern(
                recipe_id=recipe_id,
                title=_clean_title(candidate.label),
                source_node=node,
                source_section_page_id=section_page_id(source_page_id, structure, node),
                claims=_unique_entries(claims),
                technical_atoms=_recipe_atoms(_unique_atoms(atoms)),
                evidence_roles=candidate.evidence_roles,
            )
        )
    return tuple(patterns)


def _recipe_page_id(
    source_page_id: str,
    label: str,
    structure_node_id: str,
    used_page_ids: set[str],
) -> str:
    base_id = slugify(f"{source_page_id}-recipe-{label}")
    if base_id not in used_page_ids:
        used_page_ids.add(base_id)
        return base_id
    page_id = slugify(f"{base_id}-{short_digest(structure_node_id, 8)}")
    while page_id in used_page_ids:
        page_id = slugify(f"{base_id}-{short_digest(page_id, 8)}")
    used_page_ids.add(page_id)
    return page_id


def render_recipe_page(pattern: RecipePattern, source_page_id: str) -> str:
    lines = [f"# {pattern.title}", "", f"From [[{source_page_id}]].", ""]
    lines.extend(
        (
            "## Pattern",
            "",
            f"- Use the source-backed pattern described in [[{pattern.source_section_page_id}]].",
            f"- Evidence roles: {', '.join(pattern.evidence_roles) or 'source-backed pattern'}.",
            "",
        )
    )
    if pattern.claims:
        lines.extend(("## Applicability And Rationale", ""))
        for claim in pattern.claims[:_MAX_STATEMENTS]:
            lines.append(f"- {_entry_text(claim)} _({_citation(claim)})_")
        lines.append("")
    if pattern.technical_atoms:
        lines.extend(("## Technical Atoms", ""))
        for index, atom in enumerate(pattern.technical_atoms[:_MAX_ATOMS], start=1):
            lines.append(f"### Atom {index}: `{atom.technical_atom_kind}`")
            lines.append("")
            lines.append(f"_Source: {_atom_citation(atom)}_")
            lines.append("")
            lines.extend(_render_atom(atom))
            lines.append("")
    lines.extend(
        (
            "## Source Trail",
            "",
            f"- Source manifest: [[{source_page_id}]]",
            f"- Source section: [[{pattern.source_section_page_id}]]",
        )
    )
    return "\n".join(lines).strip() + "\n"


def _render_atom(atom: TechnicalAtom) -> list[str]:
    text = atom_raw_text(atom.payload).strip()
    if len(text) > _MAX_ATOM_CHARS:
        text = text[:_MAX_ATOM_CHARS].rstrip() + "\n[truncated in recipe page]"
    fence_info = ""
    if isinstance(atom.payload, CodeBlockPayload) and atom.payload.language_tag:
        fence_info = atom.payload.language_tag
    return [f"```{fence_info}", text, "```"]


def _clean_title(text: str) -> str:
    return " ".join(text.replace("/", " ").split()).strip(" :-")


def _entry_text(entry: LedgerEntry) -> str:
    return (entry.normalized_text or entry.source_text).strip()


def _citation(entry: LedgerEntry) -> str:
    return f"{entry.source_locator} ({entry.source_range_id})"


def _atom_citation(atom: TechnicalAtom) -> str:
    return f"{atom.source_locator} ({atom.source_range_id})"


def _unique_entries(entries: tuple[LedgerEntry, ...]) -> tuple[LedgerEntry, ...]:
    seen: set[tuple[str, str]] = set()
    unique: list[LedgerEntry] = []
    for entry in entries:
        key = (entry.source_range_id, _entry_text(entry))
        if key not in seen:
            seen.add(key)
            unique.append(entry)
    return tuple(unique)


def _unique_atoms(atoms: tuple[TechnicalAtom, ...]) -> tuple[TechnicalAtom, ...]:
    seen: set[str] = set()
    unique: list[TechnicalAtom] = []
    for atom in atoms:
        if atom.technical_atom_id not in seen:
            seen.add(atom.technical_atom_id)
            unique.append(atom)
    return tuple(unique)


def _recipe_atoms(atoms: tuple[TechnicalAtom, ...]) -> tuple[TechnicalAtom, ...]:
    return tuple(
        atom for atom in atoms if atom.technical_atom_kind in {"code-block", "worked-example"}
    )
