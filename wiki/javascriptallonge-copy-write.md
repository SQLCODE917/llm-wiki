---
page_id: javascriptallonge-copy-write
page_kind: concept
page_family: topic-concept
summary: Copy on Write: 18 statement(s) and 9 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-copy-write@973fb568984da95937bf16db5604bf5a
---

# Copy on Write

What [[javascriptallonge]] covers about copy on write:

## Statements

### Yes. Consider this variation: / Copy on Write

- We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: _(javascriptallonge.pdf (source-range-7239e085-01225))_

- When you take the rest of an array with destructuring ( [first, ...rest] ), you are given a copy of the elements of the array. _(javascriptallonge.pdf (source-range-7239e085-01226))_

- When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list. _(javascriptallonge.pdf (source-range-7239e085-01227))_

- The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-7239e085-01228))_

- This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection. _(javascriptallonge.pdf (source-range-7239e085-01232))_

### Yes. Consider this variation: / Copy on Write / a few utilities

- Our new at and set functions behave similarly to array[index] and array[index] = value . The main difference is that array[index] = value evaluates to value , while set(index, value, list) evaluates to the modified list . _(javascriptallonge.pdf (source-range-7239e085-01237))_

### Yes. Consider this variation: / Copy on Write / copy-on-read

- So back to the problem of structure sharing. One strategy for avoiding problems is to be pessimistic . Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-7239e085-01239))_

- This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely. _(javascriptallonge.pdf (source-range-7239e085-01241))_

- As we expected, making a copy lets us modify the copy without interfering with the original. This is, however, expensive. Sometimes we don't need to make a copy because we won't be modifying the list. Our mapWith function would be very expensive if we make a copy every time we call rest(node) . _(javascriptallonge.pdf (source-range-7239e085-01242))_

### Yes. Consider this variation: / Copy on Write / copy-on-write

- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' _(javascriptallonge.pdf (source-range-7239e085-01252))_

- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.Wikipedia 73 _(javascriptallonge.pdf (source-range-7239e085-01253))_

- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-7239e085-01255))_


## Technical atoms

### Technical frame 1: Yes. Consider this variation: / Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01232))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01228))_

<a id="atom-technical-atom-bba78c8b3994a437"></a>

> The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array.

### Technical frame 2: Yes. Consider this variation: / Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01232))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01229))_

<a id="atom-technical-atom-107209144ad81087"></a>

> Whereas if you have a linked list, and you take it's 'rest,' your 'child' list shares its nodes with the 'parent' list.

### Technical frame 3: Yes. Consider this variation: / Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01232))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01231))_

<a id="atom-technical-atom-0dba4e36fbe27ea3"></a>

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

### Technical frame 4: Yes. Consider this variation: / Copy on Write / a few utilities

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01237))_

> Our new at and set functions behave similarly to array[index] and array[index] = value . The main difference is that array[index] = value evaluates to value , while set(index, value, list) evaluates to the modified list .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01235))_

<a id="atom-technical-atom-64a7fceac62859bb"></a>

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

### Technical frame 5: Yes. Consider this variation: / Copy on Write / a few utilities

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01237))_

> Our new at and set functions behave similarly to array[index] and array[index] = value . The main difference is that array[index] = value evaluates to value , while set(index, value, list) evaluates to the modified list .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01236))_

<a id="atom-technical-atom-cb1cad9bb1c97594"></a>

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

### Technical frame 6: Yes. Consider this variation: / Copy on Write / copy-on-read

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01241))_

> This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01240))_

<a id="atom-technical-atom-05e2937fc47dd397"></a>

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

### Technical frame 7: Yes. Consider this variation: / Copy on Write / copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01252))_

> This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01246))_

<a id="atom-technical-atom-e60d6ebf60601e8a"></a>

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

### Technical frame 8: Yes. Consider this variation: / Copy on Write / copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01252))_

> This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01248))_

<a id="atom-technical-atom-75b9035c0deba14b"></a>

```
parentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{"first":{},"rest":\
{}}}}}
childList
//=> {"first":2,"rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

### Technical frame 9: Yes. Consider this variation: / Copy on Write / copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01252))_

> This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01250))_

<a id="atom-technical-atom-64e23430e7b317d4"></a>

```
newParentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\
rest":{}}}}}
newChildList
//=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```


## Related pages

### Source structure

- [[javascriptallonge-section-yes-consider-this-variation-copy-on-write-c844813d]] - source section: Yes. Consider this variation: / Copy on Write shares source evidence from Yes. Consider this variation: / Copy on Write: We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them:; Yes. Consider this variation: / Copy on Write shares technical record from Yes. Consider this variation: / Copy on Write: The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. (18 shared statement(s), 9 shared atom(s))
- [[javascriptallonge-section-yes-consider-this-variation-copy-on-write-copy-on-write-d1a59880]] - source section: Yes. Consider this variation: / Copy on Write / copy-on-write shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:'; Yes. Consider this variation: / Copy on Write / copy-on-write shares technical record from Yes. Consider this variation: / Copy on Write / copy-on-write: const rest = ({first, rest}) => rest; const set = (index, value, list) => index === 0 ? { first: value, rest: list.rest } : { first: list.first, rest: set(index - 1, ... [truncated] (4 shared statement(s), 3 shared atom(s))

### Shared technical atoms

- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from Yes. Consider this variation: / Copy on Write: We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them:; List shares technical record from Yes. Consider this variation: / Copy on Write: The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. (3 shared statement(s), 8 shared atom(s))
- [[javascriptallonge-rest]] - shared statements and technical atoms: Rest shares source evidence from Yes. Consider this variation: / Copy on Write: When you take the rest of an array with destructuring ( [first, ...rest] ), you are given a copy of the elements of the array.; Rest shares technical record from Yes. Consider this variation: / Copy on Write: The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. (3 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms: Element shares source evidence from Yes. Consider this variation: / Copy on Write: This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunc ... [truncated]; Element shares technical record from Yes. Consider this variation: / Copy on Write: The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-problem]] - shared statements and technical atoms: Problem shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-read: So back to the problem of structure sharing. One strategy for avoiding problems is to be pessimistic . Whenever we take the rest of a list, make a copy.; Problem shares technical record from Yes. Consider this variation: / Copy on Write / copy-on-read: const rest = ({first, rest}) => copy(rest); const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; const childList = rest(parentList); ... [truncated] (1 shared statement(s), 1 shared atom(s))

### Shared claims

- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-read: As we expected, making a copy lets us modify the copy without interfering with the original. This is, however, expensive. Sometimes we don't need to make a copy beca ... [truncated] (2 shared statement(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-follow]] - shared statements: Follow shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-mapwith]] - shared statements: Mapwith shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-read: As we expected, making a copy lets us modify the copy without interfering with the original. This is, however, expensive. Sometimes we don't need to make a copy beca ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-seen]] - shared statements: Seen shares source evidence from Yes. Consider this variation: / Copy on Write: We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: (1 shared statement(s))

### Topics

- [[javascriptallonge-copy]] - broader topic: Copy shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:'; Copy shares technical record from Yes. Consider this variation: / Copy on Write / copy-on-write: const rest = ({first, rest}) => rest; const set = (index, value, list) => index === 0 ? { first: value, rest: list.rest } : { first: list.first, rest: set(index - 1, ... [truncated] (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-write]] - broader topic: Write shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) c ... [truncated] (2 shared statement(s))

## Source

- [[javascriptallonge]]
