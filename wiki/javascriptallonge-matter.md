---
page_id: javascriptallonge-matter
page_kind: concept
summary: Matter: 6 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-matter@876a52463371e9c6a29fbfb2d09678dc
---

# Matter

What [[javascriptallonge]] covers about matter:

## Statements

### michael fogus

- In the case of JavaScript Allongé, you'll find the Leanpub model a shining example of effectiveness. Reg has crafted (and continues to craft) not only an interesting book from the perspective of a connoisseur, but also an entertaining exploration into some of the most interesting aspects of his art. No matter how much of an expert you think you are, JavaScript Allongé has something to teach you… about coffee. I kid. _(javascriptallonge.pdf (source-range-31a4cf47-00086))_

### undefined

- No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-) _(javascriptallonge.pdf (source-range-31a4cf47-00226))_

### void

- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined : _(javascriptallonge.pdf (source-range-31a4cf47-00246))_

### truthiness and the ternary operator

- The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on truthiness , not on boolean values. This affects the way the ! , && , and || operators work. We'll look at them in a moment, but first, we'll look at one more operator. _(javascriptallonge.pdf (source-range-31a4cf47-00767))_

### Tortoises, Hares, and Teleporting Turtles

- This algorithm is called 'The Tortoise and the Hare,' and was discovered by Robert Floyd in the 1960s. You have two node references, and one traverses the list at twice the speed of the other. No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop. _(javascriptallonge.pdf (source-range-31a4cf47-01265))_

### generators are coroutines

- But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next() , it runs until it returns, ends, or yields. If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-31a4cf47-01707))_


## Technical atoms

### Technical frame 1: undefined

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00226))_

> No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-)

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00225))_

```
undefined === undefined //=> true (() => {})() === (() => {})() //=> true (() => {})() === undefined //=> true
```

### Technical frame 2: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00247))_

```
(() => { 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined
```


## Related pages

- [[javascriptallonge-evaluate]] - shared statements and technical atoms: Evaluate shares source evidence from undefined: No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-); Evaluate shares technical record from undefined: undefined === undefined //=> true (() => {})() === (() => {})() //=> true (() => {})() === undefined //=> true (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-block]] - shared statements and technical atoms: Block shares source evidence from void: But no matter how we arrange them, a block with one or more expressions still evaluates to undefined :; Block shares technical record from void: (() => { 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from void: But no matter how we arrange them, a block with one or more expressions still evaluates to undefined :; Expression shares technical record from void: (() => { 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical record from undefined: undefined === undefined //=> true (() => {})() === (() => {})() //=> true (() => {})() === undefined //=> true (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from generators are coroutines: But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next() , it runs until it retur ... [truncated] (1 shared statement(s))
- [[javascriptallonge-truthiness]] - shared statements: Truthiness shares source evidence from truthiness and the ternary operator: The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on truthiness , not on boolean values. This af ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
