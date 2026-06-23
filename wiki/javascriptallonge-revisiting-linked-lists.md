---
page_id: javascriptallonge-revisiting-linked-lists
page_kind: source
summary: revisiting linked lists from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.137-140
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on revisiting linked lists in JavaScript Allongé, focusing on list traversal, mapping, and performance.

## Key supported claims

- Linked lists can be implemented using objects with `first` and `rest` properties, as opposed to two-element arrays. (raw/javascriptallonge.pdf p.137-140)
- The performance of list operations depends on how they are implemented; for example, mapping over a list can be done in a way that requires iterating twice, leading to higher time and memory complexity. (raw/javascriptallonge.pdf p.137-140)
- The `reverse` function is used to reverse a list, which is necessary for correctly mapping over lists when the implementation iterates in reverse. (raw/javascriptallonge.pdf p.137-140)

## Technical details

### `technical-atom-e7aa6f3f69b944ac` code

Citation: (raw/javascriptallonge.pdf p.137-140)

```javascript
const cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;
```

### `technical-atom-d944f4a4388f022e` code

Citation: (raw/javascriptallonge.pdf p.137-140)

```
In that case, a linked list of the numbers 1 , 2 , and 3 will look like this: { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY } } } . We can then perform the equivalent of [first, ...rest] with direct property accessors:
```

### `technical-atom-98e27802789dc8da` code

Citation: (raw/javascriptallonge.pdf p.137-140)

```javascript
const EMPTY = {}; const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } }; OneTwoThree.first //=> 1 OneTwoThree.rest //=> {"first":2,"rest":{"first":3,"rest":{}}} OneTwoThree.rest.rest.first //=> 3 Taking the length of a linked list is easy: const length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1); length(OneTwoThree) //=> 3
```

### `technical-atom-f58f9106e0f75fc7` code

Citation: (raw/javascriptallonge.pdf p.137-140)

```javascript
const slowcopy = (node) => node === EMPTY ? EMPTY : { first: node.first, rest: slowcopy(node.rest)}; slowcopy(OneTwoThree) //=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{}}}}
```

### `technical-atom-6312b62d26a49e8e` code

Citation: (raw/javascriptallonge.pdf p.137-140)

```javascript
const copy2 = (node, delayed = EMPTY) => node === EMPTY ? delayed : copy2(node.rest, { first: node.first, rest: delayed }); copy2(OneTwoThree) //=> {"first":3,"rest":{"first":2,"rest":{"first":1,"rest":{}}}}
```

### `technical-atom-cc1c838438cd5fc7` code

Citation: (raw/javascriptallonge.pdf p.137-140)

```javascript
const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); And now, we can make a reversing map: const reverseMapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? delayed : reverseMapWith(fn, node.rest, { first: fn(node.first), rest: delayed }); reverseMapWith((x) => x * x, OneTwoThree) //=> {"first":9,"rest":{"first":4,"rest":{"first":1,"rest":{}}}} And a regular mapWith follows: const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); const mapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? reverse(delayed) : mapWith(fn, node.rest, { first: fn(node.first), rest: delayed }); mapWith((x) => x * x, OneTwoThree) //=> {"first":1,"rest":{"first":4,"rest":{"first":9,"rest":{}}}}
```

### `technical-atom-fab4324cdd6577a6` code

Citation: (raw/javascriptallonge.pdf p.137-140)

```
So our linked list nodes will be formed from { first, rest }
```

### `technical-atom-756042e76abd0569` procedure

Citation: (raw/javascriptallonge.pdf p.137-140)

So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return.
