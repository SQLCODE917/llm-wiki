---
page_id: javascriptallonge-section-operations-that-transform-one-iterable-into-another-f5f924a7
page_kind: source
summary: **operations that transform one iterable into another**: 1 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-operations-that-transform-one-iterable-into-another-f5f924a7@e6e9d5f5a904047db4751d2e197e4e55
---

# **operations that transform one iterable into another**

From [[javascriptallonge]].

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-03059))_

> **for** ( **let** i = 0; i < numberToTake; ++i) { **const** { done, value } = iterator.next(); **if** (!done) **yield** value; } }
