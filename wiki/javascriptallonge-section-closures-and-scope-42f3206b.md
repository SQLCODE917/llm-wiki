---
page_id: javascriptallonge-section-closures-and-scope-42f3206b
page_kind: source
summary: Closures and Scope: 11 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-closures-and-scope-42f3206b@8104802f0b8fbc9ce79541b56719b03a
---

# Closures and Scope

From [[javascriptallonge]].

## Statements

- The environment belonging to the function with signature (x) => ... becomes {x: 1, ...} , and the result of applying the function is another function value. It makes sense that the result value is a function, because the expression for (x) => ... 's body is: _(javascriptallonge.pdf (source-range-31a4cf47-00337))_
- So now we have a value representing that function. Then we're going to take the value of that function and apply it to the argument 2 , something like this: _(javascriptallonge.pdf (source-range-31a4cf47-00339))_
- So we seem to get a new environment {y: 2, ...} . How is the expression x going to be evaluated in that function's environment? There is no x in its environment, it must come from somewhere else. _(javascriptallonge.pdf (source-range-31a4cf47-00341))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. For example, here's the equivalent code in Ruby: _(javascriptallonge.pdf (source-range-31a4cf47-00342))_
- It makes sense that the result value is a function, because the expression for (x) => ... _(javascriptallonge.pdf (source-range-31a4cf47-00337))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. _(javascriptallonge.pdf (source-range-31a4cf47-00342))_

## Technical atoms

### Technical frame 1: Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00337))_

> The environment belonging to the function with signature (x) => ... becomes {x: 1, ...} , and the result of applying the function is another function value. It makes sense that the result value is a function, because the expression for (x) => ... 's body is:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00334))_

```
((x) => (y) => x)(1)(2) //=> 1
```

### Technical frame 2: Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00337))_

> The environment belonging to the function with signature (x) => ... becomes {x: 1, ...} , and the result of applying the function is another function value. It makes sense that the result value is a function, because the expression for (x) => ... 's body is:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00336))_

```
((x) => (y) => x)(1) //=> [Function]
```

### Technical frame 3: Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00339))_

> So now we have a value representing that function. Then we're going to take the value of that function and apply it to the argument 2 , something like this:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00338))_

```
(y) => x
```

### Technical frame 4: Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00341))_

> So we seem to get a new environment {y: 2, ...} . How is the expression x going to be evaluated in that function's environment? There is no x in its environment, it must come from somewhere else.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00340))_

```
((y) => x)(2)
```

### Technical frame 5: Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00342))_

> This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. For example, here's the equivalent code in Ruby:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00343))_

```
lambda { |x| lambda { |y| x } }[1][2] #=> 1
```
