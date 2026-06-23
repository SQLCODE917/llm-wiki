"""Technical atom checks for ingest confidence reports."""

from __future__ import annotations

from llmwiki.domain.ingest_confidence import ValidationFinding, validation_finding
from llmwiki.domain.technical_atoms import TechnicalAtomCatalog


def technical_atom_findings(
    source_locator: str, catalog: TechnicalAtomCatalog | None
) -> tuple[ValidationFinding, ...]:
    if catalog is not None:
        return ()
    return (
        validation_finding(
            severity="warning",
            category="technical-atoms",
            source_locator=source_locator,
            message="TechnicalAtomCatalog is missing.",
        ),
    )


def technical_atom_detail(catalog: TechnicalAtomCatalog | None) -> str:
    if catalog is None:
        return "No TechnicalAtomCatalog available."
    counts = catalog.counts_by_kind()
    if not counts:
        return "Technical atoms: 0"
    rendered_counts = "\n".join(f"- {kind}: {count}" for kind, count in counts)
    return f"Technical atoms: {len(catalog.technical_atoms)}\n{rendered_counts}"
