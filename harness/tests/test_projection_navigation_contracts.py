from llmwiki.domain.ledger.atom_addressing import technical_atom_anchor_id
from llmwiki.domain.ledger.atom_context import TechnicalAtomContext
from llmwiki.domain.ledger.atoms import TablePayload, TechnicalAtom
from llmwiki.domain.ledger.collection_pages import collection_plans
from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.knowledge_shapes import build_knowledge_shape_catalog
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    FamilyLabelScore,
    SourceFamilyAssignment,
    SourceProfile,
)
from llmwiki.domain.ledger.related_link_policy import budget_related_links, group_related_links
from llmwiki.domain.ledger.source_manifest_navigation import (
    build_source_navigation_plan,
    render_source_manifest,
)
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode
from llmwiki.domain.ledger.table_authority import table_authority_decisions
from llmwiki.domain.ledger.topic_models import SourceTopic
from llmwiki.domain.ledger.topic_relations import RelatedTopicLink
from llmwiki.domain.ledger.topic_render import render_topic_page
from llmwiki.domain.pages import PageMetadata, WikiPage


def test_source_manifest_is_navigation_first_without_source_transcript() -> None:
    structure = _structure(
        StructureNode("chapter", "chapter", "1. Vel", "r1", "x.pdf", 1)
    )
    linked = (
        _page("x-section-1-vel-aaaa1111", "source", "section-reference"),
        _page("x-procedure-build-vel", "procedure", "procedure-guide"),
        _page("x-vel", "concept", "topic-concept"),
    )

    plan = build_source_navigation_plan(
        source_page_id="x",
        title="X",
        source_locator="x.pdf",
        ledger_summary="Claim-ledger projection.",
        linked_pages=linked,
        structure=structure,
    )
    body = render_source_manifest(plan)

    assert body.index("## Page Families") < body.index("## Procedure Guides")
    assert "section-reference: 1 page(s)" in body
    assert "[[x-procedure-build-vel]]" in body
    assert "```" not in body
    assert "| --- |" not in body


def test_collection_plans_use_repeated_peer_shape_not_domain_nouns() -> None:
    structure = _structure(
        StructureNode("parent", "chapter", "Mav", "r-001", "x.pdf", 1),
        StructureNode("one", "section", "Rin", "r-002", "x.pdf", 2, 1, "parent"),
        StructureNode("two", "section", "Paz", "r-003", "x.pdf", 3, 1, "parent"),
        StructureNode("three", "section", "Tov", "r-004", "x.pdf", 4, 1, "parent"),
    )
    ledger = _ledger(
        _entry("e1", "one", "Rin has a structured value."),
        _entry("e2", "two", "Paz has a structured value."),
        _entry("e3", "three", "Tov has a structured value."),
        atoms=(
            _table_atom("t1", "r-002"),
            _table_atom("t2", "r-003"),
            _table_atom("t3", "r-004"),
        ),
        atom_nodes={"t1": "one", "t2": "two", "t3": "three"},
    )
    catalog = build_knowledge_shape_catalog(ledger, structure)

    plans = collection_plans(ledger, structure, "x", catalog)

    assert len(plans) == 1
    assert plans[0].source_node_id == "parent"
    assert [member.structure_node_id for member in plans[0].members] == [
        "one",
        "two",
        "three",
    ]
    assert "sibling-structure" in plans[0].peer_signal_kinds


def test_related_link_policy_groups_and_budgets_visible_links() -> None:
    links = (
        RelatedTopicLink("prev", "Previous", "previous source section"),
        RelatedTopicLink("next", "Next", "next source section"),
        *(
            RelatedTopicLink(f"shared-{index}", "Shared", "shared statements")
            for index in range(30)
        ),
    )

    visible = budget_related_links(links)
    groups = group_related_links(visible)

    assert len(visible) == 10
    assert [group.group_kind for group in groups] == ["source-order", "shared-claim"]
    assert len(groups[1].visible_links) == 8


def test_topic_page_renders_only_contextualized_technical_atoms() -> None:
    contextual = _table_atom("contextual", "r-010")
    orphan = _table_atom("orphan", "r-011")
    ledger = _ledger(
        atoms=(contextual, orphan),
        atom_nodes={"contextual": "root", "orphan": "root"},
        contexts=(
            TechnicalAtomContext(
                "ctx",
                "contextual",
                "introduced-by-source-prose",
                "This table demonstrates vel choices.",
                (),
                ("r-009",),
                ("vel", "choices"),
                ("ev-009",),
                ConfidenceBasis("test"),
            ),
        ),
    )
    topic = SourceTopic(
        topic_key="vel",
        label="Vel",
        page_kind="concept",
        match_terms=("vel",),
        entry_ids=(),
        atom_ids=("contextual", "orphan"),
        from_heading=True,
        salience=1.0,
    )

    rendered = render_topic_page(topic, ledger, wiki_page_locator="x-vel", source_page_id="x")

    assert technical_atom_anchor_id("contextual") in rendered.page_body
    assert "This table demonstrates vel choices." in rendered.page_body
    assert technical_atom_anchor_id("orphan") not in rendered.page_body


def test_table_authority_selects_one_canonical_variant_per_source_table() -> None:
    parsed = _table_atom("parsed", "r-020", parse_status="parsed")
    partial = _table_atom("partial", "r-020", parse_status="partially-parsed")

    decisions = table_authority_decisions((partial, parsed))

    assert len(decisions) == 1
    assert decisions[0].status == "needs-review"
    assert decisions[0].canonical_atom_id == "parsed"
    assert decisions[0].variant_atom_ids == ("parsed", "partial")


def _page(page_id: str, page_kind: str, page_family: str) -> WikiPage:
    return WikiPage.from_metadata(
        PageMetadata(
            page_id=page_id,
            page_kind=page_kind,
            page_family=page_family,
            summary=f"{page_id} summary.",
            sources=("raw/x.pdf",),
        ),
        f"# {page_id}\n",
    )


def _structure(*nodes: StructureNode) -> DocumentStructure:
    root = StructureNode("root", "root", "x.pdf", "root", "x.pdf", 0)
    return DocumentStructure("root", (root, *nodes))


def _entry(entry_id: str, node_id: str, text: str) -> LedgerEntry:
    return LedgerEntry(
        ledger_entry_id=entry_id,
        source_statement_id=f"statement-{entry_id}",
        ledger_entry_kind="claim",
        ledger_entry_status="usable",
        extraction_confidence="high",
        confidence_basis=ConfidenceBasis("test"),
        source_locator="x.pdf",
        source_hash="hash",
        source_range_id=f"range-{entry_id}",
        evidence_ids=(f"ev-{entry_id}",),
        source_text=text,
        structure_node_ids=(node_id, "root"),
        normalized_text=text,
        subject=text,
        predicate="is",
        object_value=text,
        polarity="positive",
        claim_force="asserted",
    )


def _table_atom(atom_id: str, range_id: str, *, parse_status: str = "parsed") -> TechnicalAtom:
    return TechnicalAtom(
        technical_atom_id=atom_id,
        technical_atom_kind="table",
        payload=TablePayload(
            raw_table_text="Table 1: Vel\nRoll | Result\n1 | Rin",
            parse_status=parse_status,
            source_locator="x.pdf",
            caption="Table 1: Vel",
        ),
        source_locator="x.pdf",
        source_range_id=range_id,
        evidence_ids=(f"ev-{atom_id}",),
        parse_status=parse_status,
    )


def _ledger(
    *entries: LedgerEntry,
    atoms: tuple[TechnicalAtom, ...] = (),
    atom_nodes: dict[str, str] | None = None,
    contexts: tuple[TechnicalAtomContext, ...] = (),
) -> ClaimLedger:
    resolved_nodes = atom_nodes or {}
    atom_entries = tuple(
        LedgerEntry(
            ledger_entry_id=f"entry-{atom.technical_atom_id}",
            source_statement_id=f"statement-{atom.technical_atom_id}",
            ledger_entry_kind="technical-atom",
            ledger_entry_status="usable",
            extraction_confidence="high",
            confidence_basis=ConfidenceBasis("test"),
            source_locator="x.pdf",
            source_hash="hash",
            source_range_id=atom.source_range_id,
            evidence_ids=atom.evidence_ids,
            source_text="",
            structure_node_ids=(resolved_nodes.get(atom.technical_atom_id, "root"), "root"),
            technical_atom_kind=atom.technical_atom_kind,
            technical_atom_id=atom.technical_atom_id,
        )
        for atom in atoms
    )
    return ClaimLedger(
        claim_ledger_id="ledger",
        source_locator="x.pdf",
        source_hash="hash",
        evidence_registry_hash="registry",
        source_profile=SourceProfile(
            source_locator="x.pdf",
            unit_count=1,
            accepted_entry_count=len(entries) + len(atom_entries),
            claim_count=len(entries),
            event_count=0,
            concept_count=0,
            relationship_count=0,
            atom_kind_counts={"table": len(atoms)} if atoms else {},
            feature_signal_means={},
        ),
        source_family_assignment=SourceFamilyAssignment(
            labels=(FamilyLabelScore("synthetic", 1.0),),
            assignment_confidence=1.0,
        ),
        entries=(*entries, *atom_entries),
        technical_atoms=atoms,
        technical_atom_contexts=contexts,
        source_statements=(),
        extractor_decisions=(),
        rejected_candidates=(),
    )
