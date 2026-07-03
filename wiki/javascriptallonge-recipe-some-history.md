---
page_id: javascriptallonge-recipe-some-history
page_kind: recipe
page_family: recipe-pattern
summary: some history: reusable source-backed pattern with 16 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: some-history
projection_coverage: recipe-javascriptallonge-recipe-some-history@29585442fbb8df6cd7416ae4c6dbc432
---

# some history

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-garbage-garbage-everywhere-some-history-1c77955f]].
- Evidence roles: decision, constraint, definition, explanation, procedure, structured-state, example.

## Applicability And Rationale

- In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. _(javascriptallonge.pdf (source-range-7239e085-01031))_
- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. _(javascriptallonge.pdf (source-range-7239e085-01032))_
- The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells. _(javascriptallonge.pdf (source-range-7239e085-01032))_
- Lisp's basic data type is often said to be the list, but in actuality it was the 'cons cell,' the term used to describe two 15-bit values stored in one word. _(javascriptallonge.pdf (source-range-7239e085-01032))_
- Lists were represented as linked lists of cons cells, with each cell's head pointing to an element and the tail pointing to another cons cell. _(javascriptallonge.pdf (source-range-7239e085-01033))_
- Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-7239e085-01034))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01036)_

```
const cons = (a, d) => [a, d],
car
= ([a, d]) => a,
cdr
= ([a, d]) => d;
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01038)_

```
const oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, null)))));
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01039)_

```
oneToFive
//=> [1,[2,[3,[4,[5,null]]]]]
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01041)_

```
const node5 = [5,null],
node4 = [4, node5],
node3 = [3, node4],
node2 = [2, node3],
node1 = [1, node2];
const oneToFive = node1;
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01043)_

```
car(oneToFive)
//=> 1
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01046)_

```
cdr(oneToFive)
//=> [2,[3,[4,[5,null]]]]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-garbage-garbage-everywhere-some-history-1c77955f]]
