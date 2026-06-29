---
page_id: javascriptallonge-argument
page_kind: concept
summary: Argument: 14 statement(s) and 30 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-argument@29b316c59249888b2ca9ac652045b5e6
---

# Argument

What [[javascriptallonge]] covers about argument:

## Statements

### And also: / Ah. I'd Like to Have an Argument, Please. 22

- Up to now, we've looked at functions without arguments. We haven't even said what an argument is , only that our functions don't have any. _(javascriptallonge.pdf (source-range-7239e085-00270))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / a quick summary of functions and bodies

- How arguments are used in a body's expression is probably perfectly obvious to you from the examples, especially if you've used any programming language (except for the dialect of BASIC-which I recall from my secondary school-that didn't allow parameters when you called a procedure). _(javascriptallonge.pdf (source-range-7239e085-00286))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

- How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dictionary for each argument. So when we write: _(javascriptallonge.pdf (source-range-7239e085-00305))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing

- 26 Unless the argument is NaN , which isn't equal to anything, including itself . NaN in JavaScript behaves a lot like NULL in SQL. _(javascriptallonge.pdf (source-range-7239e085-00328))_

### And also: / Combinators and Function Decorators / higher-order functions

- As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. _(javascriptallonge.pdf (source-range-7239e085-00557))_

### And also: / Building Blocks / partial application

- The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-7239e085-00597))_

### And also: / Magic Names / the function keyword

- arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this: _(javascriptallonge.pdf (source-range-7239e085-00612))_

### And also: / Magic Names / magic names and fat arrows

- This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind arguments when it's invoked. But if we rewrite row to use the function keyword, it stops working: _(javascriptallonge.pdf (source-range-7239e085-00627))_

### Recipes with Basic Functions / Partial Application

- These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic. _(javascriptallonge.pdf (source-range-7239e085-00660))_

### Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

- Gathering arguments for functions is one of the ways JavaScript can destructure arrays. Another way is when assigning variables, like this: _(javascriptallonge.pdf (source-range-7239e085-00741))_

### Picking the Bean: Choice and Truthiness / truthiness and operators

- Our logical operators ! , && , and || are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-7239e085-00777))_

### Composing and Decomposing Data / Self-Similarity

- In Arrays and Destructuring Arguments, we worked with the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-7239e085-00884))_

### Composing and Decomposing Data / Tail Calls (and Default Arguments) / default arguments

- Now we don't need to use two functions. A default argument is concise and readable. _(javascriptallonge.pdf (source-range-7239e085-01009))_


## Technical atoms

### Technical frame 1: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00274))_

> This function has one argument, room , and an empty body. Here's a function with two arguments and an empty body:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00273))_

```
(room) => {}
```

### Technical frame 2: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00276))_

> I'm sure you are perfectly comfortable with the idea that this function has two arguments, room , and board . What does one do with the arguments? Use them in the body, of course. What do you think this is?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00275))_

```
(room, board) => {}
```

### Technical frame 3: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00278))_

> It's a function for calculating the circumference of a circle given the diameter. I read that aloud as 'When applied to a value representing the diameter, this function returns the diameter times 3.14159265.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00277))_

```
(diameter) => diameter * 3.14159265
```

### Technical frame 4: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00281))_

> You won't be surprised to see how to write and apply a function to two arguments:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00280))_

```
((diameter) => diameter * 3.14159265)(2)
//=> 6.2831853
```

### Technical frame 5: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00281))_

> You won't be surprised to see how to write and apply a function to two arguments:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00283))_

```
((room, board) => room + board)(800, 150)
//=> 950
```

### Technical frame 6: And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00300))_

> (x) => (y) => x just looks crazy, as if we are learning English as a second language and the teacher promises us that soon we will be using words like antidisestablishmentarianism . Besides a desire to use long words to sound impressive, this is not going to seem attractive until we find ourselves wanting to discuss the role of the Church of England in 19th century British politics.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00299))_

```
(x) => (y) => x
```

### Technical frame 7: And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00314))_

> The value '2' is bound to the name 'x' in the environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00306))_

```
((x) => x)(2)
//=> 2
```

### Technical frame 8: And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00328))_

> 26 Unless the argument is NaN , which isn't equal to anything, including itself . NaN in JavaScript behaves a lot like NULL in SQL.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00327))_

```
(value) =>
((ref1, ref2) => ref1 === ref2)(value, value)
```

### Technical frame 9: And also: / Combinators and Function Decorators / higher-order functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00557))_

> As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00559))_

```
const repeat = (num, fn) =>
(num > 0)
? (repeat(num - 1, fn), fn(num))
: undefined
repeat(3, function (n) {
console.log(`Hello ${n}`)
})
//=>
'Hello 1'
'Hello 2'
'Hello 3'
undefined
```

### Technical frame 10: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00597))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00593))_

```
_.map([1, 2, 3], (n) => n * n)
//=> [1, 4, 9]
```

### Technical frame 11: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00597))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00596))_

```
const squareAll = (array) => map(array,
(n) => n * n);
```

### Technical frame 12: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00599))_

> We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00598))_

```
const mapWith = (fn) =>
(array) => map(array, fn);
const squareAll = mapWith((n) => n * n);
squareAll([1, 2, 3])
//=> [1, 4, 9]
```

### Technical frame 13: And also: / Magic Names / the function keyword

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

### Technical frame 14: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00612))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00611))_

```
const args = function (a, b) {
return arguments;
}
args(2,3)
//=> { '0': 2, '1': 3 }
```

### Technical frame 15: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00617))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00614))_

```
const plus = function () {
return arguments[0] + arguments[1];
}
plus(2,3)
//=> 5
```

### Technical frame 16: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00617))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00616))_

```
const howMany = function () {
return arguments['length'];
}
howMany()
//=> 0
howMany('hello')
//=> 1
howMany('sharks', 'are', 'apex', 'predators')
//=> 4
```

### Technical frame 17: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00622))_

> But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function . And thus arguments[0] will refer to "outer" , not to "inner" :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00621))_

```
(function () {
return (function () { return arguments[0]; })('inner');
})('outer')
//=> "inner"
```

### Technical frame 18: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00624))_

> Although it seems quixotic for the two syntaxes to have different semantics, it makes sense when you consider the design goal: Fat arrow functions are designed to be very lightweight and are often used with constructs like mapping or callbacks to emulate syntax.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00623))_

```
(function () {
return (() => arguments[0])('inner');
})('outer')
//=> "outer"
```

### Technical frame 19: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00627))_

> This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind arguments when it's invoked. But if we rewrite row to use the function keyword, it stops working:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00626))_

```
const row = function () {
return mapWith(
(column) => column * arguments[0],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
)
}
row(3)
//=> [3,6,9,12,15,18,21,24,27,30,33,36]
```

### Technical frame 20: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00631))_

> Although this example is clearly unrealistic, there is a general design principle that deserves attention. Sometimes, a function is meant to be used as a Big-F function. It has a name, it is called by different pieces of code, it's a first-class entity in the code.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00629))_

```
const row = function () {
return mapWith(
function (column) { return column * arguments[0] },
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
)
}
row(3)
//=> [1,4,9,16,25,36,49,64,81,100,121,144]
```

### Technical frame 21: Recipes with Basic Functions / Partial Application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00662))_

> As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware. We'd need a different recipe if we wish to create partial applications of object methods.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00661))_

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

### Technical frame 22: Recipes with Basic Functions / Partial Application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00665))_

> We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00666))_

```
const callLeft = (fn, ...args) =>
(...remainingArgs) =>
fn(...args, ...remainingArgs);
const callRight = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
```

### Technical frame 23: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00747))_

> But we can write our own left-gathering function utility using the same principles without all the tedium:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00742))_

```
const [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid'];
first
//=> 'why'
butFirst
//=> ["hello","there","little","droid"]
```

### Technical frame 24: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00749))_

> With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00748))_

```
const leftGather = (outputArrayLength) => {
return function (inputArray) {
return [inputArray.slice(0, inputArray.length - outputArrayLength + 1)].conc\
at(
inputArray.slice(inputArray.length - outputArrayLength + 1)
)
}
};
const [butLast, last] = leftGather(2)(['why', 'hello', 'there', 'little', 'droid\
']);
butLast
//=> ['why', 'hello', 'there', 'little']
last
//=> 'droid'
```

### Technical frame 25: Picking the Bean: Choice and Truthiness / truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00779))_

> Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00778))_

```
!5
//=> false
!undefined
//=> true
```

### Technical frame 26: Composing and Decomposing Data / Tail Calls (and Default Arguments) / default arguments

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01009))_

> Now we don't need to use two functions. A default argument is concise and readable.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01006))_

```
const factorial = (n, work = 1) =>
n === 1
? work
: factorial(n - 1, n * work);
factorial(1)
//=> 1
factorial(6)
//=> 720
```

### Technical atom 27

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00236))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00234))_

| entry | content |
| --- | --- |
| 19 | Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This was actually the preferred mechanism until void became commonplace. |
| 20 | As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined . We have no idea. |

<details>
<summary>Raw table text</summary>

```
back on the block
Back to our function. We evaluated this:
19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This was actually the preferred mechanism until void became commonplace.
20 As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined . We have no idea.
```

</details>

### Technical atom 28

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00562))_

| entry | content |
| --- | --- |
| 35 | https://en.wikipedia.org/wiki/Combinatory_logic |
| 36 | http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20 |

<details>
<summary>Raw table text</summary>

```
combinators
The word 'combinator' has a precise technical meaning in mathematics:
'A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.'-Wikipedia 35
If we were learning Combinatorial Logic, we'd start with the most basic combinators like S , K , and I , and work up from there to practical combinators. We'd learn that the fundamental combinators are named after birds following the example of Raymond Smullyan's famous book To Mock a Mockingbird 36 .
35 https://en.wikipedia.org/wiki/Combinatory_logic
36 http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20
```

</details>

### Technical atom 29

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00570))_

| entry | content |
| --- | --- |
| 37 | As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. |
| 38 | We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args) |

<details>
<summary>Raw table text</summary>

```
function decorators
A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. Here's a ridiculously simple decorator: 38
37 As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context.
38 We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args)
```

</details>

### Technical atom 30

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00856))_

> Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00857))_

| entry | content |
| --- | --- |
| 57 | https://en.wikipedia.org/wiki/CAR_and_CDR |
| 58 | Kyle Simpson is the author of You Don't Know JS, available here |

<details>
<summary>Raw table text</summary>

```
57 https://en.wikipedia.org/wiki/CAR_and_CDR
58 Kyle Simpson is the author of You Don't Know JS, available here
```

</details>


## Related pages

- [[javascriptallonge-works-just-fine-because-arguments]] - narrower topic: Works Just Fine, Because Arguments[0 shares source evidence from And also: / Magic Names / magic names and fat arrows: This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind ar ... [truncated]; Works Just Fine, Because Arguments[0 shares technical table: back on the block Back to our function. We evaluated this: 19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This ... [truncated] (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dicti ... [truncated]; Function shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22: (room) => {} (4 shared statement(s), 24 shared atom(s))
- [[javascriptallonge-partial-application]] - shared statements and technical atoms: partial application shares source evidence from And also: / Building Blocks / partial application: The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one funct ... [truncated]; partial application shares technical record from And also: / Building Blocks / partial application: _.map([1, 2, 3], (n) => n * n) //=> [1, 4, 9] (2 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-function-keyword]] - shared statements and technical atoms: the function keyword shares source evidence from And also: / Magic Names / the function keyword: arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:; the function keyword shares technical record from And also: / Magic Names / the function keyword: const plus = function (a, b) { return arguments[0] + arguments[1]; } plus(2,3) //=> 5 (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from And also: / Combinators and Function Decorators / higher-order functions: As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as argume ... [truncated]; Return shares technical record from And also: / Building Blocks / partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (3 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-alway]] - shared statements and technical atoms: Alway shares source evidence from And also: / Magic Names / the function keyword: arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:; Alway shares technical record from And also: / Magic Names / the function keyword: const args = function (a, b) { return arguments; } args(2,3) //=> { '0': 2, '1': 3 } (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-gathering]] - shared statements and technical atoms: Gathering shares source evidence from Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring: Gathering arguments for functions is one of the ways JavaScript can destructure arrays. Another way is when assigning variables, like this:; Gathering shares technical record from Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring: const [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid']; first //=> 'why' butFirst //=> ["hello","there","little","droid"] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-bind]] - shared statements and technical atoms: Bind shares source evidence from Recipes with Basic Functions / Partial Application: These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want ... [truncated]; Bind shares technical record from Recipes with Basic Functions / Partial Application: const callFirst = (fn, larg) => function (...rest) { return fn.call(this, larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call(this, ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from Recipes with Basic Functions / Partial Application: These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want ... [truncated]; List shares technical record from Recipes with Basic Functions / Partial Application: const callFirst = (fn, larg) => function (...rest) { return fn.call(this, larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call(this, ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-mapwith]] - shared statements and technical atoms: Mapwith shares source evidence from And also: / Building Blocks / partial application: The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one funct ... [truncated]; Mapwith shares technical record from And also: / Building Blocks / partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring: const [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid']; first //=> 'why' butFirst //=> ["hello","there","little","droid"] (4 shared atom(s))
- [[javascriptallonge-code]] - shared technical atoms: Code shares technical record from And also: / Building Blocks / partial application: _.map([1, 2, 3], (n) => n * n) //=> [1, 4, 9] (2 shared atom(s))
- [[javascriptallonge-fat-arrow]] - shared technical atoms: Fat Arrow shares technical record from And also: / Magic Names / magic names and fat arrows: (function () { return (() => arguments[0])('inner'); })('outer') //=> "outer" (2 shared atom(s))
- [[javascriptallonge-program]] - shared technical atoms: Program shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (2 shared atom(s))
- [[javascriptallonge-programmer]] - shared technical atoms: Programmer shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (2 shared atom(s))
- [[javascriptallonge-purpose]] - shared technical atoms: Purpose shares technical record from And also: / Magic Names / magic names and fat arrows: const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36 ... [truncated] (2 shared atom(s))
- [[javascriptallonge-result]] - shared technical atoms: Result shares technical record from And also: / Building Blocks / partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (2 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: ((x) => x)(2) //=> 2 (2 shared atom(s))
- [[javascriptallonge-behaviour]] - shared technical atoms: Behaviour shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-block]] - shared technical atoms: Block shares technical table: back on the block Back to our function. We evaluated this: 19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This ... [truncated] (1 shared atom(s))
- [[javascriptallonge-data]] - shared technical atoms: Data shares technical table: 57 https://en.wikipedia.org/wiki/CAR_and_CDR 58 Kyle Simpson is the author of You Don't Know JS, available here (1 shared atom(s))
- [[javascriptallonge-discussing]] - shared technical atoms: Discussing shares technical record from And also: / Magic Names / magic names and fat arrows: const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36 ... [truncated] (1 shared atom(s))
- [[javascriptallonge-environment]] - shared technical atoms: Environment shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: ((x) => x)(2) //=> 2 (1 shared atom(s))
- [[javascriptallonge-evaluate]] - shared technical atoms: Evaluate shares technical table: back on the block Back to our function. We evaluated this: 19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This ... [truncated] (1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from And also: / Magic Names / magic names and fat arrows: (function () { return (function () { return arguments[0]; })('inner'); })('outer') //=> "inner" (1 shared atom(s))
- [[javascriptallonge-idea]] - shared technical atoms: Idea shares technical record from And also: / Magic Names / magic names and fat arrows: const row = function () { return mapWith( function (column) { return column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [1,4,9,16,25,36 ... [truncated] (1 shared atom(s))
- [[javascriptallonge-language]] - shared technical atoms: Language shares technical table: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))
- [[javascriptallonge-parameter]] - shared technical atoms: Parameter shares technical record from Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring: const leftGather = (outputArrayLength) => { return function (inputArray) { return [inputArray.slice(0, inputArray.length - outputArrayLength + 1)].conc\ at( inputArr ... [truncated] (1 shared atom(s))
- [[javascriptallonge-recipe]] - shared technical atoms: Recipe shares technical record from Recipes with Basic Functions / Partial Application: const callFirst = (fn, larg) => function (...rest) { return fn.call(this, larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call(this, ... [truncated] (1 shared atom(s))
- [[javascriptallonge-reference]] - shared technical atoms: Reference shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: (value) => ((ref1, ref2) => ref1 === ref2)(value, value) (1 shared atom(s))
- [[javascriptallonge-second]] - shared technical atoms: Second shares technical record from And also: / Magic Names / the function keyword: const plus = function (a, b) { return arguments[0] + arguments[1]; } plus(2,3) //=> 5 (1 shared atom(s))
- [[javascriptallonge-type]] - shared technical atoms: Type shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: (value) => ((ref1, ref2) => ref1 === ref2)(value, value) (1 shared atom(s))

## Source

- [[javascriptallonge]]
