---
page_id: javascriptallonge-important
page_kind: concept
summary: Important: 5 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-important@370502db2f907250d80376ec81c54511
---

# Important

What [[javascriptallonge]] covers about important:

## Statements

### a quick summary of functions and bodies

- One of the important possible statements is a return statement. A return statement accepts any valid JavaScript expression. _(javascriptallonge.pdf (source-range-8eb13d6b-00291))_

### const

- JavaScript gives us a way to do that, the const keyword. We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const : _(javascriptallonge.pdf (source-range-8eb13d6b-00423))_

- Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as 'first class entities. ' Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth. _(javascriptallonge.pdf (source-range-8eb13d6b-00436))_

### partial application

- We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely: _(javascriptallonge.pdf (source-range-8eb13d6b-00600))_

### linear recursion

- Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions. _(javascriptallonge.pdf (source-range-8eb13d6b-00923))_


## Technical atoms

### Technical frame 1: const

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00425))_

> The const keyword introduces one or more bindings in the block that encloses it. It doesn't incur the cost of a function invocation. That's great. Even better, it puts the symbol (like PI ) close to the value ( 3.14159265 ). That's much better than what we were writing.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00424))_

```
(diameter) => { const PI = 3.14159265; return diameter * PI }
```

### Technical frame 2: partial application

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00604))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00602))_

```
const safeSquareAll = mapWith(maybe((n) => n * n));
```

### Technical frame 3: partial application

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00604))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00603))_

```
safeSquareAll([1, null , 2, 3]) //=> [1, null, 4, 9]
```


## Related pages

- [[javascriptallonge-learn]] - shared statements and technical atoms: Learn shares source evidence from const: JavaScript gives us a way to do that, the const keyword. We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const :; Learn shares technical record from const: (diameter) => { const PI = 3.14159265; return diameter * PI } (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-mapwith]] - shared technical atoms: Mapwith shares technical record from partial application: const safeSquareAll = mapWith(maybe((n) => n * n)); (2 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from const: (diameter) => { const PI = 3.14159265; return diameter * PI } (1 shared atom(s))
- [[javascriptallonge-directly]] - shared statements: Directly shares source evidence from linear recursion: Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and com ... [truncated] (1 shared statement(s))
- [[javascriptallonge-element]] - shared statements: Element shares source evidence from linear recursion: Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and com ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from const: Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really ... [truncated] (1 shared statement(s))
- [[javascriptallonge-idea]] - shared statements: Idea shares source evidence from const: Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really ... [truncated] (1 shared statement(s))
- [[javascriptallonge-problem]] - shared statements: Problem shares source evidence from linear recursion: Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and com ... [truncated] (1 shared statement(s))
- [[javascriptallonge-statement]] - shared statements: Statement shares source evidence from a quick summary of functions and bodies: One of the important possible statements is a return statement. A return statement accepts any valid JavaScript expression. (1 shared statement(s))

## Source

- [[javascriptallonge]]
