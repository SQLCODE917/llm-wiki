# Evidence Gates for Writes and Lint

## Context & Problem

After citation parsing exists, the harness still needs a policy for using those
findings. The old repo had strict validation gates, but applying them globally
would make the lighter M5 wiki cumbersome. This TDD adds opt-in evidence gates
to `write_page` and `lint` while keeping normal synthesis permissive by default.

## Goals

- Add `off|warn|fail` strict-evidence behavior to write and lint paths.
- Default strictness to `off`.
- Surface deterministic citation findings in lint reports.
- Let `fail` mode block invalid new page writes through tool errors.
- Verify lint outcomes after the model pass with recomputed deterministic
  findings.
- Add a deterministic helper for orphan-link repairs so graph-only fixes do
  not require whole-page rewrites.
- Keep all enforcement inside the harness, not prompt instructions.

## Non-Goals & Forbidden Approaches

Non-goals:

- No new citation syntax.
- No LLM support judging.
- No mandatory evidence IDs.
- No changes to raw/PDF extraction.

Forbidden approaches:

- Do not make strict evidence the default.
- Do not let the model decide whether a deterministic finding is fatal.
- Do not let lint success be only model-reported when the harness can measure
  the underlying graph, index, or citation state.
- Do not require `write_page` for the common orphan-only repair of adding one
  inbound `[[link]]`.
- Do not write partial index/log updates for a page write that fails evidence
  enforcement.
- Do not duplicate citation parsing logic inside workflow tools.

## Requirements

- Strict mode values are exactly `off`, `warn`, and `fail`.
- `off` skips evidence validation.
- `warn` records findings but permits the operation.
- `fail` rejects page writes with fatal findings.
- Lint includes evidence findings alongside link/index/orphan findings.
- Lint recomputes deterministic findings after the model calls `finish_lint`.
- The final lint output, `wiki-health`, and `log.md` include both the model
  report and the before/after deterministic verification.
- The verified report includes a deterministic delta section listing resolved,
  new, and remaining orphan pages plus count deltas for broken links, index
  drift, and citation evidence findings.
- Lint exposes an orphan-link helper that verifies both pages exist, verifies
  the target is currently listed as an orphan, and inserts exactly one inbound
  wiki link from a related page to that orphan page.
- Evidence gates use the parser contract from
  `docs/2026-06-14-strict-citation-parser.md`.
- Tool errors are actionable enough for forge to let the model self-correct.

## Invariants

- `write_page` remains the only wiki write boundary.
- Index updates remain consistent with page writes.
- Failed page writes do not append success messages.
- Lint may write `wiki-health`, but evidence findings are deterministic inputs
  to that workflow.
- `wiki-health` records verified lint state. If the model claims a fix that the
  post-pass does not confirm, the residual deterministic finding remains
  visible in the final report.
- Existing commands work unchanged when strict mode is omitted.

## Proposed Architecture

Add a strictness policy object to the write and lint orchestration paths. The
policy calls the citation validator only when strictness is not `off`.

```
+------------+       +----------------+       +----------------+
| write_page |------>| Evidence       |------>| WikiStore      |
| tool       |       | policy         |       | write/index    |
+------------+       +-------+--------+       +----------------+
                             |
                             v
                      +--------------+
                      | Citation     |
                      | validator    |
                      +--------------+
```

Components: workflow tools invoke policy; policy maps findings to warn/fail
behavior; citation validator stays pure; WikiStore writes only accepted pages.

## Key Interactions

Write in `warn`:

```
Model       write_page       Policy        WikiStore
 | page        |               |              |
 |------------>| validate      |              |
 |             |-------------->| findings     |
 |             |<--------------|              |
 |             | write anyway                 |
 |             |----------------------------->|
 |<------------ success + warning summary ----|
```

Orphan repair:

```
Model       link_orphan       WikiStore       Post-pass lint
 | choose edge |                |                 |
 |------------>| read pages     |                 |
 |             | append link    |                 |
 |             |--------------->|                 |
 |<------------ success --------|                 |
 | finish_lint                                   |
 |---------------------------------------------->|
 |<--------------- recomputed orphan state ------|
```

Write in `fail`:

```
Model       write_page       Policy        WikiStore
 | page        |               |              |
 |------------>| validate      |              |
 |             |-------------->| fatal        |
 |             |<--------------|              |
 |<------------ tool error, no write ---------|
```

Lint:

```
Session      Deterministic lint      Lint workflow      Deterministic lint
 | before            |                    | after               |
 |------------------>|                    |                     |
 | hand findings to model                 |                     |
 |--------------------------------------->|                     |
 |<------------------ model report -------|                     |
 | recompute graph/index/evidence state                         |
 |------------------------------------------------------------->|
 | final report = model report + before/after verification      |
```

## Data Model

- **StrictEvidenceMode** — `off`, `warn`, or `fail`.
- **EvidencePolicyResult** — findings plus decision: allow, allow-with-warning,
  or reject.
- **LintSnapshot** — existing link/index/orphan findings plus citation evidence
  findings for one point in the lint operation.
- **VerifiedLintReport** — model report plus deterministic delta and
  before/after lint snapshots.
- **OrphanLinkRepair** — chosen source page and currently orphaned target page
  for one deterministic inbound-link insertion.

Access pattern: writes validate one page; lint validates all pages.

## APIs / Interfaces

- CLI option: `--strict-evidence off|warn|fail`.
- Environment fallback: `LLMWIKI_STRICT_EVIDENCE=off|warn|fail`.
- Tool behavior: `write_page` returns warning text in `warn`; raises a tool
  error in `fail`.
- Lint-only tool: `link_orphan(from_page, orphan_page)`.

CLI option precedence matches runtime precedence: CLI beats environment, which
beats default.

## Behavior & Domain Rules

- In `off`, validation is skipped.
- In `warn`, validation findings are visible but non-blocking.
- In `fail`, findings with severity `fail` reject the write.
- Lint never hides evidence findings from the model review message.
- Lint never records the model's success claim alone. The harness records the
  model report plus recomputed before/after deterministic state.
- Orphan-only repair should use `link_orphan` when the fix is a single inbound
  edge. The model chooses the related source page; the harness performs the
  mechanical edit and rejects targets that are not current deterministic
  orphans.
- `wiki-health` itself is exempt from evidence enforcement unless explicitly
  selected later.

Examples:

- `--strict-evidence off`, page cites missing source -> page write can succeed.
- `--strict-evidence warn`, page cites missing source -> page write succeeds
  and warning is returned.
- `--strict-evidence fail`, page cites missing source -> tool error and no
  page/index update.
- `llmwiki lint --strict-evidence warn` -> health report sees evidence findings
  but command can complete.
- Model says "all orphans fixed" but the graph still has orphans after the
  pass -> final report includes the model claim and the residual orphan list.
- `link_orphan(from_page="chapter", orphan_page="closure")` -> `chapter` gains
  `[[closure]]`; the post-pass verifies whether `closure` is still orphaned.

## Acceptance Criteria

- CLI help documents `--strict-evidence`.
- Tests cover CLI/env/default strictness precedence.
- Tests cover `write_page` in `off`, `warn`, and `fail`.
- Tests prove failed writes do not update page files or index entries.
- Tests prove lint includes evidence findings in the model prompt.
- Tests prove lint output and `wiki-health` include deterministic before/after
  verification.
- Tests prove the deterministic delta names resolved and remaining orphan
  pages.
- Tests prove a false model success claim remains contradicted by the
  recomputed residual findings.
- Tests prove `link_orphan` can remove an orphan from the post-pass findings.
- Existing `uv run pytest harness/tests` passes.
- `uv run ruff check harness/src harness/tests` passes.
- `uv run mypy harness/src` passes.

## Cross-Cutting Concerns

Observability: strict mode and warning/fail counts must appear in command output
or transcript messages.

Error handling: `fail` mode errors must name the page, finding code, and
correction path.

User workflow: because strictness defaults to `off`, ordinary exploratory
ingest remains lightweight.

## Reference Implementations

- Tool boundary: `harness/src/llmwiki/workflows/tools.py`
- Lint orchestration: `harness/src/llmwiki/runtime/session.py`
- Link findings shape: `harness/src/llmwiki/domain/links.py`
- Citation parser TDD: `docs/2026-06-14-strict-citation-parser.md`

## Alternatives Considered

- Always fail on evidence findings — rejected because many wiki pages are useful
  syntheses with coarse citations.
- Put strictness in prompts — rejected because enforcement is deterministic
  harness policy.
- Run evidence checks only in lint — rejected because `fail` mode is useful for
  high-stakes ingests.

## Halt Conditions

- If warning text causes small models to loop or over-rewrite pages, stop and
  move warnings to transcript/operation output instead of tool success text.
- If `fail` mode blocks common valid citations, stop and revise parser findings
  before expanding enforcement.
- If policy integration would make `WikiStore` own model-facing behavior, stop
  and keep policy in workflow/tool orchestration.
