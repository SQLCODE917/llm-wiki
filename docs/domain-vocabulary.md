# Domain Vocabulary

This is the canonical vocabulary for LLM-Wiki domain objects and boundary
shapes. It gives future TDDs and implementations stable names for the harness
bookkeeping that keeps raw sources immutable and the wiki layer compiled,
interlinked, and maintained.

## Canonical Terms

| Term | Meaning |
|---|---|
| domain object vocabulary | This document's canonical glossary and classification inventory. |
| first-level domain object | Durable LLM-Wiki noun that can anchor a feature, workflow, or lifecycle. |
| second-level domain object | Meaningful part of a first-level domain object or domain service. |
| boundary DTO | Inbound or outbound transport shape, such as CLI args, Pydantic tool params, or forge payloads. |
| persistence model | On-disk or database storage shape, such as JSON, JSONL, SQLite rows, or PDF manifest data. |
| view model | Rendered or render-ready shape for reports, prompts, transcripts, or CLI output. |
| domain service | Pure domain operation that enforces rules requiring context or multiple domain objects. |
| orchestrator | Side-effecting coordinator that arranges tools, stores, model calls, and domain services. |
| page write | One `write_page` call that creates or replaces one wiki page through the harness. |
| local flat wiki structure | The current flat `wiki/*.md` projection, represented by `LOCAL_FLAT_STRUCTURE`. |

Transport, persistence, and report labels may be reader-facing, but domain rules
and model-facing ToolDTOs must use the canonical domain term and code name.

## DomainTerm And CodeName Table

| DomainTerm | CodeName |
|---|---|
| `PageId` | `page_id` |
| `PageKind` | `page_kind` |
| `PagePath` | `page_path` |
| `PageBody` | `page_body` |
| `PageBodyContract` | `page_body_contract` |
| `ResolvedPageBodyContract` | `resolved_page_body_contract` |
| `PageBodyFinding` | `page_body_finding` |
| `PageMetadata` | `page_metadata` |
| `DomainFrontmatter` | `domain_frontmatter` |
| `GeneratedWikiState` | `generated_wiki_state` |
| `SourceLocator` | `source_locator` |
| `SourceText` | `source_text` |
| `SourceRange` | `source_range` |
| `RawSource` | `raw_source` |
| `SourceBundle` | `source_bundle` |
| `Schema` | `schema` |
| `WikiStructure` | `wiki_structure` |
| `IngestRun` | `ingest_run` |
| `ExtractedUnit` | `extracted_unit` |
| `CandidateClaim` | `candidate_claim` |
| `CandidateTopic` | `candidate_topic` |
| `CandidateEntity` | `candidate_entity` |
| `TopicCluster` | `topic_cluster` |
| `WikiMatch` | `wiki_match` |
| `ClaimComparison` | `claim_comparison` |
| `PagePlan` | `page_plan` |
| `SourcePlan` | `source_plan` |
| `SourcePlanContractSelection` | `source_plan_contract_selection` |
| `ClaimRoleTag` | `claim_role_tag` |
| `SourceClaim` | `source_claim` |
| `SourceClaimGroup` | `source_claim_group` |
| `SourceSummaryPlan` | `source_summary_plan` |
| `SourceSummaryDraft` | `source_summary_draft` |
| `SourceSummaryBullet` | `source_summary_bullet` |
| `PlannedPageWrite` | `planned_page_write` |
| `Evidence` | `evidence` |
| `EvidenceLocator` | `evidence_locator` |
| `EvidenceIdentity` | `evidence_identity` |
| `EvidenceLocatorIndex` | `evidence_locator_index` |
| `EvidenceLocatorFinding` | `evidence_locator_finding` |
| `EvidenceLocatorBuilder` | `evidence_locator_builder` |
| `LocatorArtifactFingerprint` | `locator_artifact_fingerprint` |
| `LocatorStabilityGate` | `locator_stability_gate` |
| `EvidenceRecord` | `evidence_record` |
| `EvidenceRegistry` | `evidence_registry` |
| `EvidenceBank` | `evidence_bank` |
| `LocatorMatch` | `locator_match` |
| `TechnicalAtom` | `technical_atom` |
| `TechnicalAtomKind` | `technical_atom_kind` |
| `TechnicalAtomCatalog` | `technical_atom_catalog` |
| `TechnicalDetailsSection` | `technical_details_section` |
| `AnswerEvaluationCase` | `answer_evaluation_case` |
| `AnswerEvaluationReport` | `answer_evaluation_report` |
| `ClaimSupportCandidate` | `claim_support_candidate` |
| `ClaimSupportVerdict` | `claim_support_verdict` |
| `ClaimSupportFinding` | `claim_support_finding` |
| `ClaimSupportAuditReport` | `claim_support_audit_report` |
| `IngestConfidenceReport` | `ingest_confidence_report` |
| `IngestConfidenceGate` | `ingest_confidence_gate` |
| `ValidationFinding` | `validation_finding` |
| `ArtifactReuseDecision` | `artifact_reuse_decision` |
| `IndexEntry` | `index_entry` |
| `LogEntry` | `log_entry` |
| `LintRun` | `lint_run` |
| `LintFinding` | `lint_finding` |

## Domain Object Inventory

### First-Level Domain Objects

| Term | Status | Canonical owner or current surface |
|---|---|---|
| RawSource | Exists | `llmwiki.domain.objects` |
| SourceBundle | Exists | `llmwiki.domain.objects` |
| WikiPage | Exists | `llmwiki.domain.pages` |
| WikiStructure | Exists | `llmwiki.domain.pages`; local flat value is `LOCAL_FLAT_STRUCTURE` |
| IngestRun | Exists | `llmwiki.domain.objects` |
| PagePlan | Exists | `llmwiki.domain.objects`; built by `llmwiki.domain.planning` |
| WikiGraph | Exists | `llmwiki.domain.graph` |
| CandidateBacklog | Exists | `llmwiki.domain.candidates` |
| ChatSession | Existing concept | `llmwiki.store.chat_store` SQLite rows and `llmwiki.runtime.chat_repl` flows |
| PdfIngestManifest | Existing concept | `llmwiki.pdf.manifest.Manifest` |
| EvidenceRegistry | Exists | `llmwiki.domain.evidence_registry`; persisted beside `PagePlan` cache artifacts |
| SchemaDocument | Deferred | Introduce when schema parsing, versioning, or validation becomes a domain rule. |
| QueryRun | Deferred | Introduce when query lifecycle state needs domain validation beyond orchestration. |
| LintRun | Exists | `llmwiki.domain.objects` |
| MaintenanceRun | Deferred | Introduce when maintenance lifecycle state needs domain validation beyond report filing. |

### Second-Level Domain Objects

| Term | Status | Canonical owner or current surface |
|---|---|---|
| PageMetadata | Exists | `llmwiki.domain.pages` |
| IngestRoutePlan | Exists | `llmwiki.domain.ingest_route_plan` |
| PlannedPage | Exists | `llmwiki.domain.ingest_route_plan` |
| RouteGap | Exists | `llmwiki.domain.ingest_route_plan` |
| PageBodyContract | Exists | `llmwiki.domain.page_body_contracts`; owned by `Schema` |
| ResolvedPageBodyContract | Exists | `llmwiki.domain.page_body_contracts`; bound to one `PlannedPageWrite` |
| PageBodyFinding | Exists | `llmwiki.domain.page_body_contracts`; returned by body validation |
| SourcePlanContractSelection | Exists | `llmwiki.domain.page_body_contracts`; selected through `SourcePlan` |
| ClaimRoleTag | Exists | `llmwiki.domain.source_summary`; default vocabulary owned by `Schema` |
| SourceClaim | Exists | `llmwiki.domain.source_summary`; built by `llmwiki.domain.source_claims` |
| SourceClaimGroup | Exists | `llmwiki.domain.source_summary`; groups `SourceClaim` records for coverage planning |
| SourceSummaryPlan | Exists | `llmwiki.domain.source_summary`; bound to source `PlannedPageWrite` records |
| SourceSummaryDraft | Exists | `llmwiki.domain.source_summary`; planned source-summary tool input after DTO mapping |
| SourceSummaryBullet | Exists | `llmwiki.domain.source_summary`; covers one or more selected `SourceClaim` records |
| ExtractedUnit | Exists | `llmwiki.domain.objects` |
| CandidateClaim | Exists | `llmwiki.domain.objects` |
| CandidateTopic | Exists | `llmwiki.domain.objects` |
| CandidateEntity | Exists | `llmwiki.domain.objects` |
| TopicCluster | Exists | `llmwiki.domain.objects` |
| WikiMatch | Exists | `llmwiki.domain.objects` |
| ClaimComparison | Exists | `llmwiki.domain.objects` |
| PlannedPageWrite | Exists | `llmwiki.domain.objects` |
| Evidence | Exists | `llmwiki.domain.objects`; citation evidence policy remains separate |
| SourceText | Exists | `llmwiki.domain.evidence_registry`; line-addressable generated source text |
| SourceRange | Exists | `llmwiki.domain.evidence_registry`; page-scoped source span |
| EvidenceRecord | Exists | `llmwiki.domain.evidence_registry`; stable generated evidence excerpt record |
| EvidenceBank | Exists | `llmwiki.domain.evidence_registry`; bounded snippets derived from evidence records |
| LocatorMatch | Exists | `llmwiki.domain.evidence_locators`; deterministic locator check result |
| ClaimSupportCandidate | Exists | `llmwiki.domain.claim_support`; selected generated claim with source/evidence links |
| ClaimSupportVerdict | Exists | `llmwiki.domain.claim_support`; fixed support judgment recorded by the model tool |
| ClaimSupportFinding | Exists | `llmwiki.domain.claim_support`; deterministic or support-verdict audit finding |
| ClaimSupportAuditReport | Exists | `llmwiki.domain.claim_support`; harness-owned report filed to `wiki-claim-support` |
| IngestConfidenceGate | Exists | `llmwiki.domain.ingest_confidence`; one deterministic or model-assisted confidence check |
| ValidationFinding | Exists | `llmwiki.domain.ingest_confidence`; structured source-level report finding |
| ArtifactReuseDecision | Exists | `llmwiki.domain.ingest_confidence`; generated artifact reuse or rebuild decision |
| GroundingVerdict | Exists | `llmwiki.domain.grounding` |
| ContradictionFinding | Exists | `llmwiki.domain.contradictions` |
| CandidateRecord | Exists | `llmwiki.domain.candidates` |
| Citation | Existing concept | `llmwiki.domain.citations.Citation` |
| EvidenceLocator | Exists | `llmwiki.domain.evidence_locator_index`; normalized source address for one evidence span |
| EvidenceIdentity | Exists | `llmwiki.domain.evidence_locator_index`; page-independent identity material for one `EvidenceRecord` |
| EvidenceLocatorIndex | Exists | `llmwiki.domain.evidence_locator_index`; generated locator index for one source |
| EvidenceLocatorFinding | Exists | `llmwiki.domain.evidence_locator_index`; deterministic locator index finding |
| EvidenceLocatorBuilder | Exists | `llmwiki.domain.evidence_locator_builder`; domain service that creates `EvidenceLocatorIndex` |
| LocatorArtifactFingerprint | Exists | `llmwiki.domain.evidence_locator_index`; generated locator artifact fingerprint |
| LocatorStabilityGate | Exists | `llmwiki.runtime.ingest_confidence_locator_gate`; confidence gate for locator index drift |
| TechnicalAtom | Exists | `llmwiki.domain.technical_atoms`; one preserved bounded technical item from a source |
| TechnicalAtomKind | Exists | `llmwiki.domain.technical_atoms`; kind label for a preserved technical item |
| TechnicalAtomCatalog | Exists | `llmwiki.domain.technical_atoms`; rebuildable source-scoped collection of technical atoms |
| TechnicalDetailsSection | Exists | `llmwiki.domain.technical_atoms`; source page section rendered from `TechnicalAtomCatalog` |
| AnswerEvaluationCase | Exists | `llmwiki.domain.answer_evaluation`; fixture for one normal `query` answer check |
| AnswerEvaluationReport | Exists | `llmwiki.domain.answer_evaluation`; deterministic report for one checked answer |
| SourceExcerpt | Existing concept | `ClaimCandidate.evidence_excerpt` in `llmwiki.domain.grounding` |
| LintFinding | Exists | `llmwiki.domain.objects`; citation/semantic findings remain separate concepts |
| SalienceSignal | Existing concept | `SalienceEntry` inputs in `llmwiki.domain.salience` |
| PageLink | Deferred | Introduce when individual `[[link]]` edges need validation beyond extraction. |
| PageWrite | Deferred | Introduce when a page write needs a durable domain record beyond current tool and log state. |

## Boundary Shape Inventory

### Boundary DTOs

| Term | Current surface | Maps into |
|---|---|---|
| PlanPagesParams | `llmwiki.workflows.ingest_route_tools` | `IngestRoutePlan`, `PlannedPage`, `RouteGap`, `PageMetadata` |
| PlannedPageParams | `llmwiki.workflows.ingest_route_tools` | `PlannedPage` |
| PlannedPageMetadataParams | `llmwiki.workflows.ingest_route_tools` | `PageMetadata` |
| RouteGapParams | `llmwiki.workflows.ingest_route_tools` | `RouteGap` |
| PlannedWritePageParams | `llmwiki.workflows.planned_write_tools` | `PageBody` for one authorized `PlannedPageWrite` |
| PlannedWriteSourceSummaryParams | `llmwiki.workflows.source_summary_write` | `SourceSummaryDraft` for one source-summary `PlannedPageWrite` |
| SourceSummaryBulletParams | `llmwiki.workflows.source_summary_write` | `SourceSummaryBullet` |
| WritePageParams | `llmwiki.workflows.tools` and `llmwiki.workflows.chat_file_tools` | `WikiPage` directly, or `SourceSummaryDraft` before `WikiPage` rendering when a `SourceSummaryPlan` is active |
| ReadPageParams | `llmwiki.workflows.tools` | page lookup inputs |
| ReadSourceParams | `llmwiki.workflows.tools` | raw source lookup inputs |
| SearchWikiParams | `llmwiki.workflows.tools` | wiki search inputs |
| FinishParams | `llmwiki.workflows.tools` | operation completion output |
| WriteFixedSourcePageParams | `llmwiki.workflows.fixed_page_tools` | `WikiPage` through fixed-page ingest flow |
| RecordGroundingVerdictParams | `llmwiki.workflows.grounding_tools` | `GroundingVerdict` |
| RecordClaimSupportVerdictParams | `llmwiki.workflows.claim_support_tools` | `ClaimSupportVerdict` |
| RecordContradictionParams | `llmwiki.workflows.contradiction_tools` | `ContradictionFinding` |
| RecordSemanticFindingParams | `llmwiki.workflows.semantic_lint_tools` | semantic lint finding records |
| LinkOrphanParams | `llmwiki.workflows.graph_tools` | deterministic link insertion inputs |
| CLI args | `llmwiki.cli` | orchestrator inputs and runtime/config domain values |
| forge tool payloads | `forge` tool calls entering workflow tools | Pydantic DTOs before domain mapping |

### Persistence Models

| Term | Current surface | Maps into |
|---|---|---|
| IngestRoutePlanRecord | `llmwiki.domain.ingest_route_history` JSONL | `IngestRoutePlan` summary and page write history |
| Manifest | `llmwiki.pdf.manifest.Manifest` JSON | `PdfIngestManifest` concept |
| ChunkRecord | `llmwiki.pdf.manifest.ChunkRecord` JSON | PDF chunk ingest state |
| graph JSON | `wiki/wiki-graph.json` from `llmwiki.domain.graph.WikiGraph.to_payload` | `WikiGraph` |
| candidate JSON | `wiki/wiki-candidates.json` from `CandidateBacklog.to_json_text` | `CandidateBacklog` |
| chat SQLite rows | `llmwiki.store.chat_store` | `ChatSession` concept |
| accepted source summary draft JSON | `cache/page-plans/*/accepted-source-summaries/*.json` | `SourceSummaryDraft` |
| technical atom catalog JSON | `cache/page-plans/*/technical-atoms.json` | `TechnicalAtomCatalog` |

### View Models

| Term | Current surface | Derived from |
|---|---|---|
| CuratorStatus | `llmwiki.domain.maintenance` | wiki shape, deterministic findings, route-plan status, reports |
| RoutePlanStatus | `llmwiki.domain.maintenance` | ingest route plan records |
| LintDelta | `llmwiki.runtime.session` | before/after deterministic lint snapshots |
| CitationReport | `llmwiki.domain.citations` | parsed citations and citation findings |
| EvidenceLintReport | `llmwiki.domain.evidence` | citation evidence policy evaluation |
| GroundingAuditReport | `llmwiki.domain.grounding` | selected claim candidates and grounding verdicts |
| ContradictionAuditReport | `llmwiki.domain.contradictions` | selected contradiction candidates and findings |
| SemanticLintReport | `llmwiki.domain.semantic_lint` | selected semantic lint candidates and findings |
| IngestConfidenceReport | `llmwiki.domain.ingest_confidence` | artifact decisions, confidence gates, and validation findings |
| SalienceReport | `llmwiki.domain.salience` | deterministic salience entries |
| GraphStatus | `llmwiki.domain.graph` | current graph and stored graph JSON |

## Adoption Rules

- New features must reuse a term from this document or define the new term
  before implementation.
- Each new cross-boundary shape must be classified as a domain object, boundary
  DTO, persistence model, or view model.
- Boundary DTOs, persistence models, and view models must map explicitly into
  domain objects before domain rules run.
- Pure transport, logging, and pass-through display may remain DTO-shaped when
  no domain rule is applied.
- Domain objects live under `harness/src/llmwiki/domain/` unless a later TDD
  defines a narrower package boundary.
- Domain objects validate context-free local invariants at construction time.
- Domain services validate rules that require context, stores, profiles, schema
  documents, or multiple domain objects.
- Orchestrators own side effects and arrange domain services.
- Planning artifacts, route plans, reports, and prompts are not source evidence.
- Do not use near-synonyms for established domain terms. For example, use
  `page write`, not `ingest page write`, `wiki write`, `page update`, or
  `write operation`, unless a TDD defines a different concept.
