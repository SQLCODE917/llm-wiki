---
page_id: javascriptallonge-section-copy-on-write-a1ad4ef5
page_kind: source
summary: Copy on Write: 37 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-a1ad4ef5@b4bdb1a9051a8e083f27d008a010c62e
---

# Copy on Write

From [[javascriptallonge]].

## Statements

- We’ve seen how to build lists with arrays and with linked lists. _(javascriptallonge.pdf (source-range-83ecb080-01852))_
- - When you take the rest of an array with destructuring ([first, ...rest]), you are given a _copy_ of the elements of the array. _(javascriptallonge.pdf (source-range-83ecb080-01853))_
- - When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list. _(javascriptallonge.pdf (source-range-83ecb080-01854))_
- And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-83ecb080-01855))_
- And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-83ecb080-01855))_
- And therefore, modifications to the parent also modify the child, and modifications to the child also modify the parent. _(javascriptallonge.pdf (source-range-83ecb080-01858))_
- We’ll end up reinventing reference counting and garbage collection. _(javascriptallonge.pdf (source-range-83ecb080-01863))_
- If we _know_ that a list doesn’t share any elements with another list, we can safely modify it. _(javascriptallonge.pdf (source-range-83ecb080-01863))_
- before we go any further, let’s write a few naïve list utilities so that we can work at a slightly higher level of abstraction: _(javascriptallonge.pdf (source-range-83ecb080-01865))_
- before we go any further, let’s write a few naïve list utilities so that we can work at a slightly higher level of abstraction: _(javascriptallonge.pdf (source-range-83ecb080-01865))_
- The main difference is that array[index] = value evaluates to value, while set(index, value, list) evaluates to the modified list. _(javascriptallonge.pdf (source-range-83ecb080-01873))_
- Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-83ecb080-01875))_
- One strategy for avoiding problems is to be _pessimistic_ . _(javascriptallonge.pdf (source-range-83ecb080-01875))_
- This strategy is called “copy-on-read”, because when we attempt the parent to “read” the value of a child of the list, we make a copy and read the copy of the child. _(javascriptallonge.pdf (source-range-83ecb080-01879))_
- Thereafter, we can write to the parent or the copy of the child freely. _(javascriptallonge.pdf (source-range-83ecb080-01879))_
- This strategy is called “copy-on-read”, because when we attempt the parent to “read” the value of a child of the list, we make a copy and read the copy of the child. _(javascriptallonge.pdf (source-range-83ecb080-01879))_
- As we expected, making a copy lets us modify the copy without interfering with the original. _(javascriptallonge.pdf (source-range-83ecb080-01880))_
- Our mapWith function would be very expensive if we make a copy every time we call rest(node). _(javascriptallonge.pdf (source-range-83ecb080-01880))_
- Sometimes we don’t need to make a copy because we won’t be modifying the list. _(javascriptallonge.pdf (source-range-83ecb080-01880))_
- Sometimes we don’t need to make a copy because we won’t be modifying the list. _(javascriptallonge.pdf (source-range-83ecb080-01880))_
- But before we fix that, let’s try being lazy about copying. _(javascriptallonge.pdf (source-range-83ecb080-01881))_
- But before we fix that, let’s try being lazy about copying. _(javascriptallonge.pdf (source-range-83ecb080-01881))_
- But our new parent and child lists are copies that contain the desired modifications, without interfering with each other: _(javascriptallonge.pdf (source-range-83ecb080-01891))_
- And now functions like mapWith that make copies without modifying anything, work at full speed. _(javascriptallonge.pdf (source-range-83ecb080-01894))_
- This strategy of waiting to copy until you are writing is called copy-on-write, or “COW:” _(javascriptallonge.pdf (source-range-83ecb080-01895))_
- This strategy of waiting to copy until you are writing is called copy-on-write, or “COW:” _(javascriptallonge.pdf (source-range-83ecb080-01895))_
- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.— Wikipedia[73] _(javascriptallonge.pdf (source-range-83ecb080-01898))_
- Once we’re done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-83ecb080-01900))_
- Looking at the code again, you see that the copy function doesn’t copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. _(javascriptallonge.pdf (source-range-83ecb080-01900))_

## Technical atoms

> Context: When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list.
_(context: javascriptallonge.pdf (source-range-83ecb080-01854))_

> The consequence of this is that if you have an array, and you take it’s “rest,” your “child” array is a copy of the elements of the parent array.
_(source: javascriptallonge.pdf (source-range-83ecb080-01855))_

> Whereas if you have a linked list, and you take it’s “rest,” your “child” list shares its nodes with the “parent” list.
_(source: javascriptallonge.pdf (source-range-83ecb080-01858))_

> Context: Let’s confirm our understanding:
_(context: javascriptallonge.pdf (source-range-83ecb080-01859))_

> parentList.rest.rest.first = "three"; childList.first = "two";
_(source: javascriptallonge.pdf (source-range-83ecb080-01861))_

> Context: Let’s confirm our understanding:
_(context: javascriptallonge.pdf (source-range-83ecb080-01859))_

> parentList _//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\_ {},"rest":{}}}}} childList _//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}_
_(source: javascriptallonge.pdf (source-range-83ecb080-01862))_

> Context: **const** copy = (node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail === **null** ) { **const** { first, rest } = node; **const** newNode = { first, rest }; **return** copy(rest, newNode, newNode); } **else** { **const** { first, rest } = node; **const** newNode = { first, rest }; tail.rest = newNode; **return** copy(node.rest, head, newNode); } } **const** first = ({first, rest}) => first; **const** rest = ({first, rest}) => rest; **con
_(context: javascriptallonge.pdf (source-range-83ecb080-01868))_

> **const** childList = rest(parentList);
_(source: javascriptallonge.pdf (source-range-83ecb080-01871))_

> Context: So back to the problem of structure sharing. One strategy for avoiding problems is to be _pessimistic_ . Whenever we take the rest of a list, make a copy.
_(context: javascriptallonge.pdf (source-range-83ecb080-01875))_

> **const** rest = ({first, rest}) => copy(rest);
_(source: javascriptallonge.pdf (source-range-83ecb080-01876))_

> Context: So back to the problem of structure sharing. One strategy for avoiding problems is to be _pessimistic_ . Whenever we take the rest of a list, make a copy. This strategy is called “copy-on-read”, because when we attempt the parent to “read” the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.
_(context: javascriptallonge.pdf (source-range-83ecb080-01875, source-range-83ecb080-01879))_

> parentList _//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\_ rest":{}}}}} childList //=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
_(source: javascriptallonge.pdf (source-range-83ecb080-01878))_

> Context: Why are we copying? In case we modify a child list. Ok, what if we do this: Make the copy when we know we are modifying the list. When do we know that? When we call set. We’ll restore our original definition for rest, but change set:
_(context: javascriptallonge.pdf (source-range-83ecb080-01885))_

> **const** rest = ({first, rest}) => rest;
_(source: javascriptallonge.pdf (source-range-83ecb080-01886))_
