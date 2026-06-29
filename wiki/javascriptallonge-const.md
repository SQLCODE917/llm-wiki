---
page_id: javascriptallonge-const
page_kind: concept
summary: Const: 4 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-const@0c12b6c843b5dd74bd397633876e8990
---

# Const

What [[javascriptallonge]] covers about const:

## Statements

### const and lexical scope

- This seems very straightforward, but alas, there are some semantics of binding names that we need to understand if we're to place const anywhere we like. The first thing to ask ourselves is, what happens if we use const to bind two different values to the 'same' name? _(javascriptallonge.pdf (source-range-8eb13d6b-00451))_

- Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-8eb13d6b-00465))_

### mixing let and const

- Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And: _(javascriptallonge.pdf (source-range-8eb13d6b-01182))_

- Shadowing a const with a let does not permit it to be rebound in its original scope. _(javascriptallonge.pdf (source-range-8eb13d6b-01184))_


## Technical atoms

### Technical frame 1: const and lexical scope

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00465))_

> Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00464))_

```
((diameter_fn) => { const PI = 3; return diameter_fn(2) })( (() => { const PI = 3.14159265; return (diameter) => diameter * PI })() ) //=> 6.2831853
```

### Technical frame 2: mixing let and const

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01182))_

> Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01181))_

```
(() => { let age = 49; if ( true ) { const age = 50; } age = 51; return age; })() //=> 51
```

### Technical frame 3: mixing let and const

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01184))_

> Shadowing a const with a let does not permit it to be rebound in its original scope.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01183))_

```
(() => { const age = 49; if ( true ) { let age = 50; } age = 52; return age; })() //=> ERROR: age is read-only
```


## Related pages

- [[javascriptallonge-bind]] - shared statements: Bind shares source evidence from const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. (1 shared statement(s))
- [[javascriptallonge-binding]] - shared statements: Binding shares source evidence from const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. (1 shared statement(s))
- [[javascriptallonge-parameter]] - shared statements: Parameter shares source evidence from const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. (1 shared statement(s))
- [[javascriptallonge-value]] - shared statements: Value shares source evidence from const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. (1 shared statement(s))
- [[javascriptallonge-section-const-a93a8dff]] - source section: const shares source evidence from const: Another way to write our 'circumference' function would be to pass PI along with the diameter argument, something like this:; const shares technical record from const: (diameter, PI) => diameter * PI (11 shared statement(s), 10 shared atom(s))

## Source

- [[javascriptallonge]]
