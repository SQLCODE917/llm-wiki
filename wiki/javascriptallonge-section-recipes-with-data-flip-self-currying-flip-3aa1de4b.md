---
page_id: javascriptallonge-section-recipes-with-data-flip-self-currying-flip-3aa1de4b
page_kind: source
summary: Recipes with Data / Flip / self-currying flip: 3 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-data-flip-self-currying-flip-3aa1de4b@4e243ec8e7f96c370456d98f525a31b3
---

# Recipes with Data / Flip / self-currying flip

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-recipes-with-data-flip-2cae94c7]] - broader source section: Recipes with Data / Flip

## Statements

- Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip : _(javascriptallonge.pdf (source-range-7239e085-01466))_

## Technical atoms

### Technical frame 1: Recipes with Data / Flip / self-currying flip

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01466))_

> Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01467))_

```
const flip = (fn) =>
function (first, second) {
if (arguments.length === 2) {
return fn(second, first);
}
else {
return function (second) {
return fn(second, first);
};
};
};
```

### Technical frame 2: Recipes with Data / Flip / self-currying flip

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01466))_

> Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01468))_

> Nowif we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice.

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01462))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01463))_

| entry | content |
| --- | --- |
| 84 | https://github.com/raganwald/allong.es |
| 85 | http://underscorejs.org |

<details>
<summary>Raw table text</summary>

```
84 https://github.com/raganwald/allong.es
85 http://underscorejs.org
```

</details>
