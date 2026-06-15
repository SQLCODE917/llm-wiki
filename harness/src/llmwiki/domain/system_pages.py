"""Harness-owned wiki page names shared across deterministic checks."""

HEALTH_PAGE = "wiki-health"
CURATOR_STATUS_PAGE = "wiki-curator-status"
CONTRADICTIONS_PAGE = "wiki-contradictions"
GROUNDING_PAGE = "wiki-grounding"
SEMANTIC_LINT_PAGE = "wiki-semantic-lint"
SYSTEM_PAGES = frozenset(
    {HEALTH_PAGE, CURATOR_STATUS_PAGE, CONTRADICTIONS_PAGE, GROUNDING_PAGE, SEMANTIC_LINT_PAGE}
)
ORPHAN_EXEMPT_PAGES = SYSTEM_PAGES
