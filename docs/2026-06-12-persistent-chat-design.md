# Persistent Chat over the Wiki — Design (Phase 1: read-only)

## Context & Problem

Every `llmwiki query` boots llama-server (~20–30 s for 8.4 GB of weights),
prefills the ~2.5K-token schema prompt, answers one question, and unloads
(open question #8). There is no way to ask a follow-up: each query starts
amnesiac. The pattern document describes the intended workflow as
conversational — the agent open beside Obsidian, edits flowing "based on
our conversation" — so the one-shot CLI is a bootstrapping artifact, not
the pattern. A 14B model adds a constraint cloud-model chat designs ignore:
the memory mechanism must not depend on the model compressing or curating
its own history.

## Goals

- `llmwiki chat`: load the model once; converse until exit. Both `/exit`
  and Ctrl-C unload the server gracefully.
- Follow-up questions work: each turn sees the recent conversation.
- **Conversations are a managed collection**: start new ones, list them,
  toggle between them mid-REPL, and resume old ones — including returning
  to an old conversation with new insight to suss out a statement of fact
  (which Phase 2 will make fileable on the spot).
- Conversations are preserved efficiently and verbatim, so richer chat
  features can be built on the store later **without conversation
  archaeology or restoration** (see Data Model, preservation guarantee).
- Phase 1 is **read-only**: the model answers from the wiki and the
  conversation only — no `write_page` tool in the chat workflow.
- `/ingest <file>` and `/lint` work inside chat as their own isolated
  workflow runs (unchanged semantics), reusing the warm server.
- Memory management is deterministic: no model-generated summaries, no
  model-curated history.
- Subsequent turns benefit from the server's prompt cache (shared system
  prefix prefilled once per session).

## Non-Goals

- **Writing back to the wiki from chat (Phase 2).** Filing syntheses,
  taking notes, page edits mid-conversation — deferred to keep scope down;
  the read-only workflow simply has no write tool.
- Rolling summaries or embedding retrieval over chat history (see
  Alternatives — wrong tools for this system).
- A daemon / server mode with detached lifecycle; the chat process *is*
  the lifecycle.
- Concurrent operations during a chat turn (no SlotWorker; one thing at a
  time).
- Cross-session knowledge transfer through the chat database — knowledge
  that should outlive a conversation belongs in the wiki (Phase 2's job).
- **Filing answers back into the wiki.** Sessions are a retained
  playground — expected to be mostly dead ends, red herrings, and
  inconsequential babble, and that's their job. The pattern doc's guidance
  for the valuable exceptions is per-ANSWER filing at the moment of
  creation ("good answers can be filed back into the wiki as new pages"),
  which is Phase 2: `write_page` returns to the chat workflow. There is no
  session-promotion feature, in this phase or any other.

## Requirements

- **Alignment (docs/llm-wiki.md)**: chat is the pattern's native
  interaction model; the wiki remains the only knowledge store — the chat
  database holds *conversation continuity*, never wiki content; answers
  worth keeping are explicitly out of scope until Phase 2 (the schema will
  tell the model to say so when asked to save something); `log.md` stays a
  chronology of operations (one entry per session, not per turn).
- **Model reality**: 16K context. Turn context must be budgeted
  deterministically; prior turns' tool results must not accumulate.
- **Determinism boundary**: history selection, token budgeting, and session
  bookkeeping are code; only answering is the model.
- **Durability**: a crash mid-session loses at most the in-flight turn;
  everything answered is already persisted.

## Proposed Architecture

A REPL owns the process: it boots the backend once, then loops — each user
line becomes one bounded workflow run (the same shape as every other
operation), seeded with a deterministically chosen window of past Q/A
pairs. Turns are persisted to a SQLite session store as they complete.
The key memory decision: **conversation = question/answer pairs; evidence
is re-fetched, never remembered.** Intermediate tool calls and page dumps
from prior turns are dropped from the seed — the model re-reads pages on
demand — so a long chat stays inside budget without any compression model
calls, and forge's transient-message pollution problem never arises.

```
+--------+  lines/commands  +-----------------+   one bounded run per turn
|  User  |----------------->|  Chat REPL      |------------------------+
| (tty)  |<--answers--------|  (owns process, |                        |
+--------+                  |  boots backend) |                        v
                            +---+--------+----+              +----------------+
                                |        |                   | forge Runner / |
                  window (Q/A pairs)   append turn           | Qwen3 workflows|
                                v        v                   +-------+--------+
                            +-----------------+   search_wiki        |
                            | Session store   |   read_page only     v
                            | (SQLite)        |              +----------------+
                            +-----------------+              | wiki/ (read)   |
                                                             | log.md (1/sess)|
                                                             +----------------+
```

- **Chat REPL** — reads lines; dispatches `/new`, `/sessions`, `/switch
  <id>`, `/ingest`, `/lint`, `/exit`; plain text → chat turn against the
  active conversation. Because no model state survives between turns (by
  design — the window is rebuilt every turn), switching conversations is
  just re-pointing the window builder at another session id: no reload,
  no reconstruction. SIGINT and `/exit` take the same graceful path
  (stamp activity, write the log entry, stop the server).
- **Session store** — SQLite at `harness/chat.db` (gitignored): sessions
  and turns. Append-only during a session; the window builder reads it.
- **Window builder (pure domain)** — given stored turns and a token
  budget, returns the most recent Q/A pairs that fit (~6K tokens),
  newest-first selection, chronological order in the seed.
- **Chat workflow (read-only)** — tools `search_wiki`, `read_index`,
  `read_page`, terminal `respond`; no required steps. Grounding is
  **provisioned, not enforced**: the orchestrator prepends the wiki index
  to a conversation's first message, so the opening answer starts from
  the catalog and drills into pages (the pattern doc's index-first
  navigation, implemented in code). REVISED during implementation: the
  original required-`search_wiki` guardrail was removed on live evidence
  — it interrupted a correct index-first flow ("what is this wiki
  about?"), forced a junk search, and the model answered from the junk;
  for a 14B, the last evidence in context wins.
- **forge Runner** — unchanged guardrail stack; multi-turn via the
  documented `initial_messages` seeding (system prompt + windowed pairs +
  new question).

## Key Interactions

One chat turn (turn N > 0):

```
User           REPL              Store              Runner/Qwen3
 |--question--->|                  |                     |
 |              |--load window---->|                     |
 |              |<--recent Q/A interleaved (fits budget)-|
 |              |--run(chat-wf, seed=[system, pairs, q])->|
 |              |                  |    search_wiki/read_page as needed
 |              |<-----------------+------respond(answer)-|
 |              |--append turn(q, answer, transcript)--->|
 |<--answer-----|                  |                     |
```

REPL lifecycle with conversation management (start, toggle, exit, resume):

```
User            REPL                    Backend/Store
 |--llmwiki chat-->|--boot server once------->|
 |                 |--create conversation---->| (or --resume: load one)
 |   ... turns ...|                           |
 |--/sessions----->|--list (first question, recency, turns)
 |--/switch <id>-->|--re-point window builder at <id>  (no reload)
 |--/new---------->|--create conversation---->|
 |   ... turns ...|                           |
 |--/exit or C-c-->|--append ONE log entry (chat | k turns, m conversations)
 |                 |--stop server (always: finally path)
```

## Data Model

- **Session** — id (timestamp-based), `created_at`, `last_active_at`
  (stamped per turn; a conversation is never "closed", only dormant —
  resumable forever), turn count. Listings label each session by its first
  question plus recency, so toggling is human-navigable.
- **Turn** — session id, index, question text, answer text, transcript
  path, token estimate, timestamp. Q/A text only — no tool calls, no page
  contents.
- **Preservation guarantee** (the no-archaeology rule): stored questions
  and answers are **verbatim and never truncated** — any length trimming
  happens only in the derived window seed. Answers carry their `[[page]]`
  / `(raw/...)` citations as written; turns are ordered, timestamped, and
  keep their transcript paths; the schema is stamped
  (`PRAGMA user_version`). Every future chat feature — toggling, resume,
  revisiting with new insight, Phase 2 filing, search over one's own
  conversations — is a query against this store, never a restoration
  project. The guarantee covers the conversation's *text*, not the
  continued validity of its citations: stored attribution is point-in-time
  and **presumed susceptible to bitrot** as the wiki evolves underneath it
  (pages rewritten, renamed, superseded by newer sources). Historical
  provenance survives regardless — each turn's transcript records what
  the model actually read at answer time.
- **Window** — derived, never stored: most recent turns whose cumulative
  estimate fits the seed budget (~6K tokens of the 16K: ~2.5K system +
  window + current question + tool headroom + generation). Over-long
  answers may be clipped *in the seed copy only*.
- Storage: SQLite (stdlib `sqlite3`), single file `harness/chat.db`,
  gitignored. Transactional appends; everything navigational (listings,
  labels, latest-session, windows) is derived by query, never duplicated
  into stored state.

## APIs / Interfaces

- `llmwiki chat [--resume [SESSION_ID]]` — new CLI entry point; `--resume`
  without an id continues the most recent conversation.
- In-REPL commands: `/new` (start a conversation), `/sessions` (list:
  first question, recency, turn count), `/switch <id>` (toggle the active
  conversation), `/ingest <file>`, `/lint`, `/help`, `/exit` (also
  Ctrl-C). Anything else is a chat turn against the active conversation.
- Chat workflow — `search_wiki`, `read_page`, terminal `respond`; two
  builder variants (grounded first turn of a conversation / relaxed
  follow-up), both read-only.
- `ChatStore` — internal adapter: create conversation, append turn, stamp
  activity, list conversations, load recent turns. The window builder
  stays a pure domain function over its output.
- Prompts — `CHAT_TEMPLATE`: answer from the wiki with `[[page]]` and
  `(raw/...)` citations; say plainly when the wiki lacks the answer; if
  asked to save or write something, explain that chat is read-only and the
  content belongs in a future ingest (Phase 2 lifts this). **The wiki is
  authoritative; the conversation is historical**: claims and citations in
  earlier turns are what was said then, not evidence now — when a prior
  claim becomes load-bearing for the current answer, re-verify it against
  the wiki's current pages (the same principle as re-fetching evidence,
  applied to the model's own past answers).

## Cross-Cutting Concerns

- **Graceful shutdown** — `/exit` and SIGINT converge on one path: write
  the log entry, stop llama-server. Nothing needs "closing": conversations
  are only ever dormant, and every completed turn is already in SQLite —
  a SIGKILL or crash loses only the in-flight turn (the server process
  dies with its parent).
- **Observability** — one transcript per turn under `harness/runs/`
  (tagged with conversation id and turn index), exactly like every other
  run.
- **Logging discipline** — one `chat` entry per REPL run (`## [date] chat
  | <k> turns across <m> conversations`) keeps `log.md` a chronology of
  operations rather than a duplicate transcript.
- **Latency** — turn 0 pays the boot + schema prefill; later turns reuse
  the server's prompt cache for the shared prefix, so time-to-first-token
  drops to roughly the retrieval the turn actually performs.
- **Privacy/footprint** — `chat.db` is personal session data: gitignored,
  deletable without affecting the wiki's three layers.

## Alternatives Considered

- **Per-query boots (status quo)** — no follow-ups, ~30 s tax per
  question; the measured pain behind open question #8.
- **Daemon + client commands** — detached lifecycle, stale-process states,
  port management; no benefit for one local user over a REPL whose process
  is the lifecycle.
- **Rolling summary memory** — normative for cloud chat frameworks;
  rejected here: it makes a 14B curator of its own memory (compounding
  drift — the same failure class as the destructive-rewrite incident) and
  costs extra generation at ~16 tok/s every few turns.
- **Embedding/BM25 retrieval over chat history** — rejected: sessions are
  a playground presumed full of dead ends and babble; ambient retrieval
  would promote that babble to evidence the model consults. Anything in a
  session that deserves to inform future answers gets *deliberately*
  promoted (Phase 2, human-initiated) — never picked up by a ranking
  function.
- **Persisting full forge transcripts as the seed** — rejected: prior
  turns' tool results balloon the window and re-expose forge's transient
  message pollution; Q/A pairs + re-fetching evidence is smaller and
  cleaner.
- **JSONL session files instead of SQLite** — workable, but resume,
  "latest session", and turn windowing are queries; SQLite gives them
  transactionally for free from the stdlib.
- **Threading `/ingest`/`/lint` into the conversation** — rejected
  (confirmed): they are their own workflows with step enforcement and
  their own loops; chat only shares the warm server with them.

## Open Questions / Risks

- **Window size** — ~6K tokens of Q/A pairs is a budget-table guess;
  needs a few real sessions. If long answers crowd the window, clip them
  in the seed copy only — stored turns stay verbatim (preservation
  guarantee).
- **Relaxed follow-ups and hallucination** — without required search on
  turns 1+, a 14B may answer from priors instead of re-reading the wiki.
  The prompt demands citations; if uncited answers show up, the escalation
  is a deterministic check (no `[[...]]` in answer → nudge to search), not
  a heavier prompt.
- **Resume ergonomics** — whether `--resume`/`/switch` should replay the
  last few Q/A to the terminal for human context; cosmetic, decide at
  implementation.
- **Citation bitrot in stored conversations** — by decision, stored
  attribution is treated as suspect: the wiki may have moved on (pages
  rewritten/renamed, claims superseded by later ingests) since an answer
  was given. Frequency in practice is unknown; deliberately no mitigation
  now. If revisited-conversation answers turn out to mislead often,
  candidates exist (show turn ages on resume; a lint-style checker that
  flags stored citations pointing at vanished pages) — build only on
  evidence.
- **Phase 2 boundary** — one feature, grounded in the pattern doc's
  per-answer filing guidance: `write_page` returns to the chat workflow
  (wired to the read-before-rewrite tracker) so a good answer — including
  one sussed out by revisiting an old conversation with new insight — can
  be filed as a `synthesis` page the moment it lands, mid-conversation.
