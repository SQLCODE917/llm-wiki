"""Dataclass serialization utilities using cattrs.

This module provides a shared cattrs converter for all wiki dataclasses,
reducing boilerplate from manual to_dict()/from_dict() methods.

Usage:
    from wiki_core.serde import structure, unstructure
    
    # Serialize to dict
    data = unstructure(claim)
    
    # Deserialize from dict  
    claim = structure(data, Claim)
    
Migration guide:
    Classes using manual to_dict()/from_dict() can be migrated incrementally.
    
    1. Remove to_dict() method, replace with:
       def to_dict(self) -> dict:
           return unstructure(self)
    
    2. Remove from_dict() classmethod, replace with:
       @classmethod
       def from_dict(cls, d: dict) -> Self:
           return structure(d, cls)
    
    3. Once all callers use structure/unstructure directly, remove the methods.
    
Special cases:
    - Private fields (starting with _): excluded from serialization
    - Optional nested dataclasses: handled automatically
    - Enums: converted to/from their string values
    - datetime: converted to/from ISO format strings
"""
from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any, TypeVar

import cattrs
from cattrs.gen import make_dict_structure_fn, make_dict_unstructure_fn, override

# Global converter instance - configure once, use everywhere
_converter = cattrs.Converter()

T = TypeVar("T")


def _configure_converter(converter: cattrs.Converter) -> None:
    """Configure the converter with common hooks."""

    # Handle datetime <-> ISO string
    converter.register_unstructure_hook(
        datetime,
        lambda dt: dt.isoformat() if dt else None
    )
    converter.register_structure_hook(
        datetime,
        lambda s, _: datetime.fromisoformat(s) if s else None
    )

    # Handle Enum <-> string value
    converter.register_unstructure_hook(
        Enum,
        lambda e: e.value if e else None
    )


_configure_converter(_converter)


def structure(data: dict[str, Any], cls: type[T]) -> T:
    """Convert a dictionary to a dataclass instance.

    Args:
        data: Dictionary with field values
        cls: Target dataclass type

    Returns:
        Instance of cls populated from data

    Example:
        >>> @dataclass
        ... class Person:
        ...     name: str
        ...     age: int
        >>> structure({"name": "Alice", "age": 30}, Person)
        Person(name='Alice', age=30)
    """
    return _converter.structure(data, cls)


def unstructure(obj: Any) -> dict[str, Any]:
    """Convert a dataclass instance to a dictionary.

    Args:
        obj: Dataclass instance

    Returns:
        Dictionary with field values (private fields excluded)

    Example:
        >>> @dataclass
        ... class Person:
        ...     name: str
        ...     age: int
        >>> unstructure(Person("Alice", 30))
        {'name': 'Alice', 'age': 30}
    """
    return _converter.unstructure(obj)


def register_private_fields_hook(cls: type) -> None:
    """Register hooks to exclude private fields from serialization.

    Call this for dataclasses that have private fields (starting with _)
    that should not be serialized.

    Args:
        cls: Dataclass type with private fields

    Example:
        >>> @dataclass
        ... class Config:
        ...     name: str
        ...     _internal: int = 0
        >>> register_private_fields_hook(Config)
        >>> unstructure(Config("test", _internal=42))
        {'name': 'test'}
    """
    import dataclasses

    # Get all field names
    all_fields = {f.name for f in dataclasses.fields(cls)}
    # Identify private fields
    private_fields = {f for f in all_fields if f.startswith("_")}

    if not private_fields:
        return

    # Create unstructure hook that omits private fields
    overrides = {f: override(omit=True) for f in private_fields}
    unstruct_fn = make_dict_unstructure_fn(cls, _converter, **overrides)
    _converter.register_unstructure_hook(cls, unstruct_fn)

    # Create structure hook that provides defaults for private fields
    # (they won't be in the dict, so need defaults)
    struct_fn = make_dict_structure_fn(cls, _converter)
    _converter.register_structure_hook(cls, struct_fn)


def get_converter() -> cattrs.Converter:
    """Get the shared converter for advanced customization.

    Use this when you need to register custom hooks for specific types.
    """
    return _converter
