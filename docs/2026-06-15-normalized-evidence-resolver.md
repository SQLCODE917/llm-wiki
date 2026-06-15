# Normalized Evidence Resolver

## Context & Problem

Current strict evidence mode validates citation syntax, locator syntax, and raw
source existence. The backup had stronger evidence tooling: stable evidence IDs,
normalized source locators, and excerpt-location checks. Bringing that idea into
M5 would make important wiki claims more auditable without restoring the old
directory schema.

Pattern excerpts addressed from `docs/llm-wiki.md`:

- "Raw sources ... are immutable"
- "This is your source of truth"
- "The wiki ... summaries, entity pages, concept pages"
- "synthesizes an answer with citations"

## Goals

- Resolve `raw/... normalized:Lx-Ly` citations to exact source text.
- Validate that quoted or tabled evidence appears at the cited normalized
  locator.
- Keep strict evidence optional via `off|warn|fail`.
- Avoid changing ordinary lightweight citations into mandatory evidence IDs.

## Non-Goals & Forbidden Approaches

Non-goals:

- No return to `raw/imported` / `raw/normalized` directory schema.
- No mandatory evidence IDs for every claim.
- No LLM judge in this TDD.
- No citation rewriting by default.

Forbidden approaches:

- Do not parse evidence with ad hoc line-number string slicing in workflows.
- Do not require normalized locators on all existing pages.
- Do not copy backup packages wholesale.

## Requirements

- A normalized locator attached to a raw citation is resolved against a
  line-addressable source representation.
- Missing source, invalid locator, out-of-range locator, and evidence-not-found
  are distinct findings.
- Artifact-tolerant matching may warn, but fabricated evidence fails in `fail`
  mode.
- The resolver works for current raw Markdown and cached PDF chunk/source text
  where available.

## Invariants

- `raw/` remains immutable.
- Source citation syntax remains compatible with `(raw/file.md)` and
  `(raw/book.pdf p.1-2)`.
- Existing pages without normalized locators remain valid unless strict mode is
  explicitly configured to require them later.

## Proposed Architecture

```
+-------------+       +-------------------+       +----------------+
| wiki page   |------>| citation parser   |------>| evidence policy|
+-------------+       +-------------------+       +----------------+
                                  |                         |
                                  v                         v
                           source resolver           lint/write gates
```

Citation parsing remains pure. A resolver supplies line-addressable source text.
Evidence policy combines parser and resolver findings for write/lint gates.

## Key Interactions

Write with valid locator:

```
Model -> write_page: body with raw/book.pdf normalized:L10-L12
Policy -> resolver: source lines
Policy -> write_page: pass
```

Write with fabricated quote:

```
Model -> write_page: quote plus normalized locator
Policy -> resolver: quote absent at locator and globally
Tool  -> Model: corrective evidence finding
```

Lint existing pages:

```
CLI -> lint: strict-evidence warn
Policy -> all pages: collect resolver findings
Report -> wiki-health: deterministic evidence section
```

## Data Model

- `ResolvedLocator`: source path, line range, text, confidence.
- `EvidenceFinding`: page name, source path, locator, severity, code, message.
- Optional stable evidence IDs may be parsed as aliases, but raw citations remain
  the primary contract.

## APIs / Interfaces

- Strict evidence modes remain `off`, `warn`, `fail`.
- Supported locator form: `raw/<path> normalized:L<start>-L<end>`.
- Finding codes include at least `missing-source`, `invalid-locator`,
  `locator-out-of-range`, and `evidence-not-found`.

## Behavior & Domain Rules

- Exact local match passes.
- Canonicalized local match passes or warns, depending on confidence.
- Global match outside the cited locator warns with a suggested locator.
- No match fails in `fail` mode.

Examples:

- Citation text appears exactly on lines 10-12 -> pass.
- Text appears on lines 15-17 instead -> warn with suggested locator.
- Text appears nowhere in source -> fail.

## Acceptance Criteria

- Tests cover exact, canonicalized-local, global, out-of-range, and not-found
  cases.
- `write_page` blocks fatal resolver findings in `fail` mode.
- `lint --strict-evidence warn` reports resolver findings without blocking.
- Existing `javascriptallonge` pages remain clean or produce documented warnings.
- No backup package paths are imported by active code.

## Cross-Cutting Concerns

Performance: resolver source text should be loaded once per policy run where
practical; correctness wins over caching complexity.

## Reference Implementations

- Current citation parser: `harness/src/llmwiki/domain/citations.py`.
- Current evidence policy: `harness/src/llmwiki/domain/evidence.py`.
- Backup resolver idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/packages/wiki_io/src/wiki_io/evidence/resolver.py`.
- Backup validator idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/packages/wiki_io/src/wiki_io/evidence/validator.py`.

## Alternatives Considered

- Stable evidence IDs everywhere - rejected for this TDD because direct raw
  citations are already the M5 contract.
- Model-only evidence judgment - rejected because locator/excerpt checks are
  deterministic.

## Halt Conditions

- If source text cannot be made line-addressable for PDFs without changing
  `raw/`, stop and design a cache contract before implementing.
