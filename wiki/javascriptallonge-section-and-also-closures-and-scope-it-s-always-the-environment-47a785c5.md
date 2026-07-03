---
page_id: javascriptallonge-section-and-also-closures-and-scope-it-s-always-the-environment-47a785c5
page_kind: source
page_family: section-reference
summary: And also: / Closures and Scope / it's always the environment: 15 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-closures-and-scope-it-s-always-the-environment-47a785c5@ba8192d753fd9a5ce896d69dc7472019
---

# And also: / Closures and Scope / it's always the environment

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-and-also-closures-and-scope-d1679ec0]] - broader source section: And also: / Closures and Scope

### Topics

- [[javascriptallonge-environment]] - topic hub: opens the topic page for Environment

## Statements

- To understand how closures are evaluated, we need to revisit environments. As we've said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...} ? Let's fill in the blanks! _(javascriptallonge.pdf (source-range-7239e085-00355))_
- (x) => x is called the I Combinator, or the Identity Function . (x) => (y) => x is called the K Combinator, or Kestrel . Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. a http://www.amzn.com/0192801422?tag=raganwald001-20 _(javascriptallonge.pdf (source-range-7239e085-00358))_
- Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) . _(javascriptallonge.pdf (source-range-7239e085-00365))_
- The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-7239e085-00366))_
- As we've said before, all functions are associated with an environment. _(javascriptallonge.pdf (source-range-7239e085-00355))_
- Calling a curried function with only some of its arguments is sometimes called partial application b . _(javascriptallonge.pdf (source-range-7239e085-00366))_

## Technical atoms

### Technical frame 1: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00358))_

> (x) => x is called the I Combinator, or the Identity Function . (x) => (y) => x is called the K Combinator, or Kestrel . Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. a http://www.amzn.com/0192801422?tag=raganwald001-20

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00356))_

<a id="atom-technical-atom-634e3513bd1b5d02"></a>

> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.
