---
page_id: javascriptallonge-partial-application
page_kind: concept
page_family: topic-concept
summary: partial application: 16 statement(s) and 9 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-partial-application@59ea12e2f8ff0a5869cbb1426c4293af
---

# partial application

What [[javascriptallonge]] covers about partial application:

## Statements

### And also: / Closures and Scope / it's always the environment

- The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-7239e085-00366))_

### And also: / Building Blocks / partial application

- Another basic building block is partial application . When a function takes multiple arguments, we 'apply' the function to the arguments by evaluating it with all of the arguments, producing a value. But what if we only supply some of the arguments? In that case, we can't get the final value, but we can get a function that represents part of our application. _(javascriptallonge.pdf (source-range-7239e085-00591))_

- Code is easier than words for this. The Underscore 39 library provides a higher-order function called map . 40 It applies another function to each element of an array, like this: _(javascriptallonge.pdf (source-range-7239e085-00592))_

- The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-7239e085-00597))_

- We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely: _(javascriptallonge.pdf (source-range-7239e085-00599))_

- Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe. _(javascriptallonge.pdf (source-range-7239e085-00603))_

### And also: / Magic Names / the function keyword

- The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses. _(javascriptallonge.pdf (source-range-7239e085-00617))_

### Recipes with Basic Functions / Partial Application

- These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic. _(javascriptallonge.pdf (source-range-7239e085-00660))_

- As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware. We'd need a different recipe if we wish to create partial applications of object methods. _(javascriptallonge.pdf (source-range-7239e085-00662))_

- We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument: _(javascriptallonge.pdf (source-range-7239e085-00665))_

### Composing and Decomposing Data / Tail Calls (and Default Arguments) / factorials

- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-7239e085-00999))_


## Technical atoms

### Technical frame 1: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00597))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00593))_

<a id="atom-technical-atom-d58c104eac1daf94"></a>

```
_.map([1, 2, 3], (n) => n * n)
//=> [1, 4, 9]
```

### Technical frame 2: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00597))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00596))_

<a id="atom-technical-atom-7e2e343bb8d0ba90"></a>

```
const squareAll = (array) => map(array,
(n) => n * n);
```

### Technical frame 3: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00599))_

> We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00598))_

<a id="atom-technical-atom-d427b13c540a373d"></a>

```
const mapWith = (fn) =>
(array) => map(array, fn);
const squareAll = mapWith((n) => n * n);
squareAll([1, 2, 3])
//=> [1, 4, 9]
```

### Technical frame 4: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00603))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00601))_

<a id="atom-technical-atom-330729474fe641db"></a>

```
const safeSquareAll = mapWith(maybe((n) => n * n));
```

### Technical frame 5: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00603))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00602))_

<a id="atom-technical-atom-10a4f14311565237"></a>

```
safeSquareAll([1, null, 2, 3])
//=> [1, null, 4, 9]
```

### Technical frame 6: Recipes with Basic Functions / Partial Application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00662))_

> As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware. We'd need a different recipe if we wish to create partial applications of object methods.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00661))_

<a id="atom-technical-atom-de17f73437abe2ee"></a>

```
const callFirst = (fn, larg) =>
function (...rest) {
return fn.call(this, larg, ...rest);
}
const callLast = (fn, rarg) =>
function (...rest) {
return fn.call(this, ...rest, rarg);
}
const greet = (me, you) =>
`Hello, ${you}, my name is ${me}`;
const heliosSaysHello = callFirst(greet, 'Helios');
heliosSaysHello('Eartha')
//=> 'Hello, Eartha, my name is Helios'
const sayHelloToCeline = callLast(greet, 'Celine');
sayHelloToCeline('Eartha')
//=> 'Hello, Celine, my name is Eartha'
```

### Technical frame 7: Recipes with Basic Functions / Partial Application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00665))_

> We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00666))_

<a id="atom-technical-atom-b54fb52e2a86915d"></a>

```
const callLeft = (fn, ...args) =>
(...remainingArgs) =>
fn(...args, ...remainingArgs);
const callRight = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
```

### Technical atom 8

<a id="atom-technical-atom-5fc857e371a9ac51"></a>

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00660))_

> These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00663))_

```text
45 https://github.com/fogus/lemonad 46 http://osteele.com/sources/javascript/functional/ 47 https://github.com/substack/node-ap 48
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 45 | https://github.com/fogus/lemonad |
| 46 | http://osteele.com/sources/javascript/functional/ |
| 47 | https://github.com/substack/node-ap 48 |

</details>


## Related pages

### Source structure

- [[javascriptallonge-section-and-also-building-blocks-partial-application-a5e51d71]] - source section: And also: / Building Blocks / partial application shares source evidence from And also: / Building Blocks / partial application: Another basic building block is partial application . When a function takes multiple arguments, we 'apply' the function to the arguments by evaluating it with all of ... [truncated]; And also: / Building Blocks / partial application shares technical record from And also: / Building Blocks / partial application: _.map([1, 2, 3], (n) => n * n) //=> [1, 4, 9] (9 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-section-recipes-with-basic-functions-partial-application-583028a8]] - source section: Recipes with Basic Functions / Partial Application shares source evidence from Recipes with Basic Functions / Partial Application: These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want ... [truncated]; Recipes with Basic Functions / Partial Application shares technical record from Recipes with Basic Functions / Partial Application: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (4 shared statement(s), 4 shared atom(s))

### Shared technical atoms

- [[javascriptallonge-argument]] - shared statements and technical atoms: Argument shares source evidence from And also: / Building Blocks / partial application: The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one funct ... [truncated]; Argument shares technical record from And also: / Building Blocks / partial application: _.map([1, 2, 3], (n) => n * n) //=> [1, 4, 9] (2 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from And also: / Building Blocks / partial application: The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one funct ... [truncated]; Function shares technical record from And also: / Building Blocks / partial application: _.map([1, 2, 3], (n) => n * n) //=> [1, 4, 9] (2 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-mapwith]] - shared statements and technical atoms: Mapwith shares source evidence from And also: / Building Blocks / partial application: The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one funct ... [truncated]; Mapwith shares technical record from And also: / Building Blocks / partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-recipe]] - shared statements and technical atoms: Recipe shares source evidence from Recipes with Basic Functions / Partial Application: These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want ... [truncated]; Recipe shares technical record from Recipes with Basic Functions / Partial Application: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-code]] - shared statements and technical atoms: Code shares source evidence from And also: / Building Blocks / partial application: Code is easier than words for this. The Underscore 39 library provides a higher-order function called map . 40 It applies another function to each element of an array, like this:; Code shares technical record from And also: / Building Blocks / partial application: _.map([1, 2, 3], (n) => n * n) //=> [1, 4, 9] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-important]] - shared statements and technical atoms: Important shares source evidence from And also: / Building Blocks / partial application: We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:; Important shares technical record from And also: / Building Blocks / partial application: const safeSquareAll = mapWith(maybe((n) => n * n)); (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-functional]] - shared technical atoms: Functional shares technical table: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (2 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical table: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (2 shared atom(s))

### Shared claims

- [[javascriptallonge-function-keyword]] - shared statements: the function keyword shares source evidence from And also: / Magic Names / the function keyword: The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting o ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
