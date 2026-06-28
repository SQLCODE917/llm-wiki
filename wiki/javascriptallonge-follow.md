---
page_id: javascriptallonge-follow
page_kind: concept
summary: Follow: 8 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-follow@c9faeca524192ee06ddc1a78b6246203
---

# Follow

What [[javascriptallonge]] covers about follow:

## Statements

### how this book is organized

- Following some of the chapters are a series of recipes designed to show the application of the chapter's ideas in practical form. While the content of each chapter builds naturally on what was discussed in the previous chapter, the recipes may draw upon any aspect of the JavaScript programming language. _(javascriptallonge.pdf (source-range-31a4cf47-00067))_

### michael fogus

- As a life-long bibliophile and long-time follower of Reg's online work, I was excited when he started writing books. However, I'm very conservative about books - let's just say that if there was an aftershave scented to the essence of 'Used Book Store' then I would be first in line to buy. So as you might imagine I was 'skeptical' about the decision to release JavaScript Allongé as an ongoing ebook, with a pay-what-you-want model. However, Reg sent me a copy of his book and I was humbled. Not only was this a great book, but it was also a great way to write and distribute books. Having written books myself, I know the pain of soliciting and receiving feedback. _(javascriptallonge.pdf (source-range-31a4cf47-00084))_

### void

- 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

### function declaration caveats 34

- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-31a4cf47-00551))_

### mutation and data structures

- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists from Plain Old JavaScript Objects. While we're executing the mapWith function, we're constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith . _(javascriptallonge.pdf (source-range-31a4cf47-01143))_

### copy-on-write

- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-31a4cf47-01255))_

### say 'please'

- Wekeep using the same pattern in our functions: aPair === EMPTY ? doSomething : doSomethingElse . This follows the philosophy we used with data structures: The function doing the work inspects the data structure. _(javascriptallonge.pdf (source-range-31a4cf47-01389))_


## Technical atoms

### Technical frame 1: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00250))_

```
(() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined
```

### Technical frame 2: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00251))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00103))_

| entry | content |
| --- | --- |
| 8 | https://en.wikipedia.org/wiki/Expression_ |
| 9 | https://en.wikipedia.org/wiki/Value_ |

<details>
<summary>Raw table text</summary>

```
Prelude: Values and Expressions over Coffee
The following material is extremely basic, however like most stories, the best way to begin is to start at the very beginning.
Imagine we are visiting our favourite coffee shop. They will make for you just about any drink you desire, from a short, intense espresso ristretto through a dry cappuccino, up to those coffee-flavoured desert concoctions featuring various concentrated syrups and milks. (You tolerate the existence of sugary drinks because they provide a sufficient profit margin to the establishment to finance your hanging out there all day using their WiFi and ordering a $3 drink every few hours.)
You express your order at one end of their counter, the folks behind the counter perform their magic, and deliver the coffee you value at the other end. This is exactly how the JavaScript environment works for the purpose of this book. We are going to dispense with web servers, browsers and other complexities and deal with this simple model: You give the computer an expression 8 , and it returns a value 9 , just as you express your wishes to a barista and receive a coffee in return.
8 https://en.wikipedia.org/wiki/Expression_
9 https://en.wikipedia.org/wiki/Value_
```

</details>


## Related pages

- [[javascriptallonge-code]] - shared statements and technical atoms: Code shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Code shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Javascript shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-rule]] - shared statements and technical atoms: Rule shares source evidence from void: 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basical ... [truncated]; Rule shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-write]] - shared statements and technical atoms: Write shares source evidence from copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated]; Write shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated]; Function shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (2 shared atom(s))
- [[javascriptallonge-feature]] - shared technical atoms: Feature shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared atom(s))
- [[javascriptallonge-language]] - shared technical atoms: Language shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared atom(s))
- [[javascriptallonge-program]] - shared technical atoms: Program shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared atom(s))
- [[javascriptallonge-programmer]] - shared technical atoms: Programmer shares technical record from void: (() => 2 + 2)() //=> 4 (() => { 2 + 2 })() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared atom(s))
- [[javascriptallonge-coffee]] - shared technical atoms: Coffee shares technical table: Prelude: Values and Expressions over Coffee The following material is extremely basic, however like most stories, the best way to begin is to start at the very begin ... [truncated] (1 shared atom(s))
- [[javascriptallonge-evaluating]] - shared technical atoms: Evaluating shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-result]] - shared technical atoms: Result shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical table: Prelude: Values and Expressions over Coffee The following material is extremely basic, however like most stories, the best way to begin is to start at the very begin ... [truncated] (1 shared atom(s))
- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from mutation and data structures: One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists f ... [truncated] (2 shared statement(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-copy-write]] - shared statements: Copy on Write shares source evidence from copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-environment]] - shared statements: Environment shares source evidence from function declaration caveats 34: Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the fol ... [truncated] (1 shared statement(s))
- [[javascriptallonge-mutation]] - shared statements: Mutation shares source evidence from mutation and data structures: One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists f ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
