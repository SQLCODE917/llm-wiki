"""wiki_io — I/O layer for the wiki ingestion pipeline.

This package handles all file I/O operations:
- State management (manifest, claims, candidates)
- Evidence resolution and validation
- File reading/writing
- Path utilities

Depends on wiki_core for type definitions.

Usage:
    from wiki_io.state import (
        Manifest,
        PhaseStatus,
        load_normalized_claims,
        merge_candidates,
    )
    
    from wiki_io.evidence import (
        EvidenceResolver,
        validate_evidence_location,
        SourceRange,
        parse_locator_range,
    )
"""
