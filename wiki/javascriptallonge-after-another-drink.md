---
page_id: javascriptallonge-after-another-drink
page_kind: source
summary: after another drink from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.270-272
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

A narrative chapter where The Carpenter discusses cycle detection algorithms with an engineer named Kidu, focusing on the Tortoise and Hare algorithm and its variations, including a teleporting version and a set-based approach.

## Key supported claims

- Carpenter discusses cycle detection with Kidu (raw/javascriptallonge.pdf p.270-272).
- Tortoise and Hare requires two iterators (raw/javascriptallonge.pdf p.270-272).
- Kidu suggests Set-based algorithm (raw/javascriptallonge.pdf p.270-272).

## Technical details

### `technical-atom-6e2c2d6922880d19` code

Citation: (raw/javascriptallonge.pdf p.270-272)

```javascript
// implements Teleporting Tortoise // cycle detection algorithm. const hasCycle = (iterable) => { let iterator = iterable[Symbol.iterator](), teleportDistance = 1; while ( true ) { let {value, done} = iterator.next(), tortoise = value; if (done) return false ; for ( let i = 0; i < teleportDistance; ++i) { let {value, done} = iterator.next(), hare = value; if (done) return false ; if (tortoise === hare) return true ; } teleportDistance *= 2; } return false ; };
```

### `technical-atom-1e688bef8d11d23b` code

Citation: (raw/javascriptallonge.pdf p.270-272)

```javascript
const hasCycle = (orderedCollection) => { const visited = new Set(); for ( let element of orderedCollection) { if (visited.has(element)) { return true ; } visited.add(element); } return false ; };
```

### `technical-atom-83342acdf7dcbb2e` requirement

Citation: (raw/javascriptallonge.pdf p.270-272)

But I couldn't help but notice that your solution doesn't actually meet the stated requirements for a different reason:'

### `technical-atom-26c9d6f3641a1301` requirement

Citation: (raw/javascriptallonge.pdf p.270-272)

'The hasCycle function, a/k/a Tortoise and Hare, requires two separate iterators to do its job.

### `technical-atom-e1f278e2f1b9232c` requirement

Citation: (raw/javascriptallonge.pdf p.270-272)

I should have used a Teleporting Tortoise!'

### `technical-atom-308b9af683225b19` requirement

Citation: (raw/javascriptallonge.pdf p.270-272)

'You know, the requirement asked for a finite space algorithm, not a constant state algorithm.

### `technical-atom-e612122cc371a8f2` requirement

Citation: (raw/javascriptallonge.pdf p.270-272)

'I guess,' he allowed, 'It isn't always necessary to make a solution so awesome it would please the Ghosts of Mars.'
