"""Deterministic SourceClaim extraction and source-summary planning."""

from __future__ import annotations

import re

from llmwiki.domain.objects import (
    Evidence,
    ExtractedUnit,
    Schema,
    SourceClaim,
    SourceClaimGroup,
    SourceSummaryPlan,
)
from llmwiki.domain.page_body_contracts import ResolvedPageBodyContract
from llmwiki.domain.pages import slugify
from llmwiki.domain.planning_analysis import tokens, top_terms

_SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")
_SKILL_REFERENCE_RE = re.compile(r"\b([a-z][a-z0-9-]*)\s+skills?\b", re.IGNORECASE)
_CLASS_OR_PROFESSION_REFERENCE_RE = re.compile(
    r"\b([a-z][a-z0-9-]*)s?\s+(?:is|are)\s+(?:an?\s+)?(?:[a-z0-9-]+\s+){0,4}"
    r"(?:class|profession)\b",
    re.IGNORECASE,
)
_MAX_SOURCE_SUMMARY_CLAIMS = 5
_EARLY_CLAIM_WINDOW = 20
_TOPIC_FOCUS_GAP = 3
_PAGE_TERM_STOPWORDS = frozenset(
    {
        "basic",
        "chapter",
        "complete",
        "edition",
        "for",
        "list",
        "part",
        "rpg",
        "rule",
        "rules",
        "section",
        "skill",
        "skills",
        "source",
        "sword",
        "world",
    }
)
_GENERIC_PAGE_MATCH_TERMS = frozenset(
    {
        "check",
        "checks",
        "chapter",
        "complete",
        "edition",
        "how",
        "list",
        "magic",
        "magical",
        "part",
        "rule",
        "rules",
        "section",
        "source",
        "sword",
        "type",
        "types",
        "world",
    }
)

_ROLE_PATTERNS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("uncertainty", (r"\bmay\b", r"\bmight\b", r"\bpossible\b", r"\bsuggest\w*\b", r"\bunknown\b")),
    (
        "negative-evidence",
        (r"\bno\b.+\bfound\b", r"\bnot\b.+\bfound\b", r"\bdoes not\b", r"\bwithout\b"),
    ),
    ("limitation", (r"\blimit\w*\b", r"\bunless\b", r"\bexcept\b", r"\bonly\b", r"\bcannot\b")),
    ("method", (r"\bused\b", r"\busing\b", r"\bstudy\b", r"\banalys\w*\b", r"\btest\w*\b")),
    ("evidence", (r"\bevidence\b", r"\binscription\w*\b", r"\bcitation\b", r"\brecord\b")),
    ("provenance", (r"\bfrom\b", r"\borigin\w*\b", r"\bretrieved\b", r"\bdiscovered\b")),
    ("temporal", (r"\b\d{3,4}\b", r"\bbc\b", r"\bad\b", r"\byear\b", r"\bcentur\w*\b")),
    ("quantitative", (r"\b\d+\b", r"\bat least\b", r"\bmore than\b", r"\broughly\b")),
    (
        "function",
        (r"\btrack\w*\b", r"\bpredict\w*\b", r"\badvance\b", r"\bshow\w*\b", r"\bcould\b"),
    ),
    ("mechanism", (r"\bconsists\b", r"\bgear\w*\b", r"\bcase\b", r"\bcrank\b", r"\bthrough\b")),
    ("comparison", (r"\bmatched\b", r"\bsurpass\w*\b", r"\bcompared\b", r"\bthan\b")),
    ("relationship", (r"\blink\w*\b", r"\bconnect\w*\b", r"\bbetween\b", r"\bwith\b")),
    ("requirement", (r"\bmust\b", r"\brequire\w*\b", r"\bshall\b", r"\bshould\b")),
    ("procedure", (r"\bturn\w*\b", r"\bstep\b", r"\bprocess\b", r"\bworkflow\b")),
    ("definition", (r"\bdefined as\b", r"\bmeans\b", r"\brefers to\b")),
    ("identity", (r"\bis\b", r"\bare\b", r"\bknown as\b", r"\bdescribed as\b")),
    ("attribute", (r"\bhas\b", r"\bhave\b", r"\bcontains\b", r"\bhoused\b", r"\bsize\b")),
    ("open-question", (r"\bopen question\b", r"\bunclear\b", r"\bunresolved\b")),
)

_ROLE_WEIGHTS = {
    "uncertainty": 0.33,
    "negative-evidence": 0.34,
    "limitation": 0.31,
    "method": 0.27,
    "function": 0.30,
    "mechanism": 0.25,
    "provenance": 0.22,
    "temporal": 0.18,
    "identity": 0.22,
    "definition": 0.22,
    "comparison": 0.20,
    "evidence": 0.20,
    "quantitative": 0.16,
}


def source_claims(
    units: tuple[ExtractedUnit, ...],
    schema: Schema,
) -> tuple[SourceClaim, ...]:
    claims: list[SourceClaim] = []
    allowed_roles = {role.tag_name for role in schema.claim_role_tags}
    for unit in units:
        for index, statement in enumerate(_claim_sentences(unit.text), start=1):
            role_tags = tuple(role for role in _claim_role_tags(statement) if role in allowed_roles)
            evidence = Evidence(
                raw_source=unit.raw_source,
                locator=f"{unit.locator} s.{index}".strip(),
                claim=statement,
            )
            claims.append(
                SourceClaim(
                    source_claim_id=f"source-claim-{unit.unit_id}-{index:04d}",
                    statement=statement,
                    evidence=evidence,
                    extracted_unit_id=unit.unit_id,
                    source_span=evidence.locator,
                    claim_role_tags=role_tags,
                    claim_salience=_claim_salience(statement, role_tags),
                    claim_certainty=_claim_certainty(role_tags),
                    subject_terms=top_terms(statement, 4),
                )
            )
    return tuple(claims)


def source_claim_groups(
    claims: tuple[SourceClaim, ...],
) -> tuple[SourceClaimGroup, ...]:
    grouped: dict[str, list[SourceClaim]] = {}
    for claim in claims:
        grouped.setdefault(_primary_claim_group_label(claim), []).append(claim)
    result: list[SourceClaimGroup] = []
    for label, label_claims in grouped.items():
        roles = tuple(sorted({role for claim in label_claims for role in claim.claim_role_tags}))
        units = tuple(dict.fromkeys(claim.extracted_unit_id for claim in label_claims))
        result.append(
            SourceClaimGroup(
                source_claim_group_id=f"source-claim-group-{slugify(label)}",
                label=label,
                source_claims=tuple(claim.source_claim_id for claim in label_claims),
                extracted_units=units,
                claim_role_tags=roles,
                claim_salience=round(max(claim.claim_salience for claim in label_claims), 3),
            )
        )
    return tuple(sorted(result, key=lambda group: (-group.claim_salience, group.label)))


def source_summary_plan(
    *,
    page_id: str,
    contract: ResolvedPageBodyContract,
    claims: tuple[SourceClaim, ...],
    groups: tuple[SourceClaimGroup, ...],
) -> SourceSummaryPlan | None:
    if contract.contract_id != "source-summary" or not claims:
        return None
    claims_by_id = {claim.source_claim_id: claim for claim in claims}
    page_terms = _page_terms(page_id)
    min_claims = min(contract.min_claim_bullets or 3, len(claims))
    candidate_claims = _topic_focused_claims(page_terms, claims, min_claims)
    candidate_claim_ids = {claim.source_claim_id for claim in candidate_claims}
    selected: list[SourceClaim] = []
    first_relevant_position = _first_relevant_claim_position(page_terms, candidate_claims)

    def has_unselected_relevant_claims() -> bool:
        return any(
            claim not in selected and _page_overlap(page_terms, claim) > 0
            for claim in candidate_claims
        )

    def add_role_claim(*roles: str) -> None:
        candidates = [
            claim
            for claim in candidate_claims
            if any(role in claim.claim_role_tags for role in roles) and claim not in selected
        ]
        candidates = _without_competing_section_claims(page_terms, candidates)
        relevant_candidates = [
            claim for claim in candidates if _page_overlap(page_terms, claim) > 0
        ]
        if relevant_candidates:
            candidates = relevant_candidates
        elif page_terms:
            if has_unselected_relevant_claims():
                return
            early_candidates = [
                claim
                for claim in candidates
                if _claim_position(claim) <= _EARLY_CLAIM_WINDOW
                and _after_first_relevant_claim(first_relevant_position, claim)
            ]
            if not early_candidates:
                return
            candidates = early_candidates
        if candidates and len(selected) < _MAX_SOURCE_SUMMARY_CLAIMS:
            selected.append(max(candidates, key=lambda claim: _selection_score(page_terms, claim)))

    add_role_claim("identity", "definition")
    add_role_claim("function", "mechanism", "procedure", "requirement")
    add_role_claim("limitation")
    add_role_claim("negative-evidence")
    add_role_claim("uncertainty", "open-question")

    for group in groups:
        if len(selected) >= _MAX_SOURCE_SUMMARY_CLAIMS:
            break
        if any(claim.source_claim_id in group.source_claims for claim in selected):
            continue
        group_claims = [
            claims_by_id[claim_id]
            for claim_id in group.source_claims
            if claim_id in claims_by_id and claim_id in candidate_claim_ids
        ]
        group_claims = _without_competing_section_claims(page_terms, group_claims)
        if group_claims:
            relevant_group_claims = [
                claim for claim in group_claims if _page_overlap(page_terms, claim) > 0
            ]
            if relevant_group_claims:
                group_claims = relevant_group_claims
            elif page_terms:
                if has_unselected_relevant_claims():
                    continue
                if len(selected) >= min_claims:
                    continue
                early_group_claims = [
                    claim
                    for claim in group_claims
                    if _claim_position(claim) <= _EARLY_CLAIM_WINDOW
                    and _after_first_relevant_claim(first_relevant_position, claim)
                ]
                if not early_group_claims:
                    continue
                group_claims = early_group_claims
            selected.append(
                max(group_claims, key=lambda claim: _selection_score(page_terms, claim))
            )

    for claim in sorted(
        _without_competing_section_claims(page_terms, list(candidate_claims)),
        key=lambda claim: _selection_score(page_terms, claim),
        reverse=True,
    ):
        target_size = max(min_claims, min(_MAX_SOURCE_SUMMARY_CLAIMS, len(candidate_claims)))
        if len(selected) >= target_size:
            break
        if (
            page_terms
            and len(selected) >= min_claims
            and _page_overlap(page_terms, claim) == 0
        ):
            continue
        if (
            page_terms
            and _page_overlap(page_terms, claim) == 0
            and has_unselected_relevant_claims()
        ):
            continue
        if claim not in selected:
            selected.append(claim)

    selected_ids = tuple(claim.source_claim_id for claim in selected[:_MAX_SOURCE_SUMMARY_CLAIMS])
    selected_roles = tuple(sorted({role for claim in selected for role in claim.claim_role_tags}))
    selected_groups = tuple(
        group.source_claim_group_id
        for group in groups
        if any(claim_id in group.source_claims for claim_id in selected_ids)
    )
    return SourceSummaryPlan(
        source_summary_plan_id=f"source-summary-plan-{page_id}",
        page_id=page_id,
        selected_source_claims=selected_ids,
        required_claim_role_tags=selected_roles,
        required_source_claim_groups=selected_groups,
        required_source_citations=contract.required_source_citations,
        coverage_policy=contract.coverage_policy,
    )


def _claim_sentences(text: str) -> tuple[str, ...]:
    paragraphs: list[str] = []
    current_lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            if current_lines:
                paragraphs.append(" ".join(current_lines))
                current_lines = []
            continue
        current_lines.append(stripped)
    if current_lines:
        paragraphs.append(" ".join(current_lines))
    sentences: list[str] = []
    for paragraph in paragraphs:
        for sentence in _SENTENCE_RE.split(paragraph):
            normalized = " ".join(sentence.split()).strip()
            if len(tokens(normalized)) >= 3:
                sentences.append(normalized)
    return tuple(sentences)


def _claim_role_tags(statement: str) -> tuple[str, ...]:
    lowered = statement.lower()
    roles = [
        role
        for role, patterns in _ROLE_PATTERNS
        if any(re.search(pattern, lowered) for pattern in patterns)
    ]
    return tuple(dict.fromkeys(roles))


def _claim_salience(statement: str, role_tags: tuple[str, ...]) -> float:
    role_score = max((_ROLE_WEIGHTS.get(role, 0.12) for role in role_tags), default=0.08)
    length_score = min(len(tokens(statement)) / 80, 0.18)
    return round(min(1.0, 0.38 + role_score + length_score), 3)


def _claim_certainty(role_tags: tuple[str, ...]) -> str:
    if "uncertainty" in role_tags:
        return "uncertain"
    if "negative-evidence" in role_tags:
        return "negative-evidence"
    return "supported"


def _selection_score(page_terms: frozenset[str], claim: SourceClaim) -> float:
    relevance = min(_page_overlap(page_terms, claim) * 0.12, 0.36)
    return claim.claim_salience + relevance - min(_claim_position(claim) * 0.008, 0.65)


def _page_overlap(page_terms: frozenset[str], claim: SourceClaim) -> int:
    if not page_terms:
        return 0
    claim_terms = _term_variants(tuple(tokens(claim.statement)))
    specific_page_terms = page_terms - _GENERIC_PAGE_MATCH_TERMS
    specific_overlap = specific_page_terms & claim_terms
    if specific_overlap:
        return len(specific_overlap)
    if specific_page_terms:
        return 0
    return len(page_terms & claim_terms)


def _topic_focused_claims(
    page_terms: frozenset[str],
    claims: tuple[SourceClaim, ...],
    min_claims: int,
) -> tuple[SourceClaim, ...]:
    if not page_terms or len(claims) <= _EARLY_CLAIM_WINDOW:
        return claims
    start_index = next(
        (index for index, claim in enumerate(claims) if _page_overlap(page_terms, claim) > 0),
        None,
    )
    if start_index is None:
        return claims
    focused: list[SourceClaim] = []
    gap = 0
    for claim in claims[start_index:]:
        if _page_overlap(page_terms, claim) > 0:
            gap = 0
        else:
            gap += 1
            if gap > _TOPIC_FOCUS_GAP:
                break
        focused.append(claim)
    if len(focused) < min_claims:
        return claims
    return tuple(focused)


def _first_relevant_claim_position(
    page_terms: frozenset[str],
    claims: tuple[SourceClaim, ...],
) -> int:
    positions = tuple(
        _claim_position(claim) for claim in claims if _page_overlap(page_terms, claim)
    )
    return min(positions) if positions else 0


def _after_first_relevant_claim(first_relevant_position: int, claim: SourceClaim) -> bool:
    return not first_relevant_position or _claim_position(claim) >= first_relevant_position


def _without_competing_section_claims(
    page_terms: frozenset[str],
    claims: list[SourceClaim],
) -> list[SourceClaim]:
    if not page_terms:
        return claims
    return [
        claim
        for claim in claims
        if not _has_competing_section_reference(page_terms, claim.statement)
    ]


def _has_competing_section_reference(page_terms: frozenset[str], statement: str) -> bool:
    for match in _SKILL_REFERENCE_RE.finditer(statement):
        skill_terms = _term_variants((match.group(1).lower(),))
        if page_terms.isdisjoint(skill_terms):
            return True
    for match in _CLASS_OR_PROFESSION_REFERENCE_RE.finditer(statement):
        section_terms = _term_variants((match.group(1).lower(),))
        if page_terms.isdisjoint(section_terms):
            return True
    return False


def _page_terms(page_id: str) -> frozenset[str]:
    parts = page_id.split("-")
    for index in range(len(parts) - 1):
        if parts[index].isdigit() and parts[index + 1].isdigit():
            return _specific_page_terms(_page_title_tokens(tuple(parts[index + 2 :])))
    return _specific_page_terms(_page_title_tokens(tuple(parts)))


def _page_title_tokens(parts: tuple[str, ...]) -> tuple[str, ...]:
    title_tokens = tuple(tokens(" ".join(parts)))
    if "magic" in parts and {"use", "using", "cast", "casting", "casts"} & set(parts):
        return title_tokens + ("cast", "casting")
    return title_tokens


def _specific_page_terms(page_terms: tuple[str, ...]) -> frozenset[str]:
    specific = tuple(term for term in page_terms if term not in _PAGE_TERM_STOPWORDS)
    return _term_variants(specific or page_terms)


def _term_variants(terms: tuple[str, ...]) -> frozenset[str]:
    variants: set[str] = set(terms)
    for term in terms:
        if len(term) > 3 and term.endswith("s"):
            variants.add(term[:-1])
        if len(term) > 5 and term.endswith("ing"):
            stem = term[:-3]
            if len(stem) >= 4:
                variants.add(stem)
        if term == "throwing":
            variants.add("thrown")
    return frozenset(variants)


def _claim_position(claim: SourceClaim) -> int:
    match = re.search(r"-(\d{4})$", claim.source_claim_id)
    if match is None:
        return 0
    return int(match.group(1))


def _primary_claim_group_label(claim: SourceClaim) -> str:
    for role in (
        "uncertainty",
        "negative-evidence",
        "limitation",
        "function",
        "mechanism",
        "method",
        "provenance",
        "identity",
        "temporal",
        "requirement",
        "procedure",
    ):
        if role in claim.claim_role_tags:
            return role
    return claim.subject_terms[0] if claim.subject_terms else "general"
