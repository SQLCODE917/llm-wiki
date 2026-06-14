---
category: concept
summary: mapWith curries functions for data transformation, while flip reverses argument order. Both enable functional programming patterns in JavaScript.
sources: raw/javascriptallonge.pdf
updated: 2026-06-11
---

The `mapWith` function curries a transformation function to work with data structures, enabling reusable mapping operations. `flip` reverses argument order, supporting currying and function composition. Example implementations from *JavaScript Allonge*:

```javascript
const mapWith = (fn) => (list) => list.map(fn);
const flip = (fn) => (first, second) => fn(second, first);
```

These utilities demonstrate functional programming principles like currying and higher-order functions. See [[javascriptallonge-making-data-out-of-functions]] for detailed usage examples.
