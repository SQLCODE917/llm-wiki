---
page_id: javascriptallonge-section-or-even-back-on-the-block-b9587c98
page_kind: source
summary: Or even: / back on the block: 20 source-backed entries and 9 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-or-even-back-on-the-block-b9587c98@889a60f5fe5944d0f1c90d9cd7983788
---

# Or even: / back on the block

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-or-even-6221c0af]] - broader source section: Or even:
- [[javascriptallonge-block]] - topic hub: opens the topic page for Block

## Statements

- We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21 _(javascriptallonge.pdf (source-range-7239e085-00236))_
- We haven't discussed these statements . What's a statement? _(javascriptallonge.pdf (source-range-7239e085-00238))_
- There are many kinds of JavaScript statements, but the first kind is one we've already met. An expression is a JavaScript statement. Although they aren't very practical, these are valid JavaScript functions, and they return undefined when applied: _(javascriptallonge.pdf (source-range-7239e085-00239))_
- As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way: _(javascriptallonge.pdf (source-range-7239e085-00241))_
- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined : _(javascriptallonge.pdf (source-range-7239e085-00243))_
- 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-7239e085-00246))_

## Technical atoms

### Technical frame 1: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00236))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00235))_

```
(() => {})()
//=> undefined
```

### Technical frame 2: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00241))_

> As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00240))_

```
() => { 2 + 2 }
() => { 1 + 1; 2 + 2 }
```

### Technical frame 3: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00243))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00242))_

```
() => {
1 + 1;
2 + 2
}
```

### Technical frame 4: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00244))_

```
(() => { 2 + 2 })()
//=> undefined
(() => { 1 + 1; 2 + 2 })()
//=> undefined
(() => {
1 + 1;
2 + 2
})()
//=> undefined
```

### Technical frame 5: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00247))_

```
(() => 2 + 2)()
//=> 4
(() => { 2 + 2 })()
//=> undefined
(() => (1 + 1, 2 + 2))()
//=> 4
(() => { 1 + 1; 2 + 2 })()
//=> undefined
```

### Technical frame 6: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00248))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical frame 7: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00249))_

```
(() => { return 0 })()
//=> 0
(() => { return 1 })()
//=> 1
(() => { return 'Hello ' + 'World' })()
// 'Hello World'
```

### Technical frame 8: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00251))_

```
(() => {
1 + 1;
return 2 + 2
})()
//=> 4
```

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00236))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00234))_

| entry | content |
| --- | --- |
| 19 | Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This was actually the preferred mechanism until void became commonplace. |
| 20 | As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined . We have no idea. |

<details>
<summary>Raw table text</summary>

```
back on the block
Back to our function. We evaluated this:
19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This was actually the preferred mechanism until void became commonplace.
20 As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined . We have no idea.
```

</details>
