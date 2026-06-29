---
page_id: javascriptallonge-section-functions-that-return-values-and-evaluate-expressions-8aeedb74
page_kind: source
summary: functions that return values and evaluate expressions: 13 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-functions-that-return-values-and-evaluate-expressions-8aeedb74@7e764b38301dbdb05d0ad502fd048cbc
---

# functions that return values and evaluate expressions

From [[javascriptallonge]].

## Statements

- We've seen () => 0 . We know that (() => 0)() returns 0 , and this is unsurprising. Likewise, the following all ought to be obvious: _(javascriptallonge.pdf (source-range-8eb13d6b-00192))_
- Well, the last one's a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow. _(javascriptallonge.pdf (source-range-8eb13d6b-00194))_
- In the prelude, we looked at expressions. Values like 0 are expressions, as are things like 40 + 2 . Can we put an expression to the right of the arrow? _(javascriptallonge.pdf (source-range-8eb13d6b-00195))_
- Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ? _(javascriptallonge.pdf (source-range-8eb13d6b-00197))_
- Yes we can! Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-8eb13d6b-00200))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-8eb13d6b-00197))_

## Technical atoms

### Technical frame 1: functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00194))_

> Well, the last one's a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00193))_

```
(() => 1)() //=> 1 (() => "Hello, JavaScript")() //=> "Hello, JavaScript" (() => Infinity )() //=> Infinity
```

### Technical frame 2: functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00197))_

> Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ?

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00196))_

```
(() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity )() //=> Infinity
```

### Technical frame 3: functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00200))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00199))_

```
(() => (() => 0)())() //=> 0
```

### Technical frame 4: functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00200))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00201))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.

### Technical frame 5: functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00200))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00202))_

```
(() => (() => 0 )() )() //=> 0
```
