---
category: concept
summary: JavaScript's Object.assign() method for shallow cloning and merging objects.
sources: raw/javascriptallonge.pdf
updated: 2026-06-11
---

Object.assign() is a standard function used to copy an object by extending an empty object or to merge properties from one object to another. Example:

```js
Object.assign({}, { apples: 12, oranges: 12 }) // { apples: 12, oranges: 12 }
Object.assign(inventory, shipment) // merges shipment into inventory
```

This method performs a shallow copy, meaning it copies the top-level properties but not nested objects. See [[javascriptallonge-object-assign]] for detailed examples and use cases. (raw/javascriptallonge.pdf p.198-205)
