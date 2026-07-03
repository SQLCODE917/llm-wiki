---
page_id: javascriptallonge-recipe-copy-on-read
page_kind: recipe
page_family: recipe-pattern
summary: copy-on-read: reusable source-backed pattern with 7 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: copy-on-read
projection_coverage: recipe-javascriptallonge-recipe-copy-on-read@6eb99a4752eb6d4173bc52cc36da4450
---

# copy-on-read

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-yes-consider-this-variation-copy-on-write-copy-on-read-4f68c68b]].
- Evidence roles: decision, constraint, explanation, example.

## Applicability And Rationale

- Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-7239e085-01239))_
- One strategy for avoiding problems is to be pessimistic . _(javascriptallonge.pdf (source-range-7239e085-01239))_
- Thereafter, we can write to the parent or the copy of the child freely. _(javascriptallonge.pdf (source-range-7239e085-01241))_
- This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. _(javascriptallonge.pdf (source-range-7239e085-01241))_
- As we expected, making a copy lets us modify the copy without interfering with the original. _(javascriptallonge.pdf (source-range-7239e085-01242))_
- Our mapWith function would be very expensive if we make a copy every time we call rest(node) . _(javascriptallonge.pdf (source-range-7239e085-01242))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01240)_

```
const rest = ({first, rest}) => copy(rest);
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
const childList = rest(parentList);
const newParentList = set(2, "three", parentList);
set(0, "two", childList);
parentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\
rest":{}}}}}
childList
//=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-yes-consider-this-variation-copy-on-write-copy-on-read-4f68c68b]]
