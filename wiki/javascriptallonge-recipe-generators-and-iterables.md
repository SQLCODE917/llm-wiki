---
page_id: javascriptallonge-recipe-generators-and-iterables
page_kind: recipe
page_family: recipe-pattern
summary: generators and iterables: reusable source-backed pattern with 7 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: generators-and-iterables
projection_coverage: recipe-javascriptallonge-recipe-generators-and-iterables@280294123965ecea3e18549533eb3662
---

# generators and iterables

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-we-ll-keep-it-simple-generators-and-iterables-4c3f39e4]].
- Evidence roles: decision, constraint, explanation, structured-state, example.

## Applicability And Rationale

- Our generator function oneTwoThree is not an iterator. _(javascriptallonge.pdf (source-range-7239e085-01708))_
- As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3 . _(javascriptallonge.pdf (source-range-7239e085-01709))_
- Recalling the way we wrote ordered collections, we could make a collection that uses a generator function: _(javascriptallonge.pdf (source-range-7239e085-01709))_
- This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects: _(javascriptallonge.pdf (source-range-7239e085-01712))_
- This object declares a [Symbol.iterator] function that makes it iterable. _(javascriptallonge.pdf (source-range-7239e085-01714))_
- Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-7239e085-01714))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01710)_

```
const ThreeNumbers = {
[Symbol.iterator]: function * () {
yield 1;
yield 2;
yield 3
}
}
for (const i of ThreeNumbers) {
console.log(i);
}
//=>
1
2
3
[...ThreeNumbers]
//=>
[1,2,3]
const iterator = ThreeNumbers[Symbol.iterator]();
iterator.next()
//=>
{"done":false, value: 1}
iterator.next()
//=>
{"done":false, value: 2}
iterator.next()
//=>
{"done":false, value: 3}
iterator.next()
//=>
{"done":true}
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01713)_

```
const ThreeNumbers = {
*[Symbol.iterator] () {
yield 1;
yield 2;
yield 3
}
}
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-we-ll-keep-it-simple-generators-and-iterables-4c3f39e4]]
