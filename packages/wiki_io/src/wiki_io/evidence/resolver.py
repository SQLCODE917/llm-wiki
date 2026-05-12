"""Evidence resolver for wiki ingestion pipeline.

Resolves evidence IDs to source excerpts and locators.

Usage:
    from wiki_io.evidence import EvidenceResolver, stable_evidence_id
    
    resolver = EvidenceResolver.for_slug("js-allonge")
    resolved = resolver.resolve("js-allonge:claim_test_c000_abc123")
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


# Evidence ID pattern for extracting from table cells
EVIDENCE_ID_RE = re.compile(r"\[([A-Za-z0-9_:-]+)\]")

# Locator pattern for parsing
LOCATOR_RE = re.compile(
    r"^(?:[A-Za-z0-9_-]+:)?normalized:L(?P<start>\d+)(?:-L?(?P<end>\d+))?$",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class ResolvedEvidence:
    """A resolved evidence item with all metadata."""
    evidence_id: str
    claim_id: str
    source_slug: str
    topic: str
    claim: str
    evidence: str
    locator: str
    source_page: str


def stable_evidence_id(slug: str, claim_id: str) -> str:
    """Return the canonical durable evidence ID stored in wiki pages.

    Format: <slug>:<claim_id>
    Example: js-allonge:claim_jsallonge_c001_abc12345
    """
    if claim_id.startswith(f"{slug}:"):
        return claim_id
    return f"{slug}:{claim_id}"


def bracketed_evidence_id(slug: str, claim_id: str) -> str:
    """Return evidence ID in bracket notation for tables."""
    return f"[{stable_evidence_id(slug, claim_id)}]"


def evidence_id_aliases(slug: str, claim_id: str) -> set[str]:
    """Generate all valid aliases for an evidence ID."""
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
    ids = EVIDENCE_ID_RE.findall(cell)
    if ids:
        return ids
    # Fallback: try bare ID
    stripped = cell.strip().strip("`")
    if re.fullmatch(r"[A-Za-z0-9_:-]+", stripped):
        return [stripped]
    return []


class EvidenceResolver:
    """Lookup table for evidence IDs from claims-normalized.json.

    This class loads normalized claims and provides resolution of
    evidence IDs to their full metadata including excerpts.
    """

    def __init__(self, slug: str, claims: list, source_lines: list[str] | None = None):
        """Initialize resolver with claims.

        Args:
            slug: Source slug
            claims: List of NormalizedClaim objects
            source_lines: Optional pre-loaded source lines
        """
        self.slug = slug
        self._source_lines = source_lines or self._load_source_lines(slug)
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
        """Load source lines from normalized source."""
        source = Path("raw/normalized") / slug / "source.md"
        if not source.exists():
            return None
        return source.read_text(encoding="utf-8").splitlines()

    def _exact_excerpt_for_locator(self, locator: str) -> str | None:
        """Extract exact text from source at locator."""
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
        """Create resolver for a slug by loading its claims.

        This imports from wiki_io.state to load claims.
        """
        from wiki_io.state import load_normalized_claims

        data = load_normalized_claims(slug)
        if data is None:
            return None
        return cls(slug, data.claims)

    @classmethod
    def for_source_page(cls, source_page: Path) -> EvidenceResolver | None:
        """Create resolver from a source page path."""
        slug = source_page.stem
        return cls.for_slug(slug)

    def resolve(self, raw_id: str) -> ResolvedEvidence | None:
        """Resolve an evidence ID to its full metadata."""
        cleaned = raw_id.strip().strip("[]").strip()
        return self._items.get(cleaned) or self._items.get(cleaned.lower())

    def resolve_cell(self, cell: str) -> list[ResolvedEvidence]:
        """Resolve all evidence IDs in a table cell."""
        resolved: list[ResolvedEvidence] = []
        seen: set[str] = set()
        for raw_id in extract_evidence_ids(cell):
            item = self.resolve(raw_id)
            if item and item.evidence_id not in seen:
                resolved.append(item)
                seen.add(item.evidence_id)
        return resolved

    def canonical_cell(self, cell: str) -> str | None:
        """Convert evidence IDs in a cell to canonical format."""
        items = self.resolve_cell(cell)
        if not items:
            return None
        return ", ".join(f"[{item.evidence_id}]" for item in items)

    def get_all_evidence_ids(self) -> list[str]:
        """Get all unique evidence IDs in the resolver."""
        seen: set[str] = set()
        ids: list[str] = []
        for item in self._items.values():
            if item.evidence_id not in seen:
                seen.add(item.evidence_id)
                ids.append(item.evidence_id)
        return ids
