---
page_id: javascriptallonge-recipe-left-variadic-destructuring
page_kind: recipe
page_family: recipe-pattern
summary: left-variadic destructuring: reusable source-backed pattern with 2 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: left-variadic-destructuring
projection_coverage: recipe-javascriptallonge-recipe-left-variadic-destructuring@1118ff04d63d7b6c2862a0d7b53477a9
---

# left-variadic destructuring

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-left-variadic-destructuring-81ee3116]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- Gathering arguments for functions is one of the ways JavaScript can destructure arrays. _(javascriptallonge.pdf (source-range-7239e085-00741))_
- With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function. _(javascriptallonge.pdf (source-range-7239e085-00749))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00742)_

```
const [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid'];
first
//=> 'why'
butFirst
//=> ["hello","there","little","droid"]
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00744)_

```
const [...butLast, last] = ['why', 'hello', 'there', 'little', 'droid'];
//=> Unexpected token
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00746)_

```
const [butLast, last] = leftVariadic((butLast, last) => [butLast, last])(...['wh\
y', 'hello', 'there', 'little', 'droid']);
butLast
//=> ['why', 'hello', 'there', 'little']
last
//=> 'droid'
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00748)_

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

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-left-variadic-destructuring-81ee3116]]
