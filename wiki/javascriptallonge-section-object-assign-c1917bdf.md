---
page_id: javascriptallonge-section-object-assign-c1917bdf
page_kind: source
summary: **Object.assign**: 4 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-object-assign-c1917bdf@869e34632f100fa077c9ed30d98fbb09
---

# **Object.assign**

From [[javascriptallonge]].

## Statements

- Both needs can be met with Object.assign, a standard function. _(javascriptallonge.pdf (source-range-83ecb080-02282))_

## Technical atoms

> Context: It’s very common to want to “extend” an object by assigning properties to it:
_(context: javascriptallonge.pdf (source-range-83ecb080-02278))_

> **const** inventory = { apples: 12, oranges: 12 }; inventory.bananas = 54; inventory.pears = 24;
_(source: javascriptallonge.pdf (source-range-83ecb080-02279))_

> Context: Both needs can be met with Object.assign, a standard function. You can copy an object by extending an empty object:
_(context: javascriptallonge.pdf (source-range-83ecb080-02282))_

> Object.assign({}, { apples: 12, oranges: 12 }) _//=> { apples: 12, oranges: 12 }_
_(source: javascriptallonge.pdf (source-range-83ecb080-02283))_

> Context: You can extend one object with another:
_(context: javascriptallonge.pdf (source-range-83ecb080-02284))_

> **const** inventory = { apples: 12, oranges: 12 }; **const** shipment = { bananas: 54, pears: 24 } Object.assign(inventory, shipment)
_(source: javascriptallonge.pdf (source-range-83ecb080-02285))_
