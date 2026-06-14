---
category: concept
summary: Defines iterables in JavaScript via Symbol.iterator, with emphasis on generator-based implementations.
sources: javascriptallonge.pdf p.224-245, javascriptallonge.pdf
updated: 2026-06-12
---

An **iterable** in JavaScript is an object that implements the `Symbol.iterator` method, which returns an iterator object with a `.next()` method. This enables usage with `for...of` loops and the spread operator (`...`).

**Generator-based iterables**: Modern implementations often define `[Symbol.iterator]` as a generator function (using `function *`), simplifying state management. Example:

```js
const ThreeNumbers = { *[Symbol.iterator]() { yield 1; yield 2; yield 3; } }
```

This allows:
- `for...of` iteration: `for (const num of ThreeNumbers) { ... }`
- Spreading: `['all the numbers', ...ThreeNumbers]`

See [[javascriptallonge-generating-iterables]] for detailed examples and [[generator]] for how generators enable this pattern.
