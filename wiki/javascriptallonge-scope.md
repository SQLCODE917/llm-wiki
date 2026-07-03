---
page_id: javascriptallonge-scope
page_kind: concept
page_family: topic-concept
summary: Scope: 2 statement(s) and 15 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-scope@8e4c93ecb3b005c35a9981731fafc51c
---

# Scope

What [[javascriptallonge]] covers about scope:

## Statements

### And also: / Closures and Scope / shadowy variables from a shadowy planet

- When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. _(javascriptallonge.pdf (source-range-7239e085-00375))_


## Technical atoms

### Technical frame 1: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00334))_

> The environment belonging to the function with signature (x) => ... becomes {x: 1, ...} , and the result of applying the function is another function value. It makes sense that the result value is a function, because the expression for (x) => ... 's body is:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00331))_

<a id="atom-technical-atom-f9a48554ab45582a"></a>

```
((x) => (y) => x)(1)(2)
//=> 1
```

### Technical frame 2: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00334))_

> The environment belonging to the function with signature (x) => ... becomes {x: 1, ...} , and the result of applying the function is another function value. It makes sense that the result value is a function, because the expression for (x) => ... 's body is:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00333))_

<a id="atom-technical-atom-4d31ee93c2de0bd2"></a>

```
((x) => (y) => x)(1)
//=> [Function]
```

### Technical frame 3: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00338))_

> So we seem to get a new environment {y: 2, ...} . How is the expression x going to be evaluated in that function's environment? There is no x in its environment, it must come from somewhere else.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00335))_

<a id="atom-technical-atom-025ba0651eab0fd2"></a>

```
(y) => x
```

### Technical frame 4: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00338))_

> So we seem to get a new environment {y: 2, ...} . How is the expression x going to be evaluated in that function's environment? There is no x in its environment, it must come from somewhere else.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00337))_

<a id="atom-technical-atom-b77c7e931dde1312"></a>

```
((y) => x)(2)
```

### Technical frame 5: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00339))_

> This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. For example, here's the equivalent code in Ruby:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00340))_

<a id="atom-technical-atom-40f6f8e50dccfc7c"></a>

```
lambda { |x|
lambda { |y| x }
}[1][2]
#=> 1
```

### Technical frame 6: And also: / Closures and Scope / if functions without free variables are pure, are closures impure?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00352))_

> Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00351))_

<a id="atom-technical-atom-022fdc90abb9f966"></a>

> If pure functions can contain closures, can a closure contain a pure function?

### Technical frame 7: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00358))_

> (x) => x is called the I Combinator, or the Identity Function . (x) => (y) => x is called the K Combinator, or Kestrel . Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. a http://www.amzn.com/0192801422?tag=raganwald001-20

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00356))_

<a id="atom-technical-atom-634e3513bd1b5d02"></a>

> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

### Technical frame 8: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00365))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00360))_

<a id="atom-technical-atom-25dfc322e92bb80d"></a>

```
bh
```

### Technical frame 9: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00365))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00362))_

<a id="atom-technical-atom-af55a2cd0e53b310"></a>

```
(x) =>
(y) =>
(z) => x + y + z
```

### Technical frame 10: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00365))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00364))_

<a id="atom-technical-atom-2bf197b4e3f33351"></a>

```
(x, y, z) => x + y + z
```

### Technical frame 11: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00366))_

> The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00367))_

<a id="atom-technical-atom-bef3b834b711b874"></a>

```
ah
bh
```

### Technical frame 12: And also: / Closures and Scope / shadowy variables from a shadowy planet

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00373))_

> The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x , it is ignored when evaluating x + y . JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00372))_

<a id="atom-technical-atom-28028bea365e6179"></a>

```
(x) =>
(x, y) => x + y
```

### Technical frame 13: And also: / Closures and Scope / shadowy variables from a shadowy planet

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00375))_

> When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00374))_

<a id="atom-technical-atom-d2b62258197a898f"></a>

```
(x) =>
(x, y) =>
(w, z) =>
(w) =>
x + y + z
```

### Technical frame 14: And also: / Closures and Scope / which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00383))_

> The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} . As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00381))_

<a id="atom-technical-atom-ac56068d50c46aef"></a>

> If you don't want your code to operate directly within the global environment, what can you do?

### Technical frame 15: And also: / Closures and Scope / which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00383))_

> The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} . As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00382))_

<a id="atom-technical-atom-9a38ea4605cc1786"></a>

```
// top of the file
(() => {
// ... lots of JavaScript ...
})();
// bottom of the file
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from And also: / Closures and Scope / if functions without free variables are pure, are closures impure?: If pure functions can contain closures, can a closure contain a pure function? (6 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from And also: / Closures and Scope / shadowy variables from a shadowy planet: When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is igno ... [truncated]; Javascript shares technical record from And also: / Closures and Scope / shadowy variables from a shadowy planet: (x) => (x, y) => x + y (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-evaluating]] - shared statements and technical atoms: Evaluating shares source evidence from And also: / Closures and Scope / shadowy variables from a shadowy planet: When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is igno ... [truncated]; Evaluating shares technical record from And also: / Closures and Scope / shadowy variables from a shadowy planet: (x) => (x, y) => x + y (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-alway]] - shared technical atoms: Alway shares technical record from And also: / Closures and Scope / if functions without free variables are pure, are closures impure?: If pure functions can contain closures, can a closure contain a pure function? (2 shared atom(s))
- [[javascriptallonge-closure]] - shared technical atoms: Closure shares technical record from And also: / Closures and Scope / if functions without free variables are pure, are closures impure?: If pure functions can contain closures, can a closure contain a pure function? (2 shared atom(s))
- [[javascriptallonge-evaluate]] - shared technical atoms: Evaluate shares technical record from And also: / Closures and Scope / it's always the environment: (x, y, z) => x + y + z (1 shared atom(s))
- [[javascriptallonge-language]] - shared technical atoms: Language shares technical record from And also: / Closures and Scope / it's always the environment: (x, y, z) => x + y + z (1 shared atom(s))
- [[javascriptallonge-programmer]] - shared technical atoms: Programmer shares technical record from And also: / Closures and Scope / which came first, the chicken or the egg?: // top of the file (() => { // ... lots of JavaScript ... })(); // bottom of the file (1 shared atom(s))

## Source

- [[javascriptallonge]]
