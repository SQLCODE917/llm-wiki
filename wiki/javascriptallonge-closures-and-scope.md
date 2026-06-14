---
category: source
summary: JavaScript closures, scope chains, pure functions, and environment hierarchy (pages 44-48).
sources: raw/javascriptallonge.pdf
updated: 2026-06-13
---

## Closures and Scope

This chapter explores how nested functions access variables from outer scopes, defining key concepts:

- **Closures**: Functions containing free variables (e.g., `(y) => x` where `x` is from an outer scope).
- **Scope chains**: Environments include parent environments (`'..'` references), enabling access to variables in ancestor scopes.
- **Pure functions** vs. closures: Pure functions have no free variables (e.g., `(x) => x`), while closures rely on external variables.
- **Shadowing**: Inner variables with the same name as outer ones override the outer bindings (e.g., `(x) => (x, y) => x + y`).
- **Global environment**: All functions have access to a global environment, which can be isolated using IIFEs (e.g., `(() => { ... })()`).

Examples include the K Combinator `(x) => (y) => x` and currying/partial application patterns. The chapter also discusses how closures enable functional programming techniques.

Related: [[closure]].
