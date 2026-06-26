"""Portable artifact pointers and their typed aliases.

A ``PortableArtifactPointer`` references one child artifact by id and
fingerprint and names its target artifact kind, so the target type is never
ambiguous. The typed-alias constructors below bind the pointer to one target
artifact type (claim ledger, document structure, projection coverage, quality
report, quality check catalog).
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PortableArtifactPointer:
    target_artifact_kind: str
    target_artifact_id: str
    target_artifact_fingerprint: str


def claim_ledger_pointer(artifact_id: str, fingerprint: str) -> PortableArtifactPointer:
    return PortableArtifactPointer("claim-ledger-artifact", artifact_id, fingerprint)


def document_structure_pointer(artifact_id: str, fingerprint: str) -> PortableArtifactPointer:
    return PortableArtifactPointer("document-structure-artifact", artifact_id, fingerprint)


def projection_coverage_pointer(artifact_id: str, fingerprint: str) -> PortableArtifactPointer:
    return PortableArtifactPointer("projection-coverage-artifact", artifact_id, fingerprint)


def ledger_quality_report_pointer(artifact_id: str, fingerprint: str) -> PortableArtifactPointer:
    return PortableArtifactPointer("ledger-quality-report-artifact", artifact_id, fingerprint)


def quality_check_catalog_pointer(artifact_id: str, fingerprint: str) -> PortableArtifactPointer:
    return PortableArtifactPointer("quality-check-catalog-artifact", artifact_id, fingerprint)
