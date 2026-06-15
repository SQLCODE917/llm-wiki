# Semantic Lint for Staleness and Data Gaps

## Context & Problem

Current lint measures links, orphans, index drift, citation evidence, and some
salience. The reference lint workflow also calls for stale/superseded claims and
data gaps that could become future source work. M5 needs a bounded report-only
semantic lint pass before letting the model rewrite pages for these subtler
issues.

Pattern excerpts addressed from `docs/llm-wiki.md`:

- "noting where new data contradicts old claims"
- "strengthening or challenging the evolving synthesis"
- "Look for: contradictions between pages, stale claims..."
- "missing cross-references, data gaps"

## Goals

- Surface likely stale or superseded claims.
- Surface data gaps and source-search candidates.
- Keep semantic lint bounded and report-first.
- Feed findings into curator status.

## Non-Goals & Forbidden Approaches

Non-goals:

- No live web search in this TDD.
- No automatic page rewrites.
- No global proof that no stale claims exist.
- No scheduled maintenance.

Forbidden approaches:

- Do not let the model invent missing sources.
- Do not treat "mentioned often" as proof a page must exist.
- Do not mix semantic-staleness findings into deterministic link pass counts.

## Requirements

- A deterministic selector proposes a small audit set from pages with overlapping
  sources, repeated topics, old updated dates, contradiction findings, or high
  salience gaps.
- The model records findings as structured items with type `stale_claim`,
  `possible_supersession`, or `data_gap`.
- Findings include affected page, rationale, evidence consulted, and curator
  next action.
- The pass writes a synthesis report and appends `log.md`.

## Invariants

- The command does not edit ordinary wiki pages.
- Raw sources remain immutable.
- Findings are leads for curator review, not truth declarations.
- Existing deterministic lint remains fast and available separately.

## Proposed Architecture

```
+---------------+      +----------------+      +---------------+
| audit selector|----->| semantic model |----->| report/status |
+---------------+      +----------------+      +---------------+
        |                       |
        v                       v
  wiki/link/evidence       read_page tools
```

The selector chooses bounded candidates. The model reads pages and records
structured semantic findings. Curator status summarizes the latest report.

## Key Interactions

Possible supersession:

```
Selector -> Model: overlapping pages
Model -> read_page: older and newer pages
Model -> record_semantic_finding: possible_supersession
```

Data gap:

```
Selector -> Model: high-salience missing concept
Model -> read_page: related pages
Model -> record_semantic_finding: data_gap
```

No findings:

```
Model -> finish_semantic_lint: audited scope and uncertainty
Harness -> wiki: report page
```

## Data Model

- `SemanticLintCandidate`: reason, page names, optional missing concept.
- `SemanticFinding`: type, pages, rationale, evidence, recommended action.
- Report page: harness-owned synthesis page, exempt from orphan checks.

## APIs / Interfaces

- New CLI command: `llmwiki semantic-lint`.
- Option: `--max-items N`, with a small default.
- Model tool: `record_semantic_finding`.
- Terminal tool: `finish_semantic_lint`.

## Behavior & Domain Rules

- Stale means a page likely needs review because newer wiki content changes its
  context.
- Data gap means the wiki lacks enough source-backed coverage for a recurring
  question or concept.
- Source-search suggestions must be framed as suggestions, never as facts.

Examples:

- Older page says a feature is introduced in one version; newer page cites a
  conflicting version -> possible_supersession.
- A term appears in salience but has no page and no inbound links -> data_gap.
- Two pages use different wording for compatible claims -> no finding.

## Acceptance Criteria

- Tests prove candidate selection is bounded and reasoned.
- Tests prove structured findings validate affected page names.
- Tests prove report includes audited, skipped, and uncertainty sections.
- Curator status includes latest semantic-lint summary when present.
- Existing `llmwiki lint` behavior remains unchanged.

## Cross-Cutting Concerns

Error handling: a model that records no findings still produces a useful scope
report so repeated runs can be compared.

## Reference Implementations

- Current maintenance report: `harness/src/llmwiki/domain/maintenance.py`.
- Current salience signal: `harness/src/llmwiki/domain/salience.py`.
- Backup semantic overlap idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/tools/wiki_semantic_lint.py`.

## Alternatives Considered

- Add web search immediately - rejected because source curation remains human-led.
- Fold all semantic findings into normal lint - rejected because local model
  budget should stay predictable.

## Halt Conditions

- If implementation needs internet access to decide a finding, stop and split
  source-discovery into a separate design.

## Implementation Notes

- Implemented `uv run llmwiki semantic-lint` with `--max-items`.
- Added deterministic candidate selection in `llmwiki.domain.semantic_lint`.
- Added `record_semantic_finding` with fixed finding types:
  `stale_claim`, `possible_supersession`, and `data_gap`.
- Added `wiki-semantic-lint` as a harness-owned synthesis report page exempt
  from graph health checks.
- Curator status now includes a latest semantic-lint summary when the report
  page exists.
- The selector deliberately ignores broad shared book-level sources by default;
  exact citation overlap, direct links, updated-date differences, and
  candidate-backlog data gaps carry the audit.

## Verification Plan

- Unit tests for bounded candidate selection, broad-source filtering, backlog
  data gaps, and report rendering.
- Session E2E tests for structured finding recording, no-candidate
  short-circuiting, and invalid page recovery.
- CLI tests for parser arguments and non-positive `--max-items`.
- Live `uv run llmwiki semantic-lint --max-items 2` over the current wiki,
  followed by report inspection.

## Verification Results

- Focused domain/session/maintenance/CLI tests pass.
- First live run completed but exposed an over-broad selector: broad
  `raw/javascriptallonge.pdf` overlap produced 1,749 candidate pairs and weak
  leads.
- Tightened selector to prefer exact citations/page-range sources and direct
  links; second live run produced 74 candidates and concrete stale-claim leads
  involving `partial-application`, `unary-functions`, and
  `javascriptallonge-recipes-with-basic-functions`.
- No ordinary wiki pages were edited; only `wiki-semantic-lint` and `wiki/log.md`
  were updated by the live command.
