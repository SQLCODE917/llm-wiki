---
page_id: javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-that-r-953101e3
page_kind: source
summary: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: 13 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-that-r-953101e3@37ddcd52070d4ab90b79c19c603022b1
---

# The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-0ed59777]] - broader source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

## Statements

- We've seen () => 0 . We know that (() => 0)() returns 0 , and this is unsurprising. Likewise, the following all ought to be obvious: _(javascriptallonge.pdf (source-range-7239e085-00188))_
- Well, the last one's a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow. _(javascriptallonge.pdf (source-range-7239e085-00190))_
- In the prelude, we looked at expressions. Values like 0 are expressions, as are things like 40 + 2 . Can we put an expression to the right of the arrow? _(javascriptallonge.pdf (source-range-7239e085-00191))_
- Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ? _(javascriptallonge.pdf (source-range-7239e085-00193))_
- Yes we can! Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-7239e085-00196))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-7239e085-00193))_

## Technical atoms

### Technical frame 1: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00190))_

> Well, the last one's a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00189))_

```
(() => 1)()
//=> 1
(() => "Hello, JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity)()
//=> Infinity
```

### Technical frame 2: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

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

### Technical frame 3: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00196))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00195))_

```
(() => (() => 0)())()
//=> 0
```

### Technical frame 4: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00196))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00197))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.

### Technical frame 5: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00196))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00198))_

```
(() =>
(() => 0
)()
)()
//=> 0
```
