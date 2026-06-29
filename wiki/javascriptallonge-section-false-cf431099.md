---
page_id: javascriptallonge-section-false-cf431099
page_kind: source
summary: false: 6 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-false-cf431099@d1718aa4c77dd7032c8e8f7cb9b2cc1c
---

# false

From [[javascriptallonge]].

## Statements

- true and false are value types. All values of true are === all other values of true. We can see that is the case by looking at some operators we can perform on boolean values, ! , && , and || . To being with, ! is a unary prefix operator that negates its argument. So: _(javascriptallonge.pdf (source-range-8eb13d6b-00759))_
- Now, note well: We have said what happens if you pass boolean values to ! , && , and || , but we've said nothing about expressions or about passing other values. We'll look at those presently. _(javascriptallonge.pdf (source-range-8eb13d6b-00763))_

## Technical atoms

### Technical frame 1: false

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00763))_

> Now, note well: We have said what happens if you pass boolean values to ! , && , and || , but we've said nothing about expressions or about passing other values. We'll look at those presently.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00760))_

```
! true //=> false ! false //=> true
```

### Technical frame 2: false

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00763))_

> Now, note well: We have said what happens if you pass boolean values to ! , && , and || , but we've said nothing about expressions or about passing other values. We'll look at those presently.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00762))_

```
false && false //=> false false && true //=> false true && false //=> false true && true //=> true false || false //=> false false || true //=> true true || false //=> true true || true //=> true
```
