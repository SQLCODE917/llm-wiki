---
page_id: javascriptallonge-section-why-4e397686
page_kind: source
summary: Why?: 9 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-why-4e397686@73149a650601f539861fbafde205218e
---

# Why?

From [[javascriptallonge]].

## Statements

- It enables you to make recursive functions without needing to bind a function to a name in an environment. _(javascriptallonge.pdf (source-range-83ecb080-02304))_
- This has little practical utility in JavaScript, but in combinatory logic it’s essential: With fixed-point combinators it’s possible to compute everything computable without binding names. _(javascriptallonge.pdf (source-range-83ecb080-02304))_
- Well, besides all of the practical applications that combinators provide, there is this little thing called _The joy of working things out._ _(javascriptallonge.pdf (source-range-83ecb080-02305))_
- There are many explanations of the Y Combinator’s mechanism on the internet, but resist the temptation to read any of them: Work it out for yourself. _(javascriptallonge.pdf (source-range-83ecb080-02306))_
- One tip is to use JavaScript to name things. _(javascriptallonge.pdf (source-range-83ecb080-02307))_
- Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-83ecb080-02310))_
- Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-83ecb080-02310))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02300))_

> This is the canonical Y Combinator[86] :

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02301))_

> **const** Y = (f) => ( x => f(v => x(x)(v)) )( x => f(v => x(x)(v)) );

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02307))_

> One tip is to use JavaScript to name things. For example, you could start by writing:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02308))_

> **const** Y = (f) => { **const** something = x => f(v => x(x)(v));
