# Chat Phase 2: File Durable Synthesis

## Context & Problem

`llmwiki chat` is now the most natural way to work beside the wiki, but Phase 1
is read-only. `docs/llm-wiki.md` says valuable answers should compound into the
wiki, so chat needs a deliberate way to file durable synthesis without turning
the whole conversation history into evidence.

Pattern excerpts addressed from `docs/llm-wiki.md`:

- "the wiki is a persistent, compounding artifact"
- "The LLM makes edits based on our conversation"
- "good answers can be filed back into the wiki as new pages"

## Goals

- Let chat file the current answer or a requested synthesis into `wiki/`.
- Keep normal chat turns read-first and conservative.
- Preserve deterministic conversation windowing.
- Log filed chat syntheses as wiki operations.

## Non-Goals & Forbidden Approaches

Non-goals:

- No automatic promotion of whole conversations.
- No retrieval over chat history as evidence.
- No editing raw sources.
- No multi-user collaboration.

Forbidden approaches:

- Do not add ambient `write_page` to every chat turn without an explicit filing
  request.
- Do not treat prior chat answers as source evidence.
- Do not store durable wiki knowledge only in `harness/chat.db`.

## Requirements

- Chat supports a user-visible filing path, either a command or an explicit
  natural-language save request.
- A filed chat synthesis is written through `write_page` as category
  `synthesis`.
- The model must cite current wiki pages and raw sources, not chat history, for
  durable claims.
- The write path must preserve read-before-rewrite protection for existing
  pages.
- Filing appends an operation entry to `wiki/log.md`.

## Invariants

- Chat history remains conversation continuity, not the knowledge store.
- The wiki remains the durable compiled artifact.
- Every write still updates `index.md` deterministically.
- The model must re-read load-bearing wiki pages before filing.

## Proposed Architecture

```
+----------+       +-----------+       +---------------+       +--------+
| User     |------>| Chat REPL |------>| file workflow |------>| wiki/  |
+----------+       +-----------+       +---------------+       +--------+
                         |                    |
                         v                    v
                    chat.db window       write_page/log
```

Chat REPL detects filing intent. A dedicated filing workflow gets the current
question/answer plus a bounded wiki context and writes only through existing
wiki tools.

## Key Interactions

Explicit save command:

```
User -> chat: /file title
REPL -> store: load current turn
Model -> read_page/search_wiki: verify current evidence
Model -> write_page: synthesis page
Model -> finish_chat_file: report
Session -> log.md: append filing entry
```

Natural save request:

```
User -> chat: save that comparison
Model -> respond: asks for title/scope if ambiguous
User -> chat: confirms
REPL -> file workflow: same write path
```

Rewrite existing synthesis:

```
Model -> read_page: existing synthesis
Model -> write_page: replacement carrying forward kept content
```

## Data Model

- No change to chat turn storage.
- Filed synthesis pages use the existing `WikiPage` model.
- Log subject format: `chat-file | <page-name>` or equivalent stable operation
  label chosen during implementation.

## APIs / Interfaces

- `llmwiki chat` gains a filing interface.
- Implemented as `/file <page-name> [scope]`, which files the latest completed
  chat answer into a dedicated `chat-file` workflow.
- Filing workflow exposes `search_wiki`, `read_index`, `read_page`,
  `write_page`, and a terminal finish tool.
- The file workflow receives the current turn text and selected prior Q/A pairs
  as context, but those pairs are not source citations.

## Behavior & Domain Rules

- Filing is opt-in per answer.
- A durable synthesis must cite wiki/raw evidence.
- If current wiki evidence is insufficient, the filed page must say so or the
  model must decline to file.
- `write_page.sources` is raw-source metadata. The chat filing write gate
  rejects wiki page slugs in `sources`; wiki pages must be cited in the body
  with `[[page-name]]`.

Examples:

- User asks for a comparison, then `/file array-vs-linked-lists` -> writes a
  synthesis page citing pages it re-read.
- User says "remember this whole session" -> model declines and asks which
  specific synthesis is worth filing.
- Prior answer cited a page that has since changed -> filing re-reads the page
  and uses current content.

## Acceptance Criteria

- Tests prove chat can file a new synthesis page through the dedicated path.
- Tests prove existing-page filing requires `read_page` before rewrite.
- Tests prove chat history text alone is not accepted as a raw/source citation.
- Tests prove filing updates `index.md` and appends `log.md`.
- Existing read-only chat tests still pass for ordinary turns.

## Cross-Cutting Concerns

Observability: filed chat runs write transcripts like other workflows, tagged so
the page write can be traced to the chat turn.

Live verification note: the first smoke run successfully wrote a page but put
wiki page names in `sources`. The implementation now rejects that shape and the
second smoke run produced a synthesis with `sources: raw/javascriptallonge.pdf`,
body citations, an index entry, and a `chat-file` log entry.

## Reference Implementations

- Current chat design: `docs/2026-06-12-persistent-chat-design.md`.
- Chat REPL: `harness/src/llmwiki/runtime/chat_repl.py`.
- Query write-back pattern: `harness/src/llmwiki/workflows/definitions.py`.
- Read-before-rewrite guard: `harness/src/llmwiki/workflows/tools.py`.

## Alternatives Considered

- Keep chat permanently read-only - rejected because it misses the pattern's
  compounding-query loop.
- Auto-summarize conversations into wiki pages - rejected because it promotes
  exploratory chatter.
- Let chat use `write_page` on every turn - rejected because accidental writes
  become too easy.

## Halt Conditions

- If filing requires treating chat history as source evidence, stop and ask.
- If UX cannot distinguish ordinary chat from filing intent, stop and design the
  command surface first.
