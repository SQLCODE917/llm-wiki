"""Build publication candidates from existing ledger page planning signals."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.collection_pages import CollectionPlan
from llmwiki.domain.ledger.knowledge_shapes import KnowledgeShapeCatalog
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.page_publication import (
    PAGE_FAMILY_COLLECTION_PAGE,
    PAGE_FAMILY_PROCEDURE_GUIDE,
    PAGE_FAMILY_RECIPE_PATTERN,
    PAGE_FAMILY_SECTION_REFERENCE,
    PageCandidate,
)
from llmwiki.domain.ledger.page_title_lint import lint_page_title
from llmwiki.domain.ledger.procedures import ProcedureGuide, plan_procedure_guides
from llmwiki.domain.ledger.projection_context import ProjectionContext
from llmwiki.domain.ledger.projection_policy import topic_projection_policy
from llmwiki.domain.ledger.recipe_pages import RecipePattern, plan_recipe_patterns
from llmwiki.domain.ledger.section_navigation import section_page_id
from llmwiki.domain.ledger.section_planning import SectionGroundedPlan
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.topic_models import SourceTopic
from llmwiki.domain.pages import slugify
from llmwiki.runtime.ledger_synthesis_pages import collection_plans_for_source


@dataclass(frozen=True)
class PublicationCandidateInputs:
    candidates: tuple[PageCandidate, ...]
    procedure_guides: tuple[ProcedureGuide, ...]
    collection_plans: tuple[CollectionPlan, ...]
    recipe_patterns: tuple[RecipePattern, ...]


def build_publication_candidate_inputs(
    *,
    ledger: ClaimLedger,
    structure: DocumentStructure,
    section_plan: SectionGroundedPlan,
    shape_catalog: KnowledgeShapeCatalog,
    projection_context: ProjectionContext,
    topics: tuple[SourceTopic, ...],
    source_page_id: str,
    source_profile_kind: str,
) -> PublicationCandidateInputs:
    procedure_guides = plan_procedure_guides(
        ledger, structure, source_page_id=source_page_id, shape_catalog=shape_catalog
    )
    collection_plans = collection_plans_for_source(
        ledger, structure, source_page_id, shape_catalog
    )
    recipe_patterns = plan_recipe_patterns(ledger, structure, source_page_id, shape_catalog)
    return PublicationCandidateInputs(
        candidates=(
            *_topic_candidates(
                ledger,
                structure,
                projection_context,
                topics,
                source_page_id,
                source_profile_kind,
            ),
            *_procedure_candidates(ledger, procedure_guides, source_page_id, source_profile_kind),
            *_collection_candidates(
                ledger,
                structure,
                collection_plans,
                source_page_id,
                source_profile_kind,
            ),
            *_recipe_candidates(ledger, recipe_patterns, source_page_id, source_profile_kind),
            *_section_candidates(
                ledger,
                structure,
                section_plan,
                source_page_id,
                source_profile_kind,
            ),
        ),
        procedure_guides=procedure_guides,
        collection_plans=collection_plans,
        recipe_patterns=recipe_patterns,
    )


def _candidate(
    *,
    ledger: ClaimLedger,
    source_page_id: str,
    source_profile_kind: str,
    page_id: str,
    title: str,
    page_kind: str,
    page_family: str,
    origin: str,
    rank_score: float,
    source_order: int,
) -> PageCandidate:
    return PageCandidate(
        page_candidate_id=deterministic_id("page-candidate", ledger.source_hash, page_id, origin),
        source_id=source_page_id,
        source_hash=ledger.source_hash,
        source_profile_kind=source_profile_kind,
        page_id=page_id,
        title=title,
        page_kind=page_kind,
        page_family=page_family,
        origin=origin,
        rank_score=rank_score,
        source_order=source_order,
        title_findings=lint_page_title(title, page_id, page_family),
    )


def _topic_candidates(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    projection_context: ProjectionContext,
    topics: tuple[SourceTopic, ...],
    source_page_id: str,
    source_profile_kind: str,
) -> tuple[PageCandidate, ...]:
    candidates: list[PageCandidate] = []
    for topic in topics:
        page_id = slugify(f"{source_page_id}-{topic.topic_key}")
        policy = topic_projection_policy(topic, ledger, projection_context)
        candidates.append(
            _candidate(
                ledger=ledger,
                source_page_id=source_page_id,
                source_profile_kind=source_profile_kind,
                page_id=page_id,
                title=topic.label,
                page_kind=topic.page_kind,
                page_family=policy.page_family,
                origin="topic-plan",
                rank_score=topic.salience + len(topic.entry_ids) + len(topic.atom_ids),
                source_order=_topic_order(ledger, structure, topic),
            )
        )
    return tuple(candidates)


def _procedure_candidates(
    ledger: ClaimLedger,
    guides: tuple[ProcedureGuide, ...],
    source_page_id: str,
    source_profile_kind: str,
) -> tuple[PageCandidate, ...]:
    return tuple(
        _candidate(
            ledger=ledger,
            source_page_id=source_page_id,
            source_profile_kind=source_profile_kind,
            page_id=guide.procedure_id,
            title=guide.title,
            page_kind="procedure",
            page_family=PAGE_FAMILY_PROCEDURE_GUIDE,
            origin="procedure-plan",
            rank_score=len(guide.steps) + len(guide.technical_atoms),
            source_order=guide.source_node.source_order,
        )
        for guide in guides
    )


def _collection_candidates(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    collections: tuple[CollectionPlan, ...],
    source_page_id: str,
    source_profile_kind: str,
) -> tuple[PageCandidate, ...]:
    return tuple(
        _candidate(
            ledger=ledger,
            source_page_id=source_page_id,
            source_profile_kind=source_profile_kind,
            page_id=plan.collection_page_id,
            title=plan.title,
            page_kind="source",
            page_family=PAGE_FAMILY_COLLECTION_PAGE,
            origin="collection-plan",
            rank_score=len(plan.members),
            source_order=_node_order(structure, plan.source_node_id),
        )
        for plan in collections
    )


def _recipe_candidates(
    ledger: ClaimLedger,
    recipes: tuple[RecipePattern, ...],
    source_page_id: str,
    source_profile_kind: str,
) -> tuple[PageCandidate, ...]:
    return tuple(
        _candidate(
            ledger=ledger,
            source_page_id=source_page_id,
            source_profile_kind=source_profile_kind,
            page_id=recipe.recipe_id,
            title=recipe.title,
            page_kind="recipe",
            page_family=PAGE_FAMILY_RECIPE_PATTERN,
            origin="recipe-plan",
            rank_score=len(recipe.claims) + len(recipe.technical_atoms),
            source_order=recipe.source_node.source_order,
        )
        for recipe in recipes
    )


def _section_candidates(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    section_plan: SectionGroundedPlan,
    source_page_id: str,
    source_profile_kind: str,
) -> tuple[PageCandidate, ...]:
    candidates: list[PageCandidate] = []
    for target in section_plan.page_targets:
        node = structure.node(target.structure_node_id)
        if node is None:
            continue
        candidates.append(
            _candidate(
                ledger=ledger,
                source_page_id=source_page_id,
                source_profile_kind=source_profile_kind,
                page_id=section_page_id(source_page_id, structure, node),
                title=target.label,
                page_kind="source",
                page_family=PAGE_FAMILY_SECTION_REFERENCE,
                origin="section-plan",
                rank_score=len(target.entry_ids) + len(target.atom_ids),
                source_order=node.source_order,
            )
        )
    return tuple(candidates)


def _topic_order(ledger: ClaimLedger, structure: DocumentStructure, topic: SourceTopic) -> int:
    orders: list[int] = []
    for entry_id in topic.entry_ids:
        entry = ledger.entry(entry_id)
        if entry is not None and entry.structure_node_ids:
            orders.append(_node_order(structure, entry.structure_node_ids[0]))
    return min(orders) if orders else 0


def _node_order(structure: DocumentStructure, node_id: str) -> int:
    node = structure.node(node_id)
    return node.source_order if node is not None else 0
