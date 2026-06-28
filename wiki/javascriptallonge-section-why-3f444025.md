---
page_id: javascriptallonge-section-why-3f444025
page_kind: source
summary: Why?: 10 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-why-3f444025@85d85ae29ef6174285759e64bce31d64
---

# Why?

From [[javascriptallonge]].

## Statements

- Why? It enables you to make recursive functions without needing to bind a function to a name in an environment. This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names. _(javascriptallonge.pdf (source-range-31a4cf47-01489))_
- So again, why include the recipe? Well, besides all of the practical applications that combinators provide, there is this little thing called The joy of working things out. _(javascriptallonge.pdf (source-range-31a4cf47-01490))_
- There are many explanations of the Y Combinator's mechanism on the internet, but resist the temptation to read any of them: Work it out for yourself. Use it as an excuse to get familiar with your environment's debugging facility. _(javascriptallonge.pdf (source-range-31a4cf47-01491))_
- One tip is to use JavaScript to name things. For example, you could start by writing: _(javascriptallonge.pdf (source-range-31a4cf47-01492))_
- What is this something and how does it work? Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-31a4cf47-01494))_
- Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-31a4cf47-01494))_

## Technical atoms

### Technical frame 1: Why?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01489))_

> Why? It enables you to make recursive functions without needing to bind a function to a name in an environment. This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01487))_

```
This is the canonical Y Combinator 86 : const Y = (f) => ( x => f(v => x(x)(v)) )( x => f(v => x(x)(v)) ); You use it like this: const factorial = Y( function (fac) { (n == 0 ? 1 : n * fac(n - 1));
```

### Technical frame 2: Why?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01489))_

> Why? It enables you to make recursive functions without needing to bind a function to a name in an environment. This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01488))_

```
return function (n) { return } }); factorial(5) //=> 120
```

### Technical frame 3: Why?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01494))_

> What is this something and how does it work? Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01493))_

```
const Y = (f) => { const something = x => f(v => x(x)(v)); return something(something); };
```
