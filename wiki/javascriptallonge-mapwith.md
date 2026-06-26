---
page_id: javascriptallonge-mapwith
page_kind: source
summary: mapWith from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.193-194
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

The mapWith function is a utility that wraps around the .map method, turning any function into a mapper. It takes a function as an argument and returns a new function that applies the mapping to any array.

## Key supported claims

- mapWith is a function that wraps around the .map method, turning any function into a mapper (raw/javascriptallonge.pdf p.193-194).
- mapWith is a very convenient abstraction for a very common pattern (raw/javascriptallonge.pdf p.193-194).
- mapWith differs from map in two ways: it reverses the arguments and curries the function (raw/javascriptallonge.pdf p.193-194).
- mapWith takes the function first and the list second, and it curries the function (raw/javascriptallonge.pdf p.193-194).
- mapWith is suggested by ludicast (raw/javascriptallonge.pdf p.193-194).

## Technical details

### `technical-atom-518c200c04646775` code

Citation: (raw/javascriptallonge.pdf p.193-194)

```javascript
const map = (list, fn) => list.map(fn);
```

### `technical-atom-cc99599b4ca9f803` code

Citation: (raw/javascriptallonge.pdf p.193-194)

```javascript
const mapWith = (fn) => (list) => list.map(fn);
```

### `technical-atom-49f118af13215ae0` code

Citation: (raw/javascriptallonge.pdf p.193-194)

```javascript
That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map:
```

### `technical-atom-200a75c05e224d56` code

Citation: (raw/javascriptallonge.pdf p.193-194)

```javascript
const squaresOf = (list) => list.map(x => x * x);
```

### `technical-atom-f6351842dd2b93c1` code

Citation: (raw/javascriptallonge.pdf p.193-194)

```javascript
const squaresOf = mapWith(n => n * n);
```

### `technical-atom-3fc1386c8c65b3e6` code

Citation: (raw/javascriptallonge.pdf p.193-194)

```javascript
const squaresOf = callRight(map, (n => n * n);
```

### `technical-atom-b81c568b25c3fe2e` procedure

Citation: (raw/javascriptallonge.pdf p.193-194)

Map takes a function as an argument, and applies it to each of the elements of the array, then returns the results in another array.

### `technical-atom-3d3d5bda66c820a8` procedure

Citation: (raw/javascriptallonge.pdf p.193-194)

This recipe isn’t for map: It’s for mapWith, a function that wraps around map and turns any other function into a mapper.

## Related technical details

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-cd36d849b171aa54` code

Relation: nearby source page; matched terms `function`, `identity`, `pass`, `very`, `you`

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
The identity function is a function that evaluates to whatever parameter you pass it. So I(42) => 42. Very simple, but useful. Now we’ll take it one more step forward: Passing a value to K gets a function back, and passing a value to that function gets us a value.
```

### From [[javascriptallonge-flip]]: `technical-atom-5e12113b4bab5f1d` code

Relation: nearby source page; matched terms `function`, `map`, `mapwith`, `method`

Citation: (raw/javascriptallonge.pdf p.195-197)

```javascript
Let’s return to the implementation of mapWith that relies on a map function rather than a method:
```

### From [[javascriptallonge-copy-on-write]]: `technical-atom-0fe1e1432a76a661` code

Relation: nearby source page; matched terms `first`, `list`, `mapwith`

Citation: (raw/javascriptallonge.pdf p.158-163)

```javascript
const copy = (node, head = null, tail = null) => { if (node === EMPTY) { return head; } else if (tail === null) { const { first, rest } = node; const newNode = { first, rest }; return copy(rest, newNode, newNode); } else { const { first, rest } = node; const newNode = { first, rest }; tail.rest = newNode; return copy(node.rest, head, newNode); } } const first = ({first, rest}) => first; const rest = ({first, rest}) => rest; const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed: reverse(rest(node), { first: first(node), rest: delayed }); const mapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? reverse(delayed): mapWith(fn, rest(node), { first: fn(first(node)), rest: delayed }); const at = (index, list) => index === 0 ? first(list): at(index - 1, rest(list)); const set = (index, value, list, originalList = list) => index === 0 ? (list.first = value, originalList): set(index - 1, value, rest(list), originalList) const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY } }};
```

### From [[javascriptallonge-tortoises-hares-and-teleporting-turtles]]: `technical-atom-2e8c31db597723d2` code

Relation: nearby source page; matched terms `first`, `list`

Citation: (raw/javascriptallonge.pdf p.164-166)

```javascript
const pair = (first, rest = EMPTY) => ({first, rest}); const list = (...elements) => { const [first, ...rest] = elements; return elements.length === 0 ? EMPTY: pair(first, list(...rest)) } const forceAppend = (list1, list2) => { if (isEmpty(list1)) { return "FAIL!" } if (isEmpty(list1.rest)) { list1.rest = list2; } else { forceAppend(list1.rest, list2);
```
