#!/usr/bin/env python3
"""Resolve stable wiki evidence IDs to source excerpts and locators.

MIGRATION NOTE: These functions are also available in wiki_io.evidence.
New code should prefer importing from the package:

    from wiki_io.evidence import (
        EvidenceResolver,
        ResolvedEvidence,
        stable_evidence_id,
        extract_evidence_ids,
    )
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

# Import from refactored packages
from wiki_io.state import NormalizedClaim, load_normalized_claims


LOCATOR_RE = re.compile(
    r"^(?:[A-Za-z0-9_-]+:)?normalized:L(?P<start>\d+)(?:-L?(?P<end>\d+))?$",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class ResolvedEvidence:
    evidence_id: str
    claim_id: str
    source_slug: str
    topic: str
    claim: str
    evidence: str
    locator: str
    source_page: str


def stable_evidence_id(slug: str, claim_id: str) -> str:
    """Return the canonical durable evidence ID stored in wiki pages."""
    if claim_id.startswith(f"{slug}:"):
        return claim_id
    return f"{slug}:{claim_id}"


def bracketed_evidence_id(slug: str, claim_id: str) -> str:
    return f"[{stable_evidence_id(slug, claim_id)}]"


def evidence_id_aliases(slug: str, claim_id: str) -> set[str]:
    canonical = stable_evidence_id(slug, claim_id)
    return {
        canonical,
        claim_id,
        canonical.lower(),
        claim_id.lower(),
    }


def extract_evidence_ids(cell: str) -> list[str]:
    """Extract bracketed evidence IDs from a table cell.

    Supports both durable IDs like [aoe2-basics:claim_...] and legacy prompt
    aliases like [E01].
    """
    ids = re.findall(r"\[([A-Za-z0-9_:-]+)\]", cell)
    if ids:
        return ids
    stripped = cell.strip().strip("`")
    if re.fullmatch(r"[A-Za-z0-9_:-]+", stripped):
        return [stripped]
    return []


class EvidenceResolver:
    """Lookup table for evidence IDs from claims-normalized.json."""

    def __init__(self, slug: str, claims: list[NormalizedClaim]):
        self.slug = slug
        self._source_lines = self._load_source_lines(slug)
        self._items: dict[str, ResolvedEvidence] = {}
        for claim in claims:
            stable_id = stable_evidence_id(slug, claim.claim_id)
            evidence = self._exact_excerpt_for_locator(
                claim.locator) or claim.evidence
            item = ResolvedEvidence(
                evidence_id=stable_id,
                claim_id=claim.claim_id,
                source_slug=slug,
                topic=claim.topic,
                claim=claim.claim,
                evidence=evidence,
                locator=claim.locator,
                source_page=f"wiki/sources/{slug}.md",
            )
            for alias in evidence_id_aliases(slug, claim.claim_id):
                self._items[alias] = item

    @staticmethod
    def _load_source_lines(slug: str) -> list[str] | None:
        source = Path("raw/normalized") / slug / "source.md"
        if not source.exists():
            return None
        return source.read_text(encoding="utf-8").splitlines()

    def _exact_excerpt_for_locator(self, locator: str) -> str | None:
        if self._source_lines is None:
            return None
        match = LOCATOR_RE.match(locator.strip().strip("`"))
        if not match:
            return None
        start = int(match.group("start"))
        end = int(match.group("end") or start)
        if start < 1 or end < start or end > len(self._source_lines):
            return None
        lines = [line.strip()
                 for line in self._source_lines[start - 1:end] if line.strip()]
        if not lines:
            return None
        return " ".join(lines)

    @classmethod
    def for_slug(cls, slug: str) -> EvidenceResolver | None:
        data = load_normalized_claims(slug)
        if data is None:
            return None
        return cls(slug, data.claims)

    @classmethod
    def for_source_page(cls, source_page: Path) -> EvidenceResolver | None:
        slug = source_page.stem
        return cls.for_slug(slug)

    def resolve(self, raw_id: str) -> ResolvedEvidence | None:
        cleaned = raw_id.strip().strip("[]").strip()
        return self._items.get(cleaned) or self._items.get(cleaned.lower())

    def resolve_cell(self, cell: str) -> list[ResolvedEvidence]:
        resolved: list[ResolvedEvidence] = []
        seen: set[str] = set()
        for raw_id in extract_evidence_ids(cell):
            item = self.resolve(raw_id)
            if item and item.evidence_id not in seen:
                resolved.append(item)
                seen.add(item.evidence_id)
        return resolved

    def canonical_cell(self, cell: str) -> str | None:
        items = self.resolve_cell(cell)
        if not items:
            return None
        return ", ".join(f"[{item.evidence_id}]" for item in items)
