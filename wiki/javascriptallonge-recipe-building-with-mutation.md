---
page_id: javascriptallonge-recipe-building-with-mutation
page_kind: recipe
page_family: recipe-pattern
summary: building with mutation: reusable source-backed pattern with 6 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: building-with-mutation
projection_coverage: recipe-javascriptallonge-recipe-building-with-mutation@b7534bd743e70acd04367ecaddcc0ce3
---

# building with mutation

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-mutation-building-with-mutation-bd1adba2]].
- Evidence roles: decision, constraint, procedure, example.

## Applicability And Rationale

- As noted, one pattern is to be more liberal about mutation when building a data structure. _(javascriptallonge.pdf (source-range-7239e085-01153))_
- Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list: _(javascriptallonge.pdf (source-range-7239e085-01153))_
- If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation: _(javascriptallonge.pdf (source-range-7239e085-01155))_
- This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. _(javascriptallonge.pdf (source-range-7239e085-01157))_
- But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time. _(javascriptallonge.pdf (source-range-7239e085-01157))_
- Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. _(javascriptallonge.pdf (source-range-7239e085-01157))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01154)_

```
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
const copy = (node) => reverse(reverse(node));
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01156)_

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
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01159)_

```
const mapWith = (fn, node, head = null, tail = null) => {
if (node === EMPTY) {
return head;
}
else if (tail === null) {
const { first, rest } = node;
const newNode = { first: fn(first), rest };
return mapWith(fn, rest, newNode, newNode);
}
else {
const { first, rest } = node;
const newNode = { first: fn(first), rest };
tail.rest = newNode;
return mapWith(fn, node.rest, head, newNode);
}
}
mapWith((x) => 1.0 / x, OneToFive)
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01160)_

```
//=> {"first":1,"rest":{"first":0.5,"rest":{"first":0.3333333333333333,"rest":\
{"first":0.25,"rest":{"first":0.2,"rest":{}}}}}}
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-mutation-building-with-mutation-bd1adba2]]
