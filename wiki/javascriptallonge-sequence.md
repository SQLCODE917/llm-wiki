---
page_id: javascriptallonge-sequence
page_kind: concept
summary: Sequence: 4 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-sequence@d5bd617f5439bdf9237a89d5f2f7b9d7
---

# Sequence

What [[javascriptallonge]] covers about sequence:

## Statements

### Garbage, Garbage Everywhere

- Composing and Decomposing Data

108

## **so why arrays**

If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list?

Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements. If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list.

Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We’ll see this explained later in Mutation).

For these and other reasons, almost all languages today make it possible to use a fast array or vector type that is optimized for iteration, and even Lisp now has a variety of data structures that are optimized for specific use cases.

## **summary**

Although we showed how to use tail calls to map and fold over arrays with [first, ...rest], in reality this is not how it ought to be done. But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-83ecb080-00157))_

### Generating Iterables

- Served by the Pot: Collections

205

A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We’re reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out.

## **state machines**

Some iterables can be modelled as state machines. Let’s revisit the Fibonacci sequence. Again. One way to define it is:

- The first element of the fibonacci sequence is zero.

- The second element of the fibonacci sequence is one.

- Every subsequent element of the fibonacci sequence is the sum of the previous two elements.

Let’s write a generator:

_// Generation_ **const** fibonacci = () => { **let** a, b; console.log(a = 0); console.log(b = 1); **while** ( **true** ) { [a, b] = [b, a + b]; console.log(b); } } fibonacci() _//=>_

0 1 1 2

3 5 8 13

21

34 _(javascriptallonge.pdf (source-range-83ecb080-00270))_


## Related pages

- [[javascriptallonge-element]] - shared statements: Element shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  108  ## **so why arrays**  If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? ... [truncated] (4 shared statement(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  108  ## **so why arrays**  If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? ... [truncated] (1 shared statement(s))
- [[javascriptallonge-problem]] - shared statements: Problem shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  108  ## **so why arrays**  If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? ... [truncated] (1 shared statement(s))
- [[javascriptallonge-reference]] - shared statements: Reference shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  108  ## **so why arrays**  If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? ... [truncated] (1 shared statement(s))
- [[javascriptallonge-second]] - shared statements: Second shares source evidence from Generating Iterables: Served by the Pot: Collections  205  A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We’re re ... [truncated] (1 shared statement(s))
- [[javascriptallonge-whenever]] - shared statements: Whenever shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  108  ## **so why arrays**  If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
