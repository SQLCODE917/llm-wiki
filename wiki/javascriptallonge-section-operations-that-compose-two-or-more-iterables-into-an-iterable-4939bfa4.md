---
page_id: javascriptallonge-section-operations-that-compose-two-or-more-iterables-into-an-iterable-4939bfa4
page_kind: source
summary: **operations that compose two or more iterables into an iterable**: 2 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-operations-that-compose-two-or-more-iterables-into-an-iterable-4939bfa4@2a9df3e231475e1db89e0b170ac902ab
---

# **operations that compose two or more iterables into an iterable**

From [[javascriptallonge]].

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-03061))_

> **function** * zip (...iterables) { **const** iterators = iterables.map(i => i[Symbol.iterator]());

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-03063))_

> Note: zip is also the following special case of zipWith:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-03066))_

> **const** zip = callFirst(zipWith, (...values) => values);
