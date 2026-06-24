---
page_id: javascriptallonge-mutation-and-data-structures
page_kind: source
summary: mutation and data structures from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.143-145
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on mutation and data structures from JavaScript Allongé.

## Key supported claims

- Mutation is a surprisingly complex subject. (raw/javascriptallonge.pdf p.143-145)
- Languages like Haskell 70 don't permit mutation at all. (raw/javascriptallonge.pdf p.143-145)
- In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about. (raw/javascriptallonge.pdf p.143-145)
- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. (raw/javascriptallonge.pdf p.143-145)
- But after returning the new list, we then become conservative about mutation. (raw/javascriptallonge.pdf p.143-145)

## Technical details

### `technical-atom-6fbbc51a9f84f2a8` code

Citation: (raw/javascriptallonge.pdf p.143-145)

```javascript
const EMPTY = {}; const OneToFive = { first: 1, rest: { first: 2, rest: { first: 3, rest: { first: 4, rest: { first: 5, rest: EMPTY } } } } }; OneToFive //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\ r","rest":{"first":"five","rest":{}}}}}} const ThreeToFive = OneToFive.rest.rest; ThreeToFive //=> {"first":3,"rest":{"first":4,"rest":{"first":5,"rest":{}}}} ThreeToFive.first = "three"; ThreeToFive.rest.first = "four"; ThreeToFive.rest.rest.first = "five"; ThreeToFive //=> {"first":"three","rest":{"first":"four","rest":{"first":"five","rest":{}}\ }} OneToFive //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\ r","rest":{"first":"five","rest":{}}}}}} Changes made to ThreeToFive affect OneToFive , because they share the same structure. When we wrote ThreeToFive = OneToFive.rest.rest; , we weren't making a brand new copy of {"first":3,"rest":{"fir we were getting a reference to the same chain of nodes. Structure sharing like this is what makes linked lists so fast for taking everything but the first item
```

### `technical-atom-d51c46e57b560a61` code

Citation: (raw/javascriptallonge.pdf p.143-145)

```javascript
const OneToFive = [1, 2, 3, 4, 5]; ...ThreeToFive] = OneToFive;
```

### `technical-atom-bf85b2f747efec06` code

Citation: (raw/javascriptallonge.pdf p.143-145)

```javascript
OneToFive //=> [1,2,3,4,5] const [a, b, ThreeToFive //=> [3, 4, 5] ThreeToFive[0] = "three"; ThreeToFive[1] = "four"; ThreeToFive[2] = "five"; ThreeToFive //=> ["three","four","five"] OneToFive //=> [1,2,3,4,5]
```

### `technical-atom-b7f80818a51816bb` formula

Citation: (raw/javascriptallonge.pdf p.143-145)

When we wrote ThreeToFive = OneToFive.rest.rest; , we weren't making a brand new copy of {"first":3,"rest":{"fir we were getting a reference to the same chain of nodes.

### `technical-atom-716ed5f15b0b87c8` procedure

Citation: (raw/javascriptallonge.pdf p.143-145)

But after returning the new list, we then become conservative about mutation.

### `technical-atom-696e87e5d432d18d` procedure

Citation: (raw/javascriptallonge.pdf p.143-145)

Whereas destructuring an array with [first, ...rest] does make a copy, so:

### `technical-atom-ffd604b20459277c` exception

Citation: (raw/javascriptallonge.pdf p.143-145)

It is possible to compute anything without ever mutating an existing entity.

## Related technical details

### From [[javascriptallonge-destructuring-objects]]: `technical-atom-2fa843b604012360` code

Relation: nearby source page; matched terms `allong`, `javascript`, `write`

Citation: (raw/javascriptallonge.pdf p.136-137)

```javascript
const user = { name: { first: "Reginald", last: "Braithwaite" }, occupation: { title: "Author", responsibilities: [ "JavaScript Allongé", "JavaScript Spessore", "CoffeeScript Ristretto" ] } }; user.name.last //=> "Braithwaite" user.occupation.title //=> "Author" And we can also write: const {name: { first: given, last: surname}, occupation: { title: title } er; surname //=> "Braithwaite" title //=> "Author"
```

### From [[javascriptallonge-revisiting-linked-lists]]: `technical-atom-756042e76abd0569` procedure

Relation: nearby source page; matched terms `all`, `list`, `procedure`, `then`

Citation: (raw/javascriptallonge.pdf p.137-140)

So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return.

### From [[javascriptallonge-revisiting-linked-lists]]: `technical-atom-d944f4a4388f022e` code

Relation: nearby source page; matched terms `like`, `list`, `then`

Citation: (raw/javascriptallonge.pdf p.137-140)

```
In that case, a linked list of the numbers 1 , 2 , and 3 will look like this: { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY } } } . We can then perform the equivalent of [first, ...rest] with direct property accessors:
```

### From [[javascriptallonge-var]]: `technical-atom-9598b23ff904732b` code

Relation: nearby source page; matched terms `but`, `function`, `javascript`

Citation: (raw/javascriptallonge.pdf p.151-154)

```javascript
const factorial = (n) => { let innerFactorial = function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } return innerFactorial(n, 1); } JavaScript hoists the let and the assignment. But not so with var : const factorial = (n) => { return innerFactorial(n, 1); var innerFactorial = function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } factorial(4) //=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```
