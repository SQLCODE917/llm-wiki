---
page_id: javascriptallonge-alway
page_kind: concept
summary: Alway: 9 statement(s) and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-alway@70bcf767124d0c8e7727861e387b85a4
---

# Alway

What [[javascriptallonge]] covers about alway:

## Statements

### call by value

- We'll see below that while JavaScript always calls by value, the notion of a 'value' has additional subtlety. But before we do, let's look at variables. _(javascriptallonge.pdf (source-range-31a4cf47-00299))_

### if functions without free variables are pure, are closures impure?

- Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we've already seen: _(javascriptallonge.pdf (source-range-31a4cf47-00350))_

- Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x . _(javascriptallonge.pdf (source-range-31a4cf47-00355))_

### which came first, the chicken or the egg?

- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } . _(javascriptallonge.pdf (source-range-31a4cf47-00383))_

### the function keyword

- We always use a block, we cannot write function (str) str + str . This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-31a4cf47-00516))_

- arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this: _(javascriptallonge.pdf (source-range-31a4cf47-00613))_

### Functions

- function keyword functions always have blocks as their bodies. _(javascriptallonge.pdf (source-range-31a4cf47-00643))_

### truthiness and operators

- Our logical operators ! , && , and || are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-31a4cf47-00777))_

### Garbage, Garbage Everywhere

- 64 It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. But this is not how JavaScript's built-in arrays work. _(javascriptallonge.pdf (source-range-31a4cf47-01026))_


## Technical atoms

### Technical frame 1: if functions without free variables are pure, are closures impure?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00355))_

> Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00354))_

> If pure functions can contain closures, can a closure contain a pure function?

### Technical frame 2: which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00386))_

> The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} . As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00384))_

> If you don't want your code to operate directly within the global environment, what can you do?

### Technical frame 3: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00613))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00612))_

```
const args = function (a, b) { return arguments; } args(2,3) //=> { '0': 2, '1': 3 }
```

### Technical frame 4: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00618))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00615))_

```
const plus = function () { return arguments[0] + arguments[1]; } plus(2,3) //=> 5
```

### Technical frame 5: truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00779))_

> Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00778))_

```
!5 //=> false ! undefined //=> true
```


## Related pages

- [[javascriptallonge-argument]] - shared statements and technical atoms: Argument shares source evidence from the function keyword: arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:; Argument shares technical record from the function keyword: const args = function (a, b) { return arguments; } args(2,3) //=> { '0': 2, '1': 3 } (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-function-keyword]] - shared statements and technical atoms: the function keyword shares source evidence from the function keyword: We always use a block, we cannot write function (str) str + str . This means that if we want our functions to return a value, we always need to use the return keyword; the function keyword shares technical record from the function keyword: const args = function (a, b) { return arguments; } args(2,3) //=> { '0': 2, '1': 3 } (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from if functions without free variables are pure, are closures impure?: Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure fu ... [truncated]; Function shares technical record from if functions without free variables are pure, are closures impure?: If pure functions can contain closures, can a closure contain a pure function? (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from call by value: We'll see below that while JavaScript always calls by value, the notion of a 'value' has additional subtlety. But before we do, let's look at variables.; Javascript shares technical record from which came first, the chicken or the egg?: If you don't want your code to operate directly within the global environment, what can you do? (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from truthiness and operators: Our logical operators ! , && , and || are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, ... [truncated]; Return shares technical record from truthiness and operators: !5 //=> false ! undefined //=> true (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-behaviour]] - shared technical atoms: Behaviour shares technical record from truthiness and operators: !5 //=> false ! undefined //=> true (1 shared atom(s))
- [[javascriptallonge-program]] - shared technical atoms: Program shares technical record from truthiness and operators: !5 //=> false ! undefined //=> true (1 shared atom(s))
- [[javascriptallonge-programmer]] - shared technical atoms: Programmer shares technical record from truthiness and operators: !5 //=> false ! undefined //=> true (1 shared atom(s))
- [[javascriptallonge-needn]] - shared statements: Needn shares source evidence from Garbage, Garbage Everywhere: 64 It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share c ... [truncated] (1 shared statement(s))
- [[javascriptallonge-value]] - shared statements: Value shares source evidence from call by value: We'll see below that while JavaScript always calls by value, the notion of a 'value' has additional subtlety. But before we do, let's look at variables. (1 shared statement(s))

## Source

- [[javascriptallonge]]
