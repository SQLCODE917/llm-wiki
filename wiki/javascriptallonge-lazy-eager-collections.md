---
category: source
summary: Discusses lazy and eager collections in JavaScript, their implementations via iterators, and efficiency tradeoffs between on-demand computation and immediate data processing.
sources: raw/javascriptallonge.pdf
updated: 2026-06-12
---

## Lazy and Eager Collections

JavaScript collections can be implemented as **lazy** (deferred computation) or **eager** (immediate processing). Lazy collections use iterators to delay operations until needed, reducing memory overhead. Eager collections (like arrays) process data immediately, creating new copies at each step.

### Lazy Collection Implementation
Lazy collections delegate operations like `map`, `filter`, and `reduce` to iterators. For example, the `LazyCollection` mixin provides:
- `map(fn)`: Returns an iterable that applies `fn` to each element on demand.
- `filter(fn)`: Returns an iterable that includes only elements passing `fn`.
- `take(n)`: Returns an iterable with the first `n` elements.

Example: `Pair.from([1,2,3]).map(x => x*2).first()` computes only the first element (2) rather than processing all elements upfront.

### Eager Collection Implementation
Eager collections (like arrays) process operations immediately, creating new data structures. The `EagerCollection` implementation uses `.from()` to gather results into new instances:
- `map(fn)`: Returns a new array with transformed elements.
- `filter(fn)`: Returns a new array with filtered elements.

### Tradeoffs
- **Lazy** collections save memory but may have higher computational overhead if many operations are chained.
- **Eager** collections are faster for small datasets but can be memory-intensive with large data.

Source: (raw/javascriptallonge.pdf p.246-260)

See [[eager-evaluation]] and [[lazy-evaluation]] for the underlying strategies.
