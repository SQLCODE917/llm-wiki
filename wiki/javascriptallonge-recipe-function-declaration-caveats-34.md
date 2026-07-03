---
page_id: javascriptallonge-recipe-function-declaration-caveats-34
page_kind: recipe
page_family: recipe-pattern
summary: function declaration caveats 34: reusable source-backed pattern with 7 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: function-declaration-caveats-34
projection_coverage: recipe-javascriptallonge-recipe-function-declaration-caveats-34@0a0f0d1c73cefc891c6a190c2af4bf6d
---

# function declaration caveats 34

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-naming-functions-function-declaration-caveats-34-01e57464]].
- Evidence roles: decision, explanation, constraint, procedure, example, structured-state.

## Applicability And Rationale

- Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-7239e085-00548))_
- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. _(javascriptallonge.pdf (source-range-7239e085-00548))_
- 34 A number of the caveats discussed here were described in Jyrly Zaytsev's excellent article Named function expressions demystified. _(javascriptallonge.pdf (source-range-7239e085-00549))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-7239e085-00551))_
- The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. _(javascriptallonge.pdf (source-range-7239e085-00551))_
- Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. _(javascriptallonge.pdf (source-range-7239e085-00552))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00550)_

```
(function (camelCase) {
return fizzbuzz();
if (camelCase) {
function fizzbuzz () {
return "Fizz" + "Buzz";
}
}
else {
function fizzbuzz () {
return "Fizz" + "Buzz";
}
}
})(true)
//=> 'FizzBuzz'? Or ERROR: Can't find variable: fizzbuzz?
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00553)_

```
function trueDat () { return true }
But this is not:
(function trueDat () { return true })
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-naming-functions-function-declaration-caveats-34-01e57464]]
