"""Cross-source synthesis tests for artifact-driven concept projection."""

from __future__ import annotations

import json

from forge.context import ContextManager, NoCompact

from llmwiki.cli import _build_parser
from llmwiki.config import WikiPaths
from llmwiki.domain.ledger.canonical_concept import (
    CanonicalConceptPage,
    ConceptAtomBlock,
    ConceptEvidenceItem,
    ConceptRelationship,
    ConceptSourceSection,
    render_canonical_concept_page,
)
from llmwiki.domain.ledger.concepts import concept_topic_keys
from llmwiki.domain.ledger.cross_source import (
    SourcePosition,
    classify_relationship,
    plan_cross_source_topics,
)
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.runtime.cross_source_load import load_source_positions
from llmwiki.runtime.cross_source_pipeline import build_cross_source_pages
from llmwiki.runtime.session import Session
from llmwiki.store import WikiStore

TODAY = "2026-06-27"


def test_shared_concept_across_sources_becomes_cross_source_topic() -> None:
    topics = plan_cross_source_topics((_position("alpha.pdf"), _position("beta.pdf")))

    assert len(topics) == 1
    assert topics[0].topic_key == "closure"
    assert {position.source_locator for position in topics[0].positions} == {
        "alpha.pdf",
        "beta.pdf",
    }


def test_relationship_classifier_keeps_incomparable_claims_unrelated() -> None:
    alpha = _position("alpha.pdf", predicate="contains")
    beta = _position("beta.pdf", predicate="requires")

    assert classify_relationship(alpha, beta) is None


def test_loader_reads_one_position_per_topic() -> None:
    loaded = load_source_positions(
        _topic_index("alpha.pdf", [("binding", "Binding", "A binding names a value.")])
    )

    assert loaded.source_locator == "alpha.pdf"
    assert len(loaded.positions) == 1
    assert loaded.positions[0].topic_keys == ("binding",)


def test_build_cross_source_pages_from_two_topic_indexes() -> None:
    alpha_topics = [("binding", "Binding", "A binding names a value.")]
    beta_topics = [("binding", "Binding", "Bindings attach names.")]

    result = build_cross_source_pages(
        (
            _topic_index("alpha.pdf", alpha_topics),
            _topic_index("beta.pdf", beta_topics),
        ),
        (
            _claim_ledger("alpha.pdf", alpha_topics),
            _claim_ledger("beta.pdf", beta_topics),
        ),
        today=TODAY,
    )

    concept_pages = [page for page in result.pages if page.page_kind == "concept"]
    assert any(page.page_id == "binding" for page in concept_pages)
    assert any(page.page_kind == "synthesis" for page in result.pages)
    assert result.blocked == ()
    body = next(page.page_body for page in concept_pages if page.page_id == "binding")
    assert "## Source Evidence" in body
    assert "Source topic: [[alpha-binding]]" in body
    assert "A binding names a value." in body


async def test_session_synthesize_writes_pages_and_removes_stale_cross_source(
    store: WikiStore, paths: WikiPaths
) -> None:
    for source in ("alpha.pdf", "beta.pdf"):
        topics = [("monad", "Monad", "A monad wraps a value.")]
        store.write_ledger_artifacts(
            source,
            {
                "topics.json": _topic_index(source, topics),
                "claim-ledger.json": _claim_ledger(source, topics),
            },
        )
    store.write_page(
        WikiPage.from_metadata(
            PageMetadata(
                page_id="stale-concept",
                page_kind="concept",
                summary="Stale generated concept.",
                projection_coverage_pointer="canonical-concept-stale-concept@old",
            ),
            "# Stale\n",
        )
    )

    result = await Session(
        store=store,
        client=None,
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=1),
        today=TODAY,
        runs_dir=paths.root / "runs",
        run_id="synth-test",
    ).synthesize()

    assert "Canonical concept synthesis over 2 source(s)" in result.output
    assert "monad" in store.list_pages()
    assert "cross-source-synthesis" in store.list_pages()
    assert "stale-concept" not in store.list_pages()
    body = store.read_page("monad")
    assert "[[alpha]]" in body and "[[beta]]" in body
    assert "Source topic: [[alpha-monad]]" in body
    assert "A monad wraps a value." in body
    assert f"## [{TODAY}] synthesize" in paths.log_path.read_text(encoding="utf-8")


def test_canonical_concept_page_pairs_atom_context_and_payload() -> None:
    rendered = render_canonical_concept_page(_canonical_topic_with_atom(), "closure")

    assert "##### Technical atom 1" in rendered.page_body
    assert rendered.page_body.index("**Context:**") < rendered.page_body.index("**Atom:**")
    assert "**Atom:** _(alpha.pdf (source-range-code))_" in rendered.page_body


def test_cli_exposes_synthesize_command() -> None:
    args = _build_parser().parse_args(["synthesize"])

    assert args.op == "synthesize"


def _position(
    source: str,
    *,
    predicate: str = "is",
    text: str = "A closure is a function plus its environment.",
) -> SourcePosition:
    return SourcePosition(
        source_locator=source,
        source_hash=source[:8].ljust(8, "0"),
        projection_source_support_id=f"pss-{source}",
        ledger_entry_id=f"ledger-entry-{source}-1",
        ledger_entry_kind="concept",
        subject="A closure",
        predicate=predicate,
        polarity="affirmative",
        claim_force="asserted",
        condition_scope="unconditional",
        has_scope=False,
        normalized_text=text,
        concept_facets=("closure",),
        topic_keys=concept_topic_keys(("closure",)),
        evidence_ids=(f"ev-{source}",),
        citation_label=f"{source} (source-range-1)",
    )


def _representative(entry_id: str, text: str, source: str) -> dict[str, object]:
    return {
        "ledger_entry_id": entry_id,
        "subject": "Subject",
        "predicate": "is",
        "polarity": "affirmative",
        "claim_force": "asserted",
        "condition_scope": "unconditional",
        "has_scope": False,
        "normalized_text": text,
        "citation_label": f"{source} (source-range-1)",
    }


def _topic_index(source: str, topics: list[tuple[str, str, str]]) -> str:
    return json.dumps(
        {
            "source_locator": source,
            "source_hash": source[:8].ljust(8, "0"),
            "projection_source_support_id": f"pss-{source}",
            "topics": [
                {
                    "topic_key": key,
                    "label": label,
                    "page_kind": "concept",
                    "entry_count": 1,
                    "atom_count": 0,
                    "entry_ids": [f"le-{source}-{key}"],
                    "atom_ids": [],
                    "representative": _representative(f"le-{source}-{key}", text, source),
                }
                for key, label, text in topics
            ],
        }
    )


def _claim_ledger(source: str, topics: list[tuple[str, str, str]]) -> str:
    return json.dumps(
        {
            "ledger": {
                "source_locator": source,
                "entries": [
                    {
                        "ledger_entry_id": f"le-{source}-{key}",
                        "normalized_text": text,
                        "source_text": text,
                        "source_locator": source,
                        "source_range_id": "source-range-1",
                    }
                    for key, _label, text in topics
                ],
                "technical_atoms": [],
                "technical_atom_contexts": [],
            }
        }
    )


def _canonical_topic_with_atom() -> CanonicalConceptPage:
    return CanonicalConceptPage(
        topic_key="closure",
        label="Closure",
        page_kind="concept",
        source_sections=(
            ConceptSourceSection(
                source_locator="alpha.pdf",
                source_page_id="alpha",
                topic_page_id="alpha-closure",
                label="Closure",
                evidence_items=(
                    ConceptEvidenceItem("le-a", "A closure binds scope.", "alpha.pdf (sr-1)"),
                ),
                atom_blocks=(
                    ConceptAtomBlock(
                        technical_atom_id="atom-code",
                        technical_atom_kind="code-block",
                        payload={
                            "raw_code_text": "value => value + 1",
                            "language_tag": "javascript",
                        },
                        source_locator="alpha.pdf",
                        source_range_id="source-range-code",
                        context_text="Use this helper when mapping values.",
                        context_source_range_ids=("source-range-context",),
                    ),
                ),
            ),
        ),
        relationships=(ConceptRelationship("rel-1", "agrees-with", ("alpha", "beta"), ()),),
        support_ids=("pss-alpha", "pss-beta"),
    )
