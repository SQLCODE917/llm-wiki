---
page_id: javascriptallonge-section-some-history-6c2c1826
page_kind: source
summary: **some history**: 19 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-some-history-6c2c1826@51b4e62fd0f5ea02f063380e1fcc1ef5
---

# **some history**

From [[javascriptallonge]].

## Statements

- (The very first FORTRAN implementation was also written for the 704). _(javascriptallonge.pdf (source-range-83ecb080-01527))_
- The CPU’s instruction set featured two important macros: CAR would fetch 15 bits representing the Contents of the Address part of the Register, while CDR would fetch the Contents of the Decrement part of the Register. _(javascriptallonge.pdf (source-range-83ecb080-01528))_
- The 704 had a 36-bit word, meaning that it was very fast to store and retrieve 36-bit values. _(javascriptallonge.pdf (source-range-83ecb080-01528))_
- > 66Lisp is still very much alive, and one of the most interesting and exciting programming languages in use today is Clojure, a Lisp dialect that runs on the JVM, along with its sibling ClojureScript, Clojure that transpiles to JavaScript. _(javascriptallonge.pdf (source-range-83ecb080-01530))_
- In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. _(javascriptallonge.pdf (source-range-83ecb080-01533))_
- In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. _(javascriptallonge.pdf (source-range-83ecb080-01533))_
- The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells. _(javascriptallonge.pdf (source-range-83ecb080-01534))_
- Lisp’s basic data type is often said to be the list, but in actuality it was the “cons cell,” the term used to describe two 15-bit values stored in one word. _(javascriptallonge.pdf (source-range-83ecb080-01534))_
- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. _(javascriptallonge.pdf (source-range-83ecb080-01534))_
- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. _(javascriptallonge.pdf (source-range-83ecb080-01534))_
- Lists were represented as linked lists of cons cells, with each cell’s head pointing to an element and the tail pointing to another cons cell. _(javascriptallonge.pdf (source-range-83ecb080-01535))_
- Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-83ecb080-01536))_
- Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being the others), and computers in the late 1950s were extremely small and slow by today’s standards. _(javascriptallonge.pdf (source-range-83ecb080-01536))_
- Although the 704 used core memory, it still used vacuum tubes for its logic. _(javascriptallonge.pdf (source-range-83ecb080-01536))_
- Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-83ecb080-01536))_
- Here’s the scheme in JavaScript, using two-element arrays to represent cons cells: _(javascriptallonge.pdf (source-range-83ecb080-01537))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01530))_

> > 66Lisp is still very much alive, and one of the most interesting and exciting programming languages in use today is Clojure, a Lisp dialect that runs on the JVM, along with its sibling ClojureScript, Clojure that transpiles to JavaScript. 67https://en.wikipedia.org/wiki/IBM_704

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01533))_

> If you had two 15-bit values and wished to write them to the register, the CONS macro would take the values and write them to a 36-bit word.

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01537))_

> Here’s the scheme in JavaScript, using two-element arrays to represent cons cells:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01538))_

> **const** cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01539))_

> We can make a list by calling cons repeatedly, and terminating it with null:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01540))_

> **const** oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, **null** )))));
