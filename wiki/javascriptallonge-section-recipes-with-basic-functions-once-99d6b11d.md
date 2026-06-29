---
page_id: javascriptallonge-section-recipes-with-basic-functions-once-99d6b11d
page_kind: source
summary: Recipes with Basic Functions / Once: 5 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-once-99d6b11d@14ffd04156437da3ce447ec695ad9e39
---

# Recipes with Basic Functions / Once

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-recipes-with-basic-functions-c9137465]] - broader source section: Recipes with Basic Functions

## Statements

- once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe: _(javascriptallonge.pdf (source-range-7239e085-00710))_
- It ensures that a function can only be called, well, once . _(javascriptallonge.pdf (source-range-7239e085-00710))_

## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Once

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00710))_

> once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00711))_

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
