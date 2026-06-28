---
page_id: javascriptallonge-value
page_kind: concept
summary: Value: 28 statement(s) and 27 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-value@520c66ea159f1256e09c05419e546bca
---

# Value

What [[javascriptallonge]] covers about value:

## Statements

- In JavaScript, the absence of a value is written undefined, and it means there is no value. _(javascriptallonge.pdf (source-range-83ecb080-00319))_
- We said that JavaScript binds names to values, but we didn’t say what it means to bind a name to a value. _(javascriptallonge.pdf (source-range-83ecb080-00455))_
- Every time you evaluate an expression (including typing something in) to create an array, you’re creating a new, distinct value even if it _appears_ to be the same as some other array value. _(javascriptallonge.pdf (source-range-83ecb080-00210))_
- The value of a variable when evaluated in an environment is the value bound to the variable’s name in that environment, which is ‘2’ _(javascriptallonge.pdf (source-range-83ecb080-00449))_
- We just saw that values bound with const use lexical scope, just like values bound with parameters. _(javascriptallonge.pdf (source-range-83ecb080-00644))_
- All values of true are === all other values of true. _(javascriptallonge.pdf (source-range-83ecb080-01097))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-83ecb080-01596))_
- Given two values, we can say that K always returns the _first_ value: K(x)(y) => x (that’s not valid JavaScript, but it’s essentially how it works). _(javascriptallonge.pdf (source-range-83ecb080-02060))_
- Given two values, we can say that K always returns the _first_ value, and given two values, K(I) always returns the _second_ value. _(javascriptallonge.pdf (source-range-83ecb080-02074))_
- It says, “take these two values and apply them to this function.” There are other, similar combinators that apply values to functions. _(javascriptallonge.pdf (source-range-83ecb080-02114))_
- All values are expressions. _(javascriptallonge.pdf (source-range-83ecb080-00161))_
- All values are expressions. _(javascriptallonge.pdf (source-range-83ecb080-00168))_
- This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2. _(javascriptallonge.pdf (source-range-83ecb080-00188))_
- Value types share the same identity if they have the same contents. _(javascriptallonge.pdf (source-range-83ecb080-00268))_
- Here’s how we apply a function to some values in JavaScript: Let’s say that _fn_expr_ is an expression that when evaluated, produces a function. _(javascriptallonge.pdf (source-range-83ecb080-00275))_
- Values like 0 are expressions, as are things like 40 + 2. _(javascriptallonge.pdf (source-range-83ecb080-00286))_
- We’ll see below that while JavaScript always calls by value, the notion of a “value” has additional subtlety. _(javascriptallonge.pdf (source-range-83ecb080-00427))_
- The value ‘2’ is bound to the name ‘x’ in the environment. _(javascriptallonge.pdf (source-range-83ecb080-00447))_
- JavaScript places _references_ to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-83ecb080-00460))_
- Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-83ecb080-00642))_
- But instead of binding two different variables to the same name in two different places, we’ll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-83ecb080-00646))_
- Every other value in JavaScript is “truthy” except the aforementioned false, null, undefined, NaN, 0, and ''. _(javascriptallonge.pdf (source-range-83ecb080-01106))_
- They don’t operate strictly on logical values, and they don’t commute: a || b is not always equal to b || a, and the same goes for &&. _(javascriptallonge.pdf (source-range-83ecb080-01146))_
- As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. _(javascriptallonge.pdf (source-range-83ecb080-01274))_
- The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells. _(javascriptallonge.pdf (source-range-83ecb080-01534))_
- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. _(javascriptallonge.pdf (source-range-83ecb080-01534))_
- In JavaScript, almost every type of value can _mutate_ . _(javascriptallonge.pdf (source-range-83ecb080-01688))_
- The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. _(javascriptallonge.pdf (source-range-83ecb080-01707))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00168))_

> All values are expressions. That’s easy! Are there any other kinds of expressions? Sure! let’s go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let’s hand over some ground coffee plus some boiling water.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00170))_

> And if we hand over the espresso, we get the espresso right back.

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00188))_

> Second, sometimes, the cups are of the same type–perhaps two espresso cups–but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00189))_

> **true** === **false** _//=> false_ 2 !== 5 _//=> true_ 'two' === 'five' _//=> false_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00197))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00195))_

> - 2 + 2 === 4 _//=> true_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00197))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00196))_

> - (2 + 2 === 4) === (2 !== 5) _//=> true_

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00197))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00198))_

> So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them.

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00207))_

> Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of 42 is identical to every other value of 42? Try these for yourself:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00208))_

> [2-1, 2, 2+1] === [1,2,3] [1,2,3] === [1, 2, 3] [1, 2, 3] === [1, 2, 3]

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00285))_

> Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00287))_

> (() => 1 + 1)() _//=> 2_ (() => "Hello, " + "JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** * **Infinity** )() _//=> Infinity_

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00291))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00292))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00438))_

> How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dictionary for each argument. So when we write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00439))_

> ((x) => x)(2) _//=> 2_

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00461))_

> Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00459))_

> So JavaScript can make as many copies of strings, numbers, or booleans as it wishes.

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00462))_

> And with that, we’re ready to look at _closures_ . When we combine our knowledge of value types, reference types, arguments, and closures, we’ll understand why this function always evaluates to true no matter what argument[26] you apply it to:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00464))_

> - ((ref1, ref2) => ref1 === ref2)(value, value)

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00673, source-range-83ecb080-00676))_

> This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this: If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:”

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00674))_

> ((diameter) => { **const** PI = 3.14159265;

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00673, source-range-83ecb080-00676))_

> This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this: If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:”

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00675))_

> **if** ( **true** ) { **const** PI = 3; } **return** diameter * PI; })(2) _//=> would return 6 if const had function scope_

### Technical atom 14

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00676))_

> If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:”

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00678))_

> **if** ( **true** ) { **const** PI = 3.14159265; } **return** diameter * PI; })(2) _//=> would return 6.2831853 if const had function scope_

### Technical atom 15

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01097))_

> true and false are value types. All values of true are === all other values of true. We can see that is the case by looking at some operators we can perform on boolean values, !, &&, and ||. To being with, ! is a unary prefix operator that negates its argument. So:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01100))_

> ! **true** _//=> false_ ! **false** _//=> true_

### Technical atom 16

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01272, source-range-83ecb080-01274))_

> And if there aren’t any items to assign with ..., JavaScript assigns an empty array: From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01273))_

> **const** [...they] = []; they _//=> []_ **const** [which, what, ...they] = ["duck feet", "tiger tail"]; they _//=> []_

### Technical atom 17

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01594))_

> Objects use [] to access the values by name, using a string:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01595))_

> - { year: 2012, month: 6, day: 14 }['day'] _//=> 14_

### Technical atom 18

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01596))_

> Values contained within an object work just like values contained within an array, we access them by reference to the original:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01598))_

> - x = unique(),

### Technical atom 19

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01596))_

> Values contained within an object work just like values contained within an array, we access them by reference to the original:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01599))_

> - y = unique(),

### Technical atom 20

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01604))_

> If the name is an alphanumeric string conforming to the same rules as names of variables, there’s a simplified syntax for accessing the values:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01607))_

> **const** date = { year: 2012, month: 6, day: 14 };

### Technical atom 21

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01611))_

> All containers can contain any value, including functions or other containers, like a fat arrow function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01612))_

> **const** Mathematics = { abs: (a) => a < 0 ? -a : a }; Mathematics.abs(-5) _//=> 5_

### Technical atom 22

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01688))_

> In JavaScript, almost every type of value can _mutate_ . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using []. You can reassign a value using [] =:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01689))_

> **const** oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree _//=> [ 'one', 2, 3 ]_

### Technical atom 23

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01690))_

> You can even add a value:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01693))_

> **const** oneTwoThree = [1, 2, 3]; oneTwoThree[3] = 'four'; oneTwoThree _//=> [ 1, 2, 3, 'four' ]_

### Technical atom 24

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01696))_

> We have established that JavaScript’s semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01697))_

> **const** allHallowsEve = [2012, 10, 31] **const** halloween = allHallowsEve;

### Technical atom 25

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01698, source-range-83ecb080-01701))_

> Both halloween and allHallowsEve are bound to the same array value within the local environment. And also: There are two nested environments, and each one binds a name to the exact same array value. In each of these examples, we have created two _aliases_ for the same value. Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01699))_

> **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { _// ..._

### Technical atom 26

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01702, source-range-83ecb080-01707))_

> This is vital. Consider what we already know about shadowing: The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we _mutate_ the value in the inner environment?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01705))_

> **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31];

### Technical atom 27

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01707))_

> The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we _mutate_ the value in the inner environment?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01706))_

> })(allHallowsEve); allHallowsEve _//=> [2012, 10, 31]_


## Related pages

- [[javascriptallonge-javascript]] - shared statements and technical atoms (8 shared statement(s), 8 shared atom(s))
- [[javascriptallonge-type]] - shared statements and technical atoms (3 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms (2 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-environment]] - shared statements and technical atoms (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms (4 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms (3 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms (2 shared atom(s))
- [[javascriptallonge-array]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-bind]] - shared statements (3 shared statement(s))
- [[javascriptallonge-evaluate]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
