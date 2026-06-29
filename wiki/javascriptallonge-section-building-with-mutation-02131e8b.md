---
page_id: javascriptallonge-section-building-with-mutation-02131e8b
page_kind: source
summary: building with mutation: 10 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-building-with-mutation-02131e8b@6fc647f479e79506a9d1139ed4e28d30
---

# building with mutation

From [[javascriptallonge]].

## Statements

- As noted, one pattern is to be more liberal about mutation when building a data structure. Consider our copy algorithm. Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list: _(javascriptallonge.pdf (source-range-8eb13d6b-01152))_
- If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation: _(javascriptallonge.pdf (source-range-8eb13d6b-01154))_
- This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time. _(javascriptallonge.pdf (source-range-8eb13d6b-01156))_

## Technical atoms

### Technical frame 1: building with mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01154))_

> If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01153))_

```
const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); const copy = (node) => reverse(reverse(node));
```

### Technical frame 2: building with mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01156))_

> This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01155))_

```
const copy = (node, head = null , tail = null ) => { if (node === EMPTY) { return head; } else if (tail === null ) { const { first, rest } = node; const newNode = { first, rest }; return copy(rest, newNode, newNode); } else { const { first, rest } = node; const newNode = { first, rest }; tail.rest = newNode; return copy(node.rest, head, newNode); } }
```

### Technical frame 3: building with mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01156))_

> This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01158))_

```
const mapWith = (fn, node, head = null , tail = null ) => { if (node === EMPTY) { return head; } else if (tail === null ) { const { first, rest } = node; const newNode = { first: fn(first), rest }; return mapWith(fn, rest, newNode, newNode); } else { const { first, rest } = node; const newNode = { first: fn(first), rest }; tail.rest = newNode; return mapWith(fn, node.rest, head, newNode); } } mapWith((x) => 1.0 / x, OneToFive)
```

### Technical frame 4: building with mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01156))_

> This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01159))_

```
//=> {"first":1,"rest":{"first":0.5,"rest":{"first":0.3333333333333333,"rest":\ {"first":0.25,"rest":{"first":0.2,"rest":{}}}}}}
```
