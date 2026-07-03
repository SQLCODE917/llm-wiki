---
page_id: javascriptallonge-pattern
page_kind: concept
page_family: broad-topic
summary: Pattern: 8 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-pattern@124c53c7090f2f63fe662794b7ebd57a
---

# Pattern

What [[javascriptallonge]] covers about pattern:


## Related pages

### Shared technical atoms

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated]; Function shares technical record from And also: / That Constant Coffee Craving / inside-out: (diameter) => // ... (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-generator]] - shared statements and technical atoms: Generator shares source evidence from We'll keep it simple: / generators and iterables: This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:; Generator shares technical record from We'll keep it simple: / generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-recipe]] - shared statements and technical atoms: Recipe shares source evidence from Recipes with Basic Functions / Maybe: This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing:; Recipe shares technical record from Recipes with Basic Functions / Maybe: const isSomething = (value) => value !== null && value !== void 0; const checksForSomething = (value) => { if (isSomething(value)) { // function's true logic } } (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from And also: / That Constant Coffee Craving / inside-out: (diameter) => // ... (1 shared atom(s))
- [[javascriptallonge-iterable]] - shared technical atoms: Iterable shares technical record from We'll keep it simple: / generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared atom(s))
- [[javascriptallonge-iterator]] - shared technical atoms: Iterator shares technical record from We'll keep it simple: / generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from And also: / That Constant Coffee Craving / inside-out: (diameter) => // ... (1 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical record from We'll keep it simple: / generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared atom(s))

### Shared claims

- [[javascriptallonge-follow]] - shared statements: Follow shares source evidence from Composing and Decomposing Data / Mutation / mutation and data structures: One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists f ... [truncated] (2 shared statement(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-copy-write]] - shared statements: Copy on Write shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-mutation]] - shared statements: Mutation shares source evidence from Composing and Decomposing Data / Mutation / mutation and data structures: One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists f ... [truncated] (1 shared statement(s))
- [[javascriptallonge-needn]] - shared statements: Needn shares source evidence from And also: / Building Blocks: When you look at functions within functions in JavaScript, there's a bit of a 'spaghetti code' look to it. The strength of JavaScript is that you can do anything. Th ... [truncated] (1 shared statement(s))
- [[javascriptallonge-write]] - shared statements: Write shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
## Statements by source section

### And also: / That Constant Coffee Craving / inside-out

- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated 'IIFE.' _(javascriptallonge.pdf (source-range-7239e085-00404))_

### And also: / Building Blocks

- When you look at functions within functions in JavaScript, there's a bit of a 'spaghetti code' look to it. The strength of JavaScript is that you can do anything. The weakness is that you will. There are ifs, fors, returns, everything thrown higgledy piggledy together. Although you needn't restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks. _(javascriptallonge.pdf (source-range-7239e085-00580))_

### And also: / Building Blocks / composition

- If that was all there was to it, composition wouldn't matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways. _(javascriptallonge.pdf (source-range-7239e085-00586))_

### Recipes with Basic Functions / Maybe

- This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing: _(javascriptallonge.pdf (source-range-7239e085-00696))_

### Composing and Decomposing Data / Mutation / mutation and data structures

- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists from Plain Old JavaScript Objects. While we're executing the mapWith function, we're constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith . _(javascriptallonge.pdf (source-range-7239e085-01143))_

### Yes. Consider this variation: / Copy on Write / copy-on-write

- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-7239e085-01255))_

### Like this: / operations on ordered collections

- This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order. _(javascriptallonge.pdf (source-range-7239e085-01590))_

### We'll keep it simple: / generators and iterables

- This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects: _(javascriptallonge.pdf (source-range-7239e085-01712))_


## Technical atoms

### Technical frame 1: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00406))_

> Everything else is encapsulated in its body. That's how it should be, naming PI is its concern, not ours. The other formulation:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00405))_

<a id="atom-technical-atom-ddeb9767d36d61f0"></a>

```
(diameter) =>
// ...
```

### Technical frame 2: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00587))_

> In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00588))_

<a id="atom-technical-atom-036210fddaad3323"></a>

> Of course, you needn't use combinators to implement either of these ideas, you can use if statements.

### Technical frame 3: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00698))_

> Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00697))_

<a id="atom-technical-atom-0050ec8e3fdf9f53"></a>

```
const isSomething = (value) =>
value !== null && value !== void 0;
const checksForSomething = (value) => {
if (isSomething(value)) {
// function's true logic
}
}
```

### Technical frame 4: We'll keep it simple: / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01714))_

> This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01713))_

<a id="atom-technical-atom-08b3d4cd0486cddf"></a>

```
const ThreeNumbers = {
*[Symbol.iterator] () {
yield 1;
yield 2;
yield 3
}
}
```


## Source

- [[javascriptallonge]]
