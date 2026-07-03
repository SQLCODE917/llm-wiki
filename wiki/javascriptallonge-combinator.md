---
page_id: javascriptallonge-combinator
page_kind: concept
page_family: topic-concept
summary: Combinator: 5 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-combinator@b7589521a2553b9244bcf891653c4e54
---

# Combinator

What [[javascriptallonge]] covers about combinator:

## Statements

### And also: / Combinators and Function Decorators / combinators

- In this book, we will be using a looser definition of 'combinator:' Higher-order pure functions that take only functions as arguments and return a function. We won't be strict about using only previously defined combinators in their construction. _(javascriptallonge.pdf (source-range-7239e085-00563))_

- This is, of course, just one example of many. You'll find lots more perusing the recipes in this book. While some programmers believe 'There Should Only Be One Way To Do It,' having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-7239e085-00566))_

### And also: / Combinators and Function Decorators / a balanced statement about combinators

- Code that uses a lot of combinators tends to name the verbs and adverbs (like doubleOf , addOne , and compose ) while avoiding language keywords and the names of nouns (like number ). So one perspective is that combinators are useful when you want to emphasize what you're doing and how it fits together, and more explicit code is useful when you want to emphasize what you're working with. _(javascriptallonge.pdf (source-range-7239e085-00568))_

### And also: / Combinators and Function Decorators / function decorators

- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-7239e085-00578))_


## Technical atoms

### Technical frame 1: And also: / Combinators and Function Decorators / combinators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00566))_

> This is, of course, just one example of many. You'll find lots more perusing the recipes in this book. While some programmers believe 'There Should Only Be One Way To Do It,' having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00565))_

<a id="atom-technical-atom-ae943e3fb41896af"></a>

```
const compose = (a, b) =>
(c) => a(b(c))
Let’s say we have:
const addOne = (number) => number + 1;
const doubleOf = (number) => number * 2;
With compose, anywhere you would write
const doubleOfAddOne = (number) => doubleOf(addOne(number));
You could also write:
const doubleOfAddOne = compose(doubleOf, addOne);
```

### Technical frame 2: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00578))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00577))_

<a id="atom-technical-atom-16403f5e9983b595"></a>

```
const nothing = not(something);
```


## Related pages

### Source structure

- [[javascriptallonge-section-and-also-combinators-and-function-decorators-combinators-7988daff]] - source section: And also: / Combinators and Function Decorators / combinators shares source evidence from And also: / Combinators and Function Decorators / combinators: In this book, we will be using a looser definition of 'combinator:' Higher-order pure functions that take only functions as arguments and return a function. We won't ... [truncated]; And also: / Combinators and Function Decorators / combinators shares technical record from And also: / Combinators and Function Decorators / combinators: combinators The word 'combinator' has a precise technical meaning in mathematics: 'A combinator is a higher-order function that uses only function application and ea ... [truncated] (3 shared statement(s), 3 shared atom(s))

### Shared technical atoms

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from And also: / Combinators and Function Decorators / function decorators: not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorator ... [truncated]; Function shares technical record from And also: / Combinators and Function Decorators / function decorators: const nothing = not(something); (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-function-decorator]] - shared statements and technical atoms: Function Decorator shares source evidence from And also: / Combinators and Function Decorators / function decorators: not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorator ... [truncated]; Function Decorator shares technical record from And also: / Combinators and Function Decorators / function decorators: const nothing = not(something); (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-programmer]] - shared statements and technical atoms: Programmer shares source evidence from And also: / Combinators and Function Decorators / combinators: This is, of course, just one example of many. You'll find lots more perusing the recipes in this book. While some programmers believe 'There Should Only Be One Way T ... [truncated]; Programmer shares technical record from And also: / Combinators and Function Decorators / combinators: const compose = (a, b) => (c) => a(b(c)) Let’s say we have: const addOne = (number) => number + 1; const doubleOf = (number) => number * 2; With compose, anywhere yo ... [truncated] (1 shared statement(s), 1 shared atom(s))

### Shared claims

- [[javascriptallonge-code]] - shared statements: Code shares source evidence from And also: / Combinators and Function Decorators / a balanced statement about combinators: Code that uses a lot of combinators tends to name the verbs and adverbs (like doubleOf , addOne , and compose ) while avoiding language keywords and the names of nou ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
