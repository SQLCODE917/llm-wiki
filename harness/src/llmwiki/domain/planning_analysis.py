"""Deterministic text analysis for global ingest planning."""

from __future__ import annotations

import hashlib
import math
import re
from collections import Counter

from llmwiki.domain.objects import (
    CandidateClaim,
    CandidateEntity,
    CandidateTopic,
    ClaimComparison,
    Evidence,
    ExtractedUnit,
    RawSource,
    TopicCluster,
    WikiMatch,
)
from llmwiki.domain.pages import slugify

_TOKEN_RE = re.compile(r"[a-z][a-z0-9-]{2,}")
_SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")
_MATCH_THRESHOLD = 0.12
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
    return tuple(
        CandidateTopic(
            topic_id=f"topic-{term}",
            label=term,
            candidate_claims=tuple(
                claim.claim_id for claim in claims if term in tokens(claim.statement)
            ),
        )
        for term, _ in counts.most_common(16)
    )


def candidate_entities(
    units: tuple[ExtractedUnit, ...], claims: tuple[CandidateClaim, ...]
) -> tuple[CandidateEntity, ...]:
    labels: Counter[str] = Counter()
    for unit in units:
        labels.update(re.findall(r"\b[A-Z][A-Za-z0-9]+(?:\s+[A-Z][A-Za-z0-9]+){0,2}\b", unit.text))
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
    for index, (label, cluster_units) in enumerate(sorted(grouped.items()), start=1):
        unit_ids = tuple(unit.unit_id for unit in cluster_units)
        clusters.append(
            TopicCluster(
                cluster_id=f"cluster-{index}",
                label=label,
                extracted_units=unit_ids,
                candidate_claims=tuple(
                    claim.claim_id
                    for claim in claims
                    if any(claim.claim_id.startswith(f"claim-{unit_id}-") for unit_id in unit_ids)
                ),
                candidate_topics=tuple(topic.topic_id for topic in topics if topic.label == label),
            )
        )
    return tuple(clusters)


def wiki_matches(
    units: tuple[ExtractedUnit, ...],
    existing_pages: dict[str, str],
    source_locator: str,
) -> tuple[WikiMatch, ...]:
    page_embeddings = {page_id: embedding(text) for page_id, text in existing_pages.items()}
    matches: list[WikiMatch] = []
    for unit in units:
        unit_embedding = embedding(f"{unit.heading_path} {unit.text}")
        for page_id, page_embedding in page_embeddings.items():
            score = cosine(unit_embedding, page_embedding)
            if source_locator in existing_pages[page_id]:
                score += 0.15
            if score >= _MATCH_THRESHOLD:
                matches.append(
                    WikiMatch(
                        page_id=page_id,
                        score=round(score, 6),
                        match_reason=f"nearest-neighbor:{unit.unit_id}",
                        page_excerpt=excerpt(existing_pages[page_id]),
                    )
                )
    return tuple(sorted(matches, key=lambda match: (-match.score, match.page_id)))


def claim_comparisons(
    claims: tuple[CandidateClaim, ...], matches: tuple[WikiMatch, ...]
) -> tuple[ClaimComparison, ...]:
    comparisons: list[ClaimComparison] = []
    for claim in claims:
        for match in matches[:3]:
            if cosine(embedding(claim.statement), embedding(match.page_excerpt)) > 0.2:
                comparisons.append(
                    ClaimComparison(claim.claim_id, match.page_excerpt, "overlap", match.page_id)
                )
                break
    return tuple(comparisons)


def same_section_identity(heading: str, page_id: str) -> bool:
    heading_terms = set(tokens(heading.replace("-", " ")))
    page_terms = set(tokens(page_id.replace("-", " ")))
    return bool(heading_terms) and len(heading_terms & page_terms) >= min(2, len(heading_terms))


def unit_match(match: WikiMatch, unit_id: str) -> bool:
    return match.match_reason.endswith(f":{unit_id}")


def embedding(text: str) -> dict[str, float]:
    counts = Counter(tokens(text))
    norm = math.sqrt(sum(value * value for value in counts.values()))
    if not norm:
        return {}
    return {key: value / norm for key, value in counts.items()}


def cosine(a: dict[str, float], b: dict[str, float]) -> float:
    if not a or not b:
        return 0.0
    small, large = (a, b) if len(a) <= len(b) else (b, a)
    return sum(value * large.get(key, 0.0) for key, value in small.items())


def tokens(text: str) -> tuple[str, ...]:
    return tuple(token for token in _TOKEN_RE.findall(text.lower()) if token not in _STOP_WORDS)


def top_terms(text: str, limit: int) -> tuple[str, ...]:
    return tuple(term for term, _ in Counter(tokens(text)).most_common(limit))


def excerpt(text: str) -> str:
    body = text.split("---", 2)[-1] if text.startswith("---") else text
    cleaned = " ".join(body.split())
    return cleaned if len(cleaned) <= 240 else cleaned[:239].rstrip() + "..."


def _claim_sentences(text: str) -> tuple[str, ...]:
    paragraphs = []
    current: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        current.append(stripped)
    if current:
        paragraphs.append(" ".join(current))
    sentences: list[str] = []
    for paragraph in paragraphs:
        for sentence in _SENTENCE_RE.split(paragraph):
            normalized = " ".join(sentence.split()).strip()
            if len(tokens(normalized)) >= 3:
                sentences.append(normalized)
    return tuple(sentences)
