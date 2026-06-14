---
category: source
summary: Updated to include iterable operations from the chunk: mapWith, filterWith, zip, zipWith, memoize, and reduceWith.
sources: raw/javascriptallonge.pdf
updated: 2026-06-12
---

## Iteration and Iterables

This page documents iterable operations from *JavaScript Allongé* (pages 273-292), including functions to transform and combine iterables:

### Transforming Iterables
- **mapWith(fn, iterable)**: Yields `fn(element)` for each element.
- **filterWith(fn, iterable)**: Yields elements where `fn(element)` is truthy.
- **compact(iterable)**: Yields non-null elements.
- **untilWith(fn, iterable)**: Yields elements until `fn(element)` is truthy.
- **take(number, iterable)**: Yields the first `number` elements.

### Combining Iterables
- **zip(...iterables)**: Yields tuples of elements from each iterable until one is exhausted.
- **zipWith(zipper, ...iterables)**: Applies `zipper` to tuples from multiple iterables (e.g., `zipWith((a, b) => a + b, [1,2], [3,4])` → `[4,6]`).
- **rest(iterable)**: Yields all elements except the first.

### Reducing Iterables
- **reduceWith(fn, seed, iterable)**: Applies `fn` cumulatively to reduce the iterable to a single value.
- **first(iterable)**: Returns the first element.

### Memoizing Iterables
- **memoize(generator)**: Caches results of a generator to avoid recomputation.

Citations: (raw/javascriptallonge.pdf p.273-292)
