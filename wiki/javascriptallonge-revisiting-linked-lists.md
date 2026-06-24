---
page_id: javascriptallonge-revisiting-linked-lists
page_kind: source
summary: revisiting linked lists from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.137-140
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on revisiting linked lists in JavaScript Allongé, focusing on list traversal, mapping, and performance.

## Key supported claims

- Linked lists can be implemented using objects with `first` and `rest` properties, as opposed to two-element arrays. (raw/javascriptallonge.pdf p.137-140)
- The performance of list operations depends on how they are implemented; for example, mapping over a list can be done in a way that requires iterating twice, leading to higher time and memory complexity. (raw/javascriptallonge.pdf p.137-140)
- The `reverse` function is used to reverse a list, which is necessary for correctly mapping over lists when the implementation iterates in reverse. (raw/javascriptallonge.pdf p.137-140)

## Technical details

### `technical-atom-e7aa6f3f69b944ac` code

Citation: (raw/javascriptallonge.pdf p.137-140)

```javascript
const cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;
```

### `technical-atom-d944f4a4388f022e` code

Citation: (raw/javascriptallonge.pdf p.137-140)

```
In that case, a linked list of the numbers 1 , 2 , and 3 will look like this: { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY } } } . We can then perform the equivalent of [first, ...rest] with direct property accessors:
```

### `technical-atom-98e27802789dc8da` code

Citation: (raw/javascriptallonge.pdf p.137-140)

```javascript
const EMPTY = {}; const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } }; OneTwoThree.first //=> 1 OneTwoThree.rest //=> {"first":2,"rest":{"first":3,"rest":{}}} OneTwoThree.rest.rest.first //=> 3 Taking the length of a linked list is easy: const length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1); length(OneTwoThree) //=> 3
```

### `technical-atom-f58f9106e0f75fc7` code

Citation: (raw/javascriptallonge.pdf p.137-140)

```javascript
const slowcopy = (node) => node === EMPTY ? EMPTY : { first: node.first, rest: slowcopy(node.rest)}; slowcopy(OneTwoThree) //=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{}}}}
```

### `technical-atom-6312b62d26a49e8e` code

Citation: (raw/javascriptallonge.pdf p.137-140)

```javascript
const copy2 = (node, delayed = EMPTY) => node === EMPTY ? delayed : copy2(node.rest, { first: node.first, rest: delayed }); copy2(OneTwoThree) //=> {"first":3,"rest":{"first":2,"rest":{"first":1,"rest":{}}}}
```

### `technical-atom-cc1c838438cd5fc7` code

Citation: (raw/javascriptallonge.pdf p.137-140)

```javascript
const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); And now, we can make a reversing map: const reverseMapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? delayed : reverseMapWith(fn, node.rest, { first: fn(node.first), rest: delayed }); reverseMapWith((x) => x * x, OneTwoThree) //=> {"first":9,"rest":{"first":4,"rest":{"first":1,"rest":{}}}} And a regular mapWith follows: const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); const mapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? reverse(delayed) : mapWith(fn, node.rest, { first: fn(node.first), rest: delayed }); mapWith((x) => x * x, OneTwoThree) //=> {"first":1,"rest":{"first":4,"rest":{"first":9,"rest":{}}}}
```

### `technical-atom-fab4324cdd6577a6` code

Citation: (raw/javascriptallonge.pdf p.137-140)

```
So our linked list nodes will be formed from { first, rest }
```

### `technical-atom-756042e76abd0569` procedure

Citation: (raw/javascriptallonge.pdf p.137-140)

So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return.

## Related technical details

### From [[javascriptallonge-mutation-and-data-structures]]: `technical-atom-6fbbc51a9f84f2a8` code

Relation: nearby source page; matched terms `first`, `linked`, `lists`, `makes`, `rest`, `they`

Citation: (raw/javascriptallonge.pdf p.143-145)

```javascript
const EMPTY = {}; const OneToFive = { first: 1, rest: { first: 2, rest: { first: 3, rest: { first: 4, rest: { first: 5, rest: EMPTY } } } } }; OneToFive //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\ r","rest":{"first":"five","rest":{}}}}}} const ThreeToFive = OneToFive.rest.rest; ThreeToFive //=> {"first":3,"rest":{"first":4,"rest":{"first":5,"rest":{}}}} ThreeToFive.first = "three"; ThreeToFive.rest.first = "four"; ThreeToFive.rest.rest.first = "five"; ThreeToFive //=> {"first":"three","rest":{"first":"four","rest":{"first":"five","rest":{}}\ }} OneToFive //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\ r","rest":{"first":"five","rest":{}}}}}} Changes made to ThreeToFive affect OneToFive , because they share the same structure. When we wrote ThreeToFive = OneToFive.rest.rest; , we weren't making a brand new copy of {"first":3,"rest":{"fir we were getting a reference to the same chain of nodes. Structure sharing like this is what makes linked lists so fast for taking everything but the first item
```

### From [[javascriptallonge-destructuring-objects]]: `technical-atom-2fa843b604012360` code

Relation: nearby source page; matched terms `allong`, `can`, `first`, `javascript`, `objects`

Citation: (raw/javascriptallonge.pdf p.136-137)

```javascript
const user = { name: { first: "Reginald", last: "Braithwaite" }, occupation: { title: "Author", responsibilities: [ "JavaScript Allongé", "JavaScript Spessore", "CoffeeScript Ristretto" ] } }; user.name.last //=> "Braithwaite" user.occupation.title //=> "Author" And we can also write: const {name: { first: given, last: surname}, occupation: { title: title } er; surname //=> "Braithwaite" title //=> "Author"
```

### From [[javascriptallonge-mutation]]: `technical-atom-d501bc9f53f216ef` code

Relation: nearby source page; matched terms `first`, `rest`, `reverse`

Citation: (raw/javascriptallonge.pdf p.145-147)

```javascript
const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); const copy = (node) => reverse(reverse(node));
```

### From [[javascriptallonge-plain-old-javascript-objects]]: `technical-atom-08c736021f08b986` code

Relation: nearby source page; matched terms `allong`, `first`, `javascript`, `objects`

Citation: (raw/javascriptallonge.pdf p.132)

```javascript
const NAME = 0, FIRST = 0, LAST = 1, OCCUPATION = 1, TITLE = 0, RESPONSIBILITIES = 1; const user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\ vaScript Spessore", "CoffeeScript Ristretto"]]];
```
