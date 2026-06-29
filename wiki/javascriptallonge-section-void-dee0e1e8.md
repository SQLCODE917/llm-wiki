---
page_id: javascriptallonge-section-void-dee0e1e8
page_kind: source
summary: void: 26 source-backed entries and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-void-dee0e1e8@c93176c27d573f6b80a1d57a919ad83b
---

# void

From [[javascriptallonge]].

## Statements

- We've seen that JavaScript represents an undefined value by typing undefined , and we've generated undefined values in two ways: _(javascriptallonge.pdf (source-range-8eb13d6b-00230))_
- By writing undefined ourselves. _(javascriptallonge.pdf (source-range-8eb13d6b-00232))_
- void is an operator that takes any value and evaluates to undefined , always. So, when we deliberately want an undefined value, should we use the first, second, or third form? 19 The answer is, use void . By convention, use void 0 . _(javascriptallonge.pdf (source-range-8eb13d6b-00235))_
- The first form works but it's cumbersome. The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we'll discuss in Reassignment and Mutation. The third form is guaranteed to always work, so that's what we will use. 20 _(javascriptallonge.pdf (source-range-8eb13d6b-00236))_
- We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21 _(javascriptallonge.pdf (source-range-8eb13d6b-00239))_
- We haven't discussed these statements . What's a statement? _(javascriptallonge.pdf (source-range-8eb13d6b-00241))_
- There are many kinds of JavaScript statements, but the first kind is one we've already met. An expression is a JavaScript statement. Although they aren't very practical, these are valid JavaScript functions, and they return undefined when applied: _(javascriptallonge.pdf (source-range-8eb13d6b-00242))_
- As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way: _(javascriptallonge.pdf (source-range-8eb13d6b-00244))_
- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined : _(javascriptallonge.pdf (source-range-8eb13d6b-00246))_
- 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-8eb13d6b-00249))_

## Technical atoms

### Technical frame 1: void

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00235))_

> void is an operator that takes any value and evaluates to undefined , always. So, when we deliberately want an undefined value, should we use the first, second, or third form? 19 The answer is, use void . By convention, use void 0 .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00234))_

```
void 0 //=> undefined void 1 //=> undefined void (2 + 2) //=> undefined
```

### Technical frame 2: void

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00239))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00238))_

```
(() => {})() //=> undefined
```

### Technical frame 3: void

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00244))_

> As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00243))_

```
() => { 2 + 2 } () => { 1 + 1; 2 + 2 }
```

### Technical frame 4: void

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00246))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined :

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00245))_

```
() => { 1 + 1; 2 + 2 }
```

### Technical frame 5: void

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00247))_

```
(() => { 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined
```

### Technical frame 6: void

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00250))_

```
(() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined
```

### Technical frame 7: void

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00251))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical frame 8: void

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00252))_

```
(() => { return 0 })() //=> 0 (() => { return 1 })() //=> 1 (() => { return 'Hello ' + 'World' })() // 'Hello World'
```

### Technical frame 9: void

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00254))_

```
(() => { 1 + 1; return 2 + 2 })() //=> 4
```

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00239))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00237))_

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
