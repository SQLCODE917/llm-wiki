"""Source-neutral identity names for materialized table atoms."""

from __future__ import annotations

import re

from llmwiki.domain.ledger.atoms import TablePayload
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode

_TABLE_VERB = r"shows|lists|gives|provides|contains|summarizes|describes"
_LEADING_WORDS = frozenset({"a", "an", "the", "this", "that", "these", "those", "following"})
_TRAILING_WORDS = frozenset({"table"})
_TABLE_REFERENCE_VERBS = frozenset(_TABLE_VERB.split("|"))
_TABLE_REFERENCE_BOUNDARIES = frozenset(
    {"see", "consult", "using", "use", "from", "in", "on", *_LEADING_WORDS}
)
_MAX_FORWARD_CUE_NODES = 256
_MAX_FORWARD_CUE_TABLE_ATOMS = 64
_MAX_TABLE_NAME_CHARS = 240
_MAX_TABLE_NAME_TOKENS = 32
_MAX_TABLE_REFERENCE_CHARS = 2_000
_EXPLICIT_FORWARD_REFERENCE = re.compile(
    r"\b(?:table\s+(?:below|following|that follows)|following\s+[^.]{0,80}\s+table)\b",
    re.IGNORECASE,
)


def table_identity_names(
    ledger: ClaimLedger, structure: DocumentStructure | None = None
) -> tuple[str, ...]:
    """All source-derived names attached to materialized table atoms."""
    names: list[str] = []
    for atom_names in table_identity_names_by_atom_id(ledger, structure).values():
        names.extend(atom_names)
    return tuple(dict.fromkeys(names))


def table_identity_names_by_atom_id(
    ledger: ClaimLedger, structure: DocumentStructure | None = None
) -> dict[str, tuple[str, ...]]:
    """Table atom id to source-derived names: captions, headings, and table cues."""
    node_headings = _structure_node_headings(structure)
    atom_node_ids = _table_atom_node_ids(ledger)
    inferred_names = _table_names_from_forward_cues(ledger, structure)
    forward_targets = _table_forward_targets_by_atom_id(ledger, structure)
    names_by_atom: dict[str, tuple[str, ...]] = {}
    for atom in ledger.technical_atoms:
        if atom.technical_atom_kind != "table" or not isinstance(atom.payload, TablePayload):
            continue
        heading_names = tuple(
            heading
            for node_id in atom_node_ids.get(atom.technical_atom_id, ())
            if (heading := node_headings.get(node_id, ""))
        )
        names = _normalized_names(
            (
                atom.payload.caption,
                *raw_table_caption_lines(atom.payload),
                *heading_names,
                *inferred_names.get(atom.source_range_id, ()),
                *_target_node_names(forward_targets.get(atom.technical_atom_id, ())),
            )
        )
        if names:
            names_by_atom[atom.technical_atom_id] = names
    return names_by_atom


def table_structure_node_ids_by_atom_id(ledger: ClaimLedger) -> dict[str, tuple[str, ...]]:
    return _table_atom_node_ids(ledger)


def table_forward_target_node_ids_by_atom_id(
    ledger: ClaimLedger, structure: DocumentStructure | None
) -> dict[str, tuple[str, ...]]:
    return {
        atom_id: tuple(node.structure_node_id for node in nodes)
        for atom_id, nodes in _table_forward_targets_by_atom_id(ledger, structure).items()
    }


def raw_table_caption_lines(payload: TablePayload) -> tuple[str, ...]:
    return tuple(
        line
        for line in payload.raw_table_text.splitlines()[:3]
        if _table_caption_body(line.strip()) is not None
    )


def named_table_references(text: object) -> tuple[str, ...]:
    text = _bounded_reference(text)
    if "table of contents" in text.lower():
        return ()
    refs: list[str] = []
    words = _normalized_table_words(text)
    for index, word in enumerate(words):
        if word != "table":
            continue
        next_word = words[index + 1] if index + 1 < len(words) else ""
        if next_word in _TABLE_REFERENCE_VERBS or index > 0:
            name = _table_reference_name_before(words, index)
            if name:
                refs.append(name)
    return tuple(dict.fromkeys(refs))


def normalize_table_name(text: str) -> str:
    text = _bounded_name(text)
    if caption_body := _table_caption_body(text):
        text = caption_body
    words = list(_normalized_table_words(text))
    while words and words[0] in _LEADING_WORDS:
        words.pop(0)
    while words and words[-1] in _TRAILING_WORDS:
        words.pop()
    return " ".join(words[:8])


def has_matching_table_name(reference: str, table_names: tuple[str, ...]) -> bool:
    reference = _bounded_name(reference)
    reference_tokens = _match_tokens(reference)
    reference_alpha = _alphabetic_tokens(reference)
    for name in table_names:
        name = _bounded_name(name)
        name_alpha = _alphabetic_tokens(name)
        if not reference_alpha or not name_alpha or not reference_alpha.intersection(name_alpha):
            continue
        if reference == name or reference in name or name in reference:
            return True
        name_tokens = _match_tokens(name)
        if (
            reference_tokens
            and name_tokens
            and (reference_tokens.issubset(name_tokens) or name_tokens.issubset(reference_tokens))
        ):
            return True
    return False


def explicit_forward_reference(text: object) -> bool:
    return bool(_EXPLICIT_FORWARD_REFERENCE.search(_bounded_reference(text)))


def _normalized_names(candidates: tuple[str, ...]) -> tuple[str, ...]:
    names = [name for candidate in candidates if (name := normalize_table_name(candidate))]
    return tuple(dict.fromkeys(names))


def _source_order(structure: DocumentStructure | None) -> dict[str, int]:
    if structure is None:
        return {}
    orders: dict[str, int] = {}
    for disposition in structure.dispositions:
        if (order := _coerced_source_order(disposition.source_order)) is not None:
            orders[disposition.source_range_id] = order
    return orders


def _structure_node_headings(structure: DocumentStructure | None) -> dict[str, str]:
    if structure is None:
        return {}
    headings: dict[str, str] = {}
    for node in structure.structure_nodes:
        if (
            node.structure_node_kind == "root"
            or node.heading_text.lower().endswith(".pdf")
            or _generic_table_heading_cue(node.heading_text)
        ):
            continue
        name = normalize_table_name(node.heading_text)
        if name:
            headings[node.structure_node_id] = name
    return headings


def _table_atom_node_ids(ledger: ClaimLedger) -> dict[str, tuple[str, ...]]:
    nodes: dict[str, tuple[str, ...]] = {}
    for entry in ledger.entries:
        if entry.ledger_entry_kind != "technical-atom" or entry.technical_atom_kind != "table":
            continue
        if entry.technical_atom_id:
            nodes[entry.technical_atom_id] = entry.structure_node_ids
    return nodes


def _table_names_from_forward_cues(
    ledger: ClaimLedger, structure: DocumentStructure | None
) -> dict[str, tuple[str, ...]]:
    if structure is None:
        return {}
    table_atom_count = sum(
        1
        for atom in ledger.technical_atoms
        if atom.technical_atom_kind == "table" and isinstance(atom.payload, TablePayload)
    )
    if (
        len(structure.structure_nodes) > _MAX_FORWARD_CUE_NODES
        or table_atom_count > _MAX_FORWARD_CUE_TABLE_ATOMS
    ):
        return {}
    source_order = _source_order(structure)
    nodes = tuple(
        sorted(
            (node for node in structure.structure_nodes if _node_source_order(node) is not None),
            key=lambda node: _node_source_order(node) or 0,
        )
    )
    inferred: dict[str, tuple[str, ...]] = {}
    for atom in ledger.technical_atoms:
        if atom.technical_atom_kind != "table" or not isinstance(atom.payload, TablePayload):
            continue
        table_order = source_order.get(atom.source_range_id)
        if table_order is None:
            continue
        cue = _nearest_forward_table_cue(nodes, table_order)
        if cue is None:
            continue
        names = _cue_section_names(nodes, cue, structure)
        if names:
            inferred[atom.source_range_id] = names
    return inferred


def _table_forward_targets_by_atom_id(
    ledger: ClaimLedger, structure: DocumentStructure | None
) -> dict[str, tuple[StructureNode, ...]]:
    if structure is None:
        return {}
    table_atom_count = sum(
        1
        for atom in ledger.technical_atoms
        if atom.technical_atom_kind == "table" and isinstance(atom.payload, TablePayload)
    )
    if (
        len(structure.structure_nodes) > _MAX_FORWARD_CUE_NODES
        or table_atom_count > _MAX_FORWARD_CUE_TABLE_ATOMS
    ):
        return {}
    source_order = _source_order(structure)
    nodes = tuple(
        sorted(
            (node for node in structure.structure_nodes if _node_source_order(node) is not None),
            key=lambda node: _node_source_order(node) or 0,
        )
    )
    targets: dict[str, tuple[StructureNode, ...]] = {}
    for atom in ledger.technical_atoms:
        if atom.technical_atom_kind != "table" or not isinstance(atom.payload, TablePayload):
            continue
        table_order = source_order.get(atom.source_range_id)
        if table_order is None:
            continue
        cue = _nearest_forward_table_cue(nodes, table_order)
        if cue is None:
            continue
        target_nodes = _cue_section_nodes(nodes, cue, structure)
        if target_nodes:
            targets[atom.technical_atom_id] = target_nodes
    return targets


def _nearest_forward_table_cue(
    nodes: tuple[StructureNode, ...], table_order: int
) -> StructureNode | None:
    cues = [
        node
        for node in nodes
        if (order := _node_source_order(node)) is not None
        and order < table_order
        and table_order - order <= 32
        and _generic_table_heading_cue(node.heading_text)
    ]
    return max(cues, key=lambda node: _node_source_order(node) or 0, default=None)


def _cue_section_names(
    nodes: tuple[StructureNode, ...], cue: StructureNode, structure: DocumentStructure
) -> tuple[str, ...]:
    names: list[str] = []
    parent = structure.node(cue.parent_structure_node_id) if cue.parent_structure_node_id else None
    if parent is not None:
        names.extend(_named_heading(parent.heading_text))
    for node in sorted(
        (
            node
            for node in nodes
            if (node_order := _node_source_order(node)) is not None
            and (cue_order := _node_source_order(cue)) is not None
            and node_order < cue_order
        ),
        key=lambda node: _node_source_order(node) or 0,
        reverse=True,
    ):
        if name := _named_heading(node.heading_text):
            names.extend(name)
            break
    return tuple(dict.fromkeys(names))


def _cue_section_nodes(
    nodes: tuple[StructureNode, ...], cue: StructureNode, structure: DocumentStructure
) -> tuple[StructureNode, ...]:
    targets: list[StructureNode] = []
    parent = structure.node(cue.parent_structure_node_id) if cue.parent_structure_node_id else None
    if parent is not None and _named_heading(parent.heading_text):
        targets.append(parent)
    for node in sorted(
        (
            node
            for node in nodes
            if (node_order := _node_source_order(node)) is not None
            and (cue_order := _node_source_order(cue)) is not None
            and node_order < cue_order
        ),
        key=lambda node: _node_source_order(node) or 0,
        reverse=True,
    ):
        if _named_heading(node.heading_text):
            targets.append(node)
            break
    return tuple(dict.fromkeys(targets))


def _target_node_names(nodes: tuple[StructureNode, ...]) -> tuple[str, ...]:
    names: list[str] = []
    for node in nodes:
        names.extend(_named_heading(node.heading_text))
    return tuple(dict.fromkeys(names))


def _node_source_order(node: StructureNode) -> int | None:
    return _coerced_source_order(node.source_order)


def _coerced_source_order(value: object) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, str) and value.strip().isdigit():
        return int(value.strip())
    return None


def _named_heading(text: str) -> tuple[str, ...]:
    if not text or _generic_table_heading_cue(text) or text.lower().endswith(".pdf"):
        return ()
    name = normalize_table_name(text)
    return (name,) if name else ()


def _generic_table_heading_cue(text: str) -> bool:
    normalized = " ".join(_bounded_reference(text).lower().split())
    return explicit_forward_reference(normalized) and not named_table_references(normalized)


def _match_tokens(name: str) -> set[str]:
    stopwords = {"table", "tables"}
    return {
        _singularize(word)
        for word in name.split()[:_MAX_TABLE_NAME_TOKENS]
        if word not in stopwords and not _roll_notation(word)
    }


def _alphabetic_tokens(name: str) -> set[str]:
    return {token for token in _match_tokens(name) if any(char.isalpha() for char in token)}


def _bounded_name(name: object) -> str:
    return (name if isinstance(name, str) else str(name))[:_MAX_TABLE_NAME_CHARS]


def _bounded_reference(text: object) -> str:
    return (text if isinstance(text, str) else str(text))[:_MAX_TABLE_REFERENCE_CHARS]


def _table_caption_body(text: str) -> str | None:
    stripped = _bounded_name(text).strip()
    if _ascii_startswith(stripped, "tab."):
        body = stripped[4:]
    elif _ascii_startswith(stripped, "table"):
        body = stripped[5:]
    else:
        return None
    return body.lstrip(" \t-:.0123456789") or None


def _normalized_table_words(text: str) -> tuple[str, ...]:
    words: list[str] = []
    current: list[str] = []
    for char in _bounded_name(text):
        normalized = _ascii_word_char(char)
        if normalized:
            current.append(normalized)
        elif current:
            words.append("".join(current))
            current = []
    if current:
        words.append("".join(current))
    return tuple(words)


def _table_reference_name_before(words: tuple[str, ...], table_index: int) -> str:
    start = max(0, table_index - 8)
    for index in range(table_index - 1, start - 1, -1):
        if words[index] in _TABLE_REFERENCE_BOUNDARIES:
            start = index + 1
            break
    name = normalize_table_name(" ".join(words[start:table_index]))
    return "" if name in _TABLE_REFERENCE_BOUNDARIES else name


def _ascii_startswith(text: str, prefix: str) -> bool:
    return _ascii_lower_prefix(text, len(prefix)) == prefix


def _ascii_lower_prefix(text: str, length: int) -> str:
    return "".join(_ascii_lower_char(char) for char in text[:length])


def _ascii_word_char(char: str) -> str:
    if len(char) != 1:
        return ""
    codepoint = ord(char)
    if 48 <= codepoint <= 57 or 97 <= codepoint <= 122:
        return char
    if 65 <= codepoint <= 90:
        return chr(codepoint + 32)
    return ""


def _ascii_lower_char(char: str) -> str:
    if len(char) != 1:
        return " "
    codepoint = ord(char)
    if 65 <= codepoint <= 90:
        return chr(codepoint + 32)
    if codepoint < 128:
        return char
    return " "


def _singularize(word: str) -> str:
    if len(word) > 3 and word.endswith("ies"):
        return f"{word[:-3]}y"
    if len(word) > 3 and word.endswith("s"):
        return word[:-1]
    return word


def _roll_notation(word: str) -> bool:
    if word.isdigit():
        return True
    if word.startswith("d") and word[1:].isdigit():
        return True
    left, separator, right = word.partition("d")
    return bool(separator and left.isdigit() and right.isdigit())
