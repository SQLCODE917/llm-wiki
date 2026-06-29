---
page_id: javascriptallonge-section-copy-on-write-e50e229e
page_kind: source
summary: copy-on-write: 10 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-e50e229e@e497b4e8a08dcb767f716cee4a83c6cd
---

# copy-on-write

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-copy-write]] - topic hub: opens the topic page for Copy Write
- [[javascriptallonge-section-copy-on-write-42cc7136]] - same source heading: another source section with the same heading, Copy on Write

## Statements

- But our new parent and child lists are copies that contain the desired modifications, without interfering with each other: _(javascriptallonge.pdf (source-range-8eb13d6b-01248))_
- And now functions like mapWith that make copies without modifying anything, work at full speed. _(javascriptallonge.pdf (source-range-8eb13d6b-01250))_
- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' _(javascriptallonge.pdf (source-range-8eb13d6b-01251))_
- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.Wikipedia 73 _(javascriptallonge.pdf (source-range-8eb13d6b-01252))_
- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-8eb13d6b-01254))_
- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' _(javascriptallonge.pdf (source-range-8eb13d6b-01251))_

## Technical atoms

### Technical frame 1: copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01248))_

> But our new parent and child lists are copies that contain the desired modifications, without interfering with each other:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01245))_

```
const rest = ({first, rest}) => rest; const set = (index, value, list) => index === 0 ? { first: value, rest: list.rest } : { first: list.first, rest: set(index - 1, value, list.rest) }; const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; const childList = rest(parentList); const newParentList = set(2, "three", parentList); const newChildList = set(0, "two", childList);
```

### Technical frame 2: copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01248))_

> But our new parent and child lists are copies that contain the desired modifications, without interfering with each other:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01247))_

```
parentList //=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{"first":{},"rest":\ {}}}}} childList //=> {"first":2,"rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

### Technical frame 3: copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01250))_

> And now functions like mapWith that make copies without modifying anything, work at full speed.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01249))_

```
newParentList //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\ rest":{}}}}} newChildList //=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```
