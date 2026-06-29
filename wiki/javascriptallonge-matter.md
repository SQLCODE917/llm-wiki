---
page_id: javascriptallonge-matter
page_kind: concept
summary: Matter: 6 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-matter@f74c2817e9153be3d40e9d12c61dd6ac
---

# Matter

What [[javascriptallonge]] covers about matter:

## Statements

### ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus

- In the case of JavaScript Allongé, you'll find the Leanpub model a shining example of effectiveness. Reg has crafted (and continues to craft) not only an interesting book from the perspective of a connoisseur, but also an entertaining exploration into some of the most interesting aspects of his art. No matter how much of an expert you think you are, JavaScript Allongé has something to teach you… about coffee. I kid. _(javascriptallonge.pdf (source-range-7239e085-00086))_

### Or even: / the simplest possible block / undefined

- No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-) _(javascriptallonge.pdf (source-range-7239e085-00222))_

### Or even: / back on the block

- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined : _(javascriptallonge.pdf (source-range-7239e085-00243))_

### Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

- The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on truthiness , not on boolean values. This affects the way the ! , && , and || operators work. We'll look at them in a moment, but first, we'll look at one more operator. _(javascriptallonge.pdf (source-range-7239e085-00767))_

### Yes. Consider this variation: / Tortoises, Hares, and Teleporting Turtles

- This algorithm is called 'The Tortoise and the Hare,' and was discovered by Robert Floyd in the 1960s. You have two node references, and one traverses the list at twice the speed of the other. No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop. _(javascriptallonge.pdf (source-range-7239e085-01265))_

### We'll keep it simple: / generators are coroutines

- But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next() , it runs until it returns, ends, or yields. If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-7239e085-01706))_


## Technical atoms

### Technical frame 1: Or even: / the simplest possible block / undefined

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

### Technical frame 2: Or even: / back on the block

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


## Related pages

- [[javascriptallonge-evaluate]] - shared statements and technical atoms: Evaluate shares source evidence from Or even: / the simplest possible block / undefined: No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-); Evaluate shares technical record from Or even: / the simplest possible block / undefined: undefined === undefined //=> true (() => {})() === (() => {})() //=> true (() => {})() === undefined //=> true (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-block]] - shared statements and technical atoms: Block shares source evidence from Or even: / back on the block: But no matter how we arrange them, a block with one or more expressions still evaluates to undefined :; Block shares technical record from Or even: / back on the block: (() => { 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from Or even: / back on the block: But no matter how we arrange them, a block with one or more expressions still evaluates to undefined :; Expression shares technical record from Or even: / back on the block: (() => { 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical record from Or even: / the simplest possible block / undefined: undefined === undefined //=> true (() => {})() === (() => {})() //=> true (() => {})() === undefined //=> true (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from We'll keep it simple: / generators are coroutines: But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next() , it runs until it retur ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
