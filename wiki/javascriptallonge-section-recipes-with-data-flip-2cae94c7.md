---
page_id: javascriptallonge-section-recipes-with-data-flip-2cae94c7
page_kind: source
summary: Recipes with Data / Flip: 16 source-backed entries and 13 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-data-flip-2cae94c7@c230da73e417be5e7af954c73a7f9bc7
---

# Recipes with Data / Flip

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-recipes-with-data-178f0a89]] - broader source section: Recipes with Data
- [[javascriptallonge-section-recipes-with-data-flip-self-currying-flip-3aa1de4b]] - narrower source section: Recipes with Data / Flip / self-currying flip
- [[javascriptallonge-section-recipes-with-data-flip-flipping-methods-79368074]] - narrower source section: Recipes with Data / Flip / flipping methods

## Statements

- What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry : _(javascriptallonge.pdf (source-range-7239e085-01462))_
- What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-7239e085-01462))_

## Statements by subsection

### Recipes with Data / Flip / self-currying flip

- Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip : _(javascriptallonge.pdf (source-range-7239e085-01466))_

### Recipes with Data / Flip / flipping methods

- When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. A small alteration gets the job done: _(javascriptallonge.pdf (source-range-7239e085-01470))_

## Technical atoms

### Technical frame 1: Recipes with Data / Flip

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01449))_

```
const mapWith = (fn) => (list) => list.map(fn);
```

### Technical frame 2: Recipes with Data / Flip

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01451))_

```
const mapWith = (fn) => (list) => map(list, fn);
```

### Technical frame 3: Recipes with Data / Flip

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01452))_

> You can see that if we simplify it:

### Technical frame 4: Recipes with Data / Flip

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01453))_

```
const mapWith = (fn, list) => map(list, fn);
```

### Technical frame 5: Recipes with Data / Flip

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01462))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01455))_

```
const mapper = (list) => (fn) => map(list, fn);
```

### Technical frame 6: Recipes with Data / Flip

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01462))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01457))_

```
const mapWith = (fn) => (list) => map(list, fn);
```

### Technical frame 7: Recipes with Data / Flip

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01462))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01459))_

```
const mapWith = (first) => (second) => map(second, first);
```

### Technical frame 8: Recipes with Data / Flip

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01462))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01461))_

```
const wrapper = (fn) =>
(first) => (second) => fn(second, first);
```

### Technical frame 9: Recipes with Data / Flip

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01462))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01464))_

```
const flipAndCurry = (fn) =>
(first) => (second) => fn(second, first);
Sometimes you want to flip, but not curry:
const flip = (fn) =>
(first, second) => fn(second, first);
This is gold. Consider how we define mapWith now:
var mapWith = flipAndCurry(map);
Much nicer!
```

### Technical frame 10: Recipes with Data / Flip / self-currying flip

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

### Technical frame 11: Recipes with Data / Flip / self-currying flip

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01466))_

> Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01468))_

> Nowif we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice.

### Technical frame 12: Recipes with Data / Flip / flipping methods

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01470))_

> When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. A small alteration gets the job done:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01471))_

```
const flipAndCurry = (fn) =>
(first) =>
function (second) {
return fn.call(this, second, first);
}
const flip = (fn) =>
function (first, second) {
return fn.call(this, second, first);
}
const flip = (fn) =>
function (first, second) {
if (arguments.length === 2) {
return fn.call(this, second, first);
}
else {
return function (second) {
return fn.call(this, second, first);
};
};
};
```

### Technical atom 13

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
