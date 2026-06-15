"""Harness-owned wiki page names shared across deterministic checks."""

HEALTH_PAGE = "wiki-health"
CURATOR_STATUS_PAGE = "wiki-curator-status"
CONTRADICTIONS_PAGE = "wiki-contradictions"
SYSTEM_PAGES = frozenset({HEALTH_PAGE, CURATOR_STATUS_PAGE, CONTRADICTIONS_PAGE})
ORPHAN_EXEMPT_PAGES = SYSTEM_PAGES
