"""Config-driven ingest profile loading and prompt composition."""

from __future__ import annotations

import re
import string
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from llmwiki.config import ConfigError
from llmwiki.domain.pages import slugify

type OverlayName = Literal["ingest", "pdf_map", "pdf_integrate"]

_ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
_ALLOWED_OVERLAYS: frozenset[str] = frozenset({"ingest", "pdf_map", "pdf_integrate"})
_ALLOWED_VARS: frozenset[str] = frozenset(
    {"source_path", "source_slug", "source_namespace", "profile_ids"}
)
_FORMATTER = string.Formatter()


@dataclass(frozen=True)
class IngestProfile:
    id: str
    enabled: bool
    description: str
    priority: int
    namespace_mode: str
    overlays: dict[OverlayName, str]


def load_ingest_profiles(directory: Path) -> tuple[IngestProfile, ...]:
    """Load all ingest profile TOML files in deterministic id order."""
    if not directory.exists():
        return ()
    if not directory.is_dir():
        raise ConfigError(f"Ingest profile path is not a directory: {directory}")
    profiles = tuple(_load_profile(path) for path in sorted(directory.glob("*.toml")))
    ids = [profile.id for profile in profiles]
    if len(ids) != len(set(ids)):
        raise ConfigError("Duplicate ingest profile ids found.")
    return tuple(sorted(profiles, key=lambda profile: profile.id))


def select_ingest_profiles(
    available: tuple[IngestProfile, ...], requested_ids: list[str] | tuple[str, ...]
) -> tuple[IngestProfile, ...]:
    """Select enabled profiles by id, sorted by priority then CLI order."""
    by_id = {profile.id: profile for profile in available}
    selected: list[tuple[int, IngestProfile]] = []
    seen: set[str] = set()
    for order, profile_id in enumerate(requested_ids):
        if profile_id in seen:
            continue
        seen.add(profile_id)
        profile = by_id.get(profile_id)
        if profile is None:
            valid = ", ".join(sorted(by_id)) or "none"
            raise ConfigError(f"Unknown ingest profile {profile_id!r}. Valid profiles: {valid}.")
        if not profile.enabled:
            raise ConfigError(f"Ingest profile {profile_id!r} is disabled.")
        selected.append((order, profile))
    selected.sort(key=lambda item: (item[1].priority, item[0]))
    return tuple(profile for _, profile in selected)


def compose_prompt(
    base_template: str,
    profiles: tuple[IngestProfile, ...],
    overlay_name: OverlayName,
    source_path: str,
) -> str:
    """Append rendered profile overlays to an existing prompt template."""
    if not profiles:
        return base_template
    context = _render_context(source_path, profiles)
    blocks = [
        f"Profile `{profile.id}`:\n{render_overlay(profile, overlay_name, context)}"
        for profile in profiles
        if profile.overlays.get(overlay_name, "").strip()
    ]
    if not blocks:
        return base_template
    guidance = "\n\n".join(blocks)
    return f"{base_template}\n\nAdditional ingest profile guidance:\n{guidance}"


def render_overlay(
    profile: IngestProfile, overlay_name: OverlayName, context: dict[str, str]
) -> str:
    overlay = profile.overlays.get(overlay_name, "")
    return overlay.format(**context).strip()


def render_profiles(profiles: tuple[IngestProfile, ...]) -> str:
    """Human-facing profile inventory for `llmwiki profiles`."""
    if not profiles:
        return "No ingest profiles found."
    lines = ["# Ingest Profiles", ""]
    for profile in profiles:
        status = "enabled" if profile.enabled else "disabled"
        lines.append(
            f"- {profile.id} [{status}, priority {profile.priority}] — "
            f"{profile.description}"
        )
    return "\n".join(lines)


def profile_summary(profiles: tuple[IngestProfile, ...]) -> str:
    if not profiles:
        return "none"
    return ", ".join(profile.id for profile in profiles)


def _load_profile(path: Path) -> IngestProfile:
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as exc:
        raise ConfigError(f"Invalid ingest profile TOML {path}: {exc}") from exc
    profile_id = _required_str(data, "id", path)
    if path.stem != profile_id:
        raise ConfigError(
            f"Ingest profile {path} has id {profile_id!r}, but filename stem is {path.stem!r}."
        )
    _validate_id(profile_id, path)
    enabled = _required_bool(data, "enabled", path)
    description = _required_str(data, "description", path)
    priority = _required_int(data, "priority", path)
    namespace = data.get("namespace")
    if not isinstance(namespace, dict):
        raise ConfigError(f"Ingest profile {profile_id!r} must define [namespace].")
    namespace_mode = namespace.get("mode")
    if namespace_mode != "source-slug":
        raise ConfigError(
            f"Ingest profile {profile_id!r} namespace.mode must be 'source-slug'."
        )
    overlays = _load_overlays(profile_id, data.get("overlays"))
    if not overlays:
        raise ConfigError(f"Ingest profile {profile_id!r} must define at least one overlay.")
    return IngestProfile(
        id=profile_id,
        enabled=enabled,
        description=description,
        priority=priority,
        namespace_mode=namespace_mode,
        overlays=overlays,
    )


def _load_overlays(profile_id: str, raw: object) -> dict[OverlayName, str]:
    if not isinstance(raw, dict):
        raise ConfigError(f"Ingest profile {profile_id!r} must define [overlays].")
    unknown = set(raw) - _ALLOWED_OVERLAYS
    if unknown:
        names = ", ".join(sorted(unknown))
        raise ConfigError(f"Ingest profile {profile_id!r} has unknown overlay(s): {names}.")
    overlays: dict[OverlayName, str] = {}
    for name, value in raw.items():
        if not isinstance(value, str):
            raise ConfigError(f"Ingest profile {profile_id!r} overlay {name!r} must be text.")
        _validate_overlay_vars(profile_id, name, value)
        overlays[name] = value
    return overlays


def _render_context(source_path: str, profiles: tuple[IngestProfile, ...]) -> dict[str, str]:
    source_slug = slugify(Path(source_path).stem)
    return {
        "source_path": source_path,
        "source_slug": source_slug,
        "source_namespace": source_slug,
        "profile_ids": ", ".join(profile.id for profile in profiles),
    }


def _validate_overlay_vars(profile_id: str, overlay_name: str, overlay: str) -> None:
    for _, field_name, _, _ in _FORMATTER.parse(overlay):
        if field_name is None:
            continue
        if field_name not in _ALLOWED_VARS:
            valid = ", ".join(sorted(_ALLOWED_VARS))
            raise ConfigError(
                f"Ingest profile {profile_id!r} overlay {overlay_name!r} references "
                f"unknown variable {field_name!r}. Valid variables: {valid}."
            )


def _validate_id(profile_id: str, path: Path) -> None:
    if not _ID_RE.match(profile_id):
        raise ConfigError(f"Ingest profile id in {path} must be kebab-case, got {profile_id!r}.")


def _required_str(data: dict[str, object], key: str, path: Path) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ConfigError(f"Ingest profile {path} must define non-empty string {key!r}.")
    return value.strip()


def _required_bool(data: dict[str, object], key: str, path: Path) -> bool:
    value = data.get(key)
    if not isinstance(value, bool):
        raise ConfigError(f"Ingest profile {path} must define boolean {key!r}.")
    return value


def _required_int(data: dict[str, object], key: str, path: Path) -> int:
    value = data.get(key)
    if not isinstance(value, int):
        raise ConfigError(f"Ingest profile {path} must define integer {key!r}.")
    return value
