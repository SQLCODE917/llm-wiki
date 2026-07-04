---
page_id: javascriptallonge-section-generating-iterables-a786d150
page_kind: source
page_family: section-reference
summary: Generating Iterables: 23 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-03
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-generating-iterables-a786d150@8e47a0c13c3df676b566c0ae0765bd8b
---

# Generating Iterables

From [[javascriptallonge]].

## Statements

- Served by the Pot: Collections 

201 

## **Generating Iterables** 

**==> picture [469 x 314] intentionally omitted <==**

**Banco do Café** 

Iterables look cool, but then again, everything looks amazing when you’re given cherry-picked examples. What is there they don’t do well? 

Let’s consider how they work. Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done. 

Iterators have to arrange its own state such that when you call them, they compute and return the next item. This seems blindingly obvious and simple. If, for example, you want numbers, you write: _(javascriptallonge.pdf (source-range-af806fb1-00257))_
- 202 

Served by the Pot: Collections 

**const** Numbers = { [Symbol.iterator]: () => { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } }; 

The Numbers iterable returns an object that updates a mutable variable, n, to deliver number after number. How hard can this be? 

Well, we’ve written our iterator as a _server_ . It waits until given a request, and then it returns exactly one item. Then it waits for the next request. There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers. 

Of course, when we have some code that makes a bunch of something, we don’t usually write it like that. We usually just write something like: 

**let** n = 0; 

**while** ( **true** ) { console.log(n++) } 

And magically, the numbers would pour forth. We would _generate_ numbers. Let’s put that beside the code for the iterator, minus the iterable scaffolding: 

_// Iteration_ **let** n = 0; () => ({done: **false** , value: n++}) _// Generation_ **let** n = 0; **while** ( **true** ) { console.log(n++) } _(javascriptallonge.pdf (source-range-af806fb1-00258))_
- 203 

Served by the Pot: Collections 

They’re of approximately equal complexity. So why bring up generation? Well, there are some collections that are much easier to generate than to iterate over. Let’s look at one: 

## **recursive iterators** 

Iterators maintain state, that’s what they do. Generators have to manage the exact same amount of state, but sometimes, it’s much easier to manage that state in a generator. One of those cases is when we have to recursively enumerate something. 

For example, iterating over a tree. Given an array that might contain arrays, let’s say we want to generate all the “leaf” elements, i.e. elements that are not, themselves, iterable. 

_// Generation_ **const** isIterable = (something) => !!something[Symbol.iterator]; 

**const** generate = (iterable) => { **for** ( **let** element **of** iterable) { **if** (isIterable(element)) { generate(element) } **else** { console.log(element) } } } generate([1, [2, [3, 4], 5]]) _//=>_ 1 2 3 4 5 

Very simple. Now for the iteration version. We’ll write a functional iterator to keep things simple, but it’s easy to see the shape of the basic problem: _(javascriptallonge.pdf (source-range-af806fb1-00259))_
- 204 

Served by the Pot: Collections 

_// Iteration_ **const** isIterable = (something) => !!something[Symbol.iterator]; **const** treeIterator = (iterable) => { **const** iterators = [ iterable[Symbol.iterator]() ]; **return** () => { **while** (!!iterators[0]) { **const** iterationResult = iterators[0].next(); **if** (iterationResult.done) { iterators.shift(); } **else if** (isIterable(iterationResult.value)) { iterators.unshift(iterationResult.value[Symbol.iterator]()); } **else** { **return** iterationResult.value; } } **return** ; } } **const** i = treeIterator([1, [2, [3, 4], 5]]); **let** n; **while** (n = i()) { console.log(n) } _//=>_ 1 2 3 4 5 

If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next, we’re left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. In essence, both the generation and iteration implementations have stacks, but the generation version’s stack is _implicit_ , while the iteration version’s stack is _explicit_ . _(javascriptallonge.pdf (source-range-af806fb1-00260))_
- Served by the Pot: Collections 

205 

A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We’re reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. 

## **state machines** 

Some iterables can be modelled as state machines. Let’s revisit the Fibonacci sequence. Again. One way to define it is: 

- The first element of the fibonacci sequence is zero. 

- The second element of the fibonacci sequence is one. 

- Every subsequent element of the fibonacci sequence is the sum of the previous two elements. 

Let’s write a generator: 

_// Generation_ 

**const** fibonacci = () => { **let** a, b; 

console.log(a = 0); 

console.log(b = 1); 

**while** ( **true** ) { [a, b] = [b, a + b]; console.log(b); } 

} 

fibonacci() _//=>_ 

0 1 1 2 

3 5 8 13 

21 

34 _(javascriptallonge.pdf (source-range-af806fb1-00261))_
- Iterables look cool, but then again, everything looks amazing when you’re given cherry-picked examples. _(javascriptallonge.pdf (source-range-af806fb1-00257))_
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We’re reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. _(javascriptallonge.pdf (source-range-af806fb1-00261))_
