---
page_id: javascriptallonge-argument
page_kind: concept
page_family: broad-topic
summary: Argument: 13 statement(s) and 26 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-argument@683f4d8fcb114cc49428356f004afae3
---

# Argument

What [[javascriptallonge]] covers about argument:


## Related pages

### Shared technical atoms

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dicti ... [truncated]; Function shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22: (room) => {} (4 shared statement(s), 21 shared atom(s))
- [[javascriptallonge-partial-application]] - shared statements and technical atoms: partial application shares source evidence from And also: / Building Blocks / partial application: The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one funct ... [truncated]; partial application shares technical record from And also: / Building Blocks / partial application: _.map([1, 2, 3], (n) => n * n) //=> [1, 4, 9] (2 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from And also: / Combinators and Function Decorators / higher-order functions: As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as argume ... [truncated]; Return shares technical record from And also: / Building Blocks / partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (3 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring: const [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid']; first //=> 'why' butFirst //=> ["hello","there","little","droid"] (4 shared atom(s))
- [[javascriptallonge-gathering]] - shared statements and technical atoms: Gathering shares source evidence from Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring: Gathering arguments for functions is one of the ways JavaScript can destructure arrays. Another way is when assigning variables, like this:; Gathering shares technical record from Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring: const [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid']; first //=> 'why' butFirst //=> ["hello","there","little","droid"] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-code]] - shared technical atoms: Code shares technical record from And also: / Building Blocks / partial application: _.map([1, 2, 3], (n) => n * n) //=> [1, 4, 9] (2 shared atom(s))
- [[javascriptallonge-fat-arrow]] - shared technical atoms: Fat Arrow shares technical record from And also: / Magic Names / magic names and fat arrows: (function () { return (() => arguments[0])('inner'); })('outer') //=> "outer" (2 shared atom(s))
- [[javascriptallonge-programmer]] - shared technical atoms: Programmer shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (2 shared atom(s))
## Statements by source section

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

<a id="atom-technical-atom-6a7b1c7102f82932"></a>

```
(room) => {}
```

### Technical frame 2: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00276))_

> I'm sure you are perfectly comfortable with the idea that this function has two arguments, room , and board . What does one do with the arguments? Use them in the body, of course. What do you think this is?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00275))_

<a id="atom-technical-atom-e3d6fc001ce32d0d"></a>

```
(room, board) => {}
```

### Technical frame 3: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00278))_

> It's a function for calculating the circumference of a circle given the diameter. I read that aloud as 'When applied to a value representing the diameter, this function returns the diameter times 3.14159265.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00277))_

<a id="atom-technical-atom-8b0b88078e233caf"></a>

```
(diameter) => diameter * 3.14159265
```

### Technical frame 4: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00281))_

> You won't be surprised to see how to write and apply a function to two arguments:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00280))_

<a id="atom-technical-atom-8b01b9d30a77b780"></a>

```
((diameter) => diameter * 3.14159265)(2)
//=> 6.2831853
```

### Technical frame 5: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00281))_

> You won't be surprised to see how to write and apply a function to two arguments:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00283))_

<a id="atom-technical-atom-ec0274d1c7132fae"></a>

```
((room, board) => room + board)(800, 150)
//=> 950
```

### Technical frame 6: And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00301))_

> But there's another reason for learning the word antidisestablishmentarianism : We might learn how prefixes and postfixes work in English grammar. It's the same thing with (x) => (y) => x . It has a certain important meaning in its own right, and it's also an excellent excuse to learn about functions that make functions, environments, variables, and more.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00299))_

<a id="atom-technical-atom-3aa4f4b69198f2f9"></a>

```
(x) => (y) => x
```

### Technical frame 7: And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00314))_

> The value '2' is bound to the name 'x' in the environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00306))_

<a id="atom-technical-atom-4a548db5b5a8be44"></a>

```
((x) => x)(2)
//=> 2
```

### Technical frame 8: And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00328))_

> 26 Unless the argument is NaN , which isn't equal to anything, including itself . NaN in JavaScript behaves a lot like NULL in SQL.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00327))_

<a id="atom-technical-atom-352494efef5d9591"></a>

```
(value) =>
((ref1, ref2) => ref1 === ref2)(value, value)
```

### Technical frame 9: And also: / Combinators and Function Decorators / higher-order functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00557))_

> As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00559))_

<a id="atom-technical-atom-7193eeef1bd53156"></a>

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

<a id="atom-technical-atom-d58c104eac1daf94"></a>

```
_.map([1, 2, 3], (n) => n * n)
//=> [1, 4, 9]
```

### Technical frame 11: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00597))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00596))_

<a id="atom-technical-atom-7e2e343bb8d0ba90"></a>

```
const squareAll = (array) => map(array,
(n) => n * n);
```

### Technical frame 12: And also: / Building Blocks / partial application

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

### Technical frame 13: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00625))_

> To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. It uses mapWith , which we discussed in Building Blocks. 44 We'll use arguments just to show the difference between using a fat arrow and the function keyword:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00621))_

<a id="atom-technical-atom-243e812c5a716d94"></a>

```
(function () {
return (function () { return arguments[0]; })('inner');
})('outer')
//=> "inner"
```

### Technical frame 14: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00625))_

> To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. It uses mapWith , which we discussed in Building Blocks. 44 We'll use arguments just to show the difference between using a fat arrow and the function keyword:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00623))_

<a id="atom-technical-atom-733056f2f6551e51"></a>

```
(function () {
return (() => arguments[0])('inner');
})('outer')
//=> "outer"
```

### Technical frame 15: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00627))_

> This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind arguments when it's invoked. But if we rewrite row to use the function keyword, it stops working:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00626))_

<a id="atom-technical-atom-f66c3ed611303c0d"></a>

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

### Technical frame 16: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00631))_

> Although this example is clearly unrealistic, there is a general design principle that deserves attention. Sometimes, a function is meant to be used as a Big-F function. It has a name, it is called by different pieces of code, it's a first-class entity in the code.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00629))_

<a id="atom-technical-atom-aeb7942534341524"></a>

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

### Technical frame 17: Recipes with Basic Functions / Partial Application

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

### Technical frame 18: Recipes with Basic Functions / Partial Application

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

### Technical frame 19: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00749))_

> With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00742))_

<a id="atom-technical-atom-eb3ab57c56a2f7dd"></a>

```
const [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid'];
first
//=> 'why'
butFirst
//=> ["hello","there","little","droid"]
```

### Technical frame 20: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00749))_

> With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00748))_

<a id="atom-technical-atom-fcb9efdca6bc6168"></a>

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

### Technical frame 21: Picking the Bean: Choice and Truthiness / truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00779))_

> Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00778))_

<a id="atom-technical-atom-e4e2b300bef7f5ba"></a>

```
!5
//=> false
!undefined
//=> true
```

### Technical frame 22: Composing and Decomposing Data / Tail Calls (and Default Arguments) / default arguments

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01009))_

> Now we don't need to use two functions. A default argument is concise and readable.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01006))_

<a id="atom-technical-atom-0f7127662a9c065a"></a>

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

### Technical atom 23

<a id="atom-technical-atom-6eea21698f698a20"></a>

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00236))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00234))_

```text
back on the block
Back to our function. We evaluated this:
19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This was actually the preferred mechanism until void became commonplace.
20 As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined . We have no idea.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 19 | Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This was actually the preferred mechanism until void became commonplace. |
| 20 | As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined. We have no idea. |

</details>

### Technical atom 24

<a id="atom-technical-atom-178bb2d7be7ec9fc"></a>

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00856))_

> Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00857))_

```text
57 https://en.wikipedia.org/wiki/CAR_and_CDR
58 Kyle Simpson is the author of You Don't Know JS, available here
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 57 | https://en.wikipedia.org/wiki/CAR_and_CDR |
| 58 | Kyle Simpson is the author of You Don't Know JS, available here |

</details>


## Source

- [[javascriptallonge]]
