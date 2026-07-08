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
| deterministic boundary | Project-owned boundary whose structured values come from deterministic code or persisted generated artifacts. |
| model output boundary | Boundary whose structured values come from non-deterministic model output. |
| boundary recovery | Visible rejection, retry feedback, quarantine, validation error, finding, or proposed change for invalid model output. |
| check plan | Agent-runnable contract document for source-of-truth maps, forbidden patterns, workflows, and validation passes. |
| contract source of truth | Canonical code or document that owns one contract surface. |
| forbidden pattern | Named implementation or documentation shape that active production code must not use. |
| agent workflow | Repeatable agent-facing procedure with a trigger, command, artifacts, and acceptance signal. |
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
| `DeterministicBoundary` | `deterministic_boundary` |
| `ModelOutputBoundary` | `model_output_boundary` |
| `BoundaryDTO` | `boundary_dto` |
| `BoundaryRecovery` | `boundary_recovery` |
| `CheckPlan` | `check_plan` |
| `ContractSourceOfTruth` | `contract_source_of_truth` |
| `ForbiddenPattern` | `forbidden_pattern` |
| `AgentWorkflow` | `agent_workflow` |
| `PageKind` | `page_kind` |
| `PageFamily` | `page_family` |
| `PagePath` | `page_path` |
| `PageBody` | `page_body` |
| `PageBodyContract` | `page_body_contract` |
| `ResolvedPageBodyContract` | `resolved_page_body_contract` |
| `PageBodyFinding` | `page_body_finding` |
| `PageSynthesisPlan` | `page_synthesis_plan` |
| `PageDraft` | `page_draft` |
| `DraftClaim` | `draft_claim` |
| `DraftEvidenceRef` | `draft_evidence_ref` |
| `PageSynthesisFinding` | `page_synthesis_finding` |
| `PageMetadata` | `page_metadata` |
| `DomainFrontmatter` | `domain_frontmatter` |
| `GeneratedWikiState` | `generated_wiki_state` |
| `SourceLocator` | `source_locator` |
| `SourceText` | `source_text` |
| `SourceRange` | `source_range` |
| `RawSource` | `raw_source` |
| `SourceBundle` | `source_bundle` |
| `NormalizedSourceMap` | `normalized_source_map` |
| `SourceBlock` | `source_block` |
| `SourceAnchor` | `source_anchor` |
| `SourceMapFinding` | `source_map_finding` |
| `PromptWindow` | `prompt_window` |
| `SourceProfile` | `source_profile` |
| `EvidenceRecordType` | `evidence_record_type` |
| `EvidenceVocabulary` | `evidence_vocabulary` |
| `EvidenceExtractionPlan` | `evidence_extraction_plan` |
| `EvidenceExtractionFinding` | `evidence_extraction_finding` |
| `TypedEvidenceRecord` | `typed_evidence_record` |
| `EvidenceRecordSet` | `evidence_record_set` |
| `EvidenceRecordStatus` | `evidence_record_status` |
| `EvidenceRecordFinding` | `evidence_record_finding` |
| `StructuredEvidencePayload` | `structured_evidence_payload` |
| `EvidencePack` | `evidence_pack` |
| `EvidencePackItem` | `evidence_pack_item` |
| `EvidencePackCoverage` | `evidence_pack_coverage` |
| `SupportRef` | `support_ref` |
| `HumanArticle` | `human_article` |
| `ArticleSection` | `article_section` |
| `ArticleBlock` | `article_block` |
| `ArticleClaim` | `article_claim` |
| `ArticleCitation` | `article_citation` |
| `ArticleRelatedLink` | `article_related_link` |
| `ArticleFinding` | `article_finding` |
| `ArticleCoverageRequirement` | `article_coverage_requirement` |
| `ArticleEvidenceCoverage` | `article_evidence_coverage` |
| `ArticleEvidenceCoverageMetrics` | `article_evidence_coverage_metrics` |
| `ArticleRenderer` | `article_renderer` |
| `ArticleLintRun` | `article_lint_run` |
| `ArticleLintFinding` | `article_lint_finding` |
| `ArticleAuthorityMetrics` | `article_authority_metrics` |
| `ArticleCoherenceMetrics` | `article_coherence_metrics` |
| `PublicationGate` | `publication_gate` |
| `ArticleLintArtifact` | `article_lint_artifact` |
| `IngestCompiler` | `ingest_compiler` |
| `IngestCompilerInput` | `ingest_compiler_input` |
| `IngestCompilation` | `ingest_compilation` |
| `IngestArtifactSet` | `ingest_artifact_set` |
| `CompilerStage` | `compiler_stage` |
| `CompilerFinding` | `compiler_finding` |
| `DiagnosticQuestionSet` | `diagnostic_question_set` |
| `DiagnosticQuestion` | `diagnostic_question` |
| `DiagnosticAnswer` | `diagnostic_answer` |
| `DiagnosticAnswerSet` | `diagnostic_answer_set` |
| `DiagnosticFinding` | `diagnostic_finding` |
| `DiagnosticFindingSet` | `diagnostic_finding_set` |
| `DiagnosticReport` | `diagnostic_report` |
| `RepairTask` | `repair_task` |
| `RepairTaskSet` | `repair_task_set` |
| `RepairRun` | `repair_run` |
| `DiagnosticAnswerCorpus` | `diagnostic_answer_corpus` |
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
| `TechnicalTable` | `technical_table` |
| `TechnicalTableBlock` | `technical_table_block` |
| `TechnicalDetailsSection` | `technical_details_section` |
| `AnswerEvaluationCase` | `answer_evaluation_case` |
| `AnswerEvaluationReport` | `answer_evaluation_report` |
| `ClaimSupportCandidate` | `claim_support_candidate` |
| `ClaimSupportVerdict` | `claim_support_verdict` |
| `ClaimSupportFinding` | `claim_support_finding` |
| `ClaimSupportAuditReport` | `claim_support_audit_report` |
| `ProjectionPolicy` | `projection_policy` |
| `ProjectionBudget` | `projection_budget` |
| `ProjectionContext` | `projection_context` |
| `ProjectionEligibility` | `projection_eligibility` |
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
| IngestCompiler | Exists | `llmwiki.runtime.ingest_compiler`; orchestrates one source compiler path from source map through staged publish |
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
| ProjectionPolicy | Exists | `llmwiki.domain.ledger.projection_policy`; decides page family, source-support budget, and standalone render eligibility |
| ProjectionBudget | Exists | `llmwiki.domain.ledger.projection_policy`; source-agnostic thresholds for broad topic projection |
| ProjectionContext | Exists | `llmwiki.domain.ledger.projection_context`; portable coherent evidence blocks and technical atom frames |
| ProjectionEligibility | Exists | `llmwiki.domain.ledger.projection_policy`; classifies ledger entries as standalone, contextual-only, technical-frame-only, or review-only |
| IngestRoutePlan | Exists | `llmwiki.domain.ingest_route_plan` |
| PlannedPage | Exists | `llmwiki.domain.ingest_route_plan` |
| RouteGap | Exists | `llmwiki.domain.ingest_route_plan` |
| PageBodyContract | Exists | `llmwiki.domain.page_body_contracts`; owned by `Schema` |
| ResolvedPageBodyContract | Exists | `llmwiki.domain.page_body_contracts`; bound to one `PlannedPageWrite` |
| PageBodyFinding | Exists | `llmwiki.domain.page_body_contracts`; returned by body validation |
| PageSynthesisPlan | Exists | `llmwiki.domain.ledger.page_synthesis`; selected evidence and outline for one generated projection page |
| PageDraft | Exists | `llmwiki.domain.ledger.page_synthesis`; structured draft validated before markdown rendering |
| DraftClaim | Exists | `llmwiki.domain.ledger.page_synthesis`; one factual sentence with selected evidence support |
| DraftEvidenceRef | Exists | `llmwiki.domain.ledger.page_synthesis`; ledger, atom, or stable atom-anchor support reference |
| PageSynthesisFinding | Exists | `llmwiki.domain.ledger.page_synthesis`; rejection or warning emitted by synthesis validation |
| SourcePlanContractSelection | Exists | `llmwiki.domain.page_body_contracts`; selected through `SourcePlan` |
| NormalizedSourceMap | Exists | `llmwiki.domain.source_map`; durable source model for one `RawSource` |
| SourceBlock | Exists | `llmwiki.domain.source_map`; one coherent source unit in a `NormalizedSourceMap` |
| SourceAnchor | Exists | `llmwiki.domain.source_map`; stable locator for one `SourceBlock` or source span |
| SourceMapFinding | Exists | `llmwiki.domain.source_map`; one source map quality issue |
| PromptWindow | Exists | `llmwiki.domain.source_map`; derived model prompt window from source blocks |
| SourceProfile | Exists | `llmwiki.domain.source_profiles`; source-purpose classification that selects typed evidence vocabulary, distinct from runtime `IngestProfile` overlays |
| EvidenceRecordType | Exists | `llmwiki.domain.source_profiles`; allowed typed-evidence record label selected by `SourceProfile` |
| EvidenceVocabulary | Exists | `llmwiki.domain.source_profiles`; profile-owned set of allowed `EvidenceRecordType` values |
| EvidenceExtractionPlan | Exists | `llmwiki.domain.source_profiles`; source-block plan and allowed record types for typed evidence extraction |
| EvidenceExtractionFinding | Exists | `llmwiki.domain.source_profiles`; blocking or warning finding for source-profile evidence extraction contracts |
| EvidenceRecordSet | Exists | `llmwiki.domain.typed_evidence`; source-scoped typed evidence artifact used by PDF page planning |
| TypedEvidenceRecord | Exists | `llmwiki.domain.typed_evidence`; one source-anchored factual record with an allowed `EvidenceRecordType` |
| EvidenceRecordStatus | Exists | `llmwiki.domain.typed_evidence`; accepted, fragmentary, rejected, or needs-review status for typed evidence |
| EvidenceRecordFinding | Exists | `llmwiki.domain.typed_evidence`; validation finding for one typed evidence record |
| StructuredEvidencePayload | Exists | `llmwiki.domain.typed_evidence`; non-lossy payload text and normalized fields for typed evidence |
| EvidencePack | Exists | `llmwiki.domain.ledger.evidence_pack`; selected non-lossy support for one accepted public page candidate |
| EvidencePackItem | Exists | `llmwiki.domain.ledger.evidence_pack`; one full-text or payload support item in an `EvidencePack` |
| EvidencePackCoverage | Exists | `llmwiki.domain.ledger.evidence_pack`; coverage relationship between a page purpose and selected support |
| SupportRef | Exists | `llmwiki.domain.ledger.evidence_pack`; stable support reference that article claims can cite |
| HumanArticle | Exists | `llmwiki.domain.ledger.human_article`; structured article content for one public generated page |
| ArticleSection | Exists | `llmwiki.domain.ledger.human_article`; one headed section inside a `HumanArticle` |
| ArticleBlock | Exists | `llmwiki.domain.ledger.human_article`; structured prose, list, table, or code block inside an article section |
| ArticleClaim | Exists | `llmwiki.domain.ledger.human_article`; one factual article sentence with evidence-pack support refs |
| ArticleCitation | Exists | `llmwiki.domain.ledger.human_article`; one resolved citation from an article claim to pack support |
| ArticleRelatedLink | Exists | `llmwiki.domain.ledger.human_article`; navigation-only related-page preview for a rendered article |
| ArticleFinding | Exists | `llmwiki.domain.ledger.human_article`; validation or write finding for article generation |
| ArticleCoverageRequirement | Exists | `llmwiki.domain.ledger.article_evidence_coverage`; one required or optional evidence-pack unit an article can cover |
| ArticleEvidenceCoverage | Exists | `llmwiki.domain.ledger.article_evidence_coverage`; maps one article coverage requirement to the claims that cited it |
| ArticleEvidenceCoverageMetrics | Exists | `llmwiki.domain.ledger.article_evidence_coverage`; measured required evidence coverage for one generated article |
| ArticleRenderer | Exists | `llmwiki.domain.ledger.human_article_rendering`; harness-owned renderer from accepted `HumanArticle` to wiki markdown |
| ArticleLintRun | Exists | `llmwiki.domain.ledger.article_lint_contracts`; deterministic per-page lint run after article rendering |
| ArticleLintFinding | Exists | `llmwiki.domain.ledger.article_lint_contracts`; one citation, authority, coherence, or title lint finding |
| ArticleAuthorityMetrics | Exists | `llmwiki.domain.ledger.article_lint_contracts`; measured citation coverage for rendered factual article prose |
| ArticleCoherenceMetrics | Exists | `llmwiki.domain.ledger.article_lint_contracts`; measured clipped, copied, unreadable, and missing-navigation-preview counts |
| PublicationGate | Exists | `llmwiki.domain.ledger.article_lint_contracts`; deterministic accept/block decision for one generated article page |
| ArticleLintArtifact | Exists | `llmwiki.domain.ledger.article_lint_artifacts`; source-scoped artifact containing article lint runs |
| IngestCompilerInput | Exists | `llmwiki.domain.ingest_compiler`; explicit source locator and extraction options for one compiler run |
| IngestCompilation | Exists | `llmwiki.domain.ingest_compiler`; compiler output containing accepted pages, artifacts, stage manifest, and report text |
| IngestArtifactSet | Exists | `llmwiki.domain.ingest_compiler`; source-scoped manifest for ordered compiler stage outputs, accepted pages, rejected pages, and findings |
| CompilerStage | Exists | `llmwiki.domain.ingest_compiler`; one ordered compiler stage with input/output artifact ids, status, timing, and finding count |
| CompilerFinding | Exists | `llmwiki.domain.ingest_compiler`; one source compiler blocking or diagnostic finding |
| DiagnosticQuestionSet | Exists | `llmwiki.domain.diagnostic_contracts`; deterministic source-grounded questions generated from accepted evidence packs |
| DiagnosticQuestion | Exists | `llmwiki.domain.diagnostic_contracts`; one planned diagnostic question with expected support refs and source anchors |
| DiagnosticAnswer | Exists | `llmwiki.domain.diagnostic_contracts`; one wiki-only answer to a diagnostic question |
| DiagnosticAnswerSet | Exists | `llmwiki.domain.diagnostic_contracts`; source-scoped artifact containing all wiki-only diagnostic answers |
| DiagnosticFinding | Exists | `llmwiki.domain.diagnostic_contracts`; one evidence-backed issue found while judging a diagnostic answer |
| DiagnosticFindingSet | Exists | `llmwiki.domain.diagnostic_contracts`; source-scoped artifact containing diagnostic answer findings |
| DiagnosticReport | Exists | `llmwiki.domain.diagnostic_contracts`; generated report summarizing diagnostic coverage, missing answers, unsupported answers, and repairs |
| RepairTask | Exists | `llmwiki.domain.diagnostic_contracts`; one bounded article-rewrite task derived from blocking diagnostic findings |
| RepairTaskSet | Exists | `llmwiki.domain.diagnostic_contracts`; source-scoped artifact containing planned diagnostic repair tasks |
| RepairRun | Exists | `llmwiki.domain.diagnostic_contracts`; one bounded repair attempt and its changed, accepted, or rejected article pages |
| DiagnosticAnswerCorpus | Exists | `llmwiki.domain.diagnostic_contracts`; in-memory staged-wiki snapshot available to diagnostic answerers |
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
| EvidenceRecord | Exists | `llmwiki.domain.evidence_registry`; stable generated evidence excerpt record for citation/range audits, not the typed evidence authority |
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
| TechnicalTable | Exists | `llmwiki.domain.technical_tables`; one preserved table owned by `TechnicalAtomCatalog` |
| TechnicalTableBlock | Exists | `llmwiki.domain.technical_tables`; one contiguous table block owned by `TechnicalTable` |
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
| ingest artifact set JSON | `cache/ingest-compiler/*/ingest-artifact-set.json` | `IngestArtifactSet` |
| compiler normalized source map JSON | `cache/ingest-compiler/*/normalized-source-map.json` | `NormalizedSourceMap` |
| compiler evidence pack set JSON | `cache/ingest-compiler/*/evidence-pack-set.json` | `EvidencePackSet` |
| diagnostic question set JSON | `cache/ingest-compiler/*/diagnostic-question-set.json` | `DiagnosticQuestionSet` |
| diagnostic answer set JSON | `cache/ingest-compiler/*/diagnostic-answer-set.json` | `DiagnosticAnswerSet` |
| diagnostic finding set JSON | `cache/ingest-compiler/*/diagnostic-finding-set.json` | `DiagnosticFindingSet` |
| diagnostics report markdown | `cache/ingest-compiler/*/diagnostics-report.md` | `DiagnosticReport` |
| repair task set JSON | `cache/ingest-compiler/*/repair-task-set.json` | `RepairTaskSet` |
| repair run JSON | `cache/ingest-compiler/*/repair-run.json` | `RepairRun` |
| graph JSON | `wiki/wiki-graph.json` from `llmwiki.domain.graph.WikiGraph.to_payload` | `WikiGraph` |
| candidate JSON | `wiki/wiki-candidates.json` from `CandidateBacklog.to_json_text` | `CandidateBacklog` |
| chat SQLite rows | `llmwiki.store.chat_store` | `ChatSession` concept |
| accepted source summary draft JSON | `cache/page-plans/*/accepted-source-summaries/*.json` | `SourceSummaryDraft` |
| evidence record set JSON | `cache/page-plans/*/evidence-record-set.json` | `EvidenceRecordSet` |
| technical atom catalog JSON | `cache/page-plans/*/technical-atoms.json` | `TechnicalAtomCatalog` |
| projection context JSON | `cache/page-plans/*/ledger/projection-context.json` | `ProjectionContext` |

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
