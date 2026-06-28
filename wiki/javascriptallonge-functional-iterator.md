---
page_id: javascriptallonge-functional-iterator
page_kind: concept
summary: Functional Iterators: 14 statement(s) and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-functional-iterator@9ca13242f580112730fadadb3085e046
---

# Functional Iterators

What [[javascriptallonge]] covers about functional iterators:

## Statements

### Functional Iterators

- The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays. _(javascriptallonge.pdf (source-range-31a4cf47-01276))_

- Well, we call arraySum with an array, and it has baked into it a method for traversing the array. Perhaps we could extract both of those things. Let's rearrange our code a bit: _(javascriptallonge.pdf (source-range-31a4cf47-01278))_

- What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable. _(javascriptallonge.pdf (source-range-31a4cf47-01280))_

### a look back at functional iterators

- When discussing functions, we looked at the benefits of writing Functional Iterators. We can do the same thing for objects. Here's a stack that has its own functional iterator method: _(javascriptallonge.pdf (source-range-31a4cf47-01532))_

- We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method: _(javascriptallonge.pdf (source-range-31a4cf47-01541))_

- If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-31a4cf47-01543))_

### Like this:

- Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object's scaffolding. _(javascriptallonge.pdf (source-range-31a4cf47-01552))_

### iterables

- People have been writing iterators since JavaScript was first released in the late 1990s. Since there was no particular standard way to do it, people used all sorts of methods, and their methods returned all sorts of things: Objects with various interfaces, functional iterators, you name it. _(javascriptallonge.pdf (source-range-31a4cf47-01554))_

### summary

- Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-31a4cf47-01621))_

### Generating Iterables

- Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done. _(javascriptallonge.pdf (source-range-31a4cf47-01626))_

### state machines

- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 : _(javascriptallonge.pdf (source-range-31a4cf47-01654))_


## Technical atoms

### Technical frame 1: Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01276))_

> The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01273))_

```
const arraySum = ([first, ...rest], accumulator = 0) => first === undefined ? accumulator : arraySum(rest, first + accumulator) arraySum([1, 4, 9, 16, 25]) //=> 55
```

### Technical frame 2: Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01276))_

> The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01275))_

```
const callLeft = (fn, ...args) => (...remainingArgs) => fn(...args, ...remainingArgs); const foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === undefined ? terminalValue : fn(first, foldArrayWith(fn, terminalValue, rest)); const arraySum = callLeft(foldArrayWith, (a, b) => a + b, 0); arraySum([1, 4, 9, 16, 25]) //=> 55
```

### Technical frame 3: Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01280))_

> What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01279))_

```
const callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); const foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === undefined ? terminalValue : fn(first, foldArrayWith(fn, terminalValue, rest)); const foldArray = (array) => callRight(foldArrayWith, array); const sumFoldable = (folder) => folder((a, b) => a + b, 0); sumFoldable(foldArray([1, 4, 9, 16, 25])) //=> 55
```

### Technical frame 4: Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01283))_

> We've found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we've completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really).

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01282))_

```
const callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); const foldTreeWith = (fn, terminalValue, [first, ...rest]) => first === undefined ? terminalValue : Array.isArray(first) ? fn(foldTreeWith(fn, terminalValue, first), foldTreeWith(fn, terminalValu\ e, rest)) : fn(first, foldTreeWith(fn, terminalValue, rest)); const foldTree = (tree) => callRight(foldTreeWith, tree); const sumFoldable = (folder) => folder((a, b) => a + b, 0); sumFoldable(foldTree([1, [4, [9, 16]], 25])) //=> 55
```

### Technical frame 5: a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01533))_

```
const Stack1 = () => ({ array:[], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this .array[ this .index] = undefined ; if ( this .index >= 0) { this .index -= 1 } return value }, isEmpty () { return this .index < 0 }, iterator () { let iterationIndex = this .index; return () => { if (iterationIndex > this .index) { iterationIndex = this .index; } if (iterationIndex < 0) { return {done: true }; } else { return {done: false , value: this .array[iterationIndex--]} } } } }); const stack = Stack1(); stack.push("Greetings"); stack.push("to"); stack.push("you!")
```

### Technical frame 6: a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01534))_

```
const iter = stack.iterator(); iter().value //=> "you!" iter().value //=> "to"
```

### Technical frame 7: a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01536))_

```
The .iterator() method is defined with shorthand equivalent to iterator: function iterator() { ... } . Note that it uses the function keyword, so when we invoke it with stack.iterator() , JavaScript sets this to the value of stack . But what about the function .iterator() returns? It is defined with a fat arrow () => { ... } . What is the value of this within that function? Since JavaScript doesn't bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. Although the .iterator() method has returned, its environment is the one that encloses our () => { ... } function, and that's where this is bound to the value of stack . Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter() .
```

### Technical frame 8: a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01538))_

```
const iteratorSum = (iterator) => { let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } return sum }
```

### Technical frame 9: a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01540))_

```
const stack = Stack1(); stack.push(1); stack.push(2); stack.push(3); iteratorSum(stack.iterator()) //=> 6
```

### Technical frame 10: a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01543))_

> If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01542))_

```
const collectionSum = (collection) => { const iterator = collection.iterator(); let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } return sum } collectionSum(stack) //=> 6
```


## Related pages

- [[javascriptallonge-iterator]] - broader topic: Iterator shares source evidence from summary: Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility ... [truncated] (3 shared statement(s))
- [[javascriptallonge-functional]] - broader topic: Functional shares source evidence from summary: Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility ... [truncated] (2 shared statement(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated]; Function shares technical record from a look back at functional iterators: const Stack1 = () => ({ array:[], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (4 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-array]] - shared statements and technical atoms: Array shares source evidence from Functional Iterators: Well, we call arraySum with an array, and it has baked into it a method for traversing the array. Perhaps we could extract both of those things. Let's rearrange our code a bit:; Array shares technical record from Functional Iterators: const arraySum = ([first, ...rest], accumulator = 0) => first === undefined ? accumulator : arraySum(rest, first + accumulator) arraySum([1, 4, 9, 16, 25]) //=> 55 (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-write]] - shared statements and technical atoms: Write shares source evidence from a look back at functional iterators: If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an ... [truncated]; Write shares technical record from a look back at functional iterators: const collectionSum = (collection) => { const iterator = collection.iterator(); let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-data]] - shared statements: Data shares source evidence from Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated] (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from summary: Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility ... [truncated] (1 shared statement(s))
- [[javascriptallonge-language]] - shared statements: Language shares source evidence from summary: Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility ... [truncated] (1 shared statement(s))
- [[javascriptallonge-method]] - shared statements: Method shares source evidence from Generating Iterables: Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly unt ... [truncated] (1 shared statement(s))
- [[javascriptallonge-object]] - shared statements: Object shares source evidence from Generating Iterables: Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly unt ... [truncated] (1 shared statement(s))
- [[javascriptallonge-program]] - shared statements: Program shares source evidence from a look back at functional iterators: If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an ... [truncated] (1 shared statement(s))
- [[javascriptallonge-section-functional-iterators-8ba98332]] - source section: Functional Iterators shares source evidence from Functional Iterators: The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still re ... [truncated]; Functional Iterators shares technical record from Functional Iterators: const arraySum = ([first, ...rest], accumulator = 0) => first === undefined ? accumulator : arraySum(rest, first + accumulator) arraySum([1, 4, 9, 16, 25]) //=> 55 (5 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-section-a-look-back-at-functional-iterators-98eb8fd9]] - source section: a look back at functional iterators shares source evidence from a look back at functional iterators: When discussing functions, we looked at the benefits of writing Functional Iterators. We can do the same thing for objects. Here's a stack that has its own functiona ... [truncated]; a look back at functional iterators shares technical record from a look back at functional iterators: const Stack1 = () => ({ array:[], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (4 shared statement(s), 6 shared atom(s))

## Source

- [[javascriptallonge]]
