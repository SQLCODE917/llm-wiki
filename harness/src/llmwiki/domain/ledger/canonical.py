"""Canonical serialization, deterministic ids, and artifact fingerprints.

Portable artifacts must serialize identically on any llm-wiki implementation,
so every artifact body is canonical JSON: sorted object keys, tuples rendered
as arrays, and no run timestamps. ``ArtifactFingerprint`` values hash the
domain-relevant contents, excluding the artifact's own fingerprint field and
any id field whose deterministic input is that fingerprint.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import fields, is_dataclass
from enum import Enum
from typing import Any


def to_jsonable(obj: Any) -> Any:
    """Recursively convert dataclasses/tuples/enums to JSON-safe values.

    Object key ordering is deferred to ``json.dumps(sort_keys=True)`` so the
    output is independent of dataclass field declaration order.
    """
    if obj is None or isinstance(obj, (str, int, float, bool)):
        return obj
    if isinstance(obj, Enum):
        return obj.value
    if is_dataclass(obj) and not isinstance(obj, type):
        return {f.name: to_jsonable(getattr(obj, f.name)) for f in fields(obj)}
    if isinstance(obj, dict):
        return {str(key): to_jsonable(value) for key, value in obj.items()}
    if isinstance(obj, (tuple, list, set, frozenset)):
        items = [to_jsonable(item) for item in obj]
        if isinstance(obj, (set, frozenset)):
            items.sort(key=_sort_key)
        return items
    raise TypeError(f"Cannot canonicalize {type(obj)!r}")


def canonical_json(obj: Any, *, indent: int | None = None) -> str:
    """Deterministic JSON text for an artifact body or any jsonable object."""
    separators = (",", ": ") if indent is not None else (",", ":")
    return json.dumps(
        to_jsonable(obj),
        sort_keys=True,
        ensure_ascii=False,
        indent=indent,
        separators=separators,
    )


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def short_digest(text: str, length: int = 16) -> str:
    return digest(text)[:length]


def content_fingerprint(obj: Any) -> str:
    """Fingerprint of a whole jsonable object (no key exclusions)."""
    return short_digest(canonical_json(obj))


def artifact_fingerprint(obj: Any, *, exclude: tuple[str, ...] = ()) -> str:
    """Fingerprint of an artifact body, dropping the excluded top-level keys.

    Excluded keys are the artifact's own typed fingerprint field and any id
    field whose deterministic input is that fingerprint.
    """
    body = to_jsonable(obj)
    if not isinstance(body, dict):
        raise TypeError("artifact_fingerprint requires a mapping-shaped artifact body")
    reduced = {key: value for key, value in body.items() if key not in exclude}
    return short_digest(
        json.dumps(reduced, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    )


def deterministic_id(prefix: str, *parts: str, length: int = 16) -> str:
    """Stable id ``<prefix>-<digest>`` derived from the joined parts."""
    return f"{prefix}-{short_digest(chr(31).join(parts), length)}"


def _sort_key(value: Any) -> str:
    return json.dumps(to_jsonable(value), sort_keys=True, ensure_ascii=False)
