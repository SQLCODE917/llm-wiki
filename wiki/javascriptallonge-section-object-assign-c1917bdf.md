---
page_id: javascriptallonge-section-object-assign-c1917bdf
page_kind: source
summary: **Object.assign**: 4 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-object-assign-c1917bdf@3d43dc0f0212d4a7956fcc5e36d721c4
---

# **Object.assign**

From [[javascriptallonge]].

## Statements

- Both needs can be met with Object.assign, a standard function. _(javascriptallonge.pdf (source-range-83ecb080-02282))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02278))_

> It’s very common to want to “extend” an object by assigning properties to it:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02279))_

> **const** inventory = { apples: 12, oranges: 12 }; inventory.bananas = 54; inventory.pears = 24;

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02282))_

> Both needs can be met with Object.assign, a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02283))_

> Object.assign({}, { apples: 12, oranges: 12 }) _//=> { apples: 12, oranges: 12 }_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02284))_

> You can extend one object with another:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02285))_

> **const** inventory = { apples: 12, oranges: 12 }; **const** shipment = { bananas: 54, pears: 24 } Object.assign(inventory, shipment)
