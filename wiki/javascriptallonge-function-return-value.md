---
page_id: javascriptallonge-function-return-value
page_kind: concept
summary: Function Return Value: 2 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-function-return-value@654fee76789105ecf68893a6528c09a1
---

# Function Return Value

What [[javascriptallonge]] covers about function return value:

## Statements

### functions that return values and evaluate expressions

- Well, the last one's a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow. _(javascriptallonge.pdf (source-range-31a4cf47-00194))_

- Yes we can! Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-31a4cf47-00200))_


## Technical atoms

### Technical frame 1: functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00197))_

> Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ?

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00196))_

```
(() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity )() //=> Infinity
```

### Technical frame 2: functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00200))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00201))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.


## Related pages

- [[javascriptallonge-function]] - broader topic: Function shares source evidence from functions that return values and evaluate expressions: Yes we can! Functions can return the value of evaluating another function.; Function shares technical record from functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity )() //=> Infinity (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-return]] - broader topic: Return shares technical record from functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity )() //=> Infinity (2 shared atom(s))
- [[javascriptallonge-value]] - broader topic: Value shares technical record from functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity )() //=> Infinity (2 shared atom(s))
- [[javascriptallonge-idea]] - shared statements and technical atoms: Idea shares source evidence from functions that return values and evaluate expressions: Well, the last one's a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.; Idea shares technical record from functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity )() //=> Infinity (1 shared statement(s), 1 shared atom(s))

## Source

- [[javascriptallonge]]
