---
page_id: javascriptallonge-iteration
page_kind: concept
page_family: topic-concept
summary: Iteration: 2 statement(s) and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-iteration@eec2fb21f754c7c2edf4cf19f454971b
---

# Iteration

What [[javascriptallonge]] covers about iteration:

## Statements

### Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

- If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-7239e085-01543))_

### Served by the Pot: Collections / Iteration and Iterables / iterator objects

- Iteration for functions and objects has been around for many, many decades. For simple linear collections like arrays, linked lists, stacks, and queues, functional iterators are the simplest and easiest way to implement iterators. _(javascriptallonge.pdf (source-range-7239e085-01546))_


## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01533))_

<a id="atom-technical-atom-0494f9669763f688"></a>

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

### Technical frame 2: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01534))_

<a id="atom-technical-atom-977c2f6172e80243"></a>

```
const iter = stack.iterator();
iter().value
//=> "you!"
iter().value
//=> "to"
```

### Technical frame 3: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01536))_

<a id="atom-technical-atom-637c40b765d4fca9"></a>

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

### Technical frame 4: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01538))_

<a id="atom-technical-atom-ef867f51aa5d4e3b"></a>

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

### Technical frame 5: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01540))_

<a id="atom-technical-atom-59a4e3c6819adddb"></a>

```
const stack = Stack1();
stack.push(1);
stack.push(2);
stack.push(3);
iteratorSum(stack.iterator())
//=> 6
```

### Technical frame 6: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01543))_

> If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01542))_

<a id="atom-technical-atom-bc96f54b184676fd"></a>

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


## Related pages

### Shared technical atoms

- [[javascriptallonge-functional-iterator]] - shared statements and technical atoms: Functional Iterators shares source evidence from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an ... [truncated]; Functional Iterators shares technical record from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: const Stack1 = () => ({ array:[], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array[ ... [truncated] (1 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an ... [truncated]; Function shares technical record from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: const Stack1 = () => ({ array:[], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array[ ... [truncated] (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterator objects: Iteration for functions and objects has been around for many, many decades. For simple linear collections like arrays, linked lists, stacks, and queues, functional i ... [truncated]; Object shares technical record from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: const Stack1 = () => ({ array:[], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array[ ... [truncated] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms: Write shares technical record from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: const collectionSum = (collection) => { const iterator = collection.iterator(); let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
