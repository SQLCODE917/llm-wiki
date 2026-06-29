---
page_id: javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-applying-functio-9dc686e6
page_kind: source
summary: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / applying functions: 5 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-applying-functio-9dc686e6@03c0a55856ae341b371ee5323922531d
---

# The first sip: Basic Functions / As Little As Possible About Functions, But No Less / applying functions

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-0ed59777]] - broader source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

## Statements

- Let's put functions to work. The way we use functions is to apply them to zero or more values called arguments . Just as 2 + 2 produces a value (in this case 4 ), applying a function to zero or more arguments produces a value as well. _(javascriptallonge.pdf (source-range-7239e085-00181))_
- Right now, we only know about one such expression: () => 0 , so let's use it. We'll put it in parentheses 17 to keep the parser happy, like we did above: (() => 0) . Since we aren't giving it any arguments, we'll simply write () after the expression. So we write: _(javascriptallonge.pdf (source-range-7239e085-00184))_
- 17 If you're used to other programming languages, you've probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. If not… Welcome to the ALGOL family of programming languages! _(javascriptallonge.pdf (source-range-7239e085-00186))_

## Technical atoms

### Technical frame 1: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / applying functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00184))_

> Right now, we only know about one such expression: () => 0 , so let's use it. We'll put it in parentheses 17 to keep the parser happy, like we did above: (() => 0) . Since we aren't giving it any arguments, we'll simply write () after the expression. So we write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00183))_

```
fn_expr(args)
```

### Technical frame 2: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / applying functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00186))_

> 17 If you're used to other programming languages, you've probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. If not… Welcome to the ALGOL family of programming languages!

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00185))_

```
(() => 0)()
//=> 0
```
