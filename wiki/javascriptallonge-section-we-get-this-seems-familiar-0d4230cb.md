---
page_id: javascriptallonge-section-we-get-this-seems-familiar-0d4230cb
page_kind: source
summary: We get: / this seems familiar: 10 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-get-this-seems-familiar-0d4230cb@46b334163d263a6d4e66dc2816809aa6
---

# We get: / this seems familiar

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-we-get-2605e005]] - broader source section: We get:

## Statements

- When we looked at generators, we saw that some iterators are inherently stateful, but sometimes it is awkward to represent them in a fully stateless fashion. Sometimes there is a state machine that is naturally represented implicitly in JavaScript's control flow rather than explicitly in data. _(javascriptallonge.pdf (source-range-7239e085-01930))_
- We've done almost the exact same thing here with our naughts and crosses game. A game like this is absolutely a state machine, and we've explicitly coded those states into the lookup table. Which leads us to wonder: Is there a way to encode those states implicitly , in JavaScript control flow? _(javascriptallonge.pdf (source-range-7239e085-01931))_
- If we were in full control of the interaction, it would be easy to encode the game play as a decision tree instead of as a lookup table. For example, we could do this in a browser: _(javascriptallonge.pdf (source-range-7239e085-01932))_
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree. _(javascriptallonge.pdf (source-range-7239e085-01934))_
- Canwedothesamethinghere?Atfirst glance, no. How do we get the player's moves to the generator function? But the first glance is deceptive, because we only see what we've seen so far. Let's see how it would actually work. _(javascriptallonge.pdf (source-range-7239e085-01936))_
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. _(javascriptallonge.pdf (source-range-7239e085-01934))_
- But the first glance is deceptive, because we only see what we've seen so far. _(javascriptallonge.pdf (source-range-7239e085-01936))_

## Technical atoms

### Technical frame 1: We get: / this seems familiar

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01934))_

> Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01933))_

```
function browserNaughtsAndCrosses () {
const x1 = parseInt(prompt('o plays 0, where does x play?'));
switch (x1) {
case 1:
const x2 = parseInt(prompt('o plays 6, where does x play?'));
switch (x2) {
case 2:
case 4:
case 5:
case 7:
case 8:
alert('o plays 3');
break;
case 3:
const x3 = parseInt(prompt('o plays 8, where does x play?'));
switch (x3) {
case 2:
case 5:
case 7:
alert('o plays 4');
break;
case 4:
alert('o plays 7');
break;
}
}
break;
// ...
}
}
```
