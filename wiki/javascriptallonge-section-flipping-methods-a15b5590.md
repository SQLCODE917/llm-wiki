---
page_id: javascriptallonge-section-flipping-methods-a15b5590
page_kind: source
summary: flipping methods: 2 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-flipping-methods-a15b5590@90d24a606786b4b3ed29b7e02c47ce3e
---

# flipping methods

From [[javascriptallonge]].

## Statements

- When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. A small alteration gets the job done: _(javascriptallonge.pdf (source-range-8eb13d6b-01469))_

## Technical atoms

### Technical frame 1: flipping methods

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01469))_

> When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. A small alteration gets the job done:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01470))_

```
const flipAndCurry = (fn) => (first) => function (second) { return fn.call( this , second, first); } const flip = (fn) => function (first, second) { return fn.call( this , second, first); } const flip = (fn) => function (first, second) { if (arguments.length === 2) { return fn.call( this , second, first); } else { return function (second) { return fn.call( this , second, first); }; }; };
```

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01461))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01462))_

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
