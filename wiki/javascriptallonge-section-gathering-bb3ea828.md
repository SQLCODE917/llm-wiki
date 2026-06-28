---
page_id: javascriptallonge-section-gathering-bb3ea828
page_kind: source
summary: gathering: 7 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-gathering-bb3ea828@1ea181ea9d3e8a260d028dbc639e1ab4
---

# gathering

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-gathering]] - topic hub: opens the topic page for Gathering

## Statements

- Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array: _(javascriptallonge.pdf (source-range-31a4cf47-00853))_
- car and cdr 57 are archaic terms that go back to an implementation of Lisp running on the IBM 704 computer. Some other languages call them first and butFirst , or head and tail . We will use a common convention and call variables we gather rest , but refer to the ... operation as a 'gather,' following Kyle Simpson's example. 58 _(javascriptallonge.pdf (source-range-31a4cf47-00855))_
- Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write _(javascriptallonge.pdf (source-range-31a4cf47-00856))_

## Technical atoms

### Technical frame 1: gathering

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00855))_

> car and cdr 57 are archaic terms that go back to an implementation of Lisp running on the IBM 704 computer. Some other languages call them first and butFirst , or head and tail . We will use a common convention and call variables we gather rest , but refer to the ... operation as a 'gather,' following Kyle Simpson's example. 58

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00854))_

```
const [car, ...cdr] = [1, 2, 3, 4, 5]; car //=> 1 cdr //=> [2, 3, 4, 5]
```

### Technical frame 2: gathering

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00856))_

> Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00858))_

```
const [...butLast, last] = [1, 2, 3, 4, 5]; //=> ERROR const [first, ..., last] = [1, 2, 3, 4, 5]; //=> ERROR Now, when we introduced destructuring, we saw that it is kind-of-sort-of the reverse of array literals. So if const wrapped = [something]; Then: const [unwrapped] = something; What is the reverse of gathering? We know that: const [car, ...cdr] = [1, 2, 3, 4, 5]; What is the reverse? It would be: const cons = [car, ...cdr]; oneTwoThree = ["one", "two", "three"];
```

### Technical frame 3: gathering

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00856))_

> Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00859))_

```
Let's try it: const ["zero", ...oneTwoThree] //=> ["zero","one","two","three"]
```

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00856))_

> Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00857))_

| entry | content |
| --- | --- |
| 57 | https://en.wikipedia.org/wiki/CAR_and_CDR |
| 58 | Kyle Simpson is the author of You Don't Know JS, available here |

<details>
<summary>Raw table text</summary>

```
57 https://en.wikipedia.org/wiki/CAR_and_CDR
58 Kyle Simpson is the author of You Don't Know JS, available here
```

</details>
