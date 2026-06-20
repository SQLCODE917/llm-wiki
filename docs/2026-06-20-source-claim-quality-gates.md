# Source Claim Quality Gates

## Context & Problem

Glossary:

| Term | Meaning |
|---|---|
| `ExtractedUnit` | Source-derived text unit with locator, heading path, and status. |
| `SourceClaim` | Atomic statement extracted from one `ExtractedUnit`. |
| `SourceClaimClassifier` | Domain service that classifies one `SourceClaim`. |
| `ClaimEligibility` | Selection category for one `SourceClaim`. |
| `ClaimRoleTag` | `Schema` label that describes the function of a `SourceClaim`. |
| `ClaimCentrality` | Score that compares a claim with an `ExtractedUnit.heading_path`. |
| `ClaimSalience` | Score that ranks one `SourceClaim` inside planning. |
| `SourceSummaryPlan` | Selected `SourceClaim` coverage for one source page. |
| `SourceSummaryDraft` | Model proposal before source `PageBody` rendering. |
| `SourceSummaryDraftValidator` | Domain service that validates `SourceSummaryDraft`. |
| `SourceSummaryRenderer` | Domain service that renders accepted `SourceSummaryDraft` into `PageBody`. |
| `SourceSummaryQualityReport` | Deterministic report for selected claims and generated pages. |
| `RawSource` | Immutable source file under `raw/`. |
| `Evidence` | Citation-backed support for a generated claim. |
| `PageBody` | Markdown body of one `WikiPage`. |
| `PageBodyFinding` | Domain finding returned by body validation. |
| `PageMetadata` | Page identity, summary, sources, and update date. |
| `PagePath` | Rendered location of one `WikiPage` inside `wiki/`. |
| `WikiStructure` | Domain object that renders `PagePath` from `PageMetadata`. |
| `IngestTopology` | Allowed write order for one ingest run. |
| `m5-wiki` | Sibling repo at `~/gits/llm-wiki-m5-24gb`. |

Our source-summary contract validates draft coverage after `SourceSummaryPlan` selects claims.
The selected claims still include source furniture, code fragments, narrative frame, or source-framing prose.
m5-wiki adds claim eligibility, role tags, centrality, and deterministic quality reports before source summaries.
This TDD adopts that quality gate without adding a model call.

## Goals

- Add `ClaimEligibility` to `SourceClaim`.
- Add `ClaimCentrality` to `SourceClaim`.
- Split source uncertainty from ordinary modal language.
- Prefer eligible central claims in `SourceSummaryPlan`.
- Reject source-framing source-summary bullets.
- Add deterministic quality experiments without model calls.
- Keep claim-quality code portable to m5-wiki.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not change PDF extraction.
- This TDD does not change `DocumentModel`.
- This TDD does not create a universal claim ontology.
- This TDD does not add a model call before `SourceSummaryPlan`.
- This TDD does not require perfect generated prose.

Forbidden approaches:

- Do not tune rules only for JavaScript Allonge.
- Do not select an ineligible claim when an eligible claim exists in the same `ExtractedUnit`.
- Do not require a draft to invent uncertainty.
- Do not write `SourceClaim` identifiers into `PageBody`.
- Do not make `WikiStructure` depend on claim quality.

## Requirements

- `SourceClaimClassifier` must assign `ClaimEligibility` to every `SourceClaim`.
- `SourceClaimClassifier` must assign `ClaimRoleTag` values before `ClaimSalience`.
- `SourceClaimClassifier` must assign `ClaimCentrality` before `ClaimSalience`.
- `ClaimEligibility` must use `eligible`, `analogy`, `rhetorical-example`, `narrative-frame`, `source-furniture`, `code-fragment`, or `source-framing`.
- `SourceSummaryPlan` must select eligible claims before ineligible claims.
- `SourceSummaryPlan` must select zero ineligible claims when an `ExtractedUnit` has one eligible claim.
- `SourceSummaryPlan` must select one eligible claim per `ExtractedUnit` when a source page has five or fewer units.
- `ClaimRoleTag` defaults must include `source-uncertainty`.
- `ClaimRoleTag` defaults must include `ordinary-modality`.
- `SourceSummaryPlan` must use `source-uncertainty` as uncertainty coverage.
- `SourceSummaryPlan` must exclude `ordinary-modality` from uncertainty coverage.
- `ClaimSalience` must include `ClaimCentrality`.
- `ClaimSalience` must penalize every ineligible `ClaimEligibility` value.
- `SourceSummaryDraftValidator` must reject claim bullets that start with source-framing prefixes.
- `SourceSummaryDraftValidator` must reject drafts that omit selected eligible claim coverage.
- `SourceSummaryQualityReport` must read cached `PagePlan` and generated wiki pages.
- `SourceSummaryQualityReport` must not call the model.

## Invariants

- `raw/` remains immutable.
- `Evidence` remains required for generated claims.
- `IngestTopology` remains `serial`.
- `PageMetadata.page_id` remains page identity.
- `WikiStructure` remains the only `PagePath` renderer.
- `PageBody` contains no internal planning identifiers.
- `SourceSummaryPlan` remains a planning object.

## Proposed Architecture

`SourceClaimClassifier` sits between source claim creation and source summary planning.
`SourceSummaryPlan` selects eligible central claims.
`SourceSummaryDraftValidator` checks coverage and source-framing prose.
`SourceSummaryQualityReport` checks cached plans and generated pages.

```
+---------------+     +-------------+     +-----------------------+
| ExtractedUnit |---->| SourceClaim |---->| SourceClaimClassifier |
+---------------+     +-------------+     +-----------+-----------+
                                                        |
                                                        v
                                               +-------------------+
                                               | SourceSummaryPlan |
                                               +---------+---------+
                                                         |
                                                         v
                                               +-------------------+
                                               | SourceSummaryDraft|
                                               +---------+---------+
                                                         |
                                                         v
                                               +-------------------+
                                               | PageBody          |
                                               +-------------------+
```

## Key Interactions

Claim classification:

```
ExtractedUnit -> SourceClaim -> SourceClaimClassifier
SourceClaimClassifier -> ClaimEligibility
SourceClaimClassifier -> ClaimRoleTag
SourceClaimClassifier -> ClaimCentrality
SourceClaimClassifier -> ClaimSalience
```

Source summary write:

```
SourceSummaryPlan -> SourceSummaryDraft
SourceSummaryDraft -> SourceSummaryDraftValidator
SourceSummaryDraftValidator -> SourceSummaryRenderer -> PageBody
```

Quality report:

```
PagePlan cache -> SourceSummaryQualityReport
wiki pages -> SourceSummaryQualityReport
```

## Data Model

| Object | Required fields |
|---|---|
| `SourceClaim` | Existing fields plus `claim_eligibility` and `claim_centrality` |
| `ClaimEligibility` | one allowed eligibility value |
| `ClaimCentrality` | numeric score from zero through one |
| `SourceSummaryQualityReport` | `selected_ineligible_claims`, `false_source_uncertainty_claims`, `source_framing_bullets`, `missing_unit_coverage` |

Default `ClaimRoleTag` values added by this TDD:

- `source-uncertainty`
- `ordinary-modality`
- `analogy`
- `worked-example`
- `source-framing`

## APIs / Interfaces

- `PagePlan` exposes `SourceClaim.claim_eligibility`.
- `PagePlan` exposes `SourceClaim.claim_centrality`.
- `SourceSummaryPlan.selected_source_claims` includes only selected claim identifiers.
- `validate_source_summary_draft` rejects source-framing claim bullets.
- `source_summary_quality_report` returns `SourceSummaryQualityReport`.

## Behavior & Domain Rules

Rule: `ClaimEligibility` controls default source-summary selection.

Example: input unit has one analogy claim and one eligible Object.assign claim.
Expected outcome: `SourceSummaryPlan` selects the Object.assign claim.

Example: input unit has one code fragment and one eligible map claim.
Expected outcome: `SourceSummaryPlan` selects the map claim.

Ugliest edge case: input unit has only one central code fragment.
Expected outcome: `SourceSummaryPlan` selects the code fragment and reports the fallback.

Rule: source uncertainty differs from ordinary modal language.

Example: input says a caller possibly passes a function to map.
Expected outcome: `ClaimRoleTag` includes `ordinary-modality`.

Example: input says the source does not specify resource closing.
Expected outcome: `ClaimRoleTag` includes `source-uncertainty`.

Rule: source furniture does not displace subject claims.

Example: input page has one image caption and four eligible technical claims.
Expected outcome: `SourceSummaryPlan` selects no image caption claim.

Example: input page has copyright text and no eligible subject claims.
Expected outcome: `SourceSummaryQualityReport` records ineligible fallback if selected.

Rule: source-framing bullets fail validation.

Example: input bullet starts with `The source discusses`.
Expected outcome: `SourceSummaryDraftValidator` returns `PageBodyFinding`.

Example: input bullet starts with the subject term.
Expected outcome: `SourceSummaryDraftValidator` accepts the bullet wording.

## Acceptance Criteria

Milestone 1: classifier tests.

- Tests cover every `ClaimEligibility` value.
- Tests cover `source-uncertainty` and `ordinary-modality`.
- Tests prove classifier accuracy reaches 90 percent on labeled fixtures.
- Fixtures include JavaScript Allonge examples.
- Fixtures include Antikythera examples.
- Fixtures include Sword World rulebook examples.

Milestone 2: planner tests.

- Tests prove eligible claims beat analogy claims.
- Tests prove eligible claims beat code fragments.
- Tests prove eligible claims beat source furniture.
- Tests prove central claims beat noncentral filler.
- Tests prove source pages with five or fewer units cover one eligible claim per unit.

Milestone 3: validator and report tests.

- Tests prove source-framing bullets fail validation.
- Tests prove selected eligible claim omission fails validation.
- Tests prove `SourceSummaryQualityReport` counts selected ineligible claims.
- Tests prove `SourceSummaryQualityReport` counts false source uncertainty.
- Tests prove `SourceSummaryQualityReport` counts source-framing bullets.
- `uv run pytest harness/tests/test_source_claim_quality.py harness/tests/test_source_summary_coverage.py` passes.

## Cross-Cutting Concerns

Observability: the cache must retain enough `PagePlan` data to rebuild `SourceSummaryQualityReport`.

Error handling: the write loop must return `PageBodyFinding` records for draft failures.

Portability: classifier objects and field names must match m5-wiki unless a later TDD changes both repos.

## Reference Implementations

- m5 TDD: `~/gits/llm-wiki-m5-24gb/docs/2026-06-19-source-claim-quality.md`.
- m5 classifier code: `~/gits/llm-wiki-m5-24gb/harness/src/llmwiki/domain/planning.py`.
- m5 tests: `~/gits/llm-wiki-m5-24gb/harness/tests/test_source_claim_quality.py`.
- our source claims: `harness/src/llmwiki/domain/source_claims.py`.
- our draft validation: `harness/src/llmwiki/domain/page_body_validation.py`.

## Alternatives Considered

- Chosen: deterministic classifier, because source-summary selection needs repeatable gates.
- Rejected: prompt-only instruction, because generated pages still contain source-framing bullets.
- Rejected: source-specific rules, because RPG books and technical books must both pass.
- Rejected: forced uncertainty bullet, because many sources state no uncertainty.

## Halt Conditions

- If classifier rules mention one book title as logic, stop and move the case into fixtures.
- If generated pages expose `SourceClaim` identifiers, stop and fix rendering.
- If quality reporting needs a model call, stop and redesign the report.
- If m5-wiki names differ, stop and reconcile shared object names.
