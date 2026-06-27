from __future__ import annotations

from dataclasses import dataclass

import pytest

from llmwiki.domain.ledger.canonical import to_jsonable


@dataclass(frozen=True)
class TinyRecord:
    name: str
    value: int


@dataclass
class RecursiveRecord:
    name: str
    child: RecursiveRecord | None = None


def test_to_jsonable_serializes_repeated_dataclasses() -> None:
    records = tuple(TinyRecord(f"record-{index}", index) for index in range(20))

    assert to_jsonable(records)[0] == {"name": "record-0", "value": 0}


def test_to_jsonable_rejects_recursive_dataclass() -> None:
    record = RecursiveRecord("root")
    record.child = record

    with pytest.raises(TypeError):
        to_jsonable(record)
