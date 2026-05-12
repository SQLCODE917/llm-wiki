#!/usr/bin/env python3
"""Tests for wiki_io state management."""
import json
import tempfile
from pathlib import Path

from wiki_io.state import (
    # Manifest
    Manifest,
    PhaseStatus,
    ErrorInfo,
    Phase2Progress,
    PHASE_NAMES,
    # Claims
    RawClaim,
    NormalizedClaim,
    NormalizedClaimsData,
    append_raw_claim,
    load_raw_claims,
    save_normalized_claims,
    load_normalized_claims,
    load_extraction_data_for_synthesis,
    get_processed_chunk_indices,
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


def test_paths():
    """Test path functions."""
    assert get_state_dir("test").name == "test"
    assert ".wiki-extraction-state" in str(get_state_dir("test"))
    assert get_normalized_claims_path("test").name == "claims-normalized.json"
    print("✓ test_paths passed")


def test_phase_status():
    """Test PhaseStatus enum."""
    assert PhaseStatus.PENDING.value == "pending"
    assert PhaseStatus.COMPLETE.value == "complete"
    assert PhaseStatus("running") == PhaseStatus.RUNNING
    print("✓ test_phase_status passed")


def test_error_info():
    """Test ErrorInfo dataclass."""
    error = ErrorInfo(phase="phase1a_extract", message="Test error")
    assert error.phase == "phase1a_extract"
    assert error.message == "Test error"
    assert error.occurred_at  # Auto-populated

    data = error.to_dict()
    error2 = ErrorInfo.from_dict(data)
    assert error2.message == error.message
    print("✓ test_error_info passed")


def test_phase2_progress():
    """Test Phase2Progress dataclass."""
    progress = Phase2Progress(total_candidates=10, synthesized=5)
    assert progress.total_candidates == 10
    assert progress.synthesized == 5

    data = progress.to_dict()
    progress2 = Phase2Progress.from_dict(data)
    assert progress2.total_candidates == 10
    print("✓ test_phase2_progress passed")


def test_raw_claim():
    """Test RawClaim dataclass."""
    claim = RawClaim(
        topic="Functions",
        claim="Functions are values",
        evidence="In JavaScript...",
        locator="normalized:L100",
        chunk_index=0,
    )
    assert claim.topic == "Functions"
    assert claim.extracted_at  # Auto-populated

    data = claim.to_dict()
    claim2 = RawClaim.from_dict(data)
    assert claim2.claim == claim.claim
    print("✓ test_raw_claim passed")


def test_normalized_claim():
    """Test NormalizedClaim dataclass."""
    claim = NormalizedClaim(
        claim_id="claim_test_c000_abc123",
        topic="Functions",
        claim="Functions are values",
        evidence="In JavaScript...",
        locator="normalized:L100",
        chunk_index=0,
    )
    assert claim.claim_id == "claim_test_c000_abc123"

    data = claim.to_dict()
    claim2 = NormalizedClaim.from_dict(data)
    assert claim2.claim_id == claim.claim_id
    print("✓ test_normalized_claim passed")


def test_normalized_claims_data():
    """Test NormalizedClaimsData container."""
    claims = [
        NormalizedClaim(
            claim_id="claim_test_c000_abc123",
            topic="Functions",
            claim="Test claim",
            evidence="Evidence",
            locator="normalized:L100",
            chunk_index=0,
        )
    ]
    data = NormalizedClaimsData(
        slug="test",
        claims=claims,
        topics={"Functions": ["claim_test_c000_abc123"]},
        raw_claims_count=10,
        deduped_count=5,
    )
    assert data.slug == "test"
    assert len(data.claims) == 1

    d = data.to_dict()
    data2 = NormalizedClaimsData.from_dict(d)
    assert data2.slug == "test"
    assert len(data2.claims) == 1
    print("✓ test_normalized_claims_data passed")


def test_candidate():
    """Test Candidate dataclass."""
    candidate = Candidate(
        title="Example Concept",
        path="../concepts/example.md",
        page_type="concept",
        priority="must create",
        claim_ids=["claim_1", "claim_2"],
        evidence_basis="multiple claims about example",
    )
    assert candidate.title == "Example Concept"
    assert candidate.status == "not created"

    data = candidate.to_dict()
    candidate2 = Candidate.from_dict(data)
    assert candidate2.title == candidate.title
    print("✓ test_candidate passed")


def test_generated_candidates_data():
    """Test GeneratedCandidatesData container."""
    candidates = [
        Candidate(
            title="Example",
            path="../concepts/example.md",
            page_type="concept",
            priority="must create",
            claim_ids=["c1"],
        )
    ]
    data = GeneratedCandidatesData(
        slug="test",
        candidates=candidates,
        normalized_claims_hash="abc123",
    )
    assert data.slug == "test"
    assert len(data.candidates) == 1

    d = data.to_dict()
    data2 = GeneratedCandidatesData.from_dict(d)
    assert data2.slug == "test"
    print("✓ test_generated_candidates_data passed")


def test_load_existing_claims():
    """Test loading existing claims from js-allonge."""
    claims = load_normalized_claims("js-allonge")
    if claims is None:
        print("⚠ test_load_existing_claims skipped (no js-allonge data)")
        return

    assert claims.slug == "js-allonge"
    assert len(claims.claims) > 0
    assert len(claims.topics) > 0
    print(
        f"✓ test_load_existing_claims passed (loaded {len(claims.claims)} claims)")


def test_load_extraction_data_for_synthesis():
    """Test loading extraction data for synthesis."""
    data = load_extraction_data_for_synthesis("js-allonge")
    if data is None:
        print("⚠ test_load_extraction_data_for_synthesis skipped (no js-allonge data)")
        return

    assert data.slug == "js-allonge"
    assert len(data.claims) > 0
    # Topics dict should have NormalizedClaim objects, not just IDs
    for topic, topic_claims in data.topics.items():
        assert len(topic_claims) > 0
        assert hasattr(topic_claims[0], "claim_id")
        break
    print("✓ test_load_extraction_data_for_synthesis passed")


if __name__ == "__main__":
    test_paths()
    test_phase_status()
    test_error_info()
    test_phase2_progress()
    test_raw_claim()
    test_normalized_claim()
    test_normalized_claims_data()
    test_candidate()
    test_generated_candidates_data()
    test_load_existing_claims()
    test_load_extraction_data_for_synthesis()

    print()
    print("All wiki_io.state tests passed! ✓")
