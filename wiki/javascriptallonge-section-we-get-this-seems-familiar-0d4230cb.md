---
page_id: javascriptallonge-section-we-get-this-seems-familiar-0d4230cb
page_kind: source
page_family: section-reference
summary: We get: / this seems familiar: 10 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-get-this-seems-familiar-0d4230cb@26d7cc4217ea641443ba5415aeec7b6d
---

# We get: / this seems familiar

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-we-get-2605e005]] - broader source section: We get:

## Statements

- When we looked at generators, we saw that some iterators are inherently stateful, but sometimes it is awkward to represent them in a fully stateless fashion. Sometimes there is a state machine that is naturally represented implicitly in JavaScript's control flow rather than explicitly in data. _(javascriptallonge.pdf (source-range-7239e085-01930))_
- We've done almost the exact same thing here with our naughts and crosses game. A game like this is absolutely a state machine, and we've explicitly coded those states into the lookup table. Which leads us to wonder: Is there a way to encode those states implicitly , in JavaScript control flow? _(javascriptallonge.pdf (source-range-7239e085-01931))_
- If we were in full control of the interaction, it would be easy to encode the game play as a decision tree instead of as a lookup table. For example, we could do this in a browser: _(javascriptallonge.pdf (source-range-7239e085-01932))_
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree. _(javascriptallonge.pdf (source-range-7239e085-01934))_
- Canwedothesamethinghere?Atfirst glance, no. How do we get the player's moves to the generator function? But the first glance is deceptive, because we only see what we've seen so far. Let's see how it would actually work. _(javascriptallonge.pdf (source-range-7239e085-01936))_
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. _(javascriptallonge.pdf (source-range-7239e085-01934))_
- But the first glance is deceptive, because we only see what we've seen so far. _(javascriptallonge.pdf (source-range-7239e085-01936))_
