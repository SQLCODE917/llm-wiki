---
page_id: javascriptallonge-a-few-utilities
page_kind: source
summary: a few utilities from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.159-161
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on a few utilities in JavaScriptAllonge, covering list manipulation functions.

## Key supported claims

- The section defines linked-list helpers including copy, first, rest, reverse, mapWith, at, and set (raw/javascriptallonge.pdf p.159-161).
- The set function modifies an element at a specific index in a linked list (raw/javascriptallonge.pdf p.159-161).
- The at function accesses an element at a specific index in a linked list (raw/javascriptallonge.pdf p.159-161).

## Technical details

### `technical-atom-7d32301f2d7c15dd` code

Citation: (raw/javascriptallonge.pdf p.159-161)

```javascript
const copy = (node, head = null , tail = null ) => { if (node === EMPTY) { return head; } else if (tail === null ) { const { first, rest } = node; const newNode = { first, rest }; return copy(rest, newNode, newNode); } else { const { first, rest } = node; const newNode = { first, rest }; tail.rest = newNode; return copy(node.rest, head, newNode); } } const first = ({first, rest}) => first; const rest = ({first, rest}) => rest; const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(rest(node), { first: first(node), rest: delayed }); const mapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? reverse(delayed) : mapWith(fn, rest(node), { first: fn(first(node)), rest: delayed }); const at = (index, list) => index === 0 ? first(list) : at(index - 1, rest(list)); const set = (index, value, list, originalList = list) => index === 0 ? (list.first = value, originalList) : set(index - 1, value, rest(list), originalList) const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }};
```

### `technical-atom-03f3035e8bba95aa` code

Citation: (raw/javascriptallonge.pdf p.159-161)

```javascript
const childList = rest(parentList); set(2, "three", parentList); set(0, "two", childList); parentList //=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\ {},"rest":{}}}}} childList //=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}
```

### `technical-atom-ebfedc34c9ef8cf7` code

Citation: (raw/javascriptallonge.pdf p.159-161)

```
delayed : reverse(rest(node), { first: first(node), rest: delayed }); const mapWith = (fn, node, delayed = EMPTY) => node === EMPTY ?
```

### `technical-atom-490e44302ed3a6a8` code

Citation: (raw/javascriptallonge.pdf p.159-161)

```
reverse(delayed) : mapWith(fn, rest(node), { first: fn(first(node)), rest: delayed }); const at = (index, list) => index === 0 ?
```

### `technical-atom-def42d43baa824ad` code

Citation: (raw/javascriptallonge.pdf p.159-161)

```
first(list) : at(index - 1, rest(list)); const set = (index, value, list, originalList = list) => index === 0 ?
```
