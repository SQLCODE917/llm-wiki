---
page_id: javascriptallonge-section-recipes-with-data-object-assign-c62f7bb5
page_kind: source
page_family: section-reference
summary: Recipes with Data / Object.assign: 8 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-data-object-assign-c62f7bb5@4b80e3ed927e69095b60281b2cf9f635
---

# Recipes with Data / Object.assign

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-recipes-with-data-178f0a89]] - broader source section: Recipes with Data

## Statements

- Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object: _(javascriptallonge.pdf (source-range-7239e085-01477))_

## Technical atoms

### Technical frame 1: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01477))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01476))_

<a id="atom-technical-atom-14958659bed2e9fa"></a>

```
for (let fruit in shipment) {
inventory[fruit] = shipment[fruit]
}
```

### Technical frame 2: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01477))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01478))_

<a id="atom-technical-atom-526738d82125eba6"></a>

```
Object.assign({}, {
apples: 12,
oranges: 12
})
//=> { apples: 12, oranges: 12 }
```

### Technical frame 3: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01477))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01483))_

<a id="atom-technical-atom-6655ab31ba14d03b"></a>

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

### Technical frame 4: Recipes with Data / Object.assign

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01477))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01484))_

<a id="atom-technical-atom-a404634b8bd264da"></a>

```
Recipes with Data
}
});
```
