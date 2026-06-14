---
category: source
summary: Explores interactive generators for stateful functions, using Naughts and Crosses as an example, and operations on iterables (map, filter, zip, etc.).
sources: raw/javascriptallonge.pdf
updated: 2026-06-12
---

## Interactive Generators

This chapter discusses using JavaScript generators to implement stateful functions, illustrated with a Naughts and Crosses (Tic-Tac-Toe) game. Key concepts include:

- **Stateful Functions**: Functions that maintain internal state through implicit control flow, unlike stateless functions that rely on external data structures (e.g., lookup tables).
- **Interactive Generators**: Generators that accept input values via `.next(value)` and yield outputs, enabling bidirectional interaction (e.g., a game where a player's move triggers the generator's response).
- **Example: Naughts and Crosses**: A stateless implementation uses a lookup table to determine moves, while a stateful version wraps a stateless function in a generator to track game state implicitly.
- **Iterable Operations**: Functions like `mapWith`, `filterWith`, `zip`, and `memoize` that transform or combine iterables.

Citations: (raw/javascriptallonge.pdf p.273-292)
