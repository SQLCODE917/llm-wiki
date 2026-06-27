---
page_id: javascriptallonge-section-left-variadic-destructuring-b0fc3cbc
page_kind: source
summary: **left-variadic destructuring**: 8 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-left-variadic-destructuring-b0fc3cbc@273ced007312dd4c1a193864d8006159
---

# **left-variadic destructuring**

From [[javascriptallonge]].

## Statements

- Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. _(javascriptallonge.pdf (source-range-83ecb080-01074))_
- But we can write our own left-gathering function utility using the same principles without all the tedium: _(javascriptallonge.pdf (source-range-83ecb080-01084))_
- With leftGather, we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function. _(javascriptallonge.pdf (source-range-83ecb080-01086))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01074))_

> Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. Another way is when assigning variables, like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01075))_

> **const** [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid'];

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01074))_

> Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. Another way is when assigning variables, like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01076))_

> first _//=> 'why'_ butFirst _//=> ["hello","there","little","droid"]_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01077))_

> As with parameters, we can’t gather values from the left when destructuring an array:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01078))_

> **const** [...butLast, last] = ['why', 'hello', 'there', 'little', 'droid']; _//=> Unexpected token_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01079))_

> We could use leftVariadic the hard way:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01082))_

> **const** [butLast, last] = leftVariadic((butLast, last) => [butLast, last])(...['wh\ y', 'hello', 'there', 'little', 'droid']);

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01083))_

> butLast _//=> ['why', 'hello', 'there', 'little']_ last _//=> 'droid'_
