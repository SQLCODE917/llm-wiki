---
page_id: javascriptallonge-bind
page_kind: concept
summary: Bind: 11 statement(s) and 30 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-bind@0a731779513fbcb7e54949f34e54de40
---

# Bind

What [[javascriptallonge]] covers about bind:

## Statements

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing

- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. As you recall, value types like strings and numbers are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans as it wishes. _(javascriptallonge.pdf (source-range-7239e085-00322))_

### And also: / That Constant Coffee Craving

- In order to bind 3.14159265 to the name PI , we'll need a function with a parameter of PI applied to an argument of 3.14159265 . If we put our function expression in parentheses, we can apply it to the argument of 3.14159265 : _(javascriptallonge.pdf (source-range-7239e085-00388))_

### And also: / That Constant Coffee Craving / const and lexical scope

- Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-7239e085-00462))_

### And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

- We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-7239e085-00466))_

- Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it. _(javascriptallonge.pdf (source-range-7239e085-00489))_

### And also: / Naming Functions

- It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous. _(javascriptallonge.pdf (source-range-7239e085-00501))_

### And also: / Naming Functions / function declarations

- In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-7239e085-00540))_

### Recipes with Basic Functions / Partial Application

- These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic. _(javascriptallonge.pdf (source-range-7239e085-00660))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

- That match would fail because the array doesn't have an element to assign to what . But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. Therefore: _(javascriptallonge.pdf (source-range-7239e085-00865))_

### Composing and Decomposing Data / Reassignment

- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . We go from: _(javascriptallonge.pdf (source-range-7239e085-01173))_

- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment. _(javascriptallonge.pdf (source-range-7239e085-01178))_


## Technical atoms

### Technical frame 1: And also: / That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00392))_

> This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00389))_

```
((PI) =>
// ????
)(3.14159265)
```

### Technical frame 2: And also: / That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00392))_

> This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00391))_

```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

### Technical frame 3: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00402))_

> Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00399))_

```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```

### Technical frame 4: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00419))_

> This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00418))_

```
((diameter, PI) => diameter * PI)(2, 3.14159265)
//=> 6.2831853
```

### Technical frame 5: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00432))_

> Notice calc(d) ? This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () . A name that's bound to a function is a valid expression evaluating to a function. 30

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00431))_

```
(d) => {
const calc = (diameter) => {
const PI = 3.14159265;
return diameter * PI
};
return "The circumference is " + calc(d)
}
```

### Technical frame 6: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00433))_

> Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as 'first class entities. ' Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00432))_

> This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () .

### Technical frame 7: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00436))_

> 30 We're into the second chapter and we've finally named a function. Sheesh.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00435))_

```
(d) => {
const PI
= 3.14159265,
calc = (diameter) => diameter * PI;
return "The circumference is " + calc(d)
}
```

### Technical frame 8: And also: / That Constant Coffee Craving / const and lexical scope

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00454))_

> We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00453))_

```
((diameter_fn) =>
diameter_fn(2)
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
//=> 6.2831853
```

### Technical frame 9: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00473))_

> And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the 'outer' environment? Let's rewrite things slightly differently:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00470))_

```
((PI) =>
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)(3)
```

### Technical frame 10: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00475))_

> Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . Does that binding 'overwrite' the outer one? Will our function return 6 or 6.2831853 ? This is a book, you've already scanned ahead, so you know that the answer is no , the inner binding does not overwrite the outer binding:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00474))_

```
((PI) => {
((PI) => {})(3);
return (diameter) => diameter * PI;
})(3.14159265)
```

### Technical frame 11: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00477))_

> We say that when we bind a variable using a parameter inside another binding, the inner binding shadows the outer binding. It has effect inside its own scope, but does not affect the binding in the enclosing scope.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00476))_

```
((PI) => {
((PI) => {})(3);
return (diameter) => diameter * PI;
})(3.14159265)(2)
//=> 6.2831853
```

### Technical frame 12: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00481))_

> Parameters are only bound when we invoke a function. That's why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block? We'll need a gratuitous block. We've seen if statements, what could be more gratuitous than:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00479))_

```
((diameter) => {
const PI = 3.14159265;
(() => {
const PI = 3;
})();
return diameter * PI;
})(2)
//=> 6.2831853
```

### Technical frame 13: And also: / Naming Functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00501))_

> It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00500))_

```
const repeat = (str) => str + str
```

### Technical frame 14: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00523))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00522))_

```
const double = function repeat (str) {
return str + str;
}
```

### Technical frame 15: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00529))_

> Now, the function's actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00528))_

```
someBackboneView.on('click', function clickHandler () {
//...
});
```

### Technical frame 16: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00533))_

> Clearly, the name even is bound to the function within the function's body . Is it bound to the function outside of the function's body?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00532))_

```
(function even (n) {
if (n === 0) {
return true
}
else return !even(n - 1)
})(5)
//=> false
(function even (n) {
if (n === 0) {
return true
}
else return !even(n - 1)
})(2)
//=> true
```

### Technical frame 17: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00535))_

> even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00534))_

```
even
//=> Can't find variable: even
```

### Technical frame 18: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00540))_

> In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00539))_

```
{
```

### Technical frame 19: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00543))_

> We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00542))_

```
(function () {
return fizzbuzz();
const fizzbuzz = function fizzbuzz () {
return "Fizz" + "Buzz";
}
})()
//=> undefined is not a function (evaluating 'fizzbuzz()')
```

### Technical frame 20: Recipes with Basic Functions / Partial Application

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

### Technical frame 21: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00865))_

> That match would fail because the array doesn't have an element to assign to what . But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. Therefore:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00864))_

```
const [what] = [];
```

### Technical frame 22: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00869))_

> From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00866))_

```
const [what] = [];
what
//=> undefined
const [which, what,
who
//=> undefined
```

### Technical frame 23: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00869))_

> From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00867))_

```
const [...they] = [];
they
//=> []
const [which, what, .
they
//=> []
```

### Technical frame 24: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01091))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01092))_

```
const SecretDecoderRing = {
encode (plaintext) {
return plaintext
.split('')
.map( char => char.charCodeAt() )
.map( code => code + 1 )
.map( code => String.fromCharCode(code) )
.join('');
},
decode (cyphertext) {
return cyphertext
.split('')
.map( char => char.charCodeAt() )
.map( code => code - 1 )
.map( code => String.fromCharCode(code) )
.join('');
}
}
```

### Technical frame 25: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01173))_

> Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . We go from:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01172))_

```
(() => {
let age = 49;
if (true) {
let age = 50;
}
return age;
})()
//=> 49
```

### Technical frame 26: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01178))_

> Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01174))_

```
{age: 49, '..': global-environment}
To:
{age: 50, '..': {age: 49, '..': global-environment}}
Then back to:
```

### Technical frame 27: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01178))_

> Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01175))_

```
{age: 49, '..': global-environment}
```

### Technical frame 28: Composing and Decomposing Data / Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01191))_

> But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01188))_

```
const factorial = (n) => {
let x = n;
if (x === 1) {
return 1;
}
else {
--x;
return n * factorial(x);
}
}
factorial(5)
//=> 120
const factorial2 = (n) => {
var x = n;
if (x === 1) {
return 1;
}
else {
--x;
```

### Technical frame 29: Composing and Decomposing Data / Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01191))_

> But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01190))_

```
return n * factorial2(x);
}
}
factorial2(5)
//=> 120
```

### Technical atom 30

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00612))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00613))_

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

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from And also: / Naming Functions: It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . This syntax binds an anonymous function to a name in an ... [truncated]; Function shares technical record from And also: / That Constant Coffee Craving: ((PI) => // ???? )(3.14159265) (1 shared statement(s), 15 shared atom(s))
- [[javascriptallonge-binding]] - shared statements and technical atoms: Binding shares source evidence from And also: / That Constant Coffee Craving / const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope.; Binding shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: ((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265) (3 shared statement(s), 8 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to ... [truncated]; Javascript shares technical record from And also: / Naming Functions / the function keyword: someBackboneView.on('click', function clickHandler () { //... }); (2 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-environment]] - shared statements and technical atoms: Environment shares source evidence from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated]; Environment shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: ((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265) (3 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-block]] - shared statements and technical atoms: Block shares source evidence from Composing and Decomposing Data / Reassignment: Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding ... [truncated]; Block shares technical record from Composing and Decomposing Data / Reassignment: (() => { let age = 49; if (true) { let age = 50; } return age; })() //=> 49 (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms: Value shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to ... [truncated]; Value shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching: const [...they] = []; they //=> [] const [which, what, . they //=> [] (3 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-argument]] - shared statements and technical atoms: Argument shares source evidence from Recipes with Basic Functions / Partial Application: These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want ... [truncated]; Argument shares technical record from Recipes with Basic Functions / Partial Application: const callFirst = (fn, larg) => function (...rest) { return fn.call(this, larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call(this, ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-different]] - shared statements and technical atoms: Different shares source evidence from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated]; Different shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: ((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265) (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from Recipes with Basic Functions / Partial Application: These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want ... [truncated]; List shares technical record from Recipes with Basic Functions / Partial Application: const callFirst = (fn, larg) => function (...rest) { return fn.call(this, larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call(this, ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-parameter]] - shared statements and technical atoms: Parameter shares source evidence from And also: / That Constant Coffee Craving / const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope.; Parameter shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: ((diameter) => { const PI = 3.14159265; (() => { const PI = 3; })(); return diameter * PI; })(2) //=> 6.2831853 (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-partial-application]] - shared statements and technical atoms: partial application shares source evidence from Recipes with Basic Functions / Partial Application: These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want ... [truncated]; partial application shares technical record from Recipes with Basic Functions / Partial Application: const callFirst = (fn, larg) => function (...rest) { return fn.call(this, larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call(this, ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from And also: / That Constant Coffee Craving: ((PI) => // ???? )(3.14159265) (9 shared atom(s))
- [[javascriptallonge-function-keyword]] - shared technical atoms: the function keyword shares technical record from And also: / Naming Functions / the function keyword: const double = function repeat (str) { return str + str; } (5 shared atom(s))
- [[javascriptallonge-array]] - shared technical atoms: Array shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching: const [what] = []; (3 shared atom(s))
- [[javascriptallonge-bound]] - shared technical atoms: Bound shares technical record from And also: / Naming Functions / the function keyword: (function even (n) { if (n === 0) { return true } else return !even(n - 1) })(5) //=> false (function even (n) { if (n === 0) { return true } else return !even(n - 1 ... [truncated] (2 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical record from Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax: const SecretDecoderRing = { encode (plaintext) { return plaintext .split('') .map( char => char.charCodeAt() ) .map( code => code + 1 ) .map( code => String.fromChar ... [truncated] (2 shared atom(s))
- [[javascriptallonge-declaration]] - shared technical atoms: Declaration shares technical record from And also: / Naming Functions / function declarations: { (1 shared atom(s))
- [[javascriptallonge-program]] - shared technical atoms: Program shares technical record from And also: / That Constant Coffee Craving / const and lexical scope: ((diameter_fn) => diameter_fn(2) )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) //=> 6.2831853 (1 shared atom(s))
- [[javascriptallonge-recipe]] - shared technical atoms: Recipe shares technical record from Recipes with Basic Functions / Partial Application: const callFirst = (fn, larg) => function (...rest) { return fn.call(this, larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call(this, ... [truncated] (1 shared atom(s))
- [[javascriptallonge-result]] - shared technical atoms: Result shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching: const [...they] = []; they //=> [] const [which, what, . they //=> [] (1 shared atom(s))
- [[javascriptallonge-const]] - shared statements: Const shares source evidence from And also: / That Constant Coffee Craving / const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. (1 shared statement(s))
- [[javascriptallonge-evaluating]] - shared statements: Evaluating shares source evidence from Composing and Decomposing Data / Reassignment: Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it fi ... [truncated] (1 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
