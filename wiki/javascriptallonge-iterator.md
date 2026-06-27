---
page_id: javascriptallonge-iterator
page_kind: concept
summary: Iterator: 27 statement(s) and 19 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-iterator@acae4e99b1b2a10afb60c517e6443be8
---

# Iterator

What [[javascriptallonge]] covers about iterator:

## Statements

- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer “own” that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-83ecb080-02025))_
- Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter(). _(javascriptallonge.pdf (source-range-83ecb080-02377))_
- Fortunately, an iterator object is almost as simple as an iterator function. _(javascriptallonge.pdf (source-range-83ecb080-02400))_
- Now our .iterator() method is returning an iterator object. _(javascriptallonge.pdf (source-range-83ecb080-02410))_
- So, when a standard way to write iterators was added to the JavaScript language, it didn’t make sense to use a method like .iterator() for it: That would conflict with existing code. _(javascriptallonge.pdf (source-range-83ecb080-02413))_
- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-83ecb080-02415))_
- Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. _(javascriptallonge.pdf (source-range-83ecb080-02013))_
- Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. _(javascriptallonge.pdf (source-range-83ecb080-02466))_
- Every time we get an iterator from an ordered collection, we start iterating from the beginning. _(javascriptallonge.pdf (source-range-83ecb080-02467))_
- An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order. _(javascriptallonge.pdf (source-range-83ecb080-02474))_
- Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection from what we want to do with the elements of a collection. _(javascriptallonge.pdf (source-range-83ecb080-02522))_
- Separating concerns with iterators speaks to JavaScript’s fundamental nature: It’s a language that _wants_ to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-83ecb080-02523))_
- Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done. _(javascriptallonge.pdf (source-range-83ecb080-02531))_
- Iterators maintain state, that’s what they do. _(javascriptallonge.pdf (source-range-83ecb080-02547))_

## Technical atoms

> Context: Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let’s consider the simplest example:
_(context: javascriptallonge.pdf (source-range-83ecb080-01987))_

> **const** NumberIterator = (number = 0) => () => ({ done: **false** , value: number++ })
_(source: javascriptallonge.pdf (source-range-83ecb080-01988))_

> Context: Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let’s consider the simplest example:
_(context: javascriptallonge.pdf (source-range-83ecb080-01987))_

> fromOne = NumberIterator(1);
_(source: javascriptallonge.pdf (source-range-83ecb080-01989))_

> Context: Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let’s consider the simplest example:
_(context: javascriptallonge.pdf (source-range-83ecb080-01987))_

> fromOne().value; _//=> 1_ fromOne().value; _//=> 2_ fromOne().value; _//=> 3_ fromOne().value; _//=> 4_ fromOne().value; _//=> 5_
_(source: javascriptallonge.pdf (source-range-83ecb080-01990))_

> Context: We could also write a filter for iterators to accompany our mapping function:
_(context: javascriptallonge.pdf (source-range-83ecb080-02009))_

> **const** oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1);
_(source: javascriptallonge.pdf (source-range-83ecb080-02011))_

> Context: We could also write a filter for iterators to accompany our mapping function:
_(context: javascriptallonge.pdf (source-range-83ecb080-02009))_

> toArray(take(squareOf(oddsOf(NumberIterator(1))), 5)) _//=> [1, 9, 25, 49, 81]_
_(source: javascriptallonge.pdf (source-range-83ecb080-02012))_

> Context: And here’s a sum function implemented as a fold over a functional iterator:
_(context: javascriptallonge.pdf (source-range-83ecb080-02378))_

> **const** iteratorSum = (iterator) => { **let** eachIteration, sum = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02379))_


## Source

- [[javascriptallonge]]
