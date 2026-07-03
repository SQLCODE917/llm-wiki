---
page_id: javascriptallonge-recipe-maybe
page_kind: recipe
page_family: recipe-pattern
summary: Maybe: reusable source-backed pattern with 6 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: maybe
projection_coverage: recipe-javascriptallonge-recipe-maybe@b03757f25483a4388fa4ad90ea4559c6
---

# Maybe

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-basic-functions-maybe-bddfd1b7]].
- Evidence roles: decision, constraint, example, structured-state.

## Applicability And Rationale

- Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-7239e085-00695))_
- A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'something'). _(javascriptallonge.pdf (source-range-7239e085-00695))_
- This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing: _(javascriptallonge.pdf (source-range-7239e085-00696))_
- Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing: _(javascriptallonge.pdf (source-range-7239e085-00698))_
- Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation: _(javascriptallonge.pdf (source-range-7239e085-00700))_
- If some code ever tries to call model.setSomething with nothing, the operation will be skipped. _(javascriptallonge.pdf (source-range-7239e085-00708))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00697)_

```
const isSomething = (value) =>
value !== null && value !== void 0;
const checksForSomething = (value) => {
if (isSomething(value)) {
// function's true logic
}
}
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00699)_

```
var something =
isSomething(value)
? doesntCheckForSomething(value)
: value;
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00701)_

```
const maybe = (fn) =>
function (...args) {
if (args.length === 0) {
return
}
else {
for (let arg of args) {
if (arg == null) return;
}
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00703)_

```
return fn.apply(this, args)
}
}
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00705)_

```
maybe((a, b, c) => a + b + c)(1, 2, 3)
//=> 6
maybe((a, b, c) => a + b + c)(1, null, 3)
//=> undefined
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00707)_

```
function Model () {};
Model.prototype.setSomething = maybe(function (value) {
this.something = value;
});
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-basic-functions-maybe-bddfd1b7]]
