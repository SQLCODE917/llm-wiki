---
page_id: javascriptallonge-section-const-d78dfb0f
page_kind: source
summary: **const**: 20 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-const-d78dfb0f@121df7393f60a138e7d66f88b7ed7c3b
---

# **const**

From [[javascriptallonge]].

## Statements

- Another way to write our “circumference” function would be to pass PI along with the diameter argument, something like this: _(javascriptallonge.pdf (source-range-83ecb080-00582))_
- This differs from our example above in that there is only one environment, rather than two. _(javascriptallonge.pdf (source-range-83ecb080-00588))_
- We have one binding in the environment representing our regular argument, and another our “constant.” That’s more efficient, and it’s _almost_ what we wanted all along: A way to bind 3.14159265 to a readable name. _(javascriptallonge.pdf (source-range-83ecb080-00588))_
- This differs from our example above in that there is only one environment, rather than two. _(javascriptallonge.pdf (source-range-83ecb080-00588))_
- JavaScript gives us a way to do that, the const keyword. _(javascriptallonge.pdf (source-range-83ecb080-00589))_
- We’ll learn a lot more about const in future chapters, but here’s the most important thing we can do with const: _(javascriptallonge.pdf (source-range-83ecb080-00589))_
- That’s much better than what we were writing. _(javascriptallonge.pdf (source-range-83ecb080-00592))_
- We use the const keyword in a _const statement_ . _(javascriptallonge.pdf (source-range-83ecb080-00593))_
- We can bind any expression. _(javascriptallonge.pdf (source-range-83ecb080-00602))_
- Amazing how such an important idea–naming functions–can be explained _en passant_ in just a few words. _(javascriptallonge.pdf (source-range-83ecb080-00605))_
- We can bind more than one name-value pair by separating them with commas. _(javascriptallonge.pdf (source-range-83ecb080-00606))_
- > 30We’re into the second chapter and we’ve finally named a function. _(javascriptallonge.pdf (source-range-83ecb080-00608))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00582))_

> Another way to write our “circumference” function would be to pass PI along with the diameter argument, something like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00583))_

> (diameter, PI) => diameter * PI

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00584, source-range-83ecb080-00588))_

> And we could use it like this: This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our “constant.” That’s more efficient, and it’s _almost_ what we wanted all along: A way to bind 3.14159265 to a readable name.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00587))_

> ((diameter, PI) => diameter * PI)(2, 3.14159265) _//=> 6.2831853_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00589))_

> JavaScript gives us a way to do that, the const keyword. We’ll learn a lot more about const in future chapters, but here’s the most important thing we can do with const:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00590))_

> (diameter) => { **const** PI = 3.14159265;

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00594))_

> It works just as we want. Instead of:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00595))_

> ((diameter) => ((PI) => diameter * PI)(3.14159265))(2)

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00597))_

> ((diameter, PI) => diameter * PI)(2, 3.14159265) _//=> 6.2831853_

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00598))_

> We write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00601))_

> ((diameter) => { **const** PI = 3.14159265; **return** diameter * PI })(2) _//=> 6.2831853_

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00602))_

> We can bind any expression. Functions are expressions, so we can bind helper functions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00604))_

> This underscores what we’ve said: if we have an expression that evaluates to a function, we apply it with ().

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00606))_

> We can bind more than one name-value pair by separating them with commas. For readability, most people put one binding per line:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00607))_

> (d) => { **const** PI = 3.14159265, calc = (diameter) => diameter * PI; **return** "The circumference is " + calc(d) }
