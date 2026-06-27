---
page_id: javascriptallonge-section-recursive-iterators-71141b0b
page_kind: source
summary: **recursive iterators**: 11 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recursive-iterators-71141b0b@31bce50e49ecb4d652db8a08aa4a7c06
---

# **recursive iterators**

From [[javascriptallonge]].

## Statements

- Iterators maintain state, that’s what they do. _(javascriptallonge.pdf (source-range-83ecb080-02547))_
- Generators have to manage the exact same amount of state, but sometimes, it’s much easier to manage that state in a generator. _(javascriptallonge.pdf (source-range-83ecb080-02547))_
- Given an array that might contain arrays, let’s say we want to generate all the “leaf” elements, i.e. _(javascriptallonge.pdf (source-range-83ecb080-02548))_
- elements that are not, themselves, iterable. _(javascriptallonge.pdf (source-range-83ecb080-02548))_
- For example, iterating over a tree. _(javascriptallonge.pdf (source-range-83ecb080-02548))_
- If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next, we’re left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. _(javascriptallonge.pdf (source-range-83ecb080-02555))_
- In essence, both the generation and iteration implementations have stacks, but the generation version’s stack is _implicit_ , while the iteration version’s stack is _explicit_ . _(javascriptallonge.pdf (source-range-83ecb080-02555))_
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We’re reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. _(javascriptallonge.pdf (source-range-83ecb080-02558))_
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We’re reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. _(javascriptallonge.pdf (source-range-83ecb080-02558))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02545))_

> They’re of approximately equal complexity. So why bring up generation? Well, there are some collections that are much easier to generate than to iterate over. Let’s look at one:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02547))_

> One of those cases is when we have to recursively enumerate something.

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02548))_

> For example, iterating over a tree. Given an array that might contain arrays, let’s say we want to generate all the “leaf” elements, i.e. elements that are not, themselves, iterable.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02549))_

> _// Generation_ **const** isIterable = (something) => !!something[Symbol.iterator];
