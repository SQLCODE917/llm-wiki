#!/usr/bin/env python3
"""Evidence ID system for llm-wiki.

Assigns short IDs to evidence snippets so the LLM can cite them by ID
instead of writing evidence text. This:
1. Reduces model output size
2. Eliminates evidence fabrication
3. Makes evidence handling fully deterministic

Usage:
    from wiki_evidence_ids import EvidenceBank, build_evidence_bank_with_ids
    
    bank = build_evidence_bank_with_ids(source_lines, candidates, claims)
    prompt_text = bank.render_for_prompt()
    # ... model outputs [E07] citations ...
    filled_page = bank.expand_ids_in_page(page_text)
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class EvidenceItem:
    """A single evidence snippet with an ID."""
    id: str  # e.g., "E01", "E02"
    locator: str  # e.g., "normalized:L123"
    text: str  # The actual evidence text
    candidate: str  # Which candidate/topic this belongs to


@dataclass
class EvidenceBank:
    """Collection of evidence items indexed by ID."""
    items: dict[str, EvidenceItem] = field(default_factory=dict)
    by_locator: dict[str, EvidenceItem] = field(default_factory=dict)
    _next_id: int = 1
    
    def add(self, locator: str, text: str, candidate: str) -> EvidenceItem:
        """Add evidence and return the assigned item."""
        # Check if we already have this locator
        if locator in self.by_locator:
            return self.by_locator[locator]
        
        item = EvidenceItem(
            id=f"E{self._next_id:02d}",
            locator=locator,
            text=text,
            candidate=candidate,
        )
        self._next_id += 1
        self.items[item.id] = item
        self.by_locator[locator] = item
        return item
    
    def get_by_id(self, evidence_id: str) -> EvidenceItem | None:
        """Look up evidence by ID (e.g., 'E07' or '[E07]')."""
        clean_id = evidence_id.strip("[]").upper()
        return self.items.get(clean_id)
    
    def get_by_locator(self, locator: str) -> EvidenceItem | None:
        """Look up evidence by locator."""
        # Normalize locator format
        clean = re.sub(r'[`\s]', '', locator)
        return self.by_locator.get(clean)
    
    def render_for_prompt(self, max_text_chars: int = 150) -> str:
        """Render evidence bank for inclusion in prompts.
        
        Format:
        ### Topic Name
        [E01] normalized:L123 "Evidence text here..."
        [E02] normalized:L456 "Another excerpt..."
        """
        sections: list[str] = []
        current_candidate = None
        
        for item in self.items.values():
            if item.candidate != current_candidate:
                if current_candidate is not None:
                    sections.append("")
                sections.append(f"### {item.candidate}")
                current_candidate = item.candidate
            
            # Truncate long evidence for prompt readability
            text = item.text
            if len(text) > max_text_chars:
                text = text[:max_text_chars].rsplit(" ", 1)[0] + "..."
            
            sections.append(f'[{item.id}] {item.locator} "{text}"')
        
        return "\n".join(sections)
    
    def expand_ids_in_page(self, page_text: str) -> tuple[str, list[dict]]:
        """Expand evidence IDs to full 4-column table format.
        
        Input table formats:
        1. ID-only: | Claim | [E07] | (2-column)
        2. ID with source: | Claim | [E07] | Source | (3-column)
        
        Output: | Claim | Evidence | Locator | Source |
        
        Returns:
            Tuple of (transformed_text, list of expansions)
        """
        lines = page_text.splitlines()
        result_lines: list[str] = []
        expansions: list[dict] = []
        
        in_table = False
        table_type = None  # "2col_id", "3col_id"
        row_num = 0
        
        for line in lines:
            stripped = line.strip()
            
            # Detect table start
            if stripped.startswith("|") and stripped.endswith("|") and not in_table:
                cols = self._parse_table_row(stripped)
                if cols:
                    cols_lower = [c.lower() for c in cols]
                    
                    # Check for 2-column ID format: | Claim | Evidence ID |
                    if len(cols) == 2 and "claim" in cols_lower:
                        in_table = True
                        table_type = "2col_id"
                        row_num = 0
                        # Transform to 4-column header
                        result_lines.append("| Claim | Evidence | Locator | Source |")
                        continue
                    
                    # Check for 3-column ID format: | Claim | Evidence ID | Source |
                    if len(cols) == 3 and "claim" in cols_lower and "source" in cols_lower:
                        in_table = True
                        table_type = "3col_id"
                        row_num = 0
                        # Transform to 4-column header
                        result_lines.append("| Claim | Evidence | Locator | Source |")
                        continue
            
            # Transform separator row
            if in_table and self._is_separator_row(stripped):
                result_lines.append("| --- | --- | --- | --- |")
                continue
            
            # Process data rows with evidence IDs
            if in_table and stripped.startswith("|") and stripped.endswith("|"):
                cols = self._parse_table_row(stripped)
                
                if cols and table_type == "2col_id" and len(cols) == 2:
                    row_num += 1
                    claim = cols[0]
                    evidence_id = cols[1].strip()
                    
                    item = self.get_by_id(evidence_id)
                    if item:
                        new_cols = [claim, f'"{item.text}"', f"`{item.locator}`", "[Source](../sources/source.md)"]
                        result_lines.append(self._format_table_row(new_cols))
                        expansions.append({
                            "row": row_num,
                            "id": item.id,
                            "locator": item.locator,
                            "evidence": item.text,
                        })
                        continue
                
                elif cols and table_type == "3col_id" and len(cols) == 3:
                    row_num += 1
                    claim = cols[0]
                    evidence_id = cols[1].strip()
                    source = cols[2]
                    
                    item = self.get_by_id(evidence_id)
                    if item:
                        new_cols = [claim, f'"{item.text}"', f"`{item.locator}`", source]
                        result_lines.append(self._format_table_row(new_cols))
                        expansions.append({
                            "row": row_num,
                            "id": item.id,
                            "locator": item.locator,
                            "evidence": item.text,
                        })
                        continue
            
            # End of table detection
            if in_table and stripped and not stripped.startswith("|"):
                in_table = False
                table_type = None
            
            result_lines.append(line)
        
        return "\n".join(result_lines), expansions
    
    def _parse_table_row(self, line: str) -> list[str] | None:
        """Parse a markdown table row into cells."""
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            return None
        inner = stripped[1:-1]
        return [cell.strip() for cell in inner.split("|")]
    
    def _is_separator_row(self, line: str) -> bool:
        """Check if a line is a table separator row."""
        if not line.startswith("|") or not line.endswith("|"):
            return False
        inner = line[1:-1]
        cells = inner.split("|")
        return all(cell.strip() and set(cell.strip()) <= {"-", ":", " "} for cell in cells)
    
    def _format_table_row(self, cols: list[str]) -> str:
        """Format cells into a markdown table row."""
        return "| " + " | ".join(cols) + " |"


def build_evidence_bank_with_ids(
    source_lines: list[str],
    candidates: list[str],
    extraction_claims: list[dict] | None = None,
    max_per_candidate: int = 10,
) -> EvidenceBank:
    """Build an evidence bank with IDs from extraction claims or source lines.
    
    Args:
        source_lines: Lines from the normalized source
        candidates: List of candidate topic/page names
        extraction_claims: Claims from deep-extract (preferred) or None
        max_per_candidate: Max evidence items per candidate
    
    Returns:
        EvidenceBank with items indexed by ID
    """
    bank = EvidenceBank()
    
    for candidate in candidates:
        candidate_name = Path(candidate).stem.replace("-", " ").title() if candidate.endswith(".md") else candidate
        
        # Get claims for this candidate
        if extraction_claims:
            matched = [
                c for c in extraction_claims
                if c.get("topic", "").lower() == candidate_name.lower()
            ][:max_per_candidate]
            
            for claim in matched:
                locator = claim.get("locator", "")
                evidence = claim.get("evidence", "")
                if locator and evidence:
                    bank.add(locator, evidence, candidate_name)
        else:
            # Fall back to extracting from source directly
            # This is a simplified version - real extraction would use keyword matching
            pass
    
    return bank


def extract_evidence_at_locator(
    source_lines: list[str],
    locator: str,
    max_chars: int = 200,
) -> str | None:
    """Extract evidence text from source at the given locator."""
    match = re.search(r'L(\d+)(?:-L?(\d+))?', locator)
    if not match:
        return None
    
    start_line = int(match.group(1))
    end_line = int(match.group(2)) if match.group(2) else start_line
    
    if start_line < 1 or start_line > len(source_lines):
        return None
    
    end_line = min(end_line, len(source_lines))
    
    extracted = []
    for i in range(start_line - 1, end_line):
        if i < len(source_lines):
            extracted.append(source_lines[i])
    
    text = " ".join(extracted).strip()
    
    if len(text) > max_chars:
        text = text[:max_chars].rsplit(" ", 1)[0] + "..."
    
    return text if text else None
