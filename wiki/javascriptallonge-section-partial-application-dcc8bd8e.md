---
page_id: javascriptallonge-section-partial-application-dcc8bd8e
page_kind: source
summary: **Partial Application**: 12 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-partial-application-dcc8bd8e@86d4fc40f7b13302f0f2d5e51e721ab0
---

# **Partial Application**

From [[javascriptallonge]].

## Statements

- This is such a common tool that many libraries provide some form of partial application. _(javascriptallonge.pdf (source-range-83ecb080-00931))_
- In Building Blocks, we discussed partial application, but we didn’t write a generalized recipe for it. _(javascriptallonge.pdf (source-range-83ecb080-00931))_
- These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost.[48] If you want to bind more than one argument, or you want to leave a “hole” in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. _(javascriptallonge.pdf (source-range-83ecb080-00932))_
- As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware. _(javascriptallonge.pdf (source-range-83ecb080-00940))_
- We’d need a different recipe if we wish to create partial applications of object methods. _(javascriptallonge.pdf (source-range-83ecb080-00940))_
- > 48 callFirst and callLast were inspired by Michael Fogus’ Lemonad. _(javascriptallonge.pdf (source-range-83ecb080-00944))_
- We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument: _(javascriptallonge.pdf (source-range-83ecb080-00947))_

## Technical atoms

> Context: These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost.[48] If you want to bind more than one argument, or you want to leave a “hole” in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic.
_(context: javascriptallonge.pdf (source-range-83ecb080-00932))_

> **const** heliosSaysHello = callFirst(greet, 'Helios');
_(source: javascriptallonge.pdf (source-range-83ecb080-00934))_

> **const** sayHelloToCeline = callLast(greet, 'Celine');
_(source: javascriptallonge.pdf (source-range-83ecb080-00937))_

> Context: We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument:
_(context: javascriptallonge.pdf (source-range-83ecb080-00947))_

> **const** callLeft = (fn, ...args) =>
_(source: javascriptallonge.pdf (source-range-83ecb080-00948))_

> Context: We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument:
_(context: javascriptallonge.pdf (source-range-83ecb080-00947))_

> (...remainingArgs) => fn(...args, ...remainingArgs);
_(source: javascriptallonge.pdf (source-range-83ecb080-00949))_

> Context: We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument:
_(context: javascriptallonge.pdf (source-range-83ecb080-00947))_

> **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
_(source: javascriptallonge.pdf (source-range-83ecb080-00950))_
