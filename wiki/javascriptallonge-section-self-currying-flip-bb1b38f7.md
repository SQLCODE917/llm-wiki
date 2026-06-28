---
page_id: javascriptallonge-section-self-currying-flip-bb1b38f7
page_kind: source
summary: self-currying flip: 3 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-self-currying-flip-bb1b38f7@c94fe5bfbbaa620eade6a2226f7271d8
---

# self-currying flip

From [[javascriptallonge]].

## Statements

- Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip : _(javascriptallonge.pdf (source-range-31a4cf47-01466))_

## Technical atoms

### Technical frame 1: self-currying flip

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01466))_

> Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01467))_

```
const flip = (fn) => function (first, second) { if (arguments.length === 2) { return fn(second, first); } else { return function (second) { return fn(second, first); }; }; };
```

### Technical frame 2: self-currying flip

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01466))_

> Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01468))_

> Nowif we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice.

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01462))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01463))_

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
