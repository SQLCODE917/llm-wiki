---
page_id: javascriptallonge-section-var-c73bae7a
page_kind: source
summary: **var**: 14 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-var-c73bae7a@f045545fbaa3ec098ed4d3256c8fcfef
---

# **var**

From [[javascriptallonge]].

## Statements

- JavaScript has one _more_ way to bind a name to a value, var.[71] var looks a lot like let: _(javascriptallonge.pdf (source-range-83ecb080-01793))_
- First, var is not block scoped, it’s function scoped, just like function declarations: _(javascriptallonge.pdf (source-range-83ecb080-01799))_
- Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. _(javascriptallonge.pdf (source-range-83ecb080-01801))_
- A function declaration can appear anywhere within a function, but the declaration _and_ the definition are hoisted. _(javascriptallonge.pdf (source-range-83ecb080-01802))_
- But, again, it is unwise to expect consistency. _(javascriptallonge.pdf (source-range-83ecb080-01802))_
- A function declaration can appear anywhere within a function, but the declaration _and_ the definition are hoisted. _(javascriptallonge.pdf (source-range-83ecb080-01802))_
- But it’s not like const and let in that it’s function scoped, not block scoped. _(javascriptallonge.pdf (source-range-83ecb080-01818))_
- In that way, var is a little like const and let, we should always declare and bind names before using them. _(javascriptallonge.pdf (source-range-83ecb080-01818))_
- In that way, var is a little like const and let, we should always declare and bind names before using them. _(javascriptallonge.pdf (source-range-83ecb080-01818))_

## Technical atoms

> **return** n * factorial2(x); } } factorial2(5) _//=> 120_
_(source: javascriptallonge.pdf (source-range-83ecb080-01798))_

> Context: But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration _and_ the definition are hoisted. Note this example of a function that uses a helper:
_(context: javascriptallonge.pdf (source-range-83ecb080-01802))_

> **const** factorial = (n) => {
_(source: javascriptallonge.pdf (source-range-83ecb080-01803))_

> Context: JavaScript hoists the let and the assignment. But not so with var:
_(context: javascriptallonge.pdf (source-range-83ecb080-01809))_

> **const** factorial = (n) => {
_(source: javascriptallonge.pdf (source-range-83ecb080-01810))_

> Context: JavaScript hoists the declaration, but not the assignment. It is as if we’d written:
_(context: javascriptallonge.pdf (source-range-83ecb080-01812))_

> **const** factorial = (n) => {
_(source: javascriptallonge.pdf (source-range-83ecb080-01815))_

> **let** innerFactorial = **undefined** ; **return** innerFactorial(n, 1);
_(source: javascriptallonge.pdf (source-range-83ecb080-01816))_
