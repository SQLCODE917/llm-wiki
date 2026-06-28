---
page_id: javascriptallonge-language
page_kind: concept
summary: Language: 18 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-language@aa076b3301f586f86482eac2a6936a77
---

# Language

What [[javascriptallonge]] covers about language:

## Statements

- (Many other languages that have a notion of truthiness consider zero and the empty string to be truthy, not falsy, so beware of blindly transliterating code from one language to another!) _(javascriptallonge.pdf (source-range-83ecb080-01106))_
- Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. _(javascriptallonge.pdf (source-range-83ecb080-00049))_
- A different kind of language requires a different kind of book. _(javascriptallonge.pdf (source-range-83ecb080-00130))_
- > 11In some languages, expressions are a kind of value unto themselves and can be manipulated. _(javascriptallonge.pdf (source-range-83ecb080-00175))_
- The grandfather of such languages is Lisp. _(javascriptallonge.pdf (source-range-83ecb080-00175))_
- Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. _(javascriptallonge.pdf (source-range-83ecb080-00215))_
- > 20As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined. _(javascriptallonge.pdf (source-range-83ecb080-00341))_
- Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-83ecb080-00516))_
- This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. _(javascriptallonge.pdf (source-range-83ecb080-00543))_
- Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-83ecb080-01001))_
- Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-83ecb080-01536))_
- For these and other reasons, almost all languages today make it possible to use a fast array or vector type that is optimized for iteration, and even Lisp now has a variety of data structures that are optimized for specific use cases. _(javascriptallonge.pdf (source-range-83ecb080-01568))_
- Like some imperative programming languages, JavaScript allows you to re-assign the value bound : to parameters. _(javascriptallonge.pdf (source-range-83ecb080-01758))_
- Many programmers coming to JavaScript from other languages are familiar with three “canonical” operations on collections: folding, filtering, and finding. _(javascriptallonge.pdf (source-range-83ecb080-02015))_
- Practically speaking, languages like JavaScript already provide arrays with mapping and folding methods, choice operations, and other rich constructs. _(javascriptallonge.pdf (source-range-83ecb080-02167))_
- Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator. _(javascriptallonge.pdf (source-range-83ecb080-02413))_
- Separating concerns with iterators speaks to JavaScript’s fundamental nature: It’s a language that _wants_ to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-83ecb080-02523))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00039))_

> For example, block-structured languages allow us to write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00040))_

> **for** ( **int** i = 0; i < array.length; ++i) {

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01530))_

> > 66Lisp is still very much alive, and one of the most interesting and exciting programming languages in use today is Clojure, a Lisp dialect that runs on the JVM, along with its sibling ClojureScript, Clojure that transpiles to JavaScript. 67https://en.wikipedia.org/wiki/IBM_704

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01533))_

> If you had two 15-bit values and wished to write them to the register, the CONS macro would take the values and write them to a 36-bit word.


## Related pages

- [[javascriptallonge-program]] - shared statements and technical atoms (9 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms (6 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-block]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-function]] - shared statements (3 shared statement(s))
- [[javascriptallonge-code]] - shared statements (2 shared statement(s))
- [[javascriptallonge-evaluate]] - shared statements (1 shared statement(s))
- [[javascriptallonge-expression]] - shared statements (1 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements (1 shared statement(s))
- [[javascriptallonge-write]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
