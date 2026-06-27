---
page_id: javascriptallonge-section-rewriting-iterable-operations-84d06ac3
page_kind: source
summary: **rewriting iterable operations**: 7 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-rewriting-iterable-operations-84d06ac3@4e316e3dbb763d2529bf527381e4efff
---

# **rewriting iterable operations**

From [[javascriptallonge]].

## Statements

- Now that we know about iterables, we can rewrite our iterable operations as generators. _(javascriptallonge.pdf (source-range-83ecb080-02713))_
- No need to explicitly construct an object that has a [Symbol.iterator] method. _(javascriptallonge.pdf (source-range-83ecb080-02719))_
- No need to return an object with a .next() method. _(javascriptallonge.pdf (source-range-83ecb080-02719))_
- We can do the same thing with our other operations like filterWith and untilWith. _(javascriptallonge.pdf (source-range-83ecb080-02720))_
- first works directly with iterators and remains unchanged, but rest can be rewritten as a generator: _(javascriptallonge.pdf (source-range-83ecb080-02726))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02726))_

> first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02727))_

> **const** first = (iterable) => iterable[Symbol.iterator]().next().value;

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02726))_

> first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02728))_

> **function** * rest (iterable) { **const** iterator = iterable[Symbol.iterator]();
