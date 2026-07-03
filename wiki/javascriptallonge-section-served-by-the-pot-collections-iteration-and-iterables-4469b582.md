---
page_id: javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-4469b582
page_kind: source
page_family: section-reference
summary: Served by the Pot: Collections / Iteration and Iterables: 21 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-4469b582@36eccab17fa283f9ad54af9a08b5b183
---

# Served by the Pot: Collections / Iteration and Iterables

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-served-by-the-pot-collections-bdfa40aa]] - broader source section: Served by the Pot: Collections
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-a-look-back-at-functional-iterators-4c177971]] - narrower source section: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterator-objects-00211d43]] - narrower source section: Served by the Pot: Collections / Iteration and Iterables / iterator objects

## Statements

- Many objects in JavaScript can model collections of things. A collection is like a box containing stuff. Sometimes you just want to move the box around. But sometimes you want to open it up and do things with its contents. _(javascriptallonge.pdf (source-range-7239e085-01528))_
- All of these actions involve going through the contents one by one. Acting on the elements of a collection one at a time is called iterating over the contents , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-7239e085-01530))_
- Acting on the elements of a collection one at a time is called iterating over the contents , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-7239e085-01530))_

## Statements by subsection

### Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

- When discussing functions, we looked at the benefits of writing Functional Iterators. We can do the same thing for objects. Here's a stack that has its own functional iterator method: _(javascriptallonge.pdf (source-range-7239e085-01532))_
- We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method: _(javascriptallonge.pdf (source-range-7239e085-01541))_
- If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-7239e085-01543))_

### Served by the Pot: Collections / Iteration and Iterables / iterator objects

- Iteration for functions and objects has been around for many, many decades. For simple linear collections like arrays, linked lists, stacks, and queues, functional iterators are the simplest and easiest way to implement iterators. _(javascriptallonge.pdf (source-range-7239e085-01546))_
- In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-7239e085-01547))_
- Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object with a .next() method. _(javascriptallonge.pdf (source-range-7239e085-01548))_
- The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-7239e085-01547))_
