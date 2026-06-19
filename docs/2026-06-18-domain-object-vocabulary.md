# M5-Wiki Adoption Deliverables

## Context & Problem

Glossary:

| Term | Meaning |
|---|---|
| `our wiki` | This repository. |
| `m5-wiki` | The repository at `~/gits/llm-wiki-m5-24gb`. |
| `shared harness` | Domain and workflow code that both repos can port with runtime-only changes. |
| `generated state` | `wiki/`, `index.md`, `log.md`, and disposable ingest cache. |
| `adoption TDD` | One independently shippable TDD listed by this document. |
| `DomainTerm` | Exact name of one domain concept. |
| `runtime profile` | Machine-specific model setup outside shared domain code. |

Our wiki now treats generated state as disposable test data. The old domain
object vocabulary TDD was too small for the new goal. This document splits
adoption of m5-wiki's strongest domain and ingest features into separate TDDs.
The split keeps each deliverable small while guiding both repos toward a shared
harness.

## Goals

- Replace the vocabulary-only TDD with an implementation split.
- Adopt m5-wiki domain object boundaries.
- Adopt m5-wiki domain language enforcement.
- Adopt m5-wiki global ingest planning.
- Adopt m5-wiki planned write and page body contracts.
- Adopt m5-wiki source summary coverage.
- Preserve our wiki evidence, audit, maintenance, graph, and runtime strengths.
- Keep code portable between our wiki and m5-wiki.

## Non-Goals & Forbidden Approaches

Non-goals:

- This document does not implement code changes.
- This document does not define a permanent wiki schema.
- This document does not preserve generated state.
- This document does not design m5 hardware setup.

Forbidden approaches:

- Do not combine all adoption work into one large TDD.
- Do not keep compatibility branches for old generated state.
- Do not use our current flat schema as a permanent constraint.
- Do not fork shared domain code for the 4090 runtime.
- Do not fork shared domain code for the M5 runtime.

## Requirements

- Each adoption TDD must stay under 300 lines.
- Each adoption TDD must use m5-wiki names when a matching concept exists.
- Each adoption TDD must list m5-wiki reference files.
- Each adoption TDD must preserve `raw/` immutability.
- Each adoption TDD must treat generated state as disposable.
- Each adoption TDD must isolate runtime-specific behavior outside domain code.
- Each adoption TDD must define acceptance criteria that can become tests.
- Each adoption TDD must name portability checks for our wiki and m5-wiki.

## Invariants

- `raw/` remains immutable.
- `SCHEMA.md` remains a wiki configuration input until a later TDD replaces it.
- `wiki/` remains generated knowledge.
- `index.md` remains deterministic navigation.
- `log.md` remains operation history.
- Runtime profiles remain outside shared domain code.
- m5-wiki remains the reference for adopted domain names.

## Proposed Architecture

The adoption program creates five shippable TDDs. Each TDD moves one boundary
toward the shared harness.

```
+-------------------+     +------------------+
| m5-wiki reference |---->| adoption TDDs    |
+-------------------+     +--------+---------+
                                  |
                                  v
+-------------------+     +--------+---------+
| our wiki audits   |<----| shared harness   |
+-------------------+     +------------------+
```

`m5-wiki reference` supplies proven domain names and boundary shapes.
`adoption TDDs` define shippable implementation slices.
`shared harness` is the target code surface for both repos.
`our wiki audits` supply evidence, graph, maintenance, and runtime features.

## Key Interactions

### Adopt A Deliverable

```
adoption TDD -> shared harness: constrains one boundary
tests -> shared harness: enforce contract
generated state -> rebuild: verify outcome
```

### Share Code Back

```
Shared harness -> our wiki: run with 4090 profile
Shared harness -> m5-wiki: run with M5 profile
Tests -> both repos: enforce same domain names
```

## Data Model

| Deliverable | TDD |
|---|---|
| Object boundaries | `docs/2026-06-19-shared-object-boundaries.md` |
| Domain language | `docs/2026-06-19-domain-language-consistency.md` |
| Global planning | `docs/2026-06-19-global-ingest-planning.md` |
| Planned writes | `docs/2026-06-19-planned-write-page-body-contracts.md` |
| Source coverage | `docs/2026-06-19-source-summary-coverage.md` |

Adoption order:

- Implement object boundaries first.
- Implement domain language second.
- Implement global planning third.
- Implement planned writes and page body contracts fourth.
- Implement source summary coverage fifth.

Portability targets:

- Shared domain files use the same class names as m5-wiki.
- Shared tests use the same assertion shape as m5-wiki.
- Runtime adapters translate only model startup and client construction.
- Our wiki audit modules consume shared domain objects.

## APIs / Interfaces

`harness/src/llmwiki/domain/` is the shared domain interface.

`harness/src/llmwiki/workflows/tools.py` is the model tool interface.

`harness/src/llmwiki/store/wiki_store.py` is the file boundary.

`harness/tests/test_domain_language_consistency.py` is the static portability
test interface.

## Behavior & Domain Rules

Rule: an adoption TDD owns one shippable boundary.

Example: input `PageMetadata` refactor -> expected object-boundaries TDD owns
the change.

Example: input `PageBodyContract` validation -> expected planned-write TDD owns
the change.

Rule: generated state never blocks a clean contract.

Example: input generated frontmatter uses `category` -> expected implementation
rebuilds generated state with `page_kind`.

Ugliest edge case: input old page parses only through a compatibility branch ->
expected implementation deletes generated state and removes the branch.

## Acceptance Criteria

- This document lists all five adoption TDDs.
- Each listed TDD exists.
- Each listed TDD is under 300 lines.
- Each listed TDD names m5-wiki references.
- Each listed TDD includes portability acceptance criteria.
- No listed TDD requires legacy generated-state support.

## Cross-Cutting Concerns

Observability: adoption work must keep transcripts, run artifacts, and reports
available after generated state rebuilds.

Error handling: domain errors must use shared `DomainTerm` names so both repos
can reuse tool retry behavior.

Runtime: domain code must not import 4090, Ollama, M5, or llama-server setup.

## Reference Implementations

- m5 object boundaries: `~/gits/llm-wiki-m5-24gb/harness/src/llmwiki/domain/pages.py`.
- m5 domain objects: `~/gits/llm-wiki-m5-24gb/harness/src/llmwiki/domain/objects.py`.
- m5 planning: `~/gits/llm-wiki-m5-24gb/harness/src/llmwiki/domain/planning.py`.
- m5 body contracts: `~/gits/llm-wiki-m5-24gb/harness/src/llmwiki/domain/page_body_contracts.py`.
- our evidence gates: `harness/src/llmwiki/domain/evidence.py`.
- our maintenance: `harness/src/llmwiki/domain/maintenance.py`.

## Alternatives Considered

- Chosen: five adoption TDDs, because each boundary can ship alone.
- Rejected: one large convergence TDD, because it exceeds the sizing gate.
- Rejected: vocabulary-only adoption, because tests must enforce code language.
- Rejected: compatibility-first adoption, because generated state is disposable.

## Halt Conditions

- If one adoption TDD exceeds 300 lines, stop and split it.
- If a change needs runtime-specific domain code, stop and split the runtime adapter.
- If a change preserves old generated state, stop and remove the compatibility path.
- If m5-wiki and our wiki need different domain class names, stop and choose one shared name.
