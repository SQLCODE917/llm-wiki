---
category: source
summary: JavaScript Object.assign method for shallow cloning and merging objects (pages 198-205).
sources: raw/javascriptallonge.pdf
updated: 2026-06-11
---

This chapter explains JavaScript's Object.assign() method for shallow copying and merging objects. Key examples include:

```js
Object.assign({}, { apples: 12, oranges: 12 }) // { apples: 12, oranges: 12 }
Object.assign(inventory, shipment) // merges shipment into inventory
```

The chapter also introduces quasi-literals (template strings) using backticks, e.g.:

```js
`A popular number for nerds is ${40 + 2}` // 'A popular number for nerds is 42'
```

Additionally, the Y Combinator is presented as a functional programming concept, though its practical use in JavaScript is limited. (raw/javascriptallonge.pdf p.198-205)
