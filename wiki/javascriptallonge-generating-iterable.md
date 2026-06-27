---
page_id: javascriptallonge-generating-iterable
page_kind: concept
summary: Generating Iterables: 76 statement(s) and 22 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-generating-iterable@3b2e2d28049461997016231504eebedb
---

# Generating Iterables

What [[javascriptallonge]] covers about generating iterables:

## Statements

- It works, but as we’ve just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object:[93] _(javascriptallonge.pdf (source-range-83ecb080-02689))_
- Now that we know about iterables, we can rewrite our iterable operations as generators. _(javascriptallonge.pdf (source-range-83ecb080-02713))_
- Iterables look cool, but then again, everything looks amazing when you’re given cherry-picked examples. _(javascriptallonge.pdf (source-range-83ecb080-02530))_
- Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done. _(javascriptallonge.pdf (source-range-83ecb080-02531))_
- Some iterables can be modelled as state machines. _(javascriptallonge.pdf (source-range-83ecb080-02560))_
- elements that are not, themselves, iterable. _(javascriptallonge.pdf (source-range-83ecb080-02548))_
- If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next, we’re left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. _(javascriptallonge.pdf (source-range-83ecb080-02555))_
- The thing to note here is that our fibonacci generator has three states: generating 0, generating 1, and generating everything after that. _(javascriptallonge.pdf (source-range-83ecb080-02579))_
- This object declares a [Symbol.iterator] function that makes it iterable. _(javascriptallonge.pdf (source-range-83ecb080-02664))_
- So to summarize, ThreeNumbers is an object that we’ve made iterable, by way of writing a _generator_ method for [Symbol.iterator]. _(javascriptallonge.pdf (source-range-83ecb080-02665))_
- > 93There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-83ecb080-02690))_
- If e is not an iterable, yield e. _(javascriptallonge.pdf (source-range-83ecb080-02694))_
- We take advantage of the for...of loop in a plain and direct way: For each element e, if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. _(javascriptallonge.pdf (source-range-83ecb080-02694))_
- yield* is handy when writing generator functions that operate on or create iterables. _(javascriptallonge.pdf (source-range-83ecb080-02711))_

## Technical atoms

> Context: Let’s consider how they work. Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done.
_(context: javascriptallonge.pdf (source-range-83ecb080-02531))_

> Iterators have to arrange its own state such that when you call them, they compute and return the next item.
_(source: javascriptallonge.pdf (source-range-83ecb080-02532))_

> Context: Of course, when we have some code that makes a bunch of something, we don’t usually write it like that. We usually just write something like:
_(context: javascriptallonge.pdf (source-range-83ecb080-02538))_

> **let** n = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02539))_

> Context: They’re of approximately equal complexity. So why bring up generation? Well, there are some collections that are much easier to generate than to iterate over. Let’s look at one:
_(context: javascriptallonge.pdf (source-range-83ecb080-02545))_

> One of those cases is when we have to recursively enumerate something.
_(source: javascriptallonge.pdf (source-range-83ecb080-02547))_

> Context: For example, iterating over a tree. Given an array that might contain arrays, let’s say we want to generate all the “leaf” elements, i.e. elements that are not, themselves, iterable.
_(context: javascriptallonge.pdf (source-range-83ecb080-02548))_

> _// Generation_ **const** isIterable = (something) => !!something[Symbol.iterator];
_(source: javascriptallonge.pdf (source-range-83ecb080-02549))_

> Context: Let’s write a generator:
_(context: javascriptallonge.pdf (source-range-83ecb080-02564))_

> **const** fibonacci = () => { **let** a, b;
_(source: javascriptallonge.pdf (source-range-83ecb080-02566))_

> Context: Let’s write a generator:
_(context: javascriptallonge.pdf (source-range-83ecb080-02564))_

> console.log(a = 0);
_(source: javascriptallonge.pdf (source-range-83ecb080-02567))_


## Source

- [[javascriptallonge]]
