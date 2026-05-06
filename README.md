# LLM-Wiki User Guide

This repository is a local-first implementation of the LLM-Wiki pattern described in
[REFERENCE_llm-wiki-pattern.md](REFERENCE_llm-wiki-pattern.md). The goal is not ordinary RAG. The goal is
a persistent Markdown wiki that grows over time as sources are ingested, queries are filed, contradictions
are noticed, and maintenance passes clean up the knowledge graph.

The short version:

1. Put source files in `raw/inbox/`.
2. Import and normalize them into immutable raw storage.
3. Compile source-backed wiki pages under `wiki/`.
4. Ask questions against the wiki, not the raw files.
5. File durable answers back into `wiki/analyses/`.
6. Run maintenance so the wiki remains navigable, grounded, and auditable.

The human is the curator. The local model is the disciplined maintainer. The deterministic tools are the
guard rails that make the work small enough for local models running on a 4090-class GPU.

## Table Of Contents

- [The Core Idea](#the-core-idea)
- [Architecture](#architecture)
- [Use Cases And Source Curation](#use-cases-and-source-curation)
- [Operating Schema](#operating-schema)
- [First Principles](#first-principles)
- [Quick Start](#quick-start)
- [Start Talking To The LLM-Wiki](#start-talking-to-the-llm-wiki)
- [Ingest](#ingest)
- [Query](#query)
- [File Durable Analyses](#file-durable-analyses)
- [Lint And Maintenance](#lint-and-maintenance)
- [Index And Log](#index-and-log)
- [Graph](#graph)
- [Evidence And Auditability](#evidence-and-auditability)
- [Contradictions](#contradictions)
- [Executable Concepts](#executable-concepts)
- [Curator Review Status](#curator-review-status)
- [Model Benchmarking And Defaults](#model-benchmarking-and-defaults)
- [Scheduled Maintenance](#scheduled-maintenance)
- [Optional CLI And Obsidian Workflows](#optional-cli-and-obsidian-workflows)
- [Outputs Beyond Markdown](#outputs-beyond-markdown)
- [How To Learn This System](#how-to-learn-this-system)
- [What Good Looks Like](#what-good-looks-like)
- [Why This Works](#why-this-works)
- [Scope And Adaptation](#scope-and-adaptation)

## The Core Idea

Most document AI workflows retrieve raw chunks at question time. That can answer questions, but it does not
build a durable knowledge layer. The LLM has to rediscover the same structure over and over.

LLM-Wiki works differently. The model incrementally compiles raw sources into a persistent, interlinked
Markdown wiki. The wiki becomes the reusable layer between the human and the raw documents.

Implemented here:

- Raw source files are preserved under `raw/imported/`.
- Normalized source text lives under `raw/normalized/`.
- One source page is created under `wiki/sources/` for every ingested source.
- Reusable knowledge is compiled into `wiki/concepts/`, `wiki/entities/`, `wiki/procedures/`, and
  `wiki/references/`.
- Durable answers to questions are filed under `wiki/analyses/`.
- `wiki/index.md`, `wiki/log.md`, and `wiki/_graph.json` keep the wiki navigable and machine-readable.

Expected postconditions:

- The wiki becomes more useful after each real ingest or durable query.
- Important claims link back to source pages.
- Source-backed claims include evidence excerpts and normalized locators when possible.
- The system does not need to re-read raw documents for every ordinary query.

## Architecture

The reference pattern has three layers: raw sources, wiki, and schema. This repository implements those
layers as follows.

| Layer                  | Path                            | Purpose                                                       | Who Edits It                 |
| ---------------------- | ------------------------------- | ------------------------------------------------------------- | ---------------------------- |
| Raw inbox              | `raw/inbox/`                    | Drop new PDFs or Markdown files here.                         | Human                        |
| Immutable originals    | `raw/imported/`                 | Preserved source-of-truth files.                              | Tools only on initial import |
| Normalized text        | `raw/normalized/`               | Markdown extracted from PDFs or copied from Markdown sources. | Tools                        |
| Assets                 | `raw/assets/`                   | Extracted or locally saved media.                             | Human and tools              |
| Wiki                   | `wiki/`                         | Synthesized knowledge layer.                                  | Agent and tools              |
| Operating schema       | `AGENTS.md`                     | Rules for agents maintaining the wiki.                        | Human-approved edits         |
| Design source of truth | `DESIGN_atomic-local-ingest.md` | Local-model workflow design.                                  | Human and agent              |
| Deterministic tools    | `tools/`                        | Validators, orchestrators, judges, reports.                   | Agent, with tests            |
| Executable concepts    | `packages/concepts/`            | TypeScript implementations and tests.                         | Agent, with tests            |

Expected postconditions:

- `raw/imported/` remains immutable.
- `wiki/` contains synthesized Markdown, not raw dumps.
- `AGENTS.md` remains the operating contract for future agents.
- Tooling gives repeatable checks instead of relying only on prompt compliance.

## Use Cases And Source Curation

The reference pattern can be used for personal research, books, business knowledge, course notes, competitive
analysis, trip planning, hobbies, and other long-running domains. This repository is domain-neutral, but the
current sample content includes Age of Empires II notes and compound interest.

The human curator chooses what belongs in the wiki. Good sources are:

- PDFs or Markdown files that contain durable information.
- Notes that you expect to ask about again.
- Sources whose claims should be compared with future sources.
- Materials that can produce reusable concepts, entities, procedures, references, or analyses.

Use `raw/inbox/` as the handoff point:

```bash
cp ~/Downloads/source.pdf raw/inbox/example.pdf
pnpm wiki:ingest raw/inbox/example.pdf --slug example --dry-run
```

Expected postconditions:

- Sources enter through a deliberate queue, not scattered paths.
- Private or bulky raw files can remain untracked by git according to repo policy.
- The human remains responsible for what sources are worth ingesting.
- The wiki can grow one source at a time, which is the safest mode for local models.

## Operating Schema

The reference pattern calls the schema the key configuration file. In this repo, the schema is
[AGENTS.md](AGENTS.md). It defines page formats, sacred rules, workflows, validation commands, and stop
conditions for agents.

When the operating rules need to change:

1. Prefer a proposal in `wiki/log.md`.
2. Update `AGENTS.md` only when the curator agrees with the change.
3. Update this README if the user-facing workflow changes.
4. Run maintenance after schema or tool changes.

```bash
pnpm wiki:log proposal "change ingest policy" --detail "Proposed reason and expected effect"
pnpm wiki:maintenance --append-log
```

Expected postconditions:

- Future agents get the same operating contract.
- Workflow changes are visible in git and `wiki/log.md`.
- The schema evolves with the domain instead of becoming stale hidden context.

## First Principles

These are the rules that make the wiki trustworthy.

- Never edit `raw/imported/`.
- Never invent facts to fill gaps.
- Every important claim should point back to a source page.
- Prefer updating existing pages over creating duplicates.
- Record contradictions before resolving them.
- Use deterministic validation before trusting local-model output.
- Keep local-model tasks small and atomic.
- If reusable knowledge appears during a query, file it back into the wiki.

Expected postconditions:

- Claims can be audited.
- Missing coverage is explicit as `not covered in sources`.
- The local model can check its own work using deterministic tools.
- The human can review and promote pages from `draft` to `reviewed` or `stable`.

## Quick Start

Install dependencies first:

```bash
pnpm install
```

Run the current health checks:

```bash
pnpm wiki:maintenance --append-log
```

Dry-run an ingest:

```bash
pnpm wiki:ingest raw/inbox/example.pdf --slug example --dry-run
```

Ask a query plan:

```bash
pnpm wiki:query "What should I know about this topic?" --plan-only
```

List curator review status:

```bash
pnpm wiki:curator-status --list
```

Expected postconditions:

- Maintenance writes `wiki/_maintenance-report.md`.
- Dry-run commands print the steps they would execute.
- Query planning shows which wiki pages would be read before a model is invoked.
- Status listing shows how many pages are `draft`, `reviewed`, and `stable`.

## Start Talking To The LLM-Wiki

The normal interactive workflow is: start Codex from the repo root, tell it to operate under the LLM-Wiki
contract, ask questions, and explicitly file reusable knowledge back into the wiki when something should
persist.

### 1. Launch Codex Locally

Run this from the repository root:

```bash
cd /llm-wiki
codex --profile local-4090
```

Expected postconditions:

- Codex starts with access to this repository.
- Local model execution uses the `local-4090` profile.
- Future file edits happen in the LLM-Wiki working tree.

### 2. Bootstrap The Session

`AGENTS.md` is the operating contract, but local models do better when the first prompt is explicit. Use this
at the start of a session:

```text
Read AGENTS.md fully before acting.

You are maintaining this repository as an LLM-Wiki.
Use wiki/index.md and wiki/_graph.json first.
Prefer existing wiki pages over raw sources.
Do not invent facts.
Every durable claim must point back to source pages.
If we uncover reusable knowledge, ask whether to file it back into the wiki, or file it if I explicitly request that.
When changing wiki structure, update wiki/index.md, wiki/_graph.json, and wiki/log.md.
Run the relevant checks before finishing.
```

Expected postconditions:

- The agent treats `AGENTS.md` as the source of operating rules.
- The agent answers from the wiki before falling back to raw sources.
- The agent understands that reusable answers should become wiki pages only when requested or confirmed.

### 3. Ask Without Changing Files

Use this pattern for normal questions:

```text
Using the LLM-Wiki, explain AoE2 build orders and how they relate to economy balance.
Cite the wiki pages you use.
Do not update files yet.
```

Expected postconditions:

- The agent reads `wiki/index.md` and relevant pages under `wiki/`.
- The answer cites wiki pages and source pages when useful.
- No files change.

### 4. File A Durable Answer

If an answer is reusable, tell the agent to file it:

```text
This answer is reusable. File it as a durable analysis page.
Update wiki/index.md, wiki/_graph.json, and wiki/log.md.
Run the relevant checks.
```

For a specific filename, use:

```text
File this as wiki/analyses/YYYY-MM-DD-aoe2-build-orders-and-economy-balance.md.
Use type: analysis.
Link to the source pages and related concept/procedure pages.
Make sure important claims cite source pages.
Update index, graph, and log.
Run maintenance.
```

Expected postconditions:

- A new page exists under `wiki/analyses/`.
- The analysis links to source pages and related wiki pages.
- Important claims cite source pages.
- `wiki/index.md`, `wiki/_graph.json`, and `wiki/log.md` are updated.
- Relevant checks pass.

### 5. Ingest A New Source

Put a PDF or Markdown file in `raw/inbox/` first:

```bash
cp ~/Downloads/my-source.pdf raw/inbox/my-source.pdf
```

Then ask Codex:

```text
Read AGENTS.md fully before acting.

Ingest raw/inbox/my-source.pdf as slug my-source.
Use the local-model phased workflow.
Preserve raw/imported/.
Create the source page, synthesize useful concept/entity/procedure/reference pages, update index, graph, and log.
Run the relevant checks.
```

Or run the deterministic orchestrator directly:

```bash
pnpm wiki:ingest raw/inbox/my-source.pdf --slug my-source --dry-run
pnpm wiki:ingest raw/inbox/my-source.pdf --slug my-source --max-phase2-pages 5
```

Expected postconditions:

- `raw/imported/my-source/` preserves the original.
- `raw/normalized/my-source/` contains normalized Markdown.
- `wiki/sources/my-source.md` exists.
- Useful synthesized pages are created or updated.
- Wiki bookkeeping and checks are updated.

### 6. Add Knowledge From Conversation

Do not let chat-only facts silently become wiki facts. If something learned in conversation should become part
of the wiki, first turn it into a source note.

Example:

```text
I want to add the following curator note as a source, then synthesize it into the wiki:

<your note here>

Create a Markdown source in raw/inbox/curator-note-YYYY-MM-DD-topic.md.
Then ingest it as a markdown source.
Preserve the original under raw/imported/.
Create or update relevant wiki pages.
Update index, graph, and log.
Run checks.
```

Expected postconditions:

- The curator note is preserved as an auditable source.
- Synthesized pages cite the new source page.
- Future answers can distinguish source-document facts from curator notes.

### 7. Useful Session Prompts

Ask from the wiki only:

```text
Answer from the wiki only. Cite pages used. Do not update files.
```

Save a useful answer:

```text
File this answer as a durable analysis and update the wiki bookkeeping.
```

Ingest a new source:

```text
Ingest raw/inbox/example.pdf as slug example using the phased local workflow.
```

Clean up health:

```text
Run wiki maintenance, summarize failures, and fix only deterministic/wiki-structure issues.
```

Review pages:

```text
List draft pages that are ready for curator review.
```

Expected postconditions:

- Conversation remains natural while durable knowledge is deliberately filed.
- The wiki only changes when you ask for a change.
- Filed knowledge has source links, index updates, graph updates, log entries, and checks.

## Ingest

Ingest turns one raw source into source-backed wiki knowledge. This implementation uses deep extraction
to achieve 100% source coverage, then synthesizes pages with quality gates.

### Full Orchestrated Ingest

Use the unified orchestrator for the normal path:

```bash
pnpm wiki:ingest raw/inbox/example.pdf --slug example --dry-run
pnpm wiki:ingest raw/inbox/example.pdf --slug example
```

For Markdown:

```bash
pnpm wiki:ingest raw/inbox/example.md --slug example --dry-run
pnpm wiki:ingest raw/inbox/example.md --slug example
```

The unified ingest flow:

1. **Phase 0**: Normalizes the source (PDF to markdown via `marker_single`)
2. **Phase 1**: Deep extracts claims from all chunks (100% source coverage)
3. **Phase 2a**: Creates source page from extracted topics
4. **Phase 2b**: Synthesizes each topic page with quality gates (validate + judge + repair)
5. **Phase 3**: Updates index, graph, and log

Key options:

- `--max-phase2-pages N` — limit synthesized pages (default: 10)
- `--min-claims-per-topic N` — minimum claims to create a page (default: 3)
- `--chunk-size N` — lines per chunk (default: 400)
- `--skip-extract` — skip extraction, use existing state
- `--dry-run` — show what would happen

Batch ingest is intentionally not the default. The reference allows batch ingestion, but this local-first
implementation works best one source at a time because each source can create or update many pages.

If you want to steer emphasis manually, run deep extraction only, inspect the state, then resume:

```bash
pnpm wiki:deep-extract example --extract-only
# Inspect .tmp/deep-extract/example/state.json
pnpm wiki:ingest --slug example --skip-extract --max-phase2-pages 3
```

Expected postconditions:

- `raw/imported/<slug>/original.pdf` or `original.md` exists.
- `raw/normalized/<slug>/` contains normalized Markdown.
- `wiki/sources/<slug>.md` exists and passes source validation.
- Several synthesized pages are created when the source is non-trivial.
- `wiki/index.md`, `wiki/_graph.json`, `wiki/_linter-report.md`, and `wiki/log.md` are updated.

### Phase 0: Import And Normalize

Run Phase 0 directly when you want only the raw import step:

```bash
pnpm wiki:phase0 raw/inbox/example.pdf example
pnpm wiki:phase0 raw/inbox/example.md example
```

For PDFs, Phase 0 uses `marker_single` with `TORCH_DEVICE=cuda` by default. For Markdown, it copies the
source into normalized Markdown.

Expected postconditions:

- The original file is copied exactly once into `raw/imported/<slug>/`.
- Normalized Markdown exists under `raw/normalized/<slug>/`.
- Existing imported originals are not overwritten unless `--reuse-imported` proves the bytes match.

### Deep Extraction

Deep extraction processes the source in chunks to achieve 100% coverage:

```bash
pnpm wiki:deep-extract example --dry-run   # Show chunks
pnpm wiki:deep-extract example             # Full extraction + synthesis
pnpm wiki:deep-extract example --extract-only  # Claims only, no pages
pnpm wiki:deep-extract example --resume    # Continue interrupted extraction
```

The state is saved to `.tmp/deep-extract/<slug>/state.json` after each chunk, making extraction resumable.

Expected postconditions:

- All chunks are processed.
- Claims are aggregated by topic.
- State file records progress and all extracted claims.

### Phase 1: Source Page

For manual Phase 1 trials, use the benchmark tool:

```bash
pnpm wiki:phase1-benchmark example --candidate local-4090
```

The source page must include:

- YAML frontmatter.
- `type: source`.
- Source metadata.
- `## Summary`.
- `## Key claims`.
- `## Major concepts`.
- `## Entities`.
- `## Procedures`.
- `## References`.
- `## Open questions`.
- `## Related pages`.

Expected postconditions:

- `wiki/sources/<slug>.md` exists.
- Key claims are evidence-backed and locator-backed.
- Related pages are listed as candidate paths if they do not exist yet.
- No synthesized pages are created in Phase 1.
- Validation passes:

```bash
pnpm wiki:check-source <slug>
```

### Phase 2: Synthesized Pages

Phase 2 creates or updates one synthesized page at a time:

```bash
pnpm wiki:phase2-single example ../concepts/example-topic.md --candidate local-4090 --judge-batch --report /tmp/example-phase2.md
```

This is deliberately atomic. The local model gets one selected page, a bounded evidence bank, and exact
validation commands.

Expected postconditions:

- Exactly the selected page is created or updated.
- The source page's `## Related pages` row is changed from a code-formatted candidate path to a real link.
- The page has `## Source-backed details`.
- Evidence rows use exact excerpts and normalized locators.
- Selected pages are range-gated when a source heading or `source_ranges` frontmatter can define the page's
  allowed source span.
- Deterministic validation and local claim judging pass.

### Phase 3: Finalize

Run Phase 3 after source and synthesis phases pass:

```bash
pnpm wiki:phase3 example
```

Expected postconditions:

- `wiki/index.md` is regenerated.
- `wiki/_graph.json` is regenerated.
- `wiki/_linter-report.md` is regenerated.
- `wiki/log.md` receives an `ingest` entry.

## Query

A query should use the wiki first. The model should not re-read raw sources unless the wiki is insufficient.
The query planner starts from `wiki/index.md`, uses `wiki/_graph.json` when useful, and selects a bounded set of
pages for the local model.

Plan the query:

```bash
pnpm wiki:query "How should an AoE2 player adapt strategy across water and mixed maps?" --plan-only
```

Run the query with a local model:

```bash
pnpm wiki:query "How should an AoE2 player adapt strategy across water and mixed maps?" --candidate local-4090
```

Expected postconditions:

- The query planner selects a small set of relevant wiki pages.
- The answer cites wiki pages with relative Markdown links.
- If the wiki does not cover something, the answer says `not covered in sources`.
- No files change unless `--save-analysis` is used.

## File Durable Analyses

Good answers should not disappear into chat history. File reusable answers into `wiki/analyses/`.

```bash
pnpm wiki:query "How should an AoE2 player adapt strategy across water and mixed maps?" \
  --candidate local-4090 \
  --save-analysis \
  --slug aoe2-water-and-mixed-map-strategy
```

Then validate and judge:

```bash
pnpm wiki:check-analysis wiki/analyses/YYYY-MM-DD-example.md
pnpm wiki:judge-analysis wiki/analyses/YYYY-MM-DD-example.md --candidate local-4090 --fail-on-issues
```

Expected postconditions:

- A new `wiki/analyses/YYYY-MM-DD-<slug>.md` page exists.
- Its frontmatter `sources` list contains source pages, not arbitrary related wiki pages.
- The body links to source pages and related wiki pages.
- Normalized locators such as `normalized:L12` resolve against cited source pages.
- If multiple source pages are cited, locators should be prefixed like `aoe2-basics:normalized:L12`.
- Wiki page line anchors such as `#L12` are rejected as evidence citations.
- `wiki/index.md`, `wiki/_graph.json`, and `wiki/log.md` are updated when the analysis is filed.

## Lint And Maintenance

Linting is the wiki health check. Maintenance bundles linting with other deterministic checks.

Run the full maintenance sweep:

```bash
pnpm wiki:maintenance --append-log
```

Run individual checks:

```bash
pnpm wiki:lint
pnpm wiki:grounding:check
pnpm wiki:semantic-lint
pnpm wiki:contradictions
pnpm wiki:executables --check
pnpm wiki:curator-status --check
```

Expected postconditions:

- `wiki/_maintenance-report.md` summarizes all checks.
- `wiki/_linter-report.md` reports structural wiki health.
- `wiki/_semantic-linter-report.md` reports likely duplicates or overlap.
- `wiki/_contradiction-report.md` reports possible cross-source contradictions.
- `wiki/_executable-report.md` reports executable-concept issues.
- `wiki/log.md` receives a `lint` entry when `--append-log` is used.

## Index And Log

The reference pattern calls out `index.md` and `log.md` as special files. This repo implements them as:

- `wiki/index.md`: content catalog organized by page type.
- `wiki/log.md`: append-only chronological history.

Regenerate and check the index:

```bash
pnpm wiki:index
pnpm wiki:index:check
```

Append a log entry:

```bash
pnpm wiki:log todo "short summary" --detail "specific detail"
```

Expected postconditions:

- `wiki/index.md` lists sources, entities, concepts, procedures, references, analyses, and code.
- `wiki/log.md` entries follow `## [YYYY-MM-DD] operation | summary`.
- Recent work can be found with:

```bash
grep "^## \\[" wiki/log.md | tail -5
```

## Graph

The wiki has a machine-readable dependency graph:

```bash
pnpm wiki:graph
pnpm wiki:graph:check
```

Expected postconditions:

- `wiki/_graph.json` contains one node per content page.
- Each node records type, path, description, sources, and dependencies.
- The graph is stale if wiki pages change without regeneration.

## Evidence And Auditability

Every important synthesized claim should be auditable.

Use this table shape in synthesized pages:

```md
| Claim                    | Evidence                      | Locator          | Source                                |
| ------------------------ | ----------------------------- | ---------------- | ------------------------------------- |
| Concrete reusable claim. | "Short exact source excerpt." | `normalized:L12` | [Source title](../sources/example.md) |
```

Check synthesis:

```bash
pnpm wiki:check-synthesis <slug> --normalized-source raw/normalized/<slug>/source.md
```

Check claim support with a local model:

```bash
pnpm wiki:judge-claims wiki/concepts/example.md \
  --normalized-source raw/normalized/<slug>/source.md \
  --candidate local-4090 \
  --fail-on-issues
```

Expected postconditions:

- Evidence excerpts are exact substrings from normalized source lines.
- Locators resolve to the cited line range.
- Claims do not merely repeat evidence.
- Weak generic claims are flagged.
- Range-gated pages cannot cite unrelated source sections.

## Contradictions

The reference pattern says new sources should strengthen, challenge, or contradict the evolving synthesis.
This repo records contradictions in `wiki/log.md` and scans source claim tables.

Run:

```bash
pnpm wiki:contradictions
```

Expected postconditions:

- `wiki/_contradiction-report.md` is produced.
- Candidate contradictions are listed when multiple substantial sources exist.
- If an important contradiction is found, the agent should add a `contradiction` entry to `wiki/log.md`.
- The system currently reports that contradiction scanning is not meaningful until at least two substantial
  source pages exist.

## Executable Concepts

Some sources imply deterministic formulas or procedures. The repo supports executable TypeScript concepts in:

- `packages/concepts/src/`
- `packages/concepts/tests/`

Check executable concept health:

```bash
pnpm wiki:executables
pnpm code:typecheck
pnpm code:test
```

Expected postconditions:

- Pages with `## Executable implementation` link to a TypeScript implementation and tests.
- Formula-like pages without executable implementation are reported as backlog warnings.
- Code typechecks and tests pass before code changes are considered complete.

## Curator Review Status

The human curator decides when pages move from draft to reviewed or stable.

List current status:

```bash
pnpm wiki:curator-status --list
```

Promote a page:

```bash
pnpm wiki:curator-status wiki/concepts/example.md \
  --set reviewed \
  --reason "curator checked evidence"
```

Expected postconditions:

- Page frontmatter `status` changes to `reviewed` or `stable`.
- `last_updated` is refreshed.
- `reviewed_by` is recorded for reviewed or stable pages.
- `stabilized_on` is recorded only for stable pages.
- `wiki/log.md` receives a cleanup entry documenting the review action.

## Model Benchmarking And Defaults

Local models vary. This repo keeps phase defaults in:

```text
tools/wiki_model_defaults.json
```

Dry-run a benchmark:

```bash
pnpm wiki:model-benchmark --candidate local-4090 --dry-run
```

Run a benchmark and update defaults:

```bash
pnpm wiki:model-benchmark --candidate local-4090 --update-defaults
```

Expected postconditions:

- `wiki/_model-benchmark-report.md` records benchmark results.
- Passing candidates are compared by phase and duration.
- `tools/wiki_model_defaults.json` can be updated with the fastest passing candidate per phase.
- `pnpm wiki:ingest` uses these defaults unless overridden.

## Scheduled Maintenance

The reference pattern recommends periodic linting. This repo provides a user-level systemd helper.

Inspect the unit files:

```bash
pnpm wiki:maintenance:systemd --dry-run
```

Install for the current user:

```bash
pnpm wiki:maintenance:systemd --install
```

Expected postconditions:

- User systemd units are written under `~/.config/systemd/user/`.
- The timer runs `pnpm wiki:maintenance --append-log`.
- `ops/systemd/` contains checked-in templates for review.

## Optional CLI And Obsidian Workflows

The reference pattern suggests using the wiki as a Markdown knowledge base, often with Obsidian. This repo is
compatible with that workflow because the wiki is plain Markdown.

Useful habits:

- Use Obsidian Web Clipper or another converter to turn web pages into Markdown, then put the result in
  `raw/inbox/`.
- If a source depends on images, save them locally under `raw/assets/` and link them from the normalized
  Markdown or source notes.
- Open `wiki/` in Obsidian.
- Use graph view to inspect hub pages and orphans.
- Browse `wiki/index.md` as the main table of contents.
- Use `wiki/log.md` as the chronological history.
- Use Dataview only as an optional Obsidian reading aid. The repo itself does not require it.
- Use Marp only when a wiki analysis needs to become a presentation. Markdown pages remain the primary
  durable artifact.
- Use git to review every model/tool change.

Search is currently implemented with deterministic page selection in `tools/wiki_query.py`, not a vector search
engine. A separate Markdown search tool such as `qmd` could be added later if the wiki grows beyond what the
index and graph can handle comfortably.

Expected postconditions:

- The wiki remains usable without a database.
- Obsidian is optional, not required.
- Local assets are available to humans and models even if external URLs disappear.
- Git diffs show exactly what the agent changed.

## Outputs Beyond Markdown

The reference pattern mentions answers that may become slide decks, charts, canvases, or other artifacts.
This implementation currently treats Markdown wiki pages as the durable output format.

Implemented:

- Source pages.
- Concept/entity/procedure/reference pages.
- Analysis pages.
- TypeScript executable concepts.
- Reports under `wiki/_*.md` and `wiki/_graph.json`.

Not currently automated:

- Slide decks.
- Charts.
- Canvas documents.
- Image extraction workflows beyond PDF normalization artifacts.

Expected postconditions:

- Durable knowledge is filed as Markdown first.
- Other output formats should be added only when the wiki has a concrete need for them.

## How To Learn This System

This section presents the implementation using the Michel Thomas teaching idea: analyze the material correctly,
teach the most useful pieces in a logical progression, and present each piece in a way that reduces strain.

### 1. The Analysis

There are only four things to keep in your head:

1. `raw/` is evidence.
2. `wiki/` is compiled knowledge.
3. `tools/` are checks and repeatable workflows.
4. `AGENTS.md` is the operating contract.

Everything else is a variation on that.

If a file is in `raw/imported/`, the model must not change it. If a claim is in `wiki/`, it should be traceable
back to `wiki/sources/`. If a workflow feels risky, there should be a deterministic check for it.

### 2. The Progression

Learn the system in this order:

1. Read the wiki:

```bash
less wiki/index.md
```

2. Check health:

```bash
pnpm wiki:maintenance --append-log
```

3. Ask without changing files:

```bash
pnpm wiki:query "question" --plan-only
```

4. Ask and save only if the answer is reusable:

```bash
pnpm wiki:query "question" --candidate local-4090 --save-analysis --slug useful-answer
```

5. Ingest with a dry run first:

```bash
pnpm wiki:ingest raw/inbox/example.pdf --slug example --dry-run
```

6. Review and promote pages:

```bash
pnpm wiki:curator-status wiki/concepts/example.md --set reviewed --reason "checked evidence"
```

This order matters. Query planning is easier than source ingest. Maintenance is easier than synthesis.
Reviewing a page is easier once evidence locators already exist.

### 3. The Presentation

Use the same question for every operation:

```text
What should exist after this command finishes?
```

For ingest, the answer is source page, synthesized pages, index, graph, log. For query, the answer is a cited
response and maybe an analysis page. For lint, the answer is reports and a log entry. For review, the answer is
status metadata and a log entry.

This keeps the system learnable because each command has a visible postcondition. You are not trusting a model
because it sounded confident. You are checking the files it produced.

## What Good Looks Like

A healthy LLM-Wiki has these properties:

- `wiki/index.md` is enough to navigate the knowledge base.
- `wiki/log.md` tells the history of ingests, queries, lint passes, proposals, contradictions, and review actions.
- Source pages link to synthesized pages.
- Synthesized pages link back to source pages.
- Important claims have evidence excerpts and locators.
- Durable query answers are filed under `wiki/analyses/`.
- Maintenance passes with zero failures.
- The curator can promote pages from `draft` to `reviewed` or `stable`.
- The wiki gets more useful after every source and every serious question.

The current implementation is local-first and deterministic-heavy by design. It is built to help smaller local
models succeed by giving them narrow tasks, exact checks, and a wiki that compounds instead of starting over.

## Why This Works

The reference pattern works because the model is not asked to remember everything in chat. It writes the useful
state into files.

Humans are good at choosing sources, asking questions, and noticing what matters. Humans are usually bad at
keeping hundreds of cross-links, summaries, and contradiction notes up to date. LLMs are useful here because
wiki maintenance is mostly bookkeeping with judgment at the edges.

This repo adds deterministic checks because local models need tighter rails than large frontier models:

- Exact evidence quotes prevent invented support.
- Locator checks make claims auditable.
- Range gates prevent keyword matches from unrelated sections.
- Index and graph checks prevent navigation drift.
- Maintenance reports make wiki health visible.

Expected postconditions:

- Knowledge compounds in Markdown instead of disappearing into chat history.
- The model spends less time rediscovering source structure.
- The human spends more time curating and reviewing than formatting and bookkeeping.

## Scope And Adaptation

The reference document is intentionally abstract. This repository is one concrete implementation.

Implemented now:

- Local PDF and Markdown ingest.
- Persistent Markdown wiki pages.
- Source, concept, entity, procedure, reference, and analysis page types.
- Index, log, graph, lint, grounding, semantic, contradiction, executable, and curator-status checks.
- Local-model benchmarking and phase defaults.
- Scheduled maintenance helper.
- TypeScript executable concept validation.

Not fully implemented yet:

- Automatic generation of new TypeScript code from formula-like wiki pages.
- Rich non-Markdown outputs such as slide decks, charts, or canvases.
- Vector search or qmd integration.
- Meaningful contradiction resolution before a second substantial source exists.
- A large corpus stress test.

Expected postconditions:

- The repo can be used today as a local LLM-Wiki.
- New domains should adapt page candidates, source groupings, and executable concepts as evidence demands.
- The implementation should change through logged, reviewed edits rather than hidden prompt drift.
