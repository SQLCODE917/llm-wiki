---
page_id: javascriptallonge-section-a-few-utilities-7ab880aa
page_kind: source
summary: a few utilities: 3 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-few-utilities-7ab880aa@4593c2b6129c5776faeef8f8cab31718
---

# a few utilities

From [[javascriptallonge]].

## Statements

- Our new at and set functions behave similarly to array[index] and array[index] = value . The main difference is that array[index] = value evaluates to value , while set(index, value, list) evaluates to the modified list . _(javascriptallonge.pdf (source-range-31a4cf47-01237))_

## Technical atoms

### Technical frame 1: a few utilities

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01237))_

> Our new at and set functions behave similarly to array[index] and array[index] = value . The main difference is that array[index] = value evaluates to value , while set(index, value, list) evaluates to the modified list .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01235))_

```
const copy = (node, head = null , tail = null ) => { if (node === EMPTY) { return head; } else if (tail === null ) { const { first, rest } = node; const newNode = { first, rest }; return copy(rest, newNode, newNode); } else { const { first, rest } = node; const newNode = { first, rest }; tail.rest = newNode; return copy(node.rest, head, newNode); } } const first = ({first, rest}) => first; const rest = ({first, rest}) => rest; const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(rest(node), { first: first(node), rest: delayed }); const mapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? reverse(delayed) : mapWith(fn, rest(node), { first: fn(first(node)), rest: delayed }); const at = (index, list) => index === 0 ? first(list) : at(index - 1, rest(list)); const set = (index, value, list, originalList = list) => index === 0 ? (list.first = value, originalList) : set(index - 1, value, rest(list), originalList) const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }};
```

### Technical frame 2: a few utilities

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01237))_

> Our new at and set functions behave similarly to array[index] and array[index] = value . The main difference is that array[index] = value evaluates to value , while set(index, value, list) evaluates to the modified list .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01236))_

```
const childList = rest(parentList); set(2, "three", parentList); set(0, "two", childList); parentList //=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\ {},"rest":{}}}}} childList //=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}
```
