# LLM-Wiki operating rules

> This is the operating manual for this repository.
> Read it fully before any ingest, query, lint, or cleanup operation.
> The human is the curator. The agent is the disciplined wiki maintainer.
> When this document and the agent's instincts disagree, this document wins.
> If this document seems wrong, propose an edit in `wiki/log.md` before acting against it.

---

## Mission

Maintain the wiki in `/wiki` as the compiled knowledge layer for `/raw`.

The goal is not ordinary RAG. The goal is a persistent, interlinked Markdown wiki that accumulates knowledge over time.

Raw sources are preserved. The wiki is synthesized. Queries and lint passes should improve the wiki when they produce reusable knowledge.

---

## Sacred rules

1. `raw/imported/` is immutable. Never edit, reorganize, rename, or delete anything under it.
2. Do not invent facts to fill gaps. If a source does not cover something, write `not covered in sources`.
3. Every important claim must point back to a source page.
4. Every source page must link to synthesized pages when useful.
5. A non-trivial source should not produce only one source page.
6. Prefer updating existing pages over creating duplicates.
7. If two sources disagree, record the contradiction in `wiki/log.md` before resolving it.
8. If an ingest requires changing this operating contract, propose the change in `wiki/log.md` before doing the ingest.
9. If code changes are made, tests must run before the task is considered complete.
10. Never hide uncertainty. Write the uncertainty into the page.

---

## Repository map

- `raw/inbox/`: user drops new PDFs or markdown files here
- `raw/imported/`: immutable originals
- `raw/normalized/`: extracted or normalized markdown
- `raw/assets/`: extracted images and media
- `wiki/index.md`: content catalog and main navigation entrypoint
- `wiki/log.md`: append-only chronological history
- `wiki/_graph.json`: machine-readable dependency graph
- `wiki/_linter-report.md`: latest wiki health report
- `wiki/sources/`: one page per source
- `wiki/concepts/`: canonical concept pages
- `wiki/entities/`: people, orgs, projects, libraries, games, units, named things
- `wiki/procedures/`: workflows, how-tos, build orders, operating steps
- `wiki/references/`: tables, formulas, constants, lookup facts
- `wiki/analyses/`: durable analyses generated from questions
- `packages/concepts/src/`: executable TypeScript implementations
- `packages/concepts/tests/`: tests for implementations
- `tools/`: repo helper scripts

If a needed directory does not exist, create it.

---

## Page types

Use these page types in YAML frontmatter:

- `source` — one page per ingested raw source
- `entity` — named thing: person, org, project, game, civilization, unit, building, library, tool
- `concept` — reusable explanation or abstract idea
- `procedure` — how-to, workflow, build order, debugging procedure
- `reference` — tables, formulas, constants, lookup facts
- `analysis` — durable answer to a user question

Special operational files are not content pages and do not require page-type frontmatter:

- `wiki/index.md`
- `wiki/log.md`
- `wiki/_analysis-judge-report.md`
- `wiki/_claim-judge-report.md`
- `wiki/_contradiction-report.md`
- `wiki/_graph.json`
- `wiki/_linter-report.md`
- `wiki/_grounding-report.md`
- `wiki/_maintenance-report.md`
- `wiki/_semantic-linter-report.md`

---

## Required frontmatter

Every wiki page must begin with YAML frontmatter.

General page format:

```yaml
---
title: <Human readable title>
type: source | entity | concept | procedure | reference | analysis
tags: []
status: draft
last_updated: YYYY-MM-DD
sources: []
---
```

Status values:

- `draft` — newly compiled or not yet reviewed
- `reviewed` — checked by the human
- `stable` — unlikely to change often

Source pages must include additional source metadata:

```yaml
---
title: <Human readable title>
type: source
source_id: <slug>
source_type: pdf | markdown | web | other
raw_path: ../../raw/imported/<slug>/
normalized_path: ../../raw/normalized/<slug>/
status: draft
last_updated: YYYY-MM-DD
tags: []
sources: []
---
```

---

## Source page format

Every page in `wiki/sources/` must include:

1. YAML frontmatter
2. `# Title`
3. `## Summary`
4. `## Key claims`
5. `## Major concepts`
6. `## Entities`
7. `## Procedures`
8. `## References`
9. `## Open questions`
10. `## Related pages`

If a section has no content, write `None.` or `not covered in sources`.

`## Key claims` must be auditable. Prefer this table shape over a plain list:

```md
| Claim                                             | Evidence                                          | Locator          |
| ------------------------------------------------- | ------------------------------------------------- | ---------------- |
| Concrete reusable claim in the agent's own words. | "Short exact excerpt from the normalized source." | `normalized:L12` |
```

The evidence cell must be copied exactly from `raw/normalized/<slug>/`, and the locator must point to
the normalized line or line range where that excerpt appears.

During ingest phase 1, synthesized pages usually do not exist yet. In that case, `## Related pages`
must list candidate future pages as code-formatted intended paths in a table, not Markdown links.
This records the planned graph without creating broken links.

Phase 1 must also study the source's natural groupings, even when ingesting a single PDF. Natural groupings
are source-native themes, chapters, or clusters of reusable knowledge. Record them inside `## Major concepts`
with a level-3 table, not as new wiki directories:

```md
### Natural groupings

| Group                    | Scope                       | Evidence basis                                     | Candidate page types |
| ------------------------ | --------------------------- | -------------------------------------------------- | -------------------- |
| Source-native group name | clear non-overlapping scope | concrete sections, claims, examples, or procedures | concept, procedure   |
```

Use those group names in `## Related pages` so Phase 2 can choose pages from the source's own structure.
The physical wiki directories remain type-based unless the curator approves a directory-structure proposal.

Example:

```md
| Candidate page       | Intended path                         | Group             | Priority    | Evidence basis                                 | Status          |
| -------------------- | ------------------------------------- | ----------------- | ----------- | ---------------------------------------------- | --------------- |
| AoE2 Economy Balance | `../concepts/aoe2-economy-balance.md` | Core fundamentals | must create | economy balance and resource allocation claims | not created yet |
```

After the synthesized pages are created in phase 2, replace relevant candidate rows with real Markdown
links to pages that exist.

Directory structure should follow the content, not assumptions. After 2-3 non-trivial ingests, or after one
large source makes the current structure clearly inadequate, run or draft a directory-structure proposal.
The proposal should list source-native groupings observed so far, compare them to the current type-based
directories, and recommend either keeping the current structure or changing it. Do not create new top-level
wiki directories until the proposal is logged and the curator agrees.

---

## Concept/entity/procedure/reference page format

Every synthesized page should include:

1. YAML frontmatter
2. `# Title`
3. Short definition or summary
4. Source-backed details
5. Cross-links to related pages
6. Source pages

Useful optional sections:

- `## Why it matters`
- `## Common mistakes`
- `## Examples`
- `## Open questions`
- `## Executable implementation`

Reference pages that include lookup tables must keep those tables auditable: include `Evidence` and
`Locator` columns for source-derived rows.

Type-specific required sections:

- Procedure pages must include `## Steps` with at least 3 concrete numbered or bulleted steps.
- Reference pages must include `## Reference data` with a Markdown lookup table containing at least 2 data rows.

---

## Cross-link rules

Use Markdown links for files:

```md
- [AoE2 Basics](../sources/aoe2-basics.md)
```

Use relative paths.

Every synthesized page should link back to at least one source page.

Every source page should link outward to the concept/entity/procedure/reference pages it produced or updated
once those pages exist. Before they exist, use the phase-1 candidate table described in Source page format.

Avoid orphan pages.

---

## Graph file

Maintain `wiki/_graph.json`.

Every content page under `wiki/sources/`, `wiki/concepts/`, `wiki/entities/`, `wiki/procedures/`,
`wiki/references/`, and `wiki/analyses/` should have one node.

Prefer generating `_graph.json` with:

```bash
pnpm wiki:graph
```

Use this check before finishing graph-related work:

```bash
pnpm wiki:graph:check
```

Do not hand-edit `_graph.json` unless the generator cannot represent a needed relationship. If that happens,
append a `schema-change` or `todo` entry to `wiki/log.md`.

Minimum structure:

```json
{
  "_meta": {
    "domain": "llm-wiki",
    "version": "0.1.0",
    "updated": "YYYY-MM-DD",
    "generated_by": "tools/wiki_graph.py"
  },
  "nodes": {
    "wiki:<dir>/<slug>": {
      "type": "source | entity | concept | procedure | reference | analysis",
      "path": "wiki/<dir>/<slug>.md",
      "description": "one-line summary",
      "sources": [],
      "depends_on": []
    }
  }
}
```

Update `_graph.json` on every ingest, query filing, or lint cleanup that changes wiki structure by running
`pnpm wiki:graph`.

---

## Ingest workflow

Use this workflow for each new source.

Local models must ingest in bounded phases. Do not ask a local model to perform all phases in one prompt.

### Phase 0: normalize source

1. If the source is a PDF, convert it to markdown from `raw/inbox/` into `raw/normalized/`.
2. If the source is markdown, preserve the original in `raw/imported/` and work from `raw/normalized/`.
3. Do not edit `raw/imported/`.

Use the deterministic importer when possible:

```bash
pnpm wiki:phase0 raw/inbox/<file.pdf> <slug>
pnpm wiki:phase0 raw/inbox/<file.md> <slug>
```

For PDFs, this wraps the local marker flow:

```bash
TORCH_DEVICE=cuda marker_single raw/inbox/<file.pdf> --output_format markdown --output_dir raw/normalized/<slug> --disable_tqdm
```

`wiki:phase0` copies the original once into `raw/imported/<slug>/original.pdf` or
`raw/imported/<slug>/original.md`. It refuses to overwrite imported originals. If an earlier attempt copied
the same original but normalization needs to be rerun, use `--reuse-imported --overwrite-normalized`; this
checks that the imported original bytes match the inbox file before touching `raw/normalized/`.

### Phase 1: source page only

1. Read the normalized source.
2. Create or update `wiki/sources/<slug>.md`.
3. Extract gameplay/content/domain claims, not just document metadata.
4. Identify candidate concepts, entities, procedures, and references.
5. Identify natural groupings from the source itself inside `## Major concepts`.
6. List candidate future pages in `## Related pages` as code-formatted paths in a table.
7. Prefer the evidence-aware candidate table shape with a source-native group column:

```md
| Candidate page  | Intended path                    | Group                    | Priority    | Evidence basis                                | Status          |
| --------------- | -------------------------------- | ------------------------ | ----------- | --------------------------------------------- | --------------- |
| Example Concept | `../concepts/example-concept.md` | Source-native group name | must create | concrete claims, examples, or procedure steps | not created yet |
```

8. Use priorities `must create`, `should create`, `could create`, or `defer`; Phase 2 should prefer higher-priority candidates with enough evidence for at least 3 evidence rows.
9. Do not create synthesized pages yet.
10. Do not update `wiki/index.md`, `wiki/log.md`, or `_graph.json` in this phase unless explicitly asked.
11. Validate the source page:

```bash
pnpm wiki:check-source <slug>
```

### Phase 2: synthesized pages

1. Use the source page and normalized source as needed.
2. Use the source page's natural groupings as page-boundary and priority signals; do not turn group names into new directories.
3. Create or update synthesized pages:
   - `wiki/concepts/`
   - `wiki/entities/`
   - `wiki/procedures/`
   - `wiki/references/`
4. Each synthesized page must link back to at least one source page.
5. Synthesized-page cross-links may point only to pages that already exist or pages created in the same phase.
6. Each synthesized page must have `## Source-backed details` with an evidence table:

```md
| Claim                    | Evidence                                                 | Locator          | Source                               |
| ------------------------ | -------------------------------------------------------- | ---------------- | ------------------------------------ |
| Concrete reusable claim. | "Short exact excerpt copied from the normalized source." | `normalized:L12` | [Source title](../sources/<slug>.md) |
```

7. Evidence cells must be short exact excerpts from the normalized source, not paraphrases.
8. Locator cells must use `normalized:L12` or `normalized:L12-L14`, and the evidence excerpt must appear inside that cited line range.
9. When a page is grounded in a bounded source section, add `source_ranges` frontmatter:

```yaml
source_ranges:
  - <source-slug>:normalized:L12-L34
```

10. Range-gated Phase 2 validation requires every evidence locator on the selected page to stay inside declared `source_ranges` or a normalized-source heading range derived from the page title.
11. Claim cells must synthesize the evidence in the page's own words; do not copy the evidence sentence into the claim cell.
12. Synthesized pages must not contain empty headings, duplicate headings, or `## Executable implementation` unless a real implementation file is linked.
13. Replace candidate rows in the source page with real Markdown links only for pages created in this phase.
14. Use the canonical `Related pages` row format:

```md
| Page title | [../concepts/example.md](../concepts/example.md) | Source-native group name | must create | concrete evidence basis | created |
| Page title | `../concepts/example.md` | Source-native group name | should create | concrete evidence basis | not created yet |
```

15. Prefer doing that replacement with `pnpm wiki:link-related <slug>`.
16. Do not update `wiki/index.md` or `wiki/log.md` in this phase unless explicitly asked.
17. Validate synthesized pages:

```bash
pnpm wiki:link-related <slug>
pnpm wiki:fix-links <slug>
pnpm wiki:normalize-ascii <slug>
pnpm wiki:check-synthesis <slug>
pnpm wiki:grounding:check
```

### Phase 3: navigation, graph, and log

1. Before adopting a Phase 2 benchmark worktree, generate a curator review packet:

```bash
pnpm wiki:review-phase2 <slug> <worktree>
```

2. The human curator chooses one action from the packet:
   - adopt the worktree
   - revise with another targeted Phase 2 prompt
   - defer the synthesized pages
   - record a contradiction and pause

3. Prefer the deterministic finalizer after adoption:

```bash
pnpm wiki:phase3 <slug>
```

4. If doing the steps manually, update `wiki/index.md`.
5. Run `pnpm wiki:graph`.
6. Append one `ingest` entry to `wiki/log.md`.
7. Run `pnpm wiki:lint` and address FAILs.

### Phase 4: executable concepts

If the source implies an executable concept:

1. Add or update TypeScript code and tests.
2. Link the wiki concept page to the implementation and tests.
3. Before finishing any code change, run:
   - `pnpm code:typecheck`
   - `pnpm code:test`

---

## Idempotency rules

Each phase has explicit rerun behavior to support safe resumption and debugging.

| Phase               | Rerun Behavior  | Rule                                                                                        |
| ------------------- | --------------- | ------------------------------------------------------------------------------------------- |
| Phase 0 import      | **Fail**        | Never overwrite `raw/imported/<slug>/`; use a new slug or `--reuse-imported` if bytes match |
| Phase 0 normalize   | **Conditional** | Overwrite only if original hash matches (`--reuse-imported --overwrite-normalized`)         |
| Phase 1a extract    | **Resume**      | Skip completed chunks; `--force` redoes all                                                 |
| Phase 1b dedupe     | **Overwrite**   | Always regenerate from claims-raw.jsonl                                                     |
| Phase 1c candidates | **Overwrite**   | Always regenerate from claims-normalized.json                                               |
| Phase 2a source     | **Overwrite**   | Regenerate from current extraction state                                                    |
| Phase 2b synthesize | **Worktree**    | Always write to disposable worktree first                                                   |
| Phase 2c adopt      | **Conditional** | Copy only if validation passes                                                              |
| Phase 3a index      | **Rebuild**     | Deterministic rebuild from `wiki/**/*.md` frontmatter                                       |
| Phase 3b graph      | **Rebuild**     | Deterministic rebuild from `wiki/**/*.md` links                                             |
| Phase 3c lint       | **Rebuild**     | Deterministic rebuild from `wiki/**/*.md` validation                                        |
| Phase 3d log        | **Append**      | Append-only, never overwrite                                                                |

**Key invariants**:

- `raw/imported/` is immutable after first write.
- `wiki/log.md` is append-only.
- All other generated files can be rebuilt from source of truth.
- Interrupted ingests can be resumed via manifest status.

---

## Ingest quality bar

A non-trivial source should usually create or update several pages.

A good PDF ingest should usually touch:

1. one source page
2. several concept/entity/procedure/reference pages
3. `wiki/index.md`
4. `wiki/_graph.json`
5. `wiki/log.md`

If only one page seems useful, explain why in `wiki/log.md`.

A source page alone is not enough unless the source is tiny.

---

## Execution discipline for local models

Local models may stall or drift if given a large task.

The source of truth for the atomic local-model ingest and audit loop is
`DESIGN_atomic-local-ingest.md`.

Use bounded phases:

1. Create source page only.
2. Extract concept/entity/procedure/reference candidates.
3. Create or update synthesized pages.
4. Update index.
5. Update graph.
6. Append log entry.
7. Run checks if code changed.

If the model stalls, narrow the task to one file or one phase.

Do not keep planning forever. Write files.

Prompts to local models should include:

- exact files allowed to change
- exact files forbidden to change
- the validation command to run
- a requirement to fix and rerun validation if it fails

Prefer deterministic checks over long prose reminders:

```bash
pnpm wiki:check-source <slug>
pnpm wiki:check-synthesis <slug>
pnpm wiki:ingest raw/inbox/<file> --slug <slug>
pnpm wiki:verify-ingest <slug>
pnpm wiki:deep-extract <slug> --extract-only
pnpm wiki:extraction-state <slug>
pnpm wiki:merge-candidates <slug>
pnpm wiki:phase1-benchmark <slug>
pnpm wiki:phase2-benchmark <slug>
pnpm wiki:phase2-single <slug> <candidate-path> --report .tmp/phase2-run.md
pnpm wiki:phase2-failures <slug>
pnpm wiki:phase2-clean-failures <slug> --older-than 30
pnpm wiki:review-phase2 <slug> <worktree>
pnpm wiki:adopt-phase2 <slug> <worktree>
pnpm wiki:phase3 <slug>
pnpm wiki:add-locators <slug> --normalized-source <path>
pnpm wiki:structure-proposal
pnpm wiki:index
pnpm wiki:index:check
pnpm wiki:graph
pnpm wiki:graph:check
pnpm wiki:grounding
pnpm wiki:grounding:check
pnpm wiki:judge-claims <page> --normalized-source <path> --candidate local-4090
pnpm wiki:claim-hints <page> --normalized-source <path>
pnpm wiki:repair-reference <page> --normalized-source <path>
pnpm wiki:query "question" --plan-only
pnpm wiki:check-analysis <page>
pnpm wiki:judge-analysis <page> --candidate local-4090 --fail-on-issues
pnpm wiki:model-benchmark --candidate local-4090 --dry-run
pnpm wiki:fix-links <slug>
pnpm wiki:normalize-ascii <slug>
pnpm wiki:normalize-tables <slug>
pnpm wiki:link-related <slug>
pnpm wiki:lint
pnpm wiki:semantic-lint
pnpm wiki:contradictions
pnpm wiki:maintenance --append-log
pnpm wiki:maintenance:systemd --dry-run
pnpm wiki:executables
pnpm wiki:curator-status --list
```

For a full local ingest from inbox through Phase 3, prefer the orchestrator:

```bash
pnpm wiki:ingest raw/inbox/<file.pdf> --slug <slug>
```

The unified ingest flow:

1. Phase 0: Normalizes the source (PDF to markdown)
2. Phase 1: Deep extracts claims from all chunks (100% coverage)
3. Phase 2a: Creates source page from extracted topics
4. Phase 2b: Synthesizes each topic page with quality gates (validate + judge + repair)
5. Phase 3: Updates index, graph, and log

Key options:

- `--max-phase2-pages N` — limit synthesized pages (default: 10)
- `--min-claims-per-topic N` — minimum claims to create a page (default: 3)
- `--chunk-size N` — lines per chunk (default: 400)
- `--skip-extract` — skip extraction, use existing state
- `--dry-run` — show what would happen

Use `--dry-run` first for unfamiliar sources.

For extraction only (no synthesis), use:

```bash
pnpm wiki:deep-extract <slug> --extract-only
```

For token-aware structural chunking (better for technical PDFs), use:

```bash
pnpm wiki:deep-extract <slug> --structured --target-tokens 6500
```

Structured chunking extracts blocks (headings, code, tables, lists) and packs them into
token-bounded chunks that preserve document structure. Use `--dry-run --structured` to
compare with line-based chunking.

For local-model Phase 1 prompt trials, prefer the mechanical prompt template in
`tools/prompts/phase1-source-repair.md`. To compare candidates in disposable worktrees, run:

```bash
pnpm wiki:phase1-benchmark <slug> --candidate local-4090
```

For local-model Phase 2 synthesis trials, prefer `pnpm wiki:phase2-single`. It auto-selects
`tools/prompts/phase2-reference-synthesis.md` for selected `wiki/references/**` pages and
`tools/prompts/phase2-synthesis.md` for other page types. To compare candidates in disposable
worktrees, run:

```bash
pnpm wiki:phase2-single <slug> ../concepts/example.md --candidate local-4090
```

Add `--report <path>` to `wiki:phase2-single` or `wiki:phase2-benchmark` when comparing local models
or preserving a disposable-worktree result for later review.

`wiki:phase2-single --judge-batch` may use a faster one-call local judge first. If that judge fails because
the local model does not return parseable JSON, the runner falls back to row-wise judging automatically.

For query trials, first inspect the deterministic context selection:

```bash
pnpm wiki:query "What should I know about this topic?" --plan-only
```

If the selected pages look right, run with `--candidate local-4090`. Add `--save-analysis` only for
answers that should become durable wiki knowledge.

To test the saved-analysis filing path without invoking a local model, run:

```bash
pnpm wiki:query:smoke
```

Saved analyses may use `normalized:L12` or `<source-slug>:normalized:L12` evidence locators. If multiple
source pages are cited, prefix normalized locators with the source slug. Do not use wiki-page `#L12`
anchors as evidence citations.

If a Phase 2 benchmark worktree is good enough to adopt, copy it into the real repo with:

```bash
pnpm wiki:review-phase2 <slug> <worktree>
pnpm wiki:adopt-phase2 <slug> <worktree> --normalized-source raw/normalized/<slug>/source.md
```

If a local model ignores failed validation, stop the run and narrow the next prompt to the first failing check.

---

## Query workflow

1. Read `wiki/index.md` first.
2. Use `wiki/_graph.json` if present.
3. Prefer existing wiki pages over re-reading raw sources.
4. Read only the pages needed.
5. Answer from the wiki, with links to pages used.
6. If the answer is durable, save it to `wiki/analyses/YYYY-MM-DD-<slug>.md`.
7. Add links between the new analysis and related concept/entity/procedure/reference pages.
8. Update `wiki/index.md` and `wiki/_graph.json` if a new analysis page is created.
9. Append a query entry to `wiki/log.md`.

---

## Lint workflow

Run lint when asked, after major ingests, or before cleanup commits.

Use the deterministic linter first:

```bash
pnpm wiki:lint
```

Check:

- pages listed in `wiki/index.md` but missing on disk
- pages existing on disk but missing from `wiki/index.md`
- pages missing frontmatter
- source pages missing required sections
- broken Markdown links
- orphan pages
- duplicate pages covering the same concept
- semantic overlap between synthesized pages
- possible cross-source contradictions
- source pages without related synthesized pages
- claims marked `not covered in sources`
- unresolved contradictions in `wiki/log.md`
- stale `last_updated` dates
- `_graph.json` nodes pointing to missing files
- wiki files missing from `_graph.json`

Write the result to:

```text
wiki/_linter-report.md
```

Append a lint entry to:

```text
wiki/log.md
```

The linter writes `wiki/_linter-report.md`. If you are performing an actual lint operation rather than
a quick local check, append the log entry after reviewing the report. For scheduled linting, run:

```bash
pnpm wiki:lint:log
```

Lint `TODO` items are intentional backlog, not wiki-health failures. For example, uncreated Related-pages
candidate paths should stay as TODO until a Phase 2 run creates and links those pages.

For scheduled maintenance, prefer `pnpm wiki:maintenance --append-log`. It runs index, graph, analysis,
grounding, lint, semantic overlap, contradiction, executable-concept, curator-status, and smoke checks,
then writes `wiki/_maintenance-report.md`. To install a user-level systemd timer, inspect:

```bash
pnpm wiki:maintenance:systemd --dry-run
```

Suggested log format:

```md
## [YYYY-MM-DD] lint | <summary>

- PASS:
- WARN:
- FAIL:
- TODO:

---
```

---

## Log format

`wiki/log.md` is append-only.

Prefer appending formatted entries with:

```bash
pnpm wiki:log <operation> "<short summary>" -d "<detail>"
```

Use this format:

```md
## [YYYY-MM-DD] <operation> | <short summary>

- Key detail 1
- Key detail 2
- Gaps or TODOs

---
```

Allowed operation types:

- `scaffold`
- `ingest`
- `query`
- `lint`
- `cleanup`
- `proposal`
- `contradiction`
- `schema-change`
- `todo`

Keep entries grep-able with:

```bash
grep "^## \\[" wiki/log.md
```

---

## Contradictions

If two sources disagree on an important factual, quantitative, or procedural claim:

1. Do not silently pick one.
2. Add a `contradiction` entry to `wiki/log.md`.
3. Include:
   - Source A claim
   - Source B claim
   - links to source pages
   - best proposed resolution
   - whether human input is needed
4. If the contradiction is minor and can be resolved by qualification, update the wiki with the qualification.
5. If the contradiction changes meaning or behavior, stop and wait for human input.

---

## Writing rules

- Prefer small, specific pages.
- Prefer updating existing pages over creating duplicates.
- Use short paragraphs.
- Use tables for structured facts.
- Use bullets for claim lists.
- Keep pages heavily linked.
- Every concept page should link to its source pages.
- Every executable concept page should link to its TypeScript implementation and tests.
- Write uncertainty explicitly.
- Do not over-explain basics if the source is advanced.
- Do not under-explain gotchas.

---

## Grounding rules

Run the grounding check after source repair, synthesis, or cleanup work that changes wiki content:

```bash
pnpm wiki:grounding
```

Source pages should keep key claims close to the normalized source vocabulary. Synthesized pages must include
at least one source page in frontmatter `sources` and link to at least one source page in the body.

`wiki/_grounding-report.md` records the latest grounding check. A lexical grounding pass is not proof of truth;
it is a guardrail for catching unsupported-looking claims before the wiki grows around them.

---

## Index rules

`wiki/index.md` is the content catalog.

Prefer generating `wiki/index.md` with:

```bash
pnpm wiki:index
```

Use this check before finishing index-related work:

```bash
pnpm wiki:index:check
```

Organize by type:

1. Sources
2. Entities
3. Concepts
4. Procedures
5. References
6. Analyses
7. Code

Each entry should include:

```md
- [Page title](relative/path.md) — one-line description
```

Update it on every ingest, query filing, lint cleanup, or page rename by running `pnpm wiki:index`.

Never let it go stale.

---

## Code rules

If a source implies an executable concept:

1. Add or update TypeScript in `packages/concepts/src/`.
2. Add or update tests in `packages/concepts/tests/`.
3. Link the wiki concept page to the implementation and tests.
4. Run:
   - `pnpm code:typecheck`
   - `pnpm code:test`

Use explicit `.js` extensions in TypeScript imports when using `moduleResolution: NodeNext`.

---

## Safety rails

- Never edit `raw/imported/`.
- Never delete a wiki page unless it is clearly duplicated and the replacement is linked.
- Never leave code changes untested if tests exist.
- Never invent facts.
- Never bury contradictions.
- Never create a new top-level directory without a logged proposal.
- Never commit raw PDFs, normalized markdown dumps, or extracted images unless the human explicitly changes the repo policy.

---

## When to stop

Stop and write a `proposal` or `contradiction` entry in `wiki/log.md` when:

- a source contradicts an existing source
- a new top-level directory seems necessary
- an ingest would require changing `AGENTS.md`
- a file appears corrupted or unreadable
- the model cannot identify useful synthesized pages from a source
- `raw/imported/` would need to be changed
- code tests fail and the fix is not obvious
- the source appears out of scope for the current wiki

---

## Success looks like

- `wiki/index.md` is enough to navigate the knowledge base.
- Each source page links to synthesized pages.
- Reusable answers are filed back into `wiki/analyses/`.
- `wiki/_graph.json` gives the agent a machine-readable map.
- `wiki/_linter-report.md` explains wiki health.
- `wiki/log.md` tells the full history of ingests, queries, lint passes, proposals, contradictions, and schema changes.
- The wiki gets more useful after every source and every serious question.
