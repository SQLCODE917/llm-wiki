---
category: concept
summary: Applying a function to each element of a data structure.
sources: raw/javascriptallonge.pdf p.109-125
updated: 2026-06-11
---

Mapping is a recursive pattern where a function is applied to each element of a data structure, such as an array. It is a specialized form of linear recursion and can be implemented using functions like `mapWith` in JavaScript. The key aspects include:

- **Function application**: Each element is transformed by a given function.
- **Accumulation**: Results are collected into a new data structure.

Example: Squaring each element in an array:
```js
const squareAll = ([first, ...rest]) => first === undefined ? [] : [first * first, ...squareAll(rest)];
```

Mapping is often generalized through folding, where the function is applied cumulatively. See [[javascriptallonge-self-similarity]] for implementation details.
