---
page_id: javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-after-another-drink-b1c5a752
page_kind: source
summary: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / after another drink: 8 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-after-another-drink-b1c5a752@3d446c7dcdc83eb606a81699341da15f
---

# We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / after another drink

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-196a6679]] - broader source section: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job

## Statements

- A few drinks later, The Carpenter was telling his Thing story and an engineer named Kidu introduced themself. _(javascriptallonge.pdf (source-range-7239e085-01863))_
- 'I worked at Thing, and Christine told us about your solution. I had a look at the code you left on the whiteboard. Of course, white-boarding in an interview situation is notoriously unreliable, so small defects are not important. But I couldn't help but notice that your solution doesn't actually meet the stated requirements for a different reason:' _(javascriptallonge.pdf (source-range-7239e085-01865))_
- 'The hasCycle function, a/k/a Tortoise and Hare, requires two separate iterators to do its job. Whereas the problem as stated involves a single stream of directions. You're essentially calling for the player to clone themselves and call out the directions in parallel.' _(javascriptallonge.pdf (source-range-7239e085-01866))_
- Kidu shrugged. 'You know, the requirement asked for a finite space algorithm, not a constant state algorithm. Doesn't it make sense to go with a faster finite space algorithm? There's no benefit to constant space if finite space is sufficient. ' _(javascriptallonge.pdf (source-range-7239e085-01869))_
- The Carpenter stared at Kidu's solution. 'I guess,' he allowed, 'It isn't always necessary to make a solution so awesome it would please the Ghosts of Mars.' _(javascriptallonge.pdf (source-range-7239e085-01871))_
- Whereas the problem as stated involves a single stream of directions. _(javascriptallonge.pdf (source-range-7239e085-01866))_

## Technical atoms

### Technical frame 1: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / after another drink

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01869))_

> Kidu shrugged. 'You know, the requirement asked for a finite space algorithm, not a constant state algorithm. Doesn't it make sense to go with a faster finite space algorithm? There's no benefit to constant space if finite space is sufficient. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01868))_

```
// implements Teleporting Tortoise
// cycle detection algorithm.
const hasCycle = (iterable) => {
let iterator = iterable[Symbol.iterator](),
teleportDistance = 1;
while (true) {
let {value, done} = iterator.next(),
tortoise = value;
if (done) return false;
for (let i = 0; i < teleportDistance; ++i) {
let {value, done} = iterator.next(),
hare = value;
if (done) return false;
if (tortoise === hare) return true;
}
teleportDistance *= 2;
}
return false;
};
```

### Technical frame 2: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / after another drink

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01871))_

> The Carpenter stared at Kidu's solution. 'I guess,' he allowed, 'It isn't always necessary to make a solution so awesome it would please the Ghosts of Mars.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01870))_

```
const hasCycle = (orderedCollection) => {
const visited = new Set();
for (let element of orderedCollection) {
if (visited.has(element)) {
return true;
}
visited.add(element);
}
return false;
};
```
