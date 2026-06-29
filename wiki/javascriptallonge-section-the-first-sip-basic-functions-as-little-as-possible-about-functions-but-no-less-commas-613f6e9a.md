---
page_id: javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-commas-613f6e9a
page_kind: source
summary: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas: 6 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-commas-613f6e9a@a41ab490e83fd4cd60546edb8225ff91
---

# The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-0ed59777]] - broader source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

## Statements

- The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words: _(javascriptallonge.pdf (source-range-7239e085-00201))_
- This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write: _(javascriptallonge.pdf (source-range-7239e085-00205))_

## Technical atoms

### Technical frame 1: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00205))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00202))_

```
//=> 2
(1 + 1, 2 + 2)
```

### Technical frame 2: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00205))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00204))_

```
(() => (1 + 1, 2 + 2))()
//=> 4
```

### Technical frame 3: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00201))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00205))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later.

### Technical frame 4: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00205))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00206))_

```
() =>
(1 + 1, 2 + 2)
```
