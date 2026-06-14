# Writing Technical Design Documents (TDDs)

Instructions for any design document written in this repo. Referenced from
CLAUDE.md ("Design Documents") — read this file in full before writing a
TDD, and follow it exactly.

You are writing a Technical Design Document (TDD). The TDD will be reviewed by a
human and then handed to a coding agent for implementation. Its job is to pin down
every decision that crosses a contract boundary, and to stay silent on everything
the implementer can decide for itself.

**Sizing gate (apply BEFORE writing):**
One TDD = one independently shippable and revertable unit of work. If the
architecture diagram would need more than ~6 components, or the doc would need
more than 3–4 sequence diagrams, or any diagram cannot be drawn in simple ASCII —
the scope is too big or too low-level. Stop and propose a split into multiple
TDDs instead of writing one.

**Structure (use these sections, in order):**

1. **Context & Problem** — 2–4 sentences on what exists today and what's broken
   or missing.

2. **Goals** — bulleted, measurable where possible.

3. **Non-Goals & Forbidden Approaches** — two explicit lists:
   - *Non-goals*: scope this design will not address.
   - *Forbidden approaches*: solutions the implementer must NOT use, even where
     they seem natural (e.g. "do not add a GSI", "do not introduce a new Lambda",
     "do not denormalize this table"). Include the common/obvious approach if it
     was considered and rejected.

4. **Requirements** — the constraints driving the design. Each requirement must
   be unambiguous (one possible reading) and verifiable (a finite check could
   confirm it).

5. **Invariants** — statements that must be true before AND after this work ships
   (backward compatibility guarantees, data integrity rules, idempotency
   properties). These constrain every implementation decision, including ones
   this doc doesn't anticipate.

6. **Proposed Architecture** — prose description supported by a C4 Container-level
   diagram in plain ASCII. One sentence per component stating its responsibility.

7. **Key Interactions** — sequence diagrams in plain ASCII for the 2–4 flows that
   exercise the most architectural surface.

8. **Data Model** — entities, relationships, key access patterns. Schema sketches
   are fine; full DDL is not.

9. **APIs / Interfaces** — endpoint/interface names, methods, and purpose. No
   request/response schemas or signatures UNLESS the type itself is a contract
   decision — i.e. if the implementer chose a different shape, the PR would be
   rejected. Those types must be pinned here exactly.

10. **Behavior & Domain Rules** — each business rule stated once in prose, then
    anchored with 1–3 concrete worked examples (inputs → expected outcome),
    always including the ugliest edge case. Examples are normative: if prose and
    example conflict, the example wins and the doc must be fixed.

11. **Acceptance Criteria** — observable, contract-level checks that define
    "done". Written so they can be turned directly into tests. If the work is
    large, group criteria into ordered milestones; each milestone is a
    verification gate the implementation must pass before proceeding.

12. **Cross-Cutting Concerns** — auth, observability, error handling, etc. One
    short paragraph each, only where this design deviates from or adds to repo
    conventions. Don't restate what AGENTS.md already covers.

13. **Reference Implementations** — pointers to existing files/modules in the
    repo whose patterns the implementer should imitate, one line each
    (e.g. "error handling: follow src/handlers/x.ts").

14. **Alternatives Considered** — bulleted, one line each, with the chosen option
    and a half-sentence on why. Link an ADR if the justification needs more.

15. **Halt Conditions** — anything unresolved goes here, phrased as an explicit
    instruction: "If implementation touches X, stop and ask before proceeding."
    No ambient open questions; every item is either resolved before handoff or
    converted into a halt condition.

**Style constraints:**
- All diagrams are plain ASCII. If something can't be expressed in a simple ASCII
  diagram, it is too low-level for this document — omit it or escalate via the
  sizing gate.
- No pseudocode, no implementation snippets, no function signatures — except
  public contract types per section 9.
- State technology choices as decisions, not arguments. "Uses DynamoDB" — not
  three paragraphs comparing it to Postgres. If a choice needs justification,
  write a one-line ADR pointer.
- Hard cap: ~300 lines. If a section would exceed half a page, ask whether to
  split it into a separate doc or ADR rather than expanding inline.
- Write for an engineer who already knows the stack. Don't explain what GitHub
  Actions or DynamoDB is.
- Prefer prose for design rationale; bullets for enumerable lists.
- Editing pass before finishing: delete any sentence describing HOW to build
  something rather than WHAT must be true. The test for inclusion: "if the
  implementer decided this differently, would the PR be rejected?" If no, cut it.
