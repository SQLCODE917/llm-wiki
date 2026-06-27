"""Related technical atom surfacing for ordinary source-summary pages."""

from llmwiki.config import WikiPaths
from llmwiki.domain.objects import Evidence, PlannedPageWrite, RawSource, WikiMatch
from llmwiki.domain.pages import PageMetadata
from llmwiki.domain.source_summary import SourceSummaryPlan
from llmwiki.domain.technical_atom_detection import TechnicalAtomKind
from llmwiki.domain.technical_atom_io import technical_atom_catalog_to_json
from llmwiki.domain.technical_atom_surfaces import (
    render_related_technical_details_section,
    select_related_technical_atom_surfaces,
)
from llmwiki.domain.technical_atoms import (
    TechnicalAtom,
    TechnicalAtomCatalog,
)
from llmwiki.store import WikiStore
from llmwiki.workflows.source_summary_write import (
    SourceSummaryBulletParams,
    source_summary_page_body,
)


def test_related_atom_selector_surfaces_neighboring_specifics() -> None:
    catalog = _rules_catalog()

    surfaces = select_related_technical_atom_surfaces(
        catalog,
        "rules-attacks",
        "Attacks use attack power to hit, then add bonus damage.",
        max_atoms=4,
    )

    payloads = tuple(surface.technical_atom.technical_payload for surface in surfaces)
    assert "attack power = skill level + dexterity bonus" in payloads
    assert "bonus damage = skill level + strength bonus" in payloads
    assert "Characters at zero points must make death checks" not in payloads
    assert "Powers = +1 to attack power and bonus damage" not in payloads
    assert "item price = base cost x scarcity" not in payloads


def test_related_atom_selector_can_use_explicit_linked_pages() -> None:
    catalog = _rules_catalog()

    rendered = render_related_technical_details_section(
        catalog,
        "rules-attacks",
        "Attacks use attack power and bonus damage.",
        related_page_ids=("rules-magic-items",),
        max_atoms=4,
    )

    assert "From [[rules-magic-items]]" in rendered
    assert "Powers = +1 to attack power and bonus damage" in rendered


def test_source_summary_page_body_appends_related_technical_details(
    store: WikiStore,
    paths: WikiPaths,
) -> None:
    raw_source = RawSource("rules.md", "markdown")
    (paths.raw_dir / "rules.md").write_text(
        "Attack checks compare a combat total to evasion.", encoding="utf-8"
    )
    store.write_technical_atom_catalog_artifact(
        "rules.md", technical_atom_catalog_to_json(_rules_catalog())
    )

    body, _draft = source_summary_page_body(
        store,
        _attack_write(raw_source),
        "The source explains attack checks and damage.",
        [
            SourceSummaryBulletParams(
                bullet_text=(
                    "Attacks compare attack power and then apply bonus damage. (raw/rules.md)"
                ),
                covered_source_claims=["claim-attack"],
            )
        ],
    )

    assert "## Technical details" in body
    assert "## Related technical details" in body
    assert "From [[rules-movement-and-actions]]" in body
    assert "attack power = skill level + dexterity bonus" in body
    assert "bonus damage = skill level + strength bonus" in body


def test_source_summary_ignores_planning_matches_as_explicit_links(
    store: WikiStore,
    paths: WikiPaths,
) -> None:
    raw_source = RawSource("rules.md", "markdown")
    (paths.raw_dir / "rules.md").write_text(
        "Attack checks compare a combat total to evasion.", encoding="utf-8"
    )
    store.write_technical_atom_catalog_artifact(
        "rules.md", technical_atom_catalog_to_json(_rules_catalog())
    )

    body, _draft = source_summary_page_body(
        store,
        _attack_write(
            raw_source,
            wiki_matches=(WikiMatch("rules-magic-items", 1.0, "unit"),),
        ),
        "The source explains attack checks and damage.",
        [
            SourceSummaryBulletParams(
                bullet_text=(
                    "Attacks compare attack power and then apply bonus damage. (raw/rules.md)"
                ),
                covered_source_claims=["claim-attack"],
            )
        ],
    )

    assert "Powers = +1 to attack power and bonus damage" not in body


def _attack_write(
    raw_source: RawSource, wiki_matches: tuple[WikiMatch, ...] = ()
) -> PlannedPageWrite:
    return PlannedPageWrite(
        write_id="write-rules-attacks",
        action="create-new",
        page_metadata=PageMetadata(
            page_id="rules-attacks",
            page_kind="source",
            summary="Attack checks and damage.",
            sources=("raw/rules.md",),
        ),
        extracted_units=("unit-0001",),
        evidence=(Evidence(raw_source, "document"),),
        wiki_matches=wiki_matches,
        source_summary_plan=SourceSummaryPlan(
            source_summary_plan_id="source-summary-plan-rules-attacks",
            page_id="rules-attacks",
            selected_source_claims=("claim-attack",),
            required_source_citations=("raw/rules.md",),
        ),
    )


def _rules_catalog() -> TechnicalAtomCatalog:
    return TechnicalAtomCatalog(
        catalog_id="technical-atom-catalog-rules",
        source_locator="rules.md",
        artifact_fingerprint="fp",
        technical_atoms=(
            _atom(
                "owned-procedure",
                "rules-attacks",
                "procedure",
                "1. Roll attack.\n2. Apply damage.",
            ),
            _atom(
                "attack-power",
                "rules-movement-and-actions",
                "formula",
                "attack power = skill level + dexterity bonus",
            ),
            _atom(
                "bonus-damage",
                "rules-movement-and-actions",
                "formula",
                "bonus damage = skill level + strength bonus",
            ),
            _atom("filler-a", "rules-filler-a", "formula", "travel pace = agility x 3"),
            _atom("filler-b", "rules-filler-b", "formula", "spell power = level + focus"),
            _atom(
                "death-checks",
                "rules-unconscious-and-death-checks",
                "requirement",
                "Characters at zero points must make death checks",
            ),
            _atom(
                "filler-c",
                "rules-filler-c",
                "formula",
                "item price = base cost x scarcity",
            ),
            _atom("filler-d", "rules-filler-d", "procedure", "1. Rest.\n2. Recover."),
            _atom(
                "magic-item",
                "rules-magic-items",
                "formula",
                "Powers = +1 to attack power and bonus damage",
            ),
        ),
    )


def _atom(atom_id: str, page_id: str, kind: TechnicalAtomKind, payload: str) -> TechnicalAtom:
    return TechnicalAtom(
        technical_atom_id=f"technical-atom-{atom_id}",
        source_locator="rules.md",
        page_id=page_id,
        atom_kind=kind,
        title=f"{kind}: {payload}",
        technical_payload=payload,
        normalized_fields=(("source_citation", "raw/rules.md"),),
        source_claim_ids=(),
        evidence_ids=(f"evidence-{atom_id}",),
        source_range_id=f"source-range-{page_id}",
    )
