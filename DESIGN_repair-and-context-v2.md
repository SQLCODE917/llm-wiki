# Design: Validation-Driven Wiki Compilation Pipeline (v2)

> **Framing correction**: This is not "regenerate until valid." This is
> **compile → validate → patch → prove → accept/quarantine**.

This document addresses two issues:

1. Validation failures don't trigger proper repair loops
2. Phase 2b synthesis underuses available context (context starvation)

---

## Design Principles

### 1. The LLM should not write markdown

The LLM produces **structured schema** (JSON). Python **renders markdown deterministically**.

This removes entire classes of failures:

- Malformed tables → impossible (renderer handles tables)
- Bad source cells → impossible (renderer expands from evidence bank)
- Missing frontmatter keys → impossible (renderer always emits required keys)

### 2. Validators return structured failures

Do NOT parse log text. Validators return `list[ValidationFailure]` directly.

```python
# BAD: validator prints → classifier regex parses → repair acts
# GOOD: validator emits structured → report renders → repair acts on structure
```

### 3. Invalid pages never touch `wiki/`

Use staging paths:

```
.tmp/phase2/pages/<slug>.json      # Schema WIP
.tmp/phase2/rendered/<slug>.md     # Rendered WIP
.tmp/phase2/failed/<slug>.md       # Failed attempts
wiki/concepts/<slug>.md            # Only after validation passes
wiki/_quarantine-report.md         # Quarantine tracking
```

### 4. Evidence IDs are the only model output for citations

The model returns:

```json
{ "claim": "...", "evidence_ids": ["E01", "E04"] }
```

The renderer emits:

```markdown
| Claim | Evidence | Locator | Source |
| ... | "..." | L123 | [Source](../sources/slug.md) |
```

The model should **never** write quote text, locators, or source links.

---

## Architecture

### Two-Layer Validation

```
┌─────────────────────────────────────────────────────────┐
│ Schema Validation                                       │
│ - required fields present                               │
│ - enum values valid                                     │
│ - evidence_ids exist in bank                            │
│ - list lengths (min claims)                             │
│ - slug/title consistency                                │
└─────────────────────────────────────────────────────────┘
                           ↓ render
┌─────────────────────────────────────────────────────────┐
│ Rendered Markdown Validation                            │
│ - frontmatter YAML valid                                │
│ - table columns correct                                 │
│ - wiki links resolvable                                 │
│ - evidence quotes appear at locators                    │
│ - no placeholder text                                   │
└─────────────────────────────────────────────────────────┘
```

Some failures become **renderer bugs** rather than LLM failures:

- `MALFORMED_TABLE` with deterministic rendering → fix renderer
- `BAD_SOURCE_CELL` → renderer should always emit correct format

### Revised Failure Taxonomy

#### Deterministically Fixable (no LLM needed)

```python
# Frontmatter
FRONTMATTER_MISSING_KEY      # add with default
FRONTMATTER_BAD_VALUE        # fix to valid enum
MISSING_SOURCE_LINK          # add from slug
MISSING_TAGS                 # add empty list
BAD_STATUS                   # default to "draft"
BAD_LAST_UPDATED             # set to today

# Structure
MISSING_SOURCE_SECTION       # add templated section
PLACEHOLDER_TEXT             # regex remove
EMPTY_SECTION                # fill with "None."

# Evidence binding
INVALID_EVIDENCE_ID          # remove from list
BAD_LOCATOR_FORMAT           # canonicalize from bank
```

#### Renderer/Schema Bugs (fix code, not LLM)

```python
MALFORMED_TABLE              # renderer bug
MISSING_TABLE_COLUMN         # renderer bug
BAD_SOURCE_CELL              # renderer should handle
BAD_MARKDOWN_LINK            # renderer bug for known sources
```

If these appear with deterministic rendering, the renderer is wrong.

#### Evidence-Selection Failures (rebuild bank, not LLM repair)

```python
LOCATOR_OUT_OF_RANGE         # filter bank → rerender
EVIDENCE_TEXT_MISMATCH       # refresh from bank
QUOTE_NOT_FOUND_AT_LOCATOR   # bank construction bug
EVIDENCE_ID_OUTSIDE_RANGE    # filter + rerender
TOO_FEW_VALID_EVIDENCE       # expand range or quarantine
```

Flow for `LOCATOR_OUT_OF_RANGE`:

```
→ filter evidence bank to allowed ranges
→ if enough evidence remains, rerender claims from valid evidence
→ if not enough evidence, expand source_ranges or quarantine
```

The model should **not** invent alternate locators.

#### Semantic LLM Failures (needs LLM repair)

```python
TOO_FEW_CLAIMS               # generate more
WEAK_CLAIM_TEXT              # rewrite stronger
CLAIM_COPIES_EVIDENCE        # synthesize in own words
UNSUPPORTED_CLAIM            # find evidence or remove
CLAIM_TOO_BROAD              # narrow scope
CLAIM_OFF_TOPIC              # refocus
CLAIM_DUPLICATES_EXISTING    # dedupe with existing page
TITLE_SLUG_MISMATCH          # semantic decision
```

#### Graph/Wiki Maintenance (Phase 3 or health pass)

```python
ORPHAN_PAGE                  # add links
MISSING_BACKLINK             # add to source page
DUPLICATE_CONCEPT            # merge pages
CONFLICTS_WITH_EXISTING      # resolve contradiction
```

---

## Revised Flow

```python
def run_single_candidate_with_repair(...):
    # 1. Build enriched context within budget
    evidence_bank = build_enriched_evidence_bank(...)
    context_pack = build_budgeted_context_pack(...)

    # 2. Generate schema (not markdown)
    page = llm_generate_schema(context_pack)

    for stage in range(max_total_cycles):
        # 3. Schema validation
        schema_failures = validate_schema(page, evidence_bank, slug)

        if schema_failures:
            page, changed = deterministic_schema_repair(
                page, schema_failures, evidence_bank, slug
            )
            if changed:
                continue

        # 4. Render markdown
        markdown = render_page(page, evidence_bank, slug)

        # 5. Rendered markdown validation
        render_failures = validate_rendered_markdown(markdown, evidence_bank, slug)

        all_failures = schema_failures + render_failures

        if not all_failures:
            accept_page(markdown, page)
            return page, [], True

        # 6. Partition failures
        deterministic, evidence_selection, semantic = partition_failures(all_failures)

        # 7. Deterministic repair
        page, changed = deterministic_repair(page, deterministic, evidence_bank, slug)
        if changed:
            continue

        # 8. Evidence selection repair
        if evidence_selection:
            evidence_bank = rebuild_filtered_evidence_bank(evidence_bank, page)
            if has_sufficient_evidence(evidence_bank, page):
                continue
            # else fall through to quarantine as insufficient_evidence

        # 9. LLM repair for semantic failures
        if semantic and llm_repairs_remaining:
            repair_context = build_targeted_repair_context(
                page=page,
                failures=semantic,
                evidence_bank=evidence_bank,
                context_pack=context_pack,
                previous_attempts=attempt_log,
            )
            page = llm_repair_schema(repair_context)
            continue

        # 10. Quarantine
        quarantine(page, markdown, all_failures)
        return page, all_failures, False
```

Key property:

- The renderer is deterministic
- The validator returns structured failures
- The LLM only edits semantic schema fields

---

## Evidence Bank Enhancement

### Current (too thin)

```
[E01] normalized:L1275 "Functions containing free variables are called closures."
```

### Enhanced (with context)

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

### Context Extraction (fixed indexing)

Locators are 1-indexed, arrays are 0-indexed:

```python
def extract_context(source_lines: list[str], line: int, context_lines: int = 3):
    """Extract evidence line with surrounding context.

    Args:
        source_lines: 0-indexed array
        line: 1-indexed line number from locator
        context_lines: lines before/after to include
    """
    idx = line - 1  # Convert to 0-indexed

    before_start = max(0, idx - context_lines)
    before = source_lines[before_start:idx]

    hit = source_lines[idx] if idx < len(source_lines) else ""

    after_end = min(len(source_lines), idx + 1 + context_lines)
    after = source_lines[idx + 1:after_end]

    return EnrichedContext(
        before="\n".join(before),
        evidence_line=hit,
        after="\n".join(after),
    )
```

### Neighboring Claims Selection

Use **source proximity** not arbitrary dict order:

```python
def get_neighboring_claims(
    all_claims: list[dict],
    current_topic: str,
    current_range: tuple[int, int],
    proximity_lines: int = 100,
) -> list[dict]:
    """Get claims from adjacent source regions.

    Include claims from ±100 source lines around current range,
    excluding claims belonging to current topic.
    """
    neighbors = []
    start, end = current_range

    for claim in all_claims:
        if claim.get("topic", "").lower() == current_topic.lower():
            continue

        # Parse claim's locator
        locator = claim.get("locator", "")
        claim_line = parse_line_from_locator(locator)
        if claim_line is None:
            continue

        # Check proximity
        if (start - proximity_lines) <= claim_line <= (end + proximity_lines):
            neighbors.append(claim)

    return neighbors
```

Prompt framing:

```
These claims belong to other pages. Do not absorb them unless needed for contrast.
```

---

## Context Budget Packer

Explicit token allocation, not hardcoded sections:

```python
@dataclass
class ContextBudget:
    total_tokens: int = 9000

    # Fixed allocations
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

def build_budgeted_context_pack(
    budget: ContextBudget,
    evidence_bank: EvidenceBankResult,
    source_text: str,
    candidate: RelatedCandidate,
    related_pages: list[str],
    repair_failures: list[ValidationFailure] | None = None,
) -> tuple[str, ContextStats]:
    """Build context pack within token budget.

    Returns context string and stats about what was included/dropped.
    """
    sections = []
    stats = ContextStats()

    # Fixed sections (always included)
    sections.append(render_system_schema())
    sections.append(render_validator_requirements())
    sections.append(render_candidate_intent(candidate))

    # Variable sections (trimmed to fit)
    remaining = budget.total_tokens - budget.system_schema - budget.validator_requirements - budget.candidate_intent

    # Evidence bank (priority 1)
    evidence_text, evidence_tokens = render_evidence_bank_budgeted(
        evidence_bank, min(remaining, budget.evidence_bank)
    )
    sections.append(evidence_text)
    remaining -= evidence_tokens
    stats.evidence_tokens = evidence_tokens

    # Local excerpts (priority 2)
    if remaining > 200:
        excerpts_text, excerpt_tokens = render_local_excerpts_budgeted(
            source_text, candidate, min(remaining, budget.local_excerpts)
        )
        sections.append(excerpts_text)
        remaining -= excerpt_tokens
        stats.excerpt_tokens = excerpt_tokens

    # Neighboring claims (priority 3)
    if remaining > 200:
        neighbors_text, neighbor_tokens = render_neighbors_budgeted(
            candidate, min(remaining, budget.neighboring_claims)
        )
        sections.append(neighbors_text)
        remaining -= neighbor_tokens

    # Related wiki summaries (priority 4, can be dropped)
    if remaining > 200 and related_pages:
        wiki_text, wiki_tokens = render_related_wiki_budgeted(
            related_pages, min(remaining, budget.related_wiki)
        )
        sections.append(wiki_text)
        remaining -= wiki_tokens
    else:
        stats.dropped_sections.append("related_wiki_summaries")

    # Repair context (only for repair prompts)
    if repair_failures and remaining > 100:
        repair_text = render_repair_context(repair_failures)
        sections.append(repair_text)

    stats.total_tokens = budget.total_tokens - remaining
    stats.actual_tokens = count_tokens("\n".join(sections))

    return "\n".join(sections), stats
```

Stats report:

```json
{
  "target_tokens": 9000,
  "actual_tokens": 8420,
  "evidence_tokens": 3650,
  "excerpt_tokens": 2100,
  "validator_tokens": 380,
  "repair_tokens": 0,
  "dropped_sections": ["related_wiki_summaries"]
}
```

---

## LLM Repair Prompt Design

### Restrict Editable Fields

The model receives only what it can edit:

```
You may edit only:
- title
- summary
- claims[].claim
- claims[].evidence_ids
- related_pages
- tags

You must NOT edit:
- slug
- source paths
- locators
- evidence quote text
- generated timestamps
```

### Patch Format (preferred)

Instead of full regeneration:

```json
{
  "replace_claims": [
    {
      "claim_index": 2,
      "claim": "Closures capture variables from enclosing scopes.",
      "evidence_ids": ["E03", "E05"]
    }
  ],
  "remove_claim_indices": [4],
  "add_claims": [
    {
      "claim": "All JavaScript functions are closures.",
      "evidence_ids": ["E08"]
    }
  ]
}
```

Apply patch deterministically.

---

## Staging and Acceptance

### Directory Structure

```
.tmp/phase2/
├── pages/
│   └── closures.json          # Schema WIP
├── rendered/
│   └── closures.md            # Rendered WIP
├── failed/
│   └── closures-attempt-1.md  # Failed attempts
└── stats/
    └── closures.json          # Context/token stats

wiki/
├── concepts/
│   └── closures.md            # Only after acceptance
└── _quarantine-report.md      # Quarantine tracking
```

### Acceptance Criteria

Page is accepted only when:

1. Schema validation passes
2. Rendered markdown validation passes
3. All failures resolved (none remaining)

```python
def accept_page(
    page: WikiPageSchema,
    markdown: str,
    staging_path: Path,
    target_path: Path,
):
    """Move validated page from staging to wiki."""
    # Final validation
    failures = validate_schema(page) + validate_rendered(markdown)
    if failures:
        raise AcceptanceError(f"Cannot accept page with {len(failures)} failures")

    # Archive staging artifacts
    archive_staging(staging_path)

    # Write to wiki
    target_path.write_text(markdown)

    # Update graph
    update_graph_for_page(target_path)
```

---

## Progress Detection

Use failure fingerprinting to detect progress:

```python
def failure_fingerprint(failures: list[ValidationFailure]) -> tuple:
    """Create hashable fingerprint of failure set."""
    return tuple(sorted(
        (f.category, f.page, f.row, f.field, f.message)
        for f in failures
    ))

def repair_loop_with_progress_detection(page, failures, ...):
    prev_fingerprint = failure_fingerprint(failures)

    for attempt in range(max_attempts):
        page, changed = repair_pipeline(page, failures, ...)
        failures = validate(page)

        new_fingerprint = failure_fingerprint(failures)

        if not failures:
            return page, True  # Success

        if new_fingerprint == prev_fingerprint and not changed:
            break  # No progress, stop trying

        prev_fingerprint = new_fingerprint

    return page, False  # Failed
```

---

## Metrics

### Core Metrics

```
structural_failure_rate:      failures from renderer/schema bugs
semantic_failure_rate:        unsupported/weak/copied claims
evidence_binding_success:     % claims with valid evidence IDs matching source
valid_after_deterministic:    % pages accepted without LLM repair
valid_after_targeted_repair:  % pages accepted after LLM repair
repair_regression_rate:       % repairs that fix one failure but add another
```

### Cost Metrics

```
average_accepted_page_cost:   generation + repair tokens per accepted page
context_useful_token_ratio:   evidence + excerpts / total prompt tokens
```

### Quality Metrics

```
quarantine_precision:         % quarantined pages that truly needed human review
false_acceptance_rate:        % accepted pages with semantic grounding problems
```

Track failure categories over time. The goal is to move failures from "mysterious LLM badness" into known buckets.

---

## Testable Hypotheses

### H1: Deterministic repair fixes most structural failures

**Prediction**: ≥70% of frontmatter/source/table/placeholder failures resolved without LLM.

### H2: Rich context improves first-pass semantic validity

**Prediction**: First-pass validation rate increases when prompts move from ~2.5k to ~6-8k tokens.

### H3: Schema-first output eliminates malformed markdown failures

**Prediction**: MALFORMED_TABLE, missing frontmatter, bad source-cell drop to near zero.

### H4: Evidence IDs only reduce quote/locator mismatch

**Prediction**: Evidence mismatch and locator mismatch decrease sharply with evidence-ID-only model output.

### H5: Targeted LLM repair is cheaper than full regeneration

**Prediction**: Repair token cost per accepted page drops while success rate rises.

### H6: Quarantine improves trust in accepted wiki

**Prediction**: Accepted pages have lower semantic error rate after quarantine.

---

## Implementation Order

1. **Schema-first synthesis and deterministic renderer** (foundation)
2. **Structured validator return types** (no log parsing)
3. **Failure taxonomy and deterministic repairs** (repair pipeline)
4. **Evidence bank canonical expansion** (evidence-ID-only)
5. **Context budget packer** (rich context)
6. **Staging paths** (invalid pages never touch wiki/)
7. **Targeted LLM patch repair** (semantic repair)
8. **Quarantine mechanism** (accept/reject boundary)
9. **Metrics dashboard** (observability)

---

## File Changes

| File                                 | Change                                        | Priority | Status  |
| ------------------------------------ | --------------------------------------------- | -------- | ------- |
| `tools/wiki_check_synthesis.py`      | Return `list[ValidationFailure]` not text     | P0       | TODO    |
| `tools/wiki_page_schema.py`          | Evidence-ID-only Claim, expand on render      | P0       | TODO    |
| `tools/wiki_phase2_single.py`        | Staging paths, new flow                       | P0       | Partial |
| `tools/wiki_failure_classifier.py`   | Revised taxonomy                              | P1       | ✓ Done  |
| `tools/wiki_deterministic_repair.py` | Match new taxonomy                            | P1       | ✓ Done  |
| `tools/wiki_phase2_benchmark.py`     | Fixed context indexing, enriched EvidenceItem | P1       | ✓ Done  |
| `tools/wiki_staging.py`              | NEW: Staging paths + quarantine               | P0       | ✓ Done  |
| `tools/wiki_context_packer.py`       | NEW: Budgeted context assembly                | P2       | ✓ Done  |
| `.tmp/phase2/`                       | NEW: Staging directory structure              | P0       | ✓ Done  |

---

## Key Constraints

1. **The LLM should not write markdown tables, source cells, locators, or evidence quotes.** It writes semantic schema fields and evidence IDs only.

2. **The validator emits structured failures directly.** Do not parse validation logs as source of truth.

3. **Invalid pages never touch `wiki/`.** Use staging, then accept or quarantine.

These constraints turn the design into a proper validation-driven compiler for wiki pages rather than a retry wrapper around an LLM.
