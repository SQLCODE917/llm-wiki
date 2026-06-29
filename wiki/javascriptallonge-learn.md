---
page_id: javascriptallonge-learn
page_kind: concept
summary: Learn: 5 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-learn@960c93143f5c317dd25619214662d6c8
---

# Learn

What [[javascriptallonge]] covers about learn:

## Statements

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

- But there's another reason for learning the word antidisestablishmentarianism : We might learn how prefixes and postfixes work in English grammar. It's the same thing with (x) => (y) => x . It has a certain important meaning in its own right, and it's also an excellent excuse to learn about functions that make functions, environments, variables, and more. _(javascriptallonge.pdf (source-range-7239e085-00301))_

### And also: / Closures and Scope / if functions without free variables are pure, are closures impure?

- From this, we learn something: A pure function can contain a closure. _(javascriptallonge.pdf (source-range-7239e085-00349))_

### And also: / That Constant Coffee Craving / const

- JavaScript gives us a way to do that, the const keyword. We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const : _(javascriptallonge.pdf (source-range-7239e085-00420))_

### Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring

- Wesawearlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we create a default destructuring assignment? _(javascriptallonge.pdf (source-range-7239e085-01011))_

### Recipes with Data / Flip / flipping methods

- When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. A small alteration gets the job done: _(javascriptallonge.pdf (source-range-7239e085-01470))_


## Technical atoms

### Technical frame 1: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00422))_

> The const keyword introduces one or more bindings in the block that encloses it. It doesn't incur the cost of a function invocation. That's great. Even better, it puts the symbol (like PI ) close to the value ( 3.14159265 ). That's much better than what we were writing.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00421))_

```
(diameter) => {
const PI = 3.14159265;
return diameter * PI
}
```

### Technical frame 2: Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01013))_

> How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01012))_

```
const [first, second = "two"] = ["one"];
`${first} . ${second}`
//=> "one . two"
const [first, second = "two"] = ["primus", "secundus"];
`${first} . ${second}`
//=> "primus . secundus"
```

### Technical frame 3: Recipes with Data / Flip / flipping methods

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01470))_

> When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. A small alteration gets the job done:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01471))_

```
const flipAndCurry = (fn) =>
(first) =>
function (second) {
return fn.call(this, second, first);
}
const flip = (fn) =>
function (first, second) {
return fn.call(this, second, first);
}
const flip = (fn) =>
function (first, second) {
if (arguments.length === 2) {
return fn.call(this, second, first);
}
else {
return function (second) {
return fn.call(this, second, first);
};
};
};
```


## Related pages

- [[javascriptallonge-default]] - shared statements and technical atoms: Default shares source evidence from Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring: Wesawearlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we creat ... [truncated]; Default shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring: const [first, second = "two"] = ["one"]; `${first} . ${second}` //=> "one . two" const [first, second = "two"] = ["primus", "secundus"]; `${first} . ${second}` //=> ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-important]] - shared statements and technical atoms: Important shares source evidence from And also: / That Constant Coffee Craving / const: JavaScript gives us a way to do that, the const keyword. We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const :; Important shares technical record from And also: / That Constant Coffee Craving / const: (diameter) => { const PI = 3.14159265; return diameter * PI } (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-method]] - shared statements and technical atoms: Method shares source evidence from Recipes with Data / Flip / flipping methods: When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. A small alteration gets the job done:; Method shares technical record from Recipes with Data / Flip / flipping methods: const flipAndCurry = (fn) => (first) => function (second) { return fn.call(this, second, first); } const flip = (fn) => function (first, second) { return fn.call(thi ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-destructuring]] - shared technical atoms: Destructuring shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring: const [first, second = "two"] = ["one"]; `${first} . ${second}` //=> "one . two" const [first, second = "two"] = ["primus", "secundus"]; `${first} . ${second}` //=> ... [truncated] (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from And also: / That Constant Coffee Craving / const: (diameter) => { const PI = 3.14159265; return diameter * PI } (1 shared atom(s))
- [[javascriptallonge-closure]] - shared statements: Closure shares source evidence from And also: / Closures and Scope / if functions without free variables are pure, are closures impure?: From this, we learn something: A pure function can contain a closure. (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from And also: / Closures and Scope / if functions without free variables are pure, are closures impure?: From this, we learn something: A pure function can contain a closure. (1 shared statement(s))

## Source

- [[javascriptallonge]]
