---
page_id: javascriptallonge-operations-that-compose-two-or-more-iterables-into-an-iterable
page_kind: source
summary: Summary of the section on operations that compose two or more iterables into an iterable from javascriptallonge.
sources: raw/javascriptallonge.pdf p.285-286
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This section describes functions that compose two or more iterables into an iterable, specifically zip and zipWith.

## Key supported claims

- The function *zip* composes two or more iterables into an iterable by mapping over the iterables and yielding arrays of values (raw/javascriptallonge.pdf p.285-286).
- Note: zip is also the following special case of zipWith (raw/javascriptallonge.pdf p.285-286).
- The const zip = callFirst(zipWith, (...values) => values) expresses zip as a special case of zipWith (raw/javascriptallonge.pdf p.285-286).
