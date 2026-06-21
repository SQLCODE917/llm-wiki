---
page_id: javascriptallonge-copy-on-write
page_kind: source
summary: Copy-on-write strategy in JavaScript, including its definition, tradeoffs, and implementation in the context of immutable data structures.
sources: raw/javascriptallonge.pdf p.162-163
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

Copy-on-write strategy in JavaScript, including its definition, tradeoffs, and implementation in the context of immutable data structures.

## Key supported claims

- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' (raw/javascriptallonge.pdf p.162-163).
- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks (raw/javascriptallonge.pdf p.162-163).
- Like all strategies, it makes a tradeoff: It's much cheaper than pessimistically copying structures when you make an infrequent number of small changes, but if you tend to make a lot of changes to some that you aren't sharing, it's more expensive (raw/javascriptallonge.pdf p.162-163).
- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write (raw/javascriptallonge.pdf p.162-163).
