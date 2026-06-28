---
page_id: javascriptallonge-variable
page_kind: concept
summary: Variable: 5 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-variable@0512486d4ba94f2f722269a4e7613514
---

# Variable

What [[javascriptallonge]] covers about variable:

## Statements

### variables and bindings

- But there's another reason for learning the word antidisestablishmentarianism : We might learn how prefixes and postfixes work in English grammar. It's the same thing with (x) => (y) => x . It has a certain important meaning in its own right, and it's also an excellent excuse to learn about functions that make functions, environments, variables, and more. _(javascriptallonge.pdf (source-range-31a4cf47-00304))_

- In order to talk about how this works, we should agree on a few terms (you may already know them, but let's check-in together and 'synchronize our dictionaries'). The first x , the one in (x) => ... , is an argument . The y in function (y) ... is another argument. The second x , the one in => x , is not an argument, it's an expression referring to a variable . Arguments and variables work the same way whether we're talking about (x) => (y) => x or just plain (x) => x . _(javascriptallonge.pdf (source-range-31a4cf47-00305))_

- Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. An environment is a (possibly empty) dictionary that maps variables to values by name. The x in the expression that we call a 'variable' is itself an expression that is evaluated by looking up the value in the environment. _(javascriptallonge.pdf (source-range-31a4cf47-00306))_

- The value of a variable when evaluated in an environment is the value bound to the variable's name in that environment, which is '2' _(javascriptallonge.pdf (source-range-31a4cf47-00319))_


## Related pages

- [[javascriptallonge-environment]] - shared statements: Environment shares source evidence from variables and bindings: Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. An environment is a (possibly empty) dictionary ... [truncated] (1 shared statement(s))
- [[javascriptallonge-expression]] - shared statements: Expression shares source evidence from variables and bindings: Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. An environment is a (possibly empty) dictionary ... [truncated] (1 shared statement(s))
- [[javascriptallonge-second]] - shared statements: Second shares source evidence from variables and bindings: In order to talk about how this works, we should agree on a few terms (you may already know them, but let's check-in together and 'synchronize our dictionaries'). Th ... [truncated] (1 shared statement(s))
- [[javascriptallonge-value]] - shared statements: Value shares source evidence from variables and bindings: The value of a variable when evaluated in an environment is the value bound to the variable's name in that environment, which is '2' (1 shared statement(s))

## Source

- [[javascriptallonge]]
