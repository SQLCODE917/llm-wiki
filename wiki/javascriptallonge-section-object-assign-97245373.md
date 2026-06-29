---
page_id: javascriptallonge-section-object-assign-97245373
page_kind: source
summary: Object.assign: 8 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-object-assign-97245373@a69cfdc12c43f74039632302fffdc2d8
---

# Object.assign

From [[javascriptallonge]].

## Statements

- Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object: _(javascriptallonge.pdf (source-range-8eb13d6b-01476))_

## Technical atoms

### Technical frame 1: Object.assign

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01476))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01473))_

```
const inventory = { apples: 12, oranges: 12 }; inventory.bananas = 54; inventory.pears = 24;
```

### Technical frame 2: Object.assign

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01476))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01475))_

```
for ( let fruit in shipment) { inventory[fruit] = shipment[fruit] }
```

### Technical frame 3: Object.assign

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01476))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01477))_

```
Object.assign({}, { apples: 12, oranges: 12 }) //=> { apples: 12, oranges: 12 }
```

### Technical frame 4: Object.assign

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01476))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01479))_

```
const inventory = { apples: 12, oranges: 12 }; const shipment = { bananas: 54, pears: 24 } Object.assign(inventory, shipment)
```

### Technical frame 5: Object.assign

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01476))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01480))_

```
//=> { apples: 12, // // // pears: 24 }
```

### Technical frame 6: Object.assign

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01476))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01482))_

```
const Queue = function () { this .array = []; this .head = 0; this .tail = -1 }; Queue.prototype.pushTail = function (value) { // ... }; Queue.prototype.pullHead = function () { // ... }; Queue.prototype.isEmpty = function () { // ... } Into this: const Queue = function () { Object.assign( this , { array: [], head: 0, tail: -1 }) }; Object.assign(Queue.prototype, { pushTail (value) { // ... }, pullHead () { // ... }, isEmpty () { // ...
```

### Technical frame 7: Object.assign

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01476))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01483))_

```
Recipes with Data } });
```
