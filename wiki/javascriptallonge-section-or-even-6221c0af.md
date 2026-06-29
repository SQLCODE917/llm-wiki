---
page_id: javascriptallonge-section-or-even-6221c0af
page_kind: source
summary: Or even:: 47 source-backed entries and 16 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-or-even-6221c0af@22cc5a615d2317ecfec0e6550d373fde
---

# Or even:

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-or-even-the-simplest-possible-block-528c8472]] - narrower source section: Or even: / the simplest possible block
- [[javascriptallonge-section-or-even-void-8a19170f]] - narrower source section: Or even: / void
- [[javascriptallonge-section-or-even-back-on-the-block-b9587c98]] - narrower source section: Or even: / back on the block

## Statements by subsection

### Or even: / the simplest possible block

- There's another thing we can put to the right of an arrow, a block . A block has zero or more statements , separated by semicolons. 18 _(javascriptallonge.pdf (source-range-7239e085-00210))_
- It returns the result of evaluating a block that has no statements. What would that be? Let's try it: _(javascriptallonge.pdf (source-range-7239e085-00213))_

### Or even: / the simplest possible block / undefined

- In JavaScript, the absence of a value is written undefined , and it means there is no value. It will crop up again. undefined is its own type of value, and it acts like a value type: _(javascriptallonge.pdf (source-range-7239e085-00217))_
- Like numbers, booleans and strings, JavaScript can print out the value undefined . _(javascriptallonge.pdf (source-range-7239e085-00220))_
- No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-) _(javascriptallonge.pdf (source-range-7239e085-00222))_
- 18 Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons. This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. We will not take advantage of this feature, but it's helpful to know it exists. _(javascriptallonge.pdf (source-range-7239e085-00223))_
- You might think that undefined in JavaScript is equivalent to NULL in SQL. No. In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can't be equal. In JavaScript, every undefined is identical to every other undefined . _(javascriptallonge.pdf (source-range-7239e085-00224))_
- In JavaScript, the absence of a value is written undefined , and it means there is no value. _(javascriptallonge.pdf (source-range-7239e085-00217))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-7239e085-00223))_
- In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can't be equal. _(javascriptallonge.pdf (source-range-7239e085-00224))_

### Or even: / void

- We've seen that JavaScript represents an undefined value by typing undefined , and we've generated undefined values in two ways: _(javascriptallonge.pdf (source-range-7239e085-00226))_
- By writing undefined ourselves. _(javascriptallonge.pdf (source-range-7239e085-00228))_
- void is an operator that takes any value and evaluates to undefined , always. So, when we deliberately want an undefined value, should we use the first, second, or third form? 19 The answer is, use void . By convention, use void 0 . _(javascriptallonge.pdf (source-range-7239e085-00231))_
- The first form works but it's cumbersome. The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we'll discuss in Reassignment and Mutation. The third form is guaranteed to always work, so that's what we will use. 20 _(javascriptallonge.pdf (source-range-7239e085-00232))_

### Or even: / back on the block

- We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21 _(javascriptallonge.pdf (source-range-7239e085-00236))_
- We haven't discussed these statements . What's a statement? _(javascriptallonge.pdf (source-range-7239e085-00238))_
- There are many kinds of JavaScript statements, but the first kind is one we've already met. An expression is a JavaScript statement. Although they aren't very practical, these are valid JavaScript functions, and they return undefined when applied: _(javascriptallonge.pdf (source-range-7239e085-00239))_
- As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way: _(javascriptallonge.pdf (source-range-7239e085-00241))_
- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined : _(javascriptallonge.pdf (source-range-7239e085-00243))_
- 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-7239e085-00246))_

## Technical atoms

### Technical frame 1: Or even:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00208))_

```
() => (
1 + 1,
2 + 2
)
```

### Technical frame 2: Or even: / the simplest possible block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00213))_

> It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00212))_

```
() => {}
```

### Technical frame 3: Or even: / the simplest possible block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00213))_

> It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00214))_

```
(() => {})()
//=> undefined
```

### Technical frame 4: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00220))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00218))_

```
undefined
```

### Technical frame 5: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00220))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00219))_

```
//=> undefined
```

### Technical frame 6: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00222))_

> No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-)

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00221))_

```
undefined === undefined
//=> true
(() => {})() === (() => {})()
//=> true
(() => {})() === undefined
//=> true
```

### Technical frame 7: Or even: / void

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00231))_

> void is an operator that takes any value and evaluates to undefined , always. So, when we deliberately want an undefined value, should we use the first, second, or third form? 19 The answer is, use void . By convention, use void 0 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00230))_

```
void 0
//=> undefined
void 1
//=> undefined
void (2 + 2)
//=> undefined
```

### Technical frame 8: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00236))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00235))_

```
(() => {})()
//=> undefined
```

### Technical frame 9: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00241))_

> As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00240))_

```
() => { 2 + 2 }
() => { 1 + 1; 2 + 2 }
```

### Technical frame 10: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00243))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00242))_

```
() => {
1 + 1;
2 + 2
}
```

### Technical frame 11: Or even: / back on the block

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

### Technical frame 12: Or even: / back on the block

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

### Technical frame 13: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00248))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical frame 14: Or even: / back on the block

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

### Technical frame 15: Or even: / back on the block

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

### Technical atom 16

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
