"""Frontmatter types — YAML frontmatter for wiki pages.

This module defines types for wiki page frontmatter:

1. **Frontmatter** — The typed schema for wiki page frontmatter.
   Used when constructing or validating wiki pages.

2. **ParsedFrontmatter** — The result of parsing frontmatter from markdown.
   Contains raw data, body text, and any parsing errors.

Usage:
    from wiki_core.types import Frontmatter
    
    # Create typed frontmatter
    fm = Frontmatter(
        title="Functions",
        type="concept",
        tags=["javascript", "programming"],
    )
    
    # Serialize to YAML
    yaml_str = fm.to_yaml()
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Any, Literal


# Valid page types
PageType = Literal["source", "entity", "concept", "procedure", "reference", "analysis"]

# Valid status values
PageStatus = Literal["draft", "reviewed", "stable"]


@dataclass
class Frontmatter:
    """YAML frontmatter schema for a wiki page.
    
    This represents the typed, validated structure of wiki page frontmatter.
    
    Attributes:
        title: Human-readable page title
        type: Page type (source, entity, concept, procedure, reference, analysis)
        tags: List of tags for categorization
        status: Page status (draft, reviewed, stable)
        last_updated: Date of last update (YYYY-MM-DD format)
        sources: List of source page paths this page cites
        source_ranges: List of source line ranges (e.g., "slug:normalized:L100-L200")
        
    Additional fields for source pages:
        source_id: Unique identifier for the source
        source_type: Type of source (pdf, markdown, web, etc.)
        raw_path: Path to raw imported file
        normalized_path: Path to normalized markdown
    """
    title: str
    type: PageType
    tags: list[str] = field(default_factory=list)
    status: PageStatus = "draft"
    last_updated: str = ""
    sources: list[str] = field(default_factory=list)
    source_ranges: list[str] = field(default_factory=list)
    
    # Source page specific fields
    source_id: str | None = None
    source_type: str | None = None
    raw_path: str | None = None
    normalized_path: str | None = None
    
    def __post_init__(self):
        if not self.last_updated:
            self.last_updated = date.today().isoformat()
    
    def to_dict(self) -> dict[str, Any]:
        """Serialize to dictionary for YAML conversion."""
        d: dict[str, Any] = {
            "title": self.title,
            "type": self.type,
            "tags": self.tags,
            "status": self.status,
            "last_updated": self.last_updated,
            "sources": self.sources,
        }
        
        # Only include source_ranges if non-empty
        if self.source_ranges:
            d["source_ranges"] = self.source_ranges
        
        # Include source-specific fields if present
        if self.source_id is not None:
            d["source_id"] = self.source_id
        if self.source_type is not None:
            d["source_type"] = self.source_type
        if self.raw_path is not None:
            d["raw_path"] = self.raw_path
        if self.normalized_path is not None:
            d["normalized_path"] = self.normalized_path
        
        return d
    
    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> Frontmatter:
        """Deserialize from dictionary."""
        return cls(
            title=d.get("title", "Untitled"),
            type=d.get("type", "concept"),
            tags=d.get("tags", []),
            status=d.get("status", "draft"),
            last_updated=d.get("last_updated", ""),
            sources=d.get("sources", []),
            source_ranges=d.get("source_ranges", []),
            source_id=d.get("source_id"),
            source_type=d.get("source_type"),
            raw_path=d.get("raw_path"),
            normalized_path=d.get("normalized_path"),
        )
    
    def to_yaml(self) -> str:
        """Serialize to YAML string for markdown frontmatter.
        
        Returns a string suitable for inclusion in markdown:
        ---
        title: Page Title
        type: concept
        ...
        ---
        """
        lines = ["---"]
        
        # Required fields
        lines.append(f"title: {_yaml_scalar(self.title)}")
        lines.append(f"type: {self.type}")
        
        # Source-specific fields (before common fields for source pages)
        if self.source_id is not None:
            lines.append(f"source_id: {self.source_id}")
        if self.source_type is not None:
            lines.append(f"source_type: {self.source_type}")
        if self.raw_path is not None:
            lines.append(f"raw_path: {self.raw_path}")
        if self.normalized_path is not None:
            lines.append(f"normalized_path: {self.normalized_path}")
        
        # Common fields
        lines.append(f"status: {self.status}")
        lines.append(f"last_updated: {self.last_updated}")
        
        # Tags
        if self.tags:
            lines.append("tags:")
            for tag in self.tags:
                lines.append(f"  - {tag}")
        else:
            lines.append("tags: []")
        
        # Sources
        if self.sources:
            lines.append("sources:")
            for source in self.sources:
                lines.append(f"  - {source}")
        else:
            lines.append("sources: []")
        
        # Source ranges (only if non-empty)
        if self.source_ranges:
            lines.append("source_ranges:")
            for sr in self.source_ranges:
                lines.append(f"  - {sr}")
        
        lines.append("---")
        return "\n".join(lines)


@dataclass(frozen=True)
class ParsedFrontmatter:
    """Result of parsing frontmatter from a markdown file.
    
    This is distinct from Frontmatter - it represents the raw parsing
    result, which may have errors or unexpected fields.
    
    Attributes:
        data: Raw key-value data from the YAML
        body: The markdown content after the frontmatter
        errors: List of parsing errors encountered
    """
    data: dict[str, Any]
    body: str
    errors: list[str]
    
    def to_frontmatter(self) -> Frontmatter | None:
        """Convert to typed Frontmatter if valid.
        
        Returns None if the data doesn't conform to the schema.
        """
        try:
            return Frontmatter.from_dict(self.data)
        except (KeyError, TypeError, ValueError):
            return None
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a value from the raw data."""
        return self.data.get(key, default)


def _yaml_scalar(value: str) -> str:
    """Format a string value for YAML output.
    
    Quotes the value if it contains special characters.
    """
    if not value:
        return '""'
    
    # Check if quoting is needed
    needs_quotes = (
        value.startswith((" ", "\t", '"', "'"))
        or value.endswith((" ", "\t"))
        or ":" in value
        or "#" in value
        or value in ("true", "false", "null", "yes", "no")
        or value.startswith("@")
        or value.startswith("!")
    )
    
    if needs_quotes:
        # Use double quotes and escape internal quotes
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    
    return value
