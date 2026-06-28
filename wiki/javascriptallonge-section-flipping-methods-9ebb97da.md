---
page_id: javascriptallonge-section-flipping-methods-9ebb97da
page_kind: source
summary: flipping methods: 2 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-flipping-methods-9ebb97da@167031c75cd5e76d5cf9cc0682623678
---

# flipping methods

From [[javascriptallonge]].

## Statements

- When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. A small alteration gets the job done: _(javascriptallonge.pdf (source-range-31a4cf47-01470))_

## Technical atoms

### Technical frame 1: flipping methods

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01470))_

> When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. A small alteration gets the job done:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01471))_

```
const flipAndCurry = (fn) => (first) => function (second) { return fn.call( this , second, first); } const flip = (fn) => function (first, second) { return fn.call( this , second, first); } const flip = (fn) => function (first, second) { if (arguments.length === 2) { return fn.call( this , second, first); } else { return function (second) { return fn.call( this , second, first); }; }; };
```

### Technical atom 2

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
