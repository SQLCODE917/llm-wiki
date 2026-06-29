---
page_id: javascriptallonge-section-recipes-with-basic-functions-tap-904019d9
page_kind: source
summary: Recipes with Basic Functions / Tap: 7 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-tap-904019d9@50e88e12111b2949ee8d17ee672ca3cb
---

# Recipes with Basic Functions / Tap

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-recipes-with-basic-functions-c9137465]] - broader source section: Recipes with Basic Functions

## Statements

- It has some surprising applications. One is when you want to do something with a value for sideeffects, but keep the value around. Behold: _(javascriptallonge.pdf (source-range-7239e085-00685))_
- tap is a traditional name borrowed from various Unix shell commands. It takes a value and returns a function that always returns the value, but if you pass it a function, it executes the function for side-effects. Let's see it in action as a poor-man's debugger: _(javascriptallonge.pdf (source-range-7239e085-00687))_
- p.s. tap can do more than just act as a debugging aid. It's also useful for working with object and instance methods. _(javascriptallonge.pdf (source-range-7239e085-00693))_

## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Tap

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00685))_

> It has some surprising applications. One is when you want to do something with a value for sideeffects, but keep the value around. Behold:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00684))_

```
const K = (x) => (y) => x;
```

### Technical frame 2: Recipes with Basic Functions / Tap

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00687))_

> tap is a traditional name borrowed from various Unix shell commands. It takes a value and returns a function that always returns the value, but if you pass it a function, it executes the function for side-effects. Let's see it in action as a poor-man's debugger:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00686))_

```
const tap = (value) =>
(fn) => (
typeof(fn) === 'function' && fn(value),
value
)
```

### Technical frame 3: Recipes with Basic Functions / Tap

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00693))_

> p.s. tap can do more than just act as a debugging aid. It's also useful for working with object and instance methods.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00691))_

```
const tap = (value, fn) => {
const curried = (fn) => (
typeof(fn) === 'function' && fn(value),
value
);
return fn === undefined
? curried
: curried(fn);
}
Now we can write:
tap('espresso')((it) => {
console.log(`Our drink is '${it}'`)
});
//=> Our drink is 'espresso'
'espresso'
Or:
tap('espresso', (it) => {
console.log(`Our drink is '${it}'`)
});
//=> Our drink is 'espresso'
'espresso'
```
