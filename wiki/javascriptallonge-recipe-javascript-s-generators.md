---
page_id: javascriptallonge-recipe-javascript-s-generators
page_kind: recipe
page_family: recipe-pattern
summary: javascript's generators: reusable source-backed pattern with 8 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: javascript-s-generators
projection_coverage: recipe-javascriptallonge-recipe-javascript-s-generators@62967754aba7ec095eaa75b8eb8e35cd
---

# javascript's generators

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-we-ll-keep-it-simple-javascript-s-generators-a7436505]].
- Evidence roles: decision, constraint, procedure, explanation, example, structured-state.

## Applicability And Rationale

- It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator. _(javascriptallonge.pdf (source-range-7239e085-01661))_
- Given the title of this chapter, it is not a surprise that JavaScript makes this possible. _(javascriptallonge.pdf (source-range-7239e085-01661))_
- We can write an iterator, but use a generation style of programming. _(javascriptallonge.pdf (source-range-7239e085-01662))_
- An iterator written in a generation style is called a generator . _(javascriptallonge.pdf (source-range-7239e085-01662))_
- This makes sense, because empty never yields anything. _(javascriptallonge.pdf (source-range-7239e085-01667))_
- Generator functions can take an argument. _(javascriptallonge.pdf (source-range-7239e085-01668))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01666)_

```
function * empty () {};
empty().next()
//=>
{"done":true}
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01670)_

```
function * only (something) {
yield something;
};
only("you").next()
//=>
{"done":false, value: "you"}
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01672)_

```
only("you").next()
//=>
{"done":false, value: "you"}
only("the lonely").next()
//=>
{"done":false, value: "the lonely"}
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01674)_

```
const sixteen = only("sixteen");
sixteen.next()
//=>
{"done":false, value: "sixteen"}
sixteen.next()
//=>
{"done":true}
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-we-ll-keep-it-simple-javascript-s-generators-a7436505]]
