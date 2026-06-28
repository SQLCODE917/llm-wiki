---
page_id: javascriptallonge-section-mixing-let-and-const-d447814e
page_kind: source
summary: mixing let and const: 6 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-mixing-let-and-const-d447814e@292f9541c7953c7e30437752384a0e13
---

# mixing let and const

From [[javascriptallonge]].

## Statements

- Some programmers dislike deliberately shadowing variables. The suggestion is that shadowing a variable is confusing code. If you buy that argument, the way that shadowing works in JavaScript exists to protect us from accidentally shadowing a variable when we move code around. _(javascriptallonge.pdf (source-range-31a4cf47-01180))_
- Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And: _(javascriptallonge.pdf (source-range-31a4cf47-01183))_
- Shadowing a const with a let does not permit it to be rebound in its original scope. _(javascriptallonge.pdf (source-range-31a4cf47-01185))_

## Technical atoms

### Technical frame 1: mixing let and const

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01183))_

> Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01181))_

> If you dislike deliberately shadowing variables, you'll probably take an even more opprobrious view of mixing const and let semantics with a shadowed variable:

### Technical frame 2: mixing let and const

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01183))_

> Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01182))_

```
(() => { let age = 49; if ( true ) { const age = 50; } age = 51; return age; })() //=> 51
```

### Technical frame 3: mixing let and const

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01185))_

> Shadowing a const with a let does not permit it to be rebound in its original scope.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01184))_

```
(() => { const age = 49; if ( true ) { let age = 50; } age = 52; return age; })() //=> ERROR: age is read-only
```
