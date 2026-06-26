---
page_id: javascriptallonge-mutation
page_kind: source
summary: Mutation from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.141-147
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

Chapter on mutation in JavaScript, covering data structures, aliases, and mutation patterns.

## Key supported claims

- In JavaScript, arrays and objects can mutate, changing their structure while keeping the same identity (raw/javascriptallonge.pdf p.141-147).
- Declaring a variable as const does not prevent mutation of the value it references, only rebinding of the name (raw/javascriptallonge.pdf p.141-147).
- Mutation in shared references affects all aliases, as changes are made to the same underlying data (raw/javascriptallonge.pdf p.141-147).
- Languages like Haskell avoid mutation entirely, which can make reasoning about code easier (raw/javascriptallonge.pdf p.141-147).
- Patterns exist for being liberal with mutation during construction and conservative during consumption (raw/javascriptallonge.pdf p.141-147).

## Technical details

### `technical-atom-567a5c480a1bf057` code

Citation: (raw/javascriptallonge.pdf p.141-147)

```javascript
const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3]
```

### `technical-atom-191889ae7465b169` code

Citation: (raw/javascriptallonge.pdf p.141-147)

```javascript
const oneTwoThree = [1, 2, 3]; oneTwoThree[3] = 'four'; oneTwoThree //=> [ 1, 2, 3, 'four']
```

### `technical-atom-9c85fa2c9f1e2c6c` code

Citation: (raw/javascriptallonge.pdf p.141-147)

```javascript
const name = {firstName: 'Leonard', lastName: 'Braithwaite'}; name.middleName = 'Austin' name //=> { firstName: 'Leonard', # lastName: 'Braithwaite', # middleName: 'Austin' }
```

### `technical-atom-54a458cee3a728f0` code

Citation: (raw/javascriptallonge.pdf p.141-147)

```javascript
const allHallowsEve = [2012, 10, 31] const halloween = allHallowsEve;
```

### `technical-atom-63c4747e42cd9d55` code

Citation: (raw/javascriptallonge.pdf p.141-147)

```javascript
const allHallowsEve = [2012, 10, 31]; ( function (halloween) { // ...
```

### `technical-atom-9cd3cad3711aee38` code

Citation: (raw/javascriptallonge.pdf p.141-147)

```
- })(allHallowsEve);
```

### `technical-atom-9c50c7f59d774858` code

Citation: (raw/javascriptallonge.pdf p.141-147)

```javascript
const allHallowsEve = [2012, 10, 31]; ( function (halloween) { halloween = [2013, 10, 31];
```

### `technical-atom-651b5211e2b3dca5` code

Citation: (raw/javascriptallonge.pdf p.141-147)

```javascript
})(allHallowsEve); allHallowsEve //=> [2012, 10, 31]
```

## Related technical details

### From [[javascriptallonge-self-similarity]]: `technical-atom-940ab647a8cf16dd` code

Relation: nearby source page; matched terms `arrays`, `code`, `does`, `not`, `value`

Citation: (raw/javascriptallonge.pdf p.109-116)

```javascript
> 61 Well, actually, this does not work for arrays that contain undefined as a value, but we are not going to see that in our examples. A more robust implementation would be (array) => array.length === 0, but we are doing backflips to keep this within a very small and contrived playground.
```

### From [[javascriptallonge-garbage-garbage-everywhere]]: `technical-atom-4551df707589c382` exception

Relation: nearby source page; matched terms `arrays`, `does`, `not`, `one`

Citation: (raw/javascriptallonge.pdf p.126-131)

Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another.

### From [[javascriptallonge-plain-old-javascript-objects]]: `technical-atom-aae330c293cc2f83` code

Relation: nearby source page; matched terms `code`, `const`, `javascript`, `name`, `objects`

Citation: (raw/javascriptallonge.pdf p.132-140)

```javascript
const NAME = 0, FIRST = 0, LAST = 1, OCCUPATION = 1, TITLE = 0, RESPONSIBILITIES = 1;
```

### From [[javascriptallonge-copy-on-write]]: `technical-atom-0fe1e1432a76a661` code

Relation: nearby source page; matched terms `code`, `const`, `copy`, `list`, `value`

Citation: (raw/javascriptallonge.pdf p.158-163)

```javascript
const copy = (node, head = null, tail = null) => { if (node === EMPTY) { return head; } else if (tail === null) { const { first, rest } = node; const newNode = { first, rest }; return copy(rest, newNode, newNode); } else { const { first, rest } = node; const newNode = { first, rest }; tail.rest = newNode; return copy(node.rest, head, newNode); } } const first = ({first, rest}) => first; const rest = ({first, rest}) => rest; const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed: reverse(rest(node), { first: first(node), rest: delayed }); const mapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? reverse(delayed): mapWith(fn, rest(node), { first: fn(first(node)), rest: delayed }); const at = (index, list) => index === 0 ? first(list): at(index - 1, rest(list)); const set = (index, value, list, originalList = list) => index === 0 ? (list.first = value, originalList): set(index - 1, value, rest(list), originalList) const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY } }};
```
