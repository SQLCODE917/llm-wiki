---
page_id: javascriptallonge-section-a-look-back-at-functional-iterators-c95ba37c
page_kind: source
summary: a look back at functional iterators: 10 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-look-back-at-functional-iterators-c95ba37c@c842a4b772024e3d628f1da795ba5855
---

# a look back at functional iterators

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-functional-iterator]] - topic hub: opens the topic page for Functional Iterator
- [[javascriptallonge-section-functional-iterators-17f67f36]] - same source heading: another source section with the same heading, Functional Iterators

## Statements

- When discussing functions, we looked at the benefits of writing Functional Iterators. We can do the same thing for objects. Here's a stack that has its own functional iterator method: _(javascriptallonge.pdf (source-range-8eb13d6b-01531))_
- We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method: _(javascriptallonge.pdf (source-range-8eb13d6b-01540))_
- If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-8eb13d6b-01542))_

## Technical atoms

### Technical frame 1: a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01540))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01532))_

```
const Stack1 = () => ({ array:[], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this .array[ this .index] = undefined ; if ( this .index >= 0) { this .index -= 1 } return value }, isEmpty () { return this .index < 0 }, iterator () { let iterationIndex = this .index; return () => { if (iterationIndex > this .index) { iterationIndex = this .index; } if (iterationIndex < 0) { return {done: true }; } else { return {done: false , value: this .array[iterationIndex--]} } } } }); const stack = Stack1(); stack.push("Greetings"); stack.push("to"); stack.push("you!")
```

### Technical frame 2: a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01540))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01533))_

```
const iter = stack.iterator(); iter().value //=> "you!" iter().value //=> "to"
```

### Technical frame 3: a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01540))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01535))_

```
The .iterator() method is defined with shorthand equivalent to iterator: function iterator() { ... } . Note that it uses the function keyword, so when we invoke it with stack.iterator() , JavaScript sets this to the value of stack . But what about the function .iterator() returns? It is defined with a fat arrow () => { ... } . What is the value of this within that function? Since JavaScript doesn't bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. Although the .iterator() method has returned, its environment is the one that encloses our () => { ... } function, and that's where this is bound to the value of stack . Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter() .
```

### Technical frame 4: a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01540))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01537))_

```
const iteratorSum = (iterator) => { let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } return sum }
```

### Technical frame 5: a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01540))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01539))_

```
const stack = Stack1(); stack.push(1); stack.push(2); stack.push(3); iteratorSum(stack.iterator()) //=> 6
```

### Technical frame 6: a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01542))_

> If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01541))_

```
const collectionSum = (collection) => { const iterator = collection.iterator(); let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } return sum } collectionSum(stack) //=> 6
```
