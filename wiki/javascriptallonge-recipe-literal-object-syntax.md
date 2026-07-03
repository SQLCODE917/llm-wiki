---
page_id: javascriptallonge-recipe-literal-object-syntax
page_kind: recipe
page_family: recipe-pattern
summary: literal object syntax: reusable source-backed pattern with 6 statement(s) and 10 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: literal-object-syntax
projection_coverage: recipe-javascriptallonge-recipe-literal-object-syntax@0f3f37edf5441b96b3ab39e34359ed86
---

# literal object syntax

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-plain-old-javascript-objects-literal-object-syntax-205c8f77]].
- Evidence roles: decision, explanation, constraint, procedure, example.

## Applicability And Rationale

- JavaScript has a literal syntax for creating objects. _(javascriptallonge.pdf (source-range-7239e085-01073))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-7239e085-01077))_
- Names needn't be alphanumeric strings. _(javascriptallonge.pdf (source-range-7239e085-01079))_
- If the name is an alphanumeric string conforming to the same rules as names of variables, there's a simplified syntax for accessing the values: _(javascriptallonge.pdf (source-range-7239e085-01081))_
- Expressions can be used for keys as well. _(javascriptallonge.pdf (source-range-7239e085-01083))_
- It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords: _(javascriptallonge.pdf (source-range-7239e085-01091))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01074)_

```
{ year: 2012, month: 6, day: 14 }
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01076)_

```
{ year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 }
//=> false
Objects use [] to access the values by name, using a string:
{ year: 2012, month: 6, day: 14 }['day']
//=> 14
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01078)_

```
const unique = () => [],
x = unique(),
y = unique(),
z = unique(),
o = { a: x, b: y, c: z };
o['a'] === x && o['b'] === y && o['c'] === z
//=> true
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01080)_

```
{ 'first name': 'reginald', 'last name': 'lewis' }['first name']
//=> 'reginald'
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01082)_

```
const date = { year: 2012, month: 6, day: 14 };
date['day'] === date.day
//=> true
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01084)_

```
{
["p" + "i"]: 3.14159265
}
//=> {"pi":3.14159265}
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-plain-old-javascript-objects-literal-object-syntax-205c8f77]]
