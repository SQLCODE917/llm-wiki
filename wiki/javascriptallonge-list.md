---
page_id: javascriptallonge-list
page_kind: concept
summary: List: 21 statement(s) and 26 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-list@0487c94dea412f56c87a40fbe83a2c2b
---

# List

What [[javascriptallonge]] covers about list:

## Statements

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
- But when we’re in the midst of creating a brand new list, we aren’t sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time. _(javascriptallonge.pdf (source-range-83ecb080-01747))_
- Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. _(javascriptallonge.pdf (source-range-83ecb080-01747))_
- If we _know_ that a list doesn’t share any elements with another list, we can safely modify it. _(javascriptallonge.pdf (source-range-83ecb080-01863))_
- before we go any further, let’s write a few naïve list utilities so that we can work at a slightly higher level of abstraction: _(javascriptallonge.pdf (source-range-83ecb080-01865))_
- Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-83ecb080-01875))_
- But our new parent and child lists are copies that contain the desired modifications, without interfering with each other: _(javascriptallonge.pdf (source-range-83ecb080-01891))_
- We’re passing list what we want done with an empty list, and what we want done with a list that has at least one element. _(javascriptallonge.pdf (source-range-83ecb080-02187))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01323, source-range-83ecb080-01325))_

> Let’s try it! Our length function is _recursive_ , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01324))_

> length([]) _//=> 0_ length(["foo"]) _//=> 1_ length(["foo", "bar", "baz"]) _//=> 3_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01354))_

> If we want to square each number in a list, we could write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01355))_

> **const** squareAll = ([first, ...rest]) => first === **undefined** ? [] : [first * first, ...squareAll(rest)\ ]; squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01356))_

> And if we wanted to “truthify” each element in a list, we could write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01359))_

> **const** truthyAll = ([first, ...rest]) => first === **undefined**

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01369))_

> With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn’t. A function to compute the sum of the squares of a list of numbers might look like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01372))_

> **const** sumSquares = ([first, ...rest]) => first === **undefined**

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01539))_

> We can make a list by calling cons repeatedly, and terminating it with null:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01540))_

> **const** oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, **null** )))));

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01543))_

> Notice that though JavaScript displays our list as if it is composed of arrays nested within each other like Russian Dolls, in reality the arrays refer to each other with references, so [1,[2,[3,[4,[5,null]]]]] is actually more like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01546))_

> **const** node5 = [5, **null** ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2];

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01564))_

> If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01565))_

> And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01565))_

> Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01566))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements.

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01575))_

> Lists are not the only way to represent collections of things, but they are the “oldest” data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. Lists are obviously very handy for homogeneous collections of things, like a shopping list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01576))_

> **const** remember = ["the milk", "the coffee beans", "the biscotti"];

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01579))_

> Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01580))_

> **const** NAME = 0, FIRST = 0, LAST = 1, OCCUPATION = 1, TITLE = 0, RESPONSIBILITIES = 1;

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01579))_

> Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01581))_

> **const** user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\ vaScript Spessore", "CoffeeScript Ristretto"]]];

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01644))_

> Earlier, we used two-element arrays as nodes in a linked list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01645))_

> **const** cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01654, source-range-83ecb080-01657))_

> Taking the length of a linked list is easy: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01655))_

> **const** length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1);

### Technical atom 14

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01654, source-range-83ecb080-01657))_

> Taking the length of a linked list is easy: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01656))_

> length(OneTwoThree) _//=> 3_

### Technical atom 15

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01657))_

> What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01658))_

> **const** slowcopy = (node) => node === EMPTY ? EMPTY : { first: node.first, rest: slowcopy(node.rest)};

### Technical atom 16

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01669))_

> Well, well, well. We have unwittingly _reversed_ the list. This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we’re going to get a backwards copy of the list. This isn’t a bad thing by any stretch of the imagination. Let’s call it what it is:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01670))_

> **const** reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed });

### Technical atom 17

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01740))_

> As noted, one pattern is to be more liberal about mutation when building a data structure. Consider our copy algorithm. Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01741))_

> **const** reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed });

### Technical atom 18

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01740))_

> As noted, one pattern is to be more liberal about mutation when building a data structure. Consider our copy algorithm. Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01742))_

> **const** copy = (node) => reverse(reverse(node));

### Technical atom 19

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01854))_

> When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01855))_

> The consequence of this is that if you have an array, and you take it’s “rest,” your “child” array is a copy of the elements of the parent array.

### Technical atom 20

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01868))_

> **const** copy = (node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail === **null** ) { **const** { first, rest } = node; **const** newNode = { first, rest }; **return** copy(rest, newNode, newNode); } **else** { **const** { first, rest } = node; **const** newNode = { first, rest }; tail.rest = newNode; **return** copy(node.rest, head, newNode); } } **const** first = ({first, rest}) => first; **const** rest = ({first, rest}) => rest; **con

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01871))_

> **const** childList = rest(parentList);

### Technical atom 21

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01875))_

> So back to the problem of structure sharing. One strategy for avoiding problems is to be _pessimistic_ . Whenever we take the rest of a list, make a copy.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01876))_

> **const** rest = ({first, rest}) => copy(rest);

### Technical atom 22

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01875, source-range-83ecb080-01879))_

> So back to the problem of structure sharing. One strategy for avoiding problems is to be _pessimistic_ . Whenever we take the rest of a list, make a copy. This strategy is called “copy-on-read”, because when we attempt the parent to “read” the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01878))_

> parentList _//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\_ rest":{}}}}} childList //=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}

### Technical atom 23

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01885))_

> Why are we copying? In case we modify a child list. Ok, what if we do this: Make the copy when we know we are modifying the list. When do we know that? When we call set. We’ll restore our original definition for rest, but change set:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01886))_

> **const** rest = ({first, rest}) => rest;

### Technical atom 24

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02185))_

> This is a little gratuitous, but it makes the point: The code that uses the data doesn’t reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. The same thing happens with our lists. Here’s length for lists:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02186))_

> **const** length = (list) => list( () => 0, (aPair) => 1 + length(aPair(pairRest))) );

### Technical atom 25

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02190))_

> We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally _not_ the same thing as this code for the length of a linked list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02191))_

> **const** length = (node, delayed = 0) =>

### Technical atom 26

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02190))_

> We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally _not_ the same thing as this code for the length of a linked list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02192))_

> node === EMPTY


## Related pages

- [[javascriptallonge-length]] - shared statements and technical atoms (1 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-copy]] - shared statements and technical atoms (1 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-rest]] - shared statements and technical atoms (1 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms (3 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-code]] - shared technical atoms (3 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-write]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
