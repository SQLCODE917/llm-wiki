---
page_id: javascriptallonge-section-and-also-that-constant-coffee-craving-const-and-lexical-scope-518692ba
page_kind: source
page_family: section-reference
summary: And also: / That Constant Coffee Craving / const and lexical scope: 14 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-that-constant-coffee-craving-const-and-lexical-scope-518692ba@47c313728e88996f3c51dbc234a14af0
---

# And also: / That Constant Coffee Craving / const and lexical scope

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-and-also-that-constant-coffee-craving-7d1b2fd1]] - broader source section: And also: / That Constant Coffee Craving

## Statements

- This seems very straightforward, but alas, there are some semantics of binding names that we need to understand if we're to place const anywhere we like. The first thing to ask ourselves is, what happens if we use const to bind two different values to the 'same' name? _(javascriptallonge.pdf (source-range-7239e085-00448))_
- It's more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we've elided. We can use any expression in there, and that expression can invoke diameter_fn . For example: _(javascriptallonge.pdf (source-range-7239e085-00452))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn . _(javascriptallonge.pdf (source-range-7239e085-00454))_
- This is called lexical scoping 31 , because we can discover where a name is bound by looking at the source code for the program. We can see that PI is bound in an environment surrounding (diameter) => diameter * PI , we don't need to know where diameter_fn is invoked. _(javascriptallonge.pdf (source-range-7239e085-00455))_
- That much we can carefully work out from the way closures work. Does const work the same way? Let's find out: _(javascriptallonge.pdf (source-range-7239e085-00459))_
- Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-7239e085-00462))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn . _(javascriptallonge.pdf (source-range-7239e085-00454))_
- This is called lexical scoping 31 , because we can discover where a name is bound by looking at the source code for the program. _(javascriptallonge.pdf (source-range-7239e085-00455))_
