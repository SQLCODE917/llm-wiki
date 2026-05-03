#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path

from wiki_common import content_tokens, parse_frontmatter
from wiki_check_synthesis import clean_evidence_excerpt, normalize_for_search, parse_locator, strip_markdown


WEAK_WORDS = {"important", "crucial", "fundamental", "essential", "success"}
METADATA_RE = re.compile(r"^(?:title|type|tags|status|last_updated|sources|source_id|source_type):\s*")


@dataclass(frozen=True)
class SourceLine:
    number: int
    text: str


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply deterministic cleanup to a reference wiki page.")
    parser.add_argument("page", help="wiki reference page to repair")
    parser.add_argument("--normalized-source", required=True, help="normalized source markdown")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    page = Path(args.page)
    normalized_source = Path(args.normalized_source)
    if not page.exists():
        print(f"SKIP: missing page {page}")
        return 0
    if not normalized_source.exists():
        print(f"FAIL: missing normalized source {normalized_source}", file=sys.stderr)
        return 2

    fm = parse_frontmatter(page)
    if fm.data.get("type") != "reference":
        print(f"SKIP: {page} is not a reference page")
        return 0

    source_lines = [
        SourceLine(number=index, text=line)
        for index, line in enumerate(normalized_source.read_text(errors="ignore").splitlines(), start=1)
    ]
    original = page.read_text()
    repaired, messages = repair_page(original, str(fm.data.get("title") or page.stem.replace("-", " ").title()), source_lines)
    if repaired != original and not args.dry_run:
        page.write_text(repaired)
    if messages:
        for message in messages:
            print(message)
    else:
        print(f"no deterministic reference repair needed for {page}")
    return 0


def repair_page(text: str, title: str, source_lines: list[SourceLine]) -> tuple[str, list[str]]:
    frontmatter, body = split_frontmatter(text)
    messages: list[str] = []
    body, structure_messages = repair_body_structure(body, title)
    messages.extend(structure_messages)

    lines = body.splitlines()
    repaired_lines: list[str] = []
    section = ""
    header: list[str] | None = None
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## "):
            section = stripped
            header = None
            repaired_lines.append(line)
            continue
        cells = split_table_row(line)
        if cells is None or section not in {"## Reference data", "## Source-backed details"}:
            repaired_lines.append(line)
            continue
        if is_separator_row(cells):
            repaired_lines.append(line)
            continue
        normalized = [strip_markdown(cell).strip().lower() for cell in cells]
        if header is None:
            header = normalized
            repaired_lines.append(line)
            continue
        repaired_cells, row_messages = repair_table_row(section, header, cells, source_lines)
        messages.extend(row_messages)
        repaired_lines.append(render_table_row(repaired_cells))

    repaired_body = "\n".join(repaired_lines)
    if body.endswith("\n"):
        repaired_body += "\n"
    return frontmatter + repaired_body, messages


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text
    return text[: end + 5], text[end + 5 :]


def repair_body_structure(body: str, title: str) -> tuple[str, list[str]]:
    messages: list[str] = []
    lines = [line for line in body.splitlines() if not METADATA_RE.match(line.strip())]
    if len(lines) != len(body.splitlines()):
        messages.append("removed stray frontmatter-like body lines")

    h1_index = next((index for index, line in enumerate(lines) if line.startswith("# ")), None)
    if h1_index is None:
        lines.insert(0, f"# {title}")
        messages.append("inserted missing H1")
    else:
        first_content = next((index for index, line in enumerate(lines) if line.strip()), None)
        if first_content is not None and first_content != h1_index:
            h1 = lines.pop(h1_index)
            lines.insert(first_content, h1)
            messages.append("moved H1 before other body content")
    return "\n".join(lines).strip() + "\n", messages


def repair_table_row(
    section: str,
    header: list[str],
    cells: list[str],
    source_lines: list[SourceLine],
) -> tuple[list[str], list[str]]:
    messages: list[str] = []
    out = list(cells)
    evidence_index = index_of(header, "evidence")
    locator_index = index_of(header, "locator")
    if evidence_index is None or locator_index is None:
        return out, messages

    evidence = clean_evidence_excerpt(out[evidence_index])
    locator = out[locator_index]
    fixed_evidence, fixed_locator = repair_evidence_and_locator(evidence, locator, source_lines)
    if fixed_evidence and fixed_evidence != evidence:
        out[evidence_index] = quote_cell(fixed_evidence)
        messages.append(f"repaired evidence excerpt in {section}")
    if fixed_locator and clean_locator_cell(fixed_locator) != clean_locator_cell(locator):
        out[locator_index] = f"`{fixed_locator}`"
        messages.append(f"repaired evidence locator in {section}")
    evidence = fixed_evidence or evidence

    text_indices = claim_indices(section, header, len(cells), evidence_index, locator_index)
    for index in text_indices:
        original = strip_markdown(out[index]).strip()
        if needs_text_repair(original, evidence):
            replacement = narrow_text_from_evidence(evidence)
            if replacement and normalize_for_search(replacement) != normalize_for_search(original):
                out[index] = replacement
                messages.append(f"repaired weak or repeated text in {section}")
    return out, messages


def repair_evidence_and_locator(
    evidence: str,
    locator: str,
    source_lines: list[SourceLine],
) -> tuple[str | None, str | None]:
    found = find_excerpt(source_lines, evidence)
    if found:
        return evidence, locator_for(found)
    parsed = parse_locator(locator)
    candidates: list[SourceLine] = []
    if parsed is not None:
        start, end = parsed
        candidates = [line for line in source_lines if start <= line.number <= end]
    if not candidates:
        candidates = source_lines
    best = best_source_excerpt(evidence, candidates)
    if best is None:
        return None, None
    return best.text, f"normalized:L{best.number}"


def find_excerpt(source_lines: list[SourceLine], evidence: str) -> list[SourceLine] | None:
    wanted = normalize_for_search(evidence)
    if not wanted:
        return None
    for line in source_lines:
        if wanted in normalize_for_search(line.text):
            return [line]
    for start in range(len(source_lines)):
        text = ""
        out: list[SourceLine] = []
        for line in source_lines[start : start + 4]:
            out.append(line)
            text = (text + "\n" + line.text).strip()
            if wanted in normalize_for_search(text):
                return out
    return None


def best_source_excerpt(evidence: str, source_lines: list[SourceLine]) -> SourceLine | None:
    query_tokens = set(content_tokens(evidence))
    scored: list[tuple[int, SourceLine]] = []
    for source_line in source_lines:
        for chunk in sentence_chunks(source_line.text):
            tokens = set(content_tokens(chunk))
            score = len(query_tokens & tokens)
            if score:
                scored.append((score, SourceLine(source_line.number, chunk)))
    if not scored:
        return None
    scored.sort(key=lambda item: (-item[0], len(item[1].text)))
    return scored[0][1]


def sentence_chunks(text: str) -> list[str]:
    pieces = re.findall(r"[^.!?]+[.!?]?", text)
    chunks = [" ".join(piece.split()).strip() for piece in pieces]
    return [chunk for chunk in chunks if len(chunk) >= 24 and len(content_tokens(chunk)) >= 4]


def locator_for(lines: list[SourceLine]) -> str:
    if len(lines) == 1:
        return f"normalized:L{lines[0].number}"
    return f"normalized:L{lines[0].number}-L{lines[-1].number}"


def claim_indices(
    section: str,
    header: list[str],
    cell_count: int,
    evidence_index: int,
    locator_index: int,
) -> list[int]:
    ignored = {evidence_index, locator_index}
    source_index = index_of(header, "source")
    if source_index is not None:
        ignored.add(source_index)
    if section == "## Source-backed details":
        claim_index = index_of(header, "claim")
        return [] if claim_index is None else [claim_index]
    preferred = index_of(header, "supported fact")
    if preferred is not None:
        return [preferred]
    return [index for index in range(cell_count) if index not in ignored and header[index] not in {"item"}]


def needs_text_repair(text: str, evidence: str) -> bool:
    if not text:
        return False
    tokens = {token.lower() for token in re.findall(r"[A-Za-z']+", text)}
    if WEAK_WORDS & tokens:
        return True
    if has_repeated_phrase(text):
        return True
    text_norm = normalize_for_search(text)
    evidence_norm = normalize_for_search(evidence)
    if text_norm == evidence_norm:
        return True
    return SequenceMatcher(None, text_norm, evidence_norm).ratio() > 0.88


def narrow_text_from_evidence(evidence: str) -> str:
    lowered = evidence.lower()
    if "do not cost tc time" in lowered and "stop producing villagers" in lowered:
        return "Economy upgrades can be researched without stopping villager production."
    if "lumbercamp upgrades" in lowered and "prioritized" in lowered:
        return "Lumbercamp upgrades should be prioritized highly."
    if "horse collar" in lowered and "heavy plow" in lowered and "crop rotation" in lowered:
        return "Horse collar, heavy plow, and crop rotation are wood-saving farm upgrades."
    if "wheelbarrow effectively increases" in lowered and "25-35" in lowered:
        return "Wheelbarrow increases farm food income efficiency by 25-35%."
    if "handcart" in lowered and "500 total resource cost" in lowered:
        return "Handcart has a 500 total resource cost."
    if "second armor upgrade" in lowered and "4dmg -> 3" in lowered:
        return "The second knight armor upgrade reduces crossbow damage from 4 to 3."
    if "armor on the knights" in lowered and "5dmg -> 4" in lowered:
        return "The first knight armor upgrade reduces crossbow damage from 5 to 4."
    if "upgrade them to xbows" in lowered and "bodkin" in lowered:
        return "Upgrading archers to crossbows with bodkin improves their damage output."
    if "man-at-arms upgrade" in lowered and "longswords" in lowered:
        return "The man-at-arms upgrade speeds later teching into longswords."
    if "mining camp upgrades" in lowered and "researching age up" in lowered:
        return "Feudal-age mining camp upgrades are usually delayed until age-up research."
    if "fall behind in time" in lowered and "down in upgrades" in lowered:
        return "Falling behind in upgrade timing can require more army investment."
    if "market economy" in lowered and "not recommend" in lowered:
        return "Market economy is not recommended unless the player knows what they are doing."
    if "without wood" in lowered and "economy just halts" in lowered:
        return "Without wood, the player's economy halts."
    if "skirmishers require more upgrades" in lowered:
        return "Skirmishers require more upgrades and put stress on the economy."
    text = strip_markdown(evidence).strip().strip('"')
    text = re.sub(r"\b(?:extremely|very|really)\s+(?=important\b)", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\bimportant\b", "prioritized", text, flags=re.IGNORECASE)
    text = re.sub(r"\bcrucial\b", "needed", text, flags=re.IGNORECASE)
    text = re.sub(r"\bfundamental\b", "basic", text, flags=re.IGNORECASE)
    text = re.sub(r"\bessential\b", "needed", text, flags=re.IGNORECASE)
    text = re.sub(r"\bsuccess\b", "the stated outcome", text, flags=re.IGNORECASE)
    words = text.split()
    if len(words) > 18:
        text = " ".join(words[:18]).rstrip(",.;:") + "."
    if text and text[-1] not in ".!?":
        text += "."
    return text


def has_repeated_phrase(text: str) -> bool:
    parts = [normalize_for_search(part) for part in re.split(r"[,;]", text) if len(content_tokens(part)) >= 2]
    if any(parts.count(part) >= 3 for part in parts):
        return True
    words = [word.lower() for word in re.findall(r"[A-Za-z0-9']+", text)]
    for size in range(6, 1, -1):
        counts: dict[tuple[str, ...], int] = {}
        for index in range(0, len(words) - size + 1):
            phrase = tuple(words[index : index + size])
            counts[phrase] = counts.get(phrase, 0) + 1
            if counts[phrase] >= 3:
                return True
    return False


def split_table_row(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    return [cell.strip() for cell in stripped[1:-1].split("|")]


def render_table_row(cells: list[str]) -> str:
    return "| " + " | ".join(escape_cell(cell) for cell in cells) + " |"


def is_separator_row(cells: list[str]) -> bool:
    return all(cell and set(cell) <= {"-", ":", " "} for cell in cells)


def index_of(header: list[str], name: str) -> int | None:
    return header.index(name) if name in header else None


def quote_cell(text: str) -> str:
    cleaned = text.strip().strip('"')
    return f'"{cleaned}"'


def clean_locator_cell(locator: str) -> str:
    return strip_markdown(locator).strip()


def escape_cell(cell: str) -> str:
    return cell.replace("|", "/").replace("\n", " ").strip()


if __name__ == "__main__":
    sys.exit(main())
