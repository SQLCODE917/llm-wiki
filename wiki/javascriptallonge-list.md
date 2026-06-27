---
page_id: javascriptallonge-list
page_kind: concept
summary: List: 21 statement(s) and 23 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-list@b3412adb1caa2b1f26adf257afb3e53e
---

# List

What [[javascriptallonge]] covers about list:

## Statements

_Showing 14 of 21 statements selected for this topic._

- Given an element e and a list list, [e, ...list] is a list. _(javascriptallonge.pdf (source-range-83ecb080-01304))_
- Lists were represented as linked lists of cons cells, with each cell’s head pointing to an element and the tail pointing to another cons cell. _(javascriptallonge.pdf (source-range-83ecb080-01535))_
- There’s no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-83ecb080-01661))_
- We’ve seen how to build lists with arrays and with linked lists. _(javascriptallonge.pdf (source-range-83ecb080-01852))_
- We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-83ecb080-02187))_
- Having a list know itself whether it is empty hides implementation information from the code that uses lists. _(javascriptallonge.pdf (source-range-83ecb080-02196))_
- Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-83ecb080-01187))_
- Some data structures, like lists, can obviously be seen as a collection of items. _(javascriptallonge.pdf (source-range-83ecb080-01300))_
- A function to compute the sum of the squares of a list of numbers might look like this: _(javascriptallonge.pdf (source-range-83ecb080-01369))_
- But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. _(javascriptallonge.pdf (source-range-83ecb080-01565))_
- Lists are not the only way to represent collections of things, but they are the “oldest” data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. _(javascriptallonge.pdf (source-range-83ecb080-01575))_
- So back when lists were the only things available, programmers would introduce constants to make things easier on themselves: _(javascriptallonge.pdf (source-range-83ecb080-01579))_
- For a list of length _n_ , we created _n_ superfluous nodes and copied _n_ superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-01681))_

## Technical atoms

_Showing 6 of 23 technical atoms selected for this topic._

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01323, source-range-83ecb080-01325))_

> Let’s try it! Our length function is _recursive_ , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01324))_

> length([]) _//=> 0_ length(["foo"]) _//=> 1_ length(["foo", "bar", "baz"]) _//=> 3_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01369))_

> With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn’t. A function to compute the sum of the squares of a list of numbers might look like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01372))_

> **const** sumSquares = ([first, ...rest]) => first === **undefined**

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01539))_

> We can make a list by calling cons repeatedly, and terminating it with null:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01540))_

> **const** oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, **null** )))));

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01543))_

> Notice that though JavaScript displays our list as if it is composed of arrays nested within each other like Russian Dolls, in reality the arrays refer to each other with references, so [1,[2,[3,[4,[5,null]]]]] is actually more like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01546))_

> **const** node5 = [5, **null** ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2];

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01564))_

> If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01565))_

> And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01565))_

> Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01566))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements.


## Source

- [[javascriptallonge]]
