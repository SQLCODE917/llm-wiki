---
page_id: javascriptallonge-recipe-overcoming-limitations
page_kind: recipe
page_family: recipe-pattern
summary: overcoming limitations: reusable source-backed pattern with 3 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: overcoming-limitations
projection_coverage: recipe-javascriptallonge-recipe-overcoming-limitations@cbd16b1e3a56c1d09720739ac41cdb7b
---

# overcoming limitations

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-overcoming-limitations-96b730f4]].
- Evidence roles: decision, constraint, procedure, example.

## Applicability And Rationale

- All left-variadic functions have one or more fixed arguments, and the rest are gathered into the leftmost argument. _(javascriptallonge.pdf (source-range-7239e085-00735))_
- We sure can, by using the techniques from rightVariadic . _(javascriptallonge.pdf (source-range-7239e085-00736))_
- Our leftVariadic function is a decorator that turns any function into a function that gathers parameters from the left , instead of from the right. _(javascriptallonge.pdf (source-range-7239e085-00739))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00734)_

```
const butLastAndLast = (...butLast, last) =>
[butLast, last];
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00737)_

```
const leftVariadic = (fn) => {
if (fn.length < 1) {
return fn;
}
else {
return function (...args) {
const gathered = args.slice(0, args.length - fn.length + 1),
spread
= args.slice(args.length - fn.length + 1);
return fn.apply(
this, [gathered].concat(spread)
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00738)_

```
);
}
}
};
const butLastAndLast = leftVariadic((butLast, last) => [butLast, last]);
butLastAndLast('why', 'hello', 'there', 'little', 'droid')
//=> [["why","hello","there","little"],"droid"]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-overcoming-limitations-96b730f4]]
