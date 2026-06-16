"""Page-name policies that keep source namespaces coherent."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NameCollision:
    requested: str
    existing: str
    namespace: str
    canonical_leaf: str

    def render_for_tool(self) -> str:
        return (
            f"New page '{self.requested}' conflicts with existing same-namespace "
            f"page '{self.existing}' after singular/plural normalization. "
            f"Read and update '{self.existing}' if it is the same topic, or "
            "choose a descriptive role suffix if it is different, such as "
            f"'{self.namespace}-{self.canonical_leaf}-concept', "
            f"'{self.namespace}-{self.canonical_leaf}-rules', "
            f"'{self.namespace}-{self.canonical_leaf}-spell', or "
            f"'{self.namespace}-{self.canonical_leaf}-monster'."
        )


def singular_plural_collision(
    requested: str,
    existing_names: set[str],
    *,
    namespace: str | None,
) -> NameCollision | None:
    if namespace is None:
        return None
    requested_leaf = _namespace_leaf(requested, namespace)
    if requested_leaf is None:
        return None
    requested_canonical = singularize_slug(requested_leaf)
    for existing in sorted(existing_names):
        if existing == requested:
            continue
        existing_leaf = _namespace_leaf(existing, namespace)
        if existing_leaf is None:
            continue
        if existing_leaf == requested_leaf:
            continue
        if singularize_slug(existing_leaf) == requested_canonical:
            return NameCollision(
                requested=requested,
                existing=existing,
                namespace=namespace,
                canonical_leaf=requested_canonical,
            )
    return None


def singularize_slug(slug: str) -> str:
    parts = slug.split("-")
    if not parts:
        return slug
    parts[-1] = _singularize_word(parts[-1])
    return "-".join(parts)


def _namespace_leaf(name: str, namespace: str) -> str | None:
    if name == namespace:
        return ""
    prefix = f"{namespace}-"
    if not name.startswith(prefix):
        return None
    return name.removeprefix(prefix)


def _singularize_word(word: str) -> str:
    if len(word) <= 3:
        return word
    if word.endswith("ies") and len(word) > 4:
        return word[:-3] + "y"
    if word.endswith(("sses", "shes", "ches", "xes", "zes")):
        return word[:-2]
    if word.endswith("s") and not word.endswith(("ss", "us")):
        return word[:-1]
    return word
