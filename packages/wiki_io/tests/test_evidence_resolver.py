"""Tests for wiki_io.evidence.resolver module."""
import pytest
from wiki_io.evidence.resolver import (
    stable_evidence_id,
    bracketed_evidence_id,
    evidence_id_aliases,
    extract_evidence_ids,
    ResolvedEvidence,
)


class TestStableEvidenceId:
    """Tests for stable_evidence_id()."""

    def test_basic_id(self):
        assert stable_evidence_id(
            "aoe2", "claim_test_c001") == "aoe2:claim_test_c001"

    def test_already_prefixed(self):
        """Already-prefixed IDs should not be double-prefixed."""
        assert stable_evidence_id(
            "aoe2", "aoe2:claim_test_c001") == "aoe2:claim_test_c001"

    def test_different_slug(self):
        assert stable_evidence_id("foo", "bar:claim_x") == "foo:bar:claim_x"


class TestBracketedEvidenceId:
    """Tests for bracketed_evidence_id()."""

    def test_basic(self):
        assert bracketed_evidence_id(
            "aoe2", "claim_c001") == "[aoe2:claim_c001]"


class TestEvidenceIdAliases:
    """Tests for evidence_id_aliases()."""

    def test_generates_lowercase(self):
        aliases = evidence_id_aliases("AoE2", "Claim_Test")
        assert "aoe2:claim_test" in aliases
        assert "claim_test" in aliases


class TestExtractEvidenceIds:
    """Tests for extract_evidence_ids()."""

    def test_bracketed(self):
        assert extract_evidence_ids("[aoe2:claim_c001]") == ["aoe2:claim_c001"]

    def test_multiple(self):
        ids = extract_evidence_ids("[id1], [id2]")
        assert ids == ["id1", "id2"]

    def test_bare_id(self):
        assert extract_evidence_ids("claim_c001") == ["claim_c001"]

    def test_backticked(self):
        assert extract_evidence_ids("`claim_c001`") == ["claim_c001"]

    def test_empty(self):
        assert extract_evidence_ids("no ids here") == []


class TestResolvedEvidence:
    """Tests for ResolvedEvidence dataclass."""

    def test_frozen(self):
        item = ResolvedEvidence(
            evidence_id="aoe2:c001",
            claim_id="c001",
            source_slug="aoe2",
            topic="Test",
            claim="A claim",
            evidence="Some evidence",
            locator="normalized:L10",
            source_page="wiki/sources/aoe2.md",
        )
        with pytest.raises(Exception):
            item.evidence_id = "new_id"
