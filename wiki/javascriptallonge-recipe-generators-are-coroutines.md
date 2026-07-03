---
page_id: javascriptallonge-recipe-generators-are-coroutines
page_kind: recipe
page_family: recipe-pattern
summary: generators are coroutines: reusable source-backed pattern with 15 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: generators-are-coroutines
projection_coverage: recipe-javascriptallonge-recipe-generators-are-coroutines@fb150c855f7e3514720c1a5c705a99d4
---

# generators are coroutines

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-we-ll-keep-it-simple-generators-are-coroutines-a23babe6]].
- Evidence roles: decision, procedure, explanation, constraint, example.

## Applicability And Rationale

- This is where generators behave very, very differently from ordinary functions. _(javascriptallonge.pdf (source-range-7239e085-01679))_
- - The iterator is in a nascent or 'newborn' state. _(javascriptallonge.pdf (source-range-7239e085-01681))_
- - When we call interator.next() , the body of our generator begins to be evaluated. _(javascriptallonge.pdf (source-range-7239e085-01682))_
- - The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-7239e085-01686))_
- - The iterator resumes execution from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-7239e085-01687))_
- - The body of our generator runs until it returns, ends, or encounters the next yield statement. _(javascriptallonge.pdf (source-range-7239e085-01698))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01678)_

```
const oneTwoThree = function * () {
yield 1;
yield 2;
yield 3;
};
oneTwoThree().next()
//=>
{"done":false, value: 1}
oneTwoThree().next()
//=>
{"done":false, value: 1}
oneTwoThree().next()
//=>
{"done":false, value: 1}
const iterator = oneTwoThree();
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

_Source: javascriptallonge.pdf (source-range-7239e085-01705)_

```
const oneTwoThree = function () {
let state = 'newborn';
return {
next () {
switch (state) {
case 'newborn':
state = 1;
return {value: 1};
case 1:
state = 2;
return {value: 2}
case 2:
state = 3;
return {value: 3}
case 3:
return {done: true};
}
}
}
};
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-we-ll-keep-it-simple-generators-are-coroutines-a23babe6]]
