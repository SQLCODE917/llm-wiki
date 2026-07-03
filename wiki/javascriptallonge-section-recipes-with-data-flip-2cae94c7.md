---
page_id: javascriptallonge-section-recipes-with-data-flip-2cae94c7
page_kind: source
page_family: section-reference
summary: Recipes with Data / Flip: 16 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-data-flip-2cae94c7@8e30b74fd1d6d3cf0c57217f23f9861f
---

# Recipes with Data / Flip

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-recipes-with-data-178f0a89]] - broader source section: Recipes with Data
- [[javascriptallonge-section-recipes-with-data-flip-flipping-methods-79368074]] - narrower source section: Recipes with Data / Flip / flipping methods
- [[javascriptallonge-section-recipes-with-data-flip-self-currying-flip-3aa1de4b]] - narrower source section: Recipes with Data / Flip / self-currying flip

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

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01462))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01464))_

<a id="atom-technical-atom-e40438bbd62174e0"></a>

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

### Technical frame 2: Recipes with Data / Flip / self-currying flip

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01466))_

> Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01467))_

<a id="atom-technical-atom-c08628393adc0e69"></a>

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

### Technical frame 3: Recipes with Data / Flip / self-currying flip

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01466))_

> Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01468))_

<a id="atom-technical-atom-b23695ce3f4989e7"></a>

> Nowif we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice.

### Technical frame 4: Recipes with Data / Flip / flipping methods

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01470))_

> When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. A small alteration gets the job done:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01471))_

<a id="atom-technical-atom-05c3cf12d69dbffc"></a>

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

### Technical atom 5

<a id="atom-technical-atom-f0038b4fa2ed7051"></a>

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01462))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01463))_

```text
84 https://github.com/raganwald/allong.es
85 http://underscorejs.org
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 84 | https://github.com/raganwald/allong.es |
| 85 | http://underscorejs.org |

</details>
