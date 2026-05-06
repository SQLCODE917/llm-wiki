#!/usr/bin/env python3
"""Context budget packer for Phase 2 synthesis.

Assembles synthesis context within a token budget, prioritizing
essential sections and trimming/dropping lower-priority content.

Budget allocation (targeting 8-9k tokens):
    system + schema:             900 tokens
    validator requirements:      400
    candidate/page intent:       300
    source summary:              500
    evidence bank canonical:   1,200
    local source excerpts:     3,000
    neighboring claims:          800
    related wiki summaries:      800
    previous failures:           600
    slack:                       500
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wiki_phase2_benchmark import EvidenceBankResult, RelatedCandidate
    from wiki_failure_classifier import ValidationFailure


@dataclass
class ContextBudget:
    """Token budget allocation for synthesis context."""
    total_tokens: int = 9000

    # Fixed allocations (always included)
    system_schema: int = 900
    validator_requirements: int = 400
    candidate_intent: int = 300
    source_summary: int = 500

    # Variable allocations (can be trimmed)
    evidence_bank: int = 1200
    local_excerpts: int = 3000
    neighboring_claims: int = 800
    related_wiki: int = 800
    repair_context: int = 600
    slack: int = 500


@dataclass
class ContextStats:
    """Statistics about context packing."""
    target_tokens: int = 0
    actual_tokens: int = 0
    evidence_tokens: int = 0
    excerpt_tokens: int = 0
    validator_tokens: int = 0
    neighbor_tokens: int = 0
    related_wiki_tokens: int = 0
    repair_tokens: int = 0
    dropped_sections: list[str] = field(default_factory=list)

    @property
    def useful_token_ratio(self) -> float:
        """Ratio of useful content (evidence + excerpts) to total."""
        if self.actual_tokens == 0:
            return 0.0
        return (self.evidence_tokens + self.excerpt_tokens) / self.actual_tokens


def estimate_tokens(text: str) -> int:
    """Estimate token count (rough: ~4 chars per token)."""
    return len(text) // 4


def truncate_to_tokens(text: str, max_tokens: int) -> str:
    """Truncate text to fit within token budget."""
    max_chars = max_tokens * 4
    if len(text) <= max_chars:
        return text

    # Try to truncate at a paragraph boundary
    truncated = text[:max_chars]
    last_para = truncated.rfind("\n\n")
    if last_para > max_chars // 2:
        return truncated[:last_para] + "\n\n[...truncated]"

    # Fall back to line boundary
    last_line = truncated.rfind("\n")
    if last_line > max_chars // 2:
        return truncated[:last_line] + "\n[...truncated]"

    return truncated + "..."


VALIDATOR_REQUIREMENTS = """## Validation requirements

Your output will be validated against these rules:

1. **Frontmatter**: Must include title, type, tags, status, last_updated, sources
2. **Source link**: frontmatter.sources must include path to source page
3. **Source pages section**: Required section linking to source page(s)
4. **Evidence table**: Minimum 3 rows with Claim|Evidence|Locator|Source columns
5. **Locator format**: Must be `normalized:L123` or `normalized:L123-L456`
6. **Locator range**: All locators must be within declared source_ranges
7. **Claim synthesis**: Claims must be YOUR words, not copied from evidence
8. **No placeholders**: No "Page title" or template text
9. **No empty sections**: Every section needs content or "None."
"""

COMMON_FAILURES = """## Common mistakes to avoid

BAD claim (copies evidence):
| Functions containing free variables are closures. | "Functions containing free variables are closures." |

GOOD claim (synthesizes):
| Functions that reference variables from outer scopes are termed closures. | "Functions containing free variables are closures." |

BAD locator (outside range):
| ... | `normalized:L1709` | (when source_ranges is L1260-L1290)

Use only evidence IDs from the evidence bank. Do not write quote text or locators directly.
"""

EVIDENCE_CONTRACT = """## Evidence contract

You may only cite evidence IDs from the evidence bank below.
- Return evidence_ids as an array, e.g. ["E01", "E04"]
- Do NOT write quote text in the Evidence column
- Do NOT write locators - they are derived from evidence IDs
- The renderer will expand evidence IDs to full table rows
"""


def render_candidate_intent(
    candidate: "RelatedCandidate",
    source_ranges: list[str] | None = None,
) -> str:
    """Render candidate intent section."""
    lines = [
        "## Page to create",
        "",
        f"**Path**: `{candidate.path}`",
    ]

    if hasattr(candidate, 'title') and candidate.title:
        lines.append(f"**Title**: {candidate.title}")

    if hasattr(candidate, 'group') and candidate.group:
        lines.append(f"**Topic group**: {candidate.group}")

    if hasattr(candidate, 'evidence_basis') and candidate.evidence_basis:
        lines.append(f"**Evidence basis**: {candidate.evidence_basis}")

    if source_ranges:
        lines.append("")
        lines.append("**Allowed source ranges** (cite only from these):")
        for sr in source_ranges:
            lines.append(f"- `{sr}`")

    return "\n".join(lines)


def render_evidence_bank_section(
    evidence_bank: "EvidenceBankResult",
    max_tokens: int,
    include_context: bool = True,
) -> tuple[str, int]:
    """Render evidence bank within token budget.

    Returns (text, tokens_used).
    """
    lines = ["## Evidence bank", "",
             "Use these evidence IDs in your claims:", ""]

    for eid, item in sorted(evidence_bank.items.items()):
        section_lines = [f"[{eid}] {item.locator}"]

        # Evidence text (always include)
        display_text = item.text[:200] + \
            "..." if len(item.text) > 200 else item.text
        section_lines.append(f'Evidence: "{display_text}"')

        # Context (optional, for richer understanding)
        if include_context and item.context_before:
            context_preview = item.context_before[-200:] if len(
                item.context_before) > 200 else item.context_before
            section_lines.append(f"Context before: {context_preview}")

        if include_context and item.context_after:
            context_preview = item.context_after[:200] if len(
                item.context_after) > 200 else item.context_after
            section_lines.append(f"Context after: {context_preview}")

        section_lines.append("")

        section_text = "\n".join(section_lines)
        current_text = "\n".join(lines)

        # Check if we're within budget
        if estimate_tokens(current_text + section_text) > max_tokens:
            lines.append("[...additional evidence truncated]")
            break

        lines.extend(section_lines)

    text = "\n".join(lines)
    return text, estimate_tokens(text)


def render_local_excerpts(
    source_text: str,
    start_line: int,
    end_line: int,
    max_tokens: int,
    context_lines: int = 50,
) -> tuple[str, int]:
    """Render local source excerpts around the evidence range.

    Returns (text, tokens_used).
    """
    lines = source_text.splitlines()

    # Expand range with context
    excerpt_start = max(0, start_line - context_lines - 1)
    excerpt_end = min(len(lines), end_line + context_lines)

    excerpt_lines = lines[excerpt_start:excerpt_end]
    excerpt_text = "\n".join(excerpt_lines)

    # Truncate if needed
    excerpt_text = truncate_to_tokens(excerpt_text, max_tokens - 100)

    result = f"""## Local source excerpt

Lines {excerpt_start + 1}-{min(excerpt_end, len(lines))} from normalized source:

```
{excerpt_text}
```
"""
    return result, estimate_tokens(result)


def render_neighboring_claims(
    all_claims: list[dict],
    current_topic: str,
    current_range: tuple[int, int],
    max_tokens: int,
    proximity_lines: int = 100,
) -> tuple[str, int]:
    """Render claims from adjacent source regions.

    Returns (text, tokens_used).
    """
    lines = [
        "## Neighboring claims (for boundary awareness)",
        "",
        "These claims belong to OTHER pages. Do not absorb them unless needed for contrast.",
        "",
    ]

    start, end = current_range
    neighbors_by_topic: dict[str, list[dict]] = {}

    for claim in all_claims:
        topic = claim.get("topic", "")
        if topic.lower() == current_topic.lower():
            continue

        # Parse claim's locator
        locator = claim.get("locator", "")
        match = re.search(r"L(\d+)", locator)
        if not match:
            continue

        claim_line = int(match.group(1))

        # Check proximity
        if (start - proximity_lines) <= claim_line <= (end + proximity_lines):
            if topic not in neighbors_by_topic:
                neighbors_by_topic[topic] = []
            neighbors_by_topic[topic].append(claim)

    for topic, claims in sorted(neighbors_by_topic.items()):
        lines.append(f"### {topic}")
        for c in claims[:5]:
            claim_text = c.get("claim", "")[:100]
            lines.append(f"- {claim_text}")
        lines.append("")

        # Check budget
        if estimate_tokens("\n".join(lines)) > max_tokens:
            lines.append("[...additional neighbors truncated]")
            break

    if not neighbors_by_topic:
        lines.append("No neighboring claims found within source proximity.")

    text = "\n".join(lines)
    return text, estimate_tokens(text)


def render_related_wiki_summaries(
    related_pages: list[Path],
    max_tokens: int,
) -> tuple[str, int]:
    """Render summaries of existing related wiki pages.

    Returns (text, tokens_used).
    """
    lines = [
        "## Existing related pages",
        "",
        "These pages already exist. Avoid duplicating their content.",
        "",
    ]

    for page_path in related_pages[:10]:
        if not page_path.exists():
            continue

        text = page_path.read_text()

        # Extract title
        title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
        title = title_match.group(1) if title_match else page_path.stem

        # Extract first paragraph after title
        paragraphs = re.split(r"\n\n+", text)
        summary = ""
        for para in paragraphs[1:5]:
            if para.strip() and not para.startswith("#") and not para.startswith("-"):
                summary = para.strip()[:200]
                break

        lines.append(f"- **{title}**: {summary}...")

        if estimate_tokens("\n".join(lines)) > max_tokens:
            lines.append("[...additional pages truncated]")
            break

    text = "\n".join(lines)
    return text, estimate_tokens(text)


def render_repair_context(
    failures: list["ValidationFailure"],
    previous_attempts: list[str] | None = None,
    max_tokens: int = 600,
) -> tuple[str, int]:
    """Render repair context for targeted LLM repair.

    Returns (text, tokens_used).
    """
    lines = [
        "## Failures to fix",
        "",
    ]

    for f in failures:
        cat = f.category.value if hasattr(f, 'category') and hasattr(
            f.category, 'value') else "unknown"
        msg = f.message if hasattr(f, 'message') else str(f)
        lines.append(f"- [{cat}] {msg}")
        if hasattr(f, 'fix_hint') and f.fix_hint:
            lines.append(f"  Hint: {f.fix_hint}")

    if previous_attempts:
        lines.extend(["", "## Previous attempt failures (don't repeat)", ""])
        for i, attempt in enumerate(previous_attempts[-2:], 1):
            lines.append(f"### Attempt {i}")
            lines.append(truncate_to_tokens(attempt, 200))

    text = "\n".join(lines)
    return truncate_to_tokens(text, max_tokens), estimate_tokens(text)


def build_context_pack(
    budget: ContextBudget,
    evidence_bank: "EvidenceBankResult",
    candidate: "RelatedCandidate",
    source_text: str,
    source_ranges: list[str] | None = None,
    all_claims: list[dict] | None = None,
    related_pages: list[Path] | None = None,
    failures: list["ValidationFailure"] | None = None,
    previous_attempts: list[str] | None = None,
) -> tuple[str, ContextStats]:
    """Build context pack within token budget.

    Returns (context_text, stats).
    """
    sections = []
    stats = ContextStats(target_tokens=budget.total_tokens)
    remaining = budget.total_tokens

    # Fixed sections (always included)

    # Validator requirements
    sections.append(VALIDATOR_REQUIREMENTS)
    stats.validator_tokens = estimate_tokens(VALIDATOR_REQUIREMENTS)
    remaining -= stats.validator_tokens

    # Evidence contract
    sections.append(EVIDENCE_CONTRACT)
    remaining -= estimate_tokens(EVIDENCE_CONTRACT)

    # Candidate intent
    intent_text = render_candidate_intent(candidate, source_ranges)
    sections.append(intent_text)
    remaining -= estimate_tokens(intent_text)

    # Common failures
    sections.append(COMMON_FAILURES)
    remaining -= estimate_tokens(COMMON_FAILURES)

    # Variable sections (trimmed to fit)

    # Evidence bank (priority 1)
    evidence_text, evidence_tokens = render_evidence_bank_section(
        evidence_bank,
        min(remaining, budget.evidence_bank),
        include_context=True,
    )
    sections.append(evidence_text)
    stats.evidence_tokens = evidence_tokens
    remaining -= evidence_tokens

    # Local excerpts (priority 2)
    if remaining > 200 and evidence_bank.items:
        # Find range from evidence
        line_nums = []
        for item in evidence_bank.items.values():
            if item.line_start > 0:
                line_nums.append(item.line_start)

        if line_nums:
            start_line = min(line_nums)
            end_line = max(line_nums)

            excerpt_text, excerpt_tokens = render_local_excerpts(
                source_text,
                start_line,
                end_line,
                min(remaining, budget.local_excerpts),
            )
            sections.append(excerpt_text)
            stats.excerpt_tokens = excerpt_tokens
            remaining -= excerpt_tokens

    # Neighboring claims (priority 3)
    if remaining > 200 and all_claims and evidence_bank.items:
        line_nums = [
            item.line_start for item in evidence_bank.items.values() if item.line_start > 0]
        if line_nums:
            current_range = (min(line_nums), max(line_nums))
            current_topic = getattr(candidate, 'title', None) or Path(
                candidate.path).stem.replace("-", " ")

            neighbor_text, neighbor_tokens = render_neighboring_claims(
                all_claims,
                current_topic,
                current_range,
                min(remaining, budget.neighboring_claims),
            )
            sections.append(neighbor_text)
            stats.neighbor_tokens = neighbor_tokens
            remaining -= neighbor_tokens
    else:
        stats.dropped_sections.append("neighboring_claims")

    # Related wiki summaries (priority 4, can be dropped)
    if remaining > 200 and related_pages:
        wiki_text, wiki_tokens = render_related_wiki_summaries(
            related_pages,
            min(remaining, budget.related_wiki),
        )
        sections.append(wiki_text)
        stats.related_wiki_tokens = wiki_tokens
        remaining -= wiki_tokens
    else:
        stats.dropped_sections.append("related_wiki_summaries")

    # Repair context (only for repair prompts)
    if failures and remaining > 100:
        repair_text, repair_tokens = render_repair_context(
            failures,
            previous_attempts,
            min(remaining, budget.repair_context),
        )
        sections.append(repair_text)
        stats.repair_tokens = repair_tokens
        remaining -= repair_tokens

    context_text = "\n\n".join(sections)
    stats.actual_tokens = estimate_tokens(context_text)

    return context_text, stats


def main() -> int:
    """CLI for testing context packer."""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Context budget packer")
    parser.add_argument("--budget", type=int, default=9000,
                        help="Total token budget")
    parser.add_argument("--show-budget", action="store_true",
                        help="Show default budget allocation")
    args = parser.parse_args()

    if args.show_budget:
        budget = ContextBudget(total_tokens=args.budget)
        print(json.dumps({
            "total_tokens": budget.total_tokens,
            "system_schema": budget.system_schema,
            "validator_requirements": budget.validator_requirements,
            "candidate_intent": budget.candidate_intent,
            "source_summary": budget.source_summary,
            "evidence_bank": budget.evidence_bank,
            "local_excerpts": budget.local_excerpts,
            "neighboring_claims": budget.neighboring_claims,
            "related_wiki": budget.related_wiki,
            "repair_context": budget.repair_context,
            "slack": budget.slack,
        }, indent=2))
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
