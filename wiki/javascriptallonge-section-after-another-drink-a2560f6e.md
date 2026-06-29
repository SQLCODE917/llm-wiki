---
page_id: javascriptallonge-section-after-another-drink-a2560f6e
page_kind: source
summary: after another drink: 8 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-after-another-drink-a2560f6e@fee3c23147e5d6ea56d44229aa71a225
---

# after another drink

From [[javascriptallonge]].

## Statements

- A few drinks later, The Carpenter was telling his Thing story and an engineer named Kidu introduced themself. _(javascriptallonge.pdf (source-range-8eb13d6b-01862))_
- 'I worked at Thing, and Christine told us about your solution. I had a look at the code you left on the whiteboard. Of course, white-boarding in an interview situation is notoriously unreliable, so small defects are not important. But I couldn't help but notice that your solution doesn't actually meet the stated requirements for a different reason:' _(javascriptallonge.pdf (source-range-8eb13d6b-01864))_
- 'The hasCycle function, a/k/a Tortoise and Hare, requires two separate iterators to do its job. Whereas the problem as stated involves a single stream of directions. You're essentially calling for the player to clone themselves and call out the directions in parallel.' _(javascriptallonge.pdf (source-range-8eb13d6b-01865))_
- Kidu shrugged. 'You know, the requirement asked for a finite space algorithm, not a constant state algorithm. Doesn't it make sense to go with a faster finite space algorithm? There's no benefit to constant space if finite space is sufficient. ' _(javascriptallonge.pdf (source-range-8eb13d6b-01868))_
- The Carpenter stared at Kidu's solution. 'I guess,' he allowed, 'It isn't always necessary to make a solution so awesome it would please the Ghosts of Mars.' _(javascriptallonge.pdf (source-range-8eb13d6b-01870))_
- Whereas the problem as stated involves a single stream of directions. _(javascriptallonge.pdf (source-range-8eb13d6b-01865))_

## Technical atoms

### Technical frame 1: after another drink

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01868))_

> Kidu shrugged. 'You know, the requirement asked for a finite space algorithm, not a constant state algorithm. Doesn't it make sense to go with a faster finite space algorithm? There's no benefit to constant space if finite space is sufficient. '

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01867))_

```
// implements Teleporting Tortoise // cycle detection algorithm. const hasCycle = (iterable) => { let iterator = iterable[Symbol.iterator](), teleportDistance = 1; while ( true ) { let {value, done} = iterator.next(), tortoise = value; if (done) return false ; for ( let i = 0; i < teleportDistance; ++i) { let {value, done} = iterator.next(), hare = value; if (done) return false ; if (tortoise === hare) return true ; } teleportDistance *= 2; } return false ; };
```

### Technical frame 2: after another drink

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01870))_

> The Carpenter stared at Kidu's solution. 'I guess,' he allowed, 'It isn't always necessary to make a solution so awesome it would please the Ghosts of Mars.'

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01869))_

```
const hasCycle = (orderedCollection) => { const visited = new Set(); for ( let element of orderedCollection) { if (visited.has(element)) { return true ; } visited.add(element); } return false ; };
```
