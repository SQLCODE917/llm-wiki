# Maintenance Report

Generated: 2026-05-03

## Summary

- Checks run: 11
- Failed: 0

## Checks

| Check | Status | Command |
|---|---|---|
| index | PASS | `python3 tools/wiki_index.py --check` |
| graph | PASS | `python3 tools/wiki_graph.py --check` |
| analysis | PASS | `python3 tools/wiki_check_analysis.py` |
| grounding | PASS | `python3 tools/wiki_grounding.py --check` |
| lint | PASS | `python3 tools/wiki_lint.py` |
| semantic | PASS | `python3 tools/wiki_semantic_lint.py` |
| contradictions | PASS | `python3 tools/wiki_contradictions.py` |
| executables | PASS | `python3 tools/wiki_executable_concepts.py --check` |
| curator-status | PASS | `python3 tools/wiki_curator_status.py --check` |
| phase0-smoke | PASS | `python3 tools/wiki_phase0_smoke_test.py` |
| query-smoke | PASS | `python3 tools/wiki_query_smoke_test.py` |
