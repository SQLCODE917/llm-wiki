# Maintenance Automation and Curator Status

## Context & Problem

The harness already has `llmwiki lint`, deterministic post-pass verification,
evidence gates, salience, `index.md`, and `log.md`. What is missing is a cheap
curator-facing status command that summarizes wiki health without starting a
model repair workflow. As the wiki grows, the human needs a routine dashboard
for what is stale, risky, or worth doing next.

## Goals

- Add a read-only curator status command that runs without an LLM backend.
- Add a maintenance command that files the same deterministic status as a
  harness-owned report and appends a log entry.
- Summarize link/index/orphan, citation evidence, salience, page-count, source,
  and recent-log state in one report.
- Keep model repair opt-in through the existing `llmwiki lint` command.
- Make scheduled or frequent health checks cheap enough to run after every
  substantial wiki operation.

## Non-Goals & Forbidden Approaches

Non-goals:

- No semantic contradiction detection.
- No scheduled system service or cron installer.
- No automatic page repair.
- No new evidence syntax.
- No replacement for `llmwiki lint`.

Forbidden approaches:

- Do not start Ollama or any other LLM backend for read-only curator status.
- Do not modify ordinary wiki content pages from this workflow.
- Do not let this command claim the wiki is correct; it reports measured
  maintenance state only.
- Do not duplicate link or evidence validation logic outside the existing
  domain modules.
- Do not restore backup repo reports such as `_maintenance-report.md` as a
  separate directory/schema convention.

## Requirements

- `llmwiki curator-status` prints a deterministic report and writes nothing.
- `llmwiki maintenance` writes the deterministic report to `wiki-curator-status`
  and appends one `maintenance` entry to `log.md`.
- Both commands accept the same `--strict-evidence off|warn|fail` option as
  existing wiki operations.
- Both commands complete without loading a runtime profile or contacting a
  model provider.
- The report includes page counts by category, raw source counts, latest log
  entries, link/index/orphan findings, citation evidence findings, and the
  current salience report.
- The report includes a "Recommended next actions" section derived only from
  deterministic findings.
- Empty wikis, missing `index.md`, missing `log.md`, and empty `raw/` are
  valid inputs with explicit report lines.
- The command output must be stable enough for tests to assert section names
  and finding counts.

## Invariants

- `raw/` remains immutable.
- The flat `wiki/*.md` page model remains canonical.
- `index.md`, `log.md`, `wiki-health`, and `wiki-curator-status` are
  harness-owned bookkeeping.
- Existing `llmwiki ingest`, `llmwiki query`, `llmwiki chat`, and
  `llmwiki lint` behavior is unchanged.
- `llmwiki lint` remains the only command in this design that asks the model
  to repair wiki content.
- `wiki-curator-status` is exempt from orphan findings.

## Proposed Architecture

Add one pure domain report builder and two CLI entrypoints. The report builder
uses existing deterministic facts; the CLI decides whether to print only or
file the report.

```
+-------------+     page/source/log data     +------------------+
| WikiStore   |----------------------------->| domain/maintenance|
+------+------+                              | CuratorStatus     |
       |                                      +--------+---------+
       | rendered report                               |
       v                                               v
+-------------+                              +------------------+
| curator-    |                              | maintenance      |
| status CLI  |                              | CLI              |
+-------------+                              +------------------+
 print only                                  write report + log
```

Components: `WikiStore` provides current files; `domain/maintenance` computes a
pure `CuratorStatus`; `curator-status` prints it; `maintenance` files it as
harness bookkeeping.

## Key Interactions

Read-only status:

```
User        CLI             WikiStore       CuratorStatus
 | status    |                 |                 |
 |---------->| read facts       |                 |
 |           |---------------->|                 |
 |           | build report                      |
 |           |---------------------------------->|
 |<---------- printed deterministic report ------|
```

Filed maintenance:

```
User        CLI             CuratorStatus     WikiStore
 | maintain  |                  |                |
 |---------->| build report     |                |
 |           |----------------->|                |
 |           | write report + append log         |
 |           |---------------------------------->|
 |<---------- printed deterministic report ------|
```

Strict evidence status:

```
CLI          EvidencePolicy       SourceInventory
 | mode warn      |                      |
 |--------------->| inspect pages        |
 |                |--------------------->|
 |<--------------- evidence summary -----|
```

## Data Model

- **CuratorStatus** - deterministic wiki maintenance report with rendered
  sections and aggregate counts.
- **WikiShapeSummary** - page count by category, total page count, source count,
  raw source count, and whether `index.md`/`log.md` exist.
- **RecommendedAction** - deterministic action label, reason, and suggested
  command.

Access patterns: read all current wiki page texts, read index names, inspect
raw inventory when evidence strictness is enabled, and read the latest log
headings if `log.md` exists.

## APIs / Interfaces

- CLI command: `llmwiki curator-status`.
- CLI command: `llmwiki maintenance`.
- Shared CLI option: `--strict-evidence off|warn|fail`.
- Report page name: `wiki-curator-status`.
- Log operation type: `maintenance`.

## Behavior & Domain Rules

- Curator status never contacts a model provider.
- Maintenance writes only `wiki-curator-status` and `log.md`.
- Recommended actions are derived by priority: fatal evidence findings first,
  broken links second, index drift third, orphan pages fourth, then salience
  opportunities and recent-log context.
- Evidence mode `off` reports that citation validation was skipped.
- Evidence mode `fail` does not make curator status exit non-zero; it reports
  fatal evidence findings as maintenance work.
- `wiki-health` and `wiki-curator-status` are excluded from orphan findings.

Examples:

- Input: empty wiki -> output states zero pages, no lint findings, and suggests
  ingesting a source.
- Input: page exists but is missing from `index.md` -> output includes one
  index-drift action and suggests running `llmwiki lint`.
- Input: `--strict-evidence warn` and a page cites a missing raw file -> output
  includes the citation finding and recommends fixing citations before relying
  on the affected page.
- Input: healthy links but many high-salience pages have low inbound links ->
  output recommends a future lint pass for cross-link review, not an automatic
  rewrite.

## Acceptance Criteria

- `llmwiki curator-status` prints a report without starting a backend.
- `llmwiki curator-status` leaves wiki files and `log.md` unchanged.
- `llmwiki maintenance` writes `wiki-curator-status` and appends one log entry.
- Tests cover empty wiki, healthy wiki, broken link, orphan, index drift, and
  citation warning cases.
- Tests prove `wiki-health` and `wiki-curator-status` are exempt from orphan
  findings.
- Tests prove strict-evidence CLI/env/default precedence matches existing
  operations.
- Tests prove no runtime profile is loaded for either command.
- Existing `uv run pytest harness/tests` passes.
- `uv run ruff check harness/src harness/tests` passes.
- `uv run mypy harness/src` passes.

## Cross-Cutting Concerns

Observability: the filed report and log entry must include the strict evidence
mode and deterministic finding counts.

Error handling: unreadable index or log files should appear as explicit report
warnings unless the store cannot read the wiki root at all.

User workflow: the command is safe to run often because it is deterministic,
read-only by default, and model-free.

## Reference Implementations

- Lint snapshots and deltas: `harness/src/llmwiki/runtime/session.py`
- Link findings: `harness/src/llmwiki/domain/links.py`
- Evidence policy: `harness/src/llmwiki/domain/evidence.py`
- Salience report: `harness/src/llmwiki/domain/salience.py`
- Store/report writes: `harness/src/llmwiki/store/wiki_store.py`

## Alternatives Considered

- Extend `llmwiki lint` only - rejected because lint starts a model repair
  workflow and is too heavy for routine status checks.
- Recreate the backup maintenance suite - rejected because the M5 harness only
  needs a flat deterministic status surface now.
- Add systemd automation immediately - rejected because command behavior should
  prove useful before scheduling is designed.
- Make status fail the process on findings - rejected because the curator needs
  an inspection report, not CI semantics.

## Halt Conditions

- If implementation would require restoring type-directory wiki reports, stop
  and write a separate migration proposal.
- If maintenance needs model judgment to produce a section, stop and split that
  section into a separate TDD.
- If report filing would touch ordinary content pages, stop and keep the command
  read-only except for `wiki-curator-status` and `log.md`.
