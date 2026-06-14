# Project: Local LLM setup (llama.cpp on macOS)

## Goal
Build an "LLM-Wiki" on this machine: a persistent, LLM-maintained knowledge
base following the pattern in docs/llm-wiki.md (see Reference material below).
Inference engine: Qwen3-14B Q4_K_M served locally via `llama-server`, with
forge providing tool-calling reliability for the 14B model.

## Hardware & OS
- Mac with Apple M5 chip, 24 GB unified memory
- macOS caps Metal GPU allocation at roughly 70–75% of RAM (~17–18 GB usable
  for model + KV cache). Budget model sizes accordingly: ~9 GB Q4_K_M weights
  leave room for 32K+ context; quants near 16 GB leave very little.
- Default shell is bash (`~/.bash_profile` for PATH changes)

## Hard constraint: NO ROOT / ADMIN ACCESS
- Never suggest `sudo`, system-wide Homebrew, `/usr/local`, or anything
  requiring admin privileges.
- Everything installs to user space: `~/.local/bin`, `pip3 install --user`,
  apps in `~/Applications`, npm prefix in `$HOME` if needed.
- Xcode Command Line Tools are already installed and working.

## Project layout
This file lives at the project root (`llm-wiki/`). Subdirectories:
- `llama.cpp/` — inference engine, built from source (see Current state)
- `forge/` — clone of the forge tool-calling reliability framework
- `docs/` — project documents, including the alignment document
  `docs/llm-wiki.md` (do not confuse with llama.cpp's own upstream
  `llama.cpp/docs/` directory)

## Current state
- llama.cpp built from source at `llama.cpp/` with:
  `cmake -B build -DLLAMA_BUILD_BORINGSSL=ON && cmake --build build --config Release -j`
  (BoringSSL enables HTTPS so the `-hf` Hugging Face auto-download flag works)
- Binaries in `llama.cpp/build/bin/` (`llama-cli`, `llama-server`, etc.)
- Models directory: `~/models` (downloaded GGUFs may also land in
  `~/Library/Caches/llama.cpp` via `-hf`)
- Reference run command:
  `./build/bin/llama-server -hf Qwen/Qwen3-14B-GGUF:Q4_K_M --jinja -c 16384`
- Qwen3 supports thinking/non-thinking modes; `/no_think` in the prompt
  disables reasoning preamble (preferred for factual lookups).

## Reference material (consult these — they are load-bearing)

### docs/llm-wiki.md — the alignment document (Karpathy's LLM Wiki pattern)
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
Cloned locally from https://github.com/antoinezambelli/forge (MIT).
A Python framework for reliable tool-calling and multi-step agentic
workflows on self-hosted models; supports llama-server as a backend.
- **Prefer using forge directly as a dependency** (WorkflowRunner, the
  guardrails middleware, or its OpenAI-compatible proxy in front of
  llama-server) rather than re-implementing its ideas — re-implementation
  of a maintained library counts as a workaround.
- Where direct use doesn't fit, mirror its techniques when designing the
  14B model's tool-calling: rescue parsing of malformed tool calls, retry
  nudges, required-step enforcement, the synthetic `respond` tool to keep
  the model in tool-calling mode, and token-budgeted tiered context
  compaction.
- Read its docs before designing: docs/ARCHITECTURE.md, docs/USER_GUIDE.md,
  docs/WORKFLOW.md, and docs/decisions/ (ADRs) in the forge clone.
- Note: forge requires Python 3.12+. macOS's bundled Python is older —
  use `uv` (installs and manages Python toolchains entirely in user space,
  no root) to provision 3.12+ and a venv for it.

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

