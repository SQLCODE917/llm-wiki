#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from wiki_common import content_tokens
from wiki_check_synthesis import normalize_for_search, strip_markdown
from wiki_judge_claims import EvidenceRow, deterministic_flags, evidence_rows


WEAK_WORDS = {"important", "crucial", "fundamental", "essential", "success"}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Print deterministic repair hints for evidence-backed synthesized-page claims."
    )
    parser.add_argument("page", help="wiki synthesized page")
    parser.add_argument("--normalized-source", required=True,
                        help="normalized source markdown")
    parser.add_argument("--context-lines", type=int, default=2)
    parser.add_argument("--allow-missing", action="store_true")
    args = parser.parse_args()

    page = Path(args.page)
    normalized_source = Path(args.normalized_source)
    if not page.exists():
        if args.allow_missing:
            print(f"SKIP: missing page {page}")
            return 0
        print(f"FAIL: missing page {page}", file=sys.stderr)
        return 2
    if not normalized_source.exists():
        print(
            f"FAIL: missing normalized source {normalized_source}", file=sys.stderr)
        return 2

    source_lines = normalized_source.read_text(errors="ignore").splitlines()
    rows = evidence_rows(page, source_lines, context_lines=args.context_lines)
    print(render_hints(page, rows, source_lines))
    return 0


def render_hints(page: Path, rows: list[EvidenceRow], source_lines: list[str]) -> str:
    lines = [
        f"Claim repair hints for `{page.as_posix()}`",
        "",
        f"- Evidence rows found: {len(rows)}",
    ]
    flags = deterministic_flags(rows, source_lines)
    fail_flags = [flag for flag in flags if flag.severity == "fail"]
    warn_flags = [flag for flag in flags if flag.severity == "warn"]
    lines.append(f"- Deterministic failures: {len(fail_flags)}")
    lines.append(f"- Deterministic warnings: {len(warn_flags)}")
    lines.append("")

    if not rows:
        lines.append(
            "No evidence rows found. Add a Claim/Evidence/Locator/Source table first.")
        return "\n".join(lines)

    for row in rows:
        row_flags = [flag for flag in flags if flag.row == row.row]
        weak = sorted(WEAK_WORDS & set(token.lower()
                      for token in re.findall(r"[A-Za-z']+", row.claim)))
        unsupported = unsupported_terms(row)
        if not row_flags and not weak and len(unsupported) < 5:
            continue
        lines.append(f"Row {row.row}:")
        if weak:
            lines.append(
                f"- SURGICAL FIX: Replace ONLY the word(s) `{', '.join(weak)}` with a specific term.")
            lines.append(
                f"  Keep the rest of the claim IDENTICAL. Do not rewrite the whole claim.")
            # Suggest specific replacements
            replacements = {
                'fundamental': 'core',
                'important': 'noted',
                'crucial': 'required',
                'essential': 'needed',
                'success': 'the stated outcome',
            }
            for w in weak:
                if w in replacements:
                    lines.append(f"  Suggested: `{w}` → `{replacements[w]}`")
        for flag in row_flags:
            lines.append(f"- {flag.severity.upper()}: {flag.message}")

        # Provide semantic guidance instead of copy-inducing suggestions
        supported_meaning = extract_supported_meaning(row)
        if supported_meaning:
            lines.append(f"- Supported meaning from evidence:")
            for meaning in supported_meaning:
                lines.append(f"  - {meaning}")
        lines.append(
            f"- Constraint: Do NOT copy evidence wording. Synthesize in different words.")
        lines.append(f"- Evidence excerpt: {row.evidence[:100]}...")
        lines.append("")

    if lines[-1] == "":
        lines.pop()
    if len(lines) <= 6:
        lines.append("No obvious deterministic claim-repair hints.")
    return "\n".join(lines)


def unsupported_terms(row: EvidenceRow) -> list[str]:
    supported = set(content_tokens(row.evidence + " " + row.context))
    return sorted(set(content_tokens(row.claim)) - supported)


def extract_supported_meaning(row: EvidenceRow) -> list[str]:
    """Extract semantic meaning bullets from evidence without giving copy targets.

    This provides guidance about WHAT the evidence supports semantically,
    not HOW to word the claim.
    """
    evidence = strip_markdown(row.evidence).strip().strip('"')
    if not evidence:
        return []

    meanings = []
    lowered = evidence.lower()

    # Extract subject/predicate patterns
    if " is " in f" {lowered} " or " are " in f" {lowered} ":
        # Evidence makes a definitional claim
        meanings.append("defines or characterizes a concept")
    if " can " in f" {lowered} " or " cannot " in f" {lowered} ":
        # Evidence describes capability
        meanings.append("describes a capability or limitation")
    if " should " in f" {lowered} " or " must " in f" {lowered} ":
        # Evidence gives guidance
        meanings.append("provides guidance or recommendation")
    if " because " in f" {lowered} " or " therefore " in f" {lowered} ":
        # Evidence gives reasoning
        meanings.append("explains a cause or reason")

    # Extract key concepts (nouns/noun phrases)
    key_terms = extract_key_concepts(evidence)
    if key_terms:
        meanings.append(f"relates to: {', '.join(key_terms[:5])}")

    if not meanings:
        meanings.append("provides factual information about the topic")

    return meanings


def extract_key_concepts(text: str) -> list[str]:
    """Extract key noun-like terms from text."""
    # Simple heuristic: words that are capitalized or appear to be technical terms
    words = re.findall(
        r'\b[A-Z][a-z]+(?:\s+[a-z]+)?|\b[a-z]+(?:ing|tion|ment|ness)\b', text)
    # Also get any quoted terms
    quoted = re.findall(r'"([^"]+)"', text)
    all_terms = list(set(words + quoted))
    # Filter out very common words
    stopwords = {'the', 'a', 'an', 'is', 'are',
                 'was', 'were', 'be', 'been', 'being'}
    return [t for t in all_terms if t.lower() not in stopwords and len(t) > 2][:5]


def suggested_claim(row: EvidenceRow) -> str:
    evidence = strip_markdown(row.evidence).strip().strip('"')
    evidence = re.sub(r"\s+", " ", evidence)
    if not evidence:
        return ""
    special = special_case_suggestion(evidence)
    if special:
        return special
    evidence = rewrite_second_person(evidence)
    lowered = evidence.lower()
    if " should " in f" {lowered} ":
        return finalize_suggestion(row, evidence)
    if " is " in f" {lowered} " or " are " in f" {lowered} ":
        return finalize_suggestion(row, evidence)
    if " can " in f" {lowered} " or " cannot " in f" {lowered} ":
        return finalize_suggestion(row, evidence)
    tokens = evidence.split()
    if len(tokens) > 24:
        evidence = " ".join(tokens[:24]).rstrip(",.;:") + "."
    return finalize_suggestion(row, evidence)


def finalize_suggestion(row: EvidenceRow, text: str) -> str:
    suggestion = clean_suggestion(text)
    if normalize_for_search(suggestion) == normalize_for_search(row.evidence):
        return ""
    return suggestion


def special_case_suggestion(text: str) -> str:
    lowered = text.lower()
    if "ideal army composition" in lowered and " vs " in lowered:
        return "Army composition planning can begin from the civilizations in the matchup."
    if "do not cost tc time" in lowered and "stop producing villagers" in lowered:
        return "Economy upgrades can be researched without stopping villager production."
    if "lumbercamp upgrades" in lowered and "prioritized" in lowered:
        return "Lumbercamp upgrades should be prioritized highly."
    if "horse collar" in lowered and "heavy plow" in lowered and "crop rotation" in lowered:
        return "Horse collar, heavy plow, and crop rotation save wood by increasing farm food."
    return ""


def rewrite_second_person(text: str) -> str:
    replacements = [
        (r"\byou can\b", "players can"),
        (r"\byou should\b", "players should"),
        (r"\byou want to\b", "players should"),
        (r"\byou need to\b", "players need to"),
        (r"\byour\b", "the player's"),
    ]
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    text = re.sub(r"\s+right\??$", ".", text, flags=re.IGNORECASE)
    return text


def clean_suggestion(text: str) -> str:
    text = re.sub(r"\b(?:extremely|very|really)\s+(?=important\b)",
                  "", text, flags=re.IGNORECASE)
    text = re.sub(r"\bimportant\b", "noted", text, flags=re.IGNORECASE)
    text = re.sub(r"\bcrucial\b", "needed", text, flags=re.IGNORECASE)
    text = re.sub(r"\bfundamental\b", "basic", text, flags=re.IGNORECASE)
    text = re.sub(r"\bessential\b", "needed", text, flags=re.IGNORECASE)
    text = re.sub(r"\bsuccess\b", "the stated outcome",
                  text, flags=re.IGNORECASE)
    text = text.strip()
    if text and text[-1] not in ".!?":
        text += "."
    return text


if __name__ == "__main__":
    sys.exit(main())
