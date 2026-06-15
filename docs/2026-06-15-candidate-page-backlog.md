# Candidate Page Backlog

## Context & Problem

The current harness computes salience and orphan findings, but potential pages
do not persist as a durable backlog across ingests. The backup candidate tracker
accumulated candidate mentions, aliases, and promotion status. A smaller M5
version would help the wiki grow deliberately without creating thin pages for
every mentioned term.

Pattern excerpts addressed from `docs/llm-wiki.md`:

- "the LLM incrementally builds and maintains a persistent wiki"
- "Create pages for important entities or concepts that lack one"
- "important concepts mentioned but lacking their own page"
- "the tedious part ... is the bookkeeping"

## Goals

- Track recurring missing concepts/entities across operations.
- Deduplicate candidates by slug and alias.
- Give curator status a durable "what should become a page?" view.
- Keep promotion to real wiki pages explicit.

## Non-Goals & Forbidden Approaches

Non-goals:

- No automatic page creation from candidates.
- No old type-directory schema.
- No global ontology.
- No model-only candidate memory.

Forbidden approaches:

- Do not create broken `[[links]]` solely to remember candidates.
- Do not store candidate state only in transcripts.
- Do not promote candidates without curator or explicit model workflow action.

## Requirements

- Candidate state is deterministic harness-owned data.
- Candidates record name, slug, category guess, reasons, mention count, source
  pages, first seen, last seen, and status.
- Status values are finite and include at least `discovered`, `queued`,
  `promoted`, `rejected`, and `merged`.
- Curator status reports top candidates and recommended next action.
- Lint or maintenance can update candidates from salience and broken-link data.
- V1 updates candidates from explicit broken `[[links]]` during maintenance.
  Mention-only extraction from salience/source text is deferred until precision
  can be measured.

## Invariants

- Existing wiki pages remain canonical over candidates.
- Candidate backlog never counts as wiki knowledge.
- Promotion writes a real page through normal `write_page` workflow or a future
  explicit promotion command.
- Rejected/merged candidates remain auditable.

## Proposed Architecture

```
+--------------+       +-------------------+       +----------------+
| salience/lint|------>| candidate tracker |------>| curator status |
+--------------+       +-------------------+       +----------------+
                              |
                              v
                       backlog artifact
```

Salience and lint produce signals. Candidate tracker updates a harness-owned
backlog artifact. Curator status renders it for action.

## Key Interactions

Update during maintenance:

```
maintenance -> salience/lint: current signals
tracker -> backlog: add or update candidates
status -> report: top candidates
```

Reject candidate:

```
User/CLI -> tracker: reject candidate with reason
tracker  -> backlog: status rejected
```

Promoted page detected:

```
tracker -> wiki pages: slug now exists
tracker -> backlog: status promoted or merged
```

## Data Model

- Artifact path: `wiki/wiki-candidates.json` or another harness-owned name.
- Candidate key: canonical slug.
- Candidate fields: display name, category guess, aliases, reasons, sources,
  mention count, status, dates, status reason.

## APIs / Interfaces

- Maintenance updates candidates by default or through an explicit flag chosen
  during implementation.
- Optional CLI command: `llmwiki candidates` for listing and status changes.
- Curator status includes candidate summary.

## Behavior & Domain Rules

- Existing pages beat candidates: if slug exists, candidate is not queued as
  missing.
- Multiple sources mentioning the same candidate increase priority.
- A candidate with only one weak signal remains discovered, not queued.

Examples:

- Salience repeatedly sees `iterable` and no page exists -> candidate priority
  rises.
- `iterable.md` is later created -> candidate becomes promoted.
- Candidate `NaN` aliases to existing `nan` -> candidate becomes merged.

## Acceptance Criteria

- Tests prove candidate canonicalization and alias deduplication.
- Tests prove maintenance updates candidate counts without creating pages.
- Tests prove existing pages are not reported as missing candidates.
- Tests prove curator status renders top candidates and statuses.
- Tests prove rejected candidates stay rejected across updates.

## Cross-Cutting Concerns

Observability: status changes should be visible in `wiki/log.md` when performed
by an explicit user command.

## Reference Implementations

- Current salience: `harness/src/llmwiki/domain/salience.py`.
- Current maintenance report: `harness/src/llmwiki/domain/maintenance.py`.
- Backup candidate tracker idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/tools/wiki_candidate_tracker.py`.

## Alternatives Considered

- Broken links as candidate memory - rejected because it pollutes graph health.
- Thin page creation for every candidate - rejected because it caused live wiki
  churn.

## Halt Conditions

- If candidate status changes require human-review workflow semantics, stop and
  design curator review statuses separately.

## Implementation Notes

- Implemented `wiki/wiki-candidates.json` as harness-owned JSON bookkeeping.
- Added deterministic candidate records with finite statuses:
  `discovered`, `queued`, `promoted`, `rejected`, and `merged`.
- `uv run llmwiki maintenance` refreshes candidates from broken-link signals,
  files `wiki-curator-status`, and logs the maintenance operation.
- `uv run llmwiki curator-status` reads the current backlog without writing it.
- `uv run llmwiki candidates` lists active candidates.
- `uv run llmwiki candidates reject <slug> --reason <reason>` records an
  explicit rejection and appends `wiki/log.md`.
- Existing pages supersede candidates by moving active records to `promoted`.
- Rejected records stay rejected across future maintenance refreshes.

## Verification Plan

- Unit tests for canonicalization, alias deduplication, promotion, rejection,
  and JSON round-trip.
- Maintenance tests proving refresh updates counts without creating pages.
- CLI tests proving candidate list/reject behavior is model-free and logged.
- Live `uv run llmwiki maintenance` and `uv run llmwiki candidates` over the
  current wiki, followed by inspection of `wiki/wiki-candidates.json` and
  `wiki-curator-status`.

## Verification Results

- Focused domain, salience, maintenance, and CLI tests pass.
- Live `uv run llmwiki maintenance` refreshed `wiki/wiki-candidates.json`,
  filed `wiki-curator-status`, and appended `wiki/log.md` without starting a
  model.
- Live `uv run llmwiki candidates` lists the current backlog. The present wiki
  has no explicit missing-link candidates, so the backlog is empty.
- Live maintenance exposed a report-feedback loop: harness-owned report pages
  could create graph findings or inflate salience by linking to pages. Fixed by
  making system pages graph-neutral for broken-link/inbound-link computation.
