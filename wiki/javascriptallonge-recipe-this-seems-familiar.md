---
page_id: javascriptallonge-recipe-this-seems-familiar
page_kind: recipe
page_family: recipe-pattern
summary: this seems familiar: reusable source-backed pattern with 7 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: this-seems-familiar
projection_coverage: recipe-javascriptallonge-recipe-this-seems-familiar@26c0d3804e715259c62683b64adab5ee
---

# this seems familiar

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-we-get-this-seems-familiar-0d4230cb]].
- Evidence roles: decision, constraint, explanation, example.

## Applicability And Rationale

- When we looked at generators, we saw that some iterators are inherently stateful, but sometimes it is awkward to represent them in a fully stateless fashion. _(javascriptallonge.pdf (source-range-7239e085-01930))_
- Sometimes there is a state machine that is naturally represented implicitly in JavaScript's control flow rather than explicitly in data. _(javascriptallonge.pdf (source-range-7239e085-01930))_
- A game like this is absolutely a state machine, and we've explicitly coded those states into the lookup table. _(javascriptallonge.pdf (source-range-7239e085-01931))_
- If we were in full control of the interaction, it would be easy to encode the game play as a decision tree instead of as a lookup table. _(javascriptallonge.pdf (source-range-7239e085-01932))_
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. _(javascriptallonge.pdf (source-range-7239e085-01934))_
- But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree. _(javascriptallonge.pdf (source-range-7239e085-01934))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01933)_

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

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-we-get-this-seems-familiar-0d4230cb]]
