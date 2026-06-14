---
category: concept
summary: Combinators like K (Kestrel), I (Idiot Bird), and V (Vireo) enable creating functions that manipulate data without arrays/objects. Used in functional programming for data structure creation.
sources: raw/javascriptallonge.pdf
updated: 2026-06-11
---

Combinators are higher-order functions that enable complex operations with minimal primitives. Key combinators discussed in *JavaScript Allonge* include:

- **K (Kestrel)**: Returns a constant function. Example: `K(x)(y) => x`.
- **I (Idiot Bird)**: Identity function. Example: `I(x) => x`.
- **V (Vireo)**: Applies two values to a function. Example: `V(x)(y)(z) => z(x)(y)`.

These combinators allow constructing data structures (e.g., pairs, lists) purely with functions. For instance, `pair = V` creates a data structure that holds two values and applies a selector function to them. See [[javascriptallonge-making-data-out-of-functions]] for implementation details.
