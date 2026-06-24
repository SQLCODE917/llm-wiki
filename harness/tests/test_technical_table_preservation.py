from llmwiki.domain.evidence_registry import (
    EvidenceRegistry,
    SourceTextKind,
    build_evidence_registry,
    source_text_from_text,
)
from llmwiki.domain.objects import (
    Evidence,
    ExtractedUnit,
    PagePlan,
    PlannedPageWrite,
    RawSource,
    SourceBundle,
    SourceClaim,
    SourceSummaryPlan,
)
from llmwiki.domain.pages import PageMetadata
from llmwiki.domain.technical_atom_builder import build_technical_atom_catalog
from llmwiki.domain.technical_atoms import TechnicalAtomCatalog, render_technical_details_section


def test_contiguous_table_is_preserved_as_one_table_atom() -> None:
    table_markdown = "| 2D | Result |\n| 2 | fumble |"
    catalog = _catalog("# Rules\n\n" + table_markdown, table_markdown)

    assert tuple(atom.atom_kind for atom in catalog.technical_atoms) == ("table",)
    assert len(catalog.technical_tables) == 1
    table = catalog.technical_tables[0]
    assert table.blocks[0].markdown == table_markdown
    assert table.blocks[0].row_count == 2
    assert table.blocks[0].column_count == 2
    assert "table-row" not in {atom.atom_kind for atom in catalog.technical_atoms}


def test_adjacent_continuation_blocks_stay_in_one_table_group() -> None:
    first = "| Key Number | 0 | 1 |\n| 2D | ** | ** |"
    second = "| Key Number | 2 | 3 |\n| 2D | ** | 0 |"
    source = "\n\n".join(("**Rating Table**", first, second))
    catalog = _catalog(source, f"{first}\n\n{second}")

    assert len(catalog.technical_tables) == 1
    table = catalog.technical_tables[0]
    assert table.title == "Rating Table"
    assert tuple(block.markdown for block in table.blocks) == (first, second)


def test_pdf_page_marker_narrows_table_citation_below_source_range() -> None:
    table_markdown = "| 2D | 2 | ** |\n| 3 | 0 | 0 |"
    source = "\n".join(
        (
            "Attack rules.",
            "43",
            "",
            "**Table 4-1: Rating Table**",
            table_markdown,
            "",
            "44",
            "Next page prose.",
        )
    )
    catalog = _catalog(
        source,
        table_markdown,
        source_locator="book.pdf",
        source_format="pdf",
        source_text_kind="pdf-cache",
        unit_locator="p.43-50",
    )

    table = catalog.technical_tables[0]
    atom = catalog.technical_atoms[0]
    assert table.blocks[0].source_citation == "raw/book.pdf p.43"
    assert atom.source_citation == "raw/book.pdf p.43"
    assert table.blocks[0].markdown == table_markdown


def test_table_block_can_cite_two_page_source_span_when_block_matches_source_range() -> None:
    table_markdown = "| Key | Value |\n| A | B |"
    catalog = _catalog(
        table_markdown,
        table_markdown,
        source_locator="book.pdf",
        source_format="pdf",
        source_text_kind="pdf-cache",
        unit_locator="p.1-2",
    )

    assert catalog.technical_tables[0].blocks[0].source_citation == "raw/book.pdf p.1-2"


def test_rendered_table_is_true_to_source_artifact() -> None:
    table_markdown = "| Roll | Outcome |\n| 2 | No damage |\n| 3 | One point |"
    catalog = _catalog("Table:\n" + table_markdown, table_markdown)

    rendered = render_technical_details_section(catalog, "rules")

    assert table_markdown in rendered
    assert rendered.count("| Roll | Outcome |") == 1
    assert rendered.count("| 2 | No damage |") == 1
    assert rendered.count("| 3 | One point |") == 1


def _catalog(
    source: str,
    table_claim: str,
    *,
    source_locator: str = "rules.md",
    source_format: str = "markdown",
    source_text_kind: SourceTextKind = "markdown",
    unit_locator: str = "L1-L10",
) -> TechnicalAtomCatalog:
    plan, registry = _plan(
        source,
        table_claim,
        source_locator=source_locator,
        source_format=source_format,
        source_text_kind=source_text_kind,
        unit_locator=unit_locator,
    )
    return build_technical_atom_catalog(
        source_locator=source_locator,
        page_plan=plan,
        evidence_registry=registry,
        artifact_fingerprint="fp",
    )


def _plan(
    source: str,
    table_claim: str,
    *,
    source_locator: str,
    source_format: str,
    source_text_kind: SourceTextKind,
    unit_locator: str,
) -> tuple[PagePlan, EvidenceRegistry]:
    raw = RawSource(source_locator, source_format)
    unit = ExtractedUnit("unit-1", raw, unit_locator, "Rules", source, "extracted")
    write = PlannedPageWrite(
        write_id="write-rules",
        action="create",
        page_metadata=PageMetadata("rules", "source", "Rules.", sources=(source_locator,)),
        extracted_units=("unit-1",),
        evidence=(Evidence(raw, unit_locator, "Rules", "Rules source."),),
        source_summary_plan=SourceSummaryPlan("source-summary-plan-rules", "rules", ()),
    )
    plan = PagePlan(
        plan_id="plan-rules",
        source_bundle=SourceBundle.one(raw),
        extracted_units=(unit,),
        source_claims=(_claim(raw, table_claim),),
        source_claim_groups=(),
        candidate_claims=(),
        candidate_topics=(),
        candidate_entities=(),
        topic_clusters=(),
        wiki_matches=(),
        claim_comparisons=(),
        planned_writes=(write,),
    )
    registry = build_evidence_registry(
        plan,
        (source_text_from_text(source_locator, source, source_text_kind),),
    )
    return plan, registry


def _claim(raw: RawSource, statement: str) -> SourceClaim:
    return SourceClaim(
        source_claim_id="claim-table",
        statement=statement,
        evidence=Evidence(raw, "L1-L10", "Rules", statement),
        extracted_unit_id="unit-1",
        source_span="L1-L10",
        claim_role_tags=("table",),
        claim_salience=1.0,
    )
