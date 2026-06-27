"""Wiki page model: metadata, structure projection, and frontmatter."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import PurePosixPath

from llmwiki.domain.schema import PAGE_KINDS

_SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
_FRONTMATTER_DELIM = "---"


class PageError(ValueError):
    """Invalid page data; message is safe to feed back to the model."""


def slugify(text: str) -> str:
    """Derive a valid page_id slug from arbitrary text."""
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    if not slug:
        raise PageError(f"Cannot derive a page_id from {text!r}.")
    return slug


def validate_page_id(page_id: str) -> str:
    if not _SLUG_RE.match(page_id):
        raise PageError(
            f"Invalid page_id {page_id!r}: use a kebab-case slug "
            "(lowercase letters, digits, hyphens), e.g. 'bronze-age-collapse'."
        )
    return page_id


def validate_page_kind(page_kind: str) -> str:
    if page_kind not in PAGE_KINDS:
        raise PageError(f"Invalid page_kind {page_kind!r}: must be one of {', '.join(PAGE_KINDS)}.")
    return page_kind


def validate_summary(summary: str) -> str:
    cleaned = " ".join(summary.split())
    if not cleaned:
        raise PageError("Summary must be a non-empty single line.")
    return cleaned


@dataclass(frozen=True)
class PageKind:
    """A page role declared by Schema."""

    page_kind: str

    def __post_init__(self) -> None:
        validate_page_kind(self.page_kind)


@dataclass(frozen=True)
class PageMetadata:
    """The stable identity and queryable fields for a WikiPage."""

    page_id: str
    page_kind: str
    summary: str
    sources: tuple[str, ...] = field(default=())
    updated: str = ""
    domain: str = ""
    category_path: str = ""
    project_id: str = ""
    source_id: str = ""
    tags: tuple[str, ...] = field(default=())
    aliases: tuple[str, ...] = field(default=())
    projection_coverage_pointer: str = ""

    def __post_init__(self) -> None:
        validate_page_id(self.page_id)
        validate_page_kind(self.page_kind)
        object.__setattr__(self, "summary", validate_summary(self.summary))


@dataclass(frozen=True)
class PathTemplate:
    """Renders one PagePath from one PageMetadata object."""

    template_text: str = "{PageId}.md"
    match_page_kinds: tuple[str, ...] = PAGE_KINDS
    required_page_metadata_fields: tuple[str, ...] = ("PageId",)

    def render(self, metadata: PageMetadata) -> PurePosixPath:
        if metadata.page_kind not in self.match_page_kinds:
            raise PageError(f"PageKind {metadata.page_kind!r} does not match this PathTemplate.")
        fields = dict(
            PageId=metadata.page_id,
            PageKind=metadata.page_kind,
            Summary=metadata.summary,
            Sources=",".join(metadata.sources),
            Updated=metadata.updated,
            Domain=metadata.domain,
            CategoryPath=metadata.category_path,
            ProjectId=metadata.project_id,
            SourceId=metadata.source_id,
        )
        for field_name in self.required_page_metadata_fields:
            if field_name not in fields:
                raise PageError(f"Unknown required PageMetadata field {field_name!r}.")
            if not fields[field_name]:
                raise PageError(f"PageMetadata field {field_name!r} is required.")
        path_text = self.template_text.format(**fields)
        path = PurePosixPath(path_text)
        if path.is_absolute() or ".." in path.parts or not path.name.endswith(".md"):
            raise PageError(f"Invalid rendered PagePath {path_text!r}.")
        return path


@dataclass(frozen=True)
class WikiStructure:
    """The active path-template set for a Wiki."""

    structure_id: str
    default_path_template: PathTemplate
    path_templates: tuple[PathTemplate, ...] = field(default=())

    def render_path(self, metadata: PageMetadata) -> PurePosixPath:
        for template in self.path_templates:
            if metadata.page_kind in template.match_page_kinds:
                return template.render(metadata)
        return self.default_path_template.render(metadata)


LOCAL_FLAT_STRUCTURE = WikiStructure(
    structure_id="local-flat",
    default_path_template=PathTemplate(),
)


@dataclass(frozen=True)
class WikiPage:
    """A wiki page is one PageMetadata object plus one page_body."""

    page_metadata: PageMetadata
    page_body: str

    @property
    def page_id(self) -> str:
        return self.page_metadata.page_id

    @property
    def page_kind(self) -> str:
        return self.page_metadata.page_kind

    @property
    def summary(self) -> str:
        return self.page_metadata.summary

    @property
    def sources(self) -> tuple[str, ...]:
        return self.page_metadata.sources

    @property
    def updated(self) -> str:
        return self.page_metadata.updated

    def page_path(self, structure: WikiStructure = LOCAL_FLAT_STRUCTURE) -> PurePosixPath:
        return structure.render_path(self.page_metadata)

    @classmethod
    def from_metadata(cls, metadata: PageMetadata, page_body: str) -> WikiPage:
        return cls(page_metadata=metadata, page_body=page_body)


@dataclass(frozen=True)
class DomainFrontmatter:
    """The on-disk frontmatter projection of one PageMetadata object."""

    page_metadata: PageMetadata

    def render(self) -> str:
        metadata = self.page_metadata
        lines = [
            _FRONTMATTER_DELIM,
            f"page_id: {metadata.page_id}",
            f"page_kind: {metadata.page_kind}",
            f"summary: {metadata.summary}",
        ]
        if metadata.sources:
            lines.append(f"sources: {', '.join(metadata.sources)}")
        if metadata.updated:
            lines.append(f"updated: {metadata.updated}")
        if metadata.domain:
            lines.append(f"domain: {metadata.domain}")
        if metadata.category_path:
            lines.append(f"category_path: {metadata.category_path}")
        if metadata.project_id:
            lines.append(f"project_id: {metadata.project_id}")
        if metadata.source_id:
            lines.append(f"source_id: {metadata.source_id}")
        if metadata.tags:
            lines.append(f"tags: {', '.join(metadata.tags)}")
        if metadata.aliases:
            lines.append(f"aliases: {', '.join(metadata.aliases)}")
        if metadata.projection_coverage_pointer:
            lines.append(f"projection_coverage: {metadata.projection_coverage_pointer}")
        lines.append(_FRONTMATTER_DELIM)
        return "\n".join(lines)


def render_page(page: WikiPage) -> str:
    frontmatter = DomainFrontmatter(page.page_metadata).render()
    return frontmatter + "\n\n" + page.page_body.strip() + "\n"


def parse_page(text: str) -> WikiPage:
    """Parse a rendered page back into the model. Inverse of render_page."""
    lines = text.splitlines()
    if not lines or lines[0] != _FRONTMATTER_DELIM:
        raise PageError("WikiPage has no DomainFrontmatter block.")
    fields: dict[str, str] = {}
    body_start = 0
    for i, line in enumerate(lines[1:], start=1):
        if line == _FRONTMATTER_DELIM:
            body_start = i + 1
            break
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    else:
        raise PageError("WikiPage DomainFrontmatter is unterminated.")
    metadata = PageMetadata(
        page_id=fields.get("page_id", ""),
        page_kind=fields.get("page_kind", ""),
        summary=fields.get("summary", ""),
        sources=_split_frontmatter_list(fields.get("sources", "")),
        updated=fields.get("updated", ""),
        domain=fields.get("domain", ""),
        category_path=fields.get("category_path", ""),
        project_id=fields.get("project_id", ""),
        source_id=fields.get("source_id", ""),
        tags=_split_frontmatter_list(fields.get("tags", "")),
        aliases=_split_frontmatter_list(fields.get("aliases", "")),
        projection_coverage_pointer=fields.get("projection_coverage", ""),
    )
    return WikiPage(page_metadata=metadata, page_body="\n".join(lines[body_start:]).strip())


def _split_frontmatter_list(value: str) -> tuple[str, ...]:
    return tuple(item.strip() for item in value.split(",") if item.strip())
