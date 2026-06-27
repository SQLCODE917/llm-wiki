"""Deterministic text analysis for global ingest planning."""

from __future__ import annotations

import hashlib
import math
import re
from collections import Counter

from llmwiki.domain.bounded_text import paragraphs, sentence_fragments, text_windows
from llmwiki.domain.objects import (
    CandidateClaim,
    CandidateEntity,
    CandidateTopic,
    ClaimComparison,
    Evidence,
    ExtractedUnit,
    RawSource,
    SourceClaimGroup,
    TopicCluster,
    WikiMatch,
)
from llmwiki.domain.page_match_text import page_match_text
from llmwiki.domain.pages import slugify
from llmwiki.domain.planning_topic_index import (
    candidate_claim_ids_by_unit,
    source_claim_group_ids_by_unit,
)

_TOKEN_RE = re.compile(r"[a-z][a-z0-9-]{2,}")
_MATCH_THRESHOLD = 0.12
_EMBEDDING_TOKEN_LIMIT = 4096
_TOKEN_RESULT_LIMIT = 12000
_WIKI_MATCH_CANDIDATE_LIMIT = 80
_WIKI_MATCHES_PER_UNIT_LIMIT = 24
_CLAIM_PARAGRAPH_CHAR_LIMIT = 12_000
_CLAIM_SENTENCE_CHAR_LIMIT = 1_800
_CLAIMS_PER_UNIT_LIMIT = 120
_ENTITY_SCAN_CHAR_LIMIT = 12_000
_STOP_WORDS = frozenset(
    {
        "about",
        "after",
        "also",
        "and",
        "are",
        "because",
        "before",
        "book",
        "but",
        "can",
        "each",
        "from",
        "have",
        "into",
        "page",
        "pages",
        "raw",
        "source",
        "that",
        "the",
        "their",
        "this",
        "through",
        "use",
        "when",
        "where",
        "with",
    }
)


def build_extracted_unit(
    *,
    unit_id: str,
    raw_source: RawSource,
    locator: str,
    heading_path: str,
    text: str,
    extraction_status: str = "ok",
) -> ExtractedUnit:
    return ExtractedUnit(
        unit_id=unit_id,
        raw_source=raw_source,
        locator=locator,
        heading_path=heading_path,
        text=text,
        extraction_status=extraction_status,
        source_hash=hashlib.sha256(text.encode("utf-8")).hexdigest(),
    )


def candidate_claims(units: tuple[ExtractedUnit, ...]) -> tuple[CandidateClaim, ...]:
    claims: list[CandidateClaim] = []
    for unit in units:
        for index, statement in enumerate(_claim_sentences(unit.text), start=1):
            evidence = Evidence(
                raw_source=unit.raw_source,
                locator=f"{unit.locator} s.{index}".strip(),
                claim=statement,
            )
            claims.append(
                CandidateClaim(
                    claim_id=f"claim-{unit.unit_id}-{index:04d}",
                    statement=statement,
                    evidence=evidence,
                    confidence=min(1.0, 0.45 + len(tokens(statement)) / 120),
                )
            )
    return tuple(claims)


def candidate_topics(
    units: tuple[ExtractedUnit, ...], claims: tuple[CandidateClaim, ...]
) -> tuple[CandidateTopic, ...]:
    counts: Counter[str] = Counter()
    for unit in units:
        counts.update(tokens(f"{unit.heading_path} {unit.text}"))
    claim_terms = {claim.claim_id: frozenset(tokens(claim.statement)) for claim in claims}
    topics: list[CandidateTopic] = []
    for term, _ in counts.most_common(16):
        topic_claims = tuple(
            claim.claim_id for claim in claims if term in claim_terms[claim.claim_id]
        )
        topics.append(
            CandidateTopic(
                topic_id=f"topic-{term}",
                label=term,
                candidate_claims=topic_claims,
            )
        )
    return tuple(topics)


def candidate_entities(
    units: tuple[ExtractedUnit, ...], claims: tuple[CandidateClaim, ...]
) -> tuple[CandidateEntity, ...]:
    labels: Counter[str] = Counter()
    for unit in units:
        labels.update(
            re.findall(
                r"\b[A-Z][A-Za-z0-9]+(?:\s+[A-Z][A-Za-z0-9]+){0,2}\b",
                unit.text[:_ENTITY_SCAN_CHAR_LIMIT],
            )
        )
    return tuple(
        CandidateEntity(
            entity_id=f"entity-{slugify(label)}",
            label=label,
            candidate_claims=tuple(claim.claim_id for claim in claims if label in claim.statement),
        )
        for label, _ in labels.most_common(12)
    )


def topic_clusters(
    units: tuple[ExtractedUnit, ...],
    claims: tuple[CandidateClaim, ...],
    topics: tuple[CandidateTopic, ...],
    source_claim_groups: tuple[SourceClaimGroup, ...] = (),
) -> tuple[TopicCluster, ...]:
    grouped: dict[str, list[ExtractedUnit]] = {}
    for unit in units:
        label = (
            top_terms(f"{unit.heading_path} {unit.text}", 1)[0]
            if tokens(unit.text)
            else unit.heading_path
        )
        grouped.setdefault(label, []).append(unit)
    clusters: list[TopicCluster] = []
    claim_ids_by_unit = candidate_claim_ids_by_unit(units, claims)
    group_ids_by_unit = source_claim_group_ids_by_unit(source_claim_groups)
    for index, (label, cluster_units) in enumerate(sorted(grouped.items()), start=1):
        unit_ids = tuple(unit.unit_id for unit in cluster_units)
        clusters.append(
            TopicCluster(
                cluster_id=f"cluster-{index}",
                label=label,
                extracted_units=unit_ids,
                candidate_claims=tuple(
                    claim_id
                    for unit_id in unit_ids
                    for claim_id in claim_ids_by_unit.get(unit_id, ())
                ),
                candidate_topics=tuple(topic.topic_id for topic in topics if topic.label == label),
                source_claim_groups=tuple(
                    group_id
                    for unit_id in unit_ids
                    for group_id in group_ids_by_unit.get(unit_id, ())
                ),
            )
        )
    return tuple(clusters)


def wiki_matches(
    units: tuple[ExtractedUnit, ...],
    existing_pages: dict[str, str],
    source_locator: str,
) -> tuple[WikiMatch, ...]:
    match_texts = {page_id: page_match_text(text) for page_id, text in existing_pages.items()}
    page_terms = {
        page_id: frozenset(tokens(f"{page_id} {text}")) for page_id, text in match_texts.items()
    }
    matches: list[WikiMatch] = []
    for unit in units:
        unit_terms = frozenset(tokens(f"{unit.heading_path} {unit.text}"))
        unit_matches: list[WikiMatch] = []
        for page_id in _candidate_match_page_ids(
            unit, unit_terms, match_texts, page_terms, source_locator
        ):
            score = _lexical_match_score(unit_terms, page_terms[page_id])
            if source_locator in match_texts[page_id]:
                score += 0.15
            if score >= _MATCH_THRESHOLD:
                unit_matches.append(
                    WikiMatch(
                        page_id=page_id,
                        score=round(score, 6),
                        match_reason=f"nearest-neighbor:{unit.unit_id}",
                        page_excerpt=excerpt(match_texts[page_id]),
                    )
                )
        matches.extend(
            sorted(unit_matches, key=lambda match: (-match.score, match.page_id))[
                :_WIKI_MATCHES_PER_UNIT_LIMIT
            ]
        )
    return tuple(sorted(matches, key=lambda match: (-match.score, match.page_id)))


def claim_comparisons(
    claims: tuple[CandidateClaim, ...], matches: tuple[WikiMatch, ...]
) -> tuple[ClaimComparison, ...]:
    comparisons: list[ClaimComparison] = []
    match_embeddings = tuple((match, embedding(match.page_excerpt)) for match in matches[:3])
    for claim in claims:
        claim_embedding = embedding(claim.statement)
        for match, match_embedding in match_embeddings:
            if cosine(claim_embedding, match_embedding) > 0.2:
                comparisons.append(
                    ClaimComparison(claim.claim_id, match.page_excerpt, "overlap", match.page_id)
                )
                break
    return tuple(comparisons)


def same_section_identity(heading: str, page_id: str) -> bool:
    heading_slug = slugify(heading)
    page_slug = slugify(page_id)
    if not heading_slug or not page_slug:
        return False
    return (
        heading_slug == page_slug
        or page_slug.endswith(f"-{heading_slug}")
        or heading_slug.endswith(f"-{page_slug}")
    )


def unit_match(match: WikiMatch, unit_id: str) -> bool:
    return match.match_reason.endswith(f":{unit_id}")


def embedding(text: str) -> dict[str, float]:
    counts: dict[str, int] = {}
    for token in tokens(text, limit=_EMBEDDING_TOKEN_LIMIT):
        counts[token] = counts.get(token, 0) + 1
    total = 0.0
    for value in counts.values():
        total += value * value
    norm = math.sqrt(total)
    if not norm:
        return {}
    return {key: value / norm for key, value in counts.items()}


def cosine(a: dict[str, float], b: dict[str, float]) -> float:
    if not a or not b:
        return 0.0
    small, large = (a, b) if len(a) <= len(b) else (b, a)
    score = 0.0
    for key, value in small.items():
        score += value * large.get(key, 0.0)
    return score


def _candidate_match_page_ids(
    unit: ExtractedUnit,
    unit_terms: frozenset[str],
    match_texts: dict[str, str],
    page_terms: dict[str, frozenset[str]],
    source_locator: str,
) -> tuple[str, ...]:
    ranked: list[tuple[tuple[int, int, int], str]] = []
    for page_id, page_text in match_texts.items():
        rank = _candidate_match_rank(
            unit, unit_terms, page_id, page_text, page_terms[page_id], source_locator
        )
        if rank[0] > 0:
            ranked.append((rank, page_id))
    ranked.sort(key=lambda item: (-item[0][0], -item[0][1], -item[0][2], item[1]))
    return tuple(page_id for _, page_id in ranked[:_WIKI_MATCH_CANDIDATE_LIMIT])[
        :_WIKI_MATCH_CANDIDATE_LIMIT
    ]


def _candidate_match_rank(
    unit: ExtractedUnit,
    unit_terms: frozenset[str],
    page_id: str,
    page_text: str,
    terms: frozenset[str],
    source_locator: str,
) -> tuple[int, int, int]:
    source_affinity = int(source_locator in page_text)
    heading_affinity = int(same_section_identity(unit.heading_path, page_id))
    overlap = len(unit_terms & terms)
    return (source_affinity + heading_affinity + overlap, source_affinity, overlap)


def _lexical_match_score(unit_terms: frozenset[str], page_terms: frozenset[str]) -> float:
    if not unit_terms or not page_terms:
        return 0.0
    overlap = len(unit_terms & page_terms)
    if not overlap:
        return 0.0
    return overlap / math.sqrt(len(unit_terms) * len(page_terms))


def tokens(text: str, *, limit: int = _TOKEN_RESULT_LIMIT) -> tuple[str, ...]:
    result: list[str] = []
    for match in _TOKEN_RE.finditer(text.lower()):
        token = match.group(0)
        if token in _STOP_WORDS:
            continue
        result.append(token)
        if len(result) >= limit:
            break
    return tuple(result)


def top_terms(text: str, limit: int) -> tuple[str, ...]:
    return tuple(term for term, _ in Counter(tokens(text)).most_common(limit))


def excerpt(text: str) -> str:
    body = text.split("---", 2)[-1] if text.startswith("---") else text
    cleaned = " ".join(body.split())
    return cleaned if len(cleaned) <= 240 else cleaned[:239].rstrip() + "..."


def _claim_sentences(text: str) -> tuple[str, ...]:
    sentences: list[str] = []
    for paragraph in paragraphs(text, _CLAIM_PARAGRAPH_CHAR_LIMIT):
        for sentence in sentence_fragments(paragraph):
            for fragment in text_windows(sentence, _CLAIM_SENTENCE_CHAR_LIMIT):
                normalized = " ".join(fragment.split()).strip()
                if len(tokens(normalized)) >= 3:
                    sentences.append(normalized)
                    if len(sentences) >= _CLAIMS_PER_UNIT_LIMIT:
                        return tuple(sentences)
    return tuple(sentences)
