---
page_id: javascriptallonge-section-values-are-expressions-left-variadic-functions-left-variadic-destructuring-dce6d892
page_kind: source
summary: values are expressions / Left-Variadic Functions / left-variadic destructuring: 3 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-left-variadic-functions-left-variadic-destructuring-dce6d892@9b745c7021585bfc0f9bd0abad30e7ee
---

# values are expressions / Left-Variadic Functions / left-variadic destructuring

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-left-variadic-functions-547e4e7a]] - broader source section

## Statements

- Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. _(javascriptallonge.pdf (source-range-83ecb080-00747))_
- Recipes with Basic Functions **const** [butLast, last] = leftVariadic((butLast, last) => [butLast, last])(...['wh\ y', 'hello', 'there', 'little', 'droid']); butLast _//=> ['why', 'hello', 'there', 'little']_ last _//=> 'droid'_ But we can write our own left-gathering function utility using the same principles without all the tedium: **const** leftGather = (outputArrayLength) => { **return function** (inputArray) { **return** [inputArray.slice(0, inputArray.length - outputArrayLength + 1)].conc\ at( inputArray.slice(inputArray.length - outputArrayLength + 1) ) } }; **const** [butLast, last] = leftGather(2)(['why', 'hello', 'there', 'little', 'droid\ ']); butLast _//=> ['why', 'hello', 'there', 'little']_ last _//=> 'droid'_ _(javascriptallonge.pdf (source-range-83ecb080-00750))_
- With leftGather, we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function. _(javascriptallonge.pdf (source-range-83ecb080-00751))_
