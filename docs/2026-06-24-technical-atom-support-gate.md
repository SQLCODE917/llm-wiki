# Technical Atom Support Gate

## Context & Problem

Glossary:

| Term | Meaning |
|---|---|
| `TechnicalAtom` | One preserved bounded technical item from a source. |
| `TechnicalAtomCatalog` | Rebuildable source-scoped collection of `TechnicalAtom` records. |
| `TechnicalAtomEvidenceScope` | Evidence context that can support one `TechnicalAtom`. |
| `TechnicalAtomSupportGate` | Domain service that checks `TechnicalAtom` records against evidence. |
| `TechnicalAtomSupportFinding` | Deterministic finding for one `TechnicalAtom` support problem. |
| `TechnicalDetailsSection` | Source page section that renders supported `TechnicalAtom` records. |
| `RelatedTechnicalAtomSurface` | Render-ready reference to a supported atom from another page. |
| `SourceRange` | Planned source span for one source page. |
| `EvidenceRegistry` | Rebuildable collection of source evidence records. |
| `IngestConfidenceReport` | Harness-owned report that summarizes source validation. |
| `WikiPage` | One generated markdown page in `wiki/`. |

The wiki now preserves exact technical details as `TechnicalAtom` records.
The wiki also renders related atoms on ordinary source pages.
Some atoms can cite an evidence window that does not support the exact payload.
Citation validation also treats related atom citations as page-local citations.

## Goals

- Classify each `TechnicalAtom` support status before page rendering.
- Prevent unsupported exact details from rendering as authoritative facts.
- Validate related atom citations against the atom source range.
- Report atom support failures in `ingest-confidence`.
- Improve confidence for JavaScript code and game rules without source-specific code.

## Non-Goals & Forbidden Approaches

Non-goals:

- This design does not increase the number of extracted atoms.
- This design does not add a second query workflow.
- This design does not add a new page kind.
- This design does not repair generated wiki pages by hand.

Forbidden approaches:

- Do not branch on source file names, source titles, or known book names.
- Do not add Sword World rules as hardcoded knowledge.
- Do not add JavaScript Allonge examples as hardcoded knowledge.
- Do not suppress source-range findings globally.
- Do not treat a rendered page as evidence for its own atom.
- Do not render `not_supported` atoms in `TechnicalDetailsSection`.
- Do not render `not_supported` atoms as `RelatedTechnicalAtomSurface`.
- Do not edit files under `raw/`.

## Requirements

- The harness must run `TechnicalAtomSupportGate` after it builds or reuses a catalog.
- The gate must build one `TechnicalAtomEvidenceScope` for each atom.
- The scope must include the atom evidence ids and source range id.
- The scope must include evidence excerpts from `EvidenceRegistry`.
- The scope must include source text from the atom source range.
- The gate must set one existing support status on each atom.
- The gate must emit `TechnicalAtomSupportFinding` records for support problems.
- The gate must mark an atom `supported` only when evidence supports its payload.
- The gate must mark an atom `not_supported` when evidence contradicts or misses its payload.
- The gate must mark an atom `too_broad` when the payload contains extra unsupported material.
- The gate must mark an atom `unclear` when deterministic checks cannot decide.
- The gate must validate code atoms against one contiguous code span.
- The gate must validate formula atoms against formula terms and operators.
- The gate must validate procedure atoms against ordered source steps.
- The gate must validate table-row atoms against recoverable cells.
- The gate must validate requirement, exception, and worked-example atoms against source text.
- Page rendering must include only `supported` atoms in `TechnicalDetailsSection`.
- Related atom selection must consider only `supported` atoms.
- Source-range checks must use the atom source range for rendered atom citations.
- Ordinary citations must keep the current page-local source-range check.
- `ingest-confidence` must report atom counts by support status.
- `claim-support` must sample only `supported` technical atom candidates.

## Invariants

- `raw/` remains immutable.
- `TechnicalAtomCatalog` remains rebuildable from ingest artifacts.
- `EvidenceRegistry` remains the evidence authority for atom support.
- `TechnicalAtom` ids remain stable when payload and evidence ids stay stable.
- `query` remains the only user-facing question workflow.
- Related atoms remain normal page content after rendering.

## Proposed Architecture

```
+-------------------+      +-----------------------+
| TechnicalAtom     |----->| TechnicalAtom         |
| Catalog           |      | Support Gate          |
+---------+---------+      +-----------+-----------+
          |                            |
          |                            v
          |                 +-----------------------+
          |                 | TechnicalAtom         |
          |                 | Support Finding       |
          |                 +-----------+-----------+
          |                             |
          v                             v
+-------------------+      +-----------------------+
| Page Renderer     |      | ingest-confidence     |
+---------+---------+      +-----------+-----------+
          |
          v
+-------------------+
| query workflow    |
+-------------------+
```

The `TechnicalAtomSupportGate` checks atom payloads against evidence.
The `TechnicalAtomEvidenceScope` supplies evidence text for one atom.
The `TechnicalAtomSupportFinding` records one support problem.
The page renderer renders supported atoms.
The confidence workflow reports support findings.
The query workflow reads rendered sections as ordinary wiki content.

## Key Interactions

Support gate:

```
TechnicalAtomCatalog + EvidenceRegistry
-> TechnicalAtomSupportGate
-> TechnicalAtomCatalog + TechnicalAtomSupportFinding records
```

Page render:

```
TechnicalAtomCatalog with support status
-> page renderer
-> WikiPage with supported TechnicalDetailsSection
```

Related citation audit:

```
Rendered atom citation
-> atom lookup by technical_atom_id
-> source-range check against atom source_range_id
```

## Data Model

| Object | Required fields |
|---|---|
| `TechnicalAtomEvidenceScope` | `technical_atom_id`, `source_locator`, `source_range_id`, `evidence_ids`, `evidence_texts`, `source_range_text` |
| `TechnicalAtomSupportFinding` | `finding_id`, `technical_atom_id`, `page_id`, `source_range_id`, `severity`, `category`, `message`, `evidence_id` |

`TechnicalAtom.support_status` remains the atom support status field.
Support status values remain `supported`, `too_broad`, `not_supported`, and `unclear`.
Finding category values are `missing-evidence`, `source-range`, `payload-not-found`, `payload-too-broad`, and `boundary-unclear`.
Finding severity values are `warning` and `blocker`.

## APIs / Interfaces

- `technical-atoms.json` stores the post-gate `TechnicalAtomCatalog`.
- `ingest-confidence` runs the support gate before it renders atom counts.
- `ingest-confidence --fresh` rebuilds the catalog and reruns the support gate.
- Source page rendering accepts a post-gate `TechnicalAtomCatalog`.
- `claim-support` reads support status before it builds technical atom candidates.
- Source-range checking accepts `TechnicalAtomCatalog` records for atom citations.
- `query` has no new mode or new user-facing command.

## Behavior & Domain Rules

Rule: the support gate treats evidence ids as the first authority.

Example: an atom references an evidence id from its own source range.
Expected outcome: the gate checks that evidence text before source-range text.

Example: an atom references an evidence id from a different source range.
Expected outcome: the gate emits a `source-range` blocker.

Rule: the support gate requires kind-specific payload support.

Example: a code atom payload appears in one fenced source code block.
Expected outcome: the gate marks the atom `supported`.

Example: a code atom payload includes prose before the code span.
Expected outcome: the gate marks the atom `too_broad`.

Example: a formula atom says `attack power = skill level + dexterity bonus`.
Expected outcome: source text must contain the formula terms and operator.

Rule: renderers expose only supported technical details.

Example: one page has one supported formula and one `unclear` formula.
Expected outcome: the page renders only the supported formula.

Example: a related atom has `not_supported` status.
Expected outcome: related atom selection excludes that atom.

Rule: source-range checks distinguish page citations from atom citations.

Example: a source page cites text from its planned range.
Expected outcome: citation validation keeps the current pass result.

Example: a page renders a related atom from another page.
Expected outcome: citation validation checks the atom source range.

Ugliest edge case: a rendered related atom has a valid citation but a missing atom id.
Expected outcome: citation validation emits a warning for the rendered citation.

## Acceptance Criteria

Milestone 1: domain model.

- `docs/domain-vocabulary.md` records `TechnicalAtomEvidenceScope`, `TechnicalAtomSupportGate`, and `TechnicalAtomSupportFinding`.
- Tests prove each scope contains only records for the atom evidence ids.
- Tests prove each scope keeps the atom source range id.
- Tests prove foreign evidence ids produce a `source-range` blocker.
- Tests prove missing evidence ids produce a `missing-evidence` blocker.

Milestone 2: support rules.

- Tests prove exact fenced code becomes `supported`.
- Tests prove code plus prose becomes `too_broad`.
- Tests prove a supported formula keeps `supported` status.
- Tests prove a formula missing from evidence becomes `not_supported`.
- Tests prove procedure steps must appear in source order.
- Tests prove table-row cells must appear in the evidence scope.
- Tests prove requirement and exception atoms need source support.

Milestone 3: render and sample filters.

- Tests prove `TechnicalDetailsSection` renders only `supported` atoms.
- Tests prove `RelatedTechnicalAtomSurface` selects only `supported` atoms.
- Tests prove `claim-support` samples only `supported` technical atoms.
- Tests prove support counts appear in `ingest-confidence`.
- Tests prove support findings appear in `ingest-confidence`.

Milestone 4: source-range audit.

- Tests prove ordinary citations keep page-local source-range checks.
- Tests prove owned atom citations validate against atom source range.
- Tests prove related atom citations validate against atom source range.
- Tests prove related atom citations do not create page-local range warnings.
- Tests prove a rendered atom without a catalog match reports a warning.

Milestone 5: smoke tests.

- Run Antikythera ingest confidence first.
- Run JavaScript Allonge ingest confidence after Antikythera passes.
- Run Sword World ingest confidence after JavaScript Allonge passes.
- Ask one JavaScript Allonge query that requires exact code.
- Ask one Sword World query that requires exact game rules.
- Fix each failed smoke-test finding and rerun the failed command.

Milestone 6: standard verification.

- Technical atom tests pass.
- Claim support tests pass.
- Ingest confidence tests pass.
- `uv run ruff check harness/src harness/tests` passes.
- `uv run mypy harness/src` passes.

## Cross-Cutting Concerns

Observability: confidence reports must show support status counts and support findings.

Error handling: unsupported atoms must create findings during confidence runs.

Copyright: the gate must not expand rendered exact payloads beyond current atom bounds.

Performance: artifact reuse must keep support-gated catalogs reusable by fingerprint.

## Reference Implementations

- Technical atoms: `harness/src/llmwiki/domain/technical_atoms.py`.
- Atom builder: `harness/src/llmwiki/domain/technical_atom_builder.py`.
- Related atom surfacing: `harness/src/llmwiki/domain/technical_atom_surfaces.py`.
- Evidence registry: `harness/src/llmwiki/domain/evidence_registry.py`.
- Source-range checks: `harness/src/llmwiki/domain/evidence_locators.py`.
- Claim support: `harness/src/llmwiki/domain/claim_support_selection.py`.
- Confidence gates: `harness/src/llmwiki/runtime/ingest_confidence_gate_checks.py`.

## Alternatives Considered

- Chosen: gate atoms before rendering, because unsupported details should not enter pages.
- Rejected: global source-range suppression, because it hides real citation mistakes.
- Rejected: source-specific configs, because current failures have universal causes.
- Rejected: larger claim samples only, because sampling cannot repair bad atoms.
- Rejected: LLM-only atom judging, because deterministic checks must run first.

## Halt Conditions

- If implementation needs source-specific rules, stop and ask.
- If implementation needs a second query workflow, stop and ask.
- If implementation needs a new page kind, stop and ask.
- If implementation needs to edit `raw/`, stop and ask.
- If deterministic checks cannot classify a kind, mark the atom `unclear`.
