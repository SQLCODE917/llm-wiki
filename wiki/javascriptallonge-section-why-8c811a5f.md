---
page_id: javascriptallonge-section-why-8c811a5f
page_kind: source
page_family: section-reference
summary: Why?: 7 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-03
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-why-8c811a5f@abeb5229b9013d4d65f0061cb48a0199
---

# Why?

From [[javascriptallonge]].

## Statements

- Recipes with Data 

178 

## **Why?** 

This is the canonical Y Combinator[86] : 

**const** Y = (f) => ( x => f(v => x(x)(v)) )( x => f(v => x(x)(v)) ); 

You use it like this: 

**const** factorial = Y( **function** (fac) { **return function** (n) { **return** (n == 0 ? 1 : n * fac(n - 1)); } }); factorial(5) _//=> 120_ 

Why? It enables you to make recursive functions without needing to bind a function to a name in an environment. This has little practical utility in JavaScript, but in combinatory logic it’s essential: With fixed-point combinators it’s possible to compute everything computable without binding names. 

So again, why include the recipe? Well, besides all of the practical applications that combinators provide, there is this little thing called _The joy of working things out._ 

There are many explanations of the Y Combinator’s mechanism on the internet, but resist the temptation to read any of them: Work it out for yourself. Use it as an excuse to get familiar with your environment’s debugging facility. 

One tip is to use JavaScript to name things. For example, you could start by writing: 

**const** Y = (f) => { **const** something = x => f(v => x(x)(v)); 

**return** something(something); }; 

What is this something and how does it work? Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. 

Work things out for yourself! 

> 86https://en.wikipedia.org/wiki/Fixed-point_combinator#Example_in_JavaScript _(javascriptallonge.pdf (source-range-af806fb1-00230))_
- Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-af806fb1-00230))_
