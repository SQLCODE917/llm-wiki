---
page_id: javascriptallonge-from
page_kind: source
summary: from from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.221-222
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This section discusses how to create .from functions to gather iterables into particular collection types, using JavaScript's built-in Array.from and custom implementations for other collections like Stack3 and Pair1.

## Key supported claims

- One useful thing is to write a .from function that gathers an iterable into a particular collection type. (raw/javascriptallonge.pdf p.221-222)
- As you recall, functions are mutable objects. (raw/javascriptallonge.pdf p.221-222)
- No, of course not, we can do anything we like with them. (raw/javascriptallonge.pdf p.221-222)

## Technical details

### `technical-atom-dac42232b1dd6899` code

Citation: (raw/javascriptallonge.pdf p.221-222)

```javascript
Array.from(UpTo1000) //=> [1,81,121,361,441,841,961]
```

### `technical-atom-096e3d7cf4be2948` code

Citation: (raw/javascriptallonge.pdf p.221-222)

```javascript
Stack3.from = function (iterable) { const stack = this (); for ( let element of iterable) { stack.push(element); } return stack; } Pair1.from = (iterable) => ( function iterationToList (iteration) { const {done, value} = iteration.next(); return done ? EMPTY : Pair1(value, iterationToList(iteration)); })(iterable[Symbol.iterator]())
```

### `technical-atom-bb3f798ec6996bf9` code

Citation: (raw/javascriptallonge.pdf p.221-222)

```javascript
const numberList = Pair1.from(untilWith((x) => x > 10, Numbers)); Pair1.from(Squares) //=> {"first":0, "rest":{"first":1, "rest":{"first":4, "rest":{ ...
```

### `technical-atom-dd469f1aaeba06ba` exception

Citation: (raw/javascriptallonge.pdf p.221-222)

Having iterated over a collection, are we limited to for..do and/or gathering the elements in an array literal and/or gathering the elements into the parameters of a function?

## Related technical details

### From [[javascriptallonge-basic-operations-on-iterables]]: `technical-atom-3f7ceba972853444` code

Relation: nearby source page; matched terms `anything`, `collection`, `iterable`, `iterables`, `like`, `using`

Citation: (raw/javascriptallonge.pdf p.284)

```javascript
stack.push(2000); stack.push(10); stack.push(5) const collectionSum = (collection) => { const iterator = collection[Symbol.iterator](); let eachIteration, sum = 0; while ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } return sum } collectionSum(stack) //=> 2015 Using [Symbol.iterator] instead of .iterator seems like adding an extra moving part for nothing. Do we get anything in return? Indeed we do. Behold the for...of loop: const iterableSum = (iterable) => { let sum = 0; for ( const num of iterable) { sum += num; } return sum } iterableSum(stack) //=> 2015
```

### From [[javascriptallonge-generating-iterables]]: `technical-atom-10b9ccb62f560bfc` procedure

Relation: nearby source page; matched terms `iterables`, `them`, `you`

Citation: (raw/javascriptallonge.pdf p.224-226)

Iterators have to arrange its own state such that when you call them, they compute and return the next item.

### From [[javascriptallonge-generating-iterables]]: `technical-atom-e82674fd1d436f3a` worked-example

Relation: nearby source page; matched terms `iterables`, `write`, `you`

Citation: (raw/javascriptallonge.pdf p.224-226)

If, for example, you want numbers, you write:

### From [[javascriptallonge-ordered-collections]]: `technical-atom-ad997c57b78950fc` requirement

Relation: nearby source page; matched terms `collections`, `iterable`, `you`

Citation: (raw/javascriptallonge.pdf p.216-217)

Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers.
