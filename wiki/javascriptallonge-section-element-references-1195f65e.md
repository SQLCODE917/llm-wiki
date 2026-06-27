---
page_id: javascriptallonge-section-element-references-1195f65e
page_kind: source
summary: **element references**: 7 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-element-references-1195f65e@69772005286d1992c9d9761f848352e6
---

# **element references**

From [[javascriptallonge]].

## Statements

- Array elements can be extracted using [ and ] as postfix operators. _(javascriptallonge.pdf (source-range-83ecb080-01209))_
- As we can see, JavaScript Arrays are zero-based[56] . _(javascriptallonge.pdf (source-range-83ecb080-01212))_
- We know that every array is its own unique entity, with its own unique reference. _(javascriptallonge.pdf (source-range-83ecb080-01213))_

## Technical atoms

> Context: Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract:
_(context: javascriptallonge.pdf (source-range-83ecb080-01209))_

> **const** oneTwoThree = ["one", "two", "three"];
_(source: javascriptallonge.pdf (source-range-83ecb080-01210))_

> Context: Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract:
_(context: javascriptallonge.pdf (source-range-83ecb080-01209))_

> oneTwoThree[0] _//=> 'one'_ oneTwoThree[1] _//=> 'two'_ oneTwoThree[2] _//=> 'three'_
_(source: javascriptallonge.pdf (source-range-83ecb080-01211))_

> **const** x = [], a = [x];
_(source: javascriptallonge.pdf (source-range-83ecb080-01217))_

> a[0] === x
_(source: javascriptallonge.pdf (source-range-83ecb080-01218))_
