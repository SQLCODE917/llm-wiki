---
page_id: javascriptallonge-section-we-ll-keep-it-simple-javascript-s-generators-a7436505
page_kind: source
page_family: section-reference
summary: We'll keep it simple: / javascript's generators: 17 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-ll-keep-it-simple-javascript-s-generators-a7436505@e9e5677447cda55d150e44357ec334b7
---

# We'll keep it simple: / javascript's generators

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-we-ll-keep-it-simple-1104ef0d]] - broader source section: We'll keep it simple:

## Statements

- It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator. Given the title of this chapter, it is not a surprise that JavaScript makes this possible. _(javascriptallonge.pdf (source-range-7239e085-01661))_
- We can write an iterator, but use a generation style of programming. An iterator written in a generation style is called a generator . To write a generator, we write a function, but we make two changes: _(javascriptallonge.pdf (source-range-7239e085-01662))_
- When we invoke empty , we get an iterator with no elements. This makes sense, because empty never yields anything. We call its .next() method, but it's done immediately. _(javascriptallonge.pdf (source-range-7239e085-01667))_
- Generator functions can take an argument. Let's use that to illustrate yield : _(javascriptallonge.pdf (source-range-7239e085-01668))_
- Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-7239e085-01671))_
- An iterator written in a generation style is called a generator . _(javascriptallonge.pdf (source-range-7239e085-01662))_
- This makes sense, because empty never yields anything. _(javascriptallonge.pdf (source-range-7239e085-01667))_
- Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . _(javascriptallonge.pdf (source-range-7239e085-01671))_
- Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-7239e085-01671))_
