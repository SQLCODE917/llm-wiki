---
page_id: javascriptallonge-coffee
page_kind: concept
summary: Coffee: 6 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-coffee@14a6d0dcf7e31cc235a920116e5cb5d4
---

# Coffee

What [[javascriptallonge]] covers about coffee:

## Statements

### values are expressions

- xiv

Prelude: Values and Expressions over Coffee

## **values are expressions**

All values are expressions. Say you hand the barista a café Cubano. Yup, you hand over a cup with some coffee infused through partially caramelized sugar. You say, “I want one of these.” The barista is no fool, she gives it straight back to you, and you get exactly what you want. Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista).

Let’s try this with something the computer understands easily:

## 42

Is this an expression? A value? Neither? Or both?

The answer is, this is both an expression _and_ a value.[10] The way you can tell that it’s both is very easy: When you type it into JavaScript, you get the same thing back, just like our café Cubano:

## 42

_//=> 42_

All values are expressions. That’s easy! Are there any other kinds of expressions? Sure! let’s go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let’s hand over some ground coffee plus some boiling water.

Astute readers will realize we’re omitting something. Congratulations! Take a sip of espresso. We’ll get to that in a moment.

Now the barista gives us back an espresso. And if we hand over the espresso, we get the espresso right back. So, boiling water plus ground coffee is an expression, but it isn’t a value.[11] Boiling water is a value. Ground coffee is a value. Espresso is a value. Boiling water plus ground coffee is an expression.

Let’s try this as well with something else the computer understands easily:

> "JavaScript" + " " + "Allonge"

> _//=> "JavaScript Allonge"_

> 10Technically, it’s a _representation_ of a value using Base10 notation, but we needn’t worry about that in this book. You and I both understand that this means “42,” and so does the computer.

> 11In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values. _(javascriptallonge.pdf (source-range-83ecb080-00030))_

- xv

Prelude: Values and Expressions over Coffee

Now we see that “strings” are values, and you can make an expression out of strings and an operator +. Since strings are values, they are also expressions by themselves. But strings with operators are not values, they are expressions. Now we know what was missing with our “coffee grounds plus hot water” example. The coffee grounds were a value, the boiling hot water was a value, and the “plus” operator between them made the whole thing an expression that was not a value. _(javascriptallonge.pdf (source-range-83ecb080-00031))_

### About The Author

- The Golden Crema: Appendices and Afterwords

274

## **About The Author**

When he’s not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to millions of users, Reg “Raganwald” Braithwaite has authored libraries[221] for JavaScript, CoffeeScript, and Ruby programming such as Allong.es, Method Combinators, Katy, JQuery Combinators, YouAreDaChef, andand, and others.

He writes about programming on “Raganwald[222] ,” as well as general-purpose ruminations on “Braythwayt Dot Com[223] ”.

## **contact**

Twitter: @raganwald[224] Email: reg@braythwayt.com[225] **==> picture [206 x 308] intentionally omitted <==**

**Reg “Raganwald” Braithwaite**

> 221http://github.com/raganwald

> 222http://raganwald

> 223http://braythwayt.com

> 224https://twitter.com/raganwald

> 225mailto:reg@braythwayt.com _(javascriptallonge.pdf (source-range-83ecb080-00346))_


## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00076))_

> 40 The first sip: Basic Functions **function** (n) { **return** (1.618**n - -1.618**-n) / 2.236; } This still does not _name_ a function, but as we noted above, functions written with the function keyword have an optional “something else.” Could that “something else” name a function? Yes, of course.[33] Here are our example functions written with names: **const** repeat = **function** repeat (str) { **return** str + str; }; **const** fib = **function** fib (n) { **return** (1.618**n - -1.618**-n

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00075))_

| entry | content |
| --- | --- |
| 1 | We introduce a function with the function keyword. |
| 2 | Something else we’re about to discuss is optional. |
| 3 | We have arguments in parentheses, just like fat arrow functions. |
| 4 | We do not have a fat arrow, we go directly to the body. |
| 5 | We always use a block, we cannot write function (str) str + str. This means that if we want our functions to return a value, we always need to use the return keyword If we leave out the “something optional” that comes after the function keyword, we can translate all of the fat arrow functions that we’ve seen into function keyword functions, e.g. |

<details>
<summary>Raw table text</summary>

```
Naming Functions
The first sip: Basic Functions 

39 

## **Naming Functions** 

Let’s get right to it. This code does _not_ name a function: 

**const** repeat = (str) => str + str 

It doesn’t name the function “repeat” for the same reason that const answer = 42 doesn’t name the number 42. This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous. 

## **the function keyword** 

JavaScript _does_ have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions. 

Here’s our repeat function written using a “fat arrow” 

(str) => str + str 

And here’s (almost) the exact same function written using the function keyword: 

**function** (str) { **return** str + str } 

Let’s look at the obvious differences: 

1. We introduce a function with the function keyword. 

2. Something else we’re about to discuss is optional. 

3. We have arguments in parentheses, just like fat arrow functions. 

4. We do not have a fat arrow, we go directly to the body. 

5. We always use a block, we cannot write function (str) str + str. This means that if we want our functions to return a value, we always need to use the return keyword 

If we leave out the “something optional” that comes after the function keyword, we can translate all of the fat arrow functions that we’ve seen into function keyword functions, e.g. 

(n) => (1.618**n - -1.618**-n) / 2.236 

Can be written as:
```

</details>


## Related pages

- [[javascriptallonge-const]] - shared technical atoms: Const shares technical table: Naming Functions The first sip: Basic Functions  39  ## **Naming Functions**  Let’s get right to it. This code does _not_ name a function:  **const** repeat = (str) ... [truncated] (1 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical table: Naming Functions The first sip: Basic Functions  39  ## **Naming Functions**  Let’s get right to it. This code does _not_ name a function:  **const** repeat = (str) ... [truncated] (1 shared atom(s))
- [[javascriptallonge-ground]] - shared statements: Ground shares source evidence from values are expressions: xiv  Prelude: Values and Expressions over Coffee  ## **values are expressions**  All values are expressions. Say you hand the barista a café Cubano. Yup, you hand ov ... [truncated] (4 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from About The Author: The Golden Crema: Appendices and Afterwords  274  ## **About The Author**  When he’s not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
