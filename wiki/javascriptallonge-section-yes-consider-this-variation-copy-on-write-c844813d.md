---
page_id: javascriptallonge-section-yes-consider-this-variation-copy-on-write-c844813d
page_kind: source
summary: Yes. Consider this variation: / Copy on Write: 34 source-backed entries and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-yes-consider-this-variation-copy-on-write-c844813d@cc39da0d9d5cc1572757324383cb4458
---

# Yes. Consider this variation: / Copy on Write

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-yes-consider-this-variation-b8b28d41]] - broader source section: Yes. Consider this variation:
- [[javascriptallonge-section-yes-consider-this-variation-copy-on-write-a-few-utilities-cdb2bac1]] - narrower source section: Yes. Consider this variation: / Copy on Write / a few utilities
- [[javascriptallonge-section-yes-consider-this-variation-copy-on-write-copy-on-read-4f68c68b]] - narrower source section: Yes. Consider this variation: / Copy on Write / copy-on-read
- [[javascriptallonge-section-yes-consider-this-variation-copy-on-write-copy-on-write-d1a59880]] - narrower source section: Yes. Consider this variation: / Copy on Write / copy-on-write
- [[javascriptallonge-copy-write]] - topic hub: opens the topic page for Copy Write
- [[javascriptallonge-section-yes-consider-this-variation-copy-on-write-copy-on-write-d1a59880]] - same source heading: another source section with the same heading, Yes. Consider this variation: / Copy on Write / copy-on-write

## Statements

- We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: _(javascriptallonge.pdf (source-range-7239e085-01225))_
- When you take the rest of an array with destructuring ( [first, ...rest] ), you are given a copy of the elements of the array. _(javascriptallonge.pdf (source-range-7239e085-01226))_
- When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list. _(javascriptallonge.pdf (source-range-7239e085-01227))_
- The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-7239e085-01228))_
- This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection. _(javascriptallonge.pdf (source-range-7239e085-01232))_
- And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-7239e085-01228))_

## Statements by subsection

### Yes. Consider this variation: / Copy on Write / a few utilities

- Our new at and set functions behave similarly to array[index] and array[index] = value . The main difference is that array[index] = value evaluates to value , while set(index, value, list) evaluates to the modified list . _(javascriptallonge.pdf (source-range-7239e085-01237))_

### Yes. Consider this variation: / Copy on Write / copy-on-read

- So back to the problem of structure sharing. One strategy for avoiding problems is to be pessimistic . Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-7239e085-01239))_
- This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely. _(javascriptallonge.pdf (source-range-7239e085-01241))_
- As we expected, making a copy lets us modify the copy without interfering with the original. This is, however, expensive. Sometimes we don't need to make a copy because we won't be modifying the list. Our mapWith function would be very expensive if we make a copy every time we call rest(node) . _(javascriptallonge.pdf (source-range-7239e085-01242))_
- This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. _(javascriptallonge.pdf (source-range-7239e085-01241))_
- Sometimes we don't need to make a copy because we won't be modifying the list. _(javascriptallonge.pdf (source-range-7239e085-01242))_

### Yes. Consider this variation: / Copy on Write / copy-on-write

- But our new parent and child lists are copies that contain the desired modifications, without interfering with each other: _(javascriptallonge.pdf (source-range-7239e085-01249))_
- And now functions like mapWith that make copies without modifying anything, work at full speed. _(javascriptallonge.pdf (source-range-7239e085-01251))_
- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' _(javascriptallonge.pdf (source-range-7239e085-01252))_
- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.Wikipedia 73 _(javascriptallonge.pdf (source-range-7239e085-01253))_
- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-7239e085-01255))_
- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' _(javascriptallonge.pdf (source-range-7239e085-01252))_

## Technical atoms

### Technical frame 1: Yes. Consider this variation: / Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01225))_

> We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01223))_

> [Figure] (p.158)

### Technical frame 2: Yes. Consider this variation: / Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01232))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01228))_

> The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array.

### Technical frame 3: Yes. Consider this variation: / Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01232))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01229))_

> Whereas if you have a linked list, and you take it's 'rest,' your 'child' list shares its nodes with the 'parent' list.

### Technical frame 4: Yes. Consider this variation: / Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01232))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01231))_

```
const parentArray = [1, 2, 3];
const [aFirst, ...childArray] = parentArray;
parentArray[2] = "three";
childArray[0] = "two";
parentArray
//=> [1,2,"three"]
childArray
//=> ["two",3]
const EMPTY = { first: {}, rest: {} };
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
const childList = parentList.rest;
parentList.rest.rest.first = "three";
childList.first = "two";
parentList
//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\
{},"rest":{}}}}}
childList
//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}
```

### Technical frame 5: Yes. Consider this variation: / Copy on Write / a few utilities

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01237))_

> Our new at and set functions behave similarly to array[index] and array[index] = value . The main difference is that array[index] = value evaluates to value , while set(index, value, list) evaluates to the modified list .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01235))_

```
const copy = (node, head = null, tail = null) => {
if (node === EMPTY) {
return head;
}
else if (tail === null) {
const { first, rest } = node;
const newNode = { first, rest };
return copy(rest, newNode, newNode);
}
else {
const { first, rest } = node;
const newNode = { first, rest };
tail.rest = newNode;
return copy(node.rest, head, newNode);
}
}
const first = ({first, rest}) => first;
const rest = ({first, rest}) => rest;
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(rest(node), { first: first(node), rest: delayed });
const mapWith = (fn, node, delayed = EMPTY) =>
node === EMPTY
? reverse(delayed)
: mapWith(fn, rest(node), { first: fn(first(node)), rest: delayed });
const at = (index, list) =>
index === 0
? first(list)
: at(index - 1, rest(list));
const set = (index, value, list, originalList = list) =>
index === 0
? (list.first = value, originalList)
: set(index - 1, value, rest(list), originalList)
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
```

### Technical frame 6: Yes. Consider this variation: / Copy on Write / a few utilities

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01237))_

> Our new at and set functions behave similarly to array[index] and array[index] = value . The main difference is that array[index] = value evaluates to value , while set(index, value, list) evaluates to the modified list .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01236))_

```
const childList = rest(parentList);
set(2, "three", parentList);
set(0, "two", childList);
parentList
//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\
{},"rest":{}}}}}
childList
//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}
```

### Technical frame 7: Yes. Consider this variation: / Copy on Write / copy-on-read

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01241))_

> This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01240))_

```
const rest = ({first, rest}) => copy(rest);
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
const childList = rest(parentList);
const newParentList = set(2, "three", parentList);
set(0, "two", childList);
parentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\
rest":{}}}}}
childList
//=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

### Technical frame 8: Yes. Consider this variation: / Copy on Write / copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01249))_

> But our new parent and child lists are copies that contain the desired modifications, without interfering with each other:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01246))_

```
const rest = ({first, rest}) => rest;
const set = (index, value, list) =>
index === 0
? { first: value, rest: list.rest }
: { first: list.first, rest: set(index - 1, value, list.rest) };
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
const childList = rest(parentList);
const newParentList = set(2, "three", parentList);
const newChildList = set(0, "two", childList);
```

### Technical frame 9: Yes. Consider this variation: / Copy on Write / copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01249))_

> But our new parent and child lists are copies that contain the desired modifications, without interfering with each other:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01248))_

```
parentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{"first":{},"rest":\
{}}}}}
childList
//=> {"first":2,"rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

### Technical frame 10: Yes. Consider this variation: / Copy on Write / copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01251))_

> And now functions like mapWith that make copies without modifying anything, work at full speed.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01250))_

```
newParentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\
rest":{}}}}}
newChildList
//=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```
