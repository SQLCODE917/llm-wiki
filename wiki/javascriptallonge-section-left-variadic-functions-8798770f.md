---
page_id: javascriptallonge-section-left-variadic-functions-8798770f
page_kind: source
summary: Left-Variadic Functions: 11 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-left-variadic-functions-8798770f@bb7eb5c553d0566c7a6ae62420bf0c66
---

# Left-Variadic Functions

From [[javascriptallonge]].

## Statements

- A variadic function is a function that is designed to accept a variable number of arguments. 52 In JavaScript, you can make a variadic function by gathering parameters. For example: _(javascriptallonge.pdf (source-range-31a4cf47-00717))_
- This can be useful when writing certain kinds of destructuring algorithms. For example, we might want to have a function that builds some kind of team record. It accepts a coach, a captain, and an arbitrary number of players. Easy in ECMAScript 2015: _(javascriptallonge.pdf (source-range-31a4cf47-00719))_
- 52 English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. But can they be 'variary?' No! They have to be 'variadic.' _(javascriptallonge.pdf (source-range-31a4cf47-00721))_
- ECMAScript 2015 only permits gathering parameters from the end of the parameter list. Not the beginning. What to do? _(javascriptallonge.pdf (source-range-31a4cf47-00723))_
- For example, we might want to have a function that builds some kind of team record. _(javascriptallonge.pdf (source-range-31a4cf47-00719))_
- ECMAScript 2015 only permits gathering parameters from the end of the parameter list. _(javascriptallonge.pdf (source-range-31a4cf47-00723))_

## Technical atoms

### Technical frame 1: Left-Variadic Functions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00719))_

> This can be useful when writing certain kinds of destructuring algorithms. For example, we might want to have a function that builds some kind of team record. It accepts a coach, a captain, and an arbitrary number of players. Easy in ECMAScript 2015:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00718))_

```
const abccc = (a, b, ...c) => { console.log(a); console.log(b); console.log(c); }; abccc(1, 2, 3, 4, 5) 1 2 [3,4,5]
```

### Technical frame 2: Left-Variadic Functions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00721))_

> 52 English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. But can they be 'variary?' No! They have to be 'variadic.'

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00720))_

```
function team(coach, captain, ...players) { console.log(` ${ captain } (captain)`); for ( let player of players) { console.log(player); } console.log(`squad coached by ${ coach } `); } team('Luis Enrique', 'Xavi Hernández', 'Marc-André ter Stegen', 'Martín Montoya', 'Gerard Piqué') //=> Xavi Hernández (captain) Marc-André ter Stegen Martín Montoya Gerard Piqué squad coached by Luis Enrique But we can't go the other way around:
```

### Technical frame 3: Left-Variadic Functions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00723))_

> ECMAScript 2015 only permits gathering parameters from the end of the parameter list. Not the beginning. What to do?

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00722))_

```
function team2(...players, captain, coach) { console.log(` ${ captain } (captain)`); for ( let player of players) { console.log(player); } console.log(`squad coached by ${ coach } `); } //=> Unexpected token
```
