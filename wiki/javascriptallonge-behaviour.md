---
page_id: javascriptallonge-behaviour
page_kind: concept
summary: Behaviour: 5 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-behaviour@467233522ee706e65c316b034f774b80
---

# Behaviour

What [[javascriptallonge]] covers about behaviour:

## Statements

### And also: / Closures and Scope / which came first, the chicken or the egg?

- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. We are going to explore them in some detail as well as look at some of the other mechanisms JavaScript provides for working with variables and mutable state. _(javascriptallonge.pdf (source-range-7239e085-00378))_

### And also: / Naming Functions / function declarations

- The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code. _(javascriptallonge.pdf (source-range-7239e085-00546))_

### Picking the Bean: Choice and Truthiness / truthiness and operators

- Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user. _(javascriptallonge.pdf (source-range-7239e085-00779))_

### Picking the Bean: Choice and Truthiness / function parameters are eager

- In contrast to the behaviour of the ternary operator, || , and && , function parameters are always eagerly evaluated : _(javascriptallonge.pdf (source-range-7239e085-00801))_

### We'll keep it simple: / generators are coroutines

- This behaviour is not unique to JavaScript, generators are called coroutines 92 in other languages: _(javascriptallonge.pdf (source-range-7239e085-01700))_


## Technical atoms

### Technical frame 1: Picking the Bean: Choice and Truthiness / truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00779))_

> Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00778))_

```
!5
//=> false
!undefined
//=> true
```

### Technical frame 2: Picking the Bean: Choice and Truthiness / function parameters are eager

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00804))_

> If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don't need anything like this for or and and , but to demonstrate the technique:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00802))_

```
const or = (a, b) => a || b
const and = (a, b) => a && b
const even = (n) =>
or(n === 0, and(n !== 1, even(n - 2)))
even(42)
//=> Maximum call stack size exceeded.
```


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from And also: / Closures and Scope / which came first, the chicken or the egg?: This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. We are going to explore them in some detail as wel ... [truncated]; Function shares technical record from Picking the Bean: Choice and Truthiness / function parameters are eager: const or = (a, b) => a || b const and = (a, b) => a && b const even = (n) => or(n === 0, and(n !== 1, even(n - 2))) even(42) //=> Maximum call stack size exceeded. (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-parameter]] - shared statements and technical atoms: Parameter shares source evidence from Picking the Bean: Choice and Truthiness / function parameters are eager: In contrast to the behaviour of the ternary operator, || , and && , function parameters are always eagerly evaluated :; Parameter shares technical record from Picking the Bean: Choice and Truthiness / function parameters are eager: const or = (a, b) => a || b const and = (a, b) => a && b const even = (n) => or(n === 0, and(n !== 1, even(n - 2))) even(42) //=> Maximum call stack size exceeded. (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-program]] - shared statements and technical atoms: Program shares source evidence from Picking the Bean: Choice and Truthiness / truthiness and operators: Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is ... [truncated]; Program shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-programmer]] - shared statements and technical atoms: Programmer shares source evidence from Picking the Bean: Choice and Truthiness / truthiness and operators: Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is ... [truncated]; Programmer shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-alway]] - shared technical atoms: Alway shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-closure]] - shared statements: Closure shares source evidence from And also: / Closures and Scope / which came first, the chicken or the egg?: This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. We are going to explore them in some detail as wel ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
