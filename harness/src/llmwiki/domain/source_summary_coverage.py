"""Coverage repair for source-summary drafts."""

from __future__ import annotations

from llmwiki.domain.objects import (
    SourceSummaryBullet,
    SourceSummaryClaimRequirement,
    SourceSummaryDraft,
    SourceSummaryPlan,
)
from llmwiki.domain.planning_analysis import tokens


def infer_source_summary_coverage(
    draft: SourceSummaryDraft, plan: SourceSummaryPlan
) -> SourceSummaryDraft:
    """Attach missing selected claim IDs when a bullet clearly matches their cues."""

    if not draft.claim_bullets or not plan.selected_claim_requirements:
        return draft
    covered = {
        claim_id for bullet in draft.claim_bullets for claim_id in bullet.covered_source_claims
    }
    missing = tuple(claim_id for claim_id in plan.selected_source_claims if claim_id not in covered)
    if not missing:
        return draft
    requirements = {
        requirement.source_claim_id: requirement for requirement in plan.selected_claim_requirements
    }
    inferred = [list(bullet.covered_source_claims) for bullet in draft.claim_bullets]
    for claim_id in missing:
        requirement = requirements.get(claim_id)
        if requirement is None:
            continue
        bullet_index = _best_matching_bullet(requirement, draft.claim_bullets)
        if bullet_index is not None:
            inferred[bullet_index].append(claim_id)
    return SourceSummaryDraft(
        source_record_text=draft.source_record_text,
        claim_bullets=tuple(
            SourceSummaryBullet(
                bullet_text=bullet.bullet_text,
                covered_source_claims=tuple(dict.fromkeys(inferred[index])),
            )
            for index, bullet in enumerate(draft.claim_bullets)
        ),
    )


def _best_matching_bullet(
    requirement: SourceSummaryClaimRequirement,
    bullets: tuple[SourceSummaryBullet, ...],
) -> int | None:
    required_terms = _term_variants(tokens(" ".join(requirement.cue_terms)))
    if not required_terms:
        return None
    threshold = min(2, len(required_terms))
    scores = tuple(
        (index, len(required_terms & _term_variants(tokens(bullet.bullet_text))))
        for index, bullet in enumerate(bullets)
    )
    best_index, best_score = max(scores, key=lambda item: item[1])
    return best_index if best_score >= threshold else None


def _term_variants(items: tuple[str, ...]) -> frozenset[str]:
    variants: set[str] = set(items)
    for item in items:
        if len(item) > 3 and item.endswith("s"):
            variants.add(item[:-1])
        if len(item) > 5 and item.endswith("ing"):
            variants.add(item[:-3])
    return frozenset(variants)
