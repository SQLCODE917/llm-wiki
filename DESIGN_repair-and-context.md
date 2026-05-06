# Design: Validation-Driven Repair and Richer Synthesis Context

This document addresses two related issues:

1. Validation failures don't trigger proper repair loops
2. Phase 2b synthesis underuses available context (context starvation)

## Problem Analysis

### Current Flow (Broken)

```
generate → validate → if fail: send validation log to LLM → regenerate → repeat up to N times → report failure
```

Issues:

- Most failures can be fixed deterministically without LLM
- Failures aren't classified; all get same repair treatment
- No quarantine mechanism for unfixable pages
- Repair prompt doesn't include enough context for the LLM to succeed
- ~2.5k token prompts when we have 8-12k token budget

### Target Flow

```
generate → validate → classify failures → deterministic fixes → revalidate
→ if still failing: enrich context + targeted LLM repair → revalidate
→ if still failing after N attempts: quarantine with specific reason
```

---

## Part 1: Failure Classification and Deterministic Repair

### Failure Categories

Each validation failure should be classified into a category that determines the repair strategy:

```python
@dataclass
class ValidationFailure:
    category: FailureCategory
    page: str
    row: int | None  # For row-specific failures
    field: str | None  # For field-specific failures
    message: str
    deterministic_fix: bool  # Can this be fixed without LLM?
    fix_hint: str | None  # Specific repair instruction

class FailureCategory(Enum):
    # Deterministically fixable
    FRONTMATTER_MISSING_KEY = "frontmatter_missing_key"
    FRONTMATTER_BAD_VALUE = "frontmatter_bad_value"
    MISSING_SOURCE_LINK = "missing_source_link"
    MALFORMED_TABLE = "malformed_table"
    BAD_LOCATOR_FORMAT = "bad_locator_format"
    MISSING_SOURCE_SECTION = "missing_source_section"
    PLACEHOLDER_TEXT = "placeholder_text"
    EMPTY_SECTION = "empty_section"

    # Partially deterministic
    LOCATOR_OUT_OF_RANGE = "locator_out_of_range"  # Can suggest valid locators
    EVIDENCE_MISMATCH = "evidence_mismatch"  # Can refresh from source
    DUPLICATE_HEADING = "duplicate_heading"  # Can merge/rename

    # Requires LLM
    TOO_FEW_CLAIMS = "too_few_claims"
    WEAK_CLAIM_TEXT = "weak_claim_text"
    CLAIM_COPIES_EVIDENCE = "claim_copies_evidence"
    UNSUPPORTED_CLAIM = "unsupported_claim"
    BROKEN_WIKI_LINK = "broken_wiki_link"  # May need content decision
    TITLE_SLUG_MISMATCH = "title_slug_mismatch"
```

### Deterministic Repair Functions

For JSON schema output, many fixes are trivial mutations:

```python
def repair_frontmatter_missing_key(page: WikiPageSchema, key: str, default: Any) -> WikiPageSchema:
    """Add missing frontmatter key with sensible default."""
    setattr(page.frontmatter, key, default)
    return page

def repair_missing_source_link(page: WikiPageSchema, slug: str) -> WikiPageSchema:
    """Add source link if missing from sources list."""
    source_path = f"../sources/{slug}.md"
    if source_path not in page.frontmatter.sources:
        page.frontmatter.sources.append(source_path)
    return page

def repair_missing_source_section(page: WikiPageSchema, slug: str) -> WikiPageSchema:
    """Add Source pages section if missing."""
    has_source_section = any(
        "source" in s.heading.lower() and "backed" not in s.heading.lower()
        for s in page.sections
    )
    if not has_source_section:
        page.sections.append(Section(
            heading="Source pages",
            level=2,
            content=f"- [Source](../sources/{slug}.md)"
        ))
    return page

def repair_placeholder_text(page: WikiPageSchema) -> WikiPageSchema:
    """Remove placeholder text patterns."""
    for section in page.sections:
        if section.content:
            section.content = re.sub(r"Page title", "", section.content)
    return page

def repair_evidence_from_bank(
    page: WikiPageSchema,
    evidence_bank: EvidenceBankResult
) -> WikiPageSchema:
    """Re-expand evidence from bank to fix mismatches."""
    for claim in page.claims:
        for eid in claim.evidence_ids:
            if eid not in evidence_bank.items:
                # Remove invalid evidence IDs
                claim.evidence_ids = [e for e in claim.evidence_ids if e in evidence_bank.items]
    return page

def repair_locator_out_of_range(
    page: WikiPageSchema,
    evidence_bank: EvidenceBankResult,
    allowed_ranges: list[tuple[int, int]]
) -> list[str]:
    """
    For locators outside allowed range, return suggested alternative locators.
    Returns hints for LLM repair prompt rather than modifying directly.
    """
    hints = []
    for claim in page.claims:
        for eid in claim.evidence_ids:
            if eid in evidence_bank.items:
                item = evidence_bank.items[eid]
                locator = item.locator
                # Parse locator and check range
                match = re.search(r"L(\d+)", locator)
                if match:
                    line = int(match.group(1))
                    in_range = any(start <= line <= end for start, end in allowed_ranges)
                    if not in_range:
                        # Find alternative evidence in range
                        in_range_ids = [
                            e.id for e in evidence_bank.items.values()
                            if any(start <= parse_line(e.locator) <= end for start, end in allowed_ranges)
                        ]
                        if in_range_ids:
                            hints.append(f"Claim '{claim.claim[:50]}...' uses {eid} outside allowed range. "
                                       f"Consider using: {', '.join(in_range_ids[:3])}")
    return hints
```

### Repair Pipeline

```python
def repair_pipeline(
    page: WikiPageSchema,
    failures: list[ValidationFailure],
    evidence_bank: EvidenceBankResult,
    slug: str,
) -> tuple[WikiPageSchema, list[ValidationFailure]]:
    """
    Apply deterministic fixes and return remaining failures that need LLM.
    """
    remaining: list[ValidationFailure] = []

    for failure in failures:
        if failure.category == FailureCategory.FRONTMATTER_MISSING_KEY:
            page = repair_frontmatter_missing_key(page, failure.field, get_default(failure.field))
        elif failure.category == FailureCategory.MISSING_SOURCE_LINK:
            page = repair_missing_source_link(page, slug)
        elif failure.category == FailureCategory.MISSING_SOURCE_SECTION:
            page = repair_missing_source_section(page, slug)
        elif failure.category == FailureCategory.PLACEHOLDER_TEXT:
            page = repair_placeholder_text(page)
        elif failure.category == FailureCategory.EVIDENCE_MISMATCH:
            page = repair_evidence_from_bank(page, evidence_bank)
        else:
            # Needs LLM
            remaining.append(failure)

    return page, remaining
```

---

## Part 2: Richer Synthesis Context

### Current Context (~2.5k tokens)

```
- System prompt (~500 tokens)
- Evidence bank (~10 items × 150 chars = ~400 tokens)
- User prompt template (~800 tokens)
- Selected candidate info (~200 tokens)
```

### Target Context (~6-8k tokens)

```
- System prompt (~500 tokens)
- Page schema + examples (~400 tokens)
- Evidence bank with context (~10 items × 300 chars = ~800 tokens)
- Local source excerpts around evidence (~1500 tokens)
- Neighboring claims from adjacent topics (~600 tokens)
- Source-level summary (~300 tokens)
- Validator requirements summary (~300 tokens)
- Known failure patterns (~200 tokens)
- Previous attempt failures if repair (~400 tokens)
```

### Evidence Bank Enhancement

Current: Just the evidence text

```
[E01] normalized:L1275 "Functions containing free variables are called closures."
```

Enhanced: Evidence with surrounding context

```
[E01] normalized:L1275
Evidence: "Functions containing free variables are called closures."
Context (L1272-L1278):
  > If we're discussing the term "closure" in relation to JavaScript functions,
  > named x, the variable x isn't bound in this function, which makes it "free."
  > • Functions containing one or more free variables are called closures.
  > • All functions in JavaScript are closures, since all functions have at least
  > one free variable (the built-in function and object references).
```

### Implementation

```python
@dataclass
class EnrichedEvidenceItem:
    """Evidence item with surrounding context."""
    id: str
    locator: str
    text: str
    context_before: str  # 2-3 lines before
    context_after: str   # 2-3 lines after
    candidate: str

def build_enriched_evidence_bank(
    source_lines: list[str],
    extraction_claims: list[dict],
    selected_candidates: list[RelatedCandidate],
    context_lines: int = 3,
) -> EnrichedEvidenceBankResult:
    """Build evidence bank with surrounding source context."""
    items = {}
    evidence_id = 1

    for candidate in selected_candidates:
        matched_claims = match_claims_to_candidate(extraction_claims, candidate)

        for claim in matched_claims[:10]:
            locator = claim.get("locator", "")
            evidence = claim.get("evidence", "")

            # Parse line number from locator
            line = parse_line_from_locator(locator)
            if line is None:
                continue

            # Get surrounding context
            start = max(0, line - context_lines - 1)
            end = min(len(source_lines), line + context_lines)
            context_before = "\n".join(source_lines[start:line-1])
            context_after = "\n".join(source_lines[line:end])

            eid = f"E{evidence_id:02d}"
            evidence_id += 1

            items[eid] = EnrichedEvidenceItem(
                id=eid,
                locator=locator,
                text=evidence,
                context_before=context_before,
                context_after=context_after,
                candidate=candidate.path,
            )

    return EnrichedEvidenceBankResult(items=items, ...)


def render_enriched_evidence_bank(bank: EnrichedEvidenceBankResult) -> str:
    """Render evidence bank with context for prompt."""
    sections = []
    for eid, item in sorted(bank.items.items()):
        sections.append(f"[{eid}] {item.locator}")
        sections.append(f'Evidence: "{item.text}"')
        if item.context_before.strip():
            sections.append(f"Context before:\n  > {item.context_before.replace(chr(10), chr(10) + '  > ')}")
        if item.context_after.strip():
            sections.append(f"Context after:\n  > {item.context_after.replace(chr(10), chr(10) + '  > ')}")
        sections.append("")
    return "\n".join(sections)
```

### Neighboring Claims

Include claims from adjacent topics to help the model understand boundaries:

```python
def get_neighboring_claims(
    all_claims: list[dict],
    current_topic: str,
    limit: int = 5,
) -> str:
    """Get claims from adjacent topics for context."""
    other_topics = {}
    for claim in all_claims:
        topic = claim.get("topic", "")
        if topic.lower() != current_topic.lower():
            if topic not in other_topics:
                other_topics[topic] = []
            other_topics[topic].append(claim)

    sections = ["## Claims from adjacent topics (for boundary awareness)"]
    for topic, claims in list(other_topics.items())[:3]:
        sections.append(f"\n### {topic}")
        for c in claims[:limit]:
            sections.append(f"- {c.get('claim', '')[:100]}")

    return "\n".join(sections)
```

### Validator Requirements Summary

Distill key requirements for the prompt:

```python
VALIDATOR_REQUIREMENTS = """
## Validation requirements (your output will be checked against these)

1. **Frontmatter**: Must include title, type, tags, status, last_updated, sources
2. **Source link**: Must have at least one source in frontmatter.sources
3. **Source pages section**: Required section linking to source page(s)
4. **Evidence table**: Minimum 3 rows with Claim|Evidence|Locator|Source columns
5. **Locator format**: Must be `normalized:L123` or `normalized:L123-L456`
6. **Locator range**: All locators must be within declared source_ranges
7. **Claim synthesis**: Claims must be YOUR words, not copied from evidence
8. **No placeholders**: No "Page title" or template text
9. **No empty sections**: Every section needs content or "None."
"""
```

### Known Failure Patterns

Include examples of common mistakes to avoid:

```python
COMMON_FAILURES = """
## Common mistakes to avoid

BAD claim (copies evidence):
| Functions containing free variables are closures. | "Functions containing free variables are closures." |

GOOD claim (synthesizes):
| Functions that reference variables from outer scopes are termed closures. | "Functions containing free variables are closures." |

BAD locator (outside range):
| ... | `normalized:L1709` | (when source_ranges is L1260-L1290)

BAD source cell (plain text):
| ... | ../sources/js-allonge.md |

GOOD source cell (link):
| ... | [Source](../sources/js-allonge.md) |
"""
```

---

## Part 3: Repair Prompt Enhancement

When LLM repair is needed, provide targeted context:

````python
def build_repair_prompt(
    page: WikiPageSchema,
    failures: list[ValidationFailure],
    evidence_bank: EnrichedEvidenceBankResult,
    previous_attempts: list[str],  # Previous validation logs
    slug: str,
) -> str:
    """Build targeted repair prompt with rich context."""

    sections = []

    # 1. Specific failures to fix
    sections.append("## Failures to fix")
    for f in failures:
        sections.append(f"- {f.category.value}: {f.message}")
        if f.fix_hint:
            sections.append(f"  Hint: {f.fix_hint}")

    # 2. Current page state (JSON)
    sections.append("\n## Current page (fix the issues above)")
    sections.append("```json")
    sections.append(json.dumps(asdict(page), indent=2))
    sections.append("```")

    # 3. Evidence bank with context
    sections.append("\n## Available evidence")
    sections.append(render_enriched_evidence_bank(evidence_bank))

    # 4. Validator requirements
    sections.append(VALIDATOR_REQUIREMENTS)

    # 5. Common failures
    sections.append(COMMON_FAILURES)

    # 6. Previous attempt failures (if any)
    if previous_attempts:
        sections.append("\n## Previous attempts (don't repeat these mistakes)")
        for i, attempt in enumerate(previous_attempts[-2:], 1):
            sections.append(f"\nAttempt {i}:")
            sections.append(attempt[:500])

    return "\n".join(sections)
````

---

## Part 4: Quarantine Mechanism

Pages that can't be fixed after N attempts should be quarantined:

```python
@dataclass
class QuarantinedPage:
    path: str
    slug: str
    reason: str
    failures: list[ValidationFailure]
    attempts: int
    last_attempt: str  # ISO timestamp

def quarantine_page(
    page_path: str,
    slug: str,
    failures: list[ValidationFailure],
    attempts: int,
) -> QuarantinedPage:
    """Move page to quarantine with detailed failure info."""

    # Determine primary reason
    if any(f.category == FailureCategory.TOO_FEW_CLAIMS for f in failures):
        reason = "insufficient_evidence"
    elif any(f.category == FailureCategory.LOCATOR_OUT_OF_RANGE for f in failures):
        reason = "evidence_outside_source_range"
    elif any(f.category == FailureCategory.UNSUPPORTED_CLAIM for f in failures):
        reason = "claims_not_grounded"
    else:
        reason = "validation_failures"

    return QuarantinedPage(
        path=page_path,
        slug=slug,
        reason=reason,
        failures=failures,
        attempts=attempts,
        last_attempt=datetime.now().isoformat(),
    )

def save_quarantine_report(quarantined: list[QuarantinedPage], output: Path):
    """Save quarantine report for human review."""
    lines = ["# Quarantined Pages", "", f"Generated: {date.today().isoformat()}", ""]

    for q in quarantined:
        lines.append(f"## {q.path}")
        lines.append(f"- Reason: {q.reason}")
        lines.append(f"- Attempts: {q.attempts}")
        lines.append(f"- Failures:")
        for f in q.failures:
            lines.append(f"  - {f.category.value}: {f.message}")
        lines.append("")

    output.write_text("\n".join(lines))
```

---

## Part 5: Updated Phase 2 Flow

```python
def run_single_candidate_with_repair(
    worktree: Path,
    slug: str,
    candidate: RelatedCandidate,
    evidence_bank: EnrichedEvidenceBankResult,
    max_deterministic_repairs: int = 3,
    max_llm_repairs: int = 2,
) -> tuple[WikiPageSchema | None, list[ValidationFailure], bool]:
    """
    Generate page with full repair pipeline.

    Returns:
        Tuple of (final_page, remaining_failures, success)
    """

    # 1. Initial generation with rich context
    page = generate_with_rich_context(
        worktree, slug, candidate, evidence_bank
    )

    # 2. Validate and classify failures
    failures = validate_and_classify(page, slug, evidence_bank)

    if not failures:
        return page, [], True

    # 3. Deterministic repair loop
    for _ in range(max_deterministic_repairs):
        page, remaining = repair_pipeline(page, failures, evidence_bank, slug)

        # Re-render and revalidate
        render_page_to_file(page, worktree, evidence_bank, slug)
        failures = validate_and_classify(page, slug, evidence_bank)

        if not failures:
            return page, [], True

        # Stop if no progress
        if len(failures) >= len(remaining):
            break

    # 4. LLM repair loop for remaining failures
    previous_attempts = []
    for attempt in range(max_llm_repairs):
        repair_prompt = build_repair_prompt(
            page, failures, evidence_bank, previous_attempts, slug
        )

        page = llm_repair(repair_prompt, evidence_bank, slug)

        # Record attempt
        previous_attempts.append(format_failures(failures))

        # Revalidate
        failures = validate_and_classify(page, slug, evidence_bank)

        if not failures:
            return page, [], True

    # 5. Quarantine if still failing
    return page, failures, False
```

---

## Implementation Plan

### Phase 1: Failure Classification (tools/wiki_failure_classifier.py) ✓ IMPLEMENTED

- Parse validation output into structured failures
- Classify each failure by category
- Mark which can be fixed deterministically

### Phase 2: Deterministic Repair (tools/wiki_deterministic_repair.py) ✓ IMPLEMENTED

- Implement repair functions for each deterministic category
- Operate on WikiPageSchema directly
- Re-render after repairs

### Phase 3: Enriched Evidence Bank (tools/wiki_phase2_benchmark.py) ✓ IMPLEMENTED

- Add context lines around evidence (±3 lines)
- Include neighboring claims
- Add validator requirements summary

### Phase 4: Repair Pipeline Integration (tools/wiki_phase2_single.py) ✓ IMPLEMENTED

- Added `attempt_deterministic_repairs()` function
- Integrated into validation loop (runs before LLM repair)
- Build targeted repair prompts with failure-specific hints
- Track previous attempts

### Phase 5: Quarantine Mechanism (tools/wiki_quarantine.py)

- Quarantine unfixable pages
- Generate review report
- Track quarantine reasons

### Phase 6: Integration

- Update wiki_ingest.py to handle quarantine
- Add quarantine report to maintenance

---

## Success Metrics

1. **Deterministic fix rate**: % of failures fixed without LLM
2. **First-pass success rate**: % of pages passing validation on first LLM attempt
3. **Total success rate**: % of pages eventually passing (vs quarantined)
4. **Context utilization**: Token count in synthesis prompts (target: 6-8k)
5. **Quarantine rate**: % of pages quarantined (target: <10%)

---

## File Changes

| File                                     | Change                                           | Status |
| ---------------------------------------- | ------------------------------------------------ | ------ |
| `tools/wiki_failure_classifier.py`       | NEW: Classify validation failures                | ✓ Done |
| `tools/wiki_deterministic_repair.py`     | NEW: Deterministic repair functions              | ✓ Done |
| `tools/wiki_quarantine.py`               | NEW: Quarantine mechanism                        | TODO   |
| `tools/wiki_phase2_benchmark.py`         | MODIFY: Enriched evidence bank (±3 line context) | ✓ Done |
| `tools/wiki_phase2_single.py`            | MODIFY: New repair pipeline integration          | ✓ Done |
| `tools/wiki_page_schema.py`              | MODIFY: Add repair helpers                       | N/A    |
| `tools/wiki_check_synthesis.py`          | MODIFY: Return structured failures               |
| `tools/prompts/system-synthesis-json.md` | MODIFY: Add validation requirements              |
| `wiki/_quarantine-report.md`             | NEW: Quarantine tracking                         |
