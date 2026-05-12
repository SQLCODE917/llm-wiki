"""State management for wiki extraction pipeline.

This module provides types and I/O functions for:
- Manifest tracking (pipeline status and configuration)
- Claims storage (raw and normalized)
- Candidate management (generated, overrides, merged)

Usage:
    from wiki_io.state import (
        # Manifest
        Manifest,
        PhaseStatus,
        ErrorInfo,
        Phase2Progress,
        # Claims
        RawClaim,
        NormalizedClaim,
        NormalizedClaimsData,
        append_raw_claim,
        load_raw_claims,
        save_normalized_claims,
        load_normalized_claims,
        load_extraction_data_for_synthesis,
        # Candidates
        Candidate,
        GeneratedCandidatesData,
        save_generated_candidates,
        load_generated_candidates,
        merge_candidates,
        # Paths
        get_state_dir,
        get_normalized_claims_path,
    )
"""
# Paths
from wiki_io.state.paths import (
    STATE_ROOT,
    get_state_dir,
    get_manifest_path,
    get_raw_claims_path,
    get_normalized_claims_path,
    get_generated_candidates_path,
    get_override_path,
    get_candidates_path,
    get_legacy_state_path,
    get_normalized_source_path,
    get_imported_path,
    ensure_state_dir,
)

# Manifest
from wiki_io.state.manifest import (
    SCHEMA_VERSION,
    PhaseStatus,
    PHASE_NAMES,
    ErrorInfo,
    Phase2Progress,
    Manifest,
)

# Claims
from wiki_io.state.claims import (
    RawClaim,
    NormalizedClaim,
    NormalizedClaimsData,
    ExtractionDataForSynthesis,
    append_raw_claim,
    append_raw_claims,
    load_raw_claims,
    iter_raw_claims,
    count_raw_claims,
    get_processed_chunk_indices,
    save_normalized_claims,
    load_normalized_claims,
    load_extraction_data_for_synthesis,
)

# Candidates
from wiki_io.state.candidates import (
    Candidate,
    GeneratedCandidatesData,
    CandidateOverride,
    OverridesData,
    MergedCandidatesData,
    save_generated_candidates,
    load_generated_candidates,
    load_overrides,
    save_overrides,
    save_merged_candidates,
    load_merged_candidates,
    merge_candidates,
)

__all__ = [
    # Paths
    "STATE_ROOT",
    "get_state_dir",
    "get_manifest_path",
    "get_raw_claims_path",
    "get_normalized_claims_path",
    "get_generated_candidates_path",
    "get_override_path",
    "get_candidates_path",
    "get_legacy_state_path",
    "get_normalized_source_path",
    "get_imported_path",
    "ensure_state_dir",
    # Manifest
    "SCHEMA_VERSION",
    "PhaseStatus",
    "PHASE_NAMES",
    "ErrorInfo",
    "Phase2Progress",
    "Manifest",
    # Claims
    "RawClaim",
    "NormalizedClaim",
    "NormalizedClaimsData",
    "ExtractionDataForSynthesis",
    "append_raw_claim",
    "append_raw_claims",
    "load_raw_claims",
    "iter_raw_claims",
    "count_raw_claims",
    "get_processed_chunk_indices",
    "save_normalized_claims",
    "load_normalized_claims",
    "load_extraction_data_for_synthesis",
    # Candidates
    "Candidate",
    "GeneratedCandidatesData",
    "CandidateOverride",
    "OverridesData",
    "MergedCandidatesData",
    "save_generated_candidates",
    "load_generated_candidates",
    "load_overrides",
    "save_overrides",
    "save_merged_candidates",
    "load_merged_candidates",
    "merge_candidates",
]
