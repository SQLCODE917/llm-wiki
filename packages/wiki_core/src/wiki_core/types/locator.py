"""Locator type — canonical representation of source line references.

A Locator points to a specific line range in a normalized source file.
It supports optional source prefixes (e.g., "js-allonge:normalized:L100-L105").

Usage:
    from wiki_core.types import Locator
    
    # Parse from string
    loc = Locator.parse("normalized:L100-L105")
    loc = Locator.parse("js-allonge:normalized:L100")  # Single line
    
    # Access fields
    print(loc.start_line)  # 100
    print(loc.end_line)    # 105
    print(loc.source)      # "js-allonge" or None
    
    # Serialize back to string
    print(str(loc))  # "normalized:L100-L105"
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class Locator:
    """A reference to a line range in a normalized source file.
    
    Attributes:
        start_line: First line number (1-indexed)
        end_line: Last line number (inclusive, >= start_line)
        source: Optional source slug prefix (e.g., "js-allonge")
    
    Invariants:
        - start_line >= 1
        - end_line >= start_line
        - Single lines are represented as start_line == end_line
    """
    start_line: int
    end_line: int
    source: str | None = None
    
    # Regex pattern for parsing locator strings
    # Matches: [source:]normalized:L<start>[-L<end>]
    PATTERN: ClassVar[re.Pattern[str]] = re.compile(
        r"^(?:(?P<source>[A-Za-z0-9_-]+):)?normalized:L(?P<start>\d+)(?:-L?(?P<end>\d+))?$",
        re.IGNORECASE,
    )
    
    def __post_init__(self):
        """Validate locator invariants."""
        if self.start_line < 1:
            raise ValueError(f"start_line must be >= 1, got {self.start_line}")
        if self.end_line < self.start_line:
            raise ValueError(
                f"end_line ({self.end_line}) must be >= start_line ({self.start_line})"
            )
    
    @classmethod
    def parse(cls, raw: str) -> Locator | None:
        """Parse a locator string into a Locator object.
        
        Accepts formats:
        - "normalized:L123"           -> Locator(123, 123, None)
        - "normalized:L123-L456"      -> Locator(123, 456, None)
        - "normalized:L123-456"       -> Locator(123, 456, None)
        - "slug:normalized:L123-L456" -> Locator(123, 456, "slug")
        
        Returns None if the string cannot be parsed.
        """
        # Clean up common formatting artifacts
        cleaned = raw.strip().strip("`").strip()
        
        # Handle backtick-wrapped locators
        if cleaned.startswith("`") and cleaned.endswith("`"):
            cleaned = cleaned[1:-1]
        
        match = cls.PATTERN.fullmatch(cleaned)
        if not match:
            return None
        
        source = match.group("source")
        start = int(match.group("start"))
        end_str = match.group("end")
        end = int(end_str) if end_str else start
        
        return cls(start_line=start, end_line=end, source=source)
    
    @classmethod
    def from_lines(cls, start: int, end: int | None = None, source: str | None = None) -> Locator:
        """Create a Locator from line numbers.
        
        Args:
            start: First line number (1-indexed)
            end: Last line number (default: same as start for single line)
            source: Optional source slug
        """
        return cls(start_line=start, end_line=end or start, source=source)
    
    def __str__(self) -> str:
        """Serialize to canonical string format.
        
        Always uses range format (L123-L123 for single lines) for consistency.
        """
        prefix = f"{self.source}:" if self.source else ""
        return f"{prefix}normalized:L{self.start_line}-L{self.end_line}"
    
    def to_compact_str(self) -> str:
        """Serialize to compact string format.
        
        Uses L123 for single lines, L123-L456 for ranges.
        """
        prefix = f"{self.source}:" if self.source else ""
        if self.start_line == self.end_line:
            return f"{prefix}normalized:L{self.start_line}"
        return f"{prefix}normalized:L{self.start_line}-L{self.end_line}"
    
    @property
    def is_single_line(self) -> bool:
        """True if this locator refers to a single line."""
        return self.start_line == self.end_line
    
    @property
    def line_count(self) -> int:
        """Number of lines covered by this locator."""
        return self.end_line - self.start_line + 1
    
    def contains(self, line: int) -> bool:
        """Check if a line number falls within this locator's range."""
        return self.start_line <= line <= self.end_line
    
    def overlaps(self, other: Locator) -> bool:
        """Check if this locator overlaps with another."""
        return (
            self.start_line <= other.end_line
            and other.start_line <= self.end_line
        )
    
    def with_source(self, source: str) -> Locator:
        """Return a new Locator with the given source prefix."""
        return Locator(
            start_line=self.start_line,
            end_line=self.end_line,
            source=source,
        )


# Convenience function for backward compatibility
def parse_locator(raw: str) -> tuple[int, int] | None:
    """Parse a locator string and return (start, end) tuple.
    
    This is a compatibility wrapper for code that expects the old
    tuple-based return format.
    """
    loc = Locator.parse(raw)
    if loc is None:
        return None
    return (loc.start_line, loc.end_line)


def normalize_locator(raw: str) -> str:
    """Normalize a locator to canonical range format.
    
    Converts "normalized:L123" to "normalized:L123-L123" for consistency.
    """
    loc = Locator.parse(raw)
    if loc is None:
        return raw  # Return unchanged if unparseable
    return str(loc)
