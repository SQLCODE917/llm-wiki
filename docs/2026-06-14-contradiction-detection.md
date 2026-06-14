# Contradiction Detection

## Context & Problem

The pattern document says the wiki should notice when new knowledge contradicts
old claims. Current lint can measure links, index drift, orphans, citation
shape, and evidence policy findings, but it cannot detect semantic conflict
between pages. Without a bounded contradiction audit, the wiki can accumulate
incompatible claims while still looking structurally healthy.

## Goals

- Add a model-assisted contradiction audit that is report-only by default.
- Bound the audit with deterministic candidate selection before any model call.
- Record structured contradiction candidates instead of relying on prose.
- File an auditable `wiki-contradictions` report and append a log entry.
- Make contradictions visible to future lint/maintenance runs without
  auto-resolving them.

## Non-Goals & Forbidden Approaches

Non-goals:

- No automatic contradiction resolution.
- No web search or freshness checking.
- No stable evidence-ID system.
- No full semantic overlap or duplicate-page merger.
- No requirement that every claim in every page be extracted into a database.

Forbidden approaches:

- Do not let the model silently choose which source is correct.
- Do not rewrite content pages from the contradiction command.
- Do not scan all page pairs without a deterministic cap.
- Do not treat "not found by the audit" as proof that no contradictions exist.
- Do not restore the backup repo's type-directory contradiction report format.

## Requirements

- Add `llmwiki contradictions` as a separate command.
- The command uses the configured runtime only after deterministic candidate
  pair selection is complete.
- The command selects bounded candidate page pairs from existing wiki pages
  using deterministic signals: shared sources, direct links, shared cited raw
  files, and keyword overlap.
- The command exposes a structured `record_contradiction` tool to the model.
- Each recorded contradiction includes two existing page names, two conflicting
  claim summaries, severity, rationale, and recommended curator action.
- The command writes `wiki-contradictions` and appends one `contradiction` log
  entry when findings are recorded.
- If no findings are recorded, the command prints and may file an audit report
  that says no contradiction candidates were found in the audited set.
- The report lists candidate-pair counts, audited-pair counts, skipped-pair
  counts, findings, and a caveat that the result is an audit, not proof.
- `llmwiki lint` is not required to run contradiction detection in this TDD.

## Invariants

- `raw/` remains immutable.
- Ordinary wiki content pages are not modified by this command.
- `wiki-contradictions` is harness-owned bookkeeping and is exempt from orphan
  findings.
- The model may identify conflict, but the human curator resolves it.
- Existing lint, ingest, query, and chat commands keep their current behavior.
- Candidate selection is deterministic and testable without a model backend.

## Proposed Architecture

Add a pure candidate selector and a dedicated contradiction workflow. The
selector bounds the semantic work; the workflow lets the model inspect selected
page pairs and record structured findings.

```
+------------+    page texts    +------------------+
| WikiStore  |----------------->| domain/          |
|            |                  | contradictions   |
+-----+------+                  +--------+---------+
      | selected pairs                   |
      v                                  v
+------------+                  +------------------+
| Session    |----------------->| Forge workflow   |
| command    |                  | record/findings  |
+-----+------+                  +--------+---------+
      | report + log                     |
      v                                  |
+------------+<-------------------------+
| WikiStore  |
+------------+
```

Components: `domain/contradictions` selects candidate pairs and renders the
report; `Session` orchestrates the audit; the Forge workflow records structured
findings; `WikiStore` files only harness-owned report/log output.

## Key Interactions

Candidate selection:

```
CLI          WikiStore        CandidateSelector
 | start        |                    |
 |------------->| page texts/index   |
 |              |------------------->|
 |<------------- bounded pair set ---|
```

Model-assisted audit:

```
Session      Forge workflow      Model        record_contradiction
 | pairs          |                |                 |
 |--------------->| prompt pairs   |                 |
 |                |--------------->| inspect         |
 |                |<---------------| tool call       |
 |                |------------------------------->  |
 |<--------------- structured findings -------------|
```

Report filing:

```
Session       WikiStore
 | report        |
 |-------------->| write wiki-contradictions
 |-------------->| append contradiction log
 |<--------------| command output
```

## Data Model

- **ContradictionCandidatePair** - two page names, deterministic reasons for
  pairing, and a compact text excerpt from each page.
- **ContradictionFinding** - page A, claim A, page B, claim B, severity,
  rationale, and recommended curator action.
- **ContradictionAuditReport** - candidate counts, audited counts, skipped
  counts, findings, caveats, and rendered markdown.

Candidate access pattern: read all page texts once, compute pair reasons, sort
by strongest reasons, and audit up to a command cap.

## APIs / Interfaces

- CLI command: `llmwiki contradictions`.
- CLI option: `--max-pairs N`, default chosen in code and documented in help.
- Report page name: `wiki-contradictions`.
- Log operation type: `contradiction`.
- Model tool: `record_contradiction`.

The `record_contradiction` tool contract has these required fields:

| Field | Values |
| --- | --- |
| `page_a` | existing wiki page name |
| `claim_a` | concise claim summary from page A |
| `page_b` | existing wiki page name |
| `claim_b` | concise claim summary from page B |
| `severity` | `low`, `medium`, or `high` |
| `rationale` | why the claims cannot both be true as written |
| `recommended_action` | curator-facing next action |

## Behavior & Domain Rules

- The audit only records contradictions where two claims cannot both be true as
  written.
- Differences in scope, emphasis, terminology, or abstraction level are not
  contradictions unless the pages make incompatible factual claims.
- If the model is unsure, it must not call `record_contradiction`; uncertainty
  belongs in the final audit report caveat.
- The command never edits the conflicting pages.
- Findings with missing page names are rejected by the tool.
- Duplicate findings for the same page pair and same claim summaries are
  collapsed in the final report.

Examples:

- Page A says a feature was introduced in ES2015; page B says the same feature
  was introduced in ES2019 -> record a medium contradiction.
- Page A says JavaScript arrays are objects; page B says arrays are indexed
  collections -> do not record; both can be true.
- Page A has no source citation and page B has a cited disagreement -> record
  only if the claims are incompatible; the recommended action should ask the
  curator to inspect sources, not declare a winner.
- Candidate selector finds 200 possible pairs and `--max-pairs 25` -> audit 25,
  report 175 skipped by cap.

## Acceptance Criteria

- `llmwiki contradictions` selects candidate pairs deterministically before the
  model call.
- Tests cover candidate selection by shared sources, direct links, shared raw
  citations, and keyword overlap.
- Tests prove the max-pairs cap is enforced and skipped counts are reported.
- Tests prove `record_contradiction` rejects non-existent page names.
- Tests prove duplicate structured findings are collapsed.
- Tests prove the command does not modify ordinary wiki pages.
- Tests prove findings write `wiki-contradictions` and append a
  `contradiction` log entry.
- Tests prove a no-findings audit reports its scope and caveat.
- Existing `uv run pytest harness/tests` passes.
- `uv run ruff check harness/src harness/tests` passes.
- `uv run mypy harness/src` passes.

## Cross-Cutting Concerns

Observability: the transcript must contain the candidate-pair prompt, and the
filed report must include candidate/audited/skipped counts.

Error handling: if the model fails to call either `record_contradiction` or the
terminal tool, forge retry nudges should request exactly one tool call; if the
run still fails, no report should claim an audit completed.

User workflow: contradictions are curator decisions. The report should make
review easy without turning the model into an authority on which source wins.

## Reference Implementations

- Workflow orchestration: `harness/src/llmwiki/runtime/session.py`
- Tool definitions: `harness/src/llmwiki/workflows/tools.py`
- Link/citation deterministic scans: `harness/src/llmwiki/domain/links.py`
  and `harness/src/llmwiki/domain/citations.py`
- Report filing pattern: `harness/src/llmwiki/runtime/session.py`
- Pattern north star: `docs/REFERENCE_llm-wiki-pattern.md`

## Alternatives Considered

- Fold contradiction detection into every lint run - rejected because semantic
  audits are slower, model-dependent, and should be explicit.
- Full claim extraction database - rejected as too close to the old heavy
  evidence pipeline.
- Let the model scan the whole wiki freely - rejected because small models need
  bounded, deterministic context.
- Auto-resolve high-confidence contradictions - rejected because source
  precedence is a curator decision.

## Halt Conditions

- If implementation needs a persistent claim database, stop and write a smaller
  evidence-workflow TDD first.
- If candidate selection cannot keep prompts under the configured context
  window, stop and split batching into a separate TDD.
- If a contradiction fix requires editing content pages, stop and ask the
  curator which source or wording should win.
