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
- Do not write partial index/log updates for a page write that fails evidence
  enforcement.
- Do not duplicate citation parsing logic inside workflow tools.

## Requirements

- Strict mode values are exactly `off`, `warn`, and `fail`.
- `off` skips evidence validation.
- `warn` records findings but permits the operation.
- `fail` rejects page writes with fatal findings.
- Lint includes evidence findings alongside link/index/orphan findings.
- Evidence gates use the parser contract from
  `docs/2026-06-14-strict-citation-parser.md`.
- Tool errors are actionable enough for forge to let the model self-correct.

## Invariants

- `write_page` remains the only wiki write boundary.
- Index updates remain consistent with page writes.
- Failed page writes do not append success messages.
- Lint may write `wiki-health`, but evidence findings are deterministic inputs
  to that workflow.
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
Session      Link lint      Evidence policy      Lint workflow
 | compute      |                |                    |
 |------------->|                |                    |
 | compute evidence findings     |                    |
 |------------------------------>|                    |
 | hand combined findings to model                    |
 |--------------------------------------------------->|
```

## Data Model

- **StrictEvidenceMode** — `off`, `warn`, or `fail`.
- **EvidencePolicyResult** — findings plus decision: allow, allow-with-warning,
  or reject.
- **CombinedLintFindings** — existing link/index/orphan findings plus citation
  findings.

Access pattern: writes validate one page; lint validates all pages.

## APIs / Interfaces

- CLI option: `--strict-evidence off|warn|fail`.
- Environment fallback: `LLMWIKI_STRICT_EVIDENCE=off|warn|fail`.
- Tool behavior: `write_page` returns warning text in `warn`; raises a tool
  error in `fail`.

CLI option precedence matches runtime precedence: CLI beats environment, which
beats default.

## Behavior & Domain Rules

- In `off`, validation is skipped.
- In `warn`, validation findings are visible but non-blocking.
- In `fail`, findings with severity `fail` reject the write.
- Lint never hides evidence findings from the model review message.
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

## Acceptance Criteria

- CLI help documents `--strict-evidence`.
- Tests cover CLI/env/default strictness precedence.
- Tests cover `write_page` in `off`, `warn`, and `fail`.
- Tests prove failed writes do not update page files or index entries.
- Tests prove lint includes evidence findings in the model prompt.
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
