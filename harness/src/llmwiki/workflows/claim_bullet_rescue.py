"""Small-model argument rescue for source-summary claim bullets."""

from __future__ import annotations


def rescue_claim_bullet(item: object) -> object:
    if isinstance(item, str):
        return {"bullet_text": item, "covered_source_claims": []}
    if not isinstance(item, dict):
        return item
    if "bullet_text" in item and "covered_source_claims" in item:
        return item
    bullet_text = _first_string(item, "bullet_text", "text", "claim", "statement", "summary")
    if not bullet_text:
        return item
    claim_id = _first_string(item, "source_claim_id", "claim_id", "id")
    covered = item.get("covered_source_claims", [])
    if not covered and claim_id:
        covered = [claim_id]
    return {"bullet_text": bullet_text, "covered_source_claims": covered}


def _first_string(data: dict[object, object], *keys: str) -> str:
    for key in keys:
        value = data.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""
