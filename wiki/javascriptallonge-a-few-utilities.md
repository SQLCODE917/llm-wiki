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

## Related technical details

### From [[javascriptallonge-copy-on-write]]: `technical-atom-4eed4f24bf0bbdf6` code

Relation: nearby source page; matched terms `copy`, `first`, `index`, `list`, `rest`, `set`

Citation: (raw/javascriptallonge.pdf p.162-163)

```javascript
const rest = ({first, rest}) => rest; const set = (index, value, list) => index === 0 ? { first: value, rest: list.rest } : { first: list.first, rest: set(index - 1, value, list.rest) }; const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; const childList = rest(parentList); const newParentList = set(2, "three", parentList); const newChildList = set(0, "two", childList);
```

### From [[javascriptallonge-iterating]]: `technical-atom-16b403e6c3a4e278` code

Relation: nearby source page; matched terms `array`, `function`, `index`, `value`

Citation: (raw/javascriptallonge.pdf p.169-172)

```javascript
const arraySum = (array) => { let iter, sum = 0, index = 0; while ( (eachIteration = { done: index === array.length, value: index < array.length ? array[index] : undefined }, ++index, !eachIteration.done) ) { sum += eachIteration.value; } return sum; } arraySum([1, 4, 9, 16, 25]) //=> 55 With this code, we make a POJO that has done and value keys. All the summing code needs to know is to add eachIteration.value . Now we can extract the ickiness into a separate function: const arrayIterator = (array) => { let i = 0; return () => { const done = i === array.length; return { done, value: done ? undefined : array[i++] } } } const iteratorSum = (iterator) => { let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) {
```

### From [[javascriptallonge-copy-on-read]]: `technical-atom-173bdbccb7a23701` code

Relation: nearby source page; matched terms `copy`, `first`, `rest`, `set`

Citation: (raw/javascriptallonge.pdf p.161)

```javascript
const rest = ({first, rest}) => copy(rest); const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; const childList = rest(parentList); const newParentList = set(2, "three", parentList); set(0, "two", childList); parentList //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\ rest":{}}}}} childList //=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

### From [[javascriptallonge-copy-on-write]]: `technical-atom-a0d3c2a33edd5df0` procedure

Relation: nearby source page; matched terms `array`, `copy`, `first`, `rest`

Citation: (raw/javascriptallonge.pdf p.158-159)

- When you take the rest of an array with destructuring ( [first, ...rest] ), you are given a copy of the elements of the array.
