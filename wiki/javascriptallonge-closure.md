---
page_id: javascriptallonge-closure
page_kind: concept
page_family: topic-concept
summary: Closure: 5 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-closure@bbb5bd085bdf1a56b65ff0531e85c68a
---

# Closure

What [[javascriptallonge]] covers about closure:

## Statements

### And also: / Closures and Scope / if functions without free variables are pure, are closures impure?

- Functions containing one or more free variables are called closures . _(javascriptallonge.pdf (source-range-7239e085-00346))_

- From this, we learn something: A pure function can contain a closure. _(javascriptallonge.pdf (source-range-7239e085-00349))_

- If pure functions can contain closures, can a closure contain a pure function? Using only what we've learned so far, attempt to compose a closure that contains a pure function. If you can't, give your reasoning for why it's impossible. _(javascriptallonge.pdf (source-range-7239e085-00351))_

### And also: / Closures and Scope / it's always the environment

- To understand how closures are evaluated, we need to revisit environments. As we've said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...} ? Let's fill in the blanks! _(javascriptallonge.pdf (source-range-7239e085-00355))_

### And also: / Closures and Scope / which came first, the chicken or the egg?

- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. We are going to explore them in some detail as well as look at some of the other mechanisms JavaScript provides for working with variables and mutable state. _(javascriptallonge.pdf (source-range-7239e085-00378))_


## Technical atoms

### Technical frame 1: And also: / Closures and Scope / if functions without free variables are pure, are closures impure?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00352))_

> Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00351))_

<a id="atom-technical-atom-022fdc90abb9f966"></a>

> If pure functions can contain closures, can a closure contain a pure function?

### Technical frame 2: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00358))_

> (x) => x is called the I Combinator, or the Identity Function . (x) => (y) => x is called the K Combinator, or Kestrel . Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. a http://www.amzn.com/0192801422?tag=raganwald001-20

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00356))_

<a id="atom-technical-atom-634e3513bd1b5d02"></a>

> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.


## Related pages

### Shared technical atoms

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from And also: / Closures and Scope / if functions without free variables are pure, are closures impure?: Functions containing one or more free variables are called closures .; Function shares technical record from And also: / Closures and Scope / if functions without free variables are pure, are closures impure?: If pure functions can contain closures, can a closure contain a pure function? (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-scope]] - shared technical atoms: Scope shares technical record from And also: / Closures and Scope / if functions without free variables are pure, are closures impure?: If pure functions can contain closures, can a closure contain a pure function? (2 shared atom(s))
- [[javascriptallonge-alway]] - shared technical atoms: Alway shares technical record from And also: / Closures and Scope / if functions without free variables are pure, are closures impure?: If pure functions can contain closures, can a closure contain a pure function? (1 shared atom(s))

### Shared claims

- [[javascriptallonge-behaviour]] - shared statements: Behaviour shares source evidence from And also: / Closures and Scope / which came first, the chicken or the egg?: This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. We are going to explore them in some detail as wel ... [truncated] (1 shared statement(s))
- [[javascriptallonge-learn]] - shared statements: Learn shares source evidence from And also: / Closures and Scope / if functions without free variables are pure, are closures impure?: From this, we learn something: A pure function can contain a closure. (1 shared statement(s))

## Source

- [[javascriptallonge]]
