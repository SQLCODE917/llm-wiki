---
page_id: javascriptallonge-section-iterating-fdda74e7
page_kind: source
summary: iterating: 16 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-iterating-fdda74e7@9a71d283b6554c678dd2734cef08c0e6
---

# iterating

From [[javascriptallonge]].

## Statements

- Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. Nevertheless, there is some value in being able to express some algorithms as iteration. _(javascriptallonge.pdf (source-range-8eb13d6b-01284))_
- JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with: _(javascriptallonge.pdf (source-range-8eb13d6b-01285))_
- Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 . _(javascriptallonge.pdf (source-range-8eb13d6b-01287))_
- Notice that buried inside our loop, we have bound the names done and value . We can put those into a POJO (a Plain Old JavaScript Object). It'll be a little awkward, but we'll be patient: _(javascriptallonge.pdf (source-range-8eb13d6b-01290))_
- Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } . _(javascriptallonge.pdf (source-range-8eb13d6b-01293))_
- We can write a different iterator for a different data structure. Here's one for linked lists: _(javascriptallonge.pdf (source-range-8eb13d6b-01294))_
- Notice that buried inside our loop, we have bound the names done and value . _(javascriptallonge.pdf (source-range-8eb13d6b-01290))_

## Technical atoms

### Technical frame 1: iterating

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01287))_

> Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01286))_

```
const arraySum = (array) => { let sum = 0; for ( let i = 0; i < array.length; ++i) { sum += array[i]; } return sum } arraySum([1, 4, 9, 16, 25]) //=> 55
```

### Technical frame 2: iterating

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01290))_

> Notice that buried inside our loop, we have bound the names done and value . We can put those into a POJO (a Plain Old JavaScript Object). It'll be a little awkward, but we'll be patient:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01289))_

```
const arraySum = (array) => { let done, sum = 0, i = 0; while ((done = i == array.length, !done)) { const value = array[i++]; sum += value; } return sum } arraySum([1, 4, 9, 16, 25]) //=> 55
```

### Technical frame 3: iterating

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01293))_

> Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01291))_

```
const arraySum = (array) => { let iter, sum = 0, index = 0; while ( (eachIteration = { done: index === array.length, value: index < array.length ? array[index] : undefined }, ++index, !eachIteration.done) ) { sum += eachIteration.value; } return sum; } arraySum([1, 4, 9, 16, 25]) //=> 55 With this code, we make a POJO that has done and value keys. All the summing code needs to know is to add eachIteration.value . Now we can extract the ickiness into a separate function: const arrayIterator = (array) => { let i = 0; return () => { const done = i === array.length; return { done, value: done ? undefined : array[i++] } } } const iteratorSum = (iterator) => { let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) {
```

### Technical frame 4: iterating

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01293))_

> Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01292))_

```
sum += eachIteration.value; } return sum; } iteratorSum(arrayIterator([1, 4, 9, 16, 25])) //=> 55
```

### Technical frame 5: iterating

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01294))_

> We can write a different iterator for a different data structure. Here's one for linked lists:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01295))_

```
const EMPTY = null ; const isEmpty = (node) => node === EMPTY; const pair = (first, rest = EMPTY) => ({first, rest}); const list = (...elements) => { const [first, ...rest] = elements; return elements.length === 0 ? EMPTY : pair(first, list(...rest)) } const print = (aPair) => isEmpty(aPair) ? "" : ` ${ aPair.first } ${ print(aPair.rest) } ` const listIterator = (aPair) => () => { const done = isEmpty(aPair); if (done) { return {done}; } else { const {first, rest} = aPair; aPair = aPair.rest;
```

### Technical frame 6: iterating

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01294))_

> We can write a different iterator for a different data structure. Here's one for linked lists:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01296))_

```
return { done, value: first } } } const iteratorSum = (iterator) => { let eachIteration, sum = 0;; while ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } return sum } const aListIterator = listIterator(list(1, 4, 9, 16, 25)); iteratorSum(aListIterator) //=> 55
```
