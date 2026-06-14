---
category: concept
summary: Describes ordered collections in JavaScript, which reset iteration on each access and support operations like mapWith.
sources: javascriptallonge.pdf
updated: 2026-06-12
---

An **ordered collection** in JavaScript is a collection that returns elements in a fixed order each time it is iterated. Examples include arrays, stacks, and linked lists implemented with `Symbol.iterator`.

Key properties:
- Iteration starts from the beginning each time (e.g., `for...of` on a stack yields elements in push order).
- Operations like `mapWith`, `filterWith`, and `untilWith` return new ordered collections preserving this behavior.

Example: The `mapWith` function in [[javascriptallonge-iteration-and-iterables]] transforms an ordered collection (e.g., `Numbers`) into another ordered collection (`Evens`), ensuring consistent iteration order.
