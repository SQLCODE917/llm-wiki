# Domain Object Vocabulary

## Context & Problem

The harness has useful domain objects, but future features still introduce
important LLM-Wiki concepts as loosely shaped payloads, ad hoc dictionaries, or
near-synonym terms. That makes TDDs, prompts, tests, reports, and code drift away
from shared LLM-Wiki meaning. This TDD establishes a canonical domain object
vocabulary so future feature work names first-level domain objects and
second-level domain objects before crossing code, tool, persistence, or report
boundaries.

This serves `docs/llm-wiki.md` by making the pattern's raw source layer, wiki
layer, schema layer, and operations explicit in code and design language. Raw
sources remain immutable, the wiki remains the compiled knowledge layer, and the
harness gains stable names for the bookkeeping that lets knowledge compound.

Classification reflects current architectural role, not eternal ontology. A term may move between deferred, second-level, and first-level status in a later TDD if its lifecycle changes.
Domain objects validate context-free local invariants. Domain services validate rules that require context, stores, profiles, schema documents, or multiple domain objects.
Canonical code owner means the module where the term's domain object or primary domain rules are defined. Boundary adapters, persistence models, and reports may use the term but do not own it.
Boundary DTOs and persistence models must map into domain objects before domain rules run. Pure transport, logging, or pass-through rendering may remain DTO-shaped when no domain rule is applied.

## Goals

- Create one canonical domain object vocabulary for LLM-Wiki concepts.
- Define the difference between a first-level domain object, second-level
  domain object, boundary DTO, persistence model, and view model.
- Require future TDDs to reuse existing domain terms or define new domain terms.
- Classify existing high-value LLM-Wiki concepts into first-level domain objects
  and second-level domain objects.
- Make the adoption rule incremental: new features and touched code use domain
  objects, while unrelated working code is not churned.
- Give implementers finite checks for terminology drift and object-boundary
  drift.

## Non-Goals & Forbidden Approaches

Non-goals:

- No mass refactor of the whole harness in this TDD.
- No renaming every existing class, function, file, test, or markdown heading.
- No new runtime workflow behavior.
- No schema migration for existing wiki pages.
- No generated ORM, universal base class, or reflection registry.
- No replacement for Pydantic tool parameters, CLI args, JSON payloads, or forge
  tool schemas.

Forbidden approaches:

- Do not convert every dictionary or dataclass into a domain object.
- Do not treat boundary DTOs as domain objects.
- Do not let transport or persistence field names define domain terms.
- Do not introduce near-synonyms for established domain terms.
- Do not move side effects into domain objects.
- Do not make one generic `Record`, `Item`, `Entity`, `Node`, or `Object`
  abstraction stand in for specific LLM-Wiki meaning.
- Do not refactor unrelated code only to satisfy vocabulary aesthetics.

## Requirements

- `docs/domain-vocabulary.md` must define all domain terms introduced by this TDD.
- `docs/domain-vocabulary.md` must classify each listed term as exactly one of:
  first-level domain object, second-level domain object, boundary DTO,
  persistence model, or view model.
- `docs/domain-vocabulary.md` must identify the canonical code owner for each
  existing first-level domain object and second-level domain object.
  Canonical code owner means the module where the domain object or its primary domain rules are defined.
  Persistence and boundary adapters may reference it but do not own the term.
- `docs/domain-vocabulary.md` must identify deferred domain objects.
- `docs/writing-tdds.md` must reference `docs/domain-vocabulary.md` from
  Terminology Discipline.
- Future TDDs must reuse a domain term from `docs/domain-vocabulary.md` or define
  the new domain term in their Data Model section.
- Future TDDs must classify every new cross-boundary shape.
- Domain objects must live in `harness/src/llmwiki/domain/` unless a later TDD
  defines a more specific domain package boundary.
- Boundary DTOs and persistence models must map explicitly into domain objects before domain rules run.
- Pure transport, logging, or pass-through display may remain DTO-shaped if no domain rule is applied.
- View models must be derived from domain objects or deterministic findings.
- Domain objects must validate their own local invariants at construction time.
- Domain objects validate context-free local invariants. Domain services validate context-dependent rules.
- Orchestrators must own side effects and arrange domain services.
- Tests for new behavior must use domain terms in test names and assertions.

## Invariants

- `raw/` remains immutable.
- The wiki remains the compiled knowledge layer written through harness tools.
- `SCHEMA.md`, `index.md`, and `log.md` keep their current ownership boundaries.
- Existing successful workflows must keep working during incremental adoption.
- The domain object vocabulary does not make planning artifacts source evidence.
- The domain object vocabulary does not create new wiki page categories.
- The domain object vocabulary does not force folder routing or nested wiki paths.
- The canonical term for a `write_page` call that creates or replaces one wiki
  page remains `page write`.

## Proposed Architecture

```
+--------------------+       +--------------------------+
| feature TDD        |------>| domain object vocabulary |
+--------------------+       +------------+-------------+
                                           |
                                           v
                              +------------+-------------+
                              | domain layer             |
                              +------------+-------------+
                                           |
              +----------------------------+----------------------------+
              v                                                         v
 +------------+-------------+                             +-------------+------------+
 | boundary adapters        |                             | reports and prompts      |
 +------------+-------------+                             +-------------+------------+
```

`feature TDD` introduces or reuses domain terms before implementation.

`domain object vocabulary` is the canonical glossary and classification table.

`domain layer` contains first-level domain objects, second-level domain objects,
and domain services.

`boundary adapters` map boundary DTOs and persistence models into domain objects.

`reports and prompts` render domain objects and view models with canonical terms.

## Key Interactions

### New Feature Defines a Domain Term

```
Engineer -> domain object vocabulary: check existing domain term
Engineer -> feature TDD: reuse domain term or define new domain term
Reviewer -> feature TDD: verify term classification
Implementer -> domain layer: add or reuse domain object
```

### Boundary DTO Enters a Workflow

```
Model -> boundary DTO: tool payload
Boundary adapter -> domain object: explicit mapping
Domain object -> domain object: local invariant validation
Workflow -> store: side effect after domain validation
```

### Persistence Model Feeds a Report

```
Store -> persistence model: read stored artifact
Boundary adapter -> domain object: explicit mapping
Domain service -> view model: compute report state
Report -> view model: render canonical terms
```

## Data Model

`domain object vocabulary` is the canonical set of named LLM-Wiki concepts and
their classifications.

`first-level domain object` is a durable LLM-Wiki noun that can anchor a
feature, workflow, or lifecycle.

Initial first-level domain objects marked `Exists`: `RawSource`, `SourceBundle`,
`WikiPage`, `WikiStructure`, `IngestRun`, `WikiGraph`, `CandidateBacklog`.

Initial first-level domain objects marked `Existing concept`: `ChatSession`,
`PdfIngestManifest`.

Initial first-level domain objects marked `Deferred`: `SchemaDocument`,
`QueryRun`, `LintRun`, `MaintenanceRun`.

`second-level domain object` is a meaningful part of a first-level domain object
or domain service.

Initial second-level domain objects marked `Exists`: `PageMetadata`,
`IngestRoutePlan`, `PlannedPage`, `RouteGap`, `GroundingVerdict`,
`ContradictionFinding`, `CandidateRecord`.

Initial second-level domain objects marked `Existing concept`: `Citation`,
`EvidenceLocator`, `SourceExcerpt`, `LintFinding`, `SalienceSignal`.

Initial second-level domain objects marked `Deferred`: `PageLink`, `PageWrite`.

`boundary DTO` is an inbound or outbound transport shape, such as CLI args,
Pydantic tool parameters, or forge tool payloads.

`persistence model` is an on-disk storage shape, such as JSON, JSONL, SQLite row,
or PDF manifest data.

`view model` is a rendered or render-ready shape for curator status, reports,
prompts, transcripts, or CLI output.

## APIs / Interfaces

`docs/domain-vocabulary.md` is the public design interface for domain terms. It
must contain these headings: `Canonical Terms`, `Domain Object Inventory`,
`Boundary Shape Inventory`, and `Adoption Rules`.

`docs/writing-tdds.md` must instruct TDD authors to consult
`docs/domain-vocabulary.md` before defining new domain terms.

`harness/src/llmwiki/domain/` remains the code interface for domain objects and
domain services.

`harness/tests/` remains the verification interface for domain object invariants,
boundary DTO mapping, persistence model mapping, and view model rendering.

## Behavior & Domain Rules

Every cross-boundary shape has one classification.

Example: `PlanPagesParams` is a boundary DTO, `IngestRoutePlan` is a domain
object, and `IngestRoutePlanRecord` is a persistence model. The boundary DTO does
not enforce page write rules; the domain object and domain service do.

Every domain rule uses the canonical domain term.

Example: a test name says `test_page_write_requires_ingest_route_plan`; it does
not say `test_wiki_write_requires_route`, because the canonical term is `page
write`.

Every new domain object has local invariants.

Example: `PageMetadata` rejects an invalid page ID or page kind at construction
time. A boundary DTO may accept raw text temporarily, but it must map into
`PageMetadata` before page identity rules run.

Ugliest edge case: a stored JSON record uses `page_kind`, a tool payload uses
`category`, and a report says `page type`. Expected outcome: the boundary adapter
maps both payload fields into the canonical domain term `page_kind`, and the
report renders the canonical term or a documented human-facing label.

## Acceptance Criteria

Milestone 1: Canonical vocabulary

- `docs/domain-vocabulary.md` exists and contains all required headings.
- `docs/domain-vocabulary.md` defines first-level domain object, second-level
  domain object, boundary DTO, persistence model, and view model.
- `docs/domain-vocabulary.md` classifies every term listed in this TDD.
- `docs/writing-tdds.md` references `docs/domain-vocabulary.md` in Terminology
  Discipline.

Milestone 2: Existing object audit

- Every existing term marked `Exists` has a canonical code owner listed in
  `docs/domain-vocabulary.md`.
- Every existing term marked `Existing concept` has its current module or report
  surface listed.
- Every term marked `Deferred` has a trigger for when code should be introduced.

Milestone 3: Adoption rules

- `docs/domain-vocabulary.md` states that new features must reuse a domain term
  or define a new domain term before implementation.
- `docs/domain-vocabulary.md` states that boundary DTOs, persistence models, and
  view models must map explicitly to domain objects before domain rules run.
- At least one representative test checks that a boundary DTO maps into a domain
  object before a domain rule runs.
- A test proving a domain object rejects a local invariant violation, e.g. invalid PageMetadata.page_id.
- A test proving a boundary DTO can contain raw/transport names but maps into canonical domain names before validation.
- A doc/lint-ish test proving docs/domain-vocabulary.md contains required headings and classifications.

## Cross-Cutting Concerns

Observability: curator-facing reports should render canonical domain terms where
they expose harness bookkeeping. Human-facing labels may differ only when the
domain vocabulary records the label.

Error handling: validation errors raised by domain objects and domain services
must use canonical domain terms because forge feeds tool errors back to the
model.

Migration: adoption is incremental. A feature that touches an area must align
that area's domain terms, but unrelated modules stay unchanged.

## Reference Implementations

- Domain object validation: `harness/src/llmwiki/domain/pages.py`.
- Ingest route plan domain rules: `harness/src/llmwiki/domain/ingest_route_plan.py`.
- Boundary DTO mapping: `harness/src/llmwiki/workflows/ingest_route_tools.py`.
- Persistence model mapping: `harness/src/llmwiki/domain/ingest_route_history.py`.
- Curator view model rendering: `harness/src/llmwiki/domain/maintenance.py`.
- Existing TDD terminology discipline: `docs/2026-06-16-ingest-page-plans.md`.

## Alternatives Considered

- Chosen: canonical vocabulary plus incremental adoption, because it guides
  future work without destabilizing working flows.
- Rejected: mass refactor, because it is not independently shippable and creates
  unrelated churn.
- Rejected: generated type registry, because LLM-Wiki meaning is semantic, not
  reflection metadata.
- Rejected: documentation-only glossary with no code ownership, because it would
  not constrain future implementation.

## Halt Conditions

- If implementation requires renaming more than one existing workflow operation,
  stop and ask before proceeding.
- If implementation changes wiki page schema or page categories, stop and ask
  before proceeding.
- If implementation changes raw source layout, stop and ask before proceeding.
- If implementation would make boundary DTOs import domain services directly,
  stop and ask before proceeding.
- If the domain object inventory exceeds this TDD's listed terms, stop and split
  the new terms into a follow-up TDD.
