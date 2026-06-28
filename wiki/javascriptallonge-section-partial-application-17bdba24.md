---
page_id: javascriptallonge-section-partial-application-17bdba24
page_kind: source
summary: Partial Application: 6 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-partial-application-17bdba24@8428b4f82f837170c8f0a7d4a7a73afe
---

# Partial Application

From [[javascriptallonge]].

## Statements

- Recipes with Basic Functions

57

## **Partial Application**

In Building Blocks, we discussed partial application, but we didn’t write a generalized recipe for it. This is such a common tool that many libraries provide some form of partial application. You’ll find examples in Lemonad[45] from Michael Fogus, Functional JavaScript[46] from Oliver Steele and the terse but handy node-ap[47] from James Halliday.

These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost.[48] If you want to bind more than one argument, or you want to leave a “hole” in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic.

**const** callFirst = (fn, larg) => **function** (...rest) { **return** fn.call( **this** , larg, ...rest); } **const** callLast = (fn, rarg) => **function** (...rest) { **return** fn.call( **this** , ...rest, rarg); } **const** greet = (me, you) => `Hello, **${** you **}** , my name is **${** me **}** `; **const** heliosSaysHello = callFirst(greet, 'Helios'); heliosSaysHello('Eartha') _//=> 'Hello, Eartha, my name is Helios'_ **const** sayHelloToCeline = callLast(greet, 'Celine'); sayHelloToCeline('Eartha') _//=> 'Hello, Celine, my name is Eartha'_ As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware. We’d need a different recipe if we wish to create partial applications of object methods.

> 45https://github.com/fogus/lemonad

> 46http://osteele.com/sources/javascript/functional/

> 47https://github.com/substack/node-ap

> 48 callFirst and callLast were inspired by Michael Fogus’ Lemonad. Thanks! _(javascriptallonge.pdf (source-range-83ecb080-00099))_
- 58

Recipes with Basic Functions

We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument: **const** callLeft = (fn, ...args) =>

(...remainingArgs) => fn(...args, ...remainingArgs); **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); _(javascriptallonge.pdf (source-range-83ecb080-00100))_
