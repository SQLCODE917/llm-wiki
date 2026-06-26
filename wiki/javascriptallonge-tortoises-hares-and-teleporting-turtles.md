---
page_id: javascriptallonge-tortoises-hares-and-teleporting-turtles
page_kind: source
summary: Tortoises, Hares, and Teleporting Turtles from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.164-166
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses algorithmic techniques for detecting loops in linked lists, including the Tortoise and Hare algorithm and the Teleporting Turtle algorithm.

## Key supported claims

- The Tortoise and Hare algorithm detects loops in linked lists by using two pointers moving at different speeds (raw/javascriptallonge.pdf p.164-166).
- The forceAppend function is used to create a loop in a list for testing the loop detection algorithms (raw/javascriptallonge.pdf p.164-166).
- The Teleporting Turtle algorithm is a variant that may be faster under certain circumstances (raw/javascriptallonge.pdf p.164-166).
- Both algorithms separate the concern of traversing a data structure from what to do with the elements encountered (raw/javascriptallonge.pdf p.164-166).

## Technical details

### `technical-atom-de02fda101def531` code

Citation: (raw/javascriptallonge.pdf p.164-166)

```javascript
const EMPTY = null;
```

### `technical-atom-8e4cee8ae6101044` code

Citation: (raw/javascriptallonge.pdf p.164-166)

```javascript
const isEmpty = (node) => node === EMPTY;
```

### `technical-atom-2e8c31db597723d2` code

Citation: (raw/javascriptallonge.pdf p.164-166)

```javascript
const pair = (first, rest = EMPTY) => ({first, rest}); const list = (...elements) => { const [first, ...rest] = elements; return elements.length === 0 ? EMPTY: pair(first, list(...rest)) } const forceAppend = (list1, list2) => { if (isEmpty(list1)) { return "FAIL!" } if (isEmpty(list1.rest)) { list1.rest = list2; } else { forceAppend(list1.rest, list2);
```

### `technical-atom-66a410a27125e1ea` code

Citation: (raw/javascriptallonge.pdf p.164-166)

```javascript
} } const tortoiseAndHare = (aPair) => { let tortoisePair = aPair, harePair = aPair.rest; while ( true) { if (isEmpty(tortoisePair) || isEmpty(harePair)) { return false; } if (tortoisePair.first === harePair.first) { return true; } harePair = harePair.rest; if (isEmpty(harePair)) { return false; } if (tortoisePair.first === harePair.first) { return true; } tortoisePair = tortoisePair.rest; harePair = harePair.rest; } }; const aList = list(1, 2, 3, 4, 5); tortoiseAndHare(aList) //=> false
```

### `technical-atom-3d20915cbcd4c765` code

Citation: (raw/javascriptallonge.pdf p.164-166)

```javascript
const teleportingTurtle = (list) => { let speed = 1, rabbit = list, turtle = rabbit; while ( true) { for ( let i = 0; i <= speed; i += 1) { rabbit = rabbit.rest; if (rabbit == null) { return false; } if (rabbit === turtle) { return true; } } turtle = rabbit; speed *= 2; } return false; }; const aList = list(1, 2, 3, 4, 5); teleportingTurtle(aList) //=> false forceAppend(aList, aList.rest.rest);
```

### `technical-atom-5d892367a99c2e2a` code

Citation: (raw/javascriptallonge.pdf p.164-166)

```javascript
teleportingTurtle(aList); //=> true
```

### `technical-atom-d68dc20acca48118` code

Citation: (raw/javascriptallonge.pdf p.164-166)

```javascript
const pair = (first, rest = EMPTY) => ({first, rest}); const list = (...elements) => { const [first, ...rest] = elements; return elements.length === 0 ?
```

### `technical-atom-b0354d33d6cff0e4` procedure

Citation: (raw/javascriptallonge.pdf p.164-166)

I then forgot about it for a while.

## Related technical details

### From [[javascriptallonge-functional-iterators]]: `technical-atom-9b454b81a7c87331` code

Relation: nearby source page; matched terms `data`, `function`, `structure`, `what`

Citation: (raw/javascriptallonge.pdf p.167-176)

```javascript
What we’ve done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array);. The sumFoldable function doesn’t care what kind of data structure we have, as long as it’s foldable.
```

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-aea76708de48efca` code

Relation: nearby source page; matched terms `data`, `function`, `what`

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
A constant function is a function that always returns the same thing, no matter what you give it. For example, (x) => 42 is a constant function that always evaluates to 42. The kestrel, or K, is a function that makes constant functions. You give it a value, and it returns a constant function that gives that value.
```

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-cd36d849b171aa54` code

Relation: nearby source page; matched terms `data`, `function`, `identity`

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
The identity function is a function that evaluates to whatever parameter you pass it. So I(42) => 42. Very simple, but useful. Now we’ll take it one more step forward: Passing a value to K gets a function back, and passing a value to that function gets us a value.
```

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-5c8bfdbaaac4c2b2` code

Relation: nearby source page; matched terms `data`, `interesting`, `what`

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
Now, an interesting thing happens when we pass functions to each other. Consider K(I). From what we just wrote, K(x)(y) => x So K(I)(x) => I. Makes sense. Now let’s tack one more invocation on: What is K(I)(x)(y)? If K(I)(x) => I, then K(I)(x)(y) === I(y) which is y.
```
