---
page_id: javascriptallonge-section-composing-and-decomposing-data-reassignment-mixing-let-and-const-ca678af6
page_kind: source
page_family: section-reference
summary: Composing and Decomposing Data / Reassignment / mixing let and const: 20 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-reassignment-mixing-let-and-const-ca678af6@73d6441cf35632950ddd25ca48878b07
---

# Composing and Decomposing Data / Reassignment / mixing let and const

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-reassignment-5040fcae]] - broader source section: Composing and Decomposing Data / Reassignment
- [[javascriptallonge-section-composing-and-decomposing-data-reassignment-mixing-let-and-const-var-1276f47e]] - narrower source section: Composing and Decomposing Data / Reassignment / mixing let and const / var

## Statements

- Some programmers dislike deliberately shadowing variables. The suggestion is that shadowing a variable is confusing code. If you buy that argument, the way that shadowing works in JavaScript exists to protect us from accidentally shadowing a variable when we move code around. _(javascriptallonge.pdf (source-range-7239e085-01180))_
- Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And: _(javascriptallonge.pdf (source-range-7239e085-01183))_

## Statements by subsection

### Composing and Decomposing Data / Reassignment / mixing let and const / var

- JavaScript has one more way to bind a name to a value, var . 71 var looks a lot like let : _(javascriptallonge.pdf (source-range-7239e085-01187))_
- But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations: _(javascriptallonge.pdf (source-range-7239e085-01191))_
- Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations. _(javascriptallonge.pdf (source-range-7239e085-01193))_
- But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. Note this example of a function that uses a helper: _(javascriptallonge.pdf (source-range-7239e085-01194))_
- In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped. _(javascriptallonge.pdf (source-range-7239e085-01200))_
- A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. _(javascriptallonge.pdf (source-range-7239e085-01194))_
- In that way, var is a little like const and let , we should always declare and bind names before using them. _(javascriptallonge.pdf (source-range-7239e085-01200))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Reassignment / mixing let and const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01183))_

> Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01182))_

<a id="atom-technical-atom-903c080c8c808ee9"></a>

```
(() => {
let age = 49;
if (true) {
const age = 50;
}
age = 51;
return age;
})()
//=> 51
```

### Technical frame 2: Composing and Decomposing Data / Reassignment / mixing let and const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01183))_

> Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01184))_

<a id="atom-technical-atom-3df1cddbc62de02b"></a>

```
(() => {
const age = 49;
if (true) {
let age = 50;
}
age = 52;
return age;
})()
//=> ERROR: age is read-only
```
