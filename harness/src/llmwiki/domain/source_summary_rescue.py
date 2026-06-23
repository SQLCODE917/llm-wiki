"""Mechanical rescue for source-summary drafts."""

from __future__ import annotations

import re

from llmwiki.domain.citations import parse_citations
from llmwiki.domain.objects import (
    SourceSummaryBullet,
    SourceSummaryDraft,
    SourceSummaryPlan,
)
from llmwiki.domain.source_summary_citations import (
    normalized_citation_text,
    source_summary_bullet_cites_required_locator,
)

_PAGE_ONLY_CITATION_RE = re.compile(r"\(p\.\s*(?P<start>\d+)(?:\s*-\s*(?P<end>\d+))?\)")


def repair_source_summary_draft(
    draft: SourceSummaryDraft,
    plan: SourceSummaryPlan,
    *,
    max_claim_bullets: int = 0,
) -> SourceSummaryDraft:
    needs_shape_rescue = _has_unknown_coverage(draft, plan) or _has_page_only_citation(draft)
    repaired = _discard_unknown_coverage(draft, plan)
    repaired = _merge_duplicate_coverage_bullets(repaired, max_claim_bullets)
    if needs_shape_rescue and max_claim_bullets > 0:
        repaired = _limit_claim_bullets(repaired, max_claim_bullets)
    repaired = _expand_page_only_citations(repaired, plan)
    repaired = _ensure_required_bullet_citations(repaired, plan)
    return _ensure_required_source_record_citations(repaired, plan)


def _has_unknown_coverage(draft: SourceSummaryDraft, plan: SourceSummaryPlan) -> bool:
    selected = frozenset(plan.selected_source_claims)
    if not selected:
        return False
    return any(
        claim_id not in selected
        for bullet in draft.claim_bullets
        for claim_id in bullet.covered_source_claims
    )


def _has_page_only_citation(draft: SourceSummaryDraft) -> bool:
    return any(_PAGE_ONLY_CITATION_RE.search(bullet.bullet_text) for bullet in draft.claim_bullets)


def _discard_unknown_coverage(
    draft: SourceSummaryDraft, plan: SourceSummaryPlan
) -> SourceSummaryDraft:
    selected = frozenset(plan.selected_source_claims)
    if not selected:
        return draft
    return SourceSummaryDraft(
        source_record_text=draft.source_record_text,
        claim_bullets=tuple(
            SourceSummaryBullet(
                bullet_text=bullet.bullet_text,
                covered_source_claims=tuple(
                    claim_id for claim_id in bullet.covered_source_claims if claim_id in selected
                ),
            )
            for bullet in draft.claim_bullets
        ),
    )


def _limit_claim_bullets(draft: SourceSummaryDraft, max_claim_bullets: int) -> SourceSummaryDraft:
    if len(draft.claim_bullets) <= max_claim_bullets:
        return draft
    return SourceSummaryDraft(
        source_record_text=draft.source_record_text,
        claim_bullets=draft.claim_bullets[:max_claim_bullets],
    )


def _merge_duplicate_coverage_bullets(
    draft: SourceSummaryDraft, max_claim_bullets: int
) -> SourceSummaryDraft:
    if max_claim_bullets <= 0 or len(draft.claim_bullets) <= max_claim_bullets:
        return draft
    bullets = list(draft.claim_bullets)
    while len(bullets) > max_claim_bullets:
        duplicate = _first_duplicate_coverage_pair(bullets)
        if duplicate is None:
            break
        target_index, duplicate_index = duplicate
        target = bullets[target_index]
        extra = bullets.pop(duplicate_index)
        bullets[target_index] = SourceSummaryBullet(
            bullet_text=_merge_bullet_text(target.bullet_text, extra.bullet_text),
            covered_source_claims=target.covered_source_claims,
        )
    return SourceSummaryDraft(
        source_record_text=draft.source_record_text,
        claim_bullets=tuple(bullets),
    )


def _first_duplicate_coverage_pair(
    bullets: list[SourceSummaryBullet],
) -> tuple[int, int] | None:
    seen: dict[tuple[str, ...], int] = {}
    for index, bullet in enumerate(bullets):
        coverage_key = tuple(sorted(bullet.covered_source_claims))
        if not coverage_key:
            continue
        if coverage_key in seen:
            return seen[coverage_key], index
        seen[coverage_key] = index
    return None


def _merge_bullet_text(left: str, right: str) -> str:
    left_text = left.strip()
    right_text = right.strip()
    if not left_text:
        return right_text
    if not right_text or right_text == left_text:
        return left_text
    return f"{left_text.rstrip('.')}; {right_text}"


def _expand_page_only_citations(
    draft: SourceSummaryDraft, plan: SourceSummaryPlan
) -> SourceSummaryDraft:
    required = _single_required_page_citation(plan)
    if required is None:
        return draft
    source_path, required_range = required
    return SourceSummaryDraft(
        source_record_text=draft.source_record_text,
        claim_bullets=tuple(
            SourceSummaryBullet(
                bullet_text=_expand_page_only_citation(
                    bullet.bullet_text, source_path, required_range
                ),
                covered_source_claims=bullet.covered_source_claims,
            )
            for bullet in draft.claim_bullets
        ),
    )


def _ensure_required_source_record_citations(
    draft: SourceSummaryDraft, plan: SourceSummaryPlan
) -> SourceSummaryDraft:
    rendered = normalized_citation_text(
        " ".join(
            (draft.source_record_text,)
            + tuple(bullet.bullet_text for bullet in draft.claim_bullets)
        )
    )
    missing = tuple(
        citation
        for citation in plan.required_source_citations
        if normalized_citation_text(citation) not in rendered
    )
    if not missing:
        return draft
    suffix = " ".join(f"({citation})" for citation in missing)
    return SourceSummaryDraft(
        source_record_text=f"{draft.source_record_text.strip()} {suffix}".strip(),
        claim_bullets=draft.claim_bullets,
    )


def _ensure_required_bullet_citations(
    draft: SourceSummaryDraft, plan: SourceSummaryPlan
) -> SourceSummaryDraft:
    if len(plan.required_source_citations) != 1:
        return draft
    required = plan.required_source_citations[0]
    return SourceSummaryDraft(
        source_record_text=draft.source_record_text,
        claim_bullets=tuple(
            SourceSummaryBullet(
                bullet_text=_with_required_citation(bullet.bullet_text, required),
                covered_source_claims=bullet.covered_source_claims,
            )
            for bullet in draft.claim_bullets
        ),
    )


def _with_required_citation(text: str, required_citation: str) -> str:
    if source_summary_bullet_cites_required_locator(text, (required_citation,)):
        return text
    return f"{text.strip().rstrip('.')} ({required_citation})"


def _single_required_page_citation(
    plan: SourceSummaryPlan,
) -> tuple[str, tuple[int, int]] | None:
    parsed = tuple(
        citation
        for required in plan.required_source_citations
        for citation in parse_citations("source-summary-requirement", required).citations
    )
    if len(parsed) != 1 or parsed[0].page_range is None:
        return None
    return parsed[0].source_path, parsed[0].page_range


def _expand_page_only_citation(
    text: str, source_path: str, required_range: tuple[int, int]
) -> str:
    def replace(match: re.Match[str]) -> str:
        start = int(match.group("start"))
        end_text = match.group("end")
        end = int(end_text) if end_text is not None else start
        if not _contains(required_range, (start, end)):
            return match.group(0)
        locator = f"p.{start}" if start == end else f"p.{start}-{end}"
        return f"({source_path} {locator})"

    return _PAGE_ONLY_CITATION_RE.sub(replace, text)


def _contains(required_range: tuple[int, int], candidate_range: tuple[int, int]) -> bool:
    required_start, required_end = required_range
    candidate_start, candidate_end = candidate_range
    return required_start <= candidate_start <= candidate_end <= required_end
