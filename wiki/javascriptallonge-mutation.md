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
