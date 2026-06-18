"""Wiki page model: naming, categories, and frontmatter rendering/parsing.

Frontmatter is composed here from explicit fields — the model never writes
it directly (see SCHEMA.md, "Page conventions").
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import PurePosixPath

PAGE_CATEGORIES = ("source", "entity", "concept", "synthesis")

_SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
_FRONTMATTER_DELIM = "---"


class PageError(ValueError):
    """Invalid page data; message is safe to feed back to the model."""


def slugify(text: str) -> str:
    """Derive a valid page-name slug from arbitrary text (e.g. a filename stem)."""
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    if not slug:
        raise PageError(f"Cannot derive a page name from {text!r}.")
    return slug


def validate_page_name(name: str) -> str:
    if not _SLUG_RE.match(name):
        raise PageError(
            f"Invalid page name {name!r}: use a kebab-case slug "
            "(lowercase letters, digits, hyphens), e.g. 'bronze-age-collapse'."
        )
    return name


def validate_category(category: str) -> str:
    if category not in PAGE_CATEGORIES:
        raise PageError(
            f"Invalid category {category!r}: must be one of {', '.join(PAGE_CATEGORIES)}."
        )
    return category


def validate_summary(summary: str) -> str:
    cleaned = " ".join(summary.split())
    if not cleaned:
        raise PageError("Summary must be a non-empty single line.")
    return cleaned


@dataclass(frozen=True)
class PageMetadata:
    """Stable identity and queryable fields for a wiki page."""

    page_id: str
    page_kind: str
    summary: str
    sources: tuple[str, ...] = field(default=())
    updated: str = ""

    def __post_init__(self) -> None:
        validate_page_name(self.page_id)
        validate_category(self.page_kind)
        object.__setattr__(self, "summary", validate_summary(self.summary))


@dataclass(frozen=True)
class WikiStructure:
    """Path projection for the current wiki."""

    structure_id: str
    path_template: str

    def render_path(self, metadata: PageMetadata) -> PurePosixPath:
        path_text = self.path_template.format(page_id=metadata.page_id)
        path = PurePosixPath(path_text)
        if path.is_absolute() or ".." in path.parts or path.suffix != ".md":
            raise PageError(f"Invalid rendered page path {path_text!r}.")
        return path


LOCAL_FLAT_STRUCTURE = WikiStructure(
    structure_id="local-flat",
    path_template="{page_id}.md",
)


@dataclass(frozen=True)
class WikiPage:
    """A wiki page as explicit state; rendering is derived, never stored."""

    name: str
    category: str
    summary: str
    body: str
    sources: tuple[str, ...] = field(default=())
    updated: str = ""  # ISO date, supplied by the orchestrator

    def __post_init__(self) -> None:
        validate_page_name(self.name)
        validate_category(self.category)
        object.__setattr__(self, "summary", validate_summary(self.summary))

    @property
    def page_metadata(self) -> PageMetadata:
        return PageMetadata(
            page_id=self.name,
            page_kind=self.category,
            summary=self.summary,
            sources=self.sources,
            updated=self.updated,
        )

    def page_path(self, structure: WikiStructure = LOCAL_FLAT_STRUCTURE) -> PurePosixPath:
        return structure.render_path(self.page_metadata)

    @classmethod
    def from_metadata(cls, metadata: PageMetadata, body: str) -> WikiPage:
        return cls(
            name=metadata.page_id,
            category=metadata.page_kind,
            summary=metadata.summary,
            body=body,
            sources=metadata.sources,
            updated=metadata.updated,
        )


def render_page(page: WikiPage) -> str:
    lines = [
        _FRONTMATTER_DELIM,
        f"category: {page.category}",
        f"summary: {page.summary}",
    ]
    if page.sources:
        lines.append(f"sources: {', '.join(page.sources)}")
    if page.updated:
        lines.append(f"updated: {page.updated}")
    lines.append(_FRONTMATTER_DELIM)
    return "\n".join(lines) + "\n\n" + page.body.strip() + "\n"


def parse_page(name: str, text: str) -> WikiPage:
    """Parse a rendered page back into the model. Inverse of render_page."""
    lines = text.splitlines()
    if not lines or lines[0] != _FRONTMATTER_DELIM:
        raise PageError(f"Page {name!r} has no frontmatter block.")
    fields: dict[str, str] = {}
    body_start = 0
    for i, line in enumerate(lines[1:], start=1):
        if line == _FRONTMATTER_DELIM:
            body_start = i + 1
            break
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    else:
        raise PageError(f"Page {name!r} frontmatter is unterminated.")
    sources = tuple(s.strip() for s in fields.get("sources", "").split(",") if s.strip())
    return WikiPage(
        name=name,
        category=fields.get("category", ""),
        summary=fields.get("summary", ""),
        body="\n".join(lines[body_start:]).strip(),
        sources=sources,
        updated=fields.get("updated", ""),
    )
