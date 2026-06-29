---
page_id: javascriptallonge-copy-write
page_kind: concept
summary: Copy on Write: 13 statement(s) and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-copy-write@ff5ab608181341ee39d10134e052075f
---

# Copy on Write

What [[javascriptallonge]] covers about copy on write:

## Statements

### Copy on Write

- We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: _(javascriptallonge.pdf (source-range-8eb13d6b-01224))_

- When you take the rest of an array with destructuring ( [first, ...rest] ), you are given a copy of the elements of the array. _(javascriptallonge.pdf (source-range-8eb13d6b-01225))_

- When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list. _(javascriptallonge.pdf (source-range-8eb13d6b-01226))_

- The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-8eb13d6b-01227))_

- This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection. _(javascriptallonge.pdf (source-range-8eb13d6b-01231))_

### copy-on-read

- This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely. _(javascriptallonge.pdf (source-range-8eb13d6b-01240))_

### copy-on-write

- But our new parent and child lists are copies that contain the desired modifications, without interfering with each other: _(javascriptallonge.pdf (source-range-8eb13d6b-01248))_

- And now functions like mapWith that make copies without modifying anything, work at full speed. _(javascriptallonge.pdf (source-range-8eb13d6b-01250))_

- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' _(javascriptallonge.pdf (source-range-8eb13d6b-01251))_

- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.Wikipedia 73 _(javascriptallonge.pdf (source-range-8eb13d6b-01252))_

- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-8eb13d6b-01254))_


## Technical atoms

### Technical frame 1: Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01231))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01227))_

> The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array.

### Technical frame 2: Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01231))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01228))_

> Whereas if you have a linked list, and you take it's 'rest,' your 'child' list shares its nodes with the 'parent' list.

### Technical frame 3: Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01231))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01230))_

```
const parentArray = [1, 2, 3]; const [aFirst, ...childArray] = parentArray; parentArray[2] = "three"; childArray[0] = "two"; parentArray //=> [1,2,"three"] childArray //=> ["two",3] const EMPTY = { first: {}, rest: {} }; const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; const childList = parentList.rest; parentList.rest.rest.first = "three"; childList.first = "two"; parentList //=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\ {},"rest":{}}}}} childList //=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}
```

### Technical frame 4: copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01248))_

> But our new parent and child lists are copies that contain the desired modifications, without interfering with each other:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01245))_

```
const rest = ({first, rest}) => rest; const set = (index, value, list) => index === 0 ? { first: value, rest: list.rest } : { first: list.first, rest: set(index - 1, value, list.rest) }; const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; const childList = rest(parentList); const newParentList = set(2, "three", parentList); const newChildList = set(0, "two", childList);
```

### Technical frame 5: copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01248))_

> But our new parent and child lists are copies that contain the desired modifications, without interfering with each other:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01247))_

```
parentList //=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{"first":{},"rest":\ {}}}}} childList //=> {"first":2,"rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

### Technical frame 6: copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01250))_

> And now functions like mapWith that make copies without modifying anything, work at full speed.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01249))_

```
newParentList //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\ rest":{}}}}} newChildList //=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```


## Related pages

- [[javascriptallonge-copy]] - broader topic: Copy shares source evidence from copy-on-write: This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:'; Copy shares technical record from copy-on-write: const rest = ({first, rest}) => rest; const set = (index, value, list) => index === 0 ? { first: value, rest: list.rest } : { first: list.first, rest: set(index - 1, ... [truncated] (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-write]] - broader topic: Write shares source evidence from copy-on-write: Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) c ... [truncated] (2 shared statement(s))
- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from Copy on Write: We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them:; List shares technical record from Copy on Write: The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. (3 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-rest]] - shared statements and technical atoms: Rest shares source evidence from Copy on Write: When you take the rest of an array with destructuring ( [first, ...rest] ), you are given a copy of the elements of the array.; Rest shares technical record from Copy on Write: The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms: Element shares source evidence from Copy on Write: This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunc ... [truncated]; Element shares technical record from Copy on Write: The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-array]] - shared statements: Array shares source evidence from Copy on Write: We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: (2 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from copy-on-write: And now functions like mapWith that make copies without modifying anything, work at full speed. (2 shared statement(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-follow]] - shared statements: Follow shares source evidence from copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-mapwith]] - shared statements: Mapwith shares source evidence from copy-on-write: And now functions like mapWith that make copies without modifying anything, work at full speed. (1 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-seen]] - shared statements: Seen shares source evidence from Copy on Write: We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: (1 shared statement(s))
- [[javascriptallonge-section-copy-on-write-42cc7136]] - source section: Copy on Write shares source evidence from Copy on Write: We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them:; Copy on Write shares technical record from Copy on Write: The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. (6 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-section-copy-on-write-e50e229e]] - source section: copy-on-write shares source evidence from copy-on-write: But our new parent and child lists are copies that contain the desired modifications, without interfering with each other:; copy-on-write shares technical record from copy-on-write: const rest = ({first, rest}) => rest; const set = (index, value, list) => index === 0 ? { first: value, rest: list.rest } : { first: list.first, rest: set(index - 1, ... [truncated] (6 shared statement(s), 3 shared atom(s))

## Source

- [[javascriptallonge]]
