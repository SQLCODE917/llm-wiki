---
page_id: javascriptallonge-section-like-this-f28684b0
page_kind: source
summary: Like this:: 5 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-like-this-f28684b0@fcc2c68ccabf994e39f91576f6723aca
---

# Like this:

From [[javascriptallonge]].

## Statements

- Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object's scaffolding. _(javascriptallonge.pdf (source-range-8eb13d6b-01551))_

## Technical atoms

### Technical frame 1: Like this:

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01551))_

> Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object's scaffolding.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01549))_

```
const Stack2 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this .array[ this .index] = undefined ; if ( this .index >= 0) { this .index -= 1 } return value }, isEmpty () { return this .index < 0 }, iterator () { let iterationIndex = this .index; return { next () { if (iterationIndex > this .index) { iterationIndex = this .index; } if (iterationIndex < 0) { return {done: true }; } else { return {done: false , value: this .array[iterationIndex--]} } } } } });
```

### Technical frame 2: Like this:

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01551))_

> Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object's scaffolding.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01550))_

```
const stack = Stack2(); stack.push(2000); stack.push(10); stack.push(5) const collectionSum = (collection) => { const iterator = collection.iterator(); let eachIteration, sum = 0; while ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } return sum } collectionSum(stack) //=> 2015
```
