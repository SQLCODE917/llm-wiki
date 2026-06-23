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
