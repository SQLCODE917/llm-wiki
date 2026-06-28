---
page_id: javascriptallonge-section-the-function-keyword-48d2f233
page_kind: source
summary: the function keyword: 34 source-backed entries and 14 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-function-keyword-48d2f233@88f647f4701863b798f2e27c4d8cbfcd
---

# the function keyword

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-function-keyword]] - topic hub: opens the topic page for Function Keyword
- [[javascriptallonge-section-the-function-keyword-a734ba14]] - same source heading: another source section with the same heading, the function keyword

## Statements

- JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-31a4cf47-00506))_
- Something else we're about to discuss is optional. _(javascriptallonge.pdf (source-range-31a4cf47-00513))_
- We have arguments in parentheses, just like fat arrow functions. _(javascriptallonge.pdf (source-range-31a4cf47-00514))_
- We do not have a fat arrow, we go directly to the body. _(javascriptallonge.pdf (source-range-31a4cf47-00515))_
- We always use a block, we cannot write function (str) str + str . This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-31a4cf47-00516))_
- In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment. _(javascriptallonge.pdf (source-range-31a4cf47-00526))_
- 33 'Yes of course?' Well, in chapter of a book dedicated to naming functions, it is not surprising that feature we mention has something to do with naming functions. _(javascriptallonge.pdf (source-range-31a4cf47-00530))_
- Now, the function's actual name has no effect on the environment in which it is used. To whit: _(javascriptallonge.pdf (source-range-31a4cf47-00532))_
- So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const : _(javascriptallonge.pdf (source-range-31a4cf47-00534))_
- Clearly, the name even is bound to the function within the function's body . Is it bound to the function outside of the function's body? _(javascriptallonge.pdf (source-range-31a4cf47-00536))_
- even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't. _(javascriptallonge.pdf (source-range-31a4cf47-00538))_
- This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-31a4cf47-00516))_
- Clearly, the name even is bound to the function within the function's body . _(javascriptallonge.pdf (source-range-31a4cf47-00536))_
- even is bound within the function itself, but not outside it. _(javascriptallonge.pdf (source-range-31a4cf47-00538))_

## Technical atoms

### Technical frame 1: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00513))_

> Something else we're about to discuss is optional.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00508))_

```
(str) => str + str
```

### Technical frame 2: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00513))_

> Something else we're about to discuss is optional.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00510))_

```
function (str) { return str + str }
```

### Technical frame 3: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00516))_

> We always use a block, we cannot write function (str) str + str . This means that if we want our functions to return a value, we always need to use the return keyword

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00517))_

> If we leave out the 'something optional' that comes after the function keyword, we can translate all of the fat arrow functions that we've seen into function keyword functions, e.g.

### Technical frame 4: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00526))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00518))_

```
(n) => (1.618**n - -1.618**-n) / 2.236
```

### Technical frame 5: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00526))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00520))_

```
function (n) { return (1.618**n - -1.618**-n) / 2.236; }
```

### Technical frame 6: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00526))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00523))_

```
const repeat = function repeat (str) { return str + str; }; const fib = function fib (n) { return (1.618**n - -1.618**-n) / 2.236; };
```

### Technical frame 7: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00526))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00524))_

> Placing a name between the function keyword and the argument list names the function. Confusingly, the name of the function is not exactly the same thing as the name we may choose to bind to the value of the function. For example, we can write:

### Technical frame 8: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00526))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00525))_

```
const double = function repeat (str) { return str + str; }
```

### Technical frame 9: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00530))_

> 33 'Yes of course?' Well, in chapter of a book dedicated to naming functions, it is not surprising that feature we mention has something to do with naming functions.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00528))_

```
double .name //=> 'repeat'
```

### Technical frame 10: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00532))_

> Now, the function's actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00531))_

```
someBackboneView.on('click', function clickHandler () { //... });
```

### Technical frame 11: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00534))_

> So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00533))_

```
const bindingName = function actualName () { //... }; bindingName //=> [Function: actualName] actualName //=> ReferenceError: actualName is not defined
```

### Technical frame 12: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00536))_

> Clearly, the name even is bound to the function within the function's body . Is it bound to the function outside of the function's body?

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00535))_

```
( function even (n) { if (n === 0) { return true } else return !even(n - 1) })(5) //=> false ( function even (n) { if (n === 0) { return true } else return !even(n - 1) })(2) //=> true
```

### Technical frame 13: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00538))_

> even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00537))_

```
even //=> Can't find variable: even
```

### Technical atom 14

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00613))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00614))_

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
