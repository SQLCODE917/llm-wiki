---
page_id: javascriptallonge-will-be-represented-as
page_kind: source
summary: Will be represented as: from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.277-278
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

In the 'Will be represented as' section, the author introduces the notation for keys and the use of POJOs to map positions to moves in the context of a game board representation.

## Key supported claims

- We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string (raw/javascriptallonge.pdf p.277-278).
- We can use a POJO to make a map from positions to moves (raw/javascriptallonge.pdf p.277-278).

## Technical details

### `technical-atom-b191d18ddd564c69` code

Citation: (raw/javascriptallonge.pdf p.277-278)

```
[ 'o', 'x', ' ', 'x', ' ', ' ', 'o', ' ', ' ' ]
```

### `technical-atom-56a7813dc99d4303` code

Citation: (raw/javascriptallonge.pdf p.277-278)

```javascript
const moveLookupTable = { [[ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]]: 0, [[ 'o', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]]: 6, [[ 'o', 'x', 'x', ' ', ' ', ' ', 'o', ' ', ' ' ]]: 3, [[ 'o', 'x', ' ', 'x', ' ', ' ', 'o', ' ', ' ' ]]: 8, [[ 'o', 'x', ' ', ' ', 'x', ' ', 'o', ' ', ' '
```

### `technical-atom-0ee8bb8c9b92f422` code

Citation: (raw/javascriptallonge.pdf p.277-278)

```
]]: 3, [[ 'o', 'x', ' ', ' ', ' ', 'x', 'o', ' ', ' ' ]]: 3, [[ 'o', 'x', ' ', ' ', ' ', ' ', 'o', 'x', ' ' ]]: 3, [[ 'o', 'x', ' ', ' ', ' ', ' ', 'o', ' ', 'x' ]]: 3 // ... };
```

## Related technical details

### From [[javascriptallonge-the-carpenter-s-solution]]: `technical-atom-4447f89fa1fdcec5` code

Relation: nearby source page; matched terms `board`, `game`

Citation: (raw/javascriptallonge.pdf p.264-269)

```javascript
Math.floor(Math.random() * size), Math.floor(Math.random() * size) ]; return {board, position}; }; const Game = ({board, position}) => { const size = board[0].length; return ({ *[Symbol.iterator] () { let [x, y] = position; while (x >= 0 && y >=0 && x < size && y < size) { const direction = board[y][x]; yield direction; [x, y] = MOVE[direction]([x, y]); } } }); };
```

### From [[javascriptallonge-the-carpenter-s-solution]]: `technical-atom-38c104b7ffd476a8` code

Relation: nearby source page; matched terms `board`, `game`

Citation: (raw/javascriptallonge.pdf p.264-269)

```javascript
const terminates = (game) => tortoiseAndHare(positionsOf(game)) const test = [ ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿","￿","￿","￿"] ]; terminates(Game({board: test, position: [0, 0]})) //=> false terminates(Game({board: test, position: [3, 0]})) //=> true terminates(Game({board: test, position: [0, 3]})) //=> false terminates(Game({board: test, position: [3, 3]})) //=> false
```
