---
page_id: javascriptallonge-write
page_kind: concept
summary: Write: 7 statement(s) and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-write@1736a35c7402f3458bea6f063115080c
---

# Write

What [[javascriptallonge]] covers about write:

## Statements

### void

- 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

### const

- Another way to write our 'circumference' function would be to pass PI along with the diameter argument, something like this: _(javascriptallonge.pdf (source-range-31a4cf47-00418))_

### copy-on-write

- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.Wikipedia 73 _(javascriptallonge.pdf (source-range-31a4cf47-01253))_

- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-31a4cf47-01255))_

### a look back at functional iterators

- If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-31a4cf47-01543))_

### iterables

- So, when a standard way to write iterators was added to the JavaScript language, it didn't make sense to use a method like .iterator() for it: That would conflict with existing code. Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator. _(javascriptallonge.pdf (source-range-31a4cf47-01555))_

### We'll keep it simple:

- Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. _(javascriptallonge.pdf (source-range-31a4cf47-01659))_


## Technical atoms

### Technical frame 1: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00250))_

```
(() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined
```

### Technical frame 2: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00251))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical frame 3: const

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00422))_

> This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00419))_

```
(diameter, PI) => diameter * PI
```

### Technical frame 4: const

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00433))_

> We can bind any expression. Functions are expressions, so we can bind helper functions:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00432))_

```
((diameter) => { const PI = 3.14159265; return diameter * PI })(2) //=> 6.2831853
```

### Technical frame 5: a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01543))_

> If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01542))_

```
const collectionSum = (collection) => { const iterator = collection.iterator(); let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } return sum } collectionSum(stack) //=> 6
```

### Technical atom 6

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00659))_

| entry | content |
| --- | --- |
| 45 | from Michael Fogus, Functional JavaScript |
| 46 | from Oliver Steele and the terse but handy node-ap |
| 47 | from James Halliday. |

<details>
<summary>Raw table text</summary>

```
Partial Application
In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libraries provide some form of partial application. You'll find examples in Lemonad 45 from Michael Fogus, Functional JavaScript 46 from Oliver Steele and the terse but handy node-ap 47 from James Halliday.
```

</details>


## Related pages

- [[javascriptallonge-copy-write]] - narrower topic: Copy on Write shares source evidence from copy-on-write: Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) c ... [truncated] (2 shared statement(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from const: Another way to write our 'circumference' function would be to pass PI along with the diameter argument, something like this:; Function shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Javascript shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-code]] - shared statements and technical atoms: Code shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Code shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-program]] - shared statements and technical atoms: Program shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Program shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-follow]] - shared statements and technical atoms: Follow shares source evidence from copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated]; Follow shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-language]] - shared statements and technical atoms: Language shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Language shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-programmer]] - shared statements and technical atoms: Programmer shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Programmer shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-functional-iterator]] - shared statements and technical atoms: Functional Iterators shares source evidence from a look back at functional iterators: If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an ... [truncated]; Functional Iterators shares technical record from a look back at functional iterators: const collectionSum = (collection) => { const iterator = collection.iterator(); let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-feature]] - shared technical atoms: Feature shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared atom(s))
- [[javascriptallonge-rule]] - shared technical atoms: Rule shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared atom(s))
- [[javascriptallonge-block]] - shared technical atoms: Block shares technical table: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (1 shared atom(s))
- [[javascriptallonge-evaluating]] - shared technical atoms: Evaluating shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-functional]] - shared technical atoms: Functional shares technical table: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (1 shared atom(s))
- [[javascriptallonge-recipe]] - shared technical atoms: Recipe shares technical table: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (1 shared atom(s))
- [[javascriptallonge-result]] - shared technical atoms: Result shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from copy-on-write: Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) c ... [truncated] (2 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements: Iterator shares source evidence from iterables: So, when a standard way to write iterators was added to the JavaScript language, it didn't make sense to use a method like .iterator() for it: That would conflict wi ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
