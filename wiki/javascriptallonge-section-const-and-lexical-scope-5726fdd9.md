---
page_id: javascriptallonge-section-const-and-lexical-scope-5726fdd9
page_kind: source
summary: **const and lexical scope**: 16 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-const-and-lexical-scope-5726fdd9@815356e0343b72e73ba57591ac81b732
---

# **const and lexical scope**

From [[javascriptallonge]].

## Statements

- This seems very straightforward, but alas, there are some semantics of binding names that we need to understand if we’re to place const anywhere we like. _(javascriptallonge.pdf (source-range-83ecb080-00623))_
- We can use any expression in there, and that expression can invoke diameter_fn. _(javascriptallonge.pdf (source-range-83ecb080-00627))_
- It’s more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we’ve elided. _(javascriptallonge.pdf (source-range-83ecb080-00627))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2), PI _is_ bound when we evaluated (diameter) => diameter * PI, and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn. _(javascriptallonge.pdf (source-range-83ecb080-00631))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2), PI _is_ bound when we evaluated (diameter) => diameter * PI, and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn. _(javascriptallonge.pdf (source-range-83ecb080-00631))_
- This is called lexical scoping[31] , because we can discover where a name is bound by looking at the source code for the program. _(javascriptallonge.pdf (source-range-83ecb080-00632))_
- We can see that PI is bound in an environment surrounding (diameter) => diameter * PI, we don’t need to know where diameter_fn is invoked. _(javascriptallonge.pdf (source-range-83ecb080-00632))_
- This is called lexical scoping[31] , because we can discover where a name is bound by looking at the source code for the program. _(javascriptallonge.pdf (source-range-83ecb080-00632))_
- Although we have bound 3 to PI in the environment surrounding diameter_fn(2), the value that counts is 3.14159265, the value we bound to PI in the environment surrounding (diameter) _⇒_ diameter * PI. _(javascriptallonge.pdf (source-range-83ecb080-00635))_
- That much we can carefully work out from the way closures work. _(javascriptallonge.pdf (source-range-83ecb080-00636))_
- Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-83ecb080-00642))_

## Technical atoms

> Context: Here’s the second formulation of our diameter function, bound to a name using an IIFE:
_(context: javascriptallonge.pdf (source-range-83ecb080-00625))_

> ((diameter_fn) => _// ..._ )( ((PI) => (diameter) => diameter * PI )(3.14159265) )
_(source: javascriptallonge.pdf (source-range-83ecb080-00626))_

> Context: It’s more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we’ve elided. We can use any expression in there, and that expression can invoke diameter_fn. For example: This is called lexical scoping[31] , because we can discover where a name is bound by looking at the source code for the program. We can see that PI is bound in an environment surrounding (diameter) => diameter * PI, we don’t need to know where dia
_(context: javascriptallonge.pdf (source-range-83ecb080-00627, source-range-83ecb080-00632))_

> ((diameter_fn) => diameter_fn(2) )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00630))_

> Context: We can test this by deliberately creating a “conflict:”
_(context: javascriptallonge.pdf (source-range-83ecb080-00633))_

> ((diameter_fn) => ((PI) => diameter_fn(2) )(3) )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00634))_

> ((diameter_fn) => { **const** PI = 3;
_(source: javascriptallonge.pdf (source-range-83ecb080-00640))_

> **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => diameter * PI })() ) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00641))_
