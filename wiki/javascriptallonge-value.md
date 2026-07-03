---
page_id: javascriptallonge-value
page_kind: concept
page_family: broad-topic
summary: Value: 28 statement(s) and 31 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-value@427cc6f2515368feb2e95843dfcc4de2
---

# Value

What [[javascriptallonge]] covers about value:


## Related pages

### Source structure

- [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-call-by-value-ae929990]] - source section: And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by value shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by value: Like most contemporary programming languages, JavaScript uses the 'call by value' evaluation strategy 23 . That means that when you write some code that appears to a ... [truncated]; And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by value shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by value: ((diameter) => diameter * 3.14159265)(1 + 1) //=> 6.2831853 (4 shared statement(s), 1 shared atom(s))

### Shared technical atoms

- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Prelude: Values and Expressions over Coffee / values and identity: Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to co ... [truncated]; Javascript shares technical record from Prelude: Values and Expressions over Coffee / values and identity: 2 === 2 //=> true 'hello' !== 'goodbye' //=> true (7 shared statement(s), 12 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Yes. Consider this variation: / Making Data Out Of Functions / the vireo: As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar comb ... [truncated]; Function shares technical record from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity)() //=> Infinity (1 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-type]] - shared statements and technical atoms: Type shares source evidence from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities: You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same cont ... [truncated]; Type shares technical record from Prelude: Values and Expressions over Coffee / values and identity / value types: 2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true (4 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-identity]] - shared statements and technical atoms: Identity shares source evidence from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities: You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same cont ... [truncated]; Identity shares technical record from Prelude: Values and Expressions over Coffee / values and identity: 2 === 2 //=> true 'hello' !== 'goodbye' //=> true (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-environment]] - shared statements and technical atoms: Environment shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, ... [truncated]; Environment shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: ((x) => x)(2) //=> 2 (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical record from Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax: { year: 2012, month: 6, day: 14 } (4 shared atom(s))
- [[javascriptallonge-coffee]] - shared technical atoms: Coffee shares technical record from Prelude: Values and Expressions over Coffee / values are expressions: And if we hand over the espresso, we get the espresso right back. (3 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from Prelude: Values and Expressions over Coffee / values and identity / reference types: They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to crea ... [truncated]; Expression shares technical table: Prelude: Values and Expressions over Coffee The following material is extremely basic, however like most stories, the best way to begin is to start at the very begin ... [truncated] (1 shared statement(s), 2 shared atom(s))

### Topics

- [[javascriptallonge-function-return-value]] - narrower topic: Function Return Value shares technical record from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity)() //=> Infinity (2 shared atom(s))
## Statements by source section

### Prelude: Values and Expressions over Coffee / values are expressions

- All values are expressions. Say you hand the barista a café Cubano. Yup, you hand over a cup with some coffee infused through partially caramelized sugar. You say, 'I want one of these.' The barista is no fool, she gives it straight back to you, and you get exactly what you want. Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). _(javascriptallonge.pdf (source-range-7239e085-00101))_

### Prelude: Values and Expressions over Coffee / values and identity

- Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-7239e085-00120))_

### Prelude: Values and Expressions over Coffee / values and identity / reference types

- They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you're creating a new, distinct value even if it appears to be the same as some other array value. As we'll see, this is true of many other kinds of values, including functions , the main subject of this book. _(javascriptallonge.pdf (source-range-7239e085-00137))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities

- You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same contents. Reference types do not. _(javascriptallonge.pdf (source-range-7239e085-00176))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

- In the prelude, we looked at expressions. Values like 0 are expressions, as are things like 40 + 2 . Can we put an expression to the right of the arrow? _(javascriptallonge.pdf (source-range-7239e085-00191))_

### Or even: / the simplest possible block / undefined

- In JavaScript, the absence of a value is written undefined , and it means there is no value. It will crop up again. undefined is its own type of value, and it acts like a value type: _(javascriptallonge.pdf (source-range-7239e085-00217))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by value

- We'll see below that while JavaScript always calls by value, the notion of a 'value' has additional subtlety. But before we do, let's look at variables. _(javascriptallonge.pdf (source-range-7239e085-00296))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

- The value '2' is bound to the name 'x' in the environment. _(javascriptallonge.pdf (source-range-7239e085-00314))_

- The value of a variable when evaluated in an environment is the value bound to the variable's name in that environment, which is '2' _(javascriptallonge.pdf (source-range-7239e085-00316))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing

- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. As you recall, value types like strings and numbers are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans as it wishes. _(javascriptallonge.pdf (source-range-7239e085-00322))_

- Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-7239e085-00324))_

### And also: / That Constant Coffee Craving / const and lexical scope

- Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-7239e085-00462))_

### And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

- We just saw that values bound with const use lexical scope, just like values bound with parameters. They are looked up in the environment where they are declared. And we know that functions create environments. Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions. _(javascriptallonge.pdf (source-range-7239e085-00464))_

- We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-7239e085-00466))_

### Picking the Bean: Choice and Truthiness

- true and false are value types. All values of true are === all other values of true. We can see that is the case by looking at some operators we can perform on boolean values, ! , && , and || . To being with, ! is a unary prefix operator that negates its argument. So: _(javascriptallonge.pdf (source-range-7239e085-00759))_

### Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

- Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' . (Many other languages that have a notion of truthiness consider zero and the empty string to be truthy, not falsy, so beware of blindly transliterating code from one language to another!) _(javascriptallonge.pdf (source-range-7239e085-00766))_

### Picking the Bean: Choice and Truthiness / truthiness and operators

- In JavaScript, && and || aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && . _(javascriptallonge.pdf (source-range-7239e085-00790))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

- From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-7239e085-00869))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. Lisp's basic data type is often said to be the list, but in actuality it was the 'cons cell,' the term used to describe two 15-bit values stored in one word. The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells. _(javascriptallonge.pdf (source-range-7239e085-01032))_

### Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-7239e085-01077))_

### Composing and Decomposing Data / Mutation

- In JavaScript, almost every type of value can mutate . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using [] . You can reassign a value using [] = : _(javascriptallonge.pdf (source-range-7239e085-01121))_

- The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we mutate the value in the inner environment? _(javascriptallonge.pdf (source-range-7239e085-01134))_

### Yes. Consider this variation: / Making Data Out Of Functions / the kestrel and the idiot

- This is very interesting. Given two values, we can say that K always returns the first value: K(x)(y) => x (that's not valid JavaScript, but it's essentially how it works). _(javascriptallonge.pdf (source-range-7239e085-01344))_

- This is very interesting. Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value. _(javascriptallonge.pdf (source-range-7239e085-01352))_

### Yes. Consider this variation: / Making Data Out Of Functions / the vireo

- As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap . _(javascriptallonge.pdf (source-range-7239e085-01374))_


## Technical atoms

### Technical frame 1: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00107))_

> All values are expressions. That's easy! Are there any other kinds of expressions? Sure! let's go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let's hand over some ground coffee plus some boiling water.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00106))_

<a id="atom-technical-atom-51c8d8435d99be90"></a>

```
42
//=> 42
```

### Technical frame 2: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00108))_

> Astute readers will realize we're omitting something. Congratulations! Take a sip of espresso. We'll get to that in a moment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00109))_

<a id="atom-technical-atom-eec8b1329c6317b1"></a>

> And if we hand over the espresso, we get the espresso right back.

### Technical frame 3: Prelude: Values and Expressions over Coffee / values and identity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00118))_

> First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types . For example, the string "2" is not the same thing as the number 2 . Strings and numbers are different types, so strings and numbers are never identical:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00116))_

<a id="atom-technical-atom-01aacee1aae7ab09"></a>

```
2 === 2
//=> true
'hello' !== 'goodbye'
//=> true
```

### Technical frame 4: Prelude: Values and Expressions over Coffee / values and identity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00120))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00121))_

<a id="atom-technical-atom-e1c132020e57e6fc"></a>

```
true === false
//=> false
2 !== 5
//=> true
'two' === 'five'
//=> false
```

### Technical frame 5: Prelude: Values and Expressions over Coffee / values and identity / value types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00126))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same 'content.' Strings, numbers, and booleans are examples of what JavaScript calls 'value' or 'primitive' types. We'll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00125))_

<a id="atom-technical-atom-af344335a7478637"></a>

```
2 + 2 === 4
//=> true
(2 + 2 === 4) === (2 !== 5)
//=> true
```

### Technical frame 6: Prelude: Values and Expressions over Coffee / values and identity / value types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00129))_

> Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d'Italia

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00127))_

<a id="atom-technical-atom-cb35e8520be9c9a9"></a>

> So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them.

### Technical frame 7: Prelude: Values and Expressions over Coffee / values and identity / reference types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00136))_

> How about that! When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own unique array that is not identical to any other array, even if that other array also looks like [1, 2, 3] . It's as if JavaScript is generating new cups of coffee with serial numbers on the bottom.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00135))_

<a id="atom-technical-atom-84f6c6969b1a1da1"></a>

```
[2-1, 2, 2+1] === [1,2,3]
[1,2,3] === [1, 2, 3]
[1, 2, 3] === [1, 2, 3]
```

### Technical frame 8: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00193))_

> Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00192))_

<a id="atom-technical-atom-7673f47cd782cb73"></a>

```
(() => 1 + 1)()
//=> 2
(() => "Hello, " + "JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity * Infinity)()
//=> Infinity
```

### Technical frame 9: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00196))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00197))_

<a id="atom-technical-atom-89adc0ecfdaf7a9b"></a>

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.

### Technical frame 10: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00220))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00218))_

<a id="atom-technical-atom-19e8d9573a10150a"></a>

```
undefined
```

### Technical frame 11: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00220))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00219))_

<a id="atom-technical-atom-93fa6a3bba5cbb20"></a>

```
//=> undefined
```

### Technical frame 12: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00222))_

> No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-)

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00221))_

<a id="atom-technical-atom-be928e28bfd7dbb2"></a>

```
undefined === undefined
//=> true
(() => {})() === (() => {})()
//=> true
(() => {})() === undefined
//=> true
```

### Technical frame 13: And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00314))_

> The value '2' is bound to the name 'x' in the environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00306))_

<a id="atom-technical-atom-4a548db5b5a8be44"></a>

```
((x) => x)(2)
//=> 2
```

### Technical frame 14: And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00328))_

> 26 Unless the argument is NaN , which isn't equal to anything, including itself . NaN in JavaScript behaves a lot like NULL in SQL.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00327))_

<a id="atom-technical-atom-352494efef5d9591"></a>

```
(value) =>
((ref1, ref2) => ref1 === ref2)(value, value)
```

### Technical frame 15: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00486))_

<a id="atom-technical-atom-d1848416f5b4149d"></a>

```
((diameter) => {
const PI = 3.14159265;
if (true) {
const PI = 3;
}
return diameter * PI;
})(2)
//=> would return 6 if const had function scope
```

### Technical frame 16: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00488))_

<a id="atom-technical-atom-0c5d98acca1d8c87"></a>

```
((diameter) => {
if (true) {
const PI = 3.14159265;
}
return diameter * PI;
})(2)
//=> would return 6.2831853 if const had function scope
```

### Technical frame 17: Picking the Bean: Choice and Truthiness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00763))_

> Now, note well: We have said what happens if you pass boolean values to ! , && , and || , but we've said nothing about expressions or about passing other values. We'll look at those presently.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00760))_

<a id="atom-technical-atom-843bd04c4cf702f8"></a>

```
!true
//=> false
!false
//=> true
```

### Technical frame 18: Picking the Bean: Choice and Truthiness / truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00790))_

> In JavaScript, && and || aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00789))_

<a id="atom-technical-atom-18deb0cfe93967e8"></a>

```
1 || 2
//=> 1
null && undefined
//=> null
undefined && null
//=> undefined
```

### Technical frame 19: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00869))_

> From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00867))_

<a id="atom-technical-atom-c8b4e6fb8e816337"></a>

```
const [...they] = [];
they
//=> []
const [which, what, .
they
//=> []
```

### Technical frame 20: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01077))_

> Values contained within an object work just like values contained within an array, we access them by reference to the original:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01074))_

<a id="atom-technical-atom-e11086561fe47bd6"></a>

```
{ year: 2012, month: 6, day: 14 }
```

### Technical frame 21: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01079))_

> Names needn't be alphanumeric strings. For anything else, enclose the label in quotes:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01078))_

<a id="atom-technical-atom-c5b0e41f7a0c2c27"></a>

```
const unique = () => [],
x = unique(),
y = unique(),
z = unique(),
o = { a: x, b: y, c: z };
o['a'] === x && o['b'] === y && o['c'] === z
//=> true
```

### Technical frame 22: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01083))_

> Expressions can be used for keys as well. The syntax is to enclose the key's expression in [ and ] :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01082))_

<a id="atom-technical-atom-d7c08b474a80c567"></a>

```
const date = { year: 2012, month: 6, day: 14 };
date['day'] === date.day
//=> true
```

### Technical frame 23: Composing and Decomposing Data / Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01091))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01086))_

<a id="atom-technical-atom-428f9541a890a236"></a>

```
const Mathematics = {
abs: (a) => a < 0 ? -a : a
};
Mathematics.abs(-5)
//=> 5
```

### Technical frame 24: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01127))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01122))_

<a id="atom-technical-atom-a96fb43e925c4354"></a>

```
const oneTwoThree = [1, 2, 3];
oneTwoThree[0] = 'one';
oneTwoThree
//=> [ 'one', 2, 3 ]
```

### Technical frame 25: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01127))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01124))_

<a id="atom-technical-atom-817753074035247d"></a>

```
const oneTwoThree = [1, 2, 3];
oneTwoThree[3] = 'four';
oneTwoThree
//=> [ 1, 2, 3, 'four' ]
```

### Technical frame 26: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01129))_

> Both halloween and allHallowsEve are bound to the same array value within the local environment. And also:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01128))_

<a id="atom-technical-atom-8929b738d6f87550"></a>

```
const allHallowsEve = [2012, 10, 31]
const halloween = allHallowsEve;
```

### Technical frame 27: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01131))_

> There are two nested environments, and each one binds a name to the exact same array value. In each of these examples, we have created two aliases for the same value. Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01130))_

<a id="atom-technical-atom-1b0e0f467897117c"></a>

```
const allHallowsEve = [2012, 10, 31];
(function (halloween) {
// ...
})(allHallowsEve);
```

### Technical frame 28: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01134))_

> The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we mutate the value in the inner environment?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01133))_

<a id="atom-technical-atom-27a5d53a2b1d212c"></a>

```
const allHallowsEve = [2012, 10, 31];
(function (halloween) {
halloween = [2013, 10, 31];
})(allHallowsEve);
allHallowsEve
//=> [2012, 10, 31]
```

### Technical atom 29

<a id="atom-technical-atom-08860569e8259d48"></a>

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00110))_

> Let's try this as well with something else the computer understands easily:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00112))_

```text
10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' and so does the computer.
11 In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 10 | Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' and so does the computer. |
| 11 | In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values. |

</details>


## Source

- [[javascriptallonge]]
