"""Tests for deterministic source-page provenance auditing."""

from __future__ import annotations

import json

from llmwiki.domain.pages import PageMetadata, WikiPage, render_page
from llmwiki.runtime.provenance_audit import audit_source_pages


def test_provenance_audit_flags_fragmentary_and_missing_ranges(tmp_path) -> None:
    wiki_dir = tmp_path / "wiki"
    ledger_dir = tmp_path / "ledger"
    wiki_dir.mkdir()
    ledger_dir.mkdir()
    page = WikiPage(
        page_metadata=PageMetadata(
            page_id="source-alpha",
            page_kind="concept",
            summary="Alpha topic.",
            sources=("raw/source.pdf",),
        ),
        page_body=(
            "# Alpha Topic\n\n"
            "- believe in have no temples. _(source.pdf (source-range-aaaa-00001))_\n"
            "- Untracked claim. _(source.pdf (source-range-bbbb-00002))_\n"
        ),
    )
    (wiki_dir / "source-alpha.md").write_text(render_page(page), encoding="utf-8")
    (ledger_dir / "claim-ledger.json").write_text(
        json.dumps(
            {
                "ledger": {
                    "entries": [
                        {
                            "source_range_id": "source-range-aaaa-00001",
                            "normalized_text": "believe in have no temples.",
                            "source_text": "believe in have no temples.",
                            "ledger_entry_kind": "claim",
                            "spatial_scope": {},
                            "claim_role_tags": [],
                            "structure_node_ids": ["node-alpha"],
                        }
                    ],
                    "technical_atoms": [],
                }
            }
        ),
        encoding="utf-8",
    )
    (ledger_dir / "document-structure.json").write_text(
        json.dumps(
            {
                "document_structure": {
                    "structure_nodes": [
                        {
                            "structure_node_id": "root",
                            "structure_node_kind": "root",
                            "heading_text": "",
                            "parent_structure_node_id": "",
                        },
                        {
                            "structure_node_id": "node-alpha",
                            "structure_node_kind": "section",
                            "heading_text": "Alpha Section",
                            "parent_structure_node_id": "root",
                        },
                    ],
                    "dispositions": [
                        {"source_range_id": "source-range-aaaa-00001", "source_order": 1}
                    ],
                }
            }
        ),
        encoding="utf-8",
    )

    report = audit_source_pages(tmp_path, "source", ledger_dir)

    assert report.page_count == 1
    assert report.cited_item_count == 2
    assert report.finding_counts["fragmentary-statement"] == 1
    assert report.finding_counts["missing-ledger-range"] == 1


def test_provenance_audit_accepts_projection_context_support(tmp_path) -> None:
    wiki_dir = tmp_path / "wiki"
    ledger_dir = tmp_path / "ledger"
    wiki_dir.mkdir()
    ledger_dir.mkdir()
    page = WikiPage(
        page_metadata=PageMetadata(
            page_id="source-alpha",
            page_kind="concept",
            page_family="topic-concept",
            summary="Alpha topic.",
            sources=("raw/source.pdf",),
        ),
        page_body=(
            "# Alpha Topic\n\n"
            "- Alpha is explained by a portable context block. "
            "_(source.pdf (source-range-aaaa-00001))_\n"
        ),
    )
    (wiki_dir / "source-alpha.md").write_text(render_page(page), encoding="utf-8")
    (ledger_dir / "claim-ledger.json").write_text(
        json.dumps({"ledger": {"entries": [], "technical_atoms": []}}),
        encoding="utf-8",
    )
    (ledger_dir / "document-structure.json").write_text(
        json.dumps(
            {
                "document_structure": {
                    "structure_nodes": [
                        {
                            "structure_node_id": "root",
                            "structure_node_kind": "root",
                            "heading_text": "",
                            "parent_structure_node_id": "",
                        }
                    ],
                    "dispositions": [
                        {"source_range_id": "source-range-aaaa-00001", "source_order": 1}
                    ],
                }
            }
        ),
        encoding="utf-8",
    )
    (ledger_dir / "source-coverage.json").write_text(
        json.dumps(
            {
                "source_coverage": {
                    "records": [
                        {
                            "source_range_ids": ["source-range-aaaa-00001"],
                            "coverage_kind": "segment",
                            "coverage_status": "covered",
                        }
                    ]
                }
            }
        ),
        encoding="utf-8",
    )
    (ledger_dir / "projection-context.json").write_text(
        json.dumps(
            {
                "projection_context": {
                    "evidence_blocks": [
                        {
                            "evidence_block_id": "block-alpha",
                            "source_range_id": "source-range-aaaa-00001",
                            "source_range_ids": ["source-range-aaaa-00001"],
                            "source_locator": "source.pdf",
                            "source_text": "Alpha is explained by a portable context block.",
                            "entry_ids": ["entry-alpha"],
                            "structure_node_ids": [],
                            "source_order": 1,
                            "section_label": "Alpha",
                        }
                    ],
                    "atom_frames": [],
                }
            }
        ),
        encoding="utf-8",
    )

    report = audit_source_pages(tmp_path, "source", ledger_dir)

    assert report.page_count == 1
    assert report.cited_item_count == 1
    assert "structure-only-range" not in report.finding_counts
