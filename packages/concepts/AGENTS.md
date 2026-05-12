# concepts — Package Rules

> Executable TypeScript implementations of wiki concepts.

---

## Purpose

This package contains working code for wiki concepts that can be computed or
demonstrated. When a wiki concept page describes something executable (like
compound interest, search algorithms, or game mechanics calculations), the
implementation lives here with tests.

Wiki concept pages link to these implementations via `## Executable implementation`
sections.

---

## TypeScript

- Typecheck must pass.
- Prefer explicit types on exported APIs and public functions.
- Use `unknown` at trust boundaries, then validate and narrow.
- Prefer discriminated unions over boolean flag combinations.
- Use user-defined type guards where they clarify trust boundaries.
- Avoid `any`, unsafe assertions, and `ts-ignore`.
- If `any`, an unsafe cast, or a suppression is unavoidable, isolate it, document why, and mention it in the implementation summary.
- Use reasoned `@ts-expect-error` only when TypeScript cannot express a real invariant; do not use `@ts-ignore`.
- Functions should either transform data or orchestrate work, not both.

---

## Module structure

```
concepts/
├── src/
│   ├── index.ts           # Re-exports all implementations
│   └── compoundInterest.ts  # Example: compound interest calculation
└── tests/
    └── compoundInterest.test.ts
```

Each concept gets:
1. A source file in `src/` with the implementation
2. A test file in `tests/` with the same base name
3. An export in `src/index.ts`

---

## Linking to wiki pages

When a wiki concept page has an executable implementation:

1. Add `## Executable implementation` section to the wiki page
2. Link to the source file: `[compoundInterest.ts](../../packages/concepts/src/compoundInterest.ts)`
3. Link to the test file: `[compoundInterest.test.ts](../../packages/concepts/tests/compoundInterest.test.ts)`

Example wiki section:

```markdown
## Executable implementation

- Source: [compoundInterest.ts](../../packages/concepts/src/compoundInterest.ts)
- Tests: [compoundInterest.test.ts](../../packages/concepts/tests/compoundInterest.test.ts)
```

---

## Testing

Run tests with:

```bash
pnpm --filter @llm-wiki/concepts test
# or
pnpm code:test
```

Run typecheck with:

```bash
pnpm --filter @llm-wiki/concepts typecheck
# or
pnpm code:typecheck
```

Before merging changes:
1. `pnpm code:typecheck` must pass.
2. `pnpm code:test` must pass.
3. New implementations must have corresponding tests.

---

## When to add code here

Add code to `concepts/` when:
- A wiki concept page describes something that can be computed
- The implementation helps verify the concept's correctness
- Tests can demonstrate the concept's behavior

Do **not** add code here if it:
- Is wiki infrastructure (use Python packages instead)
- Has no corresponding wiki concept page
- Is a one-off script (keep in `tools/`)
