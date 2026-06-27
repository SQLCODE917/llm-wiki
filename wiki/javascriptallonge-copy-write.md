---
page_id: javascriptallonge-copy-write
page_kind: concept
summary: Copy on Write: 22 statement(s) and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-copy-write@29f1d43ee82f36d5405626641433a61f
---

# Copy on Write

What [[javascriptallonge]] covers about copy on write:

## Statements

_Showing 14 of 22 statements selected for this topic._

- This strategy of waiting to copy until you are writing is called copy-on-write, or “COW:” _(javascriptallonge.pdf (source-range-83ecb080-01895))_
- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.— Wikipedia[73] _(javascriptallonge.pdf (source-range-83ecb080-01898))_
- before we go any further, let’s write a few naïve list utilities so that we can work at a slightly higher level of abstraction: _(javascriptallonge.pdf (source-range-83ecb080-01865))_
- Looking at the code again, you see that the copy function doesn’t copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. _(javascriptallonge.pdf (source-range-83ecb080-01900))_
- Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-83ecb080-01875))_
- This strategy is called “copy-on-read”, because when we attempt the parent to “read” the value of a child of the list, we make a copy and read the copy of the child. _(javascriptallonge.pdf (source-range-83ecb080-01879))_
- Thereafter, we can write to the parent or the copy of the child freely. _(javascriptallonge.pdf (source-range-83ecb080-01879))_
- As we expected, making a copy lets us modify the copy without interfering with the original. _(javascriptallonge.pdf (source-range-83ecb080-01880))_
- Our mapWith function would be very expensive if we make a copy every time we call rest(node). _(javascriptallonge.pdf (source-range-83ecb080-01880))_
- Sometimes we don’t need to make a copy because we won’t be modifying the list. _(javascriptallonge.pdf (source-range-83ecb080-01880))_
- But before we fix that, let’s try being lazy about copying. _(javascriptallonge.pdf (source-range-83ecb080-01881))_
- Once we’re done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-83ecb080-01900))_
- We’ve seen how to build lists with arrays and with linked lists. _(javascriptallonge.pdf (source-range-83ecb080-01852))_
- When you take the rest of an array with destructuring ([first, ...rest]), you are given a _copy_ of the elements of the array. _(javascriptallonge.pdf (source-range-83ecb080-01853))_

## Technical atoms

_Showing 6 of 8 technical atoms selected for this topic._

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01854))_

> When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01855))_

> The consequence of this is that if you have an array, and you take it’s “rest,” your “child” array is a copy of the elements of the parent array.

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01858))_

> Whereas if you have a linked list, and you take it’s “rest,” your “child” list shares its nodes with the “parent” list.

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01859))_

> Let’s confirm our understanding:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01861))_

> parentList.rest.rest.first = "three"; childList.first = "two";

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01859))_

> Let’s confirm our understanding:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01862))_

> parentList _//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\_ {},"rest":{}}}}} childList _//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}_

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01868))_

> **const** copy = (node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail === **null** ) { **const** { first, rest } = node; **const** newNode = { first, rest }; **return** copy(rest, newNode, newNode); } **else** { **const** { first, rest } = node; **const** newNode = { first, rest }; tail.rest = newNode; **return** copy(node.rest, head, newNode); } } **const** first = ({first, rest}) => first; **const** rest = ({first, rest}) => rest; **con

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01871))_

> **const** childList = rest(parentList);

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01875))_

> So back to the problem of structure sharing. One strategy for avoiding problems is to be _pessimistic_ . Whenever we take the rest of a list, make a copy.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01876))_

> **const** rest = ({first, rest}) => copy(rest);


## Source

- [[javascriptallonge]]
