---
page_id: javascriptallonge-important
page_kind: concept
page_family: topic-concept
summary: Important: 5 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-important@317b25566c88f8224a67dfc1373c0357
---

# Important

What [[javascriptallonge]] covers about important:

## Statements

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / a quick summary of functions and bodies

- One of the important possible statements is a return statement. A return statement accepts any valid JavaScript expression. _(javascriptallonge.pdf (source-range-7239e085-00288))_

### And also: / That Constant Coffee Craving / const

- JavaScript gives us a way to do that, the const keyword. We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const : _(javascriptallonge.pdf (source-range-7239e085-00420))_

- Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as 'first class entities. ' Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth. _(javascriptallonge.pdf (source-range-7239e085-00433))_

### And also: / Building Blocks / partial application

- We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely: _(javascriptallonge.pdf (source-range-7239e085-00599))_

### Composing and Decomposing Data / Self-Similarity / linear recursion

- Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions. _(javascriptallonge.pdf (source-range-7239e085-00923))_


## Technical atoms

### Technical frame 1: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00422))_

> The const keyword introduces one or more bindings in the block that encloses it. It doesn't incur the cost of a function invocation. That's great. Even better, it puts the symbol (like PI ) close to the value ( 3.14159265 ). That's much better than what we were writing.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00421))_

<a id="atom-technical-atom-96b703ac20909c60"></a>

```
(diameter) => {
const PI = 3.14159265;
return diameter * PI
}
```

### Technical frame 2: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00603))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00601))_

<a id="atom-technical-atom-330729474fe641db"></a>

```
const safeSquareAll = mapWith(maybe((n) => n * n));
```

### Technical frame 3: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00603))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00602))_

<a id="atom-technical-atom-10a4f14311565237"></a>

```
safeSquareAll([1, null, 2, 3])
//=> [1, null, 4, 9]
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-partial-application]] - shared statements and technical atoms: partial application shares source evidence from And also: / Building Blocks / partial application: We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:; partial application shares technical record from And also: / Building Blocks / partial application: const safeSquareAll = mapWith(maybe((n) => n * n)); (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-mapwith]] - shared technical atoms: Mapwith shares technical record from And also: / Building Blocks / partial application: const safeSquareAll = mapWith(maybe((n) => n * n)); (2 shared atom(s))
- [[javascriptallonge-learn]] - shared statements and technical atoms: Learn shares source evidence from And also: / That Constant Coffee Craving / const: JavaScript gives us a way to do that, the const keyword. We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const :; Learn shares technical record from And also: / That Constant Coffee Craving / const: (diameter) => { const PI = 3.14159265; return diameter * PI } (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from And also: / That Constant Coffee Craving / const: (diameter) => { const PI = 3.14159265; return diameter * PI } (1 shared atom(s))

### Shared claims

- [[javascriptallonge-element]] - shared statements: Element shares source evidence from Composing and Decomposing Data / Self-Similarity / linear recursion: Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and com ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from And also: / That Constant Coffee Craving / const: Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really ... [truncated] (1 shared statement(s))
- [[javascriptallonge-idea]] - shared statements: Idea shares source evidence from And also: / That Constant Coffee Craving / const: Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really ... [truncated] (1 shared statement(s))
- [[javascriptallonge-problem]] - shared statements: Problem shares source evidence from Composing and Decomposing Data / Self-Similarity / linear recursion: Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and com ... [truncated] (1 shared statement(s))
- [[javascriptallonge-statement]] - shared statements: Statement shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / a quick summary of functions and bodies: One of the important possible statements is a return statement. A return statement accepts any valid JavaScript expression. (1 shared statement(s))

## Source

- [[javascriptallonge]]
