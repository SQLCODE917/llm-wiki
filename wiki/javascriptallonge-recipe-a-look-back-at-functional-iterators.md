---
page_id: javascriptallonge-recipe-a-look-back-at-functional-iterators
page_kind: recipe
page_family: recipe-pattern
summary: a look back at functional iterators: reusable source-backed pattern with 4 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: a-look-back-at-functional-iterators
projection_coverage: recipe-javascriptallonge-recipe-a-look-back-at-functional-iterators@dcd4c973fa5395dd49d419d96fa15dbd
---

# a look back at functional iterators

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-a-look-back-at-functional-iterators-4c177971]].
- Evidence roles: decision, constraint, procedure, example.

## Applicability And Rationale

- We can do the same thing for objects. _(javascriptallonge.pdf (source-range-7239e085-01532))_
- We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method: _(javascriptallonge.pdf (source-range-7239e085-01541))_
- If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. _(javascriptallonge.pdf (source-range-7239e085-01543))_
- Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-7239e085-01543))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01533)_

```
const Stack1 = () =>
({
array:[],
index: -1,
push (value) {
return this.array[this.index += 1] = value;
},
pop () {
const value = this.array[this.index];
this.array[this.index] = undefined;
if (this.index >= 0) {
this.index -= 1
}
return value
},
isEmpty () {
return this.index < 0
},
iterator () {
let iterationIndex = this.index;
return () => {
if (iterationIndex > this.index) {
iterationIndex = this.index;
}
if (iterationIndex < 0) {
return {done: true};
}
else {
return {done: false, value: this.array[iterationIndex--]}
}
}
}
});
const stack = Stack1();
stack.push("Greetings");
stack.push("to");
stack.push("you!")
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01534)_

```
const iter = stack.iterator();
iter().value
//=> "you!"
iter().value
//=> "to"
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01536)_

```
The .iterator() method is defined with shorthand equivalent to iterator: function iterator()
{ ... }. Note that it uses the function keyword, so when we invoke it with stack.iterator(),
JavaScript sets this to the value of stack. But what about the function .iterator() returns? It is
defined with a fat arrow () => { ... }. What is the value of this within that function?
Since JavaScript doesn’t bind this within a fat arrow function, we follow the same rules of variable
scoping as any other variable name: We check in the environment enclosing the function. Although
the .iterator() method has returned, its environment is the one that encloses our () => { ...
} function, and that’s where this is bound to the value of stack.
Therefore, the iterator function returned by the .iterator() method has this bound to the stack
object, even though we call it with iter().
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01538)_

```
const iteratorSum = (iterator) => {
let eachIteration,
sum = 0;
while ((eachIteration = iterator(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01540)_

```
const stack = Stack1();
stack.push(1);
stack.push(2);
stack.push(3);
iteratorSum(stack.iterator())
//=> 6
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01542)_

```
const collectionSum = (collection) => {
const iterator = collection.iterator();
let eachIteration,
sum = 0;
while ((eachIteration = iterator(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
collectionSum(stack)
//=> 6
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-a-look-back-at-functional-iterators-4c177971]]
