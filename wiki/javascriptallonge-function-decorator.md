---
page_id: javascriptallonge-function-decorator
page_kind: concept
summary: Function Decorator: 2 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-function-decorator@5735e454c05174ba48acaaf06a71932c
---

# Function Decorator

What [[javascriptallonge]] covers about function decorator:

## Statements

### And also: / Combinators and Function Decorators / function decorators

- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-7239e085-00578))_


## Technical atoms

### Technical frame 1: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00578))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00577))_

```
const nothing = not(something);
```


## Related pages

- [[javascriptallonge-function]] - broader topic: Function shares source evidence from And also: / Combinators and Function Decorators / function decorators: not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorator ... [truncated]; Function shares technical record from And also: / Combinators and Function Decorators / function decorators: const nothing = not(something); (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-combinator]] - shared statements and technical atoms: Combinator shares source evidence from And also: / Combinators and Function Decorators / function decorators: not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorator ... [truncated]; Combinator shares technical record from And also: / Combinators and Function Decorators / function decorators: const nothing = not(something); (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-section-and-also-combinators-and-function-decorators-function-decorators-913f90c6]] - source section: And also: / Combinators and Function Decorators / function decorators shares source evidence from And also: / Combinators and Function Decorators / function decorators: So instead of writing !someFunction(42) , we can write not(someFunction)(42) . Hardly progress. But like compose , we could write either:; And also: / Combinators and Function Decorators / function decorators shares technical record from And also: / Combinators and Function Decorators / function decorators: combinators The word 'combinator' has a precise technical meaning in mathematics: 'A combinator is a higher-order function that uses only function application and ea ... [truncated] (3 shared statement(s), 6 shared atom(s))

## Source

- [[javascriptallonge]]
