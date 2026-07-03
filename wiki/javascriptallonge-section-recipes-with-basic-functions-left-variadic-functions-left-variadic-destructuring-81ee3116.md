---
page_id: javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-left-variadic-destructuring-81ee3116
page_kind: source
page_family: section-reference
summary: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring: 6 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-left-variadic-destructuring-81ee3116@9a5d908d87bd678472b4669f70f12522
---

# Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-d00f2bc0]] - broader source section: Recipes with Basic Functions / Left-Variadic Functions

## Statements

- Gathering arguments for functions is one of the ways JavaScript can destructure arrays. Another way is when assigning variables, like this: _(javascriptallonge.pdf (source-range-7239e085-00741))_
- With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function. _(javascriptallonge.pdf (source-range-7239e085-00749))_

## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00749))_

> With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00744))_

<a id="atom-technical-atom-d4f8344d063d56ba"></a>

```
const [...butLast, last] = ['why', 'hello', 'there', 'little', 'droid'];
//=> Unexpected token
```
