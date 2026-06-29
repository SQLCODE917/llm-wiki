---
page_id: javascriptallonge-section-applying-functions-187f9521
page_kind: source
summary: applying functions: 5 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-applying-functions-187f9521@fca458b8b538c1d6c6ea2c6572dc6a15
---

# applying functions

From [[javascriptallonge]].

## Statements

- Let's put functions to work. The way we use functions is to apply them to zero or more values called arguments . Just as 2 + 2 produces a value (in this case 4 ), applying a function to zero or more arguments produces a value as well. _(javascriptallonge.pdf (source-range-8eb13d6b-00185))_
- Right now, we only know about one such expression: () => 0 , so let's use it. We'll put it in parentheses 17 to keep the parser happy, like we did above: (() => 0) . Since we aren't giving it any arguments, we'll simply write () after the expression. So we write: _(javascriptallonge.pdf (source-range-8eb13d6b-00188))_
- 17 If you're used to other programming languages, you've probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. If not… Welcome to the ALGOL family of programming languages! _(javascriptallonge.pdf (source-range-8eb13d6b-00190))_

## Technical atoms

### Technical frame 1: applying functions

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00188))_

> Right now, we only know about one such expression: () => 0 , so let's use it. We'll put it in parentheses 17 to keep the parser happy, like we did above: (() => 0) . Since we aren't giving it any arguments, we'll simply write () after the expression. So we write:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00187))_

```
fn_expr ( args )
```

### Technical frame 2: applying functions

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00190))_

> 17 If you're used to other programming languages, you've probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. If not… Welcome to the ALGOL family of programming languages!

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00189))_

```
(() => 0)() //=> 0
```
