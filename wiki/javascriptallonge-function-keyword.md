---
page_id: javascriptallonge-function-keyword
page_kind: concept
summary: the function keyword: 27 statement(s) and 16 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-function-keyword@f8d5a33634ff17c3e3cf608f70612c95
---

# the function keyword

What [[javascriptallonge]] covers about the function keyword:

## Statements

### the function keyword

- JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-8eb13d6b-00506))_

- Something else we're about to discuss is optional. _(javascriptallonge.pdf (source-range-8eb13d6b-00513))_

- We have arguments in parentheses, just like fat arrow functions. _(javascriptallonge.pdf (source-range-8eb13d6b-00514))_

- We do not have a fat arrow, we go directly to the body. _(javascriptallonge.pdf (source-range-8eb13d6b-00515))_

- We always use a block, we cannot write function (str) str + str . This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-8eb13d6b-00516))_

- In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment. _(javascriptallonge.pdf (source-range-8eb13d6b-00526))_

- 33 'Yes of course?' Well, in chapter of a book dedicated to naming functions, it is not surprising that feature we mention has something to do with naming functions. _(javascriptallonge.pdf (source-range-8eb13d6b-00530))_

- Now, the function's actual name has no effect on the environment in which it is used. To whit: _(javascriptallonge.pdf (source-range-8eb13d6b-00532))_

- So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const : _(javascriptallonge.pdf (source-range-8eb13d6b-00534))_

- Clearly, the name even is bound to the function within the function's body . Is it bound to the function outside of the function's body? _(javascriptallonge.pdf (source-range-8eb13d6b-00536))_

- even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't. _(javascriptallonge.pdf (source-range-8eb13d6b-00538))_

- There are two separate rules for these 'magic' names, one for when you invoke a function using the function keyword, and another for functions defined with 'fat arrows.' We'll begin with how things work for functions defined with the function keyword. _(javascriptallonge.pdf (source-range-8eb13d6b-00608))_

- The first magic name is this , and it is bound to something called the function's context. We will explore this in more detail when we start discussing objects and classes. The second magic name is very interesting, it's called arguments , and the most interesting thing about it is that it contains a list of arguments passed to a function: _(javascriptallonge.pdf (source-range-8eb13d6b-00609))_

- arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this: _(javascriptallonge.pdf (source-range-8eb13d6b-00613))_

- The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses. _(javascriptallonge.pdf (source-range-8eb13d6b-00618))_

### magic names and fat arrows

- To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. It uses mapWith , which we discussed in Building Blocks. 44 We'll use arguments just to show the difference between using a fat arrow and the function keyword: _(javascriptallonge.pdf (source-range-8eb13d6b-00626))_

### Functions

- function keyword functions always have blocks as their bodies. _(javascriptallonge.pdf (source-range-8eb13d6b-00643))_

### literal object syntax

- It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords: _(javascriptallonge.pdf (source-range-8eb13d6b-01090))_


## Technical atoms

### Technical frame 1: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00513))_

> Something else we're about to discuss is optional.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00508))_

```
(str) => str + str
```

### Technical frame 2: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00513))_

> Something else we're about to discuss is optional.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00510))_

```
function (str) { return str + str }
```

### Technical frame 3: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00526))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00518))_

```
(n) => (1.618**n - -1.618**-n) / 2.236
```

### Technical frame 4: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00526))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00520))_

```
function (n) { return (1.618**n - -1.618**-n) / 2.236; }
```

### Technical frame 5: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00526))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00523))_

```
const repeat = function repeat (str) { return str + str; }; const fib = function fib (n) { return (1.618**n - -1.618**-n) / 2.236; };
```

### Technical frame 6: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00526))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00525))_

```
const double = function repeat (str) { return str + str; }
```

### Technical frame 7: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00530))_

> 33 'Yes of course?' Well, in chapter of a book dedicated to naming functions, it is not surprising that feature we mention has something to do with naming functions.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00528))_

```
double .name //=> 'repeat'
```

### Technical frame 8: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00532))_

> Now, the function's actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00531))_

```
someBackboneView.on('click', function clickHandler () { //... });
```

### Technical frame 9: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00534))_

> So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const :

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00533))_

```
const bindingName = function actualName () { //... }; bindingName //=> [Function: actualName] actualName //=> ReferenceError: actualName is not defined
```

### Technical frame 10: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00536))_

> Clearly, the name even is bound to the function within the function's body . Is it bound to the function outside of the function's body?

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00535))_

```
( function even (n) { if (n === 0) { return true } else return !even(n - 1) })(5) //=> false ( function even (n) { if (n === 0) { return true } else return !even(n - 1) })(2) //=> true
```

### Technical frame 11: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00538))_

> even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00537))_

```
even //=> Can't find variable: even
```

### Technical frame 12: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00613))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00610))_

```
const plus = function (a, b) { return arguments[0] + arguments[1]; } plus(2,3) //=> 5
```

### Technical frame 13: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00613))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00612))_

```
const args = function (a, b) { return arguments; } args(2,3) //=> { '0': 2, '1': 3 }
```

### Technical frame 14: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00618))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00615))_

```
const plus = function () { return arguments[0] + arguments[1]; } plus(2,3) //=> 5
```

### Technical frame 15: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00618))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00617))_

```
const howMany = function () { return arguments['length']; } howMany() //=> 0 howMany('hello') //=> 1 howMany('sharks', 'are', 'apex', 'predators') //=> 4
```

### Technical atom 16

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00613))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00614))_

| entry | content |
| --- | --- |
| 42 | You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. |
| 43 | We'll look at arrays and plain old javascript objects in depth later. |

<details>
<summary>Raw table text</summary>

```
42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times.
43 We'll look at arrays and plain old javascript objects in depth later.
```

</details>


## Related pages

- [[javascriptallonge-function]] - broader topic: Function shares source evidence from the function keyword: In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, b ... [truncated]; Function shares technical record from the function keyword: (str) => str + str (4 shared statement(s), 11 shared atom(s))
- [[javascriptallonge-argument]] - shared statements and technical atoms: Argument shares source evidence from the function keyword: arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:; Argument shares technical record from the function keyword: const plus = function (a, b) { return arguments[0] + arguments[1]; } plus(2,3) //=> 5 (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-alway]] - shared statements and technical atoms: Alway shares source evidence from the function keyword: We always use a block, we cannot write function (str) str + str . This means that if we want our functions to return a value, we always need to use the return keyword; Alway shares technical record from the function keyword: const args = function (a, b) { return arguments; } args(2,3) //=> { '0': 2, '1': 3 } (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-environment]] - shared statements and technical atoms: Environment shares source evidence from the function keyword: So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines wh ... [truncated]; Environment shares technical record from the function keyword: const bindingName = function actualName () { //... }; bindingName //=> [Function: actualName] actualName //=> ReferenceError: actualName is not defined (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-bound]] - shared statements and technical atoms: Bound shares source evidence from the function keyword: So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines wh ... [truncated]; Bound shares technical record from the function keyword: ( function even (n) { if (n === 0) { return true } else return !even(n - 1) })(5) //=> false ( function even (n) { if (n === 0) { return true } else return !even(n - ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from the function keyword: In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, b ... [truncated]; Expression shares technical record from the function keyword: ( function even (n) { if (n === 0) { return true } else return !even(n - 1) })(5) //=> false ( function even (n) { if (n === 0) { return true } else return !even(n - ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from the function keyword: JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions.; Javascript shares technical record from the function keyword: someBackboneView.on('click', function clickHandler () { //... }); (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-second]] - shared statements and technical atoms: Second shares source evidence from the function keyword: The first magic name is this , and it is bound to something called the function's context. We will explore this in more detail when we start discussing objects and c ... [truncated]; Second shares technical record from the function keyword: const plus = function (a, b) { return arguments[0] + arguments[1]; } plus(2,3) //=> 5 (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-array]] - shared technical atoms: Array shares technical table: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-bind]] - shared technical atoms: Bind shares technical table: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-binding]] - shared technical atoms: Binding shares technical table: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical table: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-ecmascript]] - shared statements: Ecmascript shares source evidence from the function keyword: JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions. (1 shared statement(s))
- [[javascriptallonge-fat-arrow]] - shared statements: Fat Arrow shares source evidence from magic names and fat arrows: To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. It uses mapWith , which we ... [truncated] (1 shared statement(s))
- [[javascriptallonge-section-the-function-keyword-332556f0]] - source section: the function keyword shares source evidence from the function keyword: JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions.; the function keyword shares technical record from the function keyword: (str) => str + str (18 shared statement(s), 12 shared atom(s))
- [[javascriptallonge-section-the-function-keyword-b50ba16e]] - source section: the function keyword shares source evidence from the function keyword: There are two separate rules for these 'magic' names, one for when you invoke a function using the function keyword, and another for functions defined with 'fat arro ... [truncated]; the function keyword shares technical record from the function keyword: const plus = function (a, b) { return arguments[0] + arguments[1]; } plus(2,3) //=> 5 (6 shared statement(s), 5 shared atom(s))

## Source

- [[javascriptallonge]]
