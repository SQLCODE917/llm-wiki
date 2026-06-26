---
page_id: javascriptallonge-copy-on-write
page_kind: source
summary: Copy on Write from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.158-163
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

Summary of the copy-on-write strategy in JavaScript as described in 'Composing and Decomposing Data'.

## Key supported claims

- Copy-on-write delays copying until a modification is made, making it efficient for infrequent changes (raw/javascriptallonge.pdf p.158-163).
- Arrays create copies when taking their rest, unlike linked lists which share nodes (raw/javascriptallonge.pdf p.158-163).
- COW is a strategy where modifications trigger copying, avoiding unnecessary copying when changes are rare (raw/javascriptallonge.pdf p.158-163).
- Copy-on-write avoids expensive copying when modifications are infrequent, but is more expensive if many changes are made to shared structures (raw/javascriptallonge.pdf p.158-163).
- COW is a policy where changes to shared information trigger a separate copy to prevent interference (raw/javascriptallonge.pdf p.158-163).

## Technical details

### `technical-atom-54e6116cecef1af1` code

Citation: (raw/javascriptallonge.pdf p.158-163)

```javascript
const parentArray = [1, 2, 3]; const [aFirst, ...childArray] = parentArray; parentArray[2] = "three"; childArray[0] = "two"; parentArray //=> [1,2,"three"] childArray //=> ["two",3] const EMPTY = { first: {}, rest: {} }; const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY } }}; const childList = parentList.rest;
```

### `technical-atom-ac9a28617e67a002` code

Citation: (raw/javascriptallonge.pdf p.158-163)

```javascript
parentList //=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first": {},"rest":{}}}}} childList //=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}
```

### `technical-atom-0fe1e1432a76a661` code

Citation: (raw/javascriptallonge.pdf p.158-163)

```javascript
const copy = (node, head = null, tail = null) => { if (node === EMPTY) { return head; } else if (tail === null) { const { first, rest } = node; const newNode = { first, rest }; return copy(rest, newNode, newNode); } else { const { first, rest } = node; const newNode = { first, rest }; tail.rest = newNode; return copy(node.rest, head, newNode); } } const first = ({first, rest}) => first; const rest = ({first, rest}) => rest; const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed: reverse(rest(node), { first: first(node), rest: delayed }); const mapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? reverse(delayed): mapWith(fn, rest(node), { first: fn(first(node)), rest: delayed }); const at = (index, list) => index === 0 ? first(list): at(index - 1, rest(list)); const set = (index, value, list, originalList = list) => index === 0 ? (list.first = value, originalList): set(index - 1, value, rest(list), originalList) const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY } }};
```

### `technical-atom-6ab21eefa3796c38` code

Citation: (raw/javascriptallonge.pdf p.158-163)

```javascript
const childList = rest(parentList);
```

### `technical-atom-28df9877195450e5` code

Citation: (raw/javascriptallonge.pdf p.158-163)

```javascript
set(2, "three", parentList); set(0, "two", childList); parentList //=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first": {},"rest":{}}}}} childList //=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}
```

### `technical-atom-097dfa574b91305a` code

Citation: (raw/javascriptallonge.pdf p.158-163)

```javascript
const rest = ({first, rest}) => copy(rest);
```

### `technical-atom-d07d1bc6b13e8f28` code

Citation: (raw/javascriptallonge.pdf p.158-163)

```javascript
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY } }}; const childList = rest(parentList); const newParentList = set(2, "three", parentList); set(0, "two", childList);
```

### `technical-atom-e352b06556f0fbd5` formula

Citation: (raw/javascriptallonge.pdf p.158-163)

parentList.rest.rest.first = "three"; childList.first = "two";

## Related technical details

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-cd36d849b171aa54` code

Relation: nearby source page; matched terms `but`, `data`, `function`, `identity`, `making`, `more`

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
The identity function is a function that evaluates to whatever parameter you pass it. So I(42) => 42. Very simple, but useful. Now we’ll take it one more step forward: Passing a value to K gets a function back, and passing a value to that function gets us a value.
```

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-5c8bfdbaaac4c2b2` code

Relation: nearby source page; matched terms `data`, `making`, `more`, `when`, `which`

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
Now, an interesting thing happens when we pass functions to each other. Consider K(I). From what we just wrote, K(x)(y) => x So K(I)(x) => I. Makes sense. Now let’s tack one more invocation on: What is K(I)(x)(y)? If K(I)(x) => I, then K(I)(x)(y) === I(y) which is y.
```

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-aea76708de48efca` code

Relation: nearby source page; matched terms `data`, `function`, `making`, `you`

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
A constant function is a function that always returns the same thing, no matter what you give it. For example, (x) => 42 is a constant function that always evaluates to 42. The kestrel, or K, is a function that makes constant functions. You give it a value, and it returns a constant function that gives that value.
```

### From [[javascriptallonge-functional-iterators]]: `technical-atom-9b454b81a7c87331` code

Relation: nearby source page; matched terms `array`, `data`, `function`

Citation: (raw/javascriptallonge.pdf p.167-176)

```javascript
What we’ve done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array);. The sumFoldable function doesn’t care what kind of data structure we have, as long as it’s foldable.
```
