"""Domain objects that describe wiki operations without filesystem effects."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import PurePosixPath

from llmwiki.domain.pages import LOCAL_FLAT_STRUCTURE, WikiPage, WikiStructure
from llmwiki.domain.schema import PAGE_KINDS, PAGE_METADATA_FIELDS


def _source_format(source_locator: str) -> str:
    suffix = PurePosixPath(source_locator).suffix.lower().lstrip(".")
    if suffix == "md":
        return "markdown"
    return suffix or "unknown"


@dataclass(frozen=True)
class RawSource:
    source_locator: str
    source_format: str
    source_content: str = ""
    source_assets: tuple[str, ...] = ()
    immutable: bool = True

    @classmethod
    def from_locator(cls, source_locator: str) -> RawSource:
        return cls(source_locator=source_locator, source_format=_source_format(source_locator))

    @classmethod
    def from_source_path(cls, source_path: str) -> RawSource:
        return cls.from_locator(source_path)

    @property
    def source_path(self) -> str:
        return self.source_locator


@dataclass(frozen=True)
class SourceBundle:
    raw_sources: tuple[RawSource, ...]

    def __post_init__(self) -> None:
        if not self.raw_sources:
            raise ValueError("SourceBundle requires at least one RawSource.")

    @classmethod
    def one(cls, raw_source: RawSource) -> SourceBundle:
        return cls(raw_sources=(raw_source,))


@dataclass(frozen=True)
class Schema:
    schema_id: str = "local-llm-wiki"
    page_kinds: tuple[str, ...] = PAGE_KINDS
    page_metadata_fields: tuple[str, ...] = PAGE_METADATA_FIELDS


@dataclass(frozen=True)
class IngestRun:
    source_bundle: SourceBundle
    wiki_structure: WikiStructure = LOCAL_FLAT_STRUCTURE
    schema: Schema = field(default_factory=Schema)
    ingest_topology: str = "serial"
    wiki_pages: tuple[WikiPage, ...] = ()

    def __post_init__(self) -> None:
        if self.ingest_topology != "serial":
            raise ValueError("Local LLM-Wiki supports only serial IngestRun topology.")
