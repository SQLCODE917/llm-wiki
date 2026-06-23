---
page_id: javascriptallonge-say-please
page_kind: source
summary: say 'please' from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.186-188
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on using functions as data structures in JavaScript, focusing on 'say please' pattern

## Key supported claims

- This follows the philosophy we used with data structures: The function doing the work inspects the data structure (raw/javascriptallonge.pdf p.186-188).
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us (raw/javascriptallonge.pdf p.186-188).
- Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs (raw/javascriptallonge.pdf p.186-188).

## Technical details

### `technical-atom-9e920918a4a492fa` code

Citation: (raw/javascriptallonge.pdf p.186-188)

```javascript
const length = (aPair) => aPair === EMPTY ? 0 : 1 + length(aPair(rest));
```

### `technical-atom-6f7c0b0ea78aa3e5` code

Citation: (raw/javascriptallonge.pdf p.186-188)

```javascript
const length = (list) => list( () => 0, (aPair) => 1 + length(aPair(rest))) );
```

### `technical-atom-c47b5f0df66e9a95` code

Citation: (raw/javascriptallonge.pdf p.186-188)

```javascript
const pairFirst = K, pairRest = K(I), pair = V; const first = (list) => list( () => "ERROR: Can't take first of an empty list", (aPair) => aPair(pairFirst) ); const rest = (list) => list(
```

### `technical-atom-b1a9bad2fb37cbf4` code

Citation: (raw/javascriptallonge.pdf p.186-188)

```javascript
() => "ERROR: Can't take first of an empty list", (aPair) => aPair(pairRest) ); const length = (list) => list( () => 0, (aPair) => 1 + length(aPair(pairRest))) ); We'll also write a handy list printer: const print = (list) => list( () => "", (aPair) => ` ${ aPair(pairFirst) } ${ print(aPair(pairRest)) } ` ); How would all this work? Let's start with the obvious. What is an empty list? const EMPTYLIST = (whenEmpty, unlessEmpty) => whenEmpty() And what is a node of a list? const node = (x) => (y) => (whenEmpty, unlessEmpty) => unlessEmpty(pair(x)(y)); Let's try it: const l123 = node(1)(node(2)(node(3)(EMPTYLIST))); print(l123) //=> 1 2 3
```

### `technical-atom-0174c35337cda35a` code

Citation: (raw/javascriptallonge.pdf p.186-188)

```javascript
const reverse = (list, delayed = EMPTYLIST) => list( () => delayed, (aPair) => reverse(aPair(pairRest), node(aPair(pairFirst))(delayed)) ); print(reverse(l123)); //=> 3 2 1 const mapWith = (fn, list, delayed = EMPTYLIST) => list( () => reverse(delayed), (aPair) => mapWith(fn, aPair(pairRest), node(fn(aPair(pairFirst)))(delayed)) ); print(mapWith(x => x * x, reverse(l123))) //=> 941
```

### `technical-atom-879cf8e8076dd2ee` procedure

Citation: (raw/javascriptallonge.pdf p.186-188)

We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us.

### `technical-atom-1e695cff5ef7c0b7` code

Citation: (raw/javascriptallonge.pdf p.186-188)

```
const EMPTYLIST = (whenEmpty, unlessEmpty) => whenEmpty() And what is a node of a list?
```
