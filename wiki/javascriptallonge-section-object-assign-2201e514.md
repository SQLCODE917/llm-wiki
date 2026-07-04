---
page_id: javascriptallonge-section-object-assign-2201e514
page_kind: source
page_family: section-reference
summary: Object.assign: 1 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-03
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-object-assign-2201e514@4f8e3bb21988b61ef718649c5cd84946
---

# Object.assign

From [[javascriptallonge]].

## Statements

- Recipes with Data 

175 

## **Object.assign** 

It’s very common to want to “extend” an object by assigning properties to it: 

**const** inventory = { apples: 12, oranges: 12 }; inventory.bananas = 54; inventory.pears = 24; 

It’s also common to want to assign the properties of one object to another: 

**for** ( **let** fruit **in** shipment) { inventory[fruit] = shipment[fruit] } 

Both needs can be met with Object.assign, a standard function. You can copy an object by extending an empty object: 

Object.assign({}, { apples: 12, oranges: 12 }) _//=> { apples: 12, oranges: 12 }_ 

You can extend one object with another: 

**const** inventory = { apples: 12, oranges: 12 }; **const** shipment = { bananas: 54, pears: 24 } Object.assign(inventory, shipment) _(javascriptallonge.pdf (source-range-af806fb1-00226))_
