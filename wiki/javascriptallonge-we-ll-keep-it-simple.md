---
page_id: javascriptallonge-we-ll-keep-it-simple
page_kind: source
summary: Summary of the 'We'll keep it simple' section from JavaScript Allongé, focusing on generators vs. iterators.
sources: raw/javascriptallonge.pdf p.229-230
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This section contrasts the use of generators and iterators in JavaScript, focusing on how state is handled in each approach.

## Key supported claims

- In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. (raw/javascriptallonge.pdf p.229-230)
- So we see the same thing: The generation version has state, but it's implicit in JavaScript's linear control flow. (raw/javascriptallonge.pdf p.229-230)
- Whereas the iteration version must make that state explicit. (raw/javascriptallonge.pdf p.229-230)
