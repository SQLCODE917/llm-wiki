---
page_id: javascriptallonge-like-this
page_kind: source
summary: Like this: from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.210-211
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This section demonstrates how to create a stack object with an iterator method that returns an iterator object, showing how to use the iterator to traverse the stack's elements.

## Key supported claims

- Now our .iterator() method is returning an iterator object. (raw/javascriptallonge.pdf p.210-211)
- When working with objects, we do things the object way. (raw/javascriptallonge.pdf p.210-211)
- Having started by building functional iterators, we understand what is happening underneath the object's scaffolding. (raw/javascriptallonge.pdf p.210-211)

## Technical details

### `technical-atom-c4518a45f6d0ca3a` code

Citation: (raw/javascriptallonge.pdf p.210-211)

```javascript
const Stack2 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this .array[ this .index] = undefined ; if ( this .index >= 0) { this .index -= 1 } return value }, isEmpty () { return this .index < 0 }, iterator () { let iterationIndex = this .index; return { next () { if (iterationIndex > this .index) { iterationIndex = this .index; } if (iterationIndex < 0) { return {done: true }; } else { return {done: false , value: this .array[iterationIndex--]} } } } } });
```

### `technical-atom-6a2bb4b3b3abb688` code

Citation: (raw/javascriptallonge.pdf p.210-211)

```javascript
const stack = Stack2(); stack.push(2000); stack.push(10); stack.push(5) const collectionSum = (collection) => { const iterator = collection.iterator(); let eachIteration, sum = 0; while ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } return sum } collectionSum(stack) //=> 2015
```

## Related technical details

### From [[javascriptallonge-basic-operations-on-iterables]]: `technical-atom-f9a05369dedddd46` requirement

Relation: nearby source page; matched terms `iterator`, `method`, `object`, `objects`, `use`

Citation: (raw/javascriptallonge.pdf p.211-215)

The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.

### From [[javascriptallonge-basic-operations-on-iterables]]: `technical-atom-3f7ceba972853444` code

Relation: nearby source page; matched terms `iterator`, `like`, `stack`

Citation: (raw/javascriptallonge.pdf p.284)

```javascript
stack.push(2000); stack.push(10); stack.push(5) const collectionSum = (collection) => { const iterator = collection[Symbol.iterator](); let eachIteration, sum = 0; while ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } return sum } collectionSum(stack) //=> 2015 Using [Symbol.iterator] instead of .iterator seems like adding an extra moving part for nothing. Do we get anything in return? Indeed we do. Behold the for...of loop: const iterableSum = (iterable) => { let sum = 0; for ( const num of iterable) { sum += num; } return sum } iterableSum(stack) //=> 2015
```

### From [[javascriptallonge-why]]: `technical-atom-74e1dd29d52c577b` code

Relation: nearby source page; matched terms `function`, `like`, `use`

Citation: (raw/javascriptallonge.pdf p.201)

```javascript
This is the canonical Y Combinator 86 : const Y = (f) => ( x => f(v => x(x)(v)) )( x => f(v => x(x)(v)) ); You use it like this: const factorial = Y( function (fac) { (n == 0 ? 1 : n * fac(n - 1));
```
