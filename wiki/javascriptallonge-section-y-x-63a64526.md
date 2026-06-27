---
page_id: javascriptallonge-section-y-x-63a64526
page_kind: source
summary: (y) => x: 9 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-y-x-63a64526@c44e9f81a8ab9b374c1b907e96590d15
---

# (y) => x

From [[javascriptallonge]].

## Statements

- So now we have a value representing that function. _(javascriptallonge.pdf (source-range-83ecb080-00477))_
- Then we’re going to take the value of that function and apply it to the argument 2, something like this: _(javascriptallonge.pdf (source-range-83ecb080-00477))_
- There is no x in its environment, it must come from somewhere else. _(javascriptallonge.pdf (source-range-83ecb080-00479))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from “outside” of a function that are referenced inside a function. _(javascriptallonge.pdf (source-range-83ecb080-00480))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from “outside” of a function that are referenced inside a function. _(javascriptallonge.pdf (source-range-83ecb080-00480))_
- Now let’s enjoy a relaxed Allongé before we continue! _(javascriptallonge.pdf (source-range-83ecb080-00482))_
- Now let’s enjoy a relaxed Allongé before we continue! _(javascriptallonge.pdf (source-range-83ecb080-00482))_

## Technical atoms

> Context: So now we have a value representing that function. Then we’re going to take the value of that function and apply it to the argument 2, something like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-00477))_

> - ((y) => x)(2)
_(source: javascriptallonge.pdf (source-range-83ecb080-00478))_

> Context: This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from “outside” of a function that are referenced inside a function. For example, here’s the equivalent code in Ruby:
_(context: javascriptallonge.pdf (source-range-83ecb080-00480))_

> lambda { |x| lambda { |y| x } }[1][2] _#=> 1_
_(source: javascriptallonge.pdf (source-range-83ecb080-00481))_
