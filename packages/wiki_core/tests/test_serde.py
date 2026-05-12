#!/usr/bin/env python3
"""Tests for wiki_core.serde module."""

import pytest
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum

from wiki_core.serde import structure, unstructure, register_private_fields_hook


class Priority(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass
class SimpleClaim:
    """Simple test dataclass."""
    topic: str
    claim: str
    evidence: str


@dataclass
class ClaimWithDefaults:
    """Dataclass with default values."""
    topic: str
    claim: str
    evidence: str = ""
    chunk_index: int = 0


@dataclass
class NestedExample:
    """Dataclass with nested dataclass."""
    name: str
    claims: list[SimpleClaim] = field(default_factory=list)


@dataclass
class WithPrivateField:
    """Dataclass with private field."""
    name: str
    value: int
    _internal: str = "private"


@dataclass
class WithEnum:
    """Dataclass with enum field."""
    name: str
    priority: Priority = Priority.MEDIUM


class TestUnstructure:
    """Tests for unstructure()."""

    def test_simple_dataclass(self):
        claim = SimpleClaim(
            topic="Functions", claim="Functions are first-class", evidence="page 42")
        result = unstructure(claim)
        assert result == {
            "topic": "Functions",
            "claim": "Functions are first-class",
            "evidence": "page 42",
        }

    def test_dataclass_with_defaults(self):
        claim = ClaimWithDefaults(topic="Functions", claim="First-class")
        result = unstructure(claim)
        assert result == {
            "topic": "Functions",
            "claim": "First-class",
            "evidence": "",
            "chunk_index": 0,
        }

    def test_nested_dataclass(self):
        nested = NestedExample(
            name="test",
            claims=[SimpleClaim("A", "B", "C")],
        )
        result = unstructure(nested)
        assert result == {
            "name": "test",
            "claims": [{"topic": "A", "claim": "B", "evidence": "C"}],
        }

    def test_private_field_excluded(self):
        register_private_fields_hook(WithPrivateField)
        obj = WithPrivateField(name="test", value=42, _internal="secret")
        result = unstructure(obj)
        assert result == {"name": "test", "value": 42}
        assert "_internal" not in result


class TestStructure:
    """Tests for structure()."""

    def test_simple_dataclass(self):
        data = {"topic": "Functions", "claim": "First-class", "evidence": "p42"}
        result = structure(data, SimpleClaim)
        assert result == SimpleClaim("Functions", "First-class", "p42")

    def test_dataclass_with_defaults(self):
        # Missing optional fields should use defaults
        data = {"topic": "Functions", "claim": "First-class"}
        result = structure(data, ClaimWithDefaults)
        assert result.topic == "Functions"
        assert result.claim == "First-class"
        assert result.evidence == ""
        assert result.chunk_index == 0

    def test_nested_dataclass(self):
        data = {
            "name": "test",
            "claims": [{"topic": "A", "claim": "B", "evidence": "C"}],
        }
        result = structure(data, NestedExample)
        assert result.name == "test"
        assert len(result.claims) == 1
        assert result.claims[0] == SimpleClaim("A", "B", "C")

    def test_roundtrip(self):
        original = NestedExample(
            name="roundtrip",
            claims=[
                SimpleClaim("T1", "C1", "E1"),
                SimpleClaim("T2", "C2", "E2"),
            ],
        )
        data = unstructure(original)
        restored = structure(data, NestedExample)
        assert restored == original


class TestEnumHandling:
    """Tests for enum serialization."""

    def test_enum_unstructure(self):
        obj = WithEnum(name="test", priority=Priority.HIGH)
        result = unstructure(obj)
        assert result["priority"] == "high"

    def test_enum_structure(self):
        data = {"name": "test", "priority": "low"}
        result = structure(data, WithEnum)
        assert result.priority == Priority.LOW


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
