---
page_id: javascriptallonge-mutation
page_kind: source
summary: building with mutation from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.145-147
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter explains how mutation works in JavaScript, covering arrays, objects, aliases, and assignment semantics, with possible nuances. This specific section focuses on building data structures with mutation, particularly in the context of linked lists.

## Key supported claims

- As noted, one pattern is to be more liberal about mutation when building a data structure (raw/javascriptallonge.pdf p.145-147).
- If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation (raw/javascriptallonge.pdf p.145-147).
- But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time (raw/javascriptallonge.pdf p.145-147).

## Technical details

### `technical-atom-557049b5cf0f5bf9` code

Citation: (raw/javascriptallonge.pdf p.145-147)

```javascript
const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3 ]
```

### `technical-atom-fd0c024f84e5f03d` code

Citation: (raw/javascriptallonge.pdf p.145-147)

```javascript
const oneTwoThree = [1, 2, 3]; oneTwoThree[3] = 'four'; oneTwoThree //=> [ 1, 2, 3, 'four' ]
```

### `technical-atom-cc5f70ab0a451973` code

Citation: (raw/javascriptallonge.pdf p.145-147)

```javascript
const name = {firstName: 'Leonard', lastName: 'Braithwaite'}; name.middleName = 'Austin' name //=> { firstName: 'Leonard', # lastName: 'Braithwaite', # middleName: 'Austin' }
```

### `technical-atom-26bf4ade63700da9` code

Citation: (raw/javascriptallonge.pdf p.145-147)

```javascript
const allHallowsEve = [2012, 10, 31] const halloween = allHallowsEve;
```

### `technical-atom-03b4a42d4f365721` code

Citation: (raw/javascriptallonge.pdf p.145-147)

```javascript
const allHallowsEve = [2012, 10, 31]; ( function (halloween) { // ... })(allHallowsEve);
```

### `technical-atom-8fc597545d9b2eee` code

Citation: (raw/javascriptallonge.pdf p.145-147)

```javascript
const allHallowsEve = [2012, 10, 31]; ( function (halloween) { halloween = [2013, 10, 31]; })(allHallowsEve); allHallowsEve //=> [2012, 10, 31]
```

### `technical-atom-06dddd499ef550a3` code

Citation: (raw/javascriptallonge.pdf p.145-147)

```javascript
const allHallowsEve = [2012, 10, 31]; ( function (halloween) { halloween[0] = 2013; })(allHallowsEve); allHallowsEve //=> [2013, 10, 31]
```

### `technical-atom-d501bc9f53f216ef` code

Citation: (raw/javascriptallonge.pdf p.145-147)

```javascript
const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); const copy = (node) => reverse(reverse(node));
```

## Related technical details

### From [[javascriptallonge-mutation-and-data-structures]]: `technical-atom-6fbbc51a9f84f2a8` code

Relation: nearby source page; matched terms `brand`, `but`, `copy`, `data`, `linked`, `lists`

Citation: (raw/javascriptallonge.pdf p.143-145)

```javascript
const EMPTY = {}; const OneToFive = { first: 1, rest: { first: 2, rest: { first: 3, rest: { first: 4, rest: { first: 5, rest: EMPTY } } } } }; OneToFive //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\ r","rest":{"first":"five","rest":{}}}}}} const ThreeToFive = OneToFive.rest.rest; ThreeToFive //=> {"first":3,"rest":{"first":4,"rest":{"first":5,"rest":{}}}} ThreeToFive.first = "three"; ThreeToFive.rest.first = "four"; ThreeToFive.rest.rest.first = "five"; ThreeToFive //=> {"first":"three","rest":{"first":"four","rest":{"first":"five","rest":{}}\ }} OneToFive //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\ r","rest":{"first":"five","rest":{}}}}}} Changes made to ThreeToFive affect OneToFive , because they share the same structure. When we wrote ThreeToFive = OneToFive.rest.rest; , we weren't making a brand new copy of {"first":3,"rest":{"fir we were getting a reference to the same chain of nodes. Structure sharing like this is what makes linked lists so fast for taking everything but the first item
```

### From [[javascriptallonge-mutation-and-data-structures]]: `technical-atom-716ed5f15b0b87c8` procedure

Relation: nearby source page; matched terms `about`, `but`, `data`, `list`, `mutation`, `new`

Citation: (raw/javascriptallonge.pdf p.143-145)

But after returning the new list, we then become conservative about mutation.

### From [[javascriptallonge-mutation-and-data-structures]]: `technical-atom-b7f80818a51816bb` formula

Relation: nearby source page; matched terms `brand`, `copy`, `data`, `making`, `mutation`, `new`

Citation: (raw/javascriptallonge.pdf p.143-145)

When we wrote ThreeToFive = OneToFive.rest.rest; , we weren't making a brand new copy of {"first":3,"rest":{"fir we were getting a reference to the same chain of nodes.

### From [[javascriptallonge-mutation-and-data-structures]]: `technical-atom-696e87e5d432d18d` procedure

Relation: nearby source page; matched terms `copy`, `data`, `make`, `mutation`, `structures`

Citation: (raw/javascriptallonge.pdf p.143-145)

Whereas destructuring an array with [first, ...rest] does make a copy, so:
