"""Path utilities for wiki extraction state.

Centralized path definitions for the extraction state directory structure.
All state files are stored under .wiki-extraction-state/<slug>/.

File layout:
    .wiki-extraction-state/<slug>/
    ├── manifest.json           # Pipeline status and config
    ├── claims-raw.jsonl        # Append-only raw claims (Phase 1a)
    ├── claims-normalized.json  # Deduped claims with IDs (Phase 1b)
    ├── candidates.generated.json  # Machine proposals (Phase 1c)
    ├── candidates.override.json   # Human curator overrides
    └── candidates.json         # Merged candidates
"""
from __future__ import annotations

from pathlib import Path


STATE_ROOT = Path(".wiki-extraction-state")


def get_state_dir(slug: str) -> Path:
    """Get the extraction state directory for a slug."""
    return STATE_ROOT / slug


def get_manifest_path(slug: str) -> Path:
    """Get the path to manifest.json."""
    return get_state_dir(slug) / "manifest.json"


def get_raw_claims_path(slug: str) -> Path:
    """Get the path to claims-raw.jsonl."""
    return get_state_dir(slug) / "claims-raw.jsonl"


def get_normalized_claims_path(slug: str) -> Path:
    """Get the path to claims-normalized.json."""
    return get_state_dir(slug) / "claims-normalized.json"


def get_generated_candidates_path(slug: str) -> Path:
    """Get the path to candidates.generated.json."""
    return get_state_dir(slug) / "candidates.generated.json"


def get_override_path(slug: str) -> Path:
    """Get the path to candidates.override.json."""
    return get_state_dir(slug) / "candidates.override.json"


def get_candidates_path(slug: str) -> Path:
    """Get the path to candidates.json (merged)."""
    return get_state_dir(slug) / "candidates.json"


def get_legacy_state_path(slug: str) -> Path:
    """Get the path to legacy state.json for compatibility."""
    return get_state_dir(slug) / "state.json"


def get_normalized_source_path(slug: str) -> Path:
    """Get the path to the normalized source markdown."""
    return Path(f"raw/normalized/{slug}/source.md")


def get_imported_path(slug: str, ext: str = ".pdf") -> Path:
    """Get the path to the imported original."""
    return Path(f"raw/imported/{slug}/original{ext}")


def ensure_state_dir(slug: str) -> Path:
    """Ensure the state directory exists and return its path."""
    state_dir = get_state_dir(slug)
    state_dir.mkdir(parents=True, exist_ok=True)
    return state_dir
