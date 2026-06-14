---
category: concept
summary: Describes eager evaluation in JavaScript, where operations on collections are processed immediately, creating new data structures at each step.
sources: raw/javascriptallonge.pdf
updated: 2026-06-12
---

Eager evaluation in JavaScript processes operations on collections immediately, creating new data structures at each step. This is typical for built-in types like arrays, where methods like `map`, `filter`, or `reduce` return new copies of the data. For example, `array.map(x => x*2)` creates a new array with transformed elements right away.

### Key Characteristics:
- **Immediate Processing**: Operations are executed as soon as called, even if the results are not immediately used.
- **Memory Overhead**: Creates new copies of data at each step, which can be inefficient for large datasets.
- **Example**: `array.map(x => x*2).filter(x => x % 2 == 0)` creates two temporary arrays (one from `map`, one from `filter`) before the final result is used.

### Tradeoffs:
- **Pros**: Simpler to reason about, faster for small datasets.
- **Cons**: Higher memory usage, potential performance issues with large data or many chained operations.

Cited in: [[javascriptallonge-lazy-eager-collections]] (raw/javascriptallonge.pdf p.246-260)
