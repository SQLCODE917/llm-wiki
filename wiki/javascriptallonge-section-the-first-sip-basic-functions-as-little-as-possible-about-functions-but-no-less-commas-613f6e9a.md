---
page_id: javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-commas-613f6e9a
page_kind: source
page_family: section-reference
summary: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas: 6 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-commas-613f6e9a@6216400c716e7bc54b58fdb771cab0e7
---

# The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-0ed59777]] - broader source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

## Statements

- The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words: _(javascriptallonge.pdf (source-range-7239e085-00201))_
- This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write: _(javascriptallonge.pdf (source-range-7239e085-00205))_

## Technical atoms

### Technical frame 1: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00205))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00202))_

<a id="atom-technical-atom-44cc1745b220be9f"></a>

```
//=> 2
(1 + 1, 2 + 2)
```

### Technical frame 2: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00205))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00204))_

<a id="atom-technical-atom-ead6c5c59b062746"></a>

```
(() => (1 + 1, 2 + 2))()
//=> 4
```

### Technical frame 3: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00201))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00205))_

<a id="atom-technical-atom-a037009faf63061c"></a>

> This is useful when trying to do things that might involve side-effects , but we'll get to that later.
