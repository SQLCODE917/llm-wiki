"""Strict helpers for deterministic JSON artifact boundaries."""

from __future__ import annotations

from collections.abc import Iterable


def expect_object(value: object, field: str = "value") -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"{field} must be an object")
    return {str(key): item for key, item in value.items()}


def expect_array(value: object, field: str = "value") -> tuple[object, ...]:
    if not isinstance(value, list):
        raise ValueError(f"{field} must be an array")
    return tuple(value)


def expect_str(value: object, field: str = "value") -> str:
    if not isinstance(value, str):
        raise ValueError(f"{field} must be a string")
    return value


def expect_int(value: object, field: str = "value") -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{field} must be an integer")
    return value


def expect_float(value: object, field: str = "value") -> float:
    if isinstance(value, bool) or not isinstance(value, int | float):
        raise ValueError(f"{field} must be a number")
    return float(value)


def expect_literal[T](value: object, allowed: Iterable[T], field: str = "value") -> T:
    allowed_tuple = tuple(allowed)
    if value not in allowed_tuple:
        rendered = ", ".join(repr(item) for item in allowed_tuple)
        raise ValueError(f"{field} must be one of {rendered}")
    return value


def optional_object(value: object, field: str = "value") -> dict[str, object] | None:
    if value is None:
        return None
    return expect_object(value, field)
