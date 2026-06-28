---
page_id: javascriptallonge
page_kind: source
summary: Claim-ledger projection (general-prose): 1213 usable entries, 23 technical atoms, 341 needs-review, 147 linked page(s); write decision write-with-review-work.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources
source_id: javascriptallonge.pdf
projection_coverage: projection-coverage-ce8c7843e3c27e11@2e049b5c68fb4156
---

# Document

## Document

- How to Do What You Love & Earn What You’re Worth as a Programmer _(javascriptallonge.pdf (source-range-83ecb080-00003))_

## Table of Contents

- I’d Like to Have an Argument, Please. _(javascriptallonge.pdf (source-range-83ecb080-00005))_
- |What JavaScript Allongé is. _(javascriptallonge.pdf (source-range-83ecb080-00005))_
- |**Served by the Pot: Collections** . _(javascriptallonge.pdf (source-range-83ecb080-00007))_

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00006))_

| A Pull of the Lever: Prefaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | i |
| --- | --- |
| About JavaScript Allongé . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ii |
| What JavaScript Allongé is. And isn’t. . . . . . . . . . . . . . . . . . . . . . . . . . . . . | v |
| Foreword to the “Six” edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | viii |
| Forewords to the First Edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ix |
| About The Sample PDF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xi |
| Prelude: Values and Expressions over Coffee . . . . . . . . . . . . . . . . . . . . . . . . . | xiii |
| values are expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xiv |
| values and identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xvi |
| A Rich Aroma: Basic Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 1 |
| The first sip: Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 5 |
| As Little As Possible About Functions, But No Less . . . . . . . . . . . . . . . . . . . . . | 7 |
| Ah. I’d Like to Have an Argument, Please. . . . . . . . . . . . . . . . . . . . . . . . . . . | 16 |
| Closures and Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 21 |
| That Constant Coffee Craving . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 26 |
| Naming Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 39 |
| Combinators and Function Decorators . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 45 |
| Building Blocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 48 |
| Magic Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 51 |
| Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 55 |
| Recipes with Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 56 |
| Partial Application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 57 |
| Unary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 59 |
| Tap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 61 |
| Maybe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 63 |
| Once . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 65 |
| Left-Variadic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 66 |
| Picking the Bean: Choice and Truthiness . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 71 |

<details>
<summary>Raw table text</summary>

```
| A Pull of the Lever: Prefaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | i |
| --- | --- |
| About JavaScript Allongé . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ii |
| What JavaScript Allongé is. And isn’t. . . . . . . . . . . . . . . . . . . . . . . . . . . . . | v |
| Foreword to the “Six” edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | viii |
| Forewords to the First Edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ix |
| About The Sample PDF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xi |
| Prelude: Values and Expressions over Coffee . . . . . . . . . . . . . . . . . . . . . . . . . | xiii |
| values are expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xiv |
| values and identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xvi |
| A Rich Aroma: Basic Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 1 |
| The first sip: Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 5 |
| As Little As Possible About Functions, But No Less . . . . . . . . . . . . . . . . . . . . . | 7 |
| Ah. I’d Like to Have an Argument, Please. . . . . . . . . . . . . . . . . . . . . . . . . . . | 16 |
| Closures and Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 21 |
| That Constant Coffee Craving . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 26 |
| Naming Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 39 |
| Combinators and Function Decorators . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 45 |
| Building Blocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 48 |
| Magic Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 51 |
| Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 55 |
| Recipes with Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 56 |
| Partial Application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 57 |
| Unary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 59 |
| Tap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 61 |
| Maybe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 63 |
| Once . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 65 |
| Left-Variadic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 66 |
| Picking the Bean: Choice and Truthiness . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 71 |
```

</details>

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00008))_

| Composing and Decomposing Data . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 77 |
| --- | --- | --- |
| Arrays and Destructuring Arguments . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 78 |
| Self-Similarity . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 86 |
| Tail Calls (and Default Arguments) . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 94 |
| Garbage, Garbage Everywhere . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 103 |
| Plain Old JavaScript Objects . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 109 |
| Mutation . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 118 |
| Reassignment . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 125 |
| Copy on Write . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 135 |
| Tortoises, Hares, and Teleporting Turtles . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 141 |
| Functional Iterators . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 144 |
| Making Data Out Of Functions . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 154 |
| Recipes with Data . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 168 |
| mapWith . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 170 |
| Flip . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 172 |
| Object.assign . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 175 |
| Why? . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 178 |
| A Warm Cup: Basic Strings and Quasi-Literals | . . . . . . . . . . . . . . . . . . . . . . . . | 179 |
| Served by the Pot: Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 182 |
| Iteration and Iterables . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 183 |
| Generating Iterables . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 201 |
| Lazy and Eager Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 223 |
| Interlude: The Carpenter Interviews for a Job | . . . . . . . . . . . . . . . . . . . . . . . . | 238 |
| Interactive Generators . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 250 |
| Basic Operations on Iterables . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 261 |
| The Golden Crema: Appendices and Afterwords | . . . . . . . . . . . . . . . . . . . . . . . | 265 |
| How to run the examples . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 266 |
| Thanks! . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 268 |
| Copyright Notice . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 270 |
| About The Author . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 274 |

<details>
<summary>Raw table text</summary>

```
| Composing and Decomposing Data . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 77 |
| --- | --- | --- |
| Arrays and Destructuring Arguments . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 78 |
| Self-Similarity . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 86 |
| Tail Calls (and Default Arguments) . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 94 |
| Garbage, Garbage Everywhere . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 103 |
| Plain Old JavaScript Objects . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 109 |
| Mutation . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 118 |
| Reassignment . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 125 |
| Copy on Write . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 135 |
| Tortoises, Hares, and Teleporting Turtles . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 141 |
| Functional Iterators . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 144 |
| Making Data Out Of Functions . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 154 |
| Recipes with Data . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 168 |
| mapWith . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 170 |
| Flip . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 172 |
| Object.assign . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 175 |
| Why? . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 178 |
| A Warm Cup: Basic Strings and Quasi-Literals | . . . . . . . . . . . . . . . . . . . . . . . . | 179 |
| Served by the Pot: Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 182 |
| Iteration and Iterables . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 183 |
| Generating Iterables . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 201 |
| Lazy and Eager Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 223 |
| Interlude: The Carpenter Interviews for a Job | . . . . . . . . . . . . . . . . . . . . . . . . | 238 |
| Interactive Generators . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 250 |
| Basic Operations on Iterables . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 261 |
| The Golden Crema: Appendices and Afterwords | . . . . . . . . . . . . . . . . . . . . . . . | 265 |
| How to run the examples . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 266 |
| Thanks! . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 268 |
| Copyright Notice . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 270 |
| About The Author . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 274 |
```

</details>

## A Pull of the Lever: Prefaces

- Some complain that the long pull is more bitter and detracts from the best character of the coffee, others feel it releases even more complexity. _(javascriptallonge.pdf (source-range-83ecb080-00010))_

## About JavaScript Allongé

- It’s written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope. _(javascriptallonge.pdf (source-range-83ecb080-00012))_
- _JavaScript Allongé_ begins at the beginning, with values and expressions, and builds from there to discuss types, identity, functions, closures, scopes, collections, iterators, and many more subjects up to working with classes and instances. _(javascriptallonge.pdf (source-range-83ecb080-00012))_
- It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or code-centric. _(javascriptallonge.pdf (source-range-83ecb080-00012))_
- JavaScript Allongé is a first and foremost, a book about _programming with functions_ . _(javascriptallonge.pdf (source-range-83ecb080-00012))_
- Features like destructuring, block-structured variables, iterables, generators, and the class keyword are poised to make JavaScript programming more expressive. _(javascriptallonge.pdf (source-range-83ecb080-00012))_
- For example, JavaScript did not include block-structured variables. _(javascriptallonge.pdf (source-range-83ecb080-00012))_
- JavaScript idioms like function combinators and decorators leverage JavaScript’s power to make code easier to read, modify, debug and refactor. _(javascriptallonge.pdf (source-range-83ecb080-00012))_
- Over time, programmers discovered ways to roll their own versions of important features. _(javascriptallonge.pdf (source-range-83ecb080-00012))_
- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. _(javascriptallonge.pdf (source-range-83ecb080-00012))_
- Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-83ecb080-00012))_
- ECMAScript 2015 (formerly called ECMAScript 6 or “ES6”), is ushering in a very large number of improvements to the way programmers can write small, powerful components and combine them into larger, fully featured programs. _(javascriptallonge.pdf (source-range-83ecb080-00012))_
- Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-83ecb080-00012))_
- It’s written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope. _(javascriptallonge.pdf (source-range-83ecb080-00012))_
- For example, JavaScript did not include block-structured variables. _(javascriptallonge.pdf (source-range-83ecb080-00012))_
- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. _(javascriptallonge.pdf (source-range-83ecb080-00012))_
- In Ruby, we can write: def foo (first, *rest) # ... _(javascriptallonge.pdf (source-range-83ecb080-00013))_
- Working around the missing features was a necessary evil. _(javascriptallonge.pdf (source-range-83ecb080-00013))_
- But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. _(javascriptallonge.pdf (source-range-83ecb080-00013))_
- Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like: **function** foo () { **var** first = arguments[0], rest = [].slice.call(arguments, 1); _// ..._ } The first edition of JavaScript Allongé explained these and many other patterns for writing flexible and composable programs in JavaScript, but the intention wasn’t to explain how to work around JavaScript’s missing features: The intention was to explain why the style of programming exemplified by the missing features is important. _(javascriptallonge.pdf (source-range-83ecb080-00013))_
- But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. _(javascriptallonge.pdf (source-range-83ecb080-00013))_
- Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like: **function** foo () { **var** first = arguments[0], rest = [].slice.call(arguments, 1); _// ..._ } The first edition of JavaScript Allongé explained these and many other patterns for writing flexible and composable programs in JavaScript, but the intention wasn’t to explain how to work around JavaScript’s missing features: The intention was to explain why the style of programming exemplified by the missing features is important. _(javascriptallonge.pdf (source-range-83ecb080-00013))_
- It makes a number of interesting programming techniques easy to explain and easy to use. _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- But even so, in a way it is still explaining the exact same original idea that programs are built out of small, flexible functions composed together. _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- But the common thread that runs through all these things is that since they are all simple objects and simple functions, we can use the same set of “programming with functions” techniques to build programs by composing small, flexible, and decoupled entities. _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- It would have continued to say much the same things, only with new syntax. _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- JavaScript Allongé, The “Six” Edition packs all the goodness of JavaScript Allongé into a new, updated package that is relevant for programmers working with (or planning to work with) the latest version of JavaScript. _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- The original JavaScript Allongé was not just written to teach JavaScript: It was written to describe certain ideas in programming: Working with small, independent entities that compose together to make bigger programs. _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- And introducing these new ideas did add substantially to its bulk. _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- Introducing so many new ideas did require a major rethink of the way the book was organized. _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- As noted above, JavaScript was chosen as the language for Allongé because it hit a sweet spot of having a large audience of programmers and having certain language features that happen to work well with this style of programming. _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- Not having to work around these kinds of missing features makes JavaScript Allongé a _better book_ , because it can focus on the _why_ to do something and _when_ to do it, instead of on the how to make it work _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- If it were just a matter of updating the syntax, the original version of JavaScript Allongé could have simply iterated, slowly replacing old syntax with new. _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- ECMAScript 2015 does more than simply update the language with some simpler syntax for a few things and help us avoid warts. _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- As noted above, JavaScript was chosen as the language for Allongé because it hit a sweet spot of having a large audience of programmers and having certain language features that happen to work well with this style of programming. _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- It would have continued to say much the same things, only with new syntax. _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- Not having to work around these kinds of missing features makes JavaScript Allongé a _better book_ , because it can focus on the _why_ to do something and _when_ to do it, instead of on the how to make it work _(javascriptallonge.pdf (source-range-83ecb080-00014))_

## What JavaScript Allongé is. And isn't.

- But while JavaScript Allongé attempts to be provocative, it is not _prescriptive_ . _(javascriptallonge.pdf (source-range-83ecb080-00016))_
- JavaScript Allongé is a book about programming with functions. _(javascriptallonge.pdf (source-range-83ecb080-00016))_
- People often say that software should be written for people to read. _(javascriptallonge.pdf (source-range-83ecb080-00016))_
- There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others. _(javascriptallonge.pdf (source-range-83ecb080-00016))_
- Choices in software development are also often driven by requirements specific to the type of software being developed. _(javascriptallonge.pdf (source-range-83ecb080-00016))_
- The focus in this book on the underlying ideas, what we might call the fundamentals, and how they combine to form new ideas. _(javascriptallonge.pdf (source-range-83ecb080-00016))_
- The intention is to improve the way we think about programs. _(javascriptallonge.pdf (source-range-83ecb080-00016))_
- Software development is a complex field. _(javascriptallonge.pdf (source-range-83ecb080-00016))_
- Choices in development are often driven by social considerations. _(javascriptallonge.pdf (source-range-83ecb080-00016))_
- For example, business software written in-house has a very different set of requirements than a library written to be publicly distributed as open-source. _(javascriptallonge.pdf (source-range-83ecb080-00016))_
- For example, business software written in-house has a very different set of requirements than a library written to be publicly distributed as open-source. _(javascriptallonge.pdf (source-range-83ecb080-00016))_
- There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others. _(javascriptallonge.pdf (source-range-83ecb080-00016))_
- Debuggers encourage the use of functions with explicit or implicit names. _(javascriptallonge.pdf (source-range-83ecb080-00017))_
- The use of linters[1] makes checking for certain types of undesirable code very cheap. _(javascriptallonge.pdf (source-range-83ecb080-00017))_
- Continuous integration encourages the creation of software in tandem with and factored to facilitate the creation of automated test suites. _(javascriptallonge.pdf (source-range-83ecb080-00017))_
- JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn’t a book about practicing, it’s a book about thinking. _(javascriptallonge.pdf (source-range-83ecb080-00017))_
- Code examples within each chapter are small and emphasize exposition rather than serving as patterns for everyday use. _(javascriptallonge.pdf (source-range-83ecb080-00017))_
- Choices in software development must also consider the question of consistency. _(javascriptallonge.pdf (source-range-83ecb080-00017))_
- Finally, choices in software development cannot ignore the tooling that is used to create and maintain software. _(javascriptallonge.pdf (source-range-83ecb080-00017))_
- The use of source-code control systems with integrated diffing rewards making certain types of focused changes. _(javascriptallonge.pdf (source-range-83ecb080-00017))_
- Code examples within each chapter are small and emphasize exposition rather than serving as patterns for everyday use. _(javascriptallonge.pdf (source-range-83ecb080-00017))_
- JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn’t a book about practicing, it’s a book about thinking. _(javascriptallonge.pdf (source-range-83ecb080-00017))_
- Following some of the chapters are a series of recipes designed to show the application of the chapter’s ideas in practical form. _(javascriptallonge.pdf (source-range-83ecb080-00018))_
- While the content of each chapter builds naturally on what was discussed in the previous chapter, the recipes may draw upon any aspect of the JavaScript programming language. _(javascriptallonge.pdf (source-range-83ecb080-00018))_

## Foreword to the ``Six'' edition

- This upgrade became ECMAScript 6 (some features that were initially discussed will show up later, in upcoming ECMAScript versions). _(javascriptallonge.pdf (source-range-83ecb080-00020))_
- _JavaScript Allongé, the “Six” Edition_ is both a comprehensive tour of its features and a rich collection of techniques for making better use of them. _(javascriptallonge.pdf (source-range-83ecb080-00020))_
- And you’ll do so via ES6 code, handed to you in small, easily digestible pieces. _(javascriptallonge.pdf (source-range-83ecb080-00020))_
- With ECMAScript 6, JavaScript has become much larger as a language. _(javascriptallonge.pdf (source-range-83ecb080-00020))_
- That version was planned to have numerous new features (interfaces, namespaces, packages, multimethods, etc.), which would have turned JavaScript into a completely new language. _(javascriptallonge.pdf (source-range-83ecb080-00020))_
- - A larger upgrade would substantially improve JavaScript, but without being as radical as ECMAScript 4. _(javascriptallonge.pdf (source-range-83ecb080-00020))_
- - A smaller upgrade would bring a few minor enhancements to ECMAScript 3. _(javascriptallonge.pdf (source-range-83ecb080-00020))_
- You will learn much about functional programming and object-oriented programming. _(javascriptallonge.pdf (source-range-83ecb080-00020))_
- After internal conflict, a settlement was reached in July 2008 and a new plan was made – to abandon ECMAScript 4 and to replace it with two upgrades: _(javascriptallonge.pdf (source-range-83ecb080-00020))_
- Getting there took a while – in a way, the origins of ES6 date back to the year 2000: After ECMAScript 3 was finished, TC39 (the committee evolving JavaScript) started to work on ECMAScript 4. _(javascriptallonge.pdf (source-range-83ecb080-00020))_
- ECMAScript 6 (short name: ES6; official name: ECMAScript 2015) was ratified as a standard on June 17. _(javascriptallonge.pdf (source-range-83ecb080-00020))_
- Getting there took a while – in a way, the origins of ES6 date back to the year 2000: After ECMAScript 3 was finished, TC39 (the committee evolving JavaScript) started to work on ECMAScript 4. _(javascriptallonge.pdf (source-range-83ecb080-00020))_
- After internal conflict, a settlement was reached in July 2008 and a new plan was made – to abandon ECMAScript 4 and to replace it with two upgrades: _(javascriptallonge.pdf (source-range-83ecb080-00020))_

## Forewords to the First Edition

- However, the process of soliciting feedback, gathering responses, sending out copies, waiting for people to actually read it (if they ever do), receiving feedback and then ultimately making sense out of how to use it takes weeks and sometimes months. _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- A Pull of the Lever: Prefaces As a life-long bibliophile and long-time follower of Reg’s online work, I was excited when he started writing books. _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- Instead, every section is motivated by relevant dialog and fortified with compelling source examples. _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- Not only was this a great book, but it was also a great way to write and distribute books. _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- – Fogus, fogus.me[5] A different kind of language requires a different kind of book. _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- However, you’ll not be beaten about the head and neck with dogma. _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- As a staunch advocate of functional programming, much of what Reg has written rings true to me. _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- Reg has crafted (and continues to craft) not only an interesting book from the perspective of a connoisseur, but also an entertaining exploration into some of the most interesting aspects of his art. _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- JavaScript holds surprising depths–its scoping rules are neither strictly lexical nor strictly dynamic, and it supports procedural, object-oriented (in several flavors!), and functional programming. _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- The act of writing is an iterative process with (very often) tight revision loops. _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time. _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- However, I’m very conservative about books – let’s just say that if there was an aftershave scented to the essence of “Used Book Store” then I would be first in line to buy. _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- However, Reg sent me a copy of his book and I was humbled. _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- No matter how much of an expert you think you are, JavaScript Allongé has something to teach you… about coffee. _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- On more than one occasion I’ve found myself attempting to reify feedback with content that either no longer existed or was changed beyond recognition. _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- Not only was this a great book, but it was also a great way to write and distribute books. _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- However, I’m very conservative about books – let’s just say that if there was an aftershave scented to the essence of “Used Book Store” then I would be first in line to buy. _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- However, the process of soliciting feedback, gathering responses, sending out copies, waiting for people to actually read it (if they ever do), receiving feedback and then ultimately making sense out of how to use it takes weeks and sometimes months. _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- Reg has crafted (and continues to craft) not only an interesting book from the perspective of a connoisseur, but also an entertaining exploration into some of the most interesting aspects of his art. _(javascriptallonge.pdf (source-range-83ecb080-00022))_

## About The Sample PDF

- If you read _JavaScript Allongé, The “six” edition_ and it doesn’t blow your mind, your money will be cheerfully refunded. _(javascriptallonge.pdf (source-range-83ecb080-00025))_
- This sample edition of the book includes just a portion of the complete book. _(javascriptallonge.pdf (source-range-83ecb080-00025))_

## Prelude: Values and Expressions over Coffee

## values are expressions

- The grandfather of such languages is Lisp. _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- Yup, you hand over a cup with some coffee infused through partially caramelized sugar. _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- You say, “I want one of these.” The barista is no fool, she gives it straight back to you, and you get exactly what you want. _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- The answer is, this is both an expression _and_ a value.[10] The way you can tell that it’s both is very easy: When you type it into JavaScript, you get the same thing back, just like our café Cubano: _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- Ground coffee is a value. _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- So, boiling water plus ground coffee is an expression, but it isn’t a value.[11] Boiling water is a value. _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- All values are expressions. _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- All values are expressions. _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- Instead of handing over the finished coffee, we can hand over the ingredients. _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- Astute readers will realize we’re omitting something. _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- You and I both understand that this means “42,” and so does the computer. _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- Boiling water plus ground coffee is an expression. _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- > 11In some languages, expressions are a kind of value unto themselves and can be manipulated. _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- JavaScript is not such a language, expressions in and of themselves are not values. _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- You and I both understand that this means “42,” and so does the computer. _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- But strings with operators are not values, they are expressions. _(javascriptallonge.pdf (source-range-83ecb080-00031))_
- Now we see that “strings” are values, and you can make an expression out of strings and an operator +. _(javascriptallonge.pdf (source-range-83ecb080-00031))_
- The coffee grounds were a value, the boiling hot water was a value, and the “plus” operator between them made the whole thing an expression that was not a value. _(javascriptallonge.pdf (source-range-83ecb080-00031))_
- Now we know what was missing with our “coffee grounds plus hot water” example. _(javascriptallonge.pdf (source-range-83ecb080-00031))_
- Since strings are values, they are also expressions by themselves. _(javascriptallonge.pdf (source-range-83ecb080-00031))_

## values and identity

- One is a demitasse, the other a mug. _(javascriptallonge.pdf (source-range-83ecb080-00033))_
- This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2. _(javascriptallonge.pdf (source-range-83ecb080-00033))_
- One holds a single, one a double. _(javascriptallonge.pdf (source-range-83ecb080-00033))_
- This corresponds to comparing two things in JavaScript that have different _types_ . _(javascriptallonge.pdf (source-range-83ecb080-00033))_
- First, sometimes, the cups are of different kinds. _(javascriptallonge.pdf (source-range-83ecb080-00033))_
- For example, the string "2" is not the same thing as the number 2. _(javascriptallonge.pdf (source-range-83ecb080-00033))_
- This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2. _(javascriptallonge.pdf (source-range-83ecb080-00033))_
- For example, the string "2" is not the same thing as the number 2. _(javascriptallonge.pdf (source-range-83ecb080-00033))_
- Third, some types of cups have no distinguishing marks on them. _(javascriptallonge.pdf (source-range-83ecb080-00034))_
- So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them. _(javascriptallonge.pdf (source-range-83ecb080-00034))_
- Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. _(javascriptallonge.pdf (source-range-83ecb080-00034))_
- If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. _(javascriptallonge.pdf (source-range-83ecb080-00034))_
- We haven’t encountered the fourth possibility yet. _(javascriptallonge.pdf (source-range-83ecb080-00034))_
- We’ll use both terms interchangeably. _(javascriptallonge.pdf (source-range-83ecb080-00034))_
- Let’s meet a data structure that is very common in contemporary programming languages, the _Array_ (other languages sometimes call it a List or a Vector). _(javascriptallonge.pdf (source-range-83ecb080-00034))_
- This is the case with the strings, numbers, and booleans we have seen so far. _(javascriptallonge.pdf (source-range-83ecb080-00034))_
- This is an expression, and you can combine [] with other expressions. _(javascriptallonge.pdf (source-range-83ecb080-00035))_
- Every time you evaluate an expression (including typing something in) to create an array, you’re creating a new, distinct value even if it _appears_ to be the same as some other array value. _(javascriptallonge.pdf (source-range-83ecb080-00035))_
- [2-1, 2, 2+1] [1, 1+1, 1+1+1] Notice that you are always generating arrays with the same contents. _(javascriptallonge.pdf (source-range-83ecb080-00035))_
- They look the same, but if you examine them with ===, you see that they are different. _(javascriptallonge.pdf (source-range-83ecb080-00035))_
- As we’ll see, this is true of many other kinds of values, including _functions_ , the main subject of this book. _(javascriptallonge.pdf (source-range-83ecb080-00035))_
- When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own _unique_ array that is not identical to any other array, even if that other array also looks like [1, 2, 3]. _(javascriptallonge.pdf (source-range-83ecb080-00035))_

## A Rich Aroma: Basic Numbers

- In computer science, a literal is a notation for representing a fixed value in source code. _(javascriptallonge.pdf (source-range-83ecb080-00037))_
- We saw that an expression consisting solely of numbers, like 42, is a literal. _(javascriptallonge.pdf (source-range-83ecb080-00037))_
- It represents the number forty-two, which is 42 base 10. _(javascriptallonge.pdf (source-range-83ecb080-00037))_
- Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. _(javascriptallonge.pdf (source-range-83ecb080-00037))_
- Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. _(javascriptallonge.pdf (source-range-83ecb080-00037))_
- If we start a literal with a zero, it is an octal literal. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- We can, for example, write 1.5 or 33.33, and JavaScript represents these literals as floating point numbers. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- The machine’s representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer’s behaviour surprises us if we don’t know a little about what it’s doing “under the hood.” For example, the largest integer JavaScript can safely[14] handle is 9007199254740991, or 2[‘53‘] - 1. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- > 14Implementations of JavaScript are free to handle larger numbers. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- It’s tempting to think we now have everything we need to do things like handle amounts of money, but as the late John Belushi would say, “Nooooooooooooooooooooo.” A computer’s internal representation for a floating point number is binary, while our literal number was in base ten. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- A computer’s internal representation for numbers is important to understand. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- But we mentioned that numbers are represented internally as floating point, meaning that they need not be just integers. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- 2 all numbers are base ten. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- So the literal 042 is 42 base 8, which is actually 34 base 10. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- Internally, both 042 and 34 have the same representation, as double-precision floating point[13] numbers. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- The machine’s representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer’s behaviour surprises us if we don’t know a little about what it’s doing “under the hood.” For example, the largest integer JavaScript can safely[14] handle is 9007199254740991, or 2[‘53‘] - 1. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- We can, for example, write 1.5 or 33.33, and JavaScript represents these literals as floating point numbers. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- This kind of “inexactitude” can be ignored when performing calculations that have an acceptable deviation. _(javascriptallonge.pdf (source-range-83ecb080-00039))_
- These can be combined to make more complex expressions, like 2 * 5 + 1. _(javascriptallonge.pdf (source-range-83ecb080-00039))_
- In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. _(javascriptallonge.pdf (source-range-83ecb080-00039))_
- JavaScript has many more operators. _(javascriptallonge.pdf (source-range-83ecb080-00039))_
- Professional programmers almost never use floating point numbers to represent monetary amounts. _(javascriptallonge.pdf (source-range-83ecb080-00039))_
- But as a rule, if you need to work with real numbers, you should have more than a nodding acquaintance with the IEEE Standard for Floating-Point Arithmetic[15] . _(javascriptallonge.pdf (source-range-83ecb080-00039))_
- In this book, we need not think about such details, but outside of this book, we must. _(javascriptallonge.pdf (source-range-83ecb080-00039))_
- As we’ve seen, JavaScript has many common arithmetic operators. _(javascriptallonge.pdf (source-range-83ecb080-00039))_
- For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript’s calculation is less than a pixel, there is no observable error. _(javascriptallonge.pdf (source-range-83ecb080-00039))_
- For example, “$43.21” will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21. _(javascriptallonge.pdf (source-range-83ecb080-00039))_
- For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript’s calculation is less than a pixel, there is no observable error. _(javascriptallonge.pdf (source-range-83ecb080-00039))_
- For example, “$43.21” will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21. _(javascriptallonge.pdf (source-range-83ecb080-00039))_

## The first sip: Basic Functions

## As Little As Possible About Functions, But No Less

- [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. _(javascriptallonge.pdf (source-range-83ecb080-00044))_
- Like numbers, strings, and arrays, they have a representation. _(javascriptallonge.pdf (source-range-83ecb080-00044))_
- This is a function that is applied to no values and returns 0. _(javascriptallonge.pdf (source-range-83ecb080-00044))_
- If you try the same thing in a browser, you may see something else. _(javascriptallonge.pdf (source-range-83ecb080-00044))_
- The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. _(javascriptallonge.pdf (source-range-83ecb080-00044))_
- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. _(javascriptallonge.pdf (source-range-83ecb080-00044))_
- Functions represent computations to be performed. _(javascriptallonge.pdf (source-range-83ecb080-00044))_
- This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. _(javascriptallonge.pdf (source-range-83ecb080-00044))_
- Reference types do not. _(javascriptallonge.pdf (source-range-83ecb080-00045))_
- But we must understand that whether we see [Function] or () => 0, internally JavaScript has a full and proper function. _(javascriptallonge.pdf (source-range-83ecb080-00045))_
- “Function” is a reference type. _(javascriptallonge.pdf (source-range-83ecb080-00045))_
- > 17If you’re used to other programming languages, you’ve probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. _(javascriptallonge.pdf (source-range-83ecb080-00045))_
- Value types share the same identity if they have the same contents. _(javascriptallonge.pdf (source-range-83ecb080-00045))_
- You recall that we have two types of values with respect to identity: Value types and reference types. _(javascriptallonge.pdf (source-range-83ecb080-00045))_
- I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. _(javascriptallonge.pdf (source-range-83ecb080-00045))_
- The way we use functions is to _apply_ them to zero or more values called _arguments_ . _(javascriptallonge.pdf (source-range-83ecb080-00045))_
- We’ll put it in parentheses[17] to keep the parser happy, like we did above: (() => 0). _(javascriptallonge.pdf (source-range-83ecb080-00045))_
- Right now, we only know about one such expression: () => 0, so let’s use it. _(javascriptallonge.pdf (source-range-83ecb080-00045))_
- Here’s how we apply a function to some values in JavaScript: Let’s say that _fn_expr_ is an expression that when evaluated, produces a function. _(javascriptallonge.pdf (source-range-83ecb080-00045))_
- Right now, we only know about one such expression: () => 0, so let’s use it. _(javascriptallonge.pdf (source-range-83ecb080-00045))_
- Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow. _(javascriptallonge.pdf (source-range-83ecb080-00046))_
- Values like 0 are expressions, as are things like 40 + 2. _(javascriptallonge.pdf (source-range-83ecb080-00046))_
- We can put any expression to the right of the arrow. _(javascriptallonge.pdf (source-range-83ecb080-00046))_
- We know that (() => 0)() returns 0, and this is unsurprising. _(javascriptallonge.pdf (source-range-83ecb080-00046))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-83ecb080-00046))_
- Likewise, the following all ought to be obvious: (() => 1)() _//=> 1_ (() => "Hello, JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** )() _//=> Infinity_ _(javascriptallonge.pdf (source-range-83ecb080-00046))_
- Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-83ecb080-00046))_
- In the prelude, we looked at expressions. _(javascriptallonge.pdf (source-range-83ecb080-00046))_
- When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out. _(javascriptallonge.pdf (source-range-83ecb080-00046))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-83ecb080-00046))_
- In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. _(javascriptallonge.pdf (source-range-83ecb080-00047))_
- This is useful when trying to do things that might involve _side-effects_ , but we’ll get to that later. _(javascriptallonge.pdf (source-range-83ecb080-00047))_
- The comma operator in JavaScript is interesting. _(javascriptallonge.pdf (source-range-83ecb080-00047))_
- There’s another thing we can put to the right of an arrow, a _block_ . _(javascriptallonge.pdf (source-range-83ecb080-00048))_
- > 18Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons. _(javascriptallonge.pdf (source-range-83ecb080-00048))_
- Like numbers, booleans and strings, JavaScript can print out the value undefined. _(javascriptallonge.pdf (source-range-83ecb080-00048))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-83ecb080-00048))_
- No matter how you evaluate undefined, you get an identical value back. _(javascriptallonge.pdf (source-range-83ecb080-00048))_
- It returns the result of evaluating a block that has no statements. _(javascriptallonge.pdf (source-range-83ecb080-00048))_
- A block has zero or more _statements_ , separated by semicolons.[18] So, this is a valid function: _(javascriptallonge.pdf (source-range-83ecb080-00048))_
- In JavaScript, the absence of a value is written undefined, and it means there is no value. _(javascriptallonge.pdf (source-range-83ecb080-00048))_
- It will crop up again. _(javascriptallonge.pdf (source-range-83ecb080-00048))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-83ecb080-00048))_
- In JavaScript, the absence of a value is written undefined, and it means there is no value. _(javascriptallonge.pdf (source-range-83ecb080-00048))_
- > 21You can also separate statements with line breaks. _(javascriptallonge.pdf (source-range-83ecb080-00050))_
- Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00050))_
- This feature was originally created as a kind of helpful error-correction. _(javascriptallonge.pdf (source-range-83ecb080-00050))_
- An expression is a JavaScript statement. _(javascriptallonge.pdf (source-range-83ecb080-00050))_
- Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. _(javascriptallonge.pdf (source-range-83ecb080-00050))_
- There are many kinds of JavaScript statements, but the first kind is one we’ve already met. _(javascriptallonge.pdf (source-range-83ecb080-00050))_
- Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. _(javascriptallonge.pdf (source-range-83ecb080-00050))_
- For example, you can’t use one as the expression in a simple function, because it isn’t an expression: _(javascriptallonge.pdf (source-range-83ecb080-00051))_
- The return statement is the first statement we’ve seen, and it behaves differently than an expression. _(javascriptallonge.pdf (source-range-83ecb080-00051))_
- For example, you can’t use one as the expression in a simple function, because it isn’t an expression: _(javascriptallonge.pdf (source-range-83ecb080-00051))_
- It’s a function that when applied, evaluates to a function that when applied, evaluates to 0. _(javascriptallonge.pdf (source-range-83ecb080-00052))_
- So we have _a function, that returns a function, that returns zero_ . _(javascriptallonge.pdf (source-range-83ecb080-00052))_
- Diffraction of a crystal is beautiful and interesting in its own right, but you can’t blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. _(javascriptallonge.pdf (source-range-83ecb080-00052))_
- So… In the next chapter, “I’d Like to Have an Argument, Please,” we’ll see how to make functions practical. _(javascriptallonge.pdf (source-range-83ecb080-00052))_
- We’ve been very clever, but so far this all seems very abstract. _(javascriptallonge.pdf (source-range-83ecb080-00052))_
- Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types. _(javascriptallonge.pdf (source-range-83ecb080-00054))_
- JavaScript places _references_ to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-83ecb080-00054))_
- JavaScript does not place copies of reference values in any environment. _(javascriptallonge.pdf (source-range-83ecb080-00054))_
- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. _(javascriptallonge.pdf (source-range-83ecb080-00054))_
- 20 are identical to each other if they have the same content. _(javascriptallonge.pdf (source-range-83ecb080-00054))_
- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. _(javascriptallonge.pdf (source-range-83ecb080-00054))_

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00054))_

> So JavaScript can make as many copies of strings, numbers, or booleans as it wishes.

## Closures and Scope

- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from “outside” of a function that are referenced inside a function. _(javascriptallonge.pdf (source-range-83ecb080-00056))_
- First off, let’s use what we learned above. _(javascriptallonge.pdf (source-range-83ecb080-00056))_
- There is no x in its environment, it must come from somewhere else. _(javascriptallonge.pdf (source-range-83ecb080-00056))_
- It makes sense that the result value is a function, because the expression for (x) => ...’s body is: So now we have a value representing that function. _(javascriptallonge.pdf (source-range-83ecb080-00056))_
- Now let’s enjoy a relaxed Allongé before we continue! _(javascriptallonge.pdf (source-range-83ecb080-00056))_
- Now let’s enjoy a relaxed Allongé before we continue! _(javascriptallonge.pdf (source-range-83ecb080-00056))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from “outside” of a function that are referenced inside a function. _(javascriptallonge.pdf (source-range-83ecb080-00056))_
- It makes sense that the result value is a function, because the expression for (x) => ...’s body is: So now we have a value representing that function. _(javascriptallonge.pdf (source-range-83ecb080-00056))_
- 27You may also hear the term “non-local variable.” Both are correct. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- From this, we learn something: A pure function can contain a closure. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- We can’t say what it will do with argument (2) without understanding the magic for evaluating the free variable x. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- Pure functions are easiest to understand. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- They always mean the same thing wherever you use them. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- - Functions containing no free variables are called _pure functions_ . _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- - Functions containing one or more free variables are called _closures_ . _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- The first function doesn’t have any variables, therefore doesn’t have any free variables. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- Using only what we’ve learned so far, attempt to compose a closure that contains a pure function. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- It contains a _free variable_ , x.[27] A free variable is one that is not bound within the function. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- The second doesn’t have any free variables, because its only variable is bound. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- The third one is actually two functions, one inside the other. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- If you can’t, give your reasoning for why it’s impossible. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- The second doesn’t have any free variables, because its only variable is bound. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- Using only what we’ve learned so far, attempt to compose a closure that contains a pure function. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- The third one is actually two functions, one inside the other. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- It contains a _free variable_ , x.[27] A free variable is one that is not bound within the function. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- The first function doesn’t have any variables, therefore doesn’t have any free variables. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- The variable x isn’t in (y) => ...’s immediate environment, but it is in its parent’s environment, so it evaluates to 1 and that’s what ((y) => x)(2) returns even though it ended up ignoring its own argument. _(javascriptallonge.pdf (source-range-83ecb080-00058))_
- Some people get so excited by this that they write entire books about them, some are great _[a]_ , some–how shall I put this–are interesting _[b]_ if you use Ruby. _(javascriptallonge.pdf (source-range-83ecb080-00058))_
- To understand how closures are evaluated, we need to revisit environments. _(javascriptallonge.pdf (source-range-83ecb080-00058))_
- We also hand-waved something when describing our environment. _(javascriptallonge.pdf (source-range-83ecb080-00058))_
- So whenever a function is applied to arguments, its environment always has a reference to its parent environment. _(javascriptallonge.pdf (source-range-83ecb080-00058))_
- The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3). _(javascriptallonge.pdf (source-range-83ecb080-00058))_
- As we’ve said before, all functions are associated with an environment. _(javascriptallonge.pdf (source-range-83ecb080-00058))_
- As we’ve said before, all functions are associated with an environment. _(javascriptallonge.pdf (source-range-83ecb080-00058))_
- Calling a curried function with only some of its arguments is sometimes called partial application _[b]_ . _(javascriptallonge.pdf (source-range-83ecb080-00059))_
- This is often a good thing. _(javascriptallonge.pdf (source-range-83ecb080-00059))_
- The x in the great-great-grandparent scope is ignored, as are both ws. _(javascriptallonge.pdf (source-range-83ecb080-00059))_
- When a variable has the same name as an ancestor environment’s binding, it is said to _shadow_ the ancestor. _(javascriptallonge.pdf (source-range-83ecb080-00059))_
- An interesting thing happens when a variable has the same name as an ancestor environment’s variable. _(javascriptallonge.pdf (source-range-83ecb080-00059))_
- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. _(javascriptallonge.pdf (source-range-83ecb080-00059))_
- When evaluating x + y + z, JavaScript will find x and y in the great-grandparent scope and z in the parent scope. _(javascriptallonge.pdf (source-range-83ecb080-00059))_
- Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-83ecb080-00059))_
- The first function is the result of currying _[a]_ the second function. _(javascriptallonge.pdf (source-range-83ecb080-00059))_
- Although its parent also defines an x, it is ignored when evaluating x + y. _(javascriptallonge.pdf (source-range-83ecb080-00059))_
- Calling a curried function with only some of its arguments is sometimes called partial application _[b]_ . _(javascriptallonge.pdf (source-range-83ecb080-00059))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. _(javascriptallonge.pdf (source-range-83ecb080-00060))_
- As we’ll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program. _(javascriptallonge.pdf (source-range-83ecb080-00060))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. _(javascriptallonge.pdf (source-range-83ecb080-00060))_

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00059))_

> The first sip: Basic Functions 24 The first function is the result of currying _[a]_ the second function. Calling a curried function with only some of its arguments is sometimes called partial application _[b]_ . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. > _a_ https://en.wikipedia.org/wiki/Currying > _b_ https://en.wikipedia.org/wiki/Partial_application ## **shadowy variables from a shadowy planet** An interesting thin

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00060))_

> If you don’t want your code to operate directly within the global environment, what can you do?

## That Constant Coffee Craving

- This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. _(javascriptallonge.pdf (source-range-83ecb080-00062))_
- Up to now, all we’ve really seen are _anonymous functions_ , functions that don’t have a name. _(javascriptallonge.pdf (source-range-83ecb080-00062))_
- In order to bind 3.14159265 to the name PI, we’ll need a function with a parameter of PI applied to an argument of 3.14159265. _(javascriptallonge.pdf (source-range-83ecb080-00062))_
- There are other ways to name things in JavaScript, but before we learn some of those, let’s see how to use what we already have to name things. _(javascriptallonge.pdf (source-range-83ecb080-00062))_
- But we can use it just like (diameter) => diameter * 3.14159265. _(javascriptallonge.pdf (source-range-83ecb080-00062))_
- Naming things is a critical part of programming, but all we’ve seen so far is how to name arguments. _(javascriptallonge.pdf (source-range-83ecb080-00062))_
- All of our “functions” are expressions. _(javascriptallonge.pdf (source-range-83ecb080-00062))_
- This one has a few more moving parts, that’s all. _(javascriptallonge.pdf (source-range-83ecb080-00062))_
- There are other ways to name things in JavaScript, but before we learn some of those, let’s see how to use what we already have to name things. _(javascriptallonge.pdf (source-range-83ecb080-00062))_
- A “magic literal” like 3.14159265 is anathema to sustainable software development. _(javascriptallonge.pdf (source-range-83ecb080-00063))_
- The third one is easiest for most people to read. _(javascriptallonge.pdf (source-range-83ecb080-00063))_
- > 29JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-83ecb080-00063))_
- We can bind anything we want in an expression by wrapping it in a function that is immediately invoked with the value we want to bind.[29] There’s another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-83ecb080-00063))_
- Well, the first one seems simplest, but a half-century of experience has taught us that names matter. _(javascriptallonge.pdf (source-range-83ecb080-00063))_
- > 29JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-83ecb080-00063))_
- We can bind anything we want in an expression by wrapping it in a function that is immediately invoked with the value we want to bind.[29] There’s another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-83ecb080-00063))_
- Everything else is encapsulated in its body. _(javascriptallonge.pdf (source-range-83ecb080-00064))_
- - (diameter) => ((PI) => diameter * PI)(3.14159265) Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. _(javascriptallonge.pdf (source-range-83ecb080-00064))_
- That’s how it should be, naming PI is its concern, not ours. _(javascriptallonge.pdf (source-range-83ecb080-00064))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. _(javascriptallonge.pdf (source-range-83ecb080-00064))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. _(javascriptallonge.pdf (source-range-83ecb080-00064))_
- This differs from our example above in that there is only one environment, rather than two. _(javascriptallonge.pdf (source-range-83ecb080-00065))_
- JavaScript gives us a way to do that, the const keyword. _(javascriptallonge.pdf (source-range-83ecb080-00065))_
- We have one binding in the environment representing our regular argument, and another our “constant.” That’s more efficient, and it’s _almost_ what we wanted all along: A way to bind 3.14159265 to a readable name. _(javascriptallonge.pdf (source-range-83ecb080-00065))_
- That’s much better than what we were writing. _(javascriptallonge.pdf (source-range-83ecb080-00065))_
- We use the const keyword in a _const statement_ . _(javascriptallonge.pdf (source-range-83ecb080-00065))_
- This differs from our example above in that there is only one environment, rather than two. _(javascriptallonge.pdf (source-range-83ecb080-00065))_
- A name that’s bound to a function is a valid expression evaluating to a function.[30] Amazing how such an important idea–naming functions–can be explained _en passant_ in just a few words. _(javascriptallonge.pdf (source-range-83ecb080-00066))_
- This underscores what we’ve said: if we have an expression that evaluates to a function, we apply it with (). _(javascriptallonge.pdf (source-range-83ecb080-00066))_
- We can bind more than one name-value pair by separating them with commas. _(javascriptallonge.pdf (source-range-83ecb080-00066))_
- We can bind any expression. _(javascriptallonge.pdf (source-range-83ecb080-00066))_
- But there are other kinds of blocks. _(javascriptallonge.pdf (source-range-83ecb080-00067))_
- The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. _(javascriptallonge.pdf (source-range-83ecb080-00067))_
- Up to now, we’ve only ever seen blocks we use as the body of functions. _(javascriptallonge.pdf (source-range-83ecb080-00067))_
- Up to now, we’ve only ever seen blocks we use as the body of functions. _(javascriptallonge.pdf (source-range-83ecb080-00067))_
- We’ve used a block as the else clause, and since it’s a block, we’ve placed a const statement inside it. _(javascriptallonge.pdf (source-range-83ecb080-00068))_
- Here’s the second formulation of our diameter function, bound to a name using an IIFE: ((diameter_fn) => _// ..._ )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) It’s more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we’ve elided. _(javascriptallonge.pdf (source-range-83ecb080-00068))_
- We can use any expression in there, and that expression can invoke diameter_fn. _(javascriptallonge.pdf (source-range-83ecb080-00068))_
- This seems very straightforward, but alas, there are some semantics of binding names that we need to understand if we’re to place const anywhere we like. _(javascriptallonge.pdf (source-range-83ecb080-00068))_
- We’ve used a block as the else clause, and since it’s a block, we’ve placed a const statement inside it. _(javascriptallonge.pdf (source-range-83ecb080-00068))_
- We can test this by deliberately creating a “conflict:” ((diameter_fn) => ((PI) => diameter_fn(2) )(3) )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) _//=> 6.2831853_ Although we have bound 3 to PI in the environment surrounding diameter_fn(2), the value that counts is 3.14159265, the value we bound to PI in the environment surrounding (diameter) _⇒_ diameter * PI. _(javascriptallonge.pdf (source-range-83ecb080-00069))_
- This is called lexical scoping[31] , because we can discover where a name is bound by looking at the source code for the program. _(javascriptallonge.pdf (source-range-83ecb080-00069))_
- We can see that PI is bound in an environment surrounding (diameter) => diameter * PI, we don’t need to know where diameter_fn is invoked. _(javascriptallonge.pdf (source-range-83ecb080-00069))_
- That much we can carefully work out from the way closures work. _(javascriptallonge.pdf (source-range-83ecb080-00069))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2), PI _is_ bound when we evaluated (diameter) => diameter * PI, and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn. _(javascriptallonge.pdf (source-range-83ecb080-00069))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2), PI _is_ bound when we evaluated (diameter) => diameter * PI, and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn. _(javascriptallonge.pdf (source-range-83ecb080-00069))_
- This is called lexical scoping[31] , because we can discover where a name is bound by looking at the source code for the program. _(javascriptallonge.pdf (source-range-83ecb080-00069))_
- Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions. _(javascriptallonge.pdf (source-range-83ecb080-00070))_
- Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-83ecb080-00070))_
- They are looked up in the environment where they are declared. _(javascriptallonge.pdf (source-range-83ecb080-00070))_
- But instead of binding two different variables to the same name in two different places, we’ll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-83ecb080-00070))_
- We just saw that values bound with const use lexical scope, just like values bound with parameters. _(javascriptallonge.pdf (source-range-83ecb080-00070))_
- We can test this by creating another conflict. _(javascriptallonge.pdf (source-range-83ecb080-00070))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. _(javascriptallonge.pdf (source-range-83ecb080-00070))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. _(javascriptallonge.pdf (source-range-83ecb080-00070))_
- It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-83ecb080-00071))_
- This is a book, you’ve already scanned ahead, so you know that the answer is **no** , the inner binding does not overwrite the outer binding: _(javascriptallonge.pdf (source-range-83ecb080-00071))_
- It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-83ecb080-00071))_
- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-83ecb080-00072))_
- We’ll need a gratuitous block. _(javascriptallonge.pdf (source-range-83ecb080-00072))_
- Parameters are only bound when we invoke a function. _(javascriptallonge.pdf (source-range-83ecb080-00072))_
- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-83ecb080-00072))_
- Parameters are only bound when we invoke a function. _(javascriptallonge.pdf (source-range-83ecb080-00072))_
- This design rule is called the Principle of Least Privilege[32] , and it has both quality and security implications. _(javascriptallonge.pdf (source-range-83ecb080-00073))_
- Typically, we want to bind our names as close to where we need them as possible. _(javascriptallonge.pdf (source-range-83ecb080-00073))_
- If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. _(javascriptallonge.pdf (source-range-83ecb080-00073))_
- This design rule is called the Principle of Least Privilege[32] , and it has both quality and security implications. _(javascriptallonge.pdf (source-range-83ecb080-00073))_
- If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. _(javascriptallonge.pdf (source-range-83ecb080-00073))_
- We can _shadow_ it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-83ecb080-00074))_
- This is valuable, as it greatly simplifies the analysis of programs to see at a glance that when something is bound with const, we need never worry that its value may change. _(javascriptallonge.pdf (source-range-83ecb080-00074))_
- While the name of the function is a property of the function, not of the environment. _(javascriptallonge.pdf (source-range-83ecb080-00076))_
- Confusingly, the name of the function is not exactly the same thing as the name we may choose to bind to the value of the function. _(javascriptallonge.pdf (source-range-83ecb080-00076))_
- That may seem confusing, but think of the binding names as properties of the environment, not of the function. _(javascriptallonge.pdf (source-range-83ecb080-00076))_
- This is a _named function expression_ . _(javascriptallonge.pdf (source-range-83ecb080-00076))_
- > 33“Yes of course?” Well, in chapter of a book dedicated to naming functions, it is not surprising that feature we mention has something to do with naming functions. _(javascriptallonge.pdf (source-range-83ecb080-00076))_
- Clearly, the name even is bound to the function _within the function’s body_ . _(javascriptallonge.pdf (source-range-83ecb080-00077))_
- Now, the function’s actual name has no effect on the environment in which it is used. _(javascriptallonge.pdf (source-range-83ecb080-00077))_
- Here’s a function that determines whether a positive integer is even or not. _(javascriptallonge.pdf (source-range-83ecb080-00077))_
- Function declarations are formally only supposed to be made at what we might call the “top level” of a function. _(javascriptallonge.pdf (source-range-83ecb080-00079))_
- It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const) is essential for working with production code. _(javascriptallonge.pdf (source-range-83ecb080-00079))_
- 34 A number of the caveats discussed here were described in Jyrly Zaytsev’s excellent article Named function expressions demystified. _(javascriptallonge.pdf (source-range-83ecb080-00079))_
- This behaviour is intentional on the part of JavaScript’s design to facilitate a certain style of programming where you put the main logic up front, and the “helper functions” at the bottom. _(javascriptallonge.pdf (source-range-83ecb080-00079))_
- Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-83ecb080-00079))_
- Function declarations are formally only supposed to be made at what we might call the “top level” of a function. _(javascriptallonge.pdf (source-range-83ecb080-00079))_
- Another caveat is that a function declaration cannot exist inside of _any_ expression, otherwise it’s a function expression. _(javascriptallonge.pdf (source-range-83ecb080-00080))_
- The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. _(javascriptallonge.pdf (source-range-83ecb080-00080))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-83ecb080-00080))_
- Another caveat is that a function declaration cannot exist inside of _any_ expression, otherwise it’s a function expression. _(javascriptallonge.pdf (source-range-83ecb080-00080))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-83ecb080-00080))_

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00066, source-range-83ecb080-00069))_

> 30 The first sip: Basic Functions ((diameter) => { **const** PI = 3.14159265; **return** diameter * PI })(2) _//=> 6.2831853_ We can bind any expression. Functions are expressions, so we can bind helper functions: (d) => { **const** calc = (diameter) => { **const** PI = 3.14159265; **return** diameter * PI }; **return** "The circumference is " + calc(d) } Notice calc(d)? This underscores what we’ve said: if we have an expression that evaluates to a function, we apply it with (). A name that’s bo

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00067))_

> One of the places you can find blocks is in an if statement.

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00077, source-range-83ecb080-00079))_

> The first sip: Basic Functions 41 someBackboneView.on('click', **function** clickHandler () { _//..._ }); Now, the function’s actual name has no effect on the environment in which it is used. To whit: **const** bindingName = **function** actualName () { _//..._ }; bindingName _//=> [Function: actualName]_ actualName _//=> ReferenceError: actualName is not defined_ So “actualName” isn’t bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00078))_

> The first sip: Basic Functions
> 
> 42 even _//=> Can't find variable: even_ even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don’t _need_ to name it anywhere else, you needn’t.
> 
> ## **function declarations**
> 
> There is another syntax for naming and/or defining a function. It’s called a _function declaration statement_ , and it looks a lot like a named function expression, only we use it as a statement: **function** someName () { _// ..._ } This behaves a _little_ like: **const** someName = **function** someName () { _// ..._ } In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are _hoisted_ to the top of the function in which they occur.
> 
> Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const:
> 
> ( **function** () { **return** fizzbuzz(); **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> undefined is not a function (evaluating 'fizzbuzz()')_ We haven’t actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function _declaration_ works differently:

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00079))_

> 43 The first sip: Basic Functions ( **function** () { **return** fizzbuzz(); **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> 'FizzBuzz'_ Although fizzbuzz is declared later in the function, JavaScript behaves as if we’d written: ( **function** () { **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } **return** fizzbuzz(); })() The definition of the fizzbuzz is “hoisted” to the top of its enclosing scope (an IIFE in this case). This behaviour is inten

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00080))_

> Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

## Combinators and Function Decorators

- Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function. _(javascriptallonge.pdf (source-range-83ecb080-00082))_
- We’d learn that the fundamental combinators are named after birds following the example of Raymond Smullyan’s famous book To Mock a Mockingbird[36] . _(javascriptallonge.pdf (source-range-83ecb080-00082))_
- JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. _(javascriptallonge.pdf (source-range-83ecb080-00082))_
- “A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.”–Wikipedia[35] If we were learning Combinatorial Logic, we’d start with the most basic combinators like S, K, and I, and work up from there to practical combinators. _(javascriptallonge.pdf (source-range-83ecb080-00082))_
- We’d learn that the fundamental combinators are named after birds following the example of Raymond Smullyan’s famous book To Mock a Mockingbird[36] . _(javascriptallonge.pdf (source-range-83ecb080-00082))_
- “A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.”–Wikipedia[35] If we were learning Combinatorial Logic, we’d start with the most basic combinators like S, K, and I, and work up from there to practical combinators. _(javascriptallonge.pdf (source-range-83ecb080-00082))_
- Code that uses a lot of combinators tends to name the verbs and adverbs (like doubleOf, addOne, and compose) while avoiding language keywords and the names of nouns (like number). _(javascriptallonge.pdf (source-range-83ecb080-00083))_
- We won’t be strict about using only previously defined combinators in their construction. _(javascriptallonge.pdf (source-range-83ecb080-00083))_
- Let’s start with a useful combinator: Most programmers call it _Compose_ , although the logicians call it the B combinator or “Bluebird.” Here is the typical[37] programming implementation: _(javascriptallonge.pdf (source-range-83ecb080-00083))_
- A _function decorator_ is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. _(javascriptallonge.pdf (source-range-83ecb080-00083))_
- So one perspective is that combinators are useful when you want to emphasize what you’re doing and how it fits together, and more explicit code is useful when you want to emphasize what you’re working with. _(javascriptallonge.pdf (source-range-83ecb080-00083))_
- This is, of course, just one example of many. _(javascriptallonge.pdf (source-range-83ecb080-00083))_
- While some programmers believe “There Should Only Be One Way To Do It,” having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-83ecb080-00083))_
- Here’s a ridiculously simple decorator:[38] > 37As we’ll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. _(javascriptallonge.pdf (source-range-83ecb080-00083))_
- While some programmers believe “There Should Only Be One Way To Do It,” having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-83ecb080-00083))_
- We won’t be strict about using only previously defined combinators in their construction. _(javascriptallonge.pdf (source-range-83ecb080-00083))_
- Function decorators aren’t strict about being pure functions, so there’s more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-83ecb080-00084))_
- 47 **const** not = (fn) => (x) => !fn(x) So instead of writing !someFunction(42), we can write not(someFunction)(42). _(javascriptallonge.pdf (source-range-83ecb080-00084))_

## Building Blocks

- Although you needn’t restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks. _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- The strength of JavaScript is that you can do anything. _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- Thereafter, it does nothing. _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- There are ifs, fors, returns, everything thrown higgledy piggledy together. _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- You can compose them with explicit JavaScript code as we’ve just done. _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- Once is useful for ensuring that certain side effects are not repeated. _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- Of course, you needn’t use combinators to implement either of these ideas, you can use if statements. _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- The weakness is that you will. _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- We’ll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined) as an argument. _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- But once and maybe compose, so you can chain them together as you see fit: _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways. _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- In the recipes, we’ll look at a decorator called once: It ensures that a function can only be executed once. _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- In the recipes, we’ll look at a decorator called once: It ensures that a function can only be executed once. _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely: _(javascriptallonge.pdf (source-range-83ecb080-00087))_
- We can abstract this one level higher. _(javascriptallonge.pdf (source-range-83ecb080-00087))_
- Code is easier than words for this. _(javascriptallonge.pdf (source-range-83ecb080-00087))_
- The Underscore[39] library provides a higher-order function called _map_ .[40] It applies another function to each element of an array, like this: _(javascriptallonge.pdf (source-range-83ecb080-00087))_
- Another basic building block is _partial application_ . _(javascriptallonge.pdf (source-range-83ecb080-00087))_
- The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. _(javascriptallonge.pdf (source-range-83ecb080-00087))_
- In that case, we can’t get the final value, but we can get a function that represents _part_ of our application. _(javascriptallonge.pdf (source-range-83ecb080-00087))_
- mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-83ecb080-00087))_
- > 40Modern JavaScript implementations provide a map method for arrays, but Underscore’s implementation also works with older browsers if you are working with that headache. _(javascriptallonge.pdf (source-range-83ecb080-00087))_
- Partial application also has a combinator, which we’ll see in the partial recipe. _(javascriptallonge.pdf (source-range-83ecb080-00088))_

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00087))_

> The first sip: Basic Functions 49 ## **partial application** Another basic building block is _partial application_ . When a function takes multiple arguments, we “apply” the function to the arguments by evaluating it with all of the arguments, producing a value. But what if we only supply some of the arguments? In that case, we can’t get the final value, but we can get a function that represents _part_ of our application. Code is easier than words for this. The Underscore[39] library provides a 

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00086))_

> You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators: **const** compose = (a, b) => (c) => a(b(c)); **const** cookAndEat = compose(eat, cook); If that was all there was to it, composition wouldn’t matter much.

## Magic Names

- When a function is applied to arguments (or “called”), JavaScript binds the values of arguments to the function’s argument names in an environment created for the function’s execution. _(javascriptallonge.pdf (source-range-83ecb080-00090))_
- > 42You should never attempt to define your own bindings against “magic” names that JavaScript binds for you. _(javascriptallonge.pdf (source-range-83ecb080-00090))_
- It is wise to treat them as read-only at all times. _(javascriptallonge.pdf (source-range-83ecb080-00090))_
- What we haven’t discussed so far is that JavaScript also binds values to some “magic” names in addition to any you put in the argument list.[42] There are two separate rules for these “magic” names, one for when you invoke a function using the function keyword, and another for functions defined with “fat arrows.” We’ll begin with how things work for functions defined with the function keyword. _(javascriptallonge.pdf (source-range-83ecb080-00090))_
- The first magic name is this, and it is bound to something called the function’s context. _(javascriptallonge.pdf (source-range-83ecb080-00090))_
- It is wise to treat them as read-only at all times. _(javascriptallonge.pdf (source-range-83ecb080-00090))_
- The most common use of the arguments binding is to build functions that can take a variable number of arguments. _(javascriptallonge.pdf (source-range-83ecb080-00091))_
- For example, when this expression’s inner function is defined with function, arguments[0] refers to its only argument, "inner": _(javascriptallonge.pdf (source-range-83ecb080-00091))_
- We’ll see it used in many of the recipes, starting off with partial application and ellipses. _(javascriptallonge.pdf (source-range-83ecb080-00091))_
- For example, when this expression’s inner function is defined with function, arguments[0] refers to its only argument, "inner": _(javascriptallonge.pdf (source-range-83ecb080-00091))_
- Sometimes, a function is meant to be used as a Big-F function. _(javascriptallonge.pdf (source-range-83ecb080-00093))_
- It’s a simple representation of an expression to be computed. _(javascriptallonge.pdf (source-range-83ecb080-00093))_
- Having magic variables apply to Big-F functions but not to small-G functions makes it much easier to use small-F functions as syntax, treating them as expressions or blocks that can be passed to functions like mapWith. _(javascriptallonge.pdf (source-range-83ecb080-00093))_
- Although this example is clearly unrealistic, there is a general design principle that deserves attention. _(javascriptallonge.pdf (source-range-83ecb080-00093))_
- In our example above, row is a Big-F function, but (column) => column * arguments[0] is a small-f function, it exists just to give mapWith something to apply. _(javascriptallonge.pdf (source-range-83ecb080-00093))_
- But sometimes, a function is a small-f function. _(javascriptallonge.pdf (source-range-83ecb080-00093))_
- It has a name, it is called by different pieces of code, it’s a first-class entity in the code. _(javascriptallonge.pdf (source-range-83ecb080-00093))_
- It has a name, it is called by different pieces of code, it’s a first-class entity in the code. _(javascriptallonge.pdf (source-range-83ecb080-00093))_

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00091, source-range-83ecb080-00093))_

> 52 The first sip: Basic Functions **const** plus = **function** () { **return** arguments[0] + arguments[1]; } plus(2,3) _//=> 5_ When discussing objects, we’ll discuss properties in more depth. Here’s something interesting about arguments: **const** howMany = **function** () { **return** arguments['length']; } howMany() _//=> 0_ howMany('hello') _//=> 1_ howMany('sharks', 'are', 'apex', 'predators') _//=> 4_ The most common use of the arguments binding is to build functions that can take a vari

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00092))_

> 53
> 
> The first sip: Basic Functions
> 
> ( **function** () { **return** ( **function** () { **return** arguments[0]; })('inner'); })('outer') _//=> "inner"_ But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function. And thus arguments[0] will refer to "outer", not to "inner":
> 
> ( **function** () { **return** (() => arguments[0])('inner'); })('outer') _//=> "outer"_ Although it seems quixotic for the two syntaxes to have different semantics, it makes sense when you consider the design goal: Fat arrow functions are designed to be very lightweight and are often used with constructs like mapping or callbacks to emulate syntax.
> 
> To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. It uses mapWith, which we discussed in Building Blocks.[44] We’ll use arguments just to show the difference between using a fat arrow and the function keyword: **const** row = **function** () { **return** mapWith( (column) => column * arguments[0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) _//=> [3,6,9,12,15,18,21,24,27,30,33,36]_ This works just fine, because arguments[0] refers to the 3 we passed to the function row. Our “fat arrow” function (column) => column * arguments[0] doesn’t bind arguments when it’s invoked. But if we rewrite row to use the function keyword, it stops working:
> 
> > 44Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It’s the same idea, after all.

## Summary

- - JavaScript uses function declarations to bind functions to names within function scope. _(javascriptallonge.pdf (source-range-83ecb080-00095))_
- - function keyword functions always have blocks as their bodies. _(javascriptallonge.pdf (source-range-83ecb080-00095))_
- - The arguments are passed by sharing, which is also called “pass by value.” - Fat arrow functions have expressions or blocks as their bodies. _(javascriptallonge.pdf (source-range-83ecb080-00095))_
- - Block bodies evaluate to whatever is returned with the return keyword, or to undefined. _(javascriptallonge.pdf (source-range-83ecb080-00095))_
- - Scopes are nested and free variable references closed over. _(javascriptallonge.pdf (source-range-83ecb080-00095))_
- - Functions are _reference values_ . _(javascriptallonge.pdf (source-range-83ecb080-00095))_
- - JavaScript uses const to bind values to names within block scope. _(javascriptallonge.pdf (source-range-83ecb080-00095))_
- - Variables can shadow variables in an enclosing scope. _(javascriptallonge.pdf (source-range-83ecb080-00095))_
- - Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-83ecb080-00095))_
- - Function bodies have zero or more statements. _(javascriptallonge.pdf (source-range-83ecb080-00095))_
- - Functions are values that can be part of expressions, returned from other functions, and so forth. _(javascriptallonge.pdf (source-range-83ecb080-00095))_
- - Functions are applied to arguments. _(javascriptallonge.pdf (source-range-83ecb080-00095))_
- Function declarations are “hoisted.” - Function application creates a scope. _(javascriptallonge.pdf (source-range-83ecb080-00095))_
- - Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-83ecb080-00095))_
- - JavaScript uses const to bind values to names within block scope. _(javascriptallonge.pdf (source-range-83ecb080-00095))_
- - JavaScript uses function declarations to bind functions to names within function scope. _(javascriptallonge.pdf (source-range-83ecb080-00095))_

## Recipes with Basic Functions

- The overall _use_ of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-83ecb080-00097))_
- Having looked at basic pure functions and closures, we’re going to see some practical recipes that focus on the premise of functions that return functions. _(javascriptallonge.pdf (source-range-83ecb080-00097))_
- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven’t been discussed in the text to this point, such as methods and/or prototypes. _(javascriptallonge.pdf (source-range-83ecb080-00097))_
- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven’t been discussed in the text to this point, such as methods and/or prototypes. _(javascriptallonge.pdf (source-range-83ecb080-00097))_
- The overall _use_ of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-83ecb080-00097))_

## Partial Application

- > 48 callFirst and callLast were inspired by Michael Fogus’ Lemonad. _(javascriptallonge.pdf (source-range-83ecb080-00099))_
- These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost.[48] If you want to bind more than one argument, or you want to leave a “hole” in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. _(javascriptallonge.pdf (source-range-83ecb080-00099))_
- We’d need a different recipe if we wish to create partial applications of object methods. _(javascriptallonge.pdf (source-range-83ecb080-00099))_
- In Building Blocks, we discussed partial application, but we didn’t write a generalized recipe for it. _(javascriptallonge.pdf (source-range-83ecb080-00099))_
- This is such a common tool that many libraries provide some form of partial application. _(javascriptallonge.pdf (source-range-83ecb080-00099))_
- We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument: **const** callLeft = (fn, ...args) => _(javascriptallonge.pdf (source-range-83ecb080-00100))_

## Unary

- What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-83ecb080-00102))_
- And when you call parseInt with map, the index is interpreted as a radix. _(javascriptallonge.pdf (source-range-83ecb080-00102))_
- The most common use case is to fix a problem. _(javascriptallonge.pdf (source-range-83ecb080-00102))_
- ['1', '2', '3'].map(parseInt) _//=> [1, NaN, NaN]_ This doesn’t work because parseInt is defined as parseInt(string[, radix]). _(javascriptallonge.pdf (source-range-83ecb080-00102))_
- We could write ['1', '2', '3'].map((s) => parseInt(s)), or we could come up with a decorator to do the job for us: _(javascriptallonge.pdf (source-range-83ecb080-00102))_
- “Unary” is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument. _(javascriptallonge.pdf (source-range-83ecb080-00102))_
- But some functions have optional second or even third arguments. _(javascriptallonge.pdf (source-range-83ecb080-00102))_
- JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. _(javascriptallonge.pdf (source-range-83ecb080-00102))_
- What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-83ecb080-00102))_
- ['1', '2', '3'].map(parseInt) _//=> [1, NaN, NaN]_ This doesn’t work because parseInt is defined as parseInt(string[, radix]). _(javascriptallonge.pdf (source-range-83ecb080-00102))_

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00102))_

> Recipes with Basic Functions 59 ## **Unary** “Unary” is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument. The most common use case is to fix a problem. JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. Here it is in action: ['1', '2', '3'].map(parseFloat) _//=> [1, 2, 3]_ In that example, it looks exactly like the mapping function y

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00103))_

> 60 **const** unary = (fn) => fn.length === 1

## Tap

- One is when you want to do something with a value for sideeffects, but keep the value around. _(javascriptallonge.pdf (source-range-83ecb080-00105))_
- It has some surprising applications. _(javascriptallonge.pdf (source-range-83ecb080-00105))_
- tap can do more than just act as a debugging aid. _(javascriptallonge.pdf (source-range-83ecb080-00106))_

## Maybe

- A common problem in programming is checking for null or undefined (hereafter called “nothing,” while all other values including 0, [] and false will be called “something”). _(javascriptallonge.pdf (source-range-83ecb080-00108))_
- Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-83ecb080-00108))_
- If some code ever tries to call model.setSomething with nothing, the operation will be skipped. _(javascriptallonge.pdf (source-range-83ecb080-00109))_

## Once

- 65 once is an extremely helpful combinator. _(javascriptallonge.pdf (source-range-83ecb080-00111))_
- It ensures that a function can only be called, well, _once_ . _(javascriptallonge.pdf (source-range-83ecb080-00111))_
- It ensures that a function can only be called, well, _once_ . _(javascriptallonge.pdf (source-range-83ecb080-00111))_

## Left-Variadic Functions

- A _variadic function_ is a function that is designed to accept a variable number of arguments.[52] In JavaScript, you can make a variadic function by gathering parameters. _(javascriptallonge.pdf (source-range-83ecb080-00113))_
- For example, we might want to have a function that builds some kind of team record. _(javascriptallonge.pdf (source-range-83ecb080-00113))_
- > 52English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. _(javascriptallonge.pdf (source-range-83ecb080-00113))_
- Easy in ECMAScript 2015: **function** team(coach, captain, ...players) { console.log(` **${** captain **}** (captain)`); **for** ( **let** player **of** players) { console.log(player); } console.log(`squad coached by **${** coach **}** `); } team('Luis Enrique', 'Xavi Hernández', 'Marc-André ter Stegen', 'Martín Montoya', 'Gerard Piqué') _//=>_ Xavi Hernández (captain) Marc-André ter Stegen Martín Montoya Gerard Piqué squad coached by Luis Enrique _(javascriptallonge.pdf (source-range-83ecb080-00113))_
- For example, we might want to have a function that builds some kind of team record. _(javascriptallonge.pdf (source-range-83ecb080-00113))_
- In “Ye Olde Days,”[53] JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice, or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. _(javascriptallonge.pdf (source-range-83ecb080-00114))_
- “Ye” in “Ye Olde,” was not actually spelled with a “Y” in days of old, it was spelled with a thorn, and is pronounced “the.” Another word, “Ye” in “Ye of little programming faith,” is pronounced “ye,” but it’s a different word altogether. _(javascriptallonge.pdf (source-range-83ecb080-00114))_
- This is a _right-variadic function_ , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument. _(javascriptallonge.pdf (source-range-83ecb080-00115))_
- We sure can, by using the techniques from rightVariadic. _(javascriptallonge.pdf (source-range-83ecb080-00115))_
- All left-variadic functions have one or more fixed arguments, and the rest are gathered into the leftmost argument. _(javascriptallonge.pdf (source-range-83ecb080-00115))_
- Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. _(javascriptallonge.pdf (source-range-83ecb080-00116))_
- With leftGather, we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function. _(javascriptallonge.pdf (source-range-83ecb080-00117))_
- Recipes with Basic Functions **const** [butLast, last] = leftVariadic((butLast, last) => [butLast, last])(...['wh\ y', 'hello', 'there', 'little', 'droid']); butLast _//=> ['why', 'hello', 'there', 'little']_ last _//=> 'droid'_ But we can write our own left-gathering function utility using the same principles without all the tedium: **const** leftGather = (outputArrayLength) => { **return function** (inputArray) { **return** [inputArray.slice(0, inputArray.length - outputArrayLength + 1)].conc\ at( inputArray.slice(inputArray.length - outputArrayLength + 1) ) } }; **const** [butLast, last] = leftGather(2)(['why', 'hello', 'there', 'little', 'droid\ ']); butLast _//=> ['why', 'hello', 'there', 'little']_ last _//=> 'droid'_ _(javascriptallonge.pdf (source-range-83ecb080-00117))_
- This is more than just an optimization. _(javascriptallonge.pdf (source-range-83ecb080-00119))_
- If we need to have functions with control-flow semantics, we can pass anonymous functions. _(javascriptallonge.pdf (source-range-83ecb080-00119))_
- The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. _(javascriptallonge.pdf (source-range-83ecb080-00119))_
- - Function invocation uses eager evaluation, so if we need to roll our own control-flow semantics, we pass it functions, not expressions. _(javascriptallonge.pdf (source-range-83ecb080-00120))_
- - Logical operators are based on truthiness and falsiness, not the strict values true and false. _(javascriptallonge.pdf (source-range-83ecb080-00120))_
- - The ternary operator (?:), ||, and && are control flow operators, they do not always return true or false, and they have short-cut semantics. _(javascriptallonge.pdf (source-range-83ecb080-00120))_
- Here we’ve passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation. _(javascriptallonge.pdf (source-range-83ecb080-00120))_

## Composing and Decomposing Data

- Recursion is the root of computation since it trades description for time.—Alan Perlis, Epigrams in Programming[55] > 55http://www.cs.yale.edu/homes/perlis-alan/quotes.html _(javascriptallonge.pdf (source-range-83ecb080-00122))_

## Arrays and Destructuring Arguments

- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-83ecb080-00124))_
- 78 While we have mentioned arrays briefly, we haven’t had a close look at them. _(javascriptallonge.pdf (source-range-83ecb080-00124))_
- Strings are important because they represent writing. _(javascriptallonge.pdf (source-range-83ecb080-00124))_
- We can create an empty array: [] _//=> []_ We can create an array with one or more _elements_ by placing them between the brackets and separating the items with commas. _(javascriptallonge.pdf (source-range-83ecb080-00124))_
- [ 2, 3, 2 + 2 ] _//=> [2,3,4]_ Including an expression denoting another array: [[[[[]]]]] This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. _(javascriptallonge.pdf (source-range-83ecb080-00124))_
- JavaScript has a literal syntax for creating an array: The [ and ] characters. _(javascriptallonge.pdf (source-range-83ecb080-00124))_
- Arrays are JavaScript’s “native” representation of lists. _(javascriptallonge.pdf (source-range-83ecb080-00124))_
- Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-83ecb080-00124))_
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-83ecb080-00124))_
- Strings are important because they represent writing. _(javascriptallonge.pdf (source-range-83ecb080-00124))_
- Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-83ecb080-00124))_
- Array elements can be extracted using [ and ] as postfix operators. _(javascriptallonge.pdf (source-range-83ecb080-00125))_
- We know that every array is its own unique entity, with its own unique reference. _(javascriptallonge.pdf (source-range-83ecb080-00125))_
- The statement const [something] = wrapped; _destructures_ the array represented by wrapped, binding the value of its single element to the name something. _(javascriptallonge.pdf (source-range-83ecb080-00126))_
- There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-83ecb080-00126))_
- There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-83ecb080-00126))_
- notation does not provide a universal patten-matching capability. _(javascriptallonge.pdf (source-range-83ecb080-00127))_
- Sometimes we need to extract arrays from arrays. _(javascriptallonge.pdf (source-range-83ecb080-00127))_
- We could do the same thing with (name) => name[1], but destructuring is code that resembles the data it consumes, a valuable coding style. _(javascriptallonge.pdf (source-range-83ecb080-00127))_
- Now, when we introduced destructuring, we saw that it is kind-of-sort-of the reverse of array literals. _(javascriptallonge.pdf (source-range-83ecb080-00128))_
- If it does, assignments are made where appropriate. _(javascriptallonge.pdf (source-range-83ecb080-00128))_
- JavaScript tries its best to assign things, and if there isn’t something that fits, JavaScript binds undefined to the name. _(javascriptallonge.pdf (source-range-83ecb080-00129))_
- As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. _(javascriptallonge.pdf (source-range-83ecb080-00129))_
- 83 **const** [what] = []; That match would fail because the array doesn’t have an element to assign to what. _(javascriptallonge.pdf (source-range-83ecb080-00129))_
- But this is not how JavaScript works. _(javascriptallonge.pdf (source-range-83ecb080-00129))_
- This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-83ecb080-00129))_
- 83 **const** [what] = []; That match would fail because the array doesn’t have an element to assign to what. _(javascriptallonge.pdf (source-range-83ecb080-00129))_
- This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-83ecb080-00129))_
- There is only one difference: We have not tried gathering. _(javascriptallonge.pdf (source-range-83ecb080-00130))_
- There is only one difference: We have not tried gathering. _(javascriptallonge.pdf (source-range-83ecb080-00130))_
- This is very useful indeed, and we’ll see more of it in a moment.[59] 59Gathering in parameters has a long history, and the usual terms are to call gathering “pattern matching” and to call a name that is bound to gathered values a “rest parameter.” The term “rest” is perfectly compatible with gather: “Rest” is the noun, and “gather” is the verb. _(javascriptallonge.pdf (source-range-83ecb080-00131))_
- > 61 Well, actually, this does not work for arrays that contain undefined as a value, but we are not going to see that in our examples. _(javascriptallonge.pdf (source-range-83ecb080-00133))_
- We need something for when the array isn’t empty. _(javascriptallonge.pdf (source-range-83ecb080-00134))_
- If an array is not empty, and we break it into two pieces, first and rest, the length of our array is going to be length(first) + length(rest). _(javascriptallonge.pdf (source-range-83ecb080-00134))_
- Well, the length of first is 1, there’s just one element at the front. _(javascriptallonge.pdf (source-range-83ecb080-00134))_
- Our length function is _recursive_ , it calls itself. _(javascriptallonge.pdf (source-range-83ecb080-00134))_
- If only there was a function we could call… Like length! _(javascriptallonge.pdf (source-range-83ecb080-00134))_
- This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-83ecb080-00134))_
- This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-83ecb080-00134))_
- If only there was a function we could call… Like length! _(javascriptallonge.pdf (source-range-83ecb080-00134))_
- Another common problem is applying a function to every element of an array. _(javascriptallonge.pdf (source-range-83ecb080-00136))_
- JavaScript has a built-in function for this, but let’s write our own using linear recursion. _(javascriptallonge.pdf (source-range-83ecb080-00136))_
- We can write it out using a ternary operator. _(javascriptallonge.pdf (source-range-83ecb080-00137))_
- Functions can take functions as arguments, so let’s “extract” the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together. _(javascriptallonge.pdf (source-range-83ecb080-00137))_
- A function to compute the sum of the squares of a list of numbers might look like this: _(javascriptallonge.pdf (source-range-83ecb080-00137))_
- Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution. _(javascriptallonge.pdf (source-range-83ecb080-00137))_
- Linear recursion is a basic building block of algorithms. _(javascriptallonge.pdf (source-range-83ecb080-00139))_
- Its specialized cases of mapping and folding are especially useful and can be used to build other functions. _(javascriptallonge.pdf (source-range-83ecb080-00139))_
- And finally, while folding is a special case of linear recursion, mapping is a special case of folding. _(javascriptallonge.pdf (source-range-83ecb080-00139))_
- Its basic form parallels the way linear data structures like lists are constructed: This helps make it understandable. _(javascriptallonge.pdf (source-range-83ecb080-00139))_

## Tail Calls (and Default Arguments)

- To do that, it has to evaluate fn(first) and mapWith(fn, rest), then evaluate [fn(first), ...mapWith(fn, rest)]. _(javascriptallonge.pdf (source-range-83ecb080-00141))_
- Next, JavaScript invokes mapWith(fn, rest), which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]). _(javascriptallonge.pdf (source-range-83ecb080-00141))_
- One of the reasons they are not production-ready is that they consume memory proportional to the size of the array being folded. _(javascriptallonge.pdf (source-range-83ecb080-00141))_
- The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustrating the basic principles behind using recursion to work with self-similar data structures, but they are not “production-ready” implementations. _(javascriptallonge.pdf (source-range-83ecb080-00141))_
- So we know that JavaScript is going to hang on to 1. _(javascriptallonge.pdf (source-range-83ecb080-00141))_
- First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. _(javascriptallonge.pdf (source-range-83ecb080-00141))_
- JavaScript cannot throw first away. _(javascriptallonge.pdf (source-range-83ecb080-00141))_
- first is not undefined, so it evaluates [fn(first), …mapWith(fn, rest)]. _(javascriptallonge.pdf (source-range-83ecb080-00141))_
- To do that, it has to evaluate fn(first) and mapWith(fn, rest), then evaluate [fn(first), ...mapWith(fn, rest)]. _(javascriptallonge.pdf (source-range-83ecb080-00141))_
- Making algorithms faster is a very highly studied field of computer science. _(javascriptallonge.pdf (source-range-83ecb080-00142))_
- That information is saved on a _call stack_ , and it is quite expensive. _(javascriptallonge.pdf (source-range-83ecb080-00142))_
- In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error. _(javascriptallonge.pdf (source-range-83ecb080-00142))_
- In fact, there are several better ways. _(javascriptallonge.pdf (source-range-83ecb080-00142))_
- 95 depending on the implementation), plus some housekeeping information so it remembers what to do with that value, while it calls the equivalent of mapWith((x) => x * x, [3, 4, 5]). _(javascriptallonge.pdf (source-range-83ecb080-00142))_
- It can start assembling the resulting array and start discarding the information it is saving. _(javascriptallonge.pdf (source-range-83ecb080-00142))_
- Furthermore, doubling the length of an array will double the amount of space we need on the stack, plus double all the work required to set up and tear down the housekeeping data for each call (these are called _call frames_ , and they include the place where the function was called, an environment, and so on). _(javascriptallonge.pdf (source-range-83ecb080-00142))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest). _(javascriptallonge.pdf (source-range-83ecb080-00143))_
- That is excellent, but one wrapping is not a big deal. _(javascriptallonge.pdf (source-range-83ecb080-00143))_
- This is a tail-call, because it invokes another function and returns its result. _(javascriptallonge.pdf (source-range-83ecb080-00143))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length, the other happens after the recursive call. _(javascriptallonge.pdf (source-range-83ecb080-00143))_
- This is a very important characteristic of JavaScript: **If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space.** _(javascriptallonge.pdf (source-range-83ecb080-00143))_
- But the third is fn.apply(this, args). _(javascriptallonge.pdf (source-range-83ecb080-00143))_
- This is interesting, because after sorting out what to supply as arguments (this, args), JavaScript can throw away everything in its current stack frame. _(javascriptallonge.pdf (source-range-83ecb080-00143))_
- And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe-wrapped call. _(javascriptallonge.pdf (source-range-83ecb080-00143))_
- It isn’t going to do any more work, so it can throw its existing stack frame away. _(javascriptallonge.pdf (source-range-83ecb080-00143))_
- This is interesting, because after sorting out what to supply as arguments (this, args), JavaScript can throw away everything in its current stack frame. _(javascriptallonge.pdf (source-range-83ecb080-00143))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length, the other happens after the recursive call. _(javascriptallonge.pdf (source-range-83ecb080-00143))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest). _(javascriptallonge.pdf (source-range-83ecb080-00143))_
- This is a tail-call, because it invokes another function and returns its result. _(javascriptallonge.pdf (source-range-83ecb080-00143))_
- Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. _(javascriptallonge.pdf (source-range-83ecb080-00144))_
- The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. _(javascriptallonge.pdf (source-range-83ecb080-00144))_
- This version of length calls uses lengthDelaysWork, and JavaScript optimizes that not to take up memory proportional to the length of the string. _(javascriptallonge.pdf (source-range-83ecb080-00144))_
- The obvious solution is push the 1 + work into the call to length. _(javascriptallonge.pdf (source-range-83ecb080-00144))_
- The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. _(javascriptallonge.pdf (source-range-83ecb080-00144))_
- We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. _(javascriptallonge.pdf (source-range-83ecb080-00145))_
- And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization. _(javascriptallonge.pdf (source-range-83ecb080-00145))_
- Introductions to recursion often mention calculating factorials: In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. _(javascriptallonge.pdf (source-range-83ecb080-00145))_
- Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n - 1). _(javascriptallonge.pdf (source-range-83ecb080-00147))_
- But when it calls itself, it will call factorial(5, 6) and that will not mean factorial(5, 1). _(javascriptallonge.pdf (source-range-83ecb080-00148))_
- JavaScript provides this exact syntax, it’s called a _default argument_ , and it looks like this: _(javascriptallonge.pdf (source-range-83ecb080-00148))_
- What we really want is this: We want to write something like factorial(6), and have JavaScript automatically know that we really mean factorial(6, 1). _(javascriptallonge.pdf (source-range-83ecb080-00148))_
- A default argument is concise and readable. _(javascriptallonge.pdf (source-range-83ecb080-00149))_
- Now we learn that we can create a default parameter argument. _(javascriptallonge.pdf (source-range-83ecb080-00149))_
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-83ecb080-00150))_

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00145, source-range-83ecb080-00147))_

> Composing and Decomposing Data 98 **const** mapWithDelaysWork = (fn, [first, ...rest], prepend) => first === **undefined** - ? prepend - : mapWithDelaysWork(fn, rest, [...prepend, fn(first)]); **const** mapWith = callLast(mapWithDelaysWork, []); mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_ We can use it with ridiculously large arrays: mapWith((x) => x * x, [ |0,|1,|2,|3,|4,|5,|6,|7,|8,|9,| |---|---|---|---|---|---|---|---|---|---| |10,|11,|12,|13,|14,|15,|16,|17,|18,|19,| |20,|21,

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00146))_

| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |

<details>
<summary>Raw table text</summary>

```
| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |
```

</details>

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00149))_

> Composing and Decomposing Data 101 **const** factorial = (n, work = 1) => n === 1 ? work : factorial(n - 1, n * work); factorial(1) _//=> 1_ factorial(6) _//=> 720_ By writing our parameter list as (n, work = 1) =>, we’re stating that if a second parameter is not provided, work is to be bound to 1. We can do similar things with our other tail-recursive functions: **const** length = ([first, ...rest], numberToBeAdded = 0) => first === **undefined** ? numberToBeAdded : length(rest, 1 + numberToBeA

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00150))_

> 102 **const** [first, second = "two"] = ["one"];

## Garbage, Garbage Everywhere

- The right tool to discover why it’s still slow is a memory profiler, but a simple inspection of the program will reveal the following: _(javascriptallonge.pdf (source-range-83ecb080-00152))_
- To do that, we take the array in prepend and push fn(first) onto the end, creating a new array that will be passed to the next invocation of mapWith. _(javascriptallonge.pdf (source-range-83ecb080-00152))_
- But this is not how JavaScript’s built-in arrays work. _(javascriptallonge.pdf (source-range-83ecb080-00153))_
- **Key Point** : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. _(javascriptallonge.pdf (source-range-83ecb080-00153))_
- Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another. _(javascriptallonge.pdf (source-range-83ecb080-00153))_
- In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. _(javascriptallonge.pdf (source-range-83ecb080-00153))_
- That is very laborious.[64] The array we had in prepend is no longer used. _(javascriptallonge.pdf (source-range-83ecb080-00153))_
- > 64It needn’t always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. _(javascriptallonge.pdf (source-range-83ecb080-00153))_
- We may not be creating 3,000 stack frames, but we are creating three thousand new arrays and copying elements into each and every one of them. _(javascriptallonge.pdf (source-range-83ecb080-00153))_
- Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend. _(javascriptallonge.pdf (source-range-83ecb080-00153))_
- > 64It needn’t always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. _(javascriptallonge.pdf (source-range-83ecb080-00153))_
- **Key Point** : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. _(javascriptallonge.pdf (source-range-83ecb080-00153))_
- Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend. _(javascriptallonge.pdf (source-range-83ecb080-00153))_
- > 66Lisp is still very much alive, and one of the most interesting and exciting programming languages in use today is Clojure, a Lisp dialect that runs on the JVM, along with its sibling ClojureScript, Clojure that transpiles to JavaScript. _(javascriptallonge.pdf (source-range-83ecb080-00154))_
- The CPU’s instruction set featured two important macros: CAR would fetch 15 bits representing the Contents of the Address part of the Register, while CDR would fetch the Contents of the Decrement part of the Register. _(javascriptallonge.pdf (source-range-83ecb080-00154))_
- The 704 had a 36-bit word, meaning that it was very fast to store and retrieve 36-bit values. _(javascriptallonge.pdf (source-range-83ecb080-00154))_
- (The very first FORTRAN implementation was also written for the 704). _(javascriptallonge.pdf (source-range-83ecb080-00154))_
- Lisp’s basic data type is often said to be the list, but in actuality it was the “cons cell,” the term used to describe two 15-bit values stored in one word. _(javascriptallonge.pdf (source-range-83ecb080-00155))_
- The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells. _(javascriptallonge.pdf (source-range-83ecb080-00155))_
- We can make a list by calling cons repeatedly, and terminating it with null: **const** oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, **null** ))))); _(javascriptallonge.pdf (source-range-83ecb080-00155))_
- In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. _(javascriptallonge.pdf (source-range-83ecb080-00155))_
- Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-83ecb080-00155))_
- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. _(javascriptallonge.pdf (source-range-83ecb080-00155))_
- If you had two 15-bit values and wished to write them to the register, the CONS macro would take the values and write them to a 36-bit word. _(javascriptallonge.pdf (source-range-83ecb080-00155))_
- Lists were represented as linked lists of cons cells, with each cell’s head pointing to an element and the tail pointing to another cons cell. _(javascriptallonge.pdf (source-range-83ecb080-00155))_
- Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being the others), and computers in the late 1950s were extremely small and slow by today’s standards. _(javascriptallonge.pdf (source-range-83ecb080-00155))_
- Although the 704 used core memory, it still used vacuum tubes for its logic. _(javascriptallonge.pdf (source-range-83ecb080-00155))_
- Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-83ecb080-00155))_
- In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. _(javascriptallonge.pdf (source-range-83ecb080-00155))_
- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. _(javascriptallonge.pdf (source-range-83ecb080-00155))_
- cdr does the trick: cdr(oneToFive) _//=> [2,[3,[4,[5,null]]]]_ Again, it’s just extracting a reference from a cons cell, it’s very fast. _(javascriptallonge.pdf (source-range-83ecb080-00156))_
- But it works the same way: If we want the head of a list, we call car on it: car(oneToFive) _//=> 1_ car is very fast, it simply extracts the first element of the cons cell. _(javascriptallonge.pdf (source-range-83ecb080-00156))_
- Getting one reference to a structure that already exists is faster than copying a bunch of elements. _(javascriptallonge.pdf (source-range-83ecb080-00156))_
- In JavaScript, it’s still much, much, much faster to get all the elements except the head from a linked list than from an array. _(javascriptallonge.pdf (source-range-83ecb080-00156))_
- So now we understand that in Lisp, a lot of things use linked lists, and they do that in part because it was what the hardware made possible. _(javascriptallonge.pdf (source-range-83ecb080-00156))_
- We’ll look at linked lists again when we look at Plain Old JavaScript Objects. _(javascriptallonge.pdf (source-range-83ecb080-00156))_
- This is a Linked List[68] , it’s just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference. _(javascriptallonge.pdf (source-range-83ecb080-00156))_
- That being said, it is easy to understand and helps us grasp how literals and destructuring works, and how recursive algorithms ought to mirror the self-similarity of the data structures they manipulate. _(javascriptallonge.pdf (source-range-83ecb080-00156))_
- And so it is today that languages like JavaScript have arrays that are slow to split into the equivalent of a car/cdr pair, but instructional examples of recursive programs still have echoes of their Lisp origins. _(javascriptallonge.pdf (source-range-83ecb080-00156))_
- There’s no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. _(javascriptallonge.pdf (source-range-83ecb080-00156))_
- So now we understand that in Lisp, a lot of things use linked lists, and they do that in part because it was what the hardware made possible. _(javascriptallonge.pdf (source-range-83ecb080-00156))_
- This is a Linked List[68] , it’s just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference. _(javascriptallonge.pdf (source-range-83ecb080-00156))_
- In JavaScript, it’s still much, much, much faster to get all the elements except the head from a linked list than from an array. _(javascriptallonge.pdf (source-range-83ecb080-00156))_
- Although we showed how to use tail calls to map and fold over arrays with [first, ...rest], in reality this is not how it ought to be done. _(javascriptallonge.pdf (source-range-83ecb080-00157))_
- But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. _(javascriptallonge.pdf (source-range-83ecb080-00157))_
- If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list. _(javascriptallonge.pdf (source-range-83ecb080-00157))_
- For these and other reasons, almost all languages today make it possible to use a fast array or vector type that is optimized for iteration, and even Lisp now has a variety of data structures that are optimized for specific use cases. _(javascriptallonge.pdf (source-range-83ecb080-00157))_
- But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-83ecb080-00157))_
- We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements. _(javascriptallonge.pdf (source-range-83ecb080-00157))_
- Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. _(javascriptallonge.pdf (source-range-83ecb080-00157))_
- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We’ll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-83ecb080-00157))_
- But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-83ecb080-00157))_

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00156))_

> Composing and Decomposing Data 107 **const** node5 = [5, **null** ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; **const** oneToFive = node1; This is a Linked List[68] , it’s just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference. But it works the same way: If we want the head of a list, we call car on it: car(oneToFive) _//=> 1_ car is very fast, it simply extracts the first

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00157))_

> And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

## Plain Old JavaScript Objects

- Lists are not the only way to represent collections of things, but they are the “oldest” data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. _(javascriptallonge.pdf (source-range-83ecb080-00159))_
- In JavaScript, an object is a map from string keys to values. _(javascriptallonge.pdf (source-range-83ecb080-00159))_
- Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. _(javascriptallonge.pdf (source-range-83ecb080-00159))_
- Now they could write user[NAME][LAST] or user[OCCUPATION][TITLE] instead of user[0][1] or user[1][0]. _(javascriptallonge.pdf (source-range-83ecb080-00159))_
- Over time, this need to build heterogeneous data structures with access to members by name evolved into the Dictionary[69] data type, a mapping from a unique set of objects to another set of objects. _(javascriptallonge.pdf (source-range-83ecb080-00159))_
- JavaScript has dictionaries, and it calls them “objects.” The word “object” is loaded in programming circles, due to the widespread use of the term “object-oriented programming” that was coined by Alan Kay but has since come to mean many, many things to many different people. _(javascriptallonge.pdf (source-range-83ecb080-00159))_
- Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0, we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else. _(javascriptallonge.pdf (source-range-83ecb080-00159))_
- Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0, we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else. _(javascriptallonge.pdf (source-range-83ecb080-00159))_
- Lists are not the only way to represent collections of things, but they are the “oldest” data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. _(javascriptallonge.pdf (source-range-83ecb080-00159))_
- JavaScript has a literal syntax for creating objects. _(javascriptallonge.pdf (source-range-83ecb080-00160))_
- If the name is an alphanumeric string conforming to the same rules as names of variables, there’s a simplified syntax for accessing the values: _(javascriptallonge.pdf (source-range-83ecb080-00160))_
- Names needn’t be alphanumeric strings. _(javascriptallonge.pdf (source-range-83ecb080-00160))_
- Expressions can be used for keys as well. _(javascriptallonge.pdf (source-range-83ecb080-00161))_
- 113 compact method syntax, but they are not relevant here. _(javascriptallonge.pdf (source-range-83ecb080-00163))_
- When the label is a valid variable name, it’s often the most obvious variable name as well. _(javascriptallonge.pdf (source-range-83ecb080-00164))_
- So JavaScript supports a further syntactic optimization: **const** description = ({name: { first }, occupation: { title } }) => ` **${** first **}** is a **${** title **}** `; description(user) _//=> "Reginald is a Author"_ And that same syntax works for literals: **const** abbrev = ({name: { first, last }, occupation: { title } }) => { **return** { first, last, title}; } abbrev(user) _//=> {"first":"Reginald","last":"Braithwaite","title":"Author"}_ Earlier, we used two-element arrays as nodes in a linked list: **const** cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d; _(javascriptallonge.pdf (source-range-83ecb080-00164))_
- But now that we’ve looked at objects, we can use an object instead of a two-element array. _(javascriptallonge.pdf (source-range-83ecb080-00164))_
- While we’re at it, let’s use contemporary names. _(javascriptallonge.pdf (source-range-83ecb080-00164))_
- In essence, this simple implementation used functions to create an abstraction with named elements. _(javascriptallonge.pdf (source-range-83ecb080-00164))_
- It is very common to write things like title: title when destructuring objects. _(javascriptallonge.pdf (source-range-83ecb080-00164))_
- We could follow the strategy of delaying the work. _(javascriptallonge.pdf (source-range-83ecb080-00165))_
- As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. _(javascriptallonge.pdf (source-range-83ecb080-00165))_
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-83ecb080-00165))_
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-83ecb080-00165))_
- We have unwittingly _reversed_ the list. _(javascriptallonge.pdf (source-range-83ecb080-00166))_
- This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we’re going to get a backwards copy of the list. _(javascriptallonge.pdf (source-range-83ecb080-00166))_
- For a list of length _n_ , we created _n_ superfluous nodes and copied _n_ superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-00167))_
- Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. _(javascriptallonge.pdf (source-range-83ecb080-00167))_
- Whereas our naïve array algorithm created 2 _n_ superfluous arrays and copied _n_[2] superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-00167))_
- Mind you, this is still much, much faster than making partial copies of arrays. _(javascriptallonge.pdf (source-range-83ecb080-00167))_
- Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. _(javascriptallonge.pdf (source-range-83ecb080-00167))_
- Whereas our naïve array algorithm created 2 _n_ superfluous arrays and copied _n_[2] superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-00167))_

## Mutation

- In JavaScript, almost every type of value can _mutate_ . _(javascriptallonge.pdf (source-range-83ecb080-00169))_
- Specifically, arrays and objects can mutate. _(javascriptallonge.pdf (source-range-83ecb080-00169))_
- Recall that you can access a value from within an array or an object using []. _(javascriptallonge.pdf (source-range-83ecb080-00169))_
- Recall that you can access a value from within an array or an object using []. _(javascriptallonge.pdf (source-range-83ecb080-00169))_
- But after returning the new list, we then become conservative about mutation. _(javascriptallonge.pdf (source-range-83ecb080-00171))_
- We haven’t rebound the inner name to a different variable, we’ve mutated the value that both bindings share. _(javascriptallonge.pdf (source-range-83ecb080-00171))_
- Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. _(javascriptallonge.pdf (source-range-83ecb080-00171))_
- Now that we’ve finished with mutation and aliases, let’s have a look at it. _(javascriptallonge.pdf (source-range-83ecb080-00171))_
- Let’s recall linked lists from Plain Old JavaScript Objects. _(javascriptallonge.pdf (source-range-83ecb080-00171))_
- This also makes sense: Linked lists often use structure sharing. _(javascriptallonge.pdf (source-range-83ecb080-00171))_
- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. _(javascriptallonge.pdf (source-range-83ecb080-00171))_
- While we’re executing the mapWith function, we’re constructing a new linked list. _(javascriptallonge.pdf (source-range-83ecb080-00171))_
- In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about. _(javascriptallonge.pdf (source-range-83ecb080-00171))_
- It is possible to compute anything without ever mutating an existing entity. _(javascriptallonge.pdf (source-range-83ecb080-00171))_
- Mutating existing objects has special implications when two bindings are aliases of the same value. _(javascriptallonge.pdf (source-range-83ecb080-00171))_
- Mutation is a surprisingly complex subject. _(javascriptallonge.pdf (source-range-83ecb080-00171))_
- But after returning the new list, we then become conservative about mutation. _(javascriptallonge.pdf (source-range-83ecb080-00171))_
- Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. _(javascriptallonge.pdf (source-range-83ecb080-00171))_
- Structure sharing like this is what makes linked lists so fast for taking everything but the first item of a list: We aren’t making a new list, we’re using some of the old list. _(javascriptallonge.pdf (source-range-83ecb080-00172))_
- When we wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of we were getting a reference to the same chain of nodes. _(javascriptallonge.pdf (source-range-83ecb080-00172))_
- We just use the data, and the less we mutate it, the fewer the times we have to think about whether making changes will be “safe.” As noted, one pattern is to be more liberal about mutation when building a data structure. _(javascriptallonge.pdf (source-range-83ecb080-00173))_
- If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation: _(javascriptallonge.pdf (source-range-83ecb080-00173))_
- Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. _(javascriptallonge.pdf (source-range-83ecb080-00174))_
- But when we’re in the midst of creating a brand new list, we aren’t sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time. _(javascriptallonge.pdf (source-range-83ecb080-00174))_
- Composing and Decomposing Data **const** copy = (node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail === **null** ) { **const** { first, rest } = node; **const** newNode = { first, rest }; **return** copy(rest, newNode, newNode); } **else** { **const** { first, rest } = node; **const** newNode = { first, rest }; tail.rest = newNode; **return** copy(node.rest, head, newNode); } } This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. _(javascriptallonge.pdf (source-range-83ecb080-00174))_

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00169, source-range-83ecb080-00171))_

> Composing and Decomposing Data 118 ## **Mutation** **==> picture [240 x 321] intentionally omitted <==** **Cupping Grinds** In JavaScript, almost every type of value can _mutate_ . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using []. You can reassign a value using [] =: **const** oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree _//=> [ 'one', 2, 3 ]_ You can

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00170))_

> 119
> 
> Composing and Decomposing Data **const** oneTwoThree = [1, 2, 3]; oneTwoThree[3] = 'four'; oneTwoThree _//=> [ 1, 2, 3, 'four' ]_ You can do the same thing with both syntaxes for accessing objects: **const** name = {firstName: 'Leonard', lastName: 'Braithwaite'}; name.middleName = 'Austin' name _//=> { firstName: 'Leonard',_ # lastName: 'Braithwaite', # middleName: 'Austin' } We have established that JavaScript’s semantics allow for two different bindings to refer to the same value. For example: **const** allHallowsEve = [2012, 10, 31] **const** halloween = allHallowsEve;
> 
> Both halloween and allHallowsEve are bound to the same array value within the local environment. And also: **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { _// ..._ - })(allHallowsEve);
> 
> There are two nested environments, and each one binds a name to the exact same array value. In each of these examples, we have created two _aliases_ for the same value. Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value.
> 
> This is vital. Consider what we already know about shadowing:

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00172))_

> Composing and Decomposing Data 121 **const** EMPTY = {}; **const** OneToFive = { first: 1, rest: { first: 2, rest: { first: 3, rest: { first: 4, rest: { first: 5, rest: EMPTY } } } } }; OneToFive _//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\_ r","rest":{"first":"five","rest":{}}}}}} const ThreeToFive = OneToFive.rest.rest; ThreeToFive //=> {"first":3,"rest":{"first":4,"rest":{"first":5,"rest":{}}}} ThreeToFive.first = "three"; ThreeToFive.rest.first = "four"; T

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00173))_

> We don’t have to remember to use copying operations when we pass it as a value to a function, or extract some data from it.

## Reassignment

- Like some imperative programming languages, JavaScript allows you to re-assign the value bound : to parameters. _(javascriptallonge.pdf (source-range-83ecb080-00177))_
- What we want is a statement that works like const, but permits us to rebind variables. _(javascriptallonge.pdf (source-range-83ecb080-00178))_
- The key is to understand that we are rebinding a different value to the same name in the same environment. _(javascriptallonge.pdf (source-range-83ecb080-00178))_
- We can _shadow_ it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-83ecb080-00178))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const. _(javascriptallonge.pdf (source-range-83ecb080-00178))_
- JavaScript does not permit us to rebind a name that has been bound with const. _(javascriptallonge.pdf (source-range-83ecb080-00178))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const. _(javascriptallonge.pdf (source-range-83ecb080-00178))_
- The suggestion is that shadowing a variable is confusing code. _(javascriptallonge.pdf (source-range-83ecb080-00179))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. _(javascriptallonge.pdf (source-range-83ecb080-00179))_
- Shadowing a let with a const does not change our ability to rebind the variable in its original scope. _(javascriptallonge.pdf (source-range-83ecb080-00179))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. _(javascriptallonge.pdf (source-range-83ecb080-00179))_
- Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. _(javascriptallonge.pdf (source-range-83ecb080-00181))_
- But, again, it is unwise to expect consistency. _(javascriptallonge.pdf (source-range-83ecb080-00181))_
- A function declaration can appear anywhere within a function, but the declaration _and_ the definition are hoisted. _(javascriptallonge.pdf (source-range-83ecb080-00181))_
- A function declaration can appear anywhere within a function, but the declaration _and_ the definition are hoisted. _(javascriptallonge.pdf (source-range-83ecb080-00181))_
- However, its functional scope was a problem. _(javascriptallonge.pdf (source-range-83ecb080-00183))_
- Hopefully, you can think of a faster way to calculate this sum.[72] And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. _(javascriptallonge.pdf (source-range-83ecb080-00183))_
- We haven’t looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. _(javascriptallonge.pdf (source-range-83ecb080-00183))_
- The other kids were adding the numbers like this: 1 + 2 + 3 + . _(javascriptallonge.pdf (source-range-83ecb080-00183))_
- > 72There is a well known story about Karl Friedrich Gauss when he was in elementary school. _(javascriptallonge.pdf (source-range-83ecb080-00183))_
- But it’s not like const and let in that it’s function scoped, not block scoped. _(javascriptallonge.pdf (source-range-83ecb080-00183))_
- For nearly twenty years, variables were declared with var (not counting parameters and function declarations, of course). _(javascriptallonge.pdf (source-range-83ecb080-00183))_
- There are 50 pairs of numbers, so the answer is 50*101 = 5050. _(javascriptallonge.pdf (source-range-83ecb080-00183))_
- His teacher got mad at the class and told them to add the numbers 1 to 100 and give him the answer by the end of the class. _(javascriptallonge.pdf (source-range-83ecb080-00183))_
- But Gauss rearranged the numbers to add them like this: (1 + 100) + (2 + 99) + (3 + 98) + . _(javascriptallonge.pdf (source-range-83ecb080-00183))_
- If you notice every pair of numbers adds up to 101. _(javascriptallonge.pdf (source-range-83ecb080-00183))_
- Let’s try one of our functions: introductions[1]('Raganwald') _//=> 'Hello, Raganwald, my name is undefined'_ _(javascriptallonge.pdf (source-range-83ecb080-00184))_
- The answer is that pesky var i. _(javascriptallonge.pdf (source-range-83ecb080-00184))_
- But at the time we _call_ one of the functions, i has the value 3, which is why the loop terminated. _(javascriptallonge.pdf (source-range-83ecb080-00185))_
- Now, at the time we created each function, i had a sensible value, like 0, 1, or 2. _(javascriptallonge.pdf (source-range-83ecb080-00185))_
- So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3. _(javascriptallonge.pdf (source-range-83ecb080-00185))_
- So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3. _(javascriptallonge.pdf (source-range-83ecb080-00185))_
- That does not mean that you should follow the exact same practice in your own code: The purpose of this book is to illustrate certain principles of programming. _(javascriptallonge.pdf (source-range-83ecb080-00186))_
- The purpose of your own code is to get things done. _(javascriptallonge.pdf (source-range-83ecb080-00186))_
- The two goals are often, but not always, aligned. _(javascriptallonge.pdf (source-range-83ecb080-00186))_
- This works, but let is so much simpler and cleaner that it was added to the language in the ECMAScript 2015 specification. _(javascriptallonge.pdf (source-range-83ecb080-00186))_

## Copy on Write

- And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-83ecb080-00188))_
- We’ve seen how to build lists with arrays and with linked lists. _(javascriptallonge.pdf (source-range-83ecb080-00188))_
- - When you take the rest of an array with destructuring ([first, ...rest]), you are given a _copy_ of the elements of the array. _(javascriptallonge.pdf (source-range-83ecb080-00188))_
- The consequence of this is that if you have an array, and you take it’s “rest,” your “child” array is a copy of the elements of the parent array. _(javascriptallonge.pdf (source-range-83ecb080-00188))_
- - When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list. _(javascriptallonge.pdf (source-range-83ecb080-00188))_
- And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-83ecb080-00188))_
- Let’s confirm our understanding: **const** parentArray = [1, 2, 3]; **const** [aFirst, ...childArray] = parentArray; parentArray[2] = "three"; childArray[0] = "two"; parentArray _//=> [1,2,"three"]_ childArray _//=> ["two",3]_ **const** EMPTY = { first: {}, rest: {} }; **const** parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; **const** childList = parentList.rest; parentList.rest.rest.first = "three"; childList.first = "two"; parentList _//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\_ {},"rest":{}}}}} childList _//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}_ This is remarkably unsafe. _(javascriptallonge.pdf (source-range-83ecb080-00189))_
- We’ll end up reinventing reference counting and garbage collection. _(javascriptallonge.pdf (source-range-83ecb080-00189))_
- before we go any further, let’s write a few naïve list utilities so that we can work at a slightly higher level of abstraction: _(javascriptallonge.pdf (source-range-83ecb080-00189))_
- If we _know_ that a list doesn’t share any elements with another list, we can safely modify it. _(javascriptallonge.pdf (source-range-83ecb080-00189))_
- before we go any further, let’s write a few naïve list utilities so that we can work at a slightly higher level of abstraction: _(javascriptallonge.pdf (source-range-83ecb080-00189))_
- Our mapWith function would be very expensive if we make a copy every time we call rest(node). _(javascriptallonge.pdf (source-range-83ecb080-00191))_
- One strategy for avoiding problems is to be _pessimistic_ . _(javascriptallonge.pdf (source-range-83ecb080-00191))_
- The main difference is that array[index] = value evaluates to value, while set(index, value, list) evaluates to the modified list. _(javascriptallonge.pdf (source-range-83ecb080-00191))_
- But before we fix that, let’s try being lazy about copying. _(javascriptallonge.pdf (source-range-83ecb080-00191))_
- Sometimes we don’t need to make a copy because we won’t be modifying the list. _(javascriptallonge.pdf (source-range-83ecb080-00191))_
- Thereafter, we can write to the parent or the copy of the child freely. _(javascriptallonge.pdf (source-range-83ecb080-00191))_
- As we expected, making a copy lets us modify the copy without interfering with the original. _(javascriptallonge.pdf (source-range-83ecb080-00191))_
- Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-83ecb080-00191))_
- But before we fix that, let’s try being lazy about copying. _(javascriptallonge.pdf (source-range-83ecb080-00191))_
- Sometimes we don’t need to make a copy because we won’t be modifying the list. _(javascriptallonge.pdf (source-range-83ecb080-00191))_
- Once we’re done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-83ecb080-00193))_
- Looking at the code again, you see that the copy function doesn’t copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. _(javascriptallonge.pdf (source-range-83ecb080-00193))_

## Tortoises, Hares, and Teleporting Turtles

- It was, “Write an algorithm to detect a loop in a linked list, in constant space.” I’m not particularly surprised that I couldn’t think up an answer in a few minutes at the time. _(javascriptallonge.pdf (source-range-83ecb080-00195))_
- Eventually, I came up with something and tried it (In Java!) on my home PC. _(javascriptallonge.pdf (source-range-83ecb080-00195))_
- This is the “trick answer” to a question about finding a missing integer from a list, so I was trying the old, “Transform this into a problem you’ve already solved[74] ” meta-algorithm. _(javascriptallonge.pdf (source-range-83ecb080-00195))_
- No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you’ll detect the loop. _(javascriptallonge.pdf (source-range-83ecb080-00196))_
- You have two node references, and one traverses the list at twice the speed of the other. _(javascriptallonge.pdf (source-range-83ecb080-00196))_
- This algorithm is called “The Tortoise and the Hare,” and was discovered by Robert Floyd in the 1960s. _(javascriptallonge.pdf (source-range-83ecb080-00196))_
- This algorithm is called “The Tortoise and the Hare,” and was discovered by Robert Floyd in the 1960s. _(javascriptallonge.pdf (source-range-83ecb080-00196))_
- No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you’ll detect the loop. _(javascriptallonge.pdf (source-range-83ecb080-00196))_
- It seems to be faster under certain circumstances, depending on the size of the loop and the relative costs of certain operations. _(javascriptallonge.pdf (source-range-83ecb080-00197))_
- My first pass at it was clumsy, but it was roughly equivalent to this: **const** teleportingTurtle = (list) => { **let** speed = 1, rabbit = list, turtle = rabbit; **while** ( **true** ) { **for** ( **let** i = 0; i <= speed; i += 1) { rabbit = rabbit.rest; **if** (rabbit == **null** ) { **return false** ; } **if** (rabbit === turtle) { **return true** ; } } turtle = rabbit; speed *= 2; } **return false** ; }; **const** aList = list(1, 2, 3, 4, 5); teleportingTurtle(aList) _//=> false_ forceAppend(aList, aList.rest.rest); teleportingTurtle(aList); _//=> true_ _(javascriptallonge.pdf (source-range-83ecb080-00197))_
- What’s interesting about these two algorithms is that they both _tangle_ two separate concerns: How to traverse a data structure, and what to do with the elements that you encounter. _(javascriptallonge.pdf (source-range-83ecb080-00197))_
- At the time, I couldn’t think of any way to use hashing to solve the problem, so I gave up and tried to fit this into a powers-of-two algorithm. _(javascriptallonge.pdf (source-range-83ecb080-00197))_

## Functional Iterators

- Well, we call arraySum with an array, and it has baked into it a method for traversing the array. _(javascriptallonge.pdf (source-range-83ecb080-00199))_
- But it still relies on foldArrayWith, so it can only sum arrays. _(javascriptallonge.pdf (source-range-83ecb080-00199))_
- Perhaps we could extract both of those things. _(javascriptallonge.pdf (source-range-83ecb080-00199))_
- The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. _(javascriptallonge.pdf (source-range-83ecb080-00199))_
- But it still relies on foldArrayWith, so it can only sum arrays. _(javascriptallonge.pdf (source-range-83ecb080-00199))_
- The sumFoldable function doesn’t care what kind of data structure we have, as long as it’s foldable. _(javascriptallonge.pdf (source-range-83ecb080-00200))_
- We’ve found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we’ve completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really). _(javascriptallonge.pdf (source-range-83ecb080-00200))_
- Notice that buried inside our loop, we have bound the names done and value. _(javascriptallonge.pdf (source-range-83ecb080-00201))_
- And worst of all, we’re getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0. _(javascriptallonge.pdf (source-range-83ecb080-00201))_
- Nevertheless, there is some value in being able to express some algorithms as iteration. _(javascriptallonge.pdf (source-range-83ecb080-00201))_
- We can put those into a POJO (a Plain Old JavaScript Object). _(javascriptallonge.pdf (source-range-83ecb080-00201))_
- Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. _(javascriptallonge.pdf (source-range-83ecb080-00201))_
- JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. _(javascriptallonge.pdf (source-range-83ecb080-00201))_
- Notice that buried inside our loop, we have bound the names done and value. _(javascriptallonge.pdf (source-range-83ecb080-00201))_
- All the summing code needs to know is to add eachIteration.value. _(javascriptallonge.pdf (source-range-83ecb080-00202))_
- With this code, we make a POJO that has done and value keys. _(javascriptallonge.pdf (source-range-83ecb080-00202))_
- The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. _(javascriptallonge.pdf (source-range-83ecb080-00203))_
- Now this is something else. _(javascriptallonge.pdf (source-range-83ecb080-00203))_
- We can write a different iterator for a different data structure. _(javascriptallonge.pdf (source-range-83ecb080-00203))_
- When they iterate over an array or linked list, they are traversing something that is already there. _(javascriptallonge.pdf (source-range-83ecb080-00204))_
- It’s possible to write a generic unfold mechanism, but let’s pass on to what we can do with unfolded iterators. _(javascriptallonge.pdf (source-range-83ecb080-00205))_
- A function that starts with a seed and expands it into a data structure is called an _unfold_ . _(javascriptallonge.pdf (source-range-83ecb080-00205))_
- A function that starts with a seed and expands it into a data structure is called an _unfold_ . _(javascriptallonge.pdf (source-range-83ecb080-00205))_
- We’ll need an iterator that produces odd numbers. _(javascriptallonge.pdf (source-range-83ecb080-00206))_
- This business of going on forever has some drawbacks. _(javascriptallonge.pdf (source-range-83ecb080-00206))_
- In Smalltalk, for example, they are known as collect, select, and detect. _(javascriptallonge.pdf (source-range-83ecb080-00207))_
- Many programmers coming to JavaScript from other languages are familiar with three “canonical” operations on collections: folding, filtering, and finding. _(javascriptallonge.pdf (source-range-83ecb080-00207))_
- 152 **const** odds = () => { **let** number = 1; **return** () => { **const** value = number; number += 2; **return** {done: **false** , value}; } } **const** squareOf = callLeft(mapIteratorWith, (x) => x * x) toArray(take(squareOf(odds()), 5)) _//=> [1, 9, 25, 49, 81]_ We could also write a filter for iterators to accompany our mapping function: **const** filterIteratorWith = (fn, iterator) => () => { **do** { **const** {done, value} = iterator(); } **while** (!done && !fn(value)); **return** {done, value}; } **const** oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1); toArray(take(squareOf(oddsOf(NumberIterator(1))), 5)) _//=> [1, 9, 25, 49, 81]_ Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. _(javascriptallonge.pdf (source-range-83ecb080-00207))_
- In Smalltalk, for example, they are known as collect, select, and detect. _(javascriptallonge.pdf (source-range-83ecb080-00207))_
- One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. _(javascriptallonge.pdf (source-range-83ecb080-00208))_
- This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. _(javascriptallonge.pdf (source-range-83ecb080-00208))_
- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer “own” that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-83ecb080-00208))_
- JavaScript would apply fn to every element. _(javascriptallonge.pdf (source-range-83ecb080-00208))_
- There are some important implications of stateful functions. _(javascriptallonge.pdf (source-range-83ecb080-00208))_
- If array was very large, and fn very slow, this would consume a lot of unnecessary time. _(javascriptallonge.pdf (source-range-83ecb080-00208))_
- And if fn had some sort of side-effect, the program could be buggy. _(javascriptallonge.pdf (source-range-83ecb080-00208))_
- This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. _(javascriptallonge.pdf (source-range-83ecb080-00208))_

## Making Data Out Of Functions

- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. _(javascriptallonge.pdf (source-range-83ecb080-00210))_
- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-83ecb080-00210))_
- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-83ecb080-00210))_
- For example, we don’t need arrays to represent lists, or even POJOs to represent nodes in a linked list. _(javascriptallonge.pdf (source-range-83ecb080-00211))_
- They established that arbitrary computations could be represented a small set of axiomatic components. _(javascriptallonge.pdf (source-range-83ecb080-00211))_
- The oscin.es[77] library contains code for all of the standard combinators and for experimenting using the standard notation. _(javascriptallonge.pdf (source-range-83ecb080-00211))_
- They searched for a radically simpler set of tools that could accomplish all of the same things. _(javascriptallonge.pdf (source-range-83ecb080-00211))_
- We can model lists just using functions. _(javascriptallonge.pdf (source-range-83ecb080-00211))_
- Let’s start with some of the building blocks of combinatory logic, the K, I, and V combinators, nicknamed the “Kestrel”, the “Idiot Bird”, and the “Vireo:” > 76http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422 _(javascriptallonge.pdf (source-range-83ecb080-00211))_
- For example, we don’t need arrays to represent lists, or even POJOs to represent nodes in a linked list. _(javascriptallonge.pdf (source-range-83ecb080-00211))_
- Given two values, we can say that K always returns the _first_ value: K(x)(y) => x (that’s not valid JavaScript, but it’s essentially how it works). _(javascriptallonge.pdf (source-range-83ecb080-00212))_
- The kestrel, or K, is a function that makes constant functions. _(javascriptallonge.pdf (source-range-83ecb080-00212))_
- A _constant function_ is a function that always returns the same thing, no matter what you give it. _(javascriptallonge.pdf (source-range-83ecb080-00212))_
- The _identity function_ is a function that evaluates to whatever parameter you pass it. _(javascriptallonge.pdf (source-range-83ecb080-00212))_
- You give it a value, and it returns a constant function that gives that value. _(javascriptallonge.pdf (source-range-83ecb080-00212))_
- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. _(javascriptallonge.pdf (source-range-83ecb080-00213))_
- Given two values, we can say that K always returns the _first_ value, and given two values, K(I) always returns the _second_ value. _(javascriptallonge.pdf (source-range-83ecb080-00213))_
- So if we wanted to use them with a two-element array, we’d need to have a piece of code that calls some code. _(javascriptallonge.pdf (source-range-83ecb080-00214))_
- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. _(javascriptallonge.pdf (source-range-83ecb080-00214))_
- Our latin data structure is no longer a dumb data structure, it’s a function. _(javascriptallonge.pdf (source-range-83ecb080-00215))_
- In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-83ecb080-00215))_
- Let’s extract those into parameters: (first, second) => (selector) => selector(first)(second) For consistency with the way combinators are written as functions taking just one parameter, we’ll curry[78] the function: (first) => (second) => (selector) => selector(first)(second) Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specific pair, we’ll use the name aPair by default): **const** first = K, second = K(I), pair = (first) => (second) => (selector) => selector(first)(second); **const** latin = pair("primus")("secundus"); latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_ _(javascriptallonge.pdf (source-range-83ecb080-00215))_
- One notable example is the “thrush” or T combinator: It takes one value and applies it to a function. _(javascriptallonge.pdf (source-range-83ecb080-00216))_
- Here’s another look at linked lists using POJOs. _(javascriptallonge.pdf (source-range-83ecb080-00216))_
- It is known to most programmers as .tap. _(javascriptallonge.pdf (source-range-83ecb080-00216))_
- It says, “take these two values and apply them to this function.” There are other, similar combinators that apply values to functions. _(javascriptallonge.pdf (source-range-83ecb080-00216))_
- We write them in a backwards way, but they seem to work. _(javascriptallonge.pdf (source-range-83ecb080-00218))_
- Presto, **we can use pure functions to represent a linked list** . _(javascriptallonge.pdf (source-range-83ecb080-00218))_
- And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else. _(javascriptallonge.pdf (source-range-83ecb080-00218))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-83ecb080-00219))_
- This follows the philosophy we used with data structures: The function doing the work inspects the data structure. _(javascriptallonge.pdf (source-range-83ecb080-00219))_
- Let’s presume we are working with a slightly higher abstraction, we’ll call it a list. _(javascriptallonge.pdf (source-range-83ecb080-00219))_
- Now we’ll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. _(javascriptallonge.pdf (source-range-83ecb080-00219))_
- We used functions to replace arrays and POJOs, but we still use JavaScript’s built-in operators to test for equality (===) and to branch ?:. _(javascriptallonge.pdf (source-range-83ecb080-00219))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-83ecb080-00219))_
- We can write reverse and mapWith as well. _(javascriptallonge.pdf (source-range-83ecb080-00220))_
- However, that is not the interesting thing to note here. _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- You can establish that K and K(I) can represent true and false, model magnitudes with Church Numerals[79] or Surreal Numbers[80] , and build your way up to printing FizzBuzz. _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- Practically speaking, languages like JavaScript already provide arrays with mapping and folding methods, choice operations, and other rich constructs. _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- Functions are a fundamental building block of computation. _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- (Knowing that it can be done, on the other hand, is very important to understanding computer science.) Knowing how to make a list out of just functions is a little like knowing that photons are the Gauge Bosons[81] of the electromagnetic force. _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- Knowing how to make a linked list out of functions is not really necessary for the working programmer. _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- There are lots of similar texts explaining how to construct complex semantics out of functions. _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else. _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- They are “axioms” of combinatory logic, and can be used to compute anything that JavaScript can compute. _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- All we know is that we can pass the pair function a function of our own, at it will be called with the elements of the pair. _(javascriptallonge.pdf (source-range-83ecb080-00222))_
- To make pairs work, we did things _backwards_ , we passed the first and rest functions to the pair, and the pair called our function. _(javascriptallonge.pdf (source-range-83ecb080-00222))_
- We could have written a pair that stored its elements in an array, or a pair that stored its elements in a POJO. _(javascriptallonge.pdf (source-range-83ecb080-00222))_
- The exact implementation of a pair is hidden from the code that uses a pair. _(javascriptallonge.pdf (source-range-83ecb080-00222))_
- We’re passing list what we want done with an empty list, and what we want done with a list that has at least one element. _(javascriptallonge.pdf (source-range-83ecb080-00222))_
- As it happened, the pair was composed by the vireo (or V combinator): (x) => (y) => (z) => z(x)(y). _(javascriptallonge.pdf (source-range-83ecb080-00222))_
- We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-83ecb080-00222))_
- But we could have done something completely different. _(javascriptallonge.pdf (source-range-83ecb080-00222))_
- This is a little gratuitous, but it makes the point: The code that uses the data doesn’t reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. _(javascriptallonge.pdf (source-range-83ecb080-00222))_
- We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-83ecb080-00222))_
- Having a list know itself whether it is empty hides implementation information from the code that uses lists. _(javascriptallonge.pdf (source-range-83ecb080-00223))_
- It presumes you can compare these things with the === operator. _(javascriptallonge.pdf (source-range-83ecb080-00223))_
- It is a tenet of Object-Oriented Programming, but it is **not** exclusive to OOP: We can and should design data structures to hide implementation information from the code that use them, whether we are working with functions, objects, or both. _(javascriptallonge.pdf (source-range-83ecb080-00223))_
- There are many tools for hiding implementation information, and we have now seen two particularly powerful patterns: _(javascriptallonge.pdf (source-range-83ecb080-00223))_
- - Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. _(javascriptallonge.pdf (source-range-83ecb080-00223))_
- This is a fundamental principle of good design. _(javascriptallonge.pdf (source-range-83ecb080-00223))_
- We can fix this with an isEmpty function, but now we’re pushing even more knowledge about the structure of lists into the code that uses them. _(javascriptallonge.pdf (source-range-83ecb080-00223))_
- It presumes there is one canonical empty list value. _(javascriptallonge.pdf (source-range-83ecb080-00223))_

## Recipes with Data

- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven’t been discussed in the text to this point, such as methods and/or prototypes. _(javascriptallonge.pdf (source-range-83ecb080-00226))_
- The overall _use_ of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-83ecb080-00226))_
- The overall _use_ of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-83ecb080-00226))_
- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven’t been discussed in the text to this point, such as methods and/or prototypes. _(javascriptallonge.pdf (source-range-83ecb080-00226))_

## mapWith

- But for the purposes of discussing ideas, we can use the same name twice in two different contexts. _(javascriptallonge.pdf (source-range-83ecb080-00228))_
- > 82Yes, we also used the name mapWith for working with ordinary collections elsewhere. _(javascriptallonge.pdf (source-range-83ecb080-00228))_
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. _(javascriptallonge.pdf (source-range-83ecb080-00228))_
- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. _(javascriptallonge.pdf (source-range-83ecb080-00228))_
- In JavaScript, arrays have a .map method. _(javascriptallonge.pdf (source-range-83ecb080-00228))_
- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. _(javascriptallonge.pdf (source-range-83ecb080-00228))_
- mapWith is a very convenient abstraction for a very common pattern. _(javascriptallonge.pdf (source-range-83ecb080-00229))_

## Flip

- Let’s consider the case whether we have a map function of our own, perhaps from the allong.es[84] library, perhaps from Underscore[85] . _(javascriptallonge.pdf (source-range-83ecb080-00231))_
- What we have now is a function that takes a function and “flips” the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-83ecb080-00231))_
- What we have now is a function that takes a function and “flips” the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-83ecb080-00231))_
- Now if we write mapWith = flip(map), we can call mapWith(fn, list) or mapWith(fn)(list), our choice. _(javascriptallonge.pdf (source-range-83ecb080-00232))_
- Consider how we define mapWith now: **var** mapWith = flipAndCurry(map); _(javascriptallonge.pdf (source-range-83ecb080-00232))_
- When we learn about context and methods, we’ll see that flip throws the current context away, so it can’t be used to flip methods. _(javascriptallonge.pdf (source-range-83ecb080-00232))_
- Sometimes we’ll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). _(javascriptallonge.pdf (source-range-83ecb080-00232))_

## Object.assign

## Why?

- It enables you to make recursive functions without needing to bind a function to a name in an environment. _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- One tip is to use JavaScript to name things. _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- There are many explanations of the Y Combinator’s mechanism on the internet, but resist the temptation to read any of them: Work it out for yourself. _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- Well, besides all of the practical applications that combinators provide, there is this little thing called _The joy of working things out._ _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- This has little practical utility in JavaScript, but in combinatory logic it’s essential: With fixed-point combinators it’s possible to compute everything computable without binding names. _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-83ecb080-00239))_

## A Warm Cup: Basic Strings and Quasi-Literals

- Special characters can be included in a string literal by means of an _escape sequence_ . _(javascriptallonge.pdf (source-range-83ecb080-00242))_
- Writing is a big part of what makes us human, and strings are how JavaScript and most other languages represent writing. _(javascriptallonge.pdf (source-range-83ecb080-00242))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-83ecb080-00242))_
- Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-83ecb080-00242))_
- A quasi-literal can contain an expression to be evaluated. _(javascriptallonge.pdf (source-range-83ecb080-00242))_
- A quasi-literal is computationally equivalent to an expression using +. _(javascriptallonge.pdf (source-range-83ecb080-00242))_
- There are operators that can be used on strings. _(javascriptallonge.pdf (source-range-83ecb080-00242))_
- String manipulation is extremely common in programming. _(javascriptallonge.pdf (source-range-83ecb080-00242))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-83ecb080-00242))_
- Special characters can be included in a string literal by means of an _escape sequence_ . _(javascriptallonge.pdf (source-range-83ecb080-00242))_
- - 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big semantic difference between a quasi-literal and an expression. _(javascriptallonge.pdf (source-range-83ecb080-00243))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function’s body is evaluated. _(javascriptallonge.pdf (source-range-83ecb080-00243))_
- Thus, name is not bound to "Harry", it is bound to 'Arthur Dent', the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-83ecb080-00243))_
- Quasi-literals are expressions that resemble their result. _(javascriptallonge.pdf (source-range-83ecb080-00243))_
- - 'A popular number for nerds is' + (40 + 2) - _//=> 'A popular number for nerds is42'_ _(javascriptallonge.pdf (source-range-83ecb080-00243))_
- Thus, name is not bound to "Harry", it is bound to 'Arthur Dent', the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-83ecb080-00243))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function’s body is evaluated. _(javascriptallonge.pdf (source-range-83ecb080-00243))_

## Served by the Pot: Collections

- **Some different sized and coloured coffee pots by Antti Nurmesniemi, perhaps his most known design.** _(javascriptallonge.pdf (source-range-83ecb080-00245))_

## Iteration and Iterables

- Many objects in JavaScript can model collections of things. _(javascriptallonge.pdf (source-range-83ecb080-00247))_
- But sometimes you want to open it up and do things with its contents. _(javascriptallonge.pdf (source-range-83ecb080-00247))_
- Acting on the elements of a collection one at a time is called _iterating over the contents_ , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-83ecb080-00247))_
- We can do the same thing for objects. _(javascriptallonge.pdf (source-range-83ecb080-00247))_
- Acting on the elements of a collection one at a time is called _iterating over the contents_ , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-83ecb080-00247))_
- Note that it uses the function keyword, so when we invoke it with stack.iterator(), JavaScript sets this to the value of stack. _(javascriptallonge.pdf (source-range-83ecb080-00249))_
- Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter(). _(javascriptallonge.pdf (source-range-83ecb080-00249))_
- } function, and that’s where this is bound to the value of stack. _(javascriptallonge.pdf (source-range-83ecb080-00249))_
- Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter(). _(javascriptallonge.pdf (source-range-83ecb080-00249))_
- In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. _(javascriptallonge.pdf (source-range-83ecb080-00250))_
- Iteration for functions and objects has been around for many, many decades. _(javascriptallonge.pdf (source-range-83ecb080-00250))_
- Our functions don’t need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-83ecb080-00250))_
- The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-83ecb080-00250))_
- If we write a program with the presumption that “everything is an object,” we can write maps, folds, and filters that work on objects. _(javascriptallonge.pdf (source-range-83ecb080-00250))_
- The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-83ecb080-00250))_
- Instead of having a function that you call to get the next element, you have an object with a .next() method. _(javascriptallonge.pdf (source-range-83ecb080-00251))_
- Fortunately, an iterator object is almost as simple as an iterator function. _(javascriptallonge.pdf (source-range-83ecb080-00251))_
- People have been writing iterators since JavaScript was first released in the late 1990s. _(javascriptallonge.pdf (source-range-83ecb080-00252))_
- Now our .iterator() method is returning an iterator object. _(javascriptallonge.pdf (source-range-83ecb080-00252))_
- But having started by building functional iterators, we understand what is happening underneath the object’s scaffolding. _(javascriptallonge.pdf (source-range-83ecb080-00252))_
- Since there was no particular standard way to do it, people used all sorts of methods, and their methods returned all sorts of things: Objects with various interfaces, functional iterators, you name it. _(javascriptallonge.pdf (source-range-83ecb080-00252))_
- To ensure that the method would not conflict with any existing code, JavaScript provides a _symbol_ . _(javascriptallonge.pdf (source-range-83ecb080-00252))_
- Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator. _(javascriptallonge.pdf (source-range-83ecb080-00252))_
- When working with objects, we do things the object way. _(javascriptallonge.pdf (source-range-83ecb080-00252))_
- So, when a standard way to write iterators was added to the JavaScript language, it didn’t make sense to use a method like .iterator() for it: That would conflict with existing code. _(javascriptallonge.pdf (source-range-83ecb080-00252))_
- Symbols are unique constants that are guaranteed not to conflict with existing strings. _(javascriptallonge.pdf (source-range-83ecb080-00252))_
- > 88 You can read more about JavaScript symbols in Axel Rauschmayer’s Symbols in ECMAScript 2015. _(javascriptallonge.pdf (source-range-83ecb080-00252))_
- We’ll do that using the [ ] syntax for using an expression as an object literal key: **const** Stack3 = () => ({ array: [], index: -1, push (value) { **return this** .array[ **this** .index += 1] = value; }, pop () { **const** value = **this** .array[ **this** .index]; **this** .array[ **this** .index] = **undefined** ; **if** ( **this** .index >= 0) { **this** .index -= 1 } **return** value }, isEmpty () { **return this** .index < 0 }, [Symbol.iterator] () { **let** iterationIndex = **this** .index; **return** { next () { **if** (iterationIndex > **this** .index) { iterationIndex = **this** .index; } **if** (iterationIndex < 0) { **return** {done: **true** }; } **else** { **return** {done: **false** , value: **this** .array[iterationIndex--]} } } } } }); **const** stack = Stack3(); _(javascriptallonge.pdf (source-range-83ecb080-00253))_
- Our stack does, so instead of binding the existing iterator method to the name iterator, we bind it to the Symbol.iterator. _(javascriptallonge.pdf (source-range-83ecb080-00253))_
- The for...of loop works directly with any object that is _iterable_ , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. _(javascriptallonge.pdf (source-range-83ecb080-00254))_
- And if we have an infinite collection, spreading is going to fail outright as we’re about to see. _(javascriptallonge.pdf (source-range-83ecb080-00256))_
- And there’s one more thing: You recall that the spread operator (...) can spread the elements of an array in an array literal or as parameters in a function invocation. _(javascriptallonge.pdf (source-range-83ecb080-00256))_
- That might be very wasteful for extremely large collections. _(javascriptallonge.pdf (source-range-83ecb080-00256))_
- For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-83ecb080-00256))_
- Now is the time to note that we can spread any iterable. _(javascriptallonge.pdf (source-range-83ecb080-00256))_
- For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-83ecb080-00256))_
- Attempting to spread an infinite iterable into an array is always going to fail. _(javascriptallonge.pdf (source-range-83ecb080-00257))_
- Iterables needn’t represent ordered collections. _(javascriptallonge.pdf (source-range-83ecb080-00257))_
- The iterables we’re discussing represent _ordered collections_ . _(javascriptallonge.pdf (source-range-83ecb080-00257))_
- One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. _(javascriptallonge.pdf (source-range-83ecb080-00257))_
- This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator], and ensuring that our iterators start at the beginning and work forward. _(javascriptallonge.pdf (source-range-83ecb080-00257))_
- But for the purposes of discussing ideas, we can use the same name twice in two different contexts. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- Here’s mapWith, it takes an ordered collection, and returns another ordered collection representing a mapping over the original:[89] > 89Yes, we also used the name mapWith for working with ordinary collections elsewhere. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- Let’s define some operations on ordered collections. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- To reiterate (hah), an ordered collection represents a (possibly infinite) collection of elements that are in some order. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- Every time we get an iterator from an ordered collection, we start iterating from the beginning. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- Right now, we’re just looking at ordered collections. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- Many operations on ordered collections return another ordered collection. _(javascriptallonge.pdf (source-range-83ecb080-00259))_
- They do so by taking care to iterate over a result freshly every time we get an iterator for them. _(javascriptallonge.pdf (source-range-83ecb080-00259))_
- An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order. _(javascriptallonge.pdf (source-range-83ecb080-00259))_
- This illustrates the general pattern of working with ordered collections: We make them _iterables_ , meaning that they have a [Symbol.iterator] method, that returns an _iterator_ . _(javascriptallonge.pdf (source-range-83ecb080-00259))_
- Numbers is an ordered collection. _(javascriptallonge.pdf (source-range-83ecb080-00260))_
- Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. _(javascriptallonge.pdf (source-range-83ecb080-00260))_
- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. _(javascriptallonge.pdf (source-range-83ecb080-00260))_
- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. _(javascriptallonge.pdf (source-range-83ecb080-00260))_
- Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. _(javascriptallonge.pdf (source-range-83ecb080-00260))_
- For completeness, here are two more handy iterable functions. _(javascriptallonge.pdf (source-range-83ecb080-00262))_
- No, of course not, we can do anything we like with them. _(javascriptallonge.pdf (source-range-83ecb080-00262))_
- first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. _(javascriptallonge.pdf (source-range-83ecb080-00262))_
- Like mapWith, they preserve the ordered collection semantics of whatever you give them. _(javascriptallonge.pdf (source-range-83ecb080-00262))_
- [...UpTo1000] _//=>_ [1,81,121,361,441,841,961] [...UpTo1000] _//=>_ [1,81,121,361,441,841,961] As we expect from an ordered collection, each time we iterate over UpTo1000, we begin at the beginning. _(javascriptallonge.pdf (source-range-83ecb080-00262))_
- And we can assign properties to functions with a . _(javascriptallonge.pdf (source-range-83ecb080-00263))_
- And if we assign a function to a property, we’ve created a method. _(javascriptallonge.pdf (source-range-83ecb080-00263))_
- As you recall, functions are mutable objects. _(javascriptallonge.pdf (source-range-83ecb080-00263))_
- One useful thing is to write a .from function that gathers an iterable into a particular collection type. _(javascriptallonge.pdf (source-range-83ecb080-00263))_
- Array.from(UpTo1000) _//=> [1,81,121,361,441,841,961]_ We can do the same with our own collections. _(javascriptallonge.pdf (source-range-83ecb080-00263))_
- Separating concerns with iterators speaks to JavaScript’s fundamental nature: It’s a language that _wants_ to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-83ecb080-00264))_
- _Iterable_ ordered collections can be iterated over or gathered into another collection. _(javascriptallonge.pdf (source-range-83ecb080-00264))_
- Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection from what we want to do with the elements of a collection. _(javascriptallonge.pdf (source-range-83ecb080-00264))_

## Generating Iterables

- Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done. _(javascriptallonge.pdf (source-range-83ecb080-00266))_
- Iterators have to arrange its own state such that when you call them, they compute and return the next item. _(javascriptallonge.pdf (source-range-83ecb080-00266))_
- Iterables look cool, but then again, everything looks amazing when you’re given cherry-picked examples. _(javascriptallonge.pdf (source-range-83ecb080-00266))_
- This seems blindingly obvious and simple. _(javascriptallonge.pdf (source-range-83ecb080-00266))_
- Iterables look cool, but then again, everything looks amazing when you’re given cherry-picked examples. _(javascriptallonge.pdf (source-range-83ecb080-00266))_
- We would _generate_ numbers. _(javascriptallonge.pdf (source-range-83ecb080-00267))_
- Of course, when we have some code that makes a bunch of something, we don’t usually write it like that. _(javascriptallonge.pdf (source-range-83ecb080-00267))_
- There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers. _(javascriptallonge.pdf (source-range-83ecb080-00267))_
- Given an array that might contain arrays, let’s say we want to generate all the “leaf” elements, i.e. _(javascriptallonge.pdf (source-range-83ecb080-00268))_
- elements that are not, themselves, iterable. _(javascriptallonge.pdf (source-range-83ecb080-00268))_
- One of those cases is when we have to recursively enumerate something. _(javascriptallonge.pdf (source-range-83ecb080-00268))_
- Well, there are some collections that are much easier to generate than to iterate over. _(javascriptallonge.pdf (source-range-83ecb080-00268))_
- Generators have to manage the exact same amount of state, but sometimes, it’s much easier to manage that state in a generator. _(javascriptallonge.pdf (source-range-83ecb080-00268))_
- Iterators maintain state, that’s what they do. _(javascriptallonge.pdf (source-range-83ecb080-00268))_
- If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next, we’re left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. _(javascriptallonge.pdf (source-range-83ecb080-00269))_
- In essence, both the generation and iteration implementations have stacks, but the generation version’s stack is _implicit_ , while the iteration version’s stack is _explicit_ . _(javascriptallonge.pdf (source-range-83ecb080-00269))_
- - The second element of the fibonacci sequence is one. _(javascriptallonge.pdf (source-range-83ecb080-00270))_
- - Every subsequent element of the fibonacci sequence is the sum of the previous two elements. _(javascriptallonge.pdf (source-range-83ecb080-00270))_
- Some iterables can be modelled as state machines. _(javascriptallonge.pdf (source-range-83ecb080-00270))_
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We’re reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. _(javascriptallonge.pdf (source-range-83ecb080-00270))_
- - The first element of the fibonacci sequence is zero. _(javascriptallonge.pdf (source-range-83ecb080-00270))_
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We’re reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. _(javascriptallonge.pdf (source-range-83ecb080-00270))_
- The thing to note here is that our fibonacci generator has three states: generating 0, generating 1, and generating everything after that. _(javascriptallonge.pdf (source-range-83ecb080-00271))_
- This isn’t a good fit for an iterator, because iterators have one functional entry point and therefore, we’d have to represent our three states explicitly, perhaps using a state pattern[90] : _(javascriptallonge.pdf (source-range-83ecb080-00271))_
- The thing to note here is that our fibonacci generator has three states: generating 0, generating 1, and generating everything after that. _(javascriptallonge.pdf (source-range-83ecb080-00271))_
- This isn’t a good fit for an iterator, because iterators have one functional entry point and therefore, we’d have to represent our three states explicitly, perhaps using a state pattern[90] : _(javascriptallonge.pdf (source-range-83ecb080-00271))_
- An iterator written in a generation style is called a _generator_ . _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- So we see the same thing: The generation version has state, but it’s implicit in JavaScript’s linear control flow. _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- We can write an iterator, but use a generation style of programming. _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- In a generator, we write “do this, then this, then this.” In an iterator, we have to wrap that up and explicitly keep track of what step we’re on. _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- Again, this is not particularly horrendous, but like the recursive example, we’re explicitly greenspunning the natural linear state. _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- Given the title of this chapter, it is not a surprise that JavaScript makes this possible. _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator. _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- This makes sense, because empty never yields anything. _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- Generator functions can take an argument. _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- Whereas the iteration version must make that state explicit. _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- Whereas the iteration version must make that state explicit. _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- An iterator written in a generation style is called a _generator_ . _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- This makes sense, because empty never yields anything. _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- In a generator, we write “do this, then this, then this.” In an iterator, we have to wrap that up and explicitly keep track of what step we’re on. _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- Recalling the way we wrote ordered collections, we could make a collection that uses a generator function: _(javascriptallonge.pdf (source-range-83ecb080-00275))_
- Of course, generators need not be implemented exactly as coroutines. _(javascriptallonge.pdf (source-range-83ecb080-00275))_
- For example, a “transpiler” might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we’ll see that later): **const** oneTwoThree = **function** () { **let** state = 'newborn'; **return** { next () { **switch** (state) { **case** 'newborn': state = 1; **return** {value: 1}; **case** 1: state = 2; **return** {value: 2} **case** 2: state = 3; **return** {value: 3} **case** 3: **return** {done: **true** }; } } } }; But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next(), it runs until it returns, ends, or yields. _(javascriptallonge.pdf (source-range-83ecb080-00275))_
- As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3. _(javascriptallonge.pdf (source-range-83ecb080-00275))_
- Our generator function oneTwoThree is not an iterator. _(javascriptallonge.pdf (source-range-83ecb080-00275))_
- If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-83ecb080-00275))_
- If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-83ecb080-00275))_
- For example, a “transpiler” might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we’ll see that later): **const** oneTwoThree = **function** () { **let** state = 'newborn'; **return** { next () { **switch** (state) { **case** 'newborn': state = 1; **return** {value: 1}; **case** 1: state = 2; **return** {value: 2} **case** 2: state = 3; **return** {value: 3} **case** 3: **return** {done: **true** }; } } } }; But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next(), it runs until it returns, ends, or yields. _(javascriptallonge.pdf (source-range-83ecb080-00275))_
- This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing _(javascriptallonge.pdf (source-range-83ecb080-00276))_
- Because it’s declared *[Symbol.iterator], it’s a generator instead of an iterator. _(javascriptallonge.pdf (source-range-83ecb080-00277))_
- So to summarize, ThreeNumbers is an object that we’ve made iterable, by way of writing a _generator_ method for [Symbol.iterator]. _(javascriptallonge.pdf (source-range-83ecb080-00277))_
- Because it’s declared *[Symbol.iterator], it’s a generator instead of an iterator. _(javascriptallonge.pdf (source-range-83ecb080-00277))_
- And the generator’s syntax allows us to use JavaScript’s natural management of state instead of constantly rolling our own. _(javascriptallonge.pdf (source-range-83ecb080-00279))_
- We’ve writing a function that returns an iterator, but we used a generator to do it. _(javascriptallonge.pdf (source-range-83ecb080-00279))_
- It works, but as we’ve just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object:[93] > 93There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-83ecb080-00280))_
- It works, but as we’ve just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object:[93] > 93There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-83ecb080-00280))_
- This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping. _(javascriptallonge.pdf (source-range-83ecb080-00281))_
- If e is not an iterable, yield e. _(javascriptallonge.pdf (source-range-83ecb080-00281))_
- We take advantage of the for...of loop in a plain and direct way: For each element e, if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. _(javascriptallonge.pdf (source-range-83ecb080-00281))_
- Now that we know about iterables, we can rewrite our iterable operations as generators. _(javascriptallonge.pdf (source-range-83ecb080-00283))_
- No need to return an object with a .next() method. _(javascriptallonge.pdf (source-range-83ecb080-00284))_
- We can do the same thing with our other operations like filterWith and untilWith. _(javascriptallonge.pdf (source-range-83ecb080-00284))_
- This is especially useful for making iterables. _(javascriptallonge.pdf (source-range-83ecb080-00285))_
- And we don’t need to worry about wrapping our values in an object with .done and .value properties. _(javascriptallonge.pdf (source-range-83ecb080-00285))_
- Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns. _(javascriptallonge.pdf (source-range-83ecb080-00285))_
- 222 **function** * untilWith (fn, iterable) { **for** ( **const** element **of** iterable) { **if** (fn(element)) **break** ; **yield** fn(element); } } first works directly with iterators and remains unchanged, but rest can be rewritten as a generator: **const** first = (iterable) => iterable[Symbol.iterator]().next().value; **function** * rest (iterable) { **const** iterator = iterable[Symbol.iterator](); iterator.next(); **yield** * iterator; } A generator is a function that is defined with function * and uses yield (or yield *) to generate values. _(javascriptallonge.pdf (source-range-83ecb080-00285))_

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00273, source-range-83ecb080-00276))_

> 208 Served by the Pot: Collections **function** * only (something) { **yield** something; }; only("you").next() _//=>_ {"done": **false** , value: "you"} Invoking only("you") returns an iterator that we can call with .next(), and it yields "you". Invoking only more than once gives us fresh iterators each time: only("you").next() _//=>_ {"done": **false** , value: "you"} only("the lonely").next() _//=>_ {"done": **false** , value: "the lonely"} We can invoke the same iterator twice: **const** six

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00275))_

> If we call our generator function more than once, we get new iterators.

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00279, source-range-83ecb080-00281))_

> 216 Served by the Pot: Collections We’ve writing a function that returns an iterator, but we used a generator to do it. And the generator’s syntax allows us to use JavaScript’s natural management of state instead of constantly rolling our own. Of course, we could just as easily write a generator function for Fibonacci numbers: **function** * fibonacci () { **let** a, b; **yield** a = 0; **yield** b = 1; **while** ( **true** ) { [a, b] = [b, a + b] **yield** b; } } **for** ( **const** i **of** fi

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00280))_

> But if you can write it as a simple generator, write it as a simple generator.

## Lazy and Eager Collections

- We tell ourselves that, well, a collection ought to know how to map itself. _(javascriptallonge.pdf (source-range-83ecb080-00287))_
- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack in the older style of object-oriented programming, we built “fat” objects. _(javascriptallonge.pdf (source-range-83ecb080-00287))_
- If we wanted to flatten collections to arrays, we wrote a .toArray method for each type of collection. _(javascriptallonge.pdf (source-range-83ecb080-00287))_
- Some methods are only added to a few collections, some are added to all. _(javascriptallonge.pdf (source-range-83ecb080-00287))_
- And if we want to create convenience methods, we can reuse common pieces. _(javascriptallonge.pdf (source-range-83ecb080-00287))_
- That’s a sign that we should work at a higher level of abstraction, and working with iterables is that higher level of abstraction. _(javascriptallonge.pdf (source-range-83ecb080-00287))_
- But we end up recreating the same bits of code in each .map method we create, in each .reduce method we create, in each .filter method we create, and in each .find method. _(javascriptallonge.pdf (source-range-83ecb080-00287))_
- That would be like saying that when we ask a bank teller for some cash, they personally print every bank note. _(javascriptallonge.pdf (source-range-83ecb080-00287))_
- The operations on iterables are tremendously valuable, but let’s reiterate why we care: In JavaScript, we build single-responsibility objects, and single-responsibility functions, and we compose these together to build more full-featured objects and algorithms. _(javascriptallonge.pdf (source-range-83ecb080-00287))_
- And they should know how to accomplish the desired result, but they should do so by delegating as much of the work as possible to operations like mapWith. _(javascriptallonge.pdf (source-range-83ecb080-00287))_
- Each one has its own variation, but the overall form is identical. _(javascriptallonge.pdf (source-range-83ecb080-00287))_
- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack. _(javascriptallonge.pdf (source-range-83ecb080-00287))_
- This “fat object” style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don’t need for the collection to handle every single detail. _(javascriptallonge.pdf (source-range-83ecb080-00287))_
- Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. _(javascriptallonge.pdf (source-range-83ecb080-00287))_
- Some methods are only added to a few collections, some are added to all. _(javascriptallonge.pdf (source-range-83ecb080-00287))_
- For simplicity, we’ll show how to mix it into Numbers and Pair. _(javascriptallonge.pdf (source-range-83ecb080-00291))_
- To use LazyCollection, we mix it into an any iterable object. _(javascriptallonge.pdf (source-range-83ecb080-00291))_
- Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. _(javascriptallonge.pdf (source-range-83ecb080-00294))_
- “Laziness” is a very pejorative word when applied to people. _(javascriptallonge.pdf (source-range-83ecb080-00294))_
- The effect is even more pronounced when we use methods like first, until, or take: _(javascriptallonge.pdf (source-range-83ecb080-00294))_
- They produce small iterable objects that refer back to the original iteration. _(javascriptallonge.pdf (source-range-83ecb080-00294))_
- But it can be an excellent strategy for efficiency in algorithms. _(javascriptallonge.pdf (source-range-83ecb080-00294))_
- Let’s be precise: _Laziness_ is the characteristic of not doing any work until you know you need the result of the work. _(javascriptallonge.pdf (source-range-83ecb080-00294))_
- _// Pair and Stack in action_ Stack.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .first() _//=> 100_ Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0) _//=> 220_ _(javascriptallonge.pdf (source-range-83ecb080-00294))_
- And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. _(javascriptallonge.pdf (source-range-83ecb080-00294))_
- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0) Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0) Both expressions evaluate to 220. _(javascriptallonge.pdf (source-range-83ecb080-00294))_
- And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. _(javascriptallonge.pdf (source-range-83ecb080-00294))_
- Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. _(javascriptallonge.pdf (source-range-83ecb080-00294))_
- It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. _(javascriptallonge.pdf (source-range-83ecb080-00295))_
- Stack.from([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) .map((x) => x * x) .filter((x) => x % 2 == 0) .first() This expression begins with a stack containing 30 elements. _(javascriptallonge.pdf (source-range-83ecb080-00295))_
- Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack’s elements, and it only needs to square two of those elements, 29 and 28, to return the answer. _(javascriptallonge.pdf (source-range-83ecb080-00295))_
- Same with .filter, we get an iterable that can iterate over the even squares, but not an actual stack or array. _(javascriptallonge.pdf (source-range-83ecb080-00295))_
- Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack’s elements, and it only needs to square two of those elements, 29 and 28, to return the answer. _(javascriptallonge.pdf (source-range-83ecb080-00295))_
- Let’s make iterable numbers. _(javascriptallonge.pdf (source-range-83ecb080-00296))_
- If we mutate a collection after taking an iterable, we might get an unexpected result. _(javascriptallonge.pdf (source-range-83ecb080-00297))_
- This is why “pure” functional languages like Haskell combine lazy semantics with immutable collections, and why even “impure” languages like Clojure emphasize the use of immutable collections. _(javascriptallonge.pdf (source-range-83ecb080-00297))_
- If we mutate a collection after taking an iterable, we might get an unexpected result. _(javascriptallonge.pdf (source-range-83ecb080-00297))_
- Pair is gatherable, because it implements .from(). _(javascriptallonge.pdf (source-range-83ecb080-00300))_
- Here is our Pair implementation. _(javascriptallonge.pdf (source-range-83ecb080-00300))_
- Pair is gatherable, because it implements .from(). _(javascriptallonge.pdf (source-range-83ecb080-00300))_

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00291, source-range-83ecb080-00295))_

> 227 Served by the Pot: Collections [Symbol.iterator]: () => { **const** iterator = **this** [Symbol.iterator](); **let** remainingElements = numberToTake; **return** { next: () => { **let** { done, value } = iterator.next(); done = done || remainingElements-- <= 0; **return** ({ done, value: done ? **undefined** : value }); } } } }, LazyCollection); } } To use LazyCollection, we mix it into an any iterable object. For simplicity, we’ll show how to mix it into Numbers and Pair. But it can also be

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00294))_

> When working with very large collections and many operations, this can be important.

## Interlude: The Carpenter Interviews for a Job

- Many companies use white-boarding code as an excuse to have a technical conversation with a candidate, and The Carpenter felt that being asked to whiteboard code was an excuse to have a technical conversation with a future colleague. _(javascriptallonge.pdf (source-range-83ecb080-00303))_
- A few minutes later, he was joined by one of the company’s developers, Christine. _(javascriptallonge.pdf (source-range-83ecb080-00303))_
- “The Carpenter” was a JavaScript programmer, well-known for a meticulous attention to detail and love for hand-crafted, exquisitely joined code. _(javascriptallonge.pdf (source-range-83ecb080-00303))_
- Despite his experience and industry longevity, the Carpenter did not mind being asked to demonstrate that he was, in fact, the person described on the resumé. _(javascriptallonge.pdf (source-range-83ecb080-00303))_
- After some small talk, Christine explained that they liked to ask candidates to whiteboard some code. _(javascriptallonge.pdf (source-range-83ecb080-00303))_
- After some small talk, Christine explained that they liked to ask candidates to whiteboard some code. _(javascriptallonge.pdf (source-range-83ecb080-00303))_
- Each move consists of moving the chequer one square in the direction of the arrow in the square it occupies. _(javascriptallonge.pdf (source-range-83ecb080-00304))_
- The problem is this: The game board is hidden from us. _(javascriptallonge.pdf (source-range-83ecb080-00304))_
- “↑, →, ↑, ↓, ↑, →…” Write an algorithm that will determine whether the game halts, strictly from the called out directions, in finite time and space. _(javascriptallonge.pdf (source-range-83ecb080-00304))_
- A chequer is placed randomly on the checkerboard. _(javascriptallonge.pdf (source-range-83ecb080-00304))_
- If the arrow should cause the chequer to move off the edge of the board, the game halts. _(javascriptallonge.pdf (source-range-83ecb080-00304))_
- “So,” The Carpenter asked, “I am to write an algorithm that takes a possibly infinite stream of…” Christine interrupted. _(javascriptallonge.pdf (source-range-83ecb080-00304))_
- To save time, The Carpenter had prepared the same answer for both questions. _(javascriptallonge.pdf (source-range-83ecb080-00306))_
- He then coached subsequent candidates to give polished answers to the company’s pet technical questions. _(javascriptallonge.pdf (source-range-83ecb080-00306))_
- placeholders to determine whether the game halts?” The Carpenter was not surprised at the problem. _(javascriptallonge.pdf (source-range-83ecb080-00306))_
- Bob had, in fact, warned The Carpenter that “Thing” liked to ask either or both of two questions: Determine how to detect a loop in a linked list, and determine whether the chequerboard game would halt. _(javascriptallonge.pdf (source-range-83ecb080-00306))_
- The Carpenter coughed softly, then began. _(javascriptallonge.pdf (source-range-83ecb080-00306))_
- He then coached subsequent candidates to give polished answers to the company’s pet technical questions. _(javascriptallonge.pdf (source-range-83ecb080-00306))_
- The Carpenter coughed softly, then began. _(javascriptallonge.pdf (source-range-83ecb080-00306))_
- “Now that we have an iterable, we can transform the iterable of arrows into an iterable of positions.” The Carpenter sketched quickly. _(javascriptallonge.pdf (source-range-83ecb080-00307))_
- A statefulMap is a lazy map that preserves state from iteration to iteration. _(javascriptallonge.pdf (source-range-83ecb080-00307))_
- Detecting whether the game terminates is equivalent to detecting whether the graph contains a cycle.” _(javascriptallonge.pdf (source-range-83ecb080-00308))_
- I approached this question in that spirit. _(javascriptallonge.pdf (source-range-83ecb080-00309))_
- The question was, _Given a linked list, detect whether it contains a cycle. _(javascriptallonge.pdf (source-range-83ecb080-00310))_
- I have never forgotten the question, or the general form of the solution. _(javascriptallonge.pdf (source-range-83ecb080-00310))_
- The Carpenter was confident that although nobody would write this exact code in production, prospective employers would also recognize that nobody would try to detect whether a chequer game terminates in production, either. _(javascriptallonge.pdf (source-range-83ecb080-00311))_
- It also cleanly separates the mechanics of the game from the algorithm for detecting cycles in a graph.” The Carpenter sat down and waited. _(javascriptallonge.pdf (source-range-83ecb080-00311))_
- Christine looked at the solution on the board, frowned, and glanced at the clock on the wall. _(javascriptallonge.pdf (source-range-83ecb080-00311))_
- This type of solution provided an excellent opportunity to explore lazy versus eager evaluation, the performance of iterators versus native iteration, single responsibility design, and many other rich topics. _(javascriptallonge.pdf (source-range-83ecb080-00311))_
- A few drinks later, The Carpenter was telling his Thing story and an engineer named Kidu introduced themself. _(javascriptallonge.pdf (source-range-83ecb080-00312))_
- 247 would say was, _Writes unreadable code_ . _(javascriptallonge.pdf (source-range-83ecb080-00312))_
- I should have used a Teleporting Tortoise!” _// implements Teleporting Tortoise // cycle detection algorithm._ **const** hasCycle = (iterable) => { **let** iterator = iterable[Symbol.iterator](), teleportDistance = 1; **while** ( **true** ) { **let** {value, done} = iterator.next(), tortoise = value; **if** (done) **return false** ; **for** ( **let** i = 0; i < teleportDistance; ++i) { **let** {value, done} = iterator.next(), hare = value; **if** (done) **return false** ; **if** (tortoise === hare) **return true** ; } teleportDistance *= 2; } **return false** ; }; _(javascriptallonge.pdf (source-range-83ecb080-00313))_
- I had a look at the code you left on the whiteboard. _(javascriptallonge.pdf (source-range-83ecb080-00313))_
- Whereas the problem as stated involves a single stream of directions. _(javascriptallonge.pdf (source-range-83ecb080-00313))_
- Whereas the problem as stated involves a single stream of directions. _(javascriptallonge.pdf (source-range-83ecb080-00313))_
- The Carpenter stared at Kidu’s solution. _(javascriptallonge.pdf (source-range-83ecb080-00314))_

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00304, source-range-83ecb080-00306))_

> Served by the Pot: Collections 239 **==> picture [476 x 314] intentionally omitted <==** **----- Start of picture text -----**<br> 94<br>**----- End of picture text -----**<br> Christine intoned the question, as if by rote: Consider a finite checkerboard of unknown size. On each square, we randomly place an arrow pointing to one of its four sides. A chequer is placed randomly on the checkerboard. Each move consists of moving the chequer one square in the direction of the arrow in the square it o

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00305))_

> You may use babeljs.io[95] , or ES6Fiddle[96] to check your work.

## Interactive Generators

- The moves a player makes are a stream of values, just like the contents of an array can be consider a stream of values. _(javascriptallonge.pdf (source-range-83ecb080-00316))_
- The first player will always be o, and they will always place their chequer in the top-left corner, coincidentally numbered o: _(javascriptallonge.pdf (source-range-83ecb080-00316))_
- We used generators to build iterators that maintain implicit state. _(javascriptallonge.pdf (source-range-83ecb080-00316))_
- But of course, iterating over a stream of moves requires us to wait for the game to be over so we know what moves were made. _(javascriptallonge.pdf (source-range-83ecb080-00316))_
- But there are other times we want to build functions that maintain implicit state. _(javascriptallonge.pdf (source-range-83ecb080-00316))_
- Let’s take a look at a very simple example, naughts and crosses[99] (We really ought to do something like Chess, but that might be a little out of scope for this chapter). _(javascriptallonge.pdf (source-range-83ecb080-00316))_
- Let’s start by looking at a very simple example of a function that can be written statefully. _(javascriptallonge.pdf (source-range-83ecb080-00316))_
- We saw how to use them for recursive unfolds and state machines. _(javascriptallonge.pdf (source-range-83ecb080-00316))_
- We could plays naughts and crosses as a stateless function. _(javascriptallonge.pdf (source-range-83ecb080-00318))_
- We can encode the board in several different ways. _(javascriptallonge.pdf (source-range-83ecb080-00319))_
- We’ll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. _(javascriptallonge.pdf (source-range-83ecb080-00320))_
- [ 'o', 'x', ' ', 'x', ' ', ' ', 'o', ' ', ' ' ] We can use a POJO to make a map from positions to moves. _(javascriptallonge.pdf (source-range-83ecb080-00320))_
- In that case, we need a stateful function. _(javascriptallonge.pdf (source-range-83ecb080-00322))_
- A game like this is absolutely a state machine, and we’ve explicitly coded those states into the lookup table. _(javascriptallonge.pdf (source-range-83ecb080-00323))_
- The state is encoded entirely in data. _(javascriptallonge.pdf (source-range-83ecb080-00323))_
- When we looked at generators, we saw that some iterators are inherently stateful, but sometimes it is awkward to represent them in a fully stateless fashion. _(javascriptallonge.pdf (source-range-83ecb080-00323))_
- If we were in full control of the interaction, it would be easy to encode the game play as a decision tree instead of as a lookup table. _(javascriptallonge.pdf (source-range-83ecb080-00323))_
- Let’s recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. _(javascriptallonge.pdf (source-range-83ecb080-00323))_
- Sometimes there is a state machine that is naturally represented implicitly in JavaScript’s control flow rather than explicitly in data. _(javascriptallonge.pdf (source-range-83ecb080-00323))_
- But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree. _(javascriptallonge.pdf (source-range-83ecb080-00324))_
- But the first glance is deceptive, because we only see what we’ve seen so far. _(javascriptallonge.pdf (source-range-83ecb080-00325))_
- Let’s see how it would actually work. _(javascriptallonge.pdf (source-range-83ecb080-00325))_
- So far, we have called iterators (and generators) with .next(). _(javascriptallonge.pdf (source-range-83ecb080-00325))_
- If we could do that, a generator function that played naughts and crosses would look like this: _(javascriptallonge.pdf (source-range-83ecb080-00325))_
- But the first glance is deceptive, because we only see what we’ve seen so far. _(javascriptallonge.pdf (source-range-83ecb080-00325))_
- We have looked at generators as ways of making iterators over static collections, where state is modelled implicitly in control flow. _(javascriptallonge.pdf (source-range-83ecb080-00326))_
- If we wanted to pass some state to the generator before it begins, we’d do that with parameters.): aNaughtsAndCrossesGame.next().value _(javascriptallonge.pdf (source-range-83ecb080-00326))_
- But the generator function allows us to maintain state implicitly. _(javascriptallonge.pdf (source-range-83ecb080-00326))_
- It isn’t a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-83ecb080-00326))_
- Again, the salient difference is that an “interactive” generator is stateful, and it embodies its state in its control flow. _(javascriptallonge.pdf (source-range-83ecb080-00326))_
- And sometimes, we want to use implicit state instead of explicitly storing state in our data. _(javascriptallonge.pdf (source-range-83ecb080-00326))_
- We can then get the first move by calling .next(). _(javascriptallonge.pdf (source-range-83ecb080-00326))_
- We can then get the first move by calling .next(). _(javascriptallonge.pdf (source-range-83ecb080-00326))_
- If we wanted to pass some state to the generator before it begins, we’d do that with parameters.): aNaughtsAndCrossesGame.next().value _(javascriptallonge.pdf (source-range-83ecb080-00326))_

## Basic Operations on Iterables

- Here are the operations we’ve defined on Iterables. _(javascriptallonge.pdf (source-range-83ecb080-00328))_

## The Golden Crema: Appendices and Afterwords

## How to run the examples

- At the time this book was written, ECMAScript 2015 was not yet widely available. _(javascriptallonge.pdf (source-range-83ecb080-00335))_
- Traceur and Babel are both _transpilers_ , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics. _(javascriptallonge.pdf (source-range-83ecb080-00335))_
- All of the examples in this book were tested using either Google Traceur Compiler[100] , Babel[101] , or both. _(javascriptallonge.pdf (source-range-83ecb080-00335))_
- Traceur and Babel are both _transpilers_ , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics. _(javascriptallonge.pdf (source-range-83ecb080-00335))_
- Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. _(javascriptallonge.pdf (source-range-83ecb080-00336))_
- The care and feeding of node and npm are beyond the scope of this book, but both tools offer clear instructions for those who have already installed node. _(javascriptallonge.pdf (source-range-83ecb080-00336))_
- So instead of just writing: (() => 2 + 2)() And having 4 displayed, you’d need to write: console.log( (() => 2 + 2)() ) And 4 would appear in your browser’s development console. _(javascriptallonge.pdf (source-range-83ecb080-00336))_
- To see the result of your expressions, you may have to use the console in your web browser. _(javascriptallonge.pdf (source-range-83ecb080-00336))_
- You can also install the transpilers on your development system and use them with Node[102] on the command line[103] . _(javascriptallonge.pdf (source-range-83ecb080-00336))_

## Thanks!

- But where _The Little Schemer’s_ primary focus is recursion, _JavaScript Allongé’s_ primary focus is **functions as first-class values** . _(javascriptallonge.pdf (source-range-83ecb080-00338))_
- _JavaScript Allongé_ was inspired by The Little Schemer[104] by Daniel Friedman and Matthias Felleisen. _(javascriptallonge.pdf (source-range-83ecb080-00338))_
- Richard Feynman’s QED[105] was another inspiration: A book that explains Quantum Electrodynamics and the “Sum of the Histories” methodology using the simple expedient of explaining how light reflects off a mirror, and showing how most of the things we think are happening–such as light travelling on a straight line, the angle of reflection equalling the angle of refraction, or that a beam of light only interacts with a small portion of the mirror, or that it reflects off a plane–are all wrong. _(javascriptallonge.pdf (source-range-83ecb080-00339))_
- Richard Feynman’s QED[105] was another inspiration: A book that explains Quantum Electrodynamics and the “Sum of the Histories” methodology using the simple expedient of explaining how light reflects off a mirror, and showing how most of the things we think are happening–such as light travelling on a straight line, the angle of reflection equalling the angle of refraction, or that a beam of light only interacts with a small portion of the mirror, or that it reflects off a plane–are all wrong. _(javascriptallonge.pdf (source-range-83ecb080-00339))_

## Copyright Notice

## About The Author

- When he’s not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to millions of users, Reg “Raganwald” Braithwaite has authored libraries[221] for JavaScript, CoffeeScript, and Ruby programming such as Allong.es, Method Combinators, Katy, JQuery Combinators, YouAreDaChef, andand, and others. _(javascriptallonge.pdf (source-range-83ecb080-00346))_
- Twitter: @raganwald[224] Email: reg@braythwayt.com[225] **==> picture [206 x 308] intentionally omitted <==** _(javascriptallonge.pdf (source-range-83ecb080-00346))_
- When he’s not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to millions of users, Reg “Raganwald” Braithwaite has authored libraries[221] for JavaScript, CoffeeScript, and Ruby programming such as Allong.es, Method Combinators, Katy, JQuery Combinators, YouAreDaChef, andand, and others. _(javascriptallonge.pdf (source-range-83ecb080-00346))_

## Source review

### Needs review

- |Foreword to the “Six” edition . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00005))_
- |**Recipes with Basic Functions**<br>. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00005))_
- |**Picking the Bean: Choice and Truthiness** . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00005))_
- |**A Rich Aroma: Basic Numbers** . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00005))_
- |**The first sip: Basic Functions** . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00005))_
- |That Constant Coffee Craving<br>. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00005))_
- |**Prelude: Values and Expressions over Coffee**<br>. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00005))_
- |**A Pull of the Lever: Prefaces** . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00005))_
- |Combinators and Function Decorators . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00005))_
- |As Little As Possible About Functions, But No Less . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00005))_
- |Forewords to the First Edition . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00005))_
- |Tail Calls (and Default Arguments) . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00007))_
- |Arrays and Destructuring Arguments<br>. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00007))_
- |**A Warm Cup: Basic Strings and Quasi-Literals**|. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00007))_
- |Basic Operations on Iterables . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00007))_
- |Garbage, Garbage Everywhere . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00007))_
- |Plain Old JavaScript Objects<br>. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00007))_
- |How to run the examples . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00007))_
- |Making Data Out Of Functions . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00007))_
- |**The Golden Crema: Appendices and Afterwords**|. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00007))_
- |Lazy and Eager Collections . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00007))_
- |Tortoises, Hares, and Teleporting Turtles . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00007))_
- |**Composing and Decomposing Data** . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00007))_
- This achieves approximately the same ratio of oils to water as the dilution method, but also releases a different mix of flavours due to the longer extraction. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00010))_
- _JavaScript Allongé_ teaches you how to handle complex code, and it also teaches you how to simplify code without dumbing it down. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00012))_
- _But there’s more to it than that_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- And these techniques dovetail nicely with Allongé’s focus on composing entities and working with functions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- Thus, the “six” edition introduces classes and mixins. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- Thus, the focus on things like writing decorators. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- It introduces iterators and generators. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- It introduces the notion of implementing private properties with symbols. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- We just call some of those functions constructors, others decorators, others functional mixins, and yet others, policies. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00014))_
- From functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so many fruitful directions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00016))_
- _JavaScript Allongé_ introduces new aspects of programming with functions in each chapter, explaining exactly how JavaScript works. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00017))_
- For example: classes and modules. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00020))_
- This upgrade became ECMAScript 5. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00020))_
- - Axel Rauschmayer Blogger[2] , trainer[3] and author of “Exploring ES6[4] ” > 2http://www.2ality.com — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00020))_
- - Completely new features. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00020))_
- For example: Generators, proxies and WeakMaps. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00020))_
- - New functionality in the standard library. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00020))_
- - Better syntax for features that already exist (e.g. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00020))_
- Having written books myself, I know the pain of soliciting and receiving feedback. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00022))_
- A Pull of the Lever: Prefaces x books try to hide most of those capabilities away, giving you recipes for writing JavaScript in a way that approximates class-centric programming in other languages. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00023))_
- Not JavaScript Allongé. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00023))_
- It starts with the fundamentals of values, functions, and objects, and then guides you through JavaScript from the inside with exploratory bits of code that illustrate scoping, combinators, context, state, prototypes, and constructors. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00023))_
- Besides, **there’s really no risk at all** . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00025))_
- ## **Prelude: Values and Expressions over Coffee**

_The following material is extremely basic, however like most stories, the best way to begin is to start at the very beginning._

Imagine we are visiting our favourite coffee shop. They will make for you just about any drink you desire, from a shor — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00028))_
- Let’s hand over some ground coffee plus some boiling water. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- let’s go back to the coffee shop. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- > 10Technically, it’s a _representation_ of a value using Base10 notation, but we needn’t worry about that in this book. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- Say you hand the barista a café Cubano. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00030))_
- And then you’re shown another cup of coffee. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00033))_
- Well, JavaScript’s third and fourth possibilities cover that. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00033))_
- An array looks like this: [1, 2, 3]. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00035))_
- Most programmers never encounter the limit on the magnitude of an integer. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- In a sense, they behave like little functions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00039))_
- A Rich Aroma: Basic Numbers

4

-(457 % 3) _//=> -1_

There are lots and lots more operators that can be used with numbers, including bitwise operators like | and & that allow you to operate directly on a number’s binary representation, and a number of other operators that perform assignment or logi — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00040))_
- Let’s start with the second simplest possible function.[16] In JavaScript, it looks like this: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00044))_
- Let’s call the arguments _args_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00045))_
- Let’s put functions to work. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00045))_
- Let’s try them out and see. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00045))_
- Since we aren’t giving it any arguments, we’ll simply write () after the expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00045))_
- If not… Welcome to the ALGOL family of programming languages! — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00045))_
- It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00047))_
- It evaluates to the same thing, 0. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00047))_
- The first sip: Basic Functions 

12 

You might think that undefined in JavaScript is equivalent to NULL in SQL. No. In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can’t be equal. In JavaScript, every undefined is identical to every other undefine — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00049))_
- Statements belong inside blocks and only inside blocks. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00052))_
- Likewise: () => () => **true** That’s a function, that returns a function, that returns true: (() => () => **true** )()() - _//=> true_ — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00052))_
- Some languages simplify this by making everything an expression, but JavaScript maintains this distinction, so when learning JavaScript we also learn about statements like function declarations, for loops, if statements, and so forth. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00052))_
- We’ll see a few more of these later. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00052))_
- Ah. I'd Like to Have an Argument, Please.
The first sip: Basic Functions 

16 

## **Ah. I’d Like to Have an Argument, Please.**[22] 

Up to now, we’ve looked at functions without arguments. We haven’t even said what an argument _is_ , only that our functions don’t have any. 

Most programmers are p — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00053))_
- And with that, we’re ready to look at _closures_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00054))_
- NaN in JavaScript behaves a lot like NULL in SQL. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00054))_
- Given ( _some function_ )( _some argument_ ), we know that we apply the function to the argument, create an environment, bind the value of the argument to the name, and evaluate the function’s expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00056))_
- Then we’re going to take the value of that function and apply it to the argument 2, something like this: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00056))_
- Up to now, we’ve only seen one way to “bind” a variable, namely by passing in an argument with the same name. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- has a free variable, but the entire expression refers to (x) => ..., and it doesn’t have a free variable: The only variable anywhere in its body is x, which is certainly bound within (x) => .... — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- Let’s fill in the blanks! — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00058))_
- Only you call it with (1)(2)(3) instead of (1, 2, 3). — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00058))_
- JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00059))_
- Create an environment for them, of course. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00060))_
- Sometimes, programmers wish to avoid this. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00060))_
- Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated “IIFE.” — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00063))_
- Every time we invoke the outer function, we’ll invoke the inner function. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00064))_
- Even better, it puts the symbol (like PI) close to the value (3.14159265). — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00065))_
- It doesn’t incur the cost of a function invocation. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00065))_
- Let’s back up and reconsider how closures work. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00068))_
- 31https://en.wikipedia.org/wiki/Scope_(computer_science)#Lexical_scope_vs._dynamic_scope — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00069))_
- And we know that functions create environments. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00070))_
- Let’s start, as above, by doing this with parameters. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00070))_
- We say that when we bind a variable using a parameter inside another binding, the inner binding _shadows_ the outer binding. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00071))_
- That’s why we made all these IIFEs. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00072))_
- Yes, names bound with const shadow enclosing bindings just like parameters. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00072))_
- Being able to bind a name inside of a block means that if the name is only needed in the block, we are not “leaking” its binding to other parts of the code that do not need to interact with it. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00073))_
- The line n = n - 2; _rebinds_ a new value to the name n. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00074))_
- Naming Functions
The first sip: Basic Functions 

39 

## **Naming Functions** 

Let’s get right to it. This code does _not_ name a function: 

**const** repeat = (str) => str + str 

It doesn’t name the function “repeat” for the same reason that const answer = 42 doesn’t name the number 42. This sy — _partial-parse: table parsed as enumerated rows_ _(javascriptallonge.pdf (source-range-83ecb080-00075))_
- Placing a name between the function keyword and the argument list names the function. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00076))_
- 45 As we’ve seen, JavaScript functions take values as arguments and return values. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00082))_
- But before we go on, we’ll talk about some specific types of higher-order functions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00082))_
- Higher-order functions dominate _JavaScript Allongé_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00082))_
- > 36http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20 — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00082))_
- > 38 We’ll see later why an even more useful version would be written (fn) => (...args) => !fn(...args) — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00083))_
- You’ll find lots more perusing the recipes in this book. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00083))_
- You’ll see other function decorators in the recipes, like once and maybe. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00084))_
- When you look at functions within functions in JavaScript, there’s a bit of a “spaghetti code” look to it. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- When a function takes multiple arguments, we “apply” the function to the arguments by evaluating it with all of the arguments, producing a value. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00087))_
- > 43We’ll look at arrays and plain old javascript objects in depth later. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00090))_
- - Expression bodies evaluate to the value of the expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00095))_
- You’ll find examples in Lemonad[45] from Michael Fogus, Functional JavaScript[46] from Oliver Steele and the terse but handy node-ap[47] from James Halliday. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00099))_
- It takes an optional radix argument. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00102))_
- JavaScript’s map actually calls each function with _three_ arguments: The element, the index of the element in the array, and the array itself. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00102))_
- However, that’s not the whole story. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00102))_
- ['1', '2', '3'].map(unary(parseInt)) _//=> [1, 2, 3]_ Presto! — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00103))_
- It takes a value and returns a function that always returns the value, but if you pass it a function, it executes the function for side-effects. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00105))_
- It’s also useful for working with object and instance methods. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00106))_
- **void** 0 : ((done = **true** ), fn.apply( **this** , arguments)) } } Very simple! — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00111))_
- (Note: There are some subtleties with decorators like once that involve the intersection of state with methods. — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00111))_
- You pass it a function, and you get a function back. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00111))_
- It accepts a coach, a captain, and an arbitrary number of players. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00113))_
- ECMAScript 2015 only permits gathering parameters from the _end_ of the parameter list. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00114))_
- Picking the Bean: Choice and Truthiness
## **Picking the Bean: Choice and Truthiness** 

**==> picture [469 x 264] intentionally omitted <==**

**Decaf and the Antidote** 

We’ve seen operators that act on numeric values, like + and %. In addition to numbers, we often need to represent a much more b — _partial-parse: table parsed as enumerated rows_ _(javascriptallonge.pdf (source-range-83ecb080-00118))_
- But that’s not what happens. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00119))_
- and so on and so forth until JavaScript throws up its hands and runs out of stack space. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00119))_
- This leads to the infinite recursion we fear. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00119))_
- It’s best to think of || and && as control-flow operators. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00119))_
- is a logical operator, it always returns true or false. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00120))_
- We saw how to construct an array literal using [, expressions, , and ]. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00126))_
- Some other languages call them first and butFirst, or head and tail. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00127))_
- operation as a “gather,” following Kyle Simpson’s example.[58] Alas, the ... — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00127))_
- to place the elements of an array inside another array. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00128))_
- It acts like destructuring. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00130))_
- And consider how we bind values to parameter names: **const** foo = () => ... — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00130))_
- It _looks_ like destructuring. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00130))_
- We _gather_ the _rest_ of the parameters. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00131))_
- Self-Similarity
Composing and Decomposing Data 

86 

## **Self-Similarity** 

Recursion is the root of computation since it trades description for time.—Alan Perlis, Epigrams in Programming[60] 

In Arrays and Destructuring Arguments, we worked with the basic idea that putting an array together wit — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00132))_
- Armed with our definition of an empty list and with what we’ve already learned, we can build a great many functions that operate on arrays. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00133))_
- But we don’t know the length of rest. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00134))_
- First, we pick what we call a _terminal case_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00134))_
- Composing and Decomposing Data 

89 

Of course, all the students know what to do: They fill the beaker with water, place the stand on the burner and the beaker on the stand, then they turn the burner on and use the sparker to ignite the flame. After a bit the water boils, and they turn off the burn — _partial-parse: table parsed as enumerated rows_ _(javascriptallonge.pdf (source-range-83ecb080-00135))_
- Composing and Decomposing Data 

92 

**const** sumSquares = ([first, ...rest]) => first === **undefined** 

? 0 : first * first + sumSquares(rest); 

sumSquares([1, 2, 3, 4, 5]) _//=> 55_ 

There are two differences between sumSquares and our maps above: 

1. Given the terminal case of an empty lis — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00138))_
- Let’s look at how. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00141))_
- This keeps on happening, so that JavaScript collects the values 1, 2, 3, 4, and 5 plus housekeeping information by the time it calls mapWith((x) => x * x, []). — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00142))_
- The first two don’t return anything, they don’t matter. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00143))_
- But while we’re doing that, it’s annoying to remember to call it with a zero. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00144))_
- This lengthDelaysWork function calls itself in tail position. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00144))_
- We saw earlier that destructuring parameters works the same way as destructuring assignment. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00149))_
- Much slower than the built-in .map method for arrays. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00152))_
- Every time we call mapWith, we’re calling [...prepend, fn(first)]. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00152))_
- Worse, the JavaScript Engine actually copies the elements from prepend into the new array one at a time. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00153))_
- Getting back to JavaScript now, when we write [first, ...rest] to gather or spread arrays, we’re emulating the semantics of car and cdr, but not the implementation. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00156))_
- In Lisp, it’s blazingly fast because it happens in hardware. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00156))_
- 107 **const** node5 = [5, **null** ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; **const** oneToFive = node1; — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00156))_
- In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00157))_
- Composing and Decomposing Data **const** SecretDecoderRing = { encode: **function** encode (plaintext) { **return** plaintext .split('') .map( **char** => **char** .charCodeAt() ) .map( code => code + 1 ) .map( code => String.fromCharCode(code) ) .join(''); }, decode: **function** decode (cyphertext — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00162))_
- Terrible grammar and capitalization, but let’s move on. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00164))_
- Well, let’s start with the simplest possible thing, making a _copy_ of a list. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00165))_
- This isn’t a bad thing by any stretch of the imagination. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00166))_
- Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00167))_
- Their identities stay the same, but not their structure. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00169))_
- Languages like Haskell[70] don’t permit mutation at all. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00171))_
- JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00171))_
- Consider our copy algorithm. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00173))_
- In general, it’s easier to reason about data that doesn’t change. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00173))_
- Armed with this basic copy implementation, we can write mapWith: **const** mapWith = (fn, node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail === **null** ) { **const** { first, rest } = node; **const** newNode = { first: fn(first), rest }; * — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00174))_
- Composing and Decomposing Data

124

_//=> {"first":1,"rest":{"first":0.5,"rest":{"first":0.3333333333333333,"rest":\_ {"first":0.25,"rest":{"first":0.2,"rest":{}}}}}} — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00175))_
- The line n = n - 2; _rebinds_ a new value to the name n. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00177))_
- Let’s take the time to explore what happens with reassigning values to variables. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00178))_
- We took the time to carefully examine what happens with bindings in environments. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00178))_
- It then rebinds the name in that environment. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00179))_
- Some programmers dislike deliberately shadowing variables. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00179))_
- If you buy that argument, the way that shadowing works in JavaScript exists to protect us from accidentally shadowing a variable when we move code around. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00179))_
- Well, parameters bind names. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00180))_
- So that’s five different ways so far. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00180))_
- Named function expressions bind names. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00180))_
- Function declarations bind names. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00180))_
- It’s just different enough to present a source of confusion. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00181))_
- Composing and Decomposing Data

130

JavaScript interprets this code as if we had written: **const** factorial = (n) => { **let** innerFactorial = **function** innerFactorial (x, y) { **if** (x == 1) { **return** y; } **else** { **return** innerFactorial(x-1, x * y); } } **return** innerFactorial(n, — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00182))_
- About 30 seconds later Gauss gave him the answer. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00183))_
- It looks a lot like the for loop in C. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00183))_
- Of course Gauss came up with the answer about 20 times faster than the other kids. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00183))_
- Let’s get fancy! — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00184))_
- That’s not what we want at all. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00185))_
- Now we’re creating a new inner parameter, i and binding it to the value of the outer i. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00186))_
- And therefore, modifications to the parent also modify the child, and modifications to the child also modify the parent. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00189))_
- 137

Composing and Decomposing Data **const** copy = (node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail === **null** ) { **const** { first, rest } = node; **const** newNode = { first, rest }; **return** copy(rest, newNode, newNode); } **els — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00190))_
- So back to the problem of structure sharing. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00191))_
- This strategy of waiting to copy until you are writing is called copy-on-write, or “COW:” — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00192))_
- In case we modify a child list. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00192))_
- I then forgot about it for a while. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00195))_
- I sent him an email sharing my result, to demonstrate my ability to follow through. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00195))_
- 142 } } **const** tortoiseAndHare = (aPair) => { **let** tortoisePair = aPair, harePair = aPair.rest; **while** ( **true** ) { **if** (isEmpty(tortoisePair) || isEmpty(harePair)) { **return false** ; } **if** (tortoisePair.first === harePair.first) { **return true** ; } harePair = harePair.rest; **i — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00196))_
- In Functional Iterators, we’ll investigate one pattern for separating these concerns. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00197))_
- Let’s consider a remarkably simple problem: Finding the sum of the elements of an array. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00199))_
- accumulator : arraySum(rest, first + accumulator) arraySum([1, 4, 9, 16, 25]) _//=> 55_ As we saw earlier, this entangles the mechanism of traversing the array with the business of summing the bits. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00199))_
- Once again, we’re mixing the code for iterating over an array with the code for calculating a sum. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00201))_
- Let’s introduce an idea: A function that takes an iterator and returns another iterator. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00206))_
- We haven’t written anything that finds the first element of an iteration that meets a certain criteria. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00207))_
- So as you traverse the new decorator, you’re changing the state of the original! — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00208))_
- From what we just wrote, K(x)(y) => x So K(I)(x) => I. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00212))_
- Very simple, but useful. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00212))_
- Now we’ll take it one more step forward: Passing a value to K gets a function back, and passing a value to that function gets us a value. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00212))_
- Now, an interesting thing happens when we pass functions to each other. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00212))_
- Given two values, K(I) always returns the _second_ value. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00213))_
- But the first and second we built out of K and I don’t work that way. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00214))_
- You pass the data to these functions, and they extract it. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00214))_
- You call them and pass them the bits, and they choose what to return. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00214))_
- If we change the names to x, y, and z, we get: (x) => (y) => (z) => z(x)(y). — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00215))_
- It’s _exactly backwards_ of the way we write functions that operate on data. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00215))_
- For arrays, we’d write cons = (first, second) => [first, second]. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00215))_
- And instead of passing latin to first or second, we pass first or second to latin. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00215))_
- Without arrays, and without objects, just with functions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00216))_
- We’d better try it out to check. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00216))_
- Armed with nothing more than K, I, and V, we can make a little data structure that holds two values, the cons cell of Lisp and the node of a linked list. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00216))_
- 161

Composing and Decomposing Data **const** length = (aPair) => aPair === EMPTY ? 0 : 1 + length(rest(aPair)); length(l123) _//=> 3_ **const** reverse = (aPair, delayed = EMPTY) => aPair === EMPTY ? delayed : reverse(rest(aPair), pair(first(aPair), delayed)); **const** mapWith = (fn, aPair, delaye — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00217))_
- 163 But without building our way up to something insane like writing a JavaScript interpreter using JavaScript functions and no other data structures, let’s take things another step in a slightly different direction. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00219))_
- Let’s start with the obvious. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00220))_
- Deeply important, but not practical when you’re building a bridge. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- It’s the QED of physics that underpins the Maxwell’s Equations of programming. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- The same thing happens with our lists. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00222))_
- We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00223))_
- - And instead of testing some property of an entity and making a choice of our own with ?: (or if), pass the entity the work we want done for each case and let it test itself. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00223))_
- The line node === EMPTY presumes a lot of things. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00223))_
- This recipe isn’t for map: It’s for mapWith, a function that wraps around map and turns any other function into a mapper. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00228))_
- It also “curries” the function: Instead of taking two arguments, it takes one argument and returns a function that takes another argument. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00228))_
- Map takes a function as an argument, and applies it to each of the elements of the array, then returns the results in another array. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00228))_
- It reverses the arguments, taking the function first and the list second. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00228))_
- It’s the same idea, after all. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00228))_
- Looking at this, we see we’re conflating two separate transformations. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00231))_
- First, we’re reversing the order of arguments. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00231))_
- We’re going to extract these two operations by refactoring our function to paramaterize map. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00231))_
- Recipes with Data

174 **const** flipAndCurry = (fn) => (first) => **function** (second) { **return** fn.call( **this** , second, first); } **const** flip = (fn) => **function** (first, second) { **return** fn.call( **this** , second, first); } **const** flip = (fn) => **function** (first, second) { — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00233))_
- Recipes with Data

175

## **Object.assign**

It’s very common to want to “extend” an object by assigning properties to it: **const** inventory = { apples: 12, oranges: 12 }; inventory.bananas = 54; inventory.pears = 24;

It’s also common to want to assign the properties of one object to another: ** — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00235))_
- 176

Recipes with Data

_//=> { apples: 12, // oranges: 12, // bananas: 54, // pears: 24 }_ And when we discuss prototypes, we will use Object.assign to turn this: **const** Queue = **function** () { **this** .array = []; **this** .head = 0; **this** .tail = -1 }; Queue.prototype.pushTail = **functi — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00236))_
- Recipes with Data

177 }

## });

Assigning properties from one object to another (also called “cloning” or “shallow copying”) is a basic building block that we will later use to implement more advanced paradigms like mixins. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00237))_
- Use it as an excuse to get familiar with your environment’s debugging facility. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- Work things out for yourself! — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- For example, the escape sequence \n inserts a newline character in a string literal, like this: 'first line\nsecond line'. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00242))_
- Quasi-literals go much further. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00242))_
- > 87https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00242))_
- Sometimes you just want to move the box around. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00247))_
- 184 **const** Stack1 = () => ({ array:[], index: -1, push (value) { **return this** .array[ **this** .index += 1] = value; }, pop () { **const** value = **this** .array[ **this** .index]; **this** .array[ **this** .index] = **undefined** ; **if** ( **this** .index >= 0) { **this** .index -= 1 } **re — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00248))_
- Since JavaScript doesn’t bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00249))_
- 191

Served by the Pot: Collections **const** EMPTY = { isEmpty: () => **true** }; **const** isEmpty = (node) => node === EMPTY; **const** Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { **return false** }, [Symbol.iterator] () { **let** currentPair = **this** ; **return** { next () {  — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00255))_
- One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00256))_
- It’s the same idea, after all. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- So we call it a _collection operation_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00260))_
- We invoke mapWith((x) => 2 * x, Numbers) and get Evens. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00260))_
- Every time we write for (const i of Evens), JavaScript calls Evens[Symbol.iterator](). — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00260))_
- Served by the Pot: Collections

197

6 1 ...

mapWith can get a new iterator from RandomNumbers each time we iterate over ZeroesToNines, but if RandomNumbers doesn’t behave like an ordered collection, that’s not mapWith’s fault. RandomNumbers is a _stream_ , not an ordered collection, and thus mapWi — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00261))_
- Let’s consider how they work. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00266))_
- The Numbers iterable returns an object that updates a mutable variable, n, to deliver number after number. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00267))_
- Then it waits for the next request. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00267))_
- Let’s put that beside the code for the iterator, minus the iterable scaffolding: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00267))_
- It waits until given a request, and then it returns exactly one item. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00267))_
- Well, we’ve written our iterator as a _server_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00267))_
- Now for the iteration version. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00268))_
- For example, iterating over a tree. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00268))_
- They’re of approximately equal complexity. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00268))_
- We’ll write a functional iterator to keep things simple, but it’s easy to see the shape of the basic problem: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00268))_
- Let’s revisit the Fibonacci sequence. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00270))_
- > 91We wrote a _generator declaration_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- We don’t return values or output them to console.log. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- We “yield” values using the yield keyword. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- Not a fat arrow. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- We call its .next() method, but it’s done immediately. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- Not a plain function. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- When we invoke the function, we get an iterator object back. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- We declare the function using the function * syntax. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- 208

Served by the Pot: Collections **function** * only (something) { **yield** something; }; only("you").next() _//=>_ {"done": **false** , value: "you"} Invoking only("you") returns an iterator that we can call with .next(), and it yields "you". Invoking only more than once gives us fresh iterator — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00273))_
- 209 

Served by the Pot: Collections 

**const** oneTwoThree = **function** * () { **yield** 1; **yield** 2; **yield** 3; }; 

oneTwoThree().next() _//=>_ {"done": **false** , value: 1} oneTwoThree().next() _//=>_ {"done": **false** , value: 1} oneTwoThree().next() _//=>_ {"done": **false** , value: — _partial-parse: table parsed as enumerated rows_ _(javascriptallonge.pdf (source-range-83ecb080-00274))_
- It’s a function that returns an iterator when we invoke it. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00275))_
- 211 it “suspends” and the producer starts running. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00275))_
- When the producer yields a value, the producer suspends and the consumer starts running, taking the value from the result of calling .next(). — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00275))_
- Served by the Pot: Collections **const** ThreeNumbers = { [Symbol.iterator]: **function** * () { **yield** 1; **yield** 2; **yield** 3 } } **for** ( **const** i **of** ThreeNumbers) { console.log(i); } _//=>_ 1 2 3 [...ThreeNumbers] _//=>_ [1,2,3] **const** iterator = ThreeNumbers[Symbol.iterator]() — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00276))_
- 214 

Served by the Pot: Collections 

8 9 10 ... 

Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state: 

**const** Fibonacci = { [Symbol.iterator]: () => { **let** a = 0, b = 1, state = 0; **return** { next: () => { **s — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00278))_
- Here’s a first crack at a function that returns an iterable object for iterating over trees: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00279))_
- We’ve gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00280))_
- JavaScript handles the recursion for us using its own execution stack. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00281))_
- Tucked inside of it is the same three-line idiom for yielding each element of an iterable. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00282))_
- Over time, this informal “interface” for collections grows by accretion. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00287))_
- But our objects grow fatter and fatter. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00287))_
- Each collection knew how to map itself (.map), how to fold itself (.reduce), how to filter itself (.filter) and how to find one element within itself (.find). — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00287))_
- Served by the Pot: Collections

224 **const** extend = **function** (consumer, ...providers) { **for** ( **let** i = 0; i < providers.length; ++i) { **const** provider = providers[i]; **for** ( **let** key **in** provider) { **if** (provider.hasOwnProperty(key)) { consumer[key] = provider[key] } } } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00288))_
- 225

Served by the Pot: Collections }, filter(fn) { **return** Object.assign({ [Symbol.iterator]: () => { **const** iterator = **this** [Symbol.iterator](); **return** { next: () => { **do** { **const** { done, value } = iterator.next(); } **while** (!done && !fn(value)); **return** { done, value }; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00289))_
- 226

Served by the Pot: Collections }, LazyCollection) }, until(fn) { **return** Object.assign({ [Symbol.iterator]: () => { **const** iterator = **this** [Symbol.iterator](); **return** { next: () => { **let** { done, value } = iterator.next(); done = done || fn(value); **return** ({ done, value: do — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00290))_
- 228

Served by the Pot: Collections }; **const** isEmpty = (node) => node === EMPTY; **const** Pair = (car, cdr = EMPTY) => Object.assign({ car, cdr, isEmpty: () => **false** , [Symbol.iterator]: **function** () { **let** currentPair = **this** ; **return** { next: () => { **if** (currentPair.isEmpt — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00292))_
- Served by the Pot: Collections **return this** .array[ **this** .index += 1] = value; }, pop: **function** () { **const** value = **this** .array[ **this** .index]; **this** .array[ **this** .index] = **undefined** ; **if** ( **this** .index >= 0) { **this** .index -= 1 } **return** value }, isEmpty — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00293))_
- But it’s still illustrative to dissect something important: Array’s .map and .filter methods gather their results into new arrays. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00294))_
- Whereas the .map and .filter methods on Pair work with iterators. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00294))_
- This reduces the memory footprint. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00294))_
- Arrays copy-on-read, so every time we perform a map or filter, we get a new array and perform all the computations. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00296))_
- squaring 28 squaring 29 filtering 0 filtering 1 filtering 4 ... — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00296))_
- Balanced against their flexibility, our “lazy collections” use structure sharing. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00297))_
- Served by the Pot: Collections **const** EagerCollection = (gatherable) => ({ map(fn) { **const** original = **this** ; **return** gatherable.from( ( **function** * () { **for** ( **let** element **of** original) { **yield** fn(element); } })() ); }, reduce(fn, seed) { **let** accumulator = seed; ** — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00298))_
- 235 **const** original = **this** ; **return** gatherable.from( ( **function** * () { **for** ( **let** element **of** original) { **if** (fn(element)) **break** ; **yield** element; } })() ); }, first() { **return this** [Symbol.iterator]().next().value; }, rest() { **const** iteration = **this** [ — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00299))_
- 237

Served by the Pot: Collections {"car": 2, **==> picture [234 x 111] intentionally omitted <==** } } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00301))_
- “Win, win” he thought to himself. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00303))_
- On each square, we randomly place an arrow pointing to one of its four sides. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00304))_
- A player moves the chequer, following the rules. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00304))_
- Consider a finite checkerboard of unknown size. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00304))_
- As the player moves the chequer, they calls out the direction of movement, e.g. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00304))_
- “To save time, we have written a template of the solution for you in ECMASCript 2015 notation. — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00304))_
- Served by the Pot: Collections game-board’s size or contents, only that it is given an arrow every time though the while loop. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00305))_
- “ Christine quickly scribbled on the whiteboard: **const** Game = (size = 8) => { _// initialize the board_ **const** board = []; **for** ( **let** i = 0; i < size; ++i) { board[i] = []; **for** ( **let** j = 0; j < size; ++j) { board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)]; } } _// initialize — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00305))_
- “To begin with, I’ll transform a game into an iterable that generates arrows, using the ‘Starman’ notation for generators. — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00306))_
- “We want to take the arrows and convert them to positions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00307))_
- For that, we’ll map the Game iterable to positions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00307))_
- That’s what we need, because we need to know the current position to map each move to the next position.” “This is a standard idiom we can obtain from libraries, we don’t reinvent the wheel. — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00307))_
- “Having turned our game loop into an iterable, we can now see that our problem of whether the game terminates is isomorphic to the problem of detecting whether the positions given ever repeat themselves: If the chequer ever returns to a position it has previously visited, it will cycle endlessly.” “ — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00308))_
- “There’s an old joke that a mathematician is someone who will take a five-minute problem, then spend an hour proving it is equivalent to another problem they have already solved. — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00309))_
- Use constant space._ ” “This is, of course, the most common solution, it is Floyd’s cycle-finding algorithm[97] , although there is some academic dispute as to whether Robert Floyd actually discovered it or was misattributed by Knuth.” “Thus, the solution to the game problem is:” 97https://en.wikipe — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00310))_
- “This solution makes use of iterables and a single utility function, statefulMapWith. — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00311))_
- Some time later, The Carpenter ran into Bob Plissken at a local technology meet-up. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00311))_
- “ _Well, where has the time gone?_ ” “We at the Thing Software company are very grateful you made some time to visit with us, but alas, that is all the time we have today. — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00311))_
- “I forgot about them, it’s been a while. — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00312))_
- But I couldn’t help but notice that your solution doesn’t actually meet the stated requirements for a different reason:” “The hasCycle function, a/k/a Tortoise and Hare, requires two separate iterators to do its job. — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00313))_
- “You know, the requirement asked for a finite space algorithm, not a constant state algorithm. — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00313))_
- “Kidu, you’re right, that’s a fantastic observation. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00313))_
- “I worked at Thing, and Christine told us about your solution. — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00313))_
- You’re essentially calling for the player to clone themselves and call out the directions in parallel.” The Carpenter thought about this for a moment. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00313))_
- “I guess,” he allowed, “It isn’t always necessary to make a solution so awesome it would please the Ghosts of Mars.” — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00314))_
- Consider, for example, the moves in a game. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00316))_
- To save space, we’ll ignore rotations and reflections, and we’ll model the first player’s moves as a stream. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00316))_
- Let’s consider move 1. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00317))_
- For 2, 4, 5, 7, or 8, we play 3 and win. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00317))_
- If x plays anything else, including 7, we play 4 and win. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00318))_
- If x plays 4, we play 7 and win. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00318))_
- We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00318))_
- Served by the Pot: Collections

255 ]]: 3, [[ 'o', 'x', ' ', ' ', ' ', 'x', 'o', ' ', ' ' ]]: 3, [[ 'o', 'x', ' ', ' ' ' ' ' ' , , , 'o', 'x', ' ' ]]: 3, [[ 'o', 'x', ' ', ' ' ' ' ' ' , , , 'o', ' ', 'x' ]]: 3

_// ..._

};

We get:

{ "o,x, , , , , , , ":6, "o,x,x, , , ,o, , ":3, "o,x, ,x, , ,o, ,  — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00321))_
- _// then we move, and get its next move back_ aNaughtsAndCrossesGame(1) _//=> 6 // then we move, and get its next move back_ aNaughtsAndCrossesGame(4) _//=> 3_ — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00322))_
- Our statelessNaughtsAndCrosses function pushes the work of tracking the game’s state onto us, the player. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00322))_
- We’ve done almost the exact same thing here with our naughts and crosses game. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00323))_
- We aren’t calling our function with moves, it’s calling us. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00324))_
- However, our solution inverts the control. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00324))_
- Served by the Pot: Collections **function** browserNaughtsAndCrosses () { **const** x1 = parseInt(prompt('o plays 0, where does x play?')); **switch** (x1) { **case** 1: **const** x2 = parseInt(prompt('o plays 6, where does x play?')); **switch** (x2) { **case** 2: **case** 4: **case** 5: **case** 7 — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00324))_
- 259 values while maintaining the implicit state of the generator’s control flow. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00325))_
- Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn’t started yet. — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00326))_
- Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn’t call us. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00326))_
- Served by the Pot: Collections **yield** * iterator; } **function** * take (numberToTake, iterable) { **const** iterator = iterable[Symbol.iterator](); **for** ( **let** i = 0; i < numberToTake; ++i) { **const** { done, value } = iterator.next(); **if** (!done) **yield** value; } } **function** * zi — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00329))_
- 263 **const** zip = callFirst(zipWith, (...values) => values); **const** reduceWith = (fn, seed, iterable) => { **let** accumulator = seed; **for** ( **const** element **of** iterable) { accumulator = fn(accumulator, element); } **return** accumulator; }; **const** first = (iterable) => iterable[Sym — _fragmentary: text ends with an unfinished clause_ _(javascriptallonge.pdf (source-range-83ecb080-00330))_
- He writes about programming on “Raganwald[222] ,” as well as general-purpose ruminations on “Braythwayt Dot Com[223] ”. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00346))_

### Disposition counts

- non-claim: 11
