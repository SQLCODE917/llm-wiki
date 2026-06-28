---
page_id: javascriptallonge-bind
page_kind: concept
summary: Bind: 10 statement(s) and 14 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-bind@5b3b53df1de1e401decb0760f6153f90
---

# Bind

What [[javascriptallonge]] covers about bind:

## Statements

- We said that JavaScript binds names to values, but we didn’t say what it means to bind a name to a value. _(javascriptallonge.pdf (source-range-83ecb080-00455))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const. _(javascriptallonge.pdf (source-range-83ecb080-01772))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. _(javascriptallonge.pdf (source-range-83ecb080-01782))_
- In order to bind 3.14159265 to the name PI, we’ll need a function with a parameter of PI applied to an argument of 3.14159265. _(javascriptallonge.pdf (source-range-83ecb080-00548))_
- Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-83ecb080-00642))_
- But instead of binding two different variables to the same name in two different places, we’ll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-83ecb080-00646))_
- Typically, we want to bind our names as close to where we need them as possible. _(javascriptallonge.pdf (source-range-83ecb080-00679))_
- This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous. _(javascriptallonge.pdf (source-range-83ecb080-00696))_
- In that it binds a name in the environment to a named function. _(javascriptallonge.pdf (source-range-83ecb080-00750))_
- JavaScript tries its best to assign things, and if there isn’t something that fits, JavaScript binds undefined to the name. _(javascriptallonge.pdf (source-range-83ecb080-01269))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00548))_

> In order to bind 3.14159265 to the name PI, we’ll need a function with a parameter of PI applied to an argument of 3.14159265. If we put our function expression in parentheses, we can apply it to the argument of 3.14159265:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00549))_

> ((PI) => _// ????_ )(3.14159265)

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00550))_

> What do we put inside our new function that binds 3.14159265 to the name PI when evaluated? Our circumference function, of course:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00551))_

> ((PI) => (diameter) => diameter * PI )(3.14159265)

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00561, source-range-83ecb080-00563))_

> There’s another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. We can turn things inside-out by putting the binding inside our diameter calculating function, like this: It produces the same result as our previous expressions for a diameter-calculating function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00562))_

> (diameter) => ((PI) => diameter * PI)(3.14159265)

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00584, source-range-83ecb080-00588))_

> And we could use it like this: This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our “constant.” That’s more efficient, and it’s _almost_ what we wanted all along: A way to bind 3.14159265 to a readable name.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00587))_

> ((diameter, PI) => diameter * PI)(2, 3.14159265) _//=> 6.2831853_

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00602))_

> We can bind any expression. Functions are expressions, so we can bind helper functions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00604))_

> This underscores what we’ve said: if we have an expression that evaluates to a function, we apply it with ().

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00606))_

> We can bind more than one name-value pair by separating them with commas. For readability, most people put one binding per line:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00607))_

> (d) => { **const** PI = 3.14159265, calc = (diameter) => diameter * PI; **return** "The circumference is " + calc(d) }

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00627, source-range-83ecb080-00632))_

> It’s more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we’ve elided. We can use any expression in there, and that expression can invoke diameter_fn. For example: This is called lexical scoping[31] , because we can discover where a name is bound by looking at the source code for the program. We can see that PI is bound in an environment surrounding (diameter) => diameter * PI, we don’t need to know where dia

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00630))_

> ((diameter_fn) => diameter_fn(2) )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) _//=> 6.2831853_

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00649))_

> And gratuitously wrap it in another IIFE so that we can bind PI to something else:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00652))_

> ((PI) => ((PI) => (diameter) => diameter * PI )(3.14159265) )(3)

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00655, source-range-83ecb080-00657))_

> And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the “outer” environment? Let’s rewrite things slightly differently: Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. Does that binding “overwrite” the outer one? Will our function return 6 or 6.2831853? This is a book, you’ve already scanned ahead, so you know that the

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00656))_

> ((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265)

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00657))_

> Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. Does that binding “overwrite” the outer one? Will our function return 6 or 6.2831853? This is a book, you’ve already scanned ahead, so you know that the answer is **no** , the inner binding does not overwrite the outer binding:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00658))_

> ((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265)(2) _//=> 6.2831853_

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00694, source-range-83ecb080-00696))_

> Let’s get right to it. This code does _not_ name a function: It doesn’t name the function “repeat” for the same reason that const answer = 42 doesn’t name the number 42. This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00695))_

> **const** repeat = (str) => str + str

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00718))_

> Placing a name between the function keyword and the argument list names the function. Confusingly, the name of the function is not exactly the same thing as the name we may choose to bind to the value of the function. For example, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00719))_

> **const double** = **function** repeat (str) { **return** str + str; }

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00751))_

> Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00754))_

> **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> undefined is not a function (evaluating 'fizzbuzz()')_

### Technical atom 14

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01269))_

> That match would fail because the array doesn’t have an element to assign to what. But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn’t something that fits, JavaScript binds undefined to the name. Therefore:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01271))_

> what _//=> undefined_ **const** [which, what, who] = ["duck feet", "tiger tail"]; who _//=> undefined_


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms (1 shared statement(s), 9 shared atom(s))
- [[javascriptallonge-environment]] - shared statements and technical atoms (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms (5 shared atom(s))
- [[javascriptallonge-array]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-program]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-value]] - shared statements (3 shared statement(s))
- [[javascriptallonge-block]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
