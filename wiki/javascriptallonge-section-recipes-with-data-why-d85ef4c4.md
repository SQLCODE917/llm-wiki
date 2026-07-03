---
page_id: javascriptallonge-section-recipes-with-data-why-d85ef4c4
page_kind: source
page_family: section-reference
summary: Recipes with Data / Why?: 10 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-data-why-d85ef4c4@d30683b32ef6fd157af49921f38f5f7c
---

# Recipes with Data / Why?

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-recipes-with-data-178f0a89]] - broader source section: Recipes with Data

## Statements

- Why? It enables you to make recursive functions without needing to bind a function to a name in an environment. This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names. _(javascriptallonge.pdf (source-range-7239e085-01489))_
- So again, why include the recipe? Well, besides all of the practical applications that combinators provide, there is this little thing called The joy of working things out. _(javascriptallonge.pdf (source-range-7239e085-01490))_
- There are many explanations of the Y Combinator's mechanism on the internet, but resist the temptation to read any of them: Work it out for yourself. Use it as an excuse to get familiar with your environment's debugging facility. _(javascriptallonge.pdf (source-range-7239e085-01491))_
- One tip is to use JavaScript to name things. For example, you could start by writing: _(javascriptallonge.pdf (source-range-7239e085-01492))_
- What is this something and how does it work? Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-7239e085-01494))_
- Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-7239e085-01494))_

## Technical atoms

### Technical frame 1: Recipes with Data / Why?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01489))_

> Why? It enables you to make recursive functions without needing to bind a function to a name in an environment. This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01487))_

<a id="atom-technical-atom-cf15dbfe1a5d6c6d"></a>

```
This is the canonical Y Combinator86:
const Y = (f) =>
( x => f(v => x(x)(v)) )(
x => f(v => x(x)(v))
);
You use it like this:
const factorial = Y(function (fac) {
return function (n) {
return (n == 0 ? 1 : n * fac(n - 1));
```

### Technical frame 2: Recipes with Data / Why?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01489))_

> Why? It enables you to make recursive functions without needing to bind a function to a name in an environment. This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01488))_

<a id="atom-technical-atom-3bd74a484f1de867"></a>

```
return function (n) {
return (n == 0 ? 1
}
});
factorial(5)
//=> 120
```

### Technical frame 3: Recipes with Data / Why?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01494))_

> What is this something and how does it work? Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01493))_

<a id="atom-technical-atom-69274e86b4fc6a55"></a>

```
const Y = (f) => {
const something = x => f(v => x(x)(v));
return something(something);
};
```
