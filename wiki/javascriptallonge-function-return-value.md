---
page_id: javascriptallonge-function-return-value
page_kind: concept
summary: Function Return Value: 2 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-function-return-value@04f48fa2d2664f38579dcdd9ac797768
---

# Function Return Value

What [[javascriptallonge]] covers about function return value:

## Statements

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

- Well, the last one's a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow. _(javascriptallonge.pdf (source-range-7239e085-00190))_

- Yes we can! Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-7239e085-00196))_


## Technical atoms

### Technical frame 1: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00193))_

> Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00192))_

```
(() => 1 + 1)()
//=> 2
(() => "Hello, " + "JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity * Infinity)()
//=> Infinity
```

### Technical frame 2: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00196))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00197))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.


## Related pages

- [[javascriptallonge-function]] - broader topic: Function shares source evidence from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: Yes we can! Functions can return the value of evaluating another function.; Function shares technical record from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity)() //=> Infinity (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-return]] - broader topic: Return shares technical record from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity)() //=> Infinity (2 shared atom(s))
- [[javascriptallonge-value]] - broader topic: Value shares technical record from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity)() //=> Infinity (2 shared atom(s))
- [[javascriptallonge-idea]] - shared statements and technical atoms: Idea shares source evidence from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: Well, the last one's a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.; Idea shares technical record from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity)() //=> Infinity (1 shared statement(s), 1 shared atom(s))

## Source

- [[javascriptallonge]]
