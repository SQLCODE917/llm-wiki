---
page_id: javascriptallonge-variable
page_kind: concept
page_family: topic-concept
summary: Variable: 5 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-variable@c68228425c3b517ace932551bbf784ee
---

# Variable

What [[javascriptallonge]] covers about variable:

## Statements

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

- But there's another reason for learning the word antidisestablishmentarianism : We might learn how prefixes and postfixes work in English grammar. It's the same thing with (x) => (y) => x . It has a certain important meaning in its own right, and it's also an excellent excuse to learn about functions that make functions, environments, variables, and more. _(javascriptallonge.pdf (source-range-7239e085-00301))_

- In order to talk about how this works, we should agree on a few terms (you may already know them, but let's check-in together and 'synchronize our dictionaries'). The first x , the one in (x) => ... , is an argument . The y in function (y) ... is another argument. The second x , the one in => x , is not an argument, it's an expression referring to a variable . Arguments and variables work the same way whether we're talking about (x) => (y) => x or just plain (x) => x . _(javascriptallonge.pdf (source-range-7239e085-00302))_

- Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. An environment is a (possibly empty) dictionary that maps variables to values by name. The x in the expression that we call a 'variable' is itself an expression that is evaluated by looking up the value in the environment. _(javascriptallonge.pdf (source-range-7239e085-00303))_

- The value of a variable when evaluated in an environment is the value bound to the variable's name in that environment, which is '2' _(javascriptallonge.pdf (source-range-7239e085-00316))_


## Technical atoms

### Technical frame 1: And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00301))_

> But there's another reason for learning the word antidisestablishmentarianism : We might learn how prefixes and postfixes work in English grammar. It's the same thing with (x) => (y) => x . It has a certain important meaning in its own right, and it's also an excellent excuse to learn about functions that make functions, environments, variables, and more.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00299))_

<a id="atom-technical-atom-3aa4f4b69198f2f9"></a>

```
(x) => (y) => x
```

### Technical frame 2: And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00314))_

> The value '2' is bound to the name 'x' in the environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00306))_

<a id="atom-technical-atom-4a548db5b5a8be44"></a>

```
((x) => x)(2)
//=> 2
```

### Technical frame 3: And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00314))_

> The value '2' is bound to the name 'x' in the environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00310))_

<a id="atom-technical-atom-373fadc827f1fa16"></a>

> - One sub-expression, (x) => x evaluates to a function.


## Related pages

### Shared technical atoms

- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: (x) => (y) => x (2 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: (x) => (y) => x (2 shared atom(s))
- [[javascriptallonge-environment]] - shared statements and technical atoms: Environment shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. An environment is a (possibly empty) dictionary ... [truncated]; Environment shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: ((x) => x)(2) //=> 2 (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms: Value shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: The value of a variable when evaluated in an environment is the value bound to the variable's name in that environment, which is '2'; Value shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: ((x) => x)(2) //=> 2 (1 shared statement(s), 1 shared atom(s))

### Shared claims

- [[javascriptallonge-expression]] - shared statements: Expression shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. An environment is a (possibly empty) dictionary ... [truncated] (1 shared statement(s))
- [[javascriptallonge-second]] - shared statements: Second shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: In order to talk about how this works, we should agree on a few terms (you may already know them, but let's check-in together and 'synchronize our dictionaries'). Th ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
