---
page_id: javascriptallonge-section-left-variadic-destructuring-b0fc3cbc
page_kind: source
summary: **left-variadic destructuring**: 8 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-left-variadic-destructuring-b0fc3cbc@4ca77bb545f8c2b2a943b30975a7e1a8
---

# **left-variadic destructuring**

From [[javascriptallonge]].

## Statements

- Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. _(javascriptallonge.pdf (source-range-83ecb080-01074))_
- But we can write our own left-gathering function utility using the same principles without all the tedium: _(javascriptallonge.pdf (source-range-83ecb080-01084))_
- With leftGather, we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function. _(javascriptallonge.pdf (source-range-83ecb080-01086))_

## Technical atoms

> Context: Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. Another way is when assigning variables, like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-01074))_

> **const** [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid'];
_(source: javascriptallonge.pdf (source-range-83ecb080-01075))_

> Context: Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. Another way is when assigning variables, like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-01074))_

> first _//=> 'why'_ butFirst _//=> ["hello","there","little","droid"]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01076))_

> Context: As with parameters, we can’t gather values from the left when destructuring an array:
_(context: javascriptallonge.pdf (source-range-83ecb080-01077))_

> **const** [...butLast, last] = ['why', 'hello', 'there', 'little', 'droid']; _//=> Unexpected token_
_(source: javascriptallonge.pdf (source-range-83ecb080-01078))_

> Context: We could use leftVariadic the hard way:
_(context: javascriptallonge.pdf (source-range-83ecb080-01079))_

> **const** [butLast, last] = leftVariadic((butLast, last) => [butLast, last])(...['wh\ y', 'hello', 'there', 'little', 'droid']);
_(source: javascriptallonge.pdf (source-range-83ecb080-01082))_

> butLast _//=> ['why', 'hello', 'there', 'little']_ last _//=> 'droid'_
_(source: javascriptallonge.pdf (source-range-83ecb080-01083))_
