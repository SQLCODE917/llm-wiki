---
page_id: javascriptallonge-section-iterator-objects-f38e13cb
page_kind: source
summary: **iterator objects**: 14 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-iterator-objects-f38e13cb@fdebeb57c98e25eadad0f5bb6580ec23
---

# **iterator objects**

From [[javascriptallonge]].

## Statements

- Iteration for functions and objects has been around for many, many decades. _(javascriptallonge.pdf (source-range-83ecb080-02396))_
- In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. _(javascriptallonge.pdf (source-range-83ecb080-02397))_
- The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-83ecb080-02397))_
- The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-83ecb080-02397))_
- Fortunately, an iterator object is almost as simple as an iterator function. _(javascriptallonge.pdf (source-range-83ecb080-02400))_
- Instead of having a function that you call to get the next element, you have an object with a .next() method. _(javascriptallonge.pdf (source-range-83ecb080-02400))_
- When working with objects, we do things the object way. _(javascriptallonge.pdf (source-range-83ecb080-02410))_
- But having started by building functional iterators, we understand what is happening underneath the object’s scaffolding. _(javascriptallonge.pdf (source-range-83ecb080-02410))_
- Now our .iterator() method is returning an iterator object. _(javascriptallonge.pdf (source-range-83ecb080-02410))_

## Technical atoms

> **const** stack = Stack2();
_(source: javascriptallonge.pdf (source-range-83ecb080-02404))_

> **const** collectionSum = (collection) => { **const** iterator = collection.iterator();
_(source: javascriptallonge.pdf (source-range-83ecb080-02406))_

> **let** eachIteration, sum = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02407))_

> **while** ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }
_(source: javascriptallonge.pdf (source-range-83ecb080-02408))_

> collectionSum(stack) _//=> 2015_
_(source: javascriptallonge.pdf (source-range-83ecb080-02409))_
