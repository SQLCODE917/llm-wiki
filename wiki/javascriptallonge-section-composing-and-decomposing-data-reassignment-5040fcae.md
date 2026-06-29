---
page_id: javascriptallonge-section-composing-and-decomposing-data-reassignment-5040fcae
page_kind: source
summary: Composing and Decomposing Data / Reassignment: 49 source-backed entries and 17 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-reassignment-5040fcae@9d07b779f195de77759b88e65abd06b6
---

# Composing and Decomposing Data / Reassignment

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-6f7d7870]] - broader source section: Composing and Decomposing Data
- [[javascriptallonge-section-composing-and-decomposing-data-reassignment-mixing-let-and-const-ca678af6]] - narrower source section: Composing and Decomposing Data / Reassignment / mixing let and const
- [[javascriptallonge-section-composing-and-decomposing-data-reassignment-why-const-and-let-were-invented-d21b490b]] - narrower source section: Composing and Decomposing Data / Reassignment / why const and let were invented

## Statements

- Like some imperative programming languages, JavaScript allows you to re-assign the value bound to parameters. We saw this earlier in rebinding: _(javascriptallonge.pdf (source-range-7239e085-01162))_
- JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-7239e085-01167))_
- Rebinding parameters is usually avoided, but what about rebinding names we declare within a function? What we want is a statement that works like const , but permits us to rebind variables. JavaScript has such a thing, it's called let : _(javascriptallonge.pdf (source-range-7239e085-01168))_
- We took the time to carefully examine what happens with bindings in environments. Let's take the time to explore what happens with reassigning values to variables. The key is to understand that we are rebinding a different value to the same name in the same environment. _(javascriptallonge.pdf (source-range-7239e085-01170))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . We go from: _(javascriptallonge.pdf (source-range-7239e085-01173))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment. _(javascriptallonge.pdf (source-range-7239e085-01178))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . _(javascriptallonge.pdf (source-range-7239e085-01173))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. _(javascriptallonge.pdf (source-range-7239e085-01178))_

## Statements by subsection

### Composing and Decomposing Data / Reassignment / mixing let and const

- Some programmers dislike deliberately shadowing variables. The suggestion is that shadowing a variable is confusing code. If you buy that argument, the way that shadowing works in JavaScript exists to protect us from accidentally shadowing a variable when we move code around. _(javascriptallonge.pdf (source-range-7239e085-01180))_
- Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And: _(javascriptallonge.pdf (source-range-7239e085-01183))_
- Shadowing a const with a let does not permit it to be rebound in its original scope. _(javascriptallonge.pdf (source-range-7239e085-01185))_

### Composing and Decomposing Data / Reassignment / mixing let and const / var

- JavaScript has one more way to bind a name to a value, var . 71 var looks a lot like let : _(javascriptallonge.pdf (source-range-7239e085-01187))_
- But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations: _(javascriptallonge.pdf (source-range-7239e085-01191))_
- Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations. _(javascriptallonge.pdf (source-range-7239e085-01193))_
- But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. Note this example of a function that uses a helper: _(javascriptallonge.pdf (source-range-7239e085-01194))_
- In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped. _(javascriptallonge.pdf (source-range-7239e085-01200))_
- A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. _(javascriptallonge.pdf (source-range-7239e085-01194))_
- In that way, var is a little like const and let , we should always declare and bind names before using them. _(javascriptallonge.pdf (source-range-7239e085-01200))_

### Composing and Decomposing Data / Reassignment / why const and let were invented

- const and let are recent additions to JavaScript. For nearly twenty years, variables were declared with var (not counting parameters and function declarations, of course). However, its functional scope was a problem. _(javascriptallonge.pdf (source-range-7239e085-01202))_
- We haven't looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. It looks a lot like the for loop in C. Here it is with var : _(javascriptallonge.pdf (source-range-7239e085-01203))_
- Hopefully, you can think of a faster way to calculate this sum. 72 And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. But is this ever a problem? _(javascriptallonge.pdf (source-range-7239e085-01205))_
- 72 There is a well known story about Karl Friedrich Gauss when he was in elementary school. His teacher got mad at the class and told them to add the numbers 1 to 100 and give him the answer by the end of the class. About 30 seconds later Gauss gave him the answer. The other kids were adding the numbers like this: 1 + 2 + 3 + . . . . + 99 + 100 = ? But Gauss rearranged the numbers to add them like this: (1 + 100) + (2 + 99) + (3 + 98) + . . . . + (50 + 51) = ? If you notice every pair of numbers adds up to 101. There are 50 pairs of numbers, so the answer is 50*101 = 5050. Of course Gauss came up with the answer about 20 times faster than the other kids. _(javascriptallonge.pdf (source-range-7239e085-01206))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01167))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01164))_

```
const evenStevens = (n) => {
if (n === 0) {
return true;
}
else if (n == 1) {
return false;
}
else {
n = n - 2;
return evenStevens(n);
}
}
evenStevens(42)
//=> true
```

### Technical frame 2: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01167))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01166))_

```
evenStevens = (n) => {
if (n === 0) {
return true;
}
else if (n == 1) {
return false;
}
else {
return evenStevens(n - 2);
}
}
//=> ERROR, evenStevens is read-only
```

### Technical frame 3: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01170))_

> We took the time to carefully examine what happens with bindings in environments. Let's take the time to explore what happens with reassigning values to variables. The key is to understand that we are rebinding a different value to the same name in the same environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01169))_

```
let age = 52;
age = 53;
age
//=> 53
```

### Technical frame 4: Composing and Decomposing Data / Reassignment

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

### Technical frame 5: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01178))_

> Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01174))_

```
{age: 49, '..': global-environment}
To:
{age: 50, '..': {age: 49, '..': global-environment}}
Then back to:
```

### Technical frame 6: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01178))_

> Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01175))_

```
{age: 49, '..': global-environment}
```

### Technical frame 7: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01178))_

> Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01177))_

```
(() => {
let age = 49;
if (true) {
age = 50;
}
return age;
})()
//=> 50
```

### Technical frame 8: Composing and Decomposing Data / Reassignment / mixing let and const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01183))_

> Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01181))_

> If you dislike deliberately shadowing variables, you'll probably take an even more opprobrious view of mixing const and let semantics with a shadowed variable:

### Technical frame 9: Composing and Decomposing Data / Reassignment / mixing let and const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01183))_

> Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01182))_

```
(() => {
let age = 49;
if (true) {
const age = 50;
}
age = 51;
return age;
})()
//=> 51
```

### Technical frame 10: Composing and Decomposing Data / Reassignment / mixing let and const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01185))_

> Shadowing a const with a let does not permit it to be rebound in its original scope.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01184))_

```
(() => {
const age = 49;
if (true) {
let age = 50;
}
age = 52;
return age;
})()
//=> ERROR: age is read-only
```

### Technical frame 11: Composing and Decomposing Data / Reassignment / mixing let and const / var

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

### Technical frame 12: Composing and Decomposing Data / Reassignment / mixing let and const / var

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

### Technical frame 13: Composing and Decomposing Data / Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01193))_

> Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01192))_

```
(() => {
var age = 49;
if (true) {
var age = 50;
}
return age;
})()
//=> 50
```

### Technical frame 14: Composing and Decomposing Data / Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01200))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01195))_

```
const factorial = (n) => {
return innerFactorial(n, 1);
function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
}
factorial(4)
//=> 24
```

### Technical frame 15: Composing and Decomposing Data / Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01200))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01197))_

```
const factorial = (n) => {
let innerFactorial = function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
return innerFactorial(n, 1);
}
JavaScript hoists the let and the assignment. But not so with var:
const factorial = (n) => {
return innerFactorial(n, 1);
var innerFactorial = function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
}
factorial(4)
//=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```

### Technical frame 16: Composing and Decomposing Data / Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01200))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01199))_

```
const factorial = (n) => {
let innerFactorial = undefined;
return innerFactorial(n, 1);
innerFactorial = function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
}
factorial(4)
//=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```

### Technical frame 17: Composing and Decomposing Data / Reassignment / why const and let were invented

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01205))_

> Hopefully, you can think of a faster way to calculate this sum. 72 And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. But is this ever a problem?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01204))_

```
var sum = 0;
for (var i = 1; i <= 100; i++) {
sum = sum + i
}
sum
#=> 5050
```
