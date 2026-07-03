---
page_id: javascriptallonge-recipe-after-another-drink
page_kind: recipe
page_family: recipe-pattern
summary: after another drink: reusable source-backed pattern with 5 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: after-another-drink
projection_coverage: recipe-javascriptallonge-recipe-after-another-drink@ae41577609098e462d75b179d1fdaad6
---

# after another drink

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-after-another-drink-b1c5a752]].
- Evidence roles: decision, explanation, example.

## Applicability And Rationale

- A few drinks later, The Carpenter was telling his Thing story and an engineer named Kidu introduced themself. _(javascriptallonge.pdf (source-range-7239e085-01863))_
- I had a look at the code you left on the whiteboard. _(javascriptallonge.pdf (source-range-7239e085-01865))_
- Whereas the problem as stated involves a single stream of directions. _(javascriptallonge.pdf (source-range-7239e085-01866))_
- There's no benefit to constant space if finite space is sufficient. _(javascriptallonge.pdf (source-range-7239e085-01869))_
- The Carpenter stared at Kidu's solution. _(javascriptallonge.pdf (source-range-7239e085-01871))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01868)_

```
// implements Teleporting Tortoise
// cycle detection algorithm.
const hasCycle = (iterable) => {
let iterator = iterable[Symbol.iterator](),
teleportDistance = 1;
while (true) {
let {value, done} = iterator.next(),
tortoise = value;
if (done) return false;
for (let i = 0; i < teleportDistance; ++i) {
let {value, done} = iterator.next(),
hare = value;
if (done) return false;
if (tortoise === hare) return true;
}
teleportDistance *= 2;
}
return false;
};
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01870)_

```
const hasCycle = (orderedCollection) => {
const visited = new Set();
for (let element of orderedCollection) {
if (visited.has(element)) {
return true;
}
visited.add(element);
}
return false;
};
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-after-another-drink-b1c5a752]]
