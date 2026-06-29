---
page_id: javascriptallonge-second
page_kind: concept
summary: Second: 9 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-second@5838e178ee6d151a5bb0d1b54edeafe7
---

# Second

What [[javascriptallonge]] covers about second:

## Statements

### Or even: / void

- The first form works but it's cumbersome. The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we'll discuss in Reassignment and Mutation. The third form is guaranteed to always work, so that's what we will use. 20 _(javascriptallonge.pdf (source-range-7239e085-00232))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

- In order to talk about how this works, we should agree on a few terms (you may already know them, but let's check-in together and 'synchronize our dictionaries'). The first x , the one in (x) => ... , is an argument . The y in function (y) ... is another argument. The second x , the one in => x , is not an argument, it's an expression referring to a variable . Arguments and variables work the same way whether we're talking about (x) => (y) => x or just plain (x) => x . _(javascriptallonge.pdf (source-range-7239e085-00302))_

### And also: / Closures and Scope / if functions without free variables are pure, are closures impure?

- The first function doesn't have any variables, therefore doesn't have any free variables. The second doesn't have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ... , and it doesn't have a free variable: The only variable anywhere in its body is x , which is certainly bound within (x) => ... . _(javascriptallonge.pdf (source-range-7239e085-00348))_

### And also: / That Constant Coffee Craving / const

- 30 We're into the second chapter and we've finally named a function. Sheesh. _(javascriptallonge.pdf (source-range-7239e085-00436))_

### And also: / Magic Names / the function keyword

- The first magic name is this , and it is bound to something called the function's context. We will explore this in more detail when we start discussing objects and classes. The second magic name is very interesting, it's called arguments , and the most interesting thing about it is that it contains a list of arguments passed to a function: _(javascriptallonge.pdf (source-range-7239e085-00608))_

### Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

- The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example: _(javascriptallonge.pdf (source-range-7239e085-00773))_

### Yes. Consider this variation: / Making Data Out Of Functions / backwardness

- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. If we represented a pair of values as an array, we'd write them like this: _(javascriptallonge.pdf (source-range-7239e085-01354))_

- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it. _(javascriptallonge.pdf (source-range-7239e085-01358))_

### Like this: / Generating Iterables / state machines

- The second element of the fibonacci sequence is one. _(javascriptallonge.pdf (source-range-7239e085-01648))_


## Technical atoms

### Technical frame 1: Or even: / void

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

### Technical frame 2: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00612))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00609))_

```
const plus = function (a, b) {
return arguments[0] + arguments[1];
}
plus(2,3)
//=> 5
```

### Technical frame 3: Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00775))_

> Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00774))_

```
const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\
den';
```

### Technical frame 4: Yes. Consider this variation: / Making Data Out Of Functions / backwardness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01358))_

> In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01355))_

```
const first = ([first, second]) => first,
second = ([first, second]) => second;
const latin = ["primus", "secundus"];
first(latin)
//=> "primus"
second(latin)
//=> "secundus"
```


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Yes. Consider this variation: / Making Data Out Of Functions / backwardness: Our first and second functions are a little different than what most people are used to when we talk about functions that access data. If we represented a pair of va ... [truncated]; Function shares technical record from And also: / Magic Names / the function keyword: const plus = function (a, b) { return arguments[0] + arguments[1]; } plus(2,3) //=> 5 (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-data]] - shared statements and technical atoms: Data shares source evidence from Yes. Consider this variation: / Making Data Out Of Functions / backwardness: In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it.; Data shares technical record from Yes. Consider this variation: / Making Data Out Of Functions / backwardness: const first = ([first, second]) => first, second = ([first, second]) => second; const latin = ["primus", "secundus"]; first(latin) //=> "primus" second(latin) //=> "secundus" (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example:; Expression shares technical record from Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den'; (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-function-keyword]] - shared statements and technical atoms: the function keyword shares source evidence from And also: / Magic Names / the function keyword: The first magic name is this , and it is bound to something called the function's context. We will explore this in more detail when we start discussing objects and c ... [truncated]; the function keyword shares technical record from And also: / Magic Names / the function keyword: const plus = function (a, b) { return arguments[0] + arguments[1]; } plus(2,3) //=> 5 (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from And also: / Magic Names / the function keyword: const plus = function (a, b) { return arguments[0] + arguments[1]; } plus(2,3) //=> 5 (1 shared atom(s))
- [[javascriptallonge-evaluate]] - shared technical atoms: Evaluate shares technical record from Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den'; (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Or even: / void: void 0 //=> undefined void 1 //=> undefined void (2 + 2) //=> undefined (1 shared atom(s))
- [[javascriptallonge-element]] - shared statements: Element shares source evidence from Like this: / Generating Iterables / state machines: The second element of the fibonacci sequence is one. (1 shared statement(s))
- [[javascriptallonge-variable]] - shared statements: Variable shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: In order to talk about how this works, we should agree on a few terms (you may already know them, but let's check-in together and 'synchronize our dictionaries'). Th ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
