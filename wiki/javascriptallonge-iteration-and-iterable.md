---
page_id: javascriptallonge-iteration-and-iterable
page_kind: concept
summary: Iteration and Iterables: 73 statement(s) and 33 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-iteration-and-iterable@9207ab564fcbd175c15044a267f7c4b7
---

# Iteration and Iterables

What [[javascriptallonge]] covers about iteration and iterables:

## Statements

- And here’s a computation performed using operations on ordered collections: We’ll create an ordered collection of square numbers that end in one and are less than 1,000: _(javascriptallonge.pdf (source-range-83ecb080-02497))_
- first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. _(javascriptallonge.pdf (source-range-83ecb080-02501))_
- But sometimes you want to open it up and do things with its contents. _(javascriptallonge.pdf (source-range-83ecb080-02363))_
- } function, and that’s where this is bound to the value of stack. _(javascriptallonge.pdf (source-range-83ecb080-02376))_
- Iteration for functions and objects has been around for many, many decades. _(javascriptallonge.pdf (source-range-83ecb080-02396))_
- And there’s one more thing: You recall that the spread operator (...) can spread the elements of an array in an array literal or as parameters in a function invocation. _(javascriptallonge.pdf (source-range-83ecb080-02437))_
- And if we have an infinite collection, spreading is going to fail outright as we’re about to see. _(javascriptallonge.pdf (source-range-83ecb080-02445))_
- Attempting to spread an infinite iterable into an array is always going to fail. _(javascriptallonge.pdf (source-range-83ecb080-02455))_
- The iterables we’re discussing represent _ordered collections_ . _(javascriptallonge.pdf (source-range-83ecb080-02457))_
- Iterables needn’t represent ordered collections. _(javascriptallonge.pdf (source-range-83ecb080-02461))_
- Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. _(javascriptallonge.pdf (source-range-83ecb080-02466))_
- And we can assign properties to functions with a . _(javascriptallonge.pdf (source-range-83ecb080-02510))_
- And if we assign a function to a property, we’ve created a method. _(javascriptallonge.pdf (source-range-83ecb080-02510))_
- Acting on the elements of a collection one at a time is called _iterating over the contents_ , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-83ecb080-02365))_

## Technical atoms

> **const** iter = stack.iterator(); iter().value _//=> "you!"_ iter().value _//=> "to"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02373))_

> Context: And here’s a sum function implemented as a fold over a functional iterator:
_(context: javascriptallonge.pdf (source-range-83ecb080-02378))_

> **const** iteratorSum = (iterator) => { **let** eachIteration, sum = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02379))_

> Context: And here’s a sum function implemented as a fold over a functional iterator:
_(context: javascriptallonge.pdf (source-range-83ecb080-02378))_

> **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }
_(source: javascriptallonge.pdf (source-range-83ecb080-02380))_

> Context: We can use it with our stack:
_(context: javascriptallonge.pdf (source-range-83ecb080-02381))_

> **const** stack = Stack1();
_(source: javascriptallonge.pdf (source-range-83ecb080-02384))_

> Context: We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:
_(context: javascriptallonge.pdf (source-range-83ecb080-02388))_

> **const** collectionSum = (collection) => { **const** iterator = collection.iterator();
_(source: javascriptallonge.pdf (source-range-83ecb080-02389))_

> Context: We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:
_(context: javascriptallonge.pdf (source-range-83ecb080-02388))_

> **let** eachIteration, sum = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02390))_


## Source

- [[javascriptallonge]]
