"""Claim types — canonical representation of extracted and synthesized claims.

This module defines the claim types used throughout the wiki ingestion pipeline:

1. **Claim** — The canonical extracted claim with evidence and locator.
   Used during extraction, normalization, and synthesis.

2. **SynthesisClaim** — A claim in the synthesis output format with evidence IDs.
   Used in wiki page schema for LLM output.

3. **SourceClaim** — A frozen claim for analysis (contradiction detection, etc).
   Includes computed fields like tokens for efficient comparison.

Usage:
    from wiki_core.types import Claim, SynthesisClaim, SourceClaim
    
    # Parse from JSON
    claim = Claim.from_dict({"topic": "Functions", "claim": "...", ...})
    
    # Serialize to JSON
    data = claim.to_dict()
    
    # Generate stable ID
    claim_id = Claim.generate_id("js-allonge", "Functions are...", "normalized:L100", 0)
"""
from __future__ import annotations

import hashlib
import re
import unicodedata
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def normalize_claim_text(text: str) -> str:
    """Normalize claim text for hashing.
    
    Trim whitespace, collapse repeated spaces, normalize Unicode.
    Do NOT lowercase - code, symbols, and proper nouns may be case-sensitive.
    """
    text = unicodedata.normalize("NFC", text)
    text = " ".join(text.split())
    return text.strip()


def generate_claim_id(slug: str, claim_text: str, locator: str, chunk_index: int) -> str:
    """Generate a stable, deterministic claim ID.
    
    Format: claim_<slug>_c<chunk-index>_<8-char-hash>
    
    The hash is derived from normalized claim text + primary evidence locator.
    This ensures:
    - Same input → same ID (reproducible)
    - Does not shift if earlier claims change (unlike sequence numbers)
    - Chunk index visible in ID for debugging
    """
    normalized = normalize_claim_text(claim_text)
    hash_input = f"{normalized}|{locator}"
    hash_bytes = hashlib.sha256(hash_input.encode("utf-8")).digest()
    hash_hex = hash_bytes[:4].hex()  # 8 hex chars
    
    slug_part = slug if slug else "unknown"
    return f"claim_{slug_part}_c{chunk_index:03d}_{hash_hex}"


@dataclass
class Claim:
    """An extracted claim with evidence from a source.
    
    This is the canonical claim type used throughout extraction and synthesis.
    It represents a concrete statement backed by verbatim source evidence.
    
    Attributes:
        topic: Category/topic this claim belongs to
        claim: The claim statement in the agent's own words
        evidence: Verbatim excerpt from the source
        locator: Line reference (e.g., "normalized:L100-L105")
        chunk_index: Index of the chunk this was extracted from
        claim_id: Stable identifier (auto-generated if not provided)
    """
    topic: str
    claim: str
    evidence: str
    locator: str
    chunk_index: int
    claim_id: str = ""
    
    def __post_init__(self):
        """Generate claim_id if not set."""
        if not self.claim_id:
            self.claim_id = generate_claim_id(
                "", self.claim, self.locator, self.chunk_index
            )
    
    def to_dict(self) -> dict[str, Any]:
        """Serialize to dictionary for JSON storage."""
        return {
            "claim_id": self.claim_id,
            "topic": self.topic,
            "claim": self.claim,
            "evidence": self.evidence,
            "locator": self.locator,
            "chunk_index": self.chunk_index,
        }
    
    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> Claim:
        """Deserialize from dictionary."""
        return cls(
            topic=d.get("topic", ""),
            claim=d.get("claim", ""),
            evidence=d.get("evidence", ""),
            locator=d.get("locator", ""),
            chunk_index=d.get("chunk_index", 0),
            claim_id=d.get("claim_id", ""),
        )
    
    @staticmethod
    def generate_id(slug: str, claim_text: str, locator: str, chunk_index: int) -> str:
        """Generate a stable claim ID (static method for external use)."""
        return generate_claim_id(slug, claim_text, locator, chunk_index)
    
    def with_id(self, slug: str) -> Claim:
        """Return a new Claim with a properly prefixed ID."""
        new_id = generate_claim_id(slug, self.claim, self.locator, self.chunk_index)
        return Claim(
            topic=self.topic,
            claim=self.claim,
            evidence=self.evidence,
            locator=self.locator,
            chunk_index=self.chunk_index,
            claim_id=new_id,
        )


@dataclass
class RawClaim(Claim):
    """A raw extracted claim before normalization.
    
    Extends Claim with an extraction timestamp for audit purposes.
    """
    extracted_at: str = ""
    
    def __post_init__(self):
        super().__post_init__()
        if not self.extracted_at:
            self.extracted_at = datetime.now(timezone.utc).isoformat()
    
    def to_dict(self) -> dict[str, Any]:
        """Serialize to dictionary for JSON storage."""
        d = super().to_dict()
        d["extracted_at"] = self.extracted_at
        return d
    
    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> RawClaim:
        """Deserialize from dictionary."""
        return cls(
            topic=d.get("topic", ""),
            claim=d.get("claim", ""),
            evidence=d.get("evidence", ""),
            locator=d.get("locator", ""),
            chunk_index=d.get("chunk_index", 0),
            claim_id=d.get("claim_id", ""),
            extracted_at=d.get("extracted_at", ""),
        )


# NormalizedClaim is just an alias for Claim - the normalization is in the ID
NormalizedClaim = Claim


@dataclass
class SynthesisClaim:
    """A claim in the synthesis output format with evidence ID references.
    
    Used in WikiPageSchema for LLM-generated pages. Instead of including
    the full evidence text, it references evidence by ID (e.g., "E03").
    
    Attributes:
        claim: The claim statement
        evidence_ids: List of evidence IDs (e.g., ["E03", "E07"])
    """
    claim: str
    evidence_ids: list[str] = field(default_factory=list)
    
    def to_dict(self) -> dict[str, Any]:
        return {
            "claim": self.claim,
            "evidence_ids": self.evidence_ids,
        }
    
    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> SynthesisClaim:
        return cls(
            claim=d.get("claim", ""),
            evidence_ids=d.get("evidence_ids", []),
        )


def tokenize_for_comparison(text: str) -> frozenset[str]:
    """Extract content tokens from text for comparison.
    
    Used by SourceClaim for efficient similarity detection.
    """
    # Lowercase and extract word tokens
    words = re.findall(r'[a-z][a-z0-9]*', text.lower())
    # Filter out very short words
    return frozenset(w for w in words if len(w) >= 3)


def extract_numbers(text: str) -> frozenset[str]:
    """Extract numeric values from text.
    
    Used by SourceClaim for detecting contradictory numbers.
    """
    numbers = re.findall(r'\d+(?:\.\d+)?', text)
    return frozenset(numbers)


@dataclass(frozen=True)
class SourceClaim:
    """A frozen claim for analysis and contradiction detection.
    
    This is an immutable, hashable claim with precomputed tokens
    for efficient similarity comparison.
    
    Attributes:
        page: Path to the source page containing this claim
        row: Row number in the evidence table
        claim: The claim text
        evidence: The evidence text
        locator: Line reference
        tokens: Precomputed content tokens for similarity
        numbers: Precomputed numeric values for contradiction detection
    """
    page: Path
    row: int
    claim: str
    evidence: str
    locator: str
    tokens: frozenset[str]
    numbers: frozenset[str]
    
    @classmethod
    def from_claim(cls, claim: Claim, page: Path, row: int) -> SourceClaim:
        """Create a SourceClaim from a Claim with computed fields."""
        text = f"{claim.claim} {claim.evidence}"
        return cls(
            page=page,
            row=row,
            claim=claim.claim,
            evidence=claim.evidence,
            locator=claim.locator,
            tokens=tokenize_for_comparison(text),
            numbers=extract_numbers(text),
        )
    
    @classmethod
    def from_row(
        cls,
        page: Path,
        row: int,
        claim: str,
        evidence: str,
        locator: str,
    ) -> SourceClaim:
        """Create a SourceClaim from table row data."""
        text = f"{claim} {evidence}"
        return cls(
            page=page,
            row=row,
            claim=claim,
            evidence=evidence,
            locator=locator,
            tokens=tokenize_for_comparison(text),
            numbers=extract_numbers(text),
        )
