---
page_id: javascriptallonge-recipe-the-kestrel-and-the-idiot
page_kind: recipe
page_family: recipe-pattern
summary: the kestrel and the idiot: reusable source-backed pattern with 6 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: the-kestrel-and-the-idiot
projection_coverage: recipe-javascriptallonge-recipe-the-kestrel-and-the-idiot@cedc725b02921377cf20dd41dee12110
---

# the kestrel and the idiot

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-the-kestrel-and-the-idiot-868e3ae2]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- You give it a value, and it returns a constant function that gives that value. _(javascriptallonge.pdf (source-range-7239e085-01338))_
- A constant function is a function that always returns the same thing, no matter what you give it. _(javascriptallonge.pdf (source-range-7239e085-01338))_
- The kestrel, or K , is a function that makes constant functions. _(javascriptallonge.pdf (source-range-7239e085-01338))_
- The identity function is a function that evaluates to whatever parameter you pass it. _(javascriptallonge.pdf (source-range-7239e085-01341))_
- Given two values, we can say that K always returns the first value: K(x)(y) => x (that's not valid JavaScript, but it's essentially how it works). _(javascriptallonge.pdf (source-range-7239e085-01344))_
- Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value. _(javascriptallonge.pdf (source-range-7239e085-01352))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01340)_

```
const K = (x) => (y) => x;
const fortyTwo = K(42);
fortyTwo(6)
//=> 42
fortyTwo("Hello")
//=> 42
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01343)_

```
K(6)(7)
//=> 6
K(12)(24)
//=> 12
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01346)_

```
Therefore, K(I)(x)(y) => y:
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01347)_

```
K(I)(6)(7)
//=> 7
K(I)(12)(24)
//=> 24
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01349)_

```
K("primus")("secundus")
//=> "primus"
K(I)("primus")("secundus")
//=> "secundus"
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01351)_

```
const first = K,
second = K(I);
first("primus")("secundus")
//=> "primus"
second("primus")("secundus")
//=> "secundus"
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-the-kestrel-and-the-idiot-868e3ae2]]
