# Project: LLM-Wiki

## Goal
Maintain an "LLM-Wiki": a persistent, LLM-maintained knowledge base following
the pattern in `docs/llm-wiki.md` and `docs/REFERENCE_llm-wiki-pattern.md`.
The current foundation is the M5 harness: a small, Obsidian-friendly wiki
driven through `forge` tools, with deterministic code owning bookkeeping and
the model owning wiki prose.

The active local LLM provider is Ollama through `forge`'s native
`OllamaClient`. The default profile is `ollama-default`; the 4090 profile is
`local-4090`, defaulting to `qwen3-coder:30b`. Keep the provider boundary easy
to swap later, but do not maintain parallel active providers in the harness.

## Migration state
- This repo was replaced with the M5 foundation on 2026-06-14.
- The previous working tree is preserved at
  `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/`.
- Treat that folder as read-only reference material during migration. Do not
  edit it; copy ideas out intentionally.
- High-value material to port selectively from the backup:
  - `tools/wiki_model_defaults.json` for old `local-4090` naming and sampling
    context. Do not restore direct Codex execution as the wiki runner.
  - evidence and locator validation from `packages/wiki_core/` and
    `packages/wiki_io/` for optional strict/high-stakes ingest gates.
  - deterministic lint ideas that protect against broken links,
    contradictions, and stale navigation.
- Do not restore the old type-directory schema by default. The M5 foundation's
  flat `wiki/*.md` structure and `[[page-name]]` links are now the default.

## Runtime targets
- `ollama-default`: default Ollama runtime profile. Override model with
  `LLMWIKI_OLLAMA_MODEL`.
- `local-4090`: Ollama runtime profile for the local 4090. Defaults to
  `qwen3-coder:30b`; override with `LLMWIKI_4090_MODEL`.
- Runtime selection uses `--runtime <name>` or `LLMWIKI_RUNTIME`; CLI wins over
  environment. Do not bypass the harness with standalone prompt scripts for
  ingest/query/lint.
- Keep runtime-specific setup in docs and config. The wiki schema should stay
  about wiki behavior, not machine setup.

## Project layout
This file lives at the project root (`llm-wiki/`). Subdirectories:
- `harness/` — uv Python package containing the CLI, workflows, stores,
  domain logic, chat store, PDF extraction, and tests.
- `raw/` — immutable source documents. The harness reads this layer only.
- `wiki/` — model-authored markdown pages plus deterministic `index.md` and
  append-only `log.md`.
- `docs/` — design documents, including the alignment document
  `docs/llm-wiki.md` and compatibility copy
  `docs/REFERENCE_llm-wiki-pattern.md`.
- `SCHEMA.md` — the live wiki schema rendered into the model's system prompt.
- `backup/reference/` — migration-only reference material; do not ingest from
  or write into it.

## Reference material (consult these — they are load-bearing)

### docs/llm-wiki.md / docs/REFERENCE_llm-wiki-pattern.md
The alignment document (Karpathy's LLM Wiki pattern).
This is the design north star for the LLM-Wiki. Its core pattern: three layers
(immutable raw sources → an LLM-built-and-maintained wiki of interlinked
markdown pages → a schema document defining conventions and workflows), with
three operations (ingest, query, lint) plus index.md and log.md for navigation.
- **When planning** any LLM-Wiki feature or task: read docs/llm-wiki.md first
  and state explicitly how the plan serves its principles.
- **Before marking any task done**: assert that the result is aligned with
  docs/llm-wiki.md (e.g. raw sources stay immutable, the wiki layer is
  LLM-maintained, answers worth keeping get filed back into the wiki,
  index.md and log.md stay current). If a task can't be justified against
  the document, stop and raise it rather than completing it.

### forge — reliability layer for small-model tool calling
The harness depends on `forge-guardrails`, the reliability layer for
tool-calling and multi-step agentic workflows on self-hosted models.
- **Prefer using forge directly as a dependency** (WorkflowRunner,
  `OllamaClient`, guardrails middleware, or its proxy mode) rather than
  re-implementing its ideas — re-implementation of a maintained library counts
  as a workaround.
- Where direct use doesn't fit, mirror its techniques when designing the
  14B model's tool-calling: rescue parsing of malformed tool calls, retry
  nudges, required-step enforcement, the synthetic `respond` tool to keep
  the model in tool-calling mode, and token-budgeted tiered context
  compaction.
- Read its docs before designing: docs/ARCHITECTURE.md, docs/USER_GUIDE.md,
  docs/WORKFLOW.md, and docs/decisions/ (ADRs) from the forge project when
  available.
- Forge requires Python 3.12+. Use `uv` to provision and run the harness.

## Wiki operating rules
- `raw/` is immutable. Never edit, reorganize, rename, or delete sources as
  part of an ingest.
- `wiki/` is the compiled knowledge layer. Prefer updating existing pages over
  creating duplicates.
- Important claims need source citations. If a source does not cover a point,
  say so plainly.
- If two sources disagree, document the contradiction in the affected page and
  in `wiki/log.md`; do not silently pick one.
- `index.md` and `log.md` are harness-maintained navigation/history files.
  Do not hand-edit them unless you are repairing the harness itself.
- The model writes wiki content only through `write_page`; the harness owns
  frontmatter, index updates, log appends, link checks, salience reports, and
  chat windowing.
- Keep strict evidence IDs and locator validation as optional gates for sources
  where auditability matters. Do not force them onto every page by default.

## Open questions discipline

- Use `docs/open-questions.md` as the durable backlog for unresolved design,
  runtime, model-evaluation, ingest-quality, schema, and evidence-gating
  questions discovered during migration or implementation work.
- Add an open question when the uncertainty needs future evidence, an
  experiment, curator input, or post-implementation observation and cannot be
  responsibly resolved in the current task.
- Do not use open questions as a loose TODO list. Record only uncertainties
  that would materially affect future architecture, local-model behavior,
  source fidelity, wiki health, or operating rules.
- Keep immediate blockers in the relevant design document's halt conditions.
  Move only durable follow-up questions into `docs/open-questions.md`.
- Each open question should identify where it came from, what evidence or
  experiment would resolve it, and its current status.
- When a question is answered, move it to the resolved section with the
  decision and the evidence that justified it.

## Working preferences
- Prefer normative, pragmatic, idiomatic solutions over fast hacks.
  Do not accumulate workarounds; if the standard approach needs a rebuild
  or a proper install, do that instead.
- Prefer official/first-party model releases (e.g. Qwen org on Hugging Face)
  over third-party forks or modified variants.
- When downloading with curl, always use `-fL` so HTTP errors fail loudly
  instead of writing error pages to disk.
- Verify GGUF downloads before use: plausible file size and
  `head -c 4 file.gguf` printing `GGUF`.

## Design Documents

Place them in /docs, with a date and meaningful title
(`YYYY-MM-DD-<name>.md`). Before writing ANY design document or TDD, read
`docs/writing-tdds.md` in full and follow it exactly — it defines the
sizing gate, the required section structure, and the style constraints.

## Code Implementation

- Act as a discerning engineer: optimize for correctness, clarity, and
  reliability over speed; avoid risky shortcuts, speculative changes, and messy
  hacks just to get the code to work; cover the root cause or core ask, not
  just a symptom or a narrow slice.
- Practice Domain Driven Design for encapsulation.
- Functional, composable, reusable code that minimizes mocks.
- Functions either perform work or arrange work, never both.
- Keep file size down to under 300 lines.
- Monorepo structure to synchronize packages.
- Shared libraries for network contracts: library contains the type definitions and any validation logic, so that that the client uses to make a request, and the server uses to parse requests. No duplication of effort, effortless sync between services.
- Make application state explicit.
- Do not write universal functions that infer ambiguous application state from loosely shaped input.
- Keep business rules in pure functions or domain services.
- Keep side effects in orchestrators, adapters, route handlers, hooks, or services that exist specifically to coordinate them.
- Every boundary must have a clear input contract and output contract.
- Map explicitly between DTOs, domain models, persistence models, and view models.
- Use linting and static type checking to ensure code correctness


### Server

- Validate inbound and outbound transport shapes at boundaries.
- Keep route handlers thin.
- Keep business logic out of route definitions.
- Keep persistence concerns out of route handlers and UI-facing DTO mappers.
- Use feature folders for related server behavior.

### Testing

- Every unit of work should contain unit tests.
- Test coverage should be collected and measured before every commit.
- Pragmatically raise test coverage every time you touch code.
- Use Domain Driven Design to group tests by product feature.
- Prefer unit tests as end-to-end tests that map to the features in the design doc over targeted unit tests
- Do not run tests against live network services - all network traffic should be mocked out.
- Prefer data-in/data-out unit tests with minimal mocks.
- Treat repeated mocking as a coupling smell.
- Prefer fakes at true system boundaries.
- State machines, data pipelines and selectors should have direct unit coverage.

## Done means

- Formatting passes.
- Lint passes.
- Typecheck passes.
- Relevant tests pass.
- New behavior is covered by tests.
- The diff has been self-reviewed for duplication, dead code, accidental coupling, and naming drift.

## Plan tool

- Skip for straightforward tasks; no single-step plans.
- Update the plan after completing each sub-task.
- Plan closure: reconcile every intention as Done, Blocked, or Cancelled.
  Do not end with in_progress/pending items.
- Promise discipline: don't commit to tests/refactors unless you will do them
  now. Label optional work as "Next steps" outside the committed plan.
- Only update the plan tool; do not message the user mid-turn about plan status.

## Presenting your work

Plain text output; the CLI handles styling. Be concise; friendly coding
teammate tone. Mirror the user's style.

- Lead with the change and context (where/why), not "Summary:".
- Use inline code for paths/commands/identifiers. Reference files as
  standalone clickable paths (e.g. `src/app.ts:42`). No URIs, no line ranges.
- Flat bullets (`-`), short **bold** Title Case headers, no nesting.
- Don't dump large files; reference paths. Summarize command output.

## Shell and Tools

- Run all project commands from the repo root via uv — never call `.venv/bin/...` directly or modify PATH inline:
  - `uv run llmwiki ingest <file>` — ingest a source into the wiki
  - `uv run llmwiki query "<question>"`
  - `uv run llmwiki lint`
- **No `&&`**: Run shell commands as separate tool calls (parallel when
  independent, sequential when dependent).
- **Use `jq`, not Python, for JSON**: Use `jq` directly, or `--jq` flags on
  `gh` subcommands.
- **Modern CLI tools**: Use `rg` not `grep`, `fd` not `find`, `sd` not
  `sed` where possible.
- **Never `cd` out of the worktree**: Your cwd is the worktree root. Run
  all commands there. Never `cd` into the parent checkout or any other
  directory.
- **Use `git -C` instead of `cd`**: When running git commands in another
  directory, use `git -C $DIR <command>` instead of `cd $DIR` followed by
  `git <command>`. This avoids changing the working directory and keeps
  all operations rooted in the worktree.
