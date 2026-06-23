---
page_id: javascriptallonge-basic-operations-on-iterables
page_kind: source
summary: Basic Operations on Iterables from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.284-284
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Summary of the 'Basic Operations on Iterables' section from JavaScript Allongé, covering the for...of loop, Symbol.iterator, and spreading iterables.

## Key supported claims

- The for...of loop works with any iterable object (raw/javascriptallonge.pdf p.284-284).

## Technical details

### `technical-atom-5dadf5a885619337` code

Citation: (raw/javascriptallonge.pdf p.284)

```javascript
const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this .array[ this .index] = undefined ; if ( this .index >= 0) { this .index -= 1 } return value }, isEmpty () { return this .index < 0 }, [Symbol.iterator] () { let iterationIndex = this .index; return { next () { if (iterationIndex > this .index) { iterationIndex = this .index; } if (iterationIndex < 0) { return {done: true }; } else { return {done: false , value: this .array[iterationIndex--]} } } } } }); const stack = Stack3();
```

### `technical-atom-3f7ceba972853444` code

Citation: (raw/javascriptallonge.pdf p.284)

```javascript
stack.push(2000); stack.push(10); stack.push(5) const collectionSum = (collection) => { const iterator = collection[Symbol.iterator](); let eachIteration, sum = 0; while ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } return sum } collectionSum(stack) //=> 2015 Using [Symbol.iterator] instead of .iterator seems like adding an extra moving part for nothing. Do we get anything in return? Indeed we do. Behold the for...of loop: const iterableSum = (iterable) => { let sum = 0; for ( const num of iterable) { sum += num; } return sum } iterableSum(stack) //=> 2015
```

### `technical-atom-5cf6a17f64b5d326` code

Citation: (raw/javascriptallonge.pdf p.284)

```javascript
const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { return false }, [Symbol.iterator] () { let currentPair = this ; return { next () { if (currentPair.isEmpty()) { return {done: true } } else { const value = currentPair.first; currentPair = currentPair.rest; return {done: false , value} } } } } }); const list = (...elements) => { const [first, ...rest] = elements; return elements.length === 0 ? EMPTY : Pair1(first, list(...rest)) } const someSquares = list(1, 4, 9, 16, 25); iterableSum(someSquares) //=> 55
```

### `technical-atom-91876acdf654e0cd` code

Citation: (raw/javascriptallonge.pdf p.284)

```javascript
['some squares', ...someSquares] //=> ["some squares", 1, 4, 9, 16, 25]
```

### `technical-atom-6eadb95cbdf43456` code

Citation: (raw/javascriptallonge.pdf p.284)

```javascript
const firstAndSecondElement = (first, second) => ({first, second}) firstAndSecondElement(...stack) //=> {"first":5,"second":10}
```

### `technical-atom-f9a05369dedddd46` requirement

Citation: (raw/javascriptallonge.pdf p.211-215)

The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.

### `technical-atom-13e57f96247ba73c` worked-example

Citation: (raw/javascriptallonge.pdf p.211-215)

For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.
