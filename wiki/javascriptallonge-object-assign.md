---
page_id: javascriptallonge-object-assign
page_kind: source
summary: Object.assign – object copying, extending, and prototype mixins
sources: raw/javascriptallonge.pdf p.198-205
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

Object.assign copies properties from source objects into a target object, enabling cloning, extension, and prototype manipulation.

## Key supported claims

- Assigning properties from one object to another (also called “cloning” or “shallow copying”) is a basic building block that we will later use to implement more advanced paradigms like mixins. (raw/javascriptallonge.pdf p.198-205)
- When discussing prototypes, we can use Object.assign to transform a constructor’s prototype into a mixin pattern. (raw/javascriptallonge.pdf p.198-205)
- You can extend one object with another by passing both as arguments to Object.assign, merging their properties into the target. (raw/javascriptallonge.pdf p.198-205)
- A concise example: const inventory = { apples: 12, oranges: 12 }; const shipment = { bananas: 54, pears: 24 }; Object.assign(inventory, shipment); (raw/javascriptallonge.pdf p.198-205)
- You can also copy an object by assigning it to an empty object: Object.assign({}, { apples: 12, oranges: 12 }); (raw/javascriptallonge.pdf p.198-205) **Possible**
