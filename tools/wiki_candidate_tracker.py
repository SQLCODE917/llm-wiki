#!/usr/bin/env python3
"""
Candidate page tracking and promotion.

V3 design: Task 4 - Candidate Promotion

Tracks candidate wiki pages across sources, handling:
- Deduplication via canonicalization
- Cross-source accumulation
- Promotion triggers
- Merge decisions
"""
from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------

@dataclass
class CandidateMention:
    """A single mention of a candidate from a source."""
    source: str
    priority: str
    claims: int
    claim_ids: list[str] = field(default_factory=list)
    sections: int = 0
    first_seen: str = ""
    last_seen: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "CandidateMention":
        return cls(
            source=d.get("source", ""),
            priority=d.get("priority", ""),
            claims=d.get("claims", 0),
            claim_ids=d.get("claim_ids", []),
            sections=d.get("sections", 0),
            first_seen=d.get("first_seen", ""),
            last_seen=d.get("last_seen", ""),
        )


@dataclass
class CandidateEntry:
    """A tracked candidate page."""
    canonical_slug: str
    aliases: list[str] = field(default_factory=list)
    mentions: list[CandidateMention] = field(default_factory=list)
    total_claims: int = 0
    total_sections: int = 0
    total_sources: int = 0
    referenced_by_pages: list[str] = field(default_factory=list)
    # discovered, deferred, queued, synthesizing, synthesized, rejected, merged
    status: str = "discovered"
    status_reason: str | None = None
    queued_date: str | None = None
    merged_into: str | None = None

    def to_dict(self) -> dict:
        d = asdict(self)
        d["mentions"] = [m.to_dict() if isinstance(m, CandidateMention)
                         else m for m in self.mentions]
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "CandidateEntry":
        return cls(
            canonical_slug=d.get("canonical_slug", ""),
            aliases=d.get("aliases", []),
            mentions=[CandidateMention.from_dict(
                m) for m in d.get("mentions", [])],
            total_claims=d.get("total_claims", 0),
            total_sections=d.get("total_sections", 0),
            total_sources=d.get("total_sources", 0),
            referenced_by_pages=d.get("referenced_by_pages", []),
            status=d.get("status", "discovered"),
            status_reason=d.get("status_reason"),
            queued_date=d.get("queued_date"),
            merged_into=d.get("merged_into"),
        )


@dataclass
class CandidatesData:
    """Full candidates.json schema."""
    candidates: dict[str, CandidateEntry] = field(default_factory=dict)
    updated: str = ""
    version: str = "1.0.0"

    def to_dict(self) -> dict:
        return {
            "_meta": {
                "updated": self.updated or str(date.today()),
                "version": self.version,
            },
            "candidates": {
                slug: entry.to_dict() for slug, entry in self.candidates.items()
            },
        }

    @classmethod
    def from_dict(cls, d: dict) -> "CandidatesData":
        meta = d.get("_meta", {})
        return cls(
            candidates={
                slug: CandidateEntry.from_dict(entry)
                for slug, entry in d.get("candidates", {}).items()
            },
            updated=meta.get("updated", ""),
            version=meta.get("version", "1.0.0"),
        )


# ---------------------------------------------------------------------------
# File I/O
# ---------------------------------------------------------------------------

DEFAULT_CANDIDATES_PATH = Path(".tmp/candidates.json")


def load_candidates(path: Path = DEFAULT_CANDIDATES_PATH) -> CandidatesData:
    """Load candidates data from JSON file."""
    if not path.exists():
        return CandidatesData()
    try:
        data = json.loads(path.read_text())
        return CandidatesData.from_dict(data)
    except (json.JSONDecodeError, KeyError):
        return CandidatesData()


def save_candidates(data: CandidatesData, path: Path = DEFAULT_CANDIDATES_PATH) -> None:
    """Save candidates data to JSON file."""
    data.updated = str(date.today())
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data.to_dict(), indent=2))


# ---------------------------------------------------------------------------
# Canonicalization
# ---------------------------------------------------------------------------

# Known ecosystem namespaces
KNOWN_NAMESPACES = {"js", "python", "ruby",
                    "scheme", "aoe2", "typescript", "node"}


def slugify(name: str) -> str:
    """Convert name to URL-safe slug."""
    slug = name.lower().strip()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')


def normalize_candidate_name(name: str, namespace: str | None = None) -> str:
    """
    Normalize candidate name for matching.
    Preserves namespace prefix when provided.
    """
    name = name.lower().strip()
    name = re.sub(r'\s+', '-', name)

    # Only add namespace if not already namespaced
    if namespace:
        prefix = f"{namespace}-"
        if name.startswith(prefix):
            # Keep as-is, namespace is explicit
            pass
        elif not any(name.startswith(f"{ns}-") for ns in KNOWN_NAMESPACES):
            # Add namespace if not already namespaced
            name = f"{namespace}-{name}"

    return slugify(name)


def find_wiki_page_by_title(name: str, wiki_root: Path = Path("wiki")) -> str | None:
    """
    Check if a wiki page exists with matching title.
    Returns the page slug if found, None otherwise.
    """
    normalized = slugify(name)

    # Search in concept directories
    for subdir in ["concepts", "entities", "procedures", "references"]:
        dir_path = wiki_root / subdir
        if not dir_path.exists():
            continue

        for page in dir_path.glob("*.md"):
            if page.stem == normalized:
                return page.stem

            # Also check title in frontmatter
            try:
                content = page.read_text(errors="ignore")
                if f"title: {name}" in content or f'title: "{name}"' in content:
                    return page.stem
            except Exception:
                pass

    return None


def canonicalize_candidate(
    name: str,
    existing_candidates: dict[str, CandidateEntry],
    namespace: str | None = None,
) -> tuple[str, str]:
    """
    Normalize candidate name and match against existing aliases.

    Returns (canonical_slug, action) where action is one of:
    - "existing_candidate": matched to existing candidate
    - "existing_page": matched to existing wiki page (should mark merged)
    - "new": new candidate slug

    Priority:
    1. Exact match to existing canonical slug
    2. Alias match to existing candidate
    3. Match to existing wiki page title → mark as merged, not promotable
    4. Generate new canonical slug (preserving namespace)
    """
    normalized = normalize_candidate_name(name, namespace)

    # Check existing candidates
    for slug, candidate in existing_candidates.items():
        if normalized == slug:
            return (slug, "existing_candidate")
        aliases_normalized = [normalize_candidate_name(
            a, namespace) for a in candidate.aliases]
        if normalized in aliases_normalized:
            return (slug, "existing_candidate")

    # Check existing wiki pages - these become merged, not promoted
    existing_page = find_wiki_page_by_title(name)
    if existing_page:
        return (existing_page, "existing_page")

    # Generate new slug (preserves namespace)
    return (slugify(normalized), "new")


# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------

def register_candidate(
    name: str,
    source: str,
    claims: list[str],
    priority: str,
    candidates_data: CandidatesData,
    namespace: str | None = None,
    sections: int = 0,
) -> str:
    """
    Register a candidate, handling existing page matches correctly.
    Returns the canonical slug.
    """
    canonical_slug, action = canonicalize_candidate(
        name, candidates_data.candidates, namespace
    )
    today = str(date.today())

    if action == "existing_page":
        # This concept already has a page - record as merged
        if canonical_slug not in candidates_data.candidates:
            candidates_data.candidates[canonical_slug] = CandidateEntry(
                canonical_slug=canonical_slug,
                aliases=[name] if name != canonical_slug else [],
                mentions=[],
                total_claims=0,
                total_sections=0,
                total_sources=0,
                referenced_by_pages=[],
                status="merged",
                status_reason="existing wiki page found",
                merged_into=canonical_slug,
            )
        return canonical_slug

    # Get or create candidate entry
    if canonical_slug in candidates_data.candidates:
        candidate = candidates_data.candidates[canonical_slug]
    else:
        candidate = CandidateEntry(
            canonical_slug=canonical_slug,
            aliases=[],
            mentions=[],
        )
        candidates_data.candidates[canonical_slug] = candidate

    # Add alias if it's new
    if name not in candidate.aliases and slugify(name) != canonical_slug:
        candidate.aliases.append(name)

    # Check if we already have a mention from this source
    existing_mention = next(
        (m for m in candidate.mentions if m.source == source), None
    )

    if existing_mention:
        # Update existing mention
        existing_mention.claims = max(existing_mention.claims, len(claims))
        existing_mention.claim_ids = list(
            set(existing_mention.claim_ids + claims))
        existing_mention.sections = max(existing_mention.sections, sections)
        existing_mention.last_seen = today
        # Upgrade priority if higher
        priority_order = ["defer", "could create",
                          "should create", "must create"]
        if priority in priority_order and existing_mention.priority in priority_order:
            if priority_order.index(priority) > priority_order.index(existing_mention.priority):
                existing_mention.priority = priority
    else:
        # Add new mention
        candidate.mentions.append(CandidateMention(
            source=source,
            priority=priority,
            claims=len(claims),
            claim_ids=claims,
            sections=sections,
            first_seen=today,
            last_seen=today,
        ))

    # Update totals
    candidate.total_claims = sum(m.claims for m in candidate.mentions)
    candidate.total_sections = sum(m.sections for m in candidate.mentions)
    candidate.total_sources = len(set(m.source for m in candidate.mentions))

    return canonical_slug


# ---------------------------------------------------------------------------
# Promotion
# ---------------------------------------------------------------------------

def check_candidate_promotion(candidates_data: CandidatesData) -> list[tuple[str, str]]:
    """
    Check candidates for promotion triggers.
    Returns list of (slug, trigger_reason) to promote.
    """
    to_promote = []

    for slug, candidate in candidates_data.candidates.items():
        if candidate.status in ("synthesized", "rejected", "merged", "queued", "synthesizing"):
            continue

        total_claims = candidate.total_claims
        total_sections = candidate.total_sections
        total_sources = candidate.total_sources
        referenced_by = len(candidate.referenced_by_pages)

        # Trigger: appears in ≥2 sources
        if total_sources >= 2:
            to_promote.append((slug, "cross-source"))
            continue

        # Trigger: ≥5 claims across ≥2 source sections
        if total_claims >= 5 and total_sections >= 2:
            to_promote.append((slug, "claim-diversity"))
            continue

        # Trigger: manual must_create in any source
        if any(m.priority == "must create" for m in candidate.mentions):
            to_promote.append((slug, "must-create"))
            continue

        # Trigger: referenced by ≥3 existing concept pages
        if referenced_by >= 3:
            to_promote.append((slug, "page-references"))
            continue

    return to_promote


def queue_candidate(candidates_data: CandidatesData, slug: str, reason: str) -> None:
    """Mark a candidate as queued for synthesis."""
    if slug not in candidates_data.candidates:
        return
    candidate = candidates_data.candidates[slug]
    candidate.status = "queued"
    candidate.status_reason = reason
    candidate.queued_date = str(date.today())


def mark_candidate_synthesized(candidates_data: CandidatesData, slug: str) -> None:
    """Mark a candidate as successfully synthesized."""
    if slug not in candidates_data.candidates:
        return
    candidate = candidates_data.candidates[slug]
    candidate.status = "synthesized"
    candidate.status_reason = "page created"


def mark_candidate_rejected(candidates_data: CandidatesData, slug: str, reason: str) -> None:
    """Mark a candidate as rejected (will not become a page)."""
    if slug not in candidates_data.candidates:
        return
    candidate = candidates_data.candidates[slug]
    candidate.status = "rejected"
    candidate.status_reason = reason


# ---------------------------------------------------------------------------
# Merge Decisions
# ---------------------------------------------------------------------------

def is_subtopic_of(candidate_slug: str, page_slug: str) -> bool:
    """
    Check if candidate appears to be a subtopic of an existing page.
    Uses simple prefix/suffix matching as heuristic.
    """
    # Remove common namespace prefixes for comparison
    candidate_base = candidate_slug
    page_base = page_slug
    for ns in KNOWN_NAMESPACES:
        if candidate_slug.startswith(f"{ns}-"):
            candidate_base = candidate_slug[len(ns) + 1:]
        if page_slug.startswith(f"{ns}-"):
            page_base = page_slug[len(ns) + 1:]

    # Check if candidate is a suffix of page (e.g., "closures" is subtopic of "js-closures")
    if candidate_base in page_base or page_base in candidate_base:
        return True

    # Check word overlap
    candidate_words = set(candidate_base.split('-'))
    page_words = set(page_base.split('-'))
    if candidate_words and page_words:
        overlap = len(candidate_words & page_words) / len(candidate_words)
        if overlap > 0.5:
            return True

    return False


def should_merge_candidate(
    candidate: CandidateEntry,
    existing_pages: list[str],
) -> str | None:
    """
    Check if candidate should merge into existing page.
    Returns target page slug or None.
    """
    # Too few claims for standalone page
    if candidate.total_claims < 3:
        # Find related page that covers the topic
        for page in existing_pages:
            if is_subtopic_of(candidate.canonical_slug, page):
                return page

    return None


def mark_candidate_merged(
    candidates_data: CandidatesData,
    slug: str,
    merged_into: str,
    reason: str,
) -> None:
    """Mark candidate as merged into existing page."""
    if slug not in candidates_data.candidates:
        return
    candidate = candidates_data.candidates[slug]
    candidate.status = "merged"
    candidate.merged_into = merged_into
    candidate.status_reason = reason


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Candidate page tracking")
    parser.add_argument("--candidates-path", type=Path,
                        default=DEFAULT_CANDIDATES_PATH)
    subparsers = parser.add_subparsers(dest="command")

    # check-promotion command
    promote_parser = subparsers.add_parser(
        "check-promotion", help="Check for candidates ready to promote")

    # status command
    status_parser = subparsers.add_parser(
        "status", help="Show candidates status")
    status_parser.add_argument("--status", help="Filter by status")

    # register command
    register_parser = subparsers.add_parser(
        "register", help="Register a candidate")
    register_parser.add_argument("name", help="Candidate name")
    register_parser.add_argument("--source", required=True, help="Source slug")
    register_parser.add_argument("--priority", default="should create")
    register_parser.add_argument("--claims", type=int, default=0)
    register_parser.add_argument("--namespace")

    args = parser.parse_args()

    candidates_data = load_candidates(args.candidates_path)

    if args.command == "check-promotion":
        to_promote = check_candidate_promotion(candidates_data)
        if not to_promote:
            print("No candidates ready for promotion.")
            return 0
        print(f"Candidates ready for promotion: {len(to_promote)}")
        for slug, reason in to_promote:
            print(f"  {slug}: {reason}")
        return 0

    elif args.command == "status":
        status_filter = args.status
        for slug, candidate in candidates_data.candidates.items():
            if status_filter and candidate.status != status_filter:
                continue
            print(
                f"{slug}: {candidate.status} ({candidate.total_claims} claims, {candidate.total_sources} sources)")
        return 0

    elif args.command == "register":
        claim_ids = [f"C{i+1:02d}" for i in range(args.claims)]
        slug = register_candidate(
            args.name, args.source, claim_ids, args.priority,
            candidates_data, args.namespace
        )
        save_candidates(candidates_data, args.candidates_path)
        print(f"Registered: {slug}")
        return 0

    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
