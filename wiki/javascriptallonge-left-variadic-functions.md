---
page_id: javascriptallonge-left-variadic-functions
page_kind: source
summary: Left-Variadic Functions from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.89-90
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé discusses variadic functions and the limitations of JavaScript's variadic function syntax, specifically that gathering parameters are only allowed from the end of the parameter list.

## Key supported claims

- A variadic function is a function that is designed to accept a variable number of arguments. (raw/javascriptallonge.pdf p.89-90)
- In JavaScript, you can make a variadic function by gathering parameters. For example, a function can gather the last arguments into an array using the spread operator. (raw/javascriptallonge.pdf p.89-90)
- 52 English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. But can they be 'variary?' No! They have to be 'variadic.' (raw/javascriptallonge.pdf p.89-90)

## Technical details

### `technical-atom-f75503e6cfc8b5da` code

Citation: (raw/javascriptallonge.pdf p.89-90)

```javascript
const abccc = (a, b, ...c) => { console.log(a); console.log(b); console.log(c); }; abccc(1, 2, 3, 4, 5) 1 2 [3,4,5]
```

### `technical-atom-dd2d68c5c58871a9` code

Citation: (raw/javascriptallonge.pdf p.89-90)

```javascript
function team(coach, captain, ...players) { console.log(` ${ captain } (captain)`); for ( let player of players) { console.log(player); } console.log(`squad coached by ${ coach } `); } team('Luis Enrique', 'Xavi Hernández', 'Marc-André ter Stegen', 'Martín Montoya', 'Gerard Piqué') //=> Xavi Hernández (captain) Marc-André ter Stegen Martín Montoya Gerard Piqué squad coached by Luis Enrique But we can't go the other way around:
```

### `technical-atom-6282a9bd1e49a353` code

Citation: (raw/javascriptallonge.pdf p.89-90)

```javascript
function team2(...players, captain, coach) { console.log(` ${ captain } (captain)`); for ( let player of players) { console.log(player); } console.log(`squad coached by ${ coach } `); } //=> Unexpected token
```

### `technical-atom-9bf75248160dbe49` worked-example

Citation: (raw/javascriptallonge.pdf p.89-90)

For example, we might want to have a function that builds some kind of team record.

### `technical-atom-788752f4a1e82bb0` exception

Citation: (raw/javascriptallonge.pdf p.89-90)

ECMAScript 2015 only permits gathering parameters from the end of the parameter list.
