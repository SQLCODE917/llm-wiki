# Runtime Profiles for Local 4090

## Context & Problem

The M5 harness currently assumes Qwen3-14B Q4_K_M served by `llama-server`.
This checkout already has Ollama available, and `forge-guardrails` ships a
native `OllamaClient` plus `backend="ollama"` setup support. The backup repo
preserved a `local-4090` Codex profile, but direct `codex exec` would let the
model edit files outside the M5 `write_page` boundary. The first shippable step
is to standardize on Ollama as the single active local LLM provider while
keeping the provider boundary narrow enough to swap later.

Verification on 2026-06-14: `ollama list` reached the local daemon and showed
`gpt-oss:20b` and `qwen3-coder:30b`; `forge.clients.ollama.OllamaClient` returned
`TextResponse("OK")` from `gpt-oss:20b`; the same client returned a structured
`ToolCall(tool="add", args={"a": 2, "b": 3})`.

Implementation smoke on 2026-06-14: `uv run llmwiki --runtime local-4090 query
"What is this wiki about? Answer in one sentence from the wiki index. Do not
save a new page."` completed through `local-4090 provider=ollama
model=qwen3-coder:30b ctx=16384`, returned a cited answer, appended the normal
query log entry, and wrote a transcript under `harness/runs/`.

## Goals

- Make Ollama the only implemented local LLM provider.
- Add explicit runtime selection for `llmwiki ingest/query/chat/lint`.
- Preserve `local-4090` as a named runtime target.
- Keep model/hardware profiles easy to swap without adding a second active
  provider.
- Record runtime identity in operation observability.
- Cover profile resolution and backend config with tests that use no live model.

## Non-Goals & Forbidden Approaches

Non-goals:

- No strict evidence checks in this TDD.
- No changes to wiki page schema, `SCHEMA.md`, or PDF chunking behavior.
- No support for every possible 4090 server.
- No direct migration of old `wiki_llm` backend packages.
- No vLLM, llama-server, or Codex provider implementation in this slice.

Forbidden approaches:

- Do not run `codex exec` as the wiki operation runner.
- Do not keep parallel active local providers in the harness.
- Do not let runtime profiles contain arbitrary shell fragments.
- Do not bypass `WorkflowRunner`, `Session`, or `WikiStore`.
- Do not require a live GPU/server for unit tests.

## Requirements

- `--runtime <name>` selects a runtime profile.
- `LLMWIKI_RUNTIME=<name>` selects a runtime profile when no CLI runtime is set.
- CLI runtime selection overrides `LLMWIKI_RUNTIME`.
- Missing or invalid runtime names fail before backend startup.
- The default profile is an Ollama profile.
- `local-4090` resolves to a forge `backend="ollama"` configuration.
- Runtime name, backend kind, model identity, and context tokens are visible in
  transcript metadata or command output.

## Invariants

- Existing command names and positional arguments remain valid.
- The default runtime uses Ollama when no runtime is specified.
- A runtime failure appends no success log entry.
- Runtime selection happens once per command before `Session` construction.
- The model still interacts with the wiki only through workflow tools.

## Proposed Architecture

Add a runtime profile resolver between CLI argument parsing and backend startup.
The resolver maps a profile name to structured Ollama settings, then
`start_backend` creates the forge `OllamaClient` and context manager from those
settings.

```
+---------+       +------------------+       +---------------+
| CLI     |------>| Runtime resolver |------>| start_backend |
+----+----+       +------------------+       +-------+-------+
     |                                             |
     v                                             v
+------------+                              +--------------+
| Session    |<-----------------------------| ActiveBackend |
+------------+                              +--------------+
```

Components: CLI gathers runtime inputs; runtime resolver validates profile
names and precedence; backend startup owns the forge Ollama client/server
handoff; Session remains unchanged except for receiving runtime metadata.

## Key Interactions

Runtime precedence:

```
User      CLI        Resolver       Backend
 | command |            |             |
 |-------->| read args  |             |
 |         | runtime?   |             |
 |         |----------->| choose cfg   |
 |         |<-----------|             |
 |         |------------------------->|
 |<-------- operation result ----------|
```

Startup failure:

```
CLI        Resolver       Backend       Session
 |---------->|              |             |
 |<--cfg-----|              |             |
 |---------- start -------->|             |
 |<--------- error ---------|             |
 | exit 2, no Session/log                 |
```

## Data Model

- **RuntimeName** — profile identifier. Initial allowed values:
  `ollama-default`, `local-4090`.
- **RuntimeProfile** — structured runtime settings: name, provider (`ollama`),
  model tag, context tokens, endpoint, and lifecycle mode.
- **BackendConfig** — existing backend startup configuration extended to carry
  runtime name and backend kind.
- **RuntimeSummary** — short observability record derived from the selected
  profile.

Profile access pattern: runtime profiles are loaded once per process invocation.
They are not mutable wiki state and are not written to `wiki/`.

## APIs / Interfaces

- `llmwiki --runtime <name> <op> ...`
- `LLMWIKI_RUNTIME=<name>`
- Runtime profile names are public API:
  - `ollama-default`
  - `local-4090`

Both profiles must use `forge.clients.ollama.OllamaClient` and
`setup_backend(backend="ollama", model=<tag>, client=<client>)`. A future
provider can be added behind the same profile boundary only with a new TDD.

## Behavior & Domain Rules

- CLI runtime beats environment runtime.
- Environment runtime beats default runtime.
- Unknown runtime names fail with the list of valid names.
- Runtime metadata is included in each operation's transcript path, transcript
  header, or command output.

Examples:

- No runtime input -> `ollama-default`.
- `LLMWIKI_RUNTIME=local-4090` -> `local-4090`.
- `LLMWIKI_RUNTIME=local-4090` plus `--runtime ollama-default` ->
  `ollama-default`.
- `--runtime nope` -> command exits before backend startup.

## Acceptance Criteria

- Parser help shows `--runtime`.
- Tests cover default, environment, CLI override, and invalid runtime behavior.
- Tests prove `local-4090` produces Ollama backend settings without requiring a
  GPU.
- Tests prove no llama-server GGUF path is required for Ollama profiles.
- Existing `uv run pytest harness/tests` passes.
- `uv run ruff check harness/src harness/tests` passes.
- `uv run mypy harness/src` passes.
- A manual 4090 smoke note is added to docs after one real operation succeeds.
  Completed 2026-06-14.

## Cross-Cutting Concerns

Observability: runtime identity must be visible enough that a transcript can be
matched to the hardware/profile used.

Security: profile settings are structured values. No user-provided shell command
is executed from a runtime profile.

Portability: Linux/4090 additions must not import Linux-only packages at module
import time in a way that breaks macOS/M5.

## Reference Implementations

- Current backend startup to replace/adapt: `harness/src/llmwiki/runtime/backend.py`
- Current env config: `harness/src/llmwiki/config.py`
- Current CLI boundary: `harness/src/llmwiki/cli.py`
- Forge Ollama client: `.venv/lib/python3.12/site-packages/forge/clients/ollama.py`
- Forge Ollama setup: `.venv/lib/python3.12/site-packages/forge/server.py`
- Backup naming reference:
  `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/tools/wiki_model_defaults.json`

## Alternatives Considered

- Keep only `LLMWIKI_GGUF` — rejected because it cannot distinguish M5 and 4090
  runtime behavior.
- Keep llama-server as a parallel provider — rejected because the harness should
  have one active local provider first.
- Restore backup `CodexBackend` — rejected because direct Codex execution
  bypasses harness tools.
- Vendor runtime profiles into `SCHEMA.md` — rejected because model behavior and
  machine setup are separate contracts.
- Require a running server for tests — rejected because tests must be offline.

## Halt Conditions

- If Ollama cannot support required tool-calling for the target model, stop and
  choose a different Ollama model before considering another provider.
- If `local-4090` cannot be made forge-compatible through Ollama, stop and
  decide whether to patch forge, add an adapter, or accept a separate TDD for a
  second provider.
- If implementation needs arbitrary shell commands in profile config, stop and
  redesign the config boundary.
- If runtime metadata would require changing wiki page schema, stop and keep it
  in transcripts/log output instead.
