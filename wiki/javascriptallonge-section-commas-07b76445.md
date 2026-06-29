---
page_id: javascriptallonge-section-commas-07b76445
page_kind: source
summary: commas: 6 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-commas-07b76445@d0f51167fd80317bb364ba33bea00ae3
---

# commas

From [[javascriptallonge]].

## Statements

- The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words: _(javascriptallonge.pdf (source-range-8eb13d6b-00205))_
- This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write: _(javascriptallonge.pdf (source-range-8eb13d6b-00209))_

## Technical atoms

### Technical frame 1: commas

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00209))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00206))_

```
//=> 2 (1 + 1, 2 + 2)
```

### Technical frame 2: commas

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00209))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00208))_

```
(() => (1 + 1, 2 + 2))() //=> 4
```

### Technical frame 3: commas

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00205))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00209))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later.

### Technical frame 4: commas

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00209))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00210))_

```
() => (1 + 1, 2 + 2)
```
