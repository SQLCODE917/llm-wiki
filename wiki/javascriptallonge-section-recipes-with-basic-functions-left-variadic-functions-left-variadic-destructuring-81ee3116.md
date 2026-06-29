---
page_id: javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-left-variadic-destructuring-81ee3116
page_kind: source
summary: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring: 7 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-left-variadic-destructuring-81ee3116@3eedb327c2f81261c8ab9812ba5e860a
---

# Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-d00f2bc0]] - broader source section: Recipes with Basic Functions / Left-Variadic Functions

## Statements

- Gathering arguments for functions is one of the ways JavaScript can destructure arrays. Another way is when assigning variables, like this: _(javascriptallonge.pdf (source-range-7239e085-00741))_
- But we can write our own left-gathering function utility using the same principles without all the tedium: _(javascriptallonge.pdf (source-range-7239e085-00747))_
- With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function. _(javascriptallonge.pdf (source-range-7239e085-00749))_

## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00747))_

> But we can write our own left-gathering function utility using the same principles without all the tedium:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00742))_

```
const [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid'];
first
//=> 'why'
butFirst
//=> ["hello","there","little","droid"]
```

### Technical frame 2: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00747))_

> But we can write our own left-gathering function utility using the same principles without all the tedium:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00744))_

```
const [...butLast, last] = ['why', 'hello', 'there', 'little', 'droid'];
//=> Unexpected token
```

### Technical frame 3: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00747))_

> But we can write our own left-gathering function utility using the same principles without all the tedium:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00746))_

```
const [butLast, last] = leftVariadic((butLast, last) => [butLast, last])(...['wh\
y', 'hello', 'there', 'little', 'droid']);
butLast
//=> ['why', 'hello', 'there', 'little']
last
//=> 'droid'
```

### Technical frame 4: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00749))_

> With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00748))_

```
const leftGather = (outputArrayLength) => {
return function (inputArray) {
return [inputArray.slice(0, inputArray.length - outputArrayLength + 1)].conc\
at(
inputArray.slice(inputArray.length - outputArrayLength + 1)
)
}
};
const [butLast, last] = leftGather(2)(['why', 'hello', 'there', 'little', 'droid\
']);
butLast
//=> ['why', 'hello', 'there', 'little']
last
//=> 'droid'
```
