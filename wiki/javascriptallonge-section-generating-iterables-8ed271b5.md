---
page_id: javascriptallonge-section-generating-iterables-8ed271b5
page_kind: source
summary: Generating Iterables: 14 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-generating-iterables-8ed271b5@9e4687b675a0f7789ea22e19e88685bc
---

# Generating Iterables

From [[javascriptallonge]].

## Statements

- Iterables look cool, but then again, everything looks amazing when you're given cherry-picked examples. What is there they don't do well? _(javascriptallonge.pdf (source-range-8eb13d6b-01624))_
- Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done. _(javascriptallonge.pdf (source-range-8eb13d6b-01625))_
- Iterators have to arrange its own state such that when you call them, they compute and return the next item. This seems blindingly obvious and simple. If, for example, you want numbers, you write: _(javascriptallonge.pdf (source-range-8eb13d6b-01626))_
- Well, we've written our iterator as a server . It waits until given a request, and then it returns exactly one item. Then it waits for the next request. There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers. _(javascriptallonge.pdf (source-range-8eb13d6b-01629))_
- Of course, when we have some code that makes a bunch of something, we don't usually write it like that. We usually just write something like: _(javascriptallonge.pdf (source-range-8eb13d6b-01630))_
- And magically, the numbers would pour forth. We would generate numbers. Let's put that beside the code for the iterator, minus the iterable scaffolding: _(javascriptallonge.pdf (source-range-8eb13d6b-01632))_
- They're of approximately equal complexity. So why bring up generation? Well, there are some collections that are much easier to generate than to iterate over. Let's look at one: _(javascriptallonge.pdf (source-range-8eb13d6b-01634))_
- Iterables look cool, but then again, everything looks amazing when you're given cherry-picked examples. _(javascriptallonge.pdf (source-range-8eb13d6b-01624))_

## Technical atoms

### Technical frame 1: Generating Iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01624))_

> Iterables look cool, but then again, everything looks amazing when you're given cherry-picked examples. What is there they don't do well?

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01622))_

> [Figure] (p.224)

### Technical frame 2: Generating Iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01629))_

> Well, we've written our iterator as a server . It waits until given a request, and then it returns exactly one item. Then it waits for the next request. There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01626))_

> Iterators have to arrange its own state such that when you call them, they compute and return the next item.

### Technical frame 3: Generating Iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01629))_

> Well, we've written our iterator as a server . It waits until given a request, and then it returns exactly one item. Then it waits for the next request. There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01627))_

```
const Numbers = { [Symbol.iterator]: () => { let n = 0; return { next: () => ({done: false , value: n++}) } } };
```

### Technical frame 4: Generating Iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01632))_

> And magically, the numbers would pour forth. We would generate numbers. Let's put that beside the code for the iterator, minus the iterable scaffolding:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01631))_

```
let n = 0; while ( true ) { console.log(n++) }
```

### Technical frame 5: Generating Iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01634))_

> They're of approximately equal complexity. So why bring up generation? Well, there are some collections that are much easier to generate than to iterate over. Let's look at one:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01633))_

```
// Iteration let n = 0; () => ({done: false , value: n++}) // Generation let n = 0; while ( true ) { console.log(n++) }
```
