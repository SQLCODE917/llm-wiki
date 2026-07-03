---
page_id: javascriptallonge-recipe-state-machines
page_kind: recipe
page_family: recipe-pattern
summary: state machines: reusable source-backed pattern with 6 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: state-machines
projection_coverage: recipe-javascriptallonge-recipe-state-machines@5656eeef7de81668e9991961dab91802
---

# state machines

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-like-this-generating-iterables-state-machines-774a067e]].
- Evidence roles: decision, constraint, procedure, explanation, example.

## Applicability And Rationale

- Some iterables can be modelled as state machines. _(javascriptallonge.pdf (source-range-7239e085-01646))_
- - The first element of the fibonacci sequence is zero. _(javascriptallonge.pdf (source-range-7239e085-01647))_
- - The second element of the fibonacci sequence is one. _(javascriptallonge.pdf (source-range-7239e085-01648))_
- - Every subsequent element of the fibonacci sequence is the sum of the previous two elements. _(javascriptallonge.pdf (source-range-7239e085-01649))_
- This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 : _(javascriptallonge.pdf (source-range-7239e085-01653))_
- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. _(javascriptallonge.pdf (source-range-7239e085-01653))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01651)_

```
// Generation
const fibonacci = () => {
let a, b;
console.log(a = 0);
console.log(b = 1);
while (true) {
[a, b] = [b, a + b];
console.log(b);
}
}
fibonacci()
//=>
0
1
1
2
3
5
8
13
21
34
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01652)_

```
55
89
144
...
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-like-this-generating-iterables-state-machines-774a067e]]
