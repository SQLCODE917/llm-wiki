---
page_id: javascriptallonge-copy-on-write
page_kind: source
summary: copy-on-write from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.162-163
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Copy-on-write strategy in JavaScript, including its definition, tradeoffs, and implementation in the context of immutable data structures.

## Key supported claims

- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' (raw/javascriptallonge.pdf p.162-163).
- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks (raw/javascriptallonge.pdf p.162-163).
- Like all strategies, it makes a tradeoff: It's much cheaper than pessimistically copying structures when you make an infrequent number of small changes, but if you tend to make a lot of changes to some that you aren't sharing, it's more expensive (raw/javascriptallonge.pdf p.162-163).
- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write (raw/javascriptallonge.pdf p.162-163).

## Technical details

### `technical-atom-49060aaa6b4317dc` code

Citation: (raw/javascriptallonge.pdf p.162-163)

```javascript
const parentArray = [1, 2, 3]; const [aFirst, ...childArray] = parentArray; parentArray[2] = "three"; childArray[0] = "two"; parentArray //=> [1,2,"three"] childArray //=> ["two",3] const EMPTY = { first: {}, rest: {} }; const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; const childList = parentList.rest; parentList.rest.rest.first = "three"; childList.first = "two"; parentList //=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\ {},"rest":{}}}}} childList //=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}
```

### `technical-atom-4eed4f24bf0bbdf6` code

Citation: (raw/javascriptallonge.pdf p.162-163)

```javascript
const rest = ({first, rest}) => rest; const set = (index, value, list) => index === 0 ? { first: value, rest: list.rest } : { first: list.first, rest: set(index - 1, value, list.rest) }; const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; const childList = rest(parentList); const newParentList = set(2, "three", parentList); const newChildList = set(0, "two", childList);
```

### `technical-atom-e63cf9cc59579e9b` code

Citation: (raw/javascriptallonge.pdf p.162-163)

```javascript
parentList //=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{"first":{},"rest":\ {}}}}} childList //=> {"first":2,"rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

### `technical-atom-fa08eb46591ee594` code

Citation: (raw/javascriptallonge.pdf p.162-163)

```javascript
newParentList //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\ rest":{}}}}} newChildList //=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

### `technical-atom-a0d3c2a33edd5df0` procedure

Citation: (raw/javascriptallonge.pdf p.158-159)

- When you take the rest of an array with destructuring ( [first, ...rest] ), you are given a copy of the elements of the array.

### `technical-atom-7b66382009088ae1` exception

Citation: (raw/javascriptallonge.pdf p.158-159)

But our new parent and child lists are copies that contain the desired modifications, without interfering with each other:

### `technical-atom-e64cc42cc4a0c67e` exception

Citation: (raw/javascriptallonge.pdf p.158-159)

And now functions like mapWith that make copies without modifying anything, work at full speed.

### `technical-atom-dfa4f08a62133cc5` requirement

Citation: (raw/javascriptallonge.pdf p.158-159)

Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.Wikipedia 73
