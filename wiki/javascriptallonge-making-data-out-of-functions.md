---
category: source
summary: Explores using combinators (K, I, V) and functions to create data structures like lists and pairs, avoiding arrays/objects. Introduces mapWith and flip functions.
sources: raw/javascriptallonge.pdf
updated: 2026-06-11
---

## Making Data Out Of Functions

This chapter demonstrates how to represent data structures (like lists and pairs) using pure functions and combinators, avoiding arrays and objects. Key concepts include:

- **Combinators**: K (constant function), I (identity), and V (Vireo) for creating data structures.
- **Functional Data Structures**: Using functions to model linked lists and pairs (e.g., `pair = V`).
- **mapWith**: A curried function that applies a transformation to each element of a data structure.
- **flip**: A utility to reverse function argument order, enabling currying.

Examples include creating a list with `pair` and implementing `mapWith` and `flip` for functional programming patterns. See (raw/javascriptallonge.pdf p.177-197) for detailed code.
