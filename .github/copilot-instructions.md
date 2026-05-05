# Copilot Instructions for llm-wiki

Read and follow [AGENTS.md](../AGENTS.md) for all wiki maintenance tasks.

## Quick Reference

### Ingest a PDF (Phase 0-3)

1. **Phase 0 - Normalize**: `pnpm wiki:phase0 raw/inbox/<file.pdf> <slug>`
2. **Phase 1 - Source page**: Create `wiki/sources/<slug>.md`, validate with `pnpm wiki:check-source <slug>`
3. **Phase 2 - Synthesized pages**: Create concept/entity/procedure/reference pages, validate with `pnpm wiki:check-synthesis <slug>`
4. **Phase 3 - Finalize**: `pnpm wiki:phase3 <slug>`

### Query the Wiki

1. Read `wiki/index.md` to find relevant pages
2. Use `wiki/_graph.json` for relationships
3. Read specific wiki pages to answer questions
4. For durable answers, file to `wiki/analyses/`

### Maintenance

- Lint: `pnpm wiki:lint`
- Full maintenance: `pnpm wiki:maintenance --append-log`
- Check index: `pnpm wiki:index:check`
- Check graph: `pnpm wiki:graph:check`

### Validation Commands

| Phase       | Command                            |
| ----------- | ---------------------------------- |
| Source page | `pnpm wiki:check-source <slug>`    |
| Synthesis   | `pnpm wiki:check-synthesis <slug>` |
| Grounding   | `pnpm wiki:grounding:check`        |
| Links       | `pnpm wiki:fix-links <slug>`       |

## Key Rules

1. **Never edit `raw/imported/`** — it's immutable
2. **Every claim needs evidence** — use `normalized:L12` locators
3. **Prefer updating existing pages** over creating duplicates
4. **Run validation after edits** — fix issues before moving on
5. **Log operations** — append to `wiki/log.md`

## AWS Bedrock Setup (for CLI mode)

```bash
# One-time SSO configuration
aws configure sso --profile sdai-dev

# Authenticate (refresh as needed)
aws sso login --profile sdai-dev

# Verify
aws bedrock list-foundation-models --region us-east-1 --profile sdai-dev | head -5
```

## Environment Variables

```bash
export AWS_PROFILE=sdai-dev
export AWS_REGION=us-east-1
export WIKI_MODEL_BACKEND=bedrock
```
