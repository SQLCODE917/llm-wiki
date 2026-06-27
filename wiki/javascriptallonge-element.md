---
page_id: javascriptallonge-element
page_kind: concept
summary: Element: 22 statement(s) and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-element@f83f042c14aa61997a945af0467342c8
---

# Element

What [[javascriptallonge]] covers about element:

## Statements

_Showing 14 of 22 statements selected for this topic._

- The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. _(javascriptallonge.pdf (source-range-83ecb080-01338))_
- There’s no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-83ecb080-02444))_
- first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. _(javascriptallonge.pdf (source-range-83ecb080-02501))_
- Every subsequent element of the fibonacci sequence is the sum of the previous two elements. _(javascriptallonge.pdf (source-range-83ecb080-02563))_
- We take advantage of the for...of loop in a plain and direct way: For each element e, if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. _(javascriptallonge.pdf (source-range-83ecb080-02694))_
- Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack’s elements, and it only needs to square two of those elements, 29 and 28, to return the answer. _(javascriptallonge.pdf (source-range-83ecb080-02789))_
- Array elements can be extracted using [ and ] as postfix operators. _(javascriptallonge.pdf (source-range-83ecb080-01209))_
- Given an element e and a list list, [e, ...list] is a list. _(javascriptallonge.pdf (source-range-83ecb080-01304))_
- Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions. _(javascriptallonge.pdf (source-range-83ecb080-01351))_
- Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend. _(javascriptallonge.pdf (source-range-83ecb080-01517))_
- Here’s the scheme in JavaScript, using two-element arrays to represent cons cells: _(javascriptallonge.pdf (source-range-83ecb080-01537))_
- In JavaScript, it’s still much, much, much faster to get all the elements except the head from a linked list than from an array. _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We’ll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-83ecb080-01567))_

## Technical atoms

_Showing 6 of 10 technical atoms selected for this topic._

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01209))_

> Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01210))_

> **const** oneTwoThree = ["one", "two", "three"];

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01209))_

> Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01211))_

> oneTwoThree[0] _//=> 'one'_ oneTwoThree[1] _//=> 'two'_ oneTwoThree[2] _//=> 'three'_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01537))_

> Here’s the scheme in JavaScript, using two-element arrays to represent cons cells:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01538))_

> **const** cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01565))_

> Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01566))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements.

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01854))_

> When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01855))_

> The consequence of this is that if you have an array, and you take it’s “rest,” your “child” array is a copy of the elements of the parent array.

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02438))_

> Now is the time to note that we can spread any iterable. So we can spread the elements of an iterable into an array literal:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02439))_

> - ['some squares', ...someSquares] _//=> ["some squares", 1, 4, 9, 16, 25]_


## Source

- [[javascriptallonge]]
