---
page_id: javascriptallonge-feature
page_kind: concept
summary: Feature: 5 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-feature@a82ac0beecabfee03d5b64787bef7c36
---

# Feature

What [[javascriptallonge]] covers about feature:

## Statements

### why the 'six' edition?

- ECMAScript 2015 (formerly called ECMAScript 6 or 'ES6'), is ushering in a very large number of improvements to the way programmers can write small, powerful components and combine them into larger, fully featured programs. Features like destructuring, block-structured variables, iterables, generators, and the class keyword are poised to make JavaScript programming more expressive. _(javascriptallonge.pdf (source-range-31a4cf47-00021))_

- Working around the missing features was a necessary evil. _(javascriptallonge.pdf (source-range-31a4cf47-00033))_

- And presto, rest collects the rest of the arguments without a lot of malarky involving slicing arguments . Not having to work around these kinds of missing features makes JavaScript Allongé a better book , because it can focus on the why to do something and when to do it, instead of on the how to make it work _(javascriptallonge.pdf (source-range-31a4cf47-00038))_

### Foreword to the 'Six' edition

- A larger upgrade would substantially improve JavaScript, but without being as radical as ECMAScript 4. This upgrade became ECMAScript 6 (some features that were initially discussed will show up later, in upcoming ECMAScript versions). _(javascriptallonge.pdf (source-range-31a4cf47-00071))_

### void

- 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-31a4cf47-00249))_


## Technical atoms

### Technical frame 1: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00036))_

> And i is scoped to the for loop. We can also write:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00035))_

```
for ( let i = 0; i < array.length; ++i) { // ... }
```

### Technical frame 2: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00038))_

> And presto, rest collects the rest of the arguments without a lot of malarky involving slicing arguments . Not having to work around these kinds of missing features makes JavaScript Allongé a better book , because it can focus on the why to do something and when to do it, instead of on the how to make it work

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00037))_

```
function foo (first, ...rest) { // ... }
```

### Technical frame 3: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00250))_

```
(() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined
```

### Technical frame 4: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00251))_

> So how do we get a function that evaluates a block to return a value when applied?


## Related pages

- [[javascriptallonge-ecmascript]] - shared statements and technical atoms: Ecmascript shares source evidence from Foreword to the 'Six' edition: A larger upgrade would substantially improve JavaScript, but without being as radical as ECMAScript 4. This upgrade became ECMAScript 6 (some features that were init ... [truncated]; Ecmascript shares technical record from why the 'six' edition?: for ( let i = 0; i < array.length; ++i) { // ... } (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from why the 'six' edition?: for ( let i = 0; i < array.length; ++i) { // ... } (4 shared atom(s))
- [[javascriptallonge-program]] - shared technical atoms: Program shares technical record from why the 'six' edition?: for ( let i = 0; i < array.length; ++i) { // ... } (3 shared atom(s))
- [[javascriptallonge-programmer]] - shared technical atoms: Programmer shares technical record from why the 'six' edition?: for ( let i = 0; i < array.length; ++i) { // ... } (3 shared atom(s))
- [[javascriptallonge-code]] - shared technical atoms: Code shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared atom(s))
- [[javascriptallonge-follow]] - shared technical atoms: Follow shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared atom(s))
- [[javascriptallonge-language]] - shared technical atoms: Language shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared atom(s))
- [[javascriptallonge-rule]] - shared technical atoms: Rule shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms: Write shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared atom(s))
- [[javascriptallonge-allong]] - shared technical atoms: Allong shares technical record from why the 'six' edition?: function foo (first, ...rest) { // ... } (1 shared atom(s))
- [[javascriptallonge-evaluating]] - shared technical atoms: Evaluating shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-result]] - shared technical atoms: Result shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-block]] - shared statements: Block shares source evidence from why the 'six' edition?: ECMAScript 2015 (formerly called ECMAScript 6 or 'ES6'), is ushering in a very large number of improvements to the way programmers can write small, powerful componen ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
