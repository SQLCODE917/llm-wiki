---
page_id: javascriptallonge-plain-old-javascript-objects
page_kind: source
summary: Plain Old JavaScript Objects from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.132-140
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

JavaScript objects are maps from string keys to values, and they use literal syntax for creation. This chapter covers object composition, decomposition, destructuring, and linked lists using objects.

## Key supported claims

- JavaScript objects are maps from string keys to values, using literal syntax for creation (raw/javascriptallonge.pdf p.132-140).
- Objects can store key-value pairs and access values by name using bracket notation (raw/javascriptallonge.pdf p.132-140).
- JavaScript objects support various syntaxes for property access, including bracket notation and dot notation (raw/javascriptallonge.pdf p.132-140).
- Objects can contain functions and other data structures, and use compact method syntax for named function expressions (raw/javascriptallonge.pdf p.132-140).
- Destructuring assignments can be used with objects to extract values (raw/javascriptallonge.pdf p.132-140).

## Technical details

### `technical-atom-31274c701c75c742` code

Citation: (raw/javascriptallonge.pdf p.132-140)

```javascript
const remember = ["the milk", "the coffee beans", "the biscotti"];
```

### `technical-atom-d6ba7e5f33c9f02b` code

Citation: (raw/javascriptallonge.pdf p.132-140)

```javascript
const user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja vaScript Spessore", "CoffeeScript Ristretto"]]];
```

### `technical-atom-aae330c293cc2f83` code

Citation: (raw/javascriptallonge.pdf p.132-140)

```javascript
const NAME = 0, FIRST = 0, LAST = 1, OCCUPATION = 1, TITLE = 0, RESPONSIBILITIES = 1;
```

### `technical-atom-c42523bb272ff848` code

Citation: (raw/javascriptallonge.pdf p.132-140)

```
- { year: 2012, month: 6, day: 14 }
```

### `technical-atom-63b7015f42c45b72` code

Citation: (raw/javascriptallonge.pdf p.132-140)

```javascript
- { year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 } //=> false
```

### `technical-atom-daba175ac6c4caee` code

Citation: (raw/javascriptallonge.pdf p.132-140)

```javascript
- { year: 2012, month: 6, day: 14 }['day'] //=> 14
```

### `technical-atom-fe9470f7a0484918` code

Citation: (raw/javascriptallonge.pdf p.132-140)

```javascript
const unique = () => [],
```

### `technical-atom-912fef7389f54f60` code

Citation: (raw/javascriptallonge.pdf p.132-140)

```
- z = unique(), o = { a: x, b: y, c: z };
```

## Related technical details

### From [[javascriptallonge-tail-calls-and-default-arguments]]: `technical-atom-b4bbdc6766be3fad` code

Relation: nearby source page; matched terms `can`, `function`, `javascript`, `they`

Citation: (raw/javascriptallonge.pdf p.117-125)

```javascript
There are three places it returns. The first two don’t return anything, they don’t matter. But the third is fn.apply(this, args). This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments (this, args), JavaScript can throw away everything in its current stack frame. It isn’t going to do any more work, so it can throw its existing stack frame away.
```
