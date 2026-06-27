---
page_id: javascriptallonge-lazy-and-eager-collection
page_kind: concept
summary: Lazy and Eager Collections: 34 statement(s) and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-lazy-and-eager-collection@c221921603dae4ced4c77fbbc0a06578
---

# Lazy and Eager Collections

What [[javascriptallonge]] covers about lazy and eager collections:

## Statements

_Showing 14 of 34 statements selected for this topic._

- This “fat object” style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don’t need for the collection to handle every single detail. _(javascriptallonge.pdf (source-range-83ecb080-02742))_
- We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs: _(javascriptallonge.pdf (source-range-83ecb080-02813))_
- We tell ourselves that, well, a collection ought to know how to map itself. _(javascriptallonge.pdf (source-range-83ecb080-02740))_
- And they should know how to accomplish the desired result, but they should do so by delegating as much of the work as possible to operations like mapWith. _(javascriptallonge.pdf (source-range-83ecb080-02744))_
- And if we want to create convenience methods, we can reuse common pieces. _(javascriptallonge.pdf (source-range-83ecb080-02745))_
- And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. _(javascriptallonge.pdf (source-range-83ecb080-02781))_
- If we mutate a collection after taking an iterable, we might get an unexpected result. _(javascriptallonge.pdf (source-range-83ecb080-02801))_
- The operations on iterables are tremendously valuable, but let’s reiterate why we care: In JavaScript, we build single-responsibility objects, and single-responsibility functions, and we compose these together to build more full-featured objects and algorithms. _(javascriptallonge.pdf (source-range-83ecb080-02737))_
- If we wanted to flatten collections to arrays, we wrote a .toArray method for each type of collection. _(javascriptallonge.pdf (source-range-83ecb080-02739))_
- Some methods are only added to a few collections, some are added to all. _(javascriptallonge.pdf (source-range-83ecb080-02740))_
- That’s a sign that we should work at a higher level of abstraction, and working with iterables is that higher level of abstraction. _(javascriptallonge.pdf (source-range-83ecb080-02741))_
- But we end up recreating the same bits of code in each .map method we create, in each .reduce method we create, in each .filter method we create, and in each .find method. _(javascriptallonge.pdf (source-range-83ecb080-02741))_
- Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. _(javascriptallonge.pdf (source-range-83ecb080-02744))_
- To use LazyCollection, we mix it into an any iterable object. _(javascriptallonge.pdf (source-range-83ecb080-02759))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02761))_

> _// Pair, a/k/a linked lists_

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02762))_

> **const** EMPTY = { isEmpty: () => **true**

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02766))_

> **const** isEmpty = (node) => node === EMPTY;

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02769))_

> _// Stack_ **const** Stack = () => Object.assign({ array: [], index: -1, push: **function** (value) {

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02781))_

> Both expressions evaluate to 220. And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02783))_

> When working with very large collections and many operations, this can be important.

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02781))_

> Both expressions evaluate to 220. And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02784))_

> The effect is even more pronounced when we use methods like first, until, or take:

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02790))_

> We can confirm this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02792))_

> If we write the almost identical thing with an array, we get a different behaviour:


## Source

- [[javascriptallonge]]
