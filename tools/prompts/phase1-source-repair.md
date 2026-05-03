Read `AGENTS.md` fully before acting.

You are performing LLM-Wiki ingest Phase 1 only: source page repair.

Current date: {{current_date}}
Source slug: `{{slug}}`
Normalized source to read: `{{normalized_source}}`
Target source page to rewrite: `wiki/sources/{{slug}}.md`

Allowed write:
- `wiki/sources/{{slug}}.md`

Forbidden writes:
- `raw/imported/**`
- `raw/normalized/**`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/_graph.json`
- `wiki/_linter-report.md`
- `wiki/concepts/**`
- `wiki/entities/**`
- `wiki/procedures/**`
- `wiki/references/**`
- `wiki/analyses/**`
- `packages/**`
- `tools/**`

Do not create related pages yet. This is Phase 1 only.

Rewrite `wiki/sources/{{slug}}.md` from the normalized source.

The source page must include:
- proper YAML frontmatter
- `type: source`
- `source_id: {{slug}}`
- `source_type: pdf`
- `raw_path: ../../raw/imported/{{slug}}/`
- `normalized_path: ../../raw/normalized/{{slug}}/`
- `status: draft`
- `last_updated: {{current_date}}`
- `tags: []`
- `sources` containing `../../raw/imported/{{slug}}/original.pdf`
- one H1 title
- exactly these H2 headings, in this order:
  - `## Summary`
  - `## Key claims`
  - `## Major concepts`
  - `## Entities`
  - `## Procedures`
  - `## References`
  - `## Open questions`
  - `## Related pages`

Mechanical content rules:
- Keep this as a source page only.
- Do not write process notes such as "created as part of ingestion."
- Do not invent facts.
- If the source does not cover a section, write `not covered in sources` or `None.`

`## Key claims` rules:
- Write {{min_claims}} to {{max_claims}} numbered claims.
- Use plain numbered sentences. Do not use bold labels in the claim list.
- Each claim must be at least {{min_claim_words}} words.
- The words important, crucial, fundamental, essential, and success are validation failures in `## Key claims`.
- Each claim must include a concrete action, cause, effect, condition, tradeoff, timing, unit interaction, resource relationship, or map/team implication from the source.
- Every key claim must be reusable gameplay/content/domain knowledge from the normalized source.
- Do not include document metadata as key claims.
- In `## Key claims`, these words are validation failures: guide, document, author, coached, coaching, Twitch, Google Docs, published.
- Claims should talk about game actions, strategy, economy, scouting, units, buildings, timings, resources, team play, or improvement procedures.
- A bad claim is "The guide covers scouting."
- A good claim is "Scouting gives the player information about enemy openings, army movement, and resource exposure."

`## Major concepts` rules:
- Study the source's natural groupings even if this is the only PDF ingested so far.
- Natural groupings are source-native themes, chapters, or clusters of reusable knowledge.
- Do not create new wiki directories from these groupings in Phase 1.
- Include at least {{min_natural_groups}} natural groups in this exact table shape:

```md
### Natural groupings

| Group | Scope | Evidence basis | Candidate page types |
|---|---|---|---|
| Source-native group name | clear non-overlapping scope | concrete sections, claims, examples, or procedures | concept, procedure |
```

- If the source is tiny and has fewer natural groups, write the real groups it contains and keep the scopes narrow.

`## Related pages` rules:
- If a related page does not already exist, do not use a Markdown link to it.
- List future synthesized pages as a candidate table only.
- Use code-formatted intended paths in the table.
- List {{min_related_candidates}} to {{max_related_candidates}} strong candidate pages.
- Prefer candidates with enough source evidence to support at least 3 later evidence-table rows.
- Every related-page row must include a `Group` value copied exactly from the `## Major concepts` natural groupings table.
- Set priority to one of: `must create`, `should create`, `could create`, `defer`.
- Use `must create` only for high-evidence reusable pages that should be created in Phase 2.
- Use `Evidence basis` to name the concrete source material that supports the candidate.
- Do not list generic, vague, or duplicate pages such as wisdom, knowledge, community, streaming, best practices, improvement, progress, or experience unless the source contains a specific reusable concept by that name.
- Use this table shape:

```md
| Candidate page | Intended path | Group | Priority | Evidence basis | Status |
|---|---|---|---|---|---|
| Example Concept | `../concepts/example-concept.md` | Source-native group name | must create | concrete claims, examples, or procedure steps | not created yet |
```

After writing, run exactly:

```bash
python3 tools/wiki_check_source.py {{slug}} --min-claims {{min_claims}} --max-claims {{max_claims}} --min-claim-words {{min_claim_words}} --min-related-candidates {{min_related_candidates}} --max-related-candidates {{max_related_candidates}} --require-natural-groups --min-natural-groups {{min_natural_groups}} {{weak_claims_flag}} {{grounding_flag}}
```

If validation fails, repair only `wiki/sources/{{slug}}.md` and rerun the same command.

Stop only when validation passes, or when you cannot proceed. If you cannot proceed, report the exact failing validation output.
