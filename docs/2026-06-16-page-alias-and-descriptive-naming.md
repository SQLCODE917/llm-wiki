# Page Alias and Descriptive Naming

## Context & Problem

The Sword World ingest showed source-prefixed names are necessary but not
sufficient: the model created same-namespace singular/plural siblings such as
`daemon` and `daemons`, and ambiguous names such as `wraith` where one source
section meant a spell-created state and another meant a monster entry. The
LLM-Wiki pattern expects the wiki to be maintained over time, but ingest should
prevent obvious naming drift before lint has to repair it.

Pattern excerpts addressed from `docs/llm-wiki.md`:

- "the LLM incrementally builds and maintains a persistent wiki"
- "updating cross-references, keeping summaries current"
- "the exact directory structure ... will depend on your domain"

## Goals

- Merge known duplicate Sword World pages without hand-editing `index.md`.
- Rename ambiguous pages to descriptive, role-bearing names.
- Add a profile-configured guard that prevents new singular/plural sibling pages
  within the same source namespace.
- Keep the guard broad enough for multiple books in the same category, e.g.
  JavaScript/TypeScript/React books and Sword World rulebook/GM guide/setting
  booklet.

## Non-Goals & Forbidden Approaches

Non-goals:

- No folder migration or multi-root wiki layout.
- No automatic semantic merge of arbitrary near-duplicates.
- No language-wide stemming or lemmatization engine.
- No rollback/reingest of already useful Sword World pages.

Forbidden approaches:

- Do not hard-code Sword World terms such as `wraith` or `daemon` in Python.
- Do not let the model decide whether `index.md` or inbound links were updated.
- Do not allow a merge to delete a page while inbound links still point to it.
- Do not force descriptive-name guards on profiles that did not opt in.

## Requirements

- The store exposes a deterministic merge/rename operation for content pages.
- Merge/rename rewrites all `[[old-page]]` inbound links to `[[new-page]]`.
- Merge/rename removes the old page file and stale index entry.
- Merge/rename appends an operation log entry through the harness.
- Profile TOML supports an opt-in naming rule that blocks new
  singular/plural sibling pages under the active source namespace.
- When blocked, the model receives corrective guidance to read/update the
  existing page or choose a descriptive role suffix.
- Existing no-profile ingest behavior remains unchanged.

## Invariants

- `raw/` remains immutable.
- Wiki content pages are still Markdown files with harness-composed
  frontmatter.
- Page names remain globally unique kebab-case slugs.
- `index.md`, `log.md`, graph export, candidates, and hub key lists remain
  harness-owned.
- Existing pages may still be updated after `read_page`; the new guard applies
  only to new page creation.

## Proposed Architecture

```
+----------------+      +----------------+      +-------------------+
| profile config |----->| naming policy  |----->| write_page guard  |
+----------------+      +----------------+      +-------------------+
        |                        |
        v                        v
+----------------+      +----------------+
| curator CLI    |----->| wiki store     |
+----------------+      +----------------+
```

Profile config declares whether naming collision prevention is active. The
naming policy detects same-namespace singular/plural siblings. The `write_page`
guard rejects new colliding pages with corrective guidance. The curator CLI uses
store merge/rename operations to repair existing pages deterministically.

## Key Interactions

Profiled ingest collision:

```
Model -> write_page: new page source-daemon
write_page -> naming policy: compare against source-daemons
naming policy -> write_page: collision
write_page -> Model: update existing page or choose descriptive suffix
```

Curator merge:

```
User -> CLI: pages merge old new --summary ...
CLI -> store: merge/rename page
store -> wiki: write new page, rewrite inbound links, remove old file
store -> log: append maintenance entry
```

## Data Model

`IngestProfile` gains a naming-policy flag:

- `naming.prevent_singular_plural_siblings`: boolean, default false.

The policy operates on source-prefixed page names by removing the active source
namespace prefix and comparing a conservative singularized leaf slug.

## APIs / Interfaces

- `profiles/ingest/*.toml`: optional `[naming]` table.
- `llmwiki pages rename <old> <new> --summary <text>`: rename a page while
  preserving links and index consistency.
- `llmwiki pages merge <old> <target> --summary <text>`: remove a duplicate
  page, keep the target page, and rewrite inbound links to the target.

## Behavior & Domain Rules

- If `source-daemons` exists, creating `source-daemon` is blocked unless the
  model is updating an existing page it has read.
- `source-daemon-lord` is allowed because it is descriptively distinct.
- If no singular/plural sibling exists, `source-wraith` is allowed; profile
  prompt guidance still asks for descriptive suffixes when a source uses the
  same noun for different roles.

## Acceptance Criteria

- Tests prove profile loading accepts and renders the naming flag.
- Tests prove same-namespace singular/plural new-page creation is blocked only
  when a selected profile opts in.
- Tests prove descriptive suffixes are allowed.
- Tests prove merge/rename rewrites inbound links, removes the old file, and
  removes stale index entries.
- Existing no-profile tests continue to pass.
- The known Sword World `daemon`/`daemons` duplicate is merged.
- The known Sword World `wraith`/`wraiths` ambiguity is renamed to descriptive
  pages.

## Cross-Cutting Concerns

Observability: merge/rename writes a maintenance log entry so page history is
discoverable from `wiki/log.md`.

Error handling: collisions are corrective tool errors. Merge/rename refuses
missing pages, reserved names, invalid slugs, and attempts to overwrite a
different target without explicit merge semantics.

## Reference Implementations

- Store/index coupling: `harness/src/llmwiki/store/wiki_store.py`.
- Link extraction: `harness/src/llmwiki/domain/links.py`.
- Profile loading: `harness/src/llmwiki/domain/ingest_profiles.py`.
- CLI deterministic maintenance commands: `harness/src/llmwiki/cli.py`.

## Implementation Notes

- Added `llmwiki pages rename` and `llmwiki pages merge` as deterministic
  maintenance operations. They update page files, inbound `[[links]]`,
  `index.md`, and `log.md` without asking the model to report success.
- Extended link parsing to treat `[[page|label]]` aliases as graph links to
  `page`, so rename/merge can preserve aliases without hiding edges from
  lint, graph export, salience, semantic lint, or contradiction selection.
- Added the profile data flag `naming.prevent_singular_plural_siblings` and
  enabled it for `profiles/ingest/rulebook.toml`.
- Added prompt/schema guidance that asks profiled ingests to use descriptive
  role suffixes when the same noun can name rules, spells, monsters, items,
  or lore.
- Applied the cleanup to the known Sword World ambiguities: wraith spell effect
  versus monster, daemon duplicate drift, ability-score duplicate drift,
  playable-race duplicate drift, and magical-item rules versus examples.
- Verified the focused behavior with:
  `uv run pytest harness/tests/test_ingest_profiles.py harness/tests/test_store.py harness/tests/test_domain.py`.

## Alternatives Considered

- Roll back and reingest Sword World: rejected because most pages are useful and
  the problem is local maintenance debt plus a preventable naming guard.
- Prompt-only naming instruction: rejected because prompt-only namespace rules
  already proved insufficient during live ingest.
- Folder grouping now: rejected as a separate schema migration.

## Halt Conditions

- If implementation would change wiki link syntax away from `[[page-name]]`,
  stop and ask.
- If implementation would require moving pages into folders, stop and split a
  folder-layout TDD.
