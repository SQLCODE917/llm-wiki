---
page_id: javascriptallonge-iterating
page_kind: source
summary: iterating from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.169-172
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses the concept of iteration in JavaScript, emphasizing that while folding is a universal operation, there is still value in expressing algorithms as iteration. It explores the use of for loops and while loops for summing array elements, and introduces the concept of iterators.

## Key supported claims

- Once again, we're mixing the code for iterating over an array with the code for calculating a sum. (raw/javascriptallonge.pdf p.169-172)
- And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0. (raw/javascriptallonge.pdf p.169-172)
- We can write this a slightly different way, using a while loop. (raw/javascriptallonge.pdf p.169-172)

## Technical details

### `technical-atom-515f295a0aab7df3` code

Citation: (raw/javascriptallonge.pdf p.169-172)

```javascript
const arraySum = (array) => { let sum = 0; for ( let i = 0; i < array.length; ++i) { sum += array[i]; } return sum } arraySum([1, 4, 9, 16, 25]) //=> 55
```

### `technical-atom-c933dfece0b8eb81` code

Citation: (raw/javascriptallonge.pdf p.169-172)

```javascript
const arraySum = (array) => { let done, sum = 0, i = 0; while ((done = i == array.length, !done)) { const value = array[i++]; sum += value; } return sum } arraySum([1, 4, 9, 16, 25]) //=> 55
```

### `technical-atom-16b403e6c3a4e278` code

Citation: (raw/javascriptallonge.pdf p.169-172)

```javascript
const arraySum = (array) => { let iter, sum = 0, index = 0; while ( (eachIteration = { done: index === array.length, value: index < array.length ? array[index] : undefined }, ++index, !eachIteration.done) ) { sum += eachIteration.value; } return sum; } arraySum([1, 4, 9, 16, 25]) //=> 55 With this code, we make a POJO that has done and value keys. All the summing code needs to know is to add eachIteration.value . Now we can extract the ickiness into a separate function: const arrayIterator = (array) => { let i = 0; return () => { const done = i === array.length; return { done, value: done ? undefined : array[i++] } } } const iteratorSum = (iterator) => { let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) {
```

### `technical-atom-5fe8f6d295ad9992` code

Citation: (raw/javascriptallonge.pdf p.169-172)

```javascript
sum += eachIteration.value; } return sum; } iteratorSum(arrayIterator([1, 4, 9, 16, 25])) //=> 55
```

### `technical-atom-5252cb209adbc2eb` code

Citation: (raw/javascriptallonge.pdf p.169-172)

```javascript
const EMPTY = null ; const isEmpty = (node) => node === EMPTY; const pair = (first, rest = EMPTY) => ({first, rest}); const list = (...elements) => { const [first, ...rest] = elements; return elements.length === 0 ? EMPTY : pair(first, list(...rest)) } const print = (aPair) => isEmpty(aPair) ? "" : ` ${ aPair.first } ${ print(aPair.rest) } ` const listIterator = (aPair) => () => { const done = isEmpty(aPair); if (done) { return {done}; } else { const {first, rest} = aPair; aPair = aPair.rest;
```

### `technical-atom-fb1410295f080372` code

Citation: (raw/javascriptallonge.pdf p.169-172)

```javascript
return { done, value: first } } } const iteratorSum = (iterator) => { let eachIteration, sum = 0;; while ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } return sum } const aListIterator = listIterator(list(1, 4, 9, 16, 25)); iteratorSum(aListIterator) //=> 55
```

### `technical-atom-820beff3f61f6705` code

Citation: (raw/javascriptallonge.pdf p.169-172)

```
Now we can extract the ickiness into a separate function: const arrayIterator = (array) => { let i = 0; return () => { const done = i === array.length; return { done, value: done ?
```

### `technical-atom-e082dcf0169ed9ae` code

Citation: (raw/javascriptallonge.pdf p.169-172)

```
The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } .
```
