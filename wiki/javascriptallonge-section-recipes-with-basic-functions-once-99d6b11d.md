---
page_id: javascriptallonge-section-recipes-with-basic-functions-once-99d6b11d
page_kind: source
page_family: section-reference
summary: Recipes with Basic Functions / Once: 5 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-once-99d6b11d@e8439ce469a6587ff41de974273848d7
---

# Recipes with Basic Functions / Once

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-recipes-with-basic-functions-c9137465]] - broader source section: Recipes with Basic Functions

## Statements

- once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe: _(javascriptallonge.pdf (source-range-7239e085-00710))_
- It ensures that a function can only be called, well, once . _(javascriptallonge.pdf (source-range-7239e085-00710))_

## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Once

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00710))_

> once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00711))_

<a id="atom-technical-atom-2388b6615c013cfa"></a>

```
const once = (fn) => {
let done = false;
return function () {
return done ? void 0 : ((done = true), fn.apply(this, arguments))
}
}
```

### Technical frame 2: Recipes with Basic Functions / Once

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00710))_

> once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00713))_

<a id="atom-technical-atom-4a54ace1417283a8"></a>

```
const askedOnBlindDate = once(
() => "sure, why not?"
);
askedOnBlindDate()
//=> 'sure, why not?'
askedOnBlindDate()
//=> undefined
askedOnBlindDate()
//=> undefined
```
