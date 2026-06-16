# Ingest Profiles

## Context & Problem

The current ingest prompts are intentionally generic and worked for a technical
book, but a tabletop RPG rulebook needs different wiki emphasis: rules
procedures, exceptions, tables, catalogs, and lookup-oriented page names. The
harness should support source-aware ingest strategy without hard-coding a
specific book, domain, or page prefix in Python.

Pattern excerpts addressed from `docs/llm-wiki.md`:

- "The schema ... tells the LLM how the wiki is structured"
- "It's up to you to develop the workflow that fits your style and document it
  in the schema for future sessions"
- "The exact directory structure ... will depend on your domain"

## Goals

- Add config-driven ingest profiles that can be added, removed, enabled, or
  disabled without editing workflow code.
- Let an ingest run select one or more profiles explicitly.
- Keep the default ingest behavior unchanged when no profile is selected.
- Provide a first `rulebook` profile suitable for tabletop RPG rulebooks.
- Derive source namespacing from the source file name, not hard-coded strings.

## Non-Goals & Forbidden Approaches

Non-goals:

- No separate wiki roots or multi-wiki router.
- No automatic profile classifier.
- No deterministic table parser or catalog database.
- No change to page categories, frontmatter shape, raw-source storage, or graph
  export schema.

Forbidden approaches:

- Do not hard-code `sword-world` or any other source-specific prefix in Python.
- Do not create a rulebook-only workflow fork.
- Do not make profiles executable code.
- Do not let profile config bypass `write_page`, evidence gates, index updates,
  log appends, or read-before-rewrite guardrails.
- Do not enable a profile implicitly from filename matching in this TDD.

## Requirements

- Profile definitions live as data files under `profiles/ingest/*.toml`.
- Each profile has a stable kebab-case `id`, `enabled` flag, description, and
  workflow-specific prompt overlays.
- `llmwiki ingest` accepts repeatable `--profile <id>` arguments.
- `llmwiki profiles` lists available ingest profiles and whether each is
  enabled.
- Selecting an unknown or disabled profile fails before any source extraction or
  model call.
- The harness renders these variables for prompt overlays:
  - `source_path`: source path relative to `raw/`.
  - `source_slug`: `slugify(Path(source_path).stem)`.
  - `source_namespace`: defaults to `source_slug`.
  - `profile_ids`: comma-separated selected profile ids.
- Profile overlays may reference only those variables. Unknown variables are a
  configuration error.
- For PDF sources, selected profile overlays apply to both map and integrate
  workflows.
- For non-PDF sources, selected profile overlays apply to the normal ingest
  workflow.

## Invariants

- `raw/` remains immutable.
- The model still writes wiki content only through `write_page`.
- `index.md`, `log.md`, key lists, candidate backlog, graph export, and evidence
  gates remain harness-owned.
- Page names remain global kebab-case slugs in the existing flat `wiki/*.md`
  structure.
- Existing commands without `--profile` preserve current behavior.

## Proposed Architecture

```
+-----------------+      +------------------+      +-------------------+
| profiles/ingest |----->| profile registry |----->| prompt assembler  |
+-----------------+      +------------------+      +-------------------+
                                  |                         |
                                  v                         v
                           ingest CLI/session        forge workflows
                                  |
                                  v
                              wiki store
```

`profiles/ingest` stores curator-editable TOML profiles. The profile registry
loads, validates, and selects enabled profiles. The prompt assembler combines
the existing generic ingest prompt with selected overlays and rendered source
variables. The ingest CLI/session passes selected profile ids into the existing
workflows.

## Key Interactions

Profile discovery:

```
User -> CLI: llmwiki profiles
CLI -> registry: load profiles/ingest
registry -> CLI: profiles with enabled status and descriptions
CLI -> User: table of available ingest profiles
```

Profiled PDF ingest:

```
User -> CLI: llmwiki ingest raw-book.pdf --profile rulebook
CLI -> registry: select enabled rulebook profile
Session -> PDF pipeline: extract/chunk source
Session -> prompt assembler: map prompt + rulebook overlay + source variables
Model -> tools: write chunk pages through existing write_page
Session -> prompt assembler: integrate prompt + rulebook overlay + source variables
Model -> tools: write hub/cross-links through existing write_page
```

Invalid profile:

```
User -> CLI: llmwiki ingest book.pdf --profile missing
CLI -> registry: select profile
registry -> CLI: configuration error
CLI -> User: fail before extraction or model call
```

## Data Model

`IngestProfile` is loaded from one TOML file:

- `id`: kebab-case identifier, matching the filename stem.
- `enabled`: boolean.
- `description`: one-line human-readable purpose.
- `priority`: integer; lower numbers compose earlier when multiple profiles are
  selected.
- `namespace.mode`: initially only `source-slug`.
- `namespace.require_for_new_pages`: optional boolean; when true, new pages
  must use the active source namespace.
- `naming.prevent_singular_plural_siblings`: optional boolean; when true, new
  pages under the active source namespace cannot be bare singular/plural
  siblings of existing pages.
- `overlays.ingest`: optional prompt overlay for normal source ingest.
- `overlays.pdf_map`: optional prompt overlay for PDF chunk map runs.
- `overlays.pdf_integrate`: optional prompt overlay for PDF integrate runs.

The first shipped profile is `rulebook`. Its overlays instruct the model to:

- Use `source_namespace` when naming ambiguous domain pages.
- Preserve procedures, exceptions, prerequisites, and table lookup meaning.
- Treat catalogs as overview/index pages unless the chunk deeply explains a
  specific entry.
- Avoid one page per spell, monster, item, or table row by default.
- Avoid singular/plural sibling pages; use descriptive role suffixes when the
  same noun names different rulebook roles.
- Prefer durable lookup pages over broad prose summaries when the source section
  is operational rules.

## APIs / Interfaces

- `llmwiki profiles`: lists ingest profile ids, enabled status, and descriptions.
- `llmwiki ingest <source> --profile <id>`: applies one enabled profile.
- `llmwiki ingest <source> --profile <id> --profile <id2>`: applies multiple
  profiles in ascending `priority`, then CLI order for ties.
- `profiles/ingest/*.toml`: the curator-facing profile extension point.

Profile TOML contract:

```toml
id = "rulebook"
enabled = true
description = "Operational rules, procedures, catalogs, and lookup tables."
priority = 100

[namespace]
mode = "source-slug"
require_for_new_pages = true

[naming]
prevent_singular_plural_siblings = true

[overlays]
ingest = "..."
pdf_map = "..."
pdf_integrate = "..."
```

## Behavior & Domain Rules

- Profiles are selected explicitly. A filename can suggest a profile to the
  curator, but it cannot activate one automatically in this TDD.
- Source namespace is derived from the source path. For
  `raw/Sword World RPG - Complete Edition.pdf`, `source_namespace` is
  `sword-world-rpg-complete-edition`.
- Profile overlays add guidance; they do not replace the base schema or generic
  workflow prompt.
- Multiple profiles compose deterministically by priority and CLI order.
- A disabled profile is visible in `llmwiki profiles` but cannot be selected.

Examples:

- `uv run llmwiki ingest "Sword World RPG - Complete Edition.pdf" --profile
  rulebook` -> the model receives rulebook guidance and the namespace
  `sword-world-rpg-complete-edition`.
- `uv run llmwiki ingest javascriptallonge.pdf` -> existing PDF ingest behavior
  is unchanged.
- `uv run llmwiki ingest book.pdf --profile rulebook --profile table-heavy` ->
  overlays compose in deterministic order; neither profile can hard-code the
  source prefix.

## Acceptance Criteria

- Tests prove profile TOML loading validates required fields, filename/id
  agreement, enabled status, overlay variable names, and priority ordering.
- Tests prove unknown and disabled profile selection fails before model or PDF
  extraction work begins.
- Tests prove `source_slug` and `source_namespace` are derived from the source
  name and rendered into overlays.
- Tests prove no-profile ingest builds the same prompt template text as today.
- Tests prove PDF map and integrate workflows both receive selected overlays.
- `llmwiki profiles` lists enabled and disabled profiles without starting the
  model backend.
- README documents `--profile` and the `profiles/ingest/*.toml` extension point.
- `SCHEMA.md` states how profiles relate to the base ingest workflow.
- `uv run ruff check harness/src harness/tests` passes.
- Relevant tests pass.

## Implementation Notes

- Added `llmwiki.domain.ingest_profiles` as the pure profile registry and prompt
  composition boundary.
- Added `profiles/ingest/rulebook.toml` as the first data-defined profile.
- Added repeatable `llmwiki ingest --profile <id>` selection and
  `llmwiki profiles` discovery.
- Profile selection happens before backend startup, PDF extraction, or model
  calls.
- Selected profile ids print on ingest stderr as `[ingest-profiles: ...]`.
- Existing no-profile ingest prompt templates remain unchanged.
- Live Sword World validation added several profile-adjacent guardrails:
  - non-Apple platforms fall back to text-layer PDF extraction without requiring
    Apple Vision OCR;
  - namespace enforcement can be enabled from profile data with
    `namespace.require_for_new_pages = true`;
  - rulebook naming can block new same-namespace singular/plural sibling pages
    with `naming.prevent_singular_plural_siblings = true`;
  - chunk map runs use bounded page previews so a large prior chunk page cannot
    consume the local model's context;
  - final PDF integration writes through a fixed hub-page adapter, so the model
    cannot accidentally create `*-hub` or unrelated chapter pages during the hub
    pass;
  - the hub writer rescues two observed small-model tool-call malformations:
    source strings supplied as a single value and `content` embedded in the
    `summary` field after a `parameter=content>` marker;
  - the final hub writer now measures links against the chunk manifest and adds
    a deterministic `Page-Map Navigation` section when the model-authored prose
    under-links the pages written during chunking.

## Verification

- `uv run pytest harness/tests/test_ingest_profiles.py harness/tests/test_cli_config.py`
  passed: 42 tests.
- `uv run ruff check harness/src harness/tests` passed.
- `uv run mypy harness/src` passed.
- `uv run pytest harness/tests` passed: 258 tests.
- `uv run llmwiki profiles` listed the enabled `rulebook` profile without
  starting the model.
- `uv run llmwiki ingest --help` shows repeatable `--profile PROFILE`.
- `git diff --check` passed.
- Live validation on `raw/Sword World RPG - Complete Edition.pdf`:
  - all 69 chunks completed and the manifest was reused with `--reintegrate`
    while fixing the hub phase;
  - final hub `wiki/sword-world-rpg-complete-edition.md` was written with 34
    wiki links, including the deterministic `Page-Map Navigation` fallback;
  - no stray `sword-world-rpg-complete-edition-hub` or
    `sword-world-rpg-complete-edition-chapter-13-2-1-humans` page/link remains.

## Cross-Cutting Concerns

Observability: ingest stderr should print selected profile ids next to runtime
and strict-evidence status so transcripts can be interpreted later.

Error handling: profile validation errors are configuration errors and must
occur before extraction, model startup, or wiki writes.

Security: profiles are inert data. Overlay rendering is variable substitution
only; profiles cannot invoke shell commands, import Python, or alter tool
contracts.

## Reference Implementations

- CLI option patterns: `harness/src/llmwiki/cli.py`.
- Ingest orchestration: `harness/src/llmwiki/runtime/session.py`.
- PDF map/integrate workflow construction:
  `harness/src/llmwiki/workflows/pdf_ingest.py`.
- Prompt templates: `harness/src/llmwiki/workflows/prompts.py`.
- Slug behavior: `harness/src/llmwiki/domain/pages.py`.

## Alternatives Considered

- Hard-code a Sword World prompt branch - rejected because profiles must be
  source-agnostic and removable.
- Separate wiki roots now - rejected until open question #18 has evidence that
  namespacing and index routing fail.
- Automatic filename-based profile activation - rejected for v1 because profile
  choice is a curator decision.
- One opaque extra prompt string flag - rejected because reusable profiles need
  validation, listing, disabled state, and deterministic composition.

## Halt Conditions

- If implementation requires changing `wiki/` from a flat page namespace to
  domain directories, stop and write a separate TDD.
- If rulebook support requires deterministic table extraction or catalog JSON,
  stop and write a separate TDD.
- If profile overlays need variables beyond the required contract, stop and
  update this TDD before implementation.
- If prompt composition changes the no-profile ingest prompt, stop unless the
  curator explicitly accepts that compatibility break.
