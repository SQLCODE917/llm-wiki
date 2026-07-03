---
page_id: javascriptallonge-recipe-partial-application-583028a8
page_kind: recipe
page_family: recipe-pattern
summary: Partial Application: reusable source-backed pattern with 4 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: partial-application
projection_coverage: recipe-javascriptallonge-recipe-partial-application-583028a8@861b216fe0888cbf6df03f56ca7e29ce
---

# Partial Application

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-basic-functions-partial-application-583028a8]].
- Evidence roles: decision, constraint, procedure, example, structured-state.

## Applicability And Rationale

- 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. _(javascriptallonge.pdf (source-range-7239e085-00660))_
- These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. _(javascriptallonge.pdf (source-range-7239e085-00660))_
- We'd need a different recipe if we wish to create partial applications of object methods. _(javascriptallonge.pdf (source-range-7239e085-00662))_
- We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument: _(javascriptallonge.pdf (source-range-7239e085-00665))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00661)_

```
const callFirst = (fn, larg) =>
function (...rest) {
return fn.call(this, larg, ...rest);
}
const callLast = (fn, rarg) =>
function (...rest) {
return fn.call(this, ...rest, rarg);
}
const greet = (me, you) =>
`Hello, ${you}, my name is ${me}`;
const heliosSaysHello = callFirst(greet, 'Helios');
heliosSaysHello('Eartha')
//=> 'Hello, Eartha, my name is Helios'
const sayHelloToCeline = callLast(greet, 'Celine');
sayHelloToCeline('Eartha')
//=> 'Hello, Celine, my name is Eartha'
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00666)_

```
const callLeft = (fn, ...args) =>
(...remainingArgs) =>
fn(...args, ...remainingArgs);
const callRight = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-basic-functions-partial-application-583028a8]]
