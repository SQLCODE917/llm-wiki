---
category: source
summary: Updated to include interactive generators and stateful function examples from the Naughts and Crosses game.
sources: raw/javascriptallonge.pdf
updated: 2026-06-12
---

## Generating Iterables

JavaScript generators are a powerful tool for creating iterators, coroutines, and stateful functions. This page expands on the concepts introduced in the 'Interactive Generators' chapter (pages 273-292 of *JavaScript Allongé*), including:

- **Interactive Generators**: Generators that accept input values via `.next(value)` and yield outputs, enabling bidirectional interaction. Example: A Naughts and Crosses game where a player's move triggers the generator's response.
- **Stateful Functions**: Functions that maintain internal state implicitly through control flow, as opposed to explicitly storing state in data structures. The chapter contrasts stateless implementations (using lookup tables) with stateful ones (using generators).
- **Coroutine Pattern**: Generators generalize subroutines by allowing suspension and resumption, making them ideal for stateful computations.

Citations: (raw/javascriptallonge.pdf p.273-292)
