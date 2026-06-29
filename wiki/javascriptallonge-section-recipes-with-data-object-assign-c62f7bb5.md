---
page_id: javascriptallonge-section-recipes-with-data-object-assign-c62f7bb5
page_kind: source
summary: Recipes with Data / Object.assign: 8 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-data-object-assign-c62f7bb5@03aefc091f102e4edcd89545f263f4ad
---

# Recipes with Data / Object.assign

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-recipes-with-data-178f0a89]] - broader source section: Recipes with Data

## Statements

- Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object: _(javascriptallonge.pdf (source-range-7239e085-01477))_

## Technical atoms

### Technical frame 1: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01477))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01474))_

```
const inventory = {
apples: 12,
oranges: 12
};
inventory.bananas = 54;
inventory.pears = 24;
```

### Technical frame 2: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01477))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01476))_

```
for (let fruit in shipment) {
inventory[fruit] = shipment[fruit]
}
```

### Technical frame 3: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01477))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01478))_

```
Object.assign({}, {
apples: 12,
oranges: 12
})
//=> { apples: 12, oranges: 12 }
```

### Technical frame 4: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01477))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01480))_

```
const inventory = {
apples: 12,
oranges: 12
};
const shipment = {
bananas: 54,
pears: 24
}
Object.assign(inventory, shipment)
```

### Technical frame 5: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01477))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01481))_

```
//=> { apples: 12,
//
oranges: 12,
//
bananas: 54,
//
pears: 24 }
```

### Technical frame 6: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01477))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01483))_

```
const Queue = function () {
this.array = [];
this.head = 0;
this.tail = -1
};
Queue.prototype.pushTail = function (value) {
// ...
};
Queue.prototype.pullHead = function () {
// ...
};
Queue.prototype.isEmpty = function () {
// ...
}
Into this:
const Queue = function () {
Object.assign(this, {
array: [],
head: 0,
tail: -1
})
};
Object.assign(Queue.prototype, {
pushTail (value) {
// ...
},
pullHead () {
// ...
},
isEmpty () {
// ...
```

### Technical frame 7: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01477))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01484))_

```
Recipes with Data
}
});
```
