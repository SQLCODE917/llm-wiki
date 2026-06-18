# Ingest Route Plans

## Context & Problem

Ingest profiles and descriptive naming guards reduced bad page names, but the
model still chooses page destinations at the same moment it writes page prose.
That leaves page structure to improvisation and creates generic pages, duplicate
targets, weak catalog entries, broken imagined links, and orphans. This feature
adds an ingest route plan contract before any page write, so the harness can
validate the ingest route plan and authorize only planned page writes.

This serves `docs/llm-wiki.md` by improving the compiled wiki layer without
mutating raw sources: ingest still updates durable wiki pages, but page targets
become checked bookkeeping instead of hidden prompt behavior.

## Goals

- Require an ingest route plan before any page write.
- Require the harness to validate the ingest route plan before any page write.
- Use the validated ingest route plan as the allowlist for page writes in the current run.
- Make ingest route plan decisions auditable to the model during the run and to the curator through manifest/status output after the run.
- Add a small domain-object layer for the ingest route plan: `RawSource`,
  `SourceBundle`, `PageMetadata`, `WikiStructure.local_flat`, and `IngestRun`.
- Keep the ingest route plan contract planner-agnostic so later global planning,
  embedding routing, or ML-assisted routing can emit the same plan shape.

## Non-Goals & Forbidden Approaches

Non-goals:

- No full global PDF planner in this TDD.
- No true ML, embedding, clustering, or normalized claim extraction pipeline.
- No folder routing, nested wiki paths, or separate wiki roots.
- No human approval UI before synthesis.
- No automatic semantic merge of existing pages.
- No migration of existing wiki pages.

Forbidden approaches:

- Do not make the `plan_pages` tool the permanent center of the architecture.
- Do not hard-code Sword World, JavaScript, or any source-specific terms.
- Do not infer page identity, category, or source meaning from a file path.
- Do not let prompts create page categories outside `SCHEMA.md`.
- Do not allow unplanned page writes.
- Do not create placeholder pages for route gaps.
- Do not treat planning artifacts as source evidence.

## Requirements

- Every ingest workflow that can perform a page write must record a valid
  `IngestRoutePlan` first.
- The ingest route plan applies only to the current source ingest or PDF chunk
  map run.
- The first plan producer is the model-facing `plan_pages` tool.
- Future plan producers must be able to emit the same `IngestRoutePlan` without changing `write_page` enforcement.
- Every planned page has `PageMetadata`, action, role, source scope,
  confidence, and rationale.
- `PageMetadata.page_id` is the stable page identity.
- `PageMetadata.page_kind` is one of `source`, `entity`, `concept`, or
  `synthesis`.
- `WikiStructure.local_flat` renders every page path as `{page_id}.md`.
- Validation rejects plans whose `source_path`, `scope`, `chunk_id`, or
  `profile_ids` do not match the active ingest context.
- Validation rejects duplicate planned page IDs.
- Validation rejects planned page IDs that are not valid kebab-case wiki slugs.
- Validation rejects planned page kinds outside `SCHEMA.md` categories.
- Validation rejects planned actions other than `create` or `enrich`.
- Validation rejects `create` for an existing page and `enrich` for a missing page.
- Validation rejects new planned pages that violate active namespace and
  singular/plural naming rules.
- Validation rejects planned pages with empty summary, role, source scope,
  confidence, or rationale.
- Validation rejects route gaps with unsupported reasons or empty source scope.
- `write_page` rejects page IDs not present in the active ingest route plan.
- `write_page` rejects category mismatches against the planned `page_kind`.
- Existing-page writes require a planned `enrich` action and still require
  `read_page` first.
- New-page writes require a planned `create` action and still pass namespace,
  naming, singular/plural, and evidence gates.
- Route gaps are accepted ingest route plan outcomes and are persisted for
  health/status.
- PDF chunk manifests record ingest route plan stats and route gap summaries for
  completed chunks.

## Invariants

- `raw/` remains immutable.
- The model performs page writes only through `write_page`.
- `index.md`, `log.md`, graph export, hub key lists, and candidate backlog remain
  harness-owned.
- The wiki remains flat `wiki/*.md` with `[[page-name]]` links.
- Planning artifacts are bookkeeping, not wiki evidence and not citations.
- Failed validation prevents page writes rather than repairing after the fact.
- Page identity is `PageMetadata.page_id`, not the rendered path.
- `WikiStructure.local_flat` is the only active path projection in this TDD.

## Proposed Architecture

```
+----------------+      +---------------+      +-------------------+
| ingest context |----->| plan producer |----->| ingest route plan |
+----------------+      +---------------+      +---------+---------+
                                |                       |
                                v                       v
                         +--------------+        +--------------+
                         | domain layer |<------>| validator    |
                         +--------------+        +------+-------+
                                                         |
                                                         v
                                                  +--------------+
                                                  | write guard  |
                                                  +------+-------+
                                                         |
                                                         v
                                                  +--------------+
                                                  | wiki store   |
                                                  +--------------+
```

`ingest context` provides the source, scope, schema, and profile guidance.
`plan producer` creates an `IngestRoutePlan`; the initial plan producer is
`plan_pages`, and later plan producers may be global or embedding-assisted.
`domain layer` defines source, page metadata, wiki structure, and run objects.
`validator` enforces schema, namespace, category, action, and gap rules.
`write guard` blocks page writes that are not authorized by the active ingest route plan.
`wiki store` continues to own markdown writes, index updates, and log appends.

## Key Interactions

PDF chunk:

```
Session -> Plan producer: source/chunk context + profile guidance
Plan producer -> Validator: IngestRoutePlan
Validator -> Session: validated ingest route plan
Session -> Model: write only planned targets
Model -> write_page: planned page body
write guard -> WikiStore: authorized page write
Session -> Manifest: ingest route plan stats, route gaps, page writes
```

Unplanned page attempt:

```
Model -> write_page: unplanned page
write guard -> Model: corrective tool error
Model -> plan_pages: revised ingest route plan or route gap
Validator -> Session: validated ingest route plan
Model -> write_page: planned page
```

Route gap:

```
Plan producer -> Validator: route gap for weak or ambiguous material
Validator -> Session: validated route gap
Model -> write_page: no page for that gap
curator-status -> Curator: recent route gap count and examples
```

## Data Model

| Object | Contract |
|---|---|
| `page write` | One `write_page` call that creates or replaces one wiki page. |
| `ingest route plan` | The validated page write allowlist for one ingest run. |
| `plan producer` | The component that emits an `IngestRoutePlan`; the first plan producer is `plan_pages`. |
| `write guard` | The `write_page` enforcement layer that rejects page writes outside the active ingest route plan. |
| `route gap` | A planned non-write for source material that should not become a wiki page in the current run. |
| `RawSource` | One immutable source from `raw/`, with `source_path` and `source_format`. |
| `SourceBundle` | One or more `RawSource` values selected for a single ingest run. |
| `PageMetadata` | Stable page identity and queryable metadata: `page_id`, `page_kind`, `summary`, `sources`, `updated`. |
| `WikiStructure.local_flat` | Active path projection for this TDD: `structure_id = local-flat`, path template `{page_id}.md`. |
| `IngestRun` | One operation record with `SourceBundle`, active `WikiStructure`, profile context, ingest route plan summary, and page writes. |
| `IngestRoutePlan` | Run-scoped page write allowlist: `version`, `source_path`, `scope`, optional `chunk_id`, profile IDs in effect, `planned_pages`, and `gaps`. |
| `PlannedPage` | One authorized page target: `metadata`, `role`, `action`, `source_scope`, `confidence`, and `rationale`. |
| `RouteGap` | One planned non-write: `reason`, `source_scope`, and `summary`. Reasons are `too-granular`, `weak-evidence`, `ambiguous-existing-page`, `out-of-profile-scope`, or `needs-curator-review`. |

## APIs / Interfaces

- `plan_pages`: forge tool available only in ingest workflows when planning is
  ready to route a source or chunk; emits `IngestRoutePlan`.
- `write_page`: existing tool gains a write guard for ingest workflows.
- `WikiStore`: continues to persist rendered `WikiPage` objects; path projection
  uses `WikiStructure.local_flat`.
- PDF manifest: records per-chunk ingest route plan stats and route gap
  summaries.
- `curator-status`: reports latest ingest route plan stats and recent route
  gaps.

## Behavior & Domain Rules

An ingest route plan authorizes page targets, not content quality. Evidence
gates, read-before-rewrite, naming, and citation checks still apply after an
ingest route plan is validated.

A planned `create` page may be skipped if the model later decides the content is
better represented as a route gap. It may not be replaced by an unplanned page
write.

A route gap is not a failure. It is the correct outcome for weak,
over-granular, ambiguous, or out-of-scope material.

Examples:

- Input: a programming-book chunk discusses closures and lexical scope, and the
  wiki already has `closures`. Expected: plan enriches `closures` or creates a
  namespaced source-section page with rationale; an unplanned generic `scope`
  page is rejected.
- Input: a product catalog row briefly names one product without durable
  specifications. Expected: either a planned `catalog-entry` page with evidence
  scope and rationale, or a `too-granular` gap; no placeholder product page.
- Input: a rulebook chunk mentions two different things with similar names.
  Expected: plan creates/enriches separate precise targets or records
  `ambiguous-existing-page`; a bare ambiguous page name is rejected.

## Acceptance Criteria

Milestone 1: Domain objects and ingest route plan validation

- Tests prove `RawSource`, `SourceBundle`, `PageMetadata`,
  `WikiStructure.local_flat`, and `IngestRun` cover existing flat wiki behavior.
- Tests prove `WikiStructure.local_flat` renders `{page_id}.md` for all current
  page kinds.
- Tests prove valid ingest route plans are accepted and invalid categories are
  rejected.
- Tests prove mismatched ingest context fields are rejected.
- Tests prove duplicate page IDs and invalid slugs are rejected.
- Tests prove invalid actions and create/enrich existence mismatches are
  rejected.
- Tests prove source-namespace requirements apply to planned page IDs.
- Tests prove incomplete planned pages and invalid route gaps are rejected.
- Tests prove valid route gaps are accepted outcomes and are not pages.

Milestone 2: Workflow enforcement

- Tests prove ingest requires an ingest route plan before `write_page`.
- Tests prove unplanned page writes fail with a corrective tool error.
- Tests prove planned category/action mismatches fail.
- Tests prove existing-page `enrich` still requires `read_page`.
- Tests prove future non-tool plan producers can pass an `IngestRoutePlan` into
  the same validator/write-guard path.

Milestone 3: Observability and live validation

- PDF chunk manifests include ingest route plan stats and route gap summaries.
- `curator-status` reports latest ingest route plan stats and recent route gaps.
- README and `SCHEMA.md` document ingest route plans as page write allowlists.
- Live validation on a small profiled pilot chunk shows planned pages, accepted
  gaps, and no unplanned page writes.
- `uv run ruff check harness/src harness/tests`, `uv run mypy harness/src`, and
  relevant tests pass.

## Cross-Cutting Concerns

Observability: ingest route plan stats and route gaps are deterministic
bookkeeping. They must be concise and must not include long source excerpts.

Error handling: validation errors are corrective tool errors. Invalid plans
block writes in the current run without changing wiki files.

Security and provenance: ingest route plans are not source evidence. Wiki claims
still require raw-source citations and pass the existing evidence policy.

Future compatibility: planner intelligence is outside this contract. Global,
embedding, or ML-assisted planners must produce `IngestRoutePlan` and reuse the
same validation and page write allowlist path.

## Reference Implementations

- Profile loading: `harness/src/llmwiki/domain/ingest_profiles.py`.
- Write guards: `harness/src/llmwiki/workflows/tools.py`.
- Page/frontmatter model: `harness/src/llmwiki/domain/pages.py`.
- PDF manifests: `harness/src/llmwiki/pdf/manifest.py`.
- Curator status: `harness/src/llmwiki/domain/maintenance.py`.
- Naming policy: `harness/src/llmwiki/domain/naming.py`.
- Page-map navigation: `harness/src/llmwiki/workflows/fixed_page_tools.py`.

## Alternatives Considered

- Chosen: planner-agnostic ingest route plans because they prevent bad page
  writes and can survive later global planning.
- Chunk-local `plan_pages` only: rejected because it would churn when a global
  planner arrives.
- Prompt-only planning: rejected because prompt-only naming guidance already
  allowed duplicate and dangling pages.
- Full global planner now: deferred because ingest needs a stable authorization
  contract first.
- Folder classifier: rejected because the M5 wiki's canonical structure is flat.
- Automatic source classifier: deferred; profile selection remains curator-led.

## Halt Conditions

- If implementation requires moving pages into folders, stop and split a folder
  structure TDD.
- If implementation requires normalized claim extraction, stop and split a claim
  pipeline TDD.
- If implementation requires embedding, ML, or global PDF planning, stop and
  split a planner TDD.
