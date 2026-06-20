---
page_id: mutation
page_kind: source
summary: Chapter on mutation in JavaScript, covering mutability of arrays and objects, aliases, and implications of mutation.
updated: 2026-06-19
---

## Mutation

This chapter covers the mutability of arrays and objects, how aliases work, and the implications of mutation in JavaScript.

### Mutability of Arrays and Objects

In JavaScript, arrays and objects are mutable. This means that their contents can be changed after they are created.

```javascript
let arr = [1, 2, 3];
arr[0] = 5;
console.log(arr); // [5, 2, 3]

let obj = {a: 1, b: 2};
obj.a = 5;
console.log(obj); // {a: 5, b: 2}
```

### Aliases

When you assign an array or object to a variable, you're not creating a copy. Instead, you're creating a reference to the same object in memory.

```javascript
let arr1 = [1, 2, 3];
let arr2 = arr1;
arr2[0] = 5;
console.log(arr1); // [5, 2, 3]
console.log(arr2); // [5, 2, 3]
```

In this example, `arr1` and `arr2` are aliases for the same array. Changing one affects the other.

### Implications of Mutation

Mutation can lead to unexpected behavior if you're not careful. For example, if you pass an array or object to a function, and that function modifies it, the original array or object will also be modified.

```javascript
function modifyArray(arr) {
  arr.push(4);
}

let originalArray = [1, 2, 3];
modifyArray(originalArray);
console.log(originalArray); // [1, 2, 3, 4]
```

To avoid this, you can create a copy of the array or object before modifying it.

### Reassignment vs. Mutation

It's important to distinguish between reassignment and mutation:

```javascript
let arr = [1, 2, 3];
arr = [4, 5, 6]; // Reassignment
console.log(arr); // [4, 5, 6]

let obj = {a: 1, b: 2};
obj = {a: 3, b: 4}; // Reassignment
console.log(obj); // {a: 3, b: 4}
```

In these examples, we're reassigning the variable to point to a new array or object, rather than modifying the contents of the existing array or object.

### const and Mutation

Even though `const` prevents reassignment, it doesn't prevent mutation of the object or array it refers to:

```javascript
const arr = [1, 2, 3];
arr.push(4); // This is allowed
console.log(arr); // [1, 2, 3, 4]

const obj = {a: 1, b: 2};
obj.a = 3; // This is allowed
console.log(obj); // {a: 3, b: 2}
```

To prevent both reassignment and mutation, you need to use `Object.freeze()` or similar techniques.

## Reassignment

Like some imperative programming languages, JavaScript allows you to re-assign the value bound to parameters. We saw this earlier in rebinding.

By default, JavaScript permits us to _rebind_ new values to names bound with a parameter. For example, we can write:

```javascript
const evenStevens = (n) => {
  if (n === 0) {
    return true;
  } else if (n == 1) {
    return false;
  } else {
    n = n - 2;
    return evenStevens(n);
  }
}
evenStevens(42) //=> true
```

The line `n = n - 2;` _rebinds_ a new value to the name `n`. We will discuss this at much greater length in Reassignment, but long before we do, let's try a similar thing with a name bound using `const`. We've already bound `evenStevens` using `const`, let's try rebinding it:

```javascript
evenStevens = (n) => {
  if (n === 0) {
    return true;
  } else if (n == 1) {
    return false;
  } else {
    return evenStevens(n - 2);
  }
} //=> ERROR, evenStevens is read-only
```

JavaScript does not permit us to rebind a name that has been bound with `const`. We can _shadow_ it by using `const` to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with `const` in an existing scope.

Rebinding parameters is usually avoided, but what about rebinding names we declare within a function? What we want is a statement that works like `const`, but permits us to rebind variables. JavaScript has such a thing, it's called `let`:

```javascript
let age = 52;
age = 53;
console.log(age); // 53
```

We took the time to carefully examine what happens with bindings in environments. Let's take the time to explore what happens with reassigning values to variables. The key is to understand that we are rebinding a different value to the same name in the same environment.

So let's consider what happens with a shadowed variable:

```javascript
(() => {
  let age = 49;
  if (true) {
    let age = 50;
  }
  return age;
})() //=> 49
```

Using `let` to bind 50 to `age` within the block does not change the binding of `age` in the outer environment because the binding of `age` in the block shadows the binding of `age` in the outer environment, just like `const`. We go from:

```
{age: 49, '..': global-environment}
```

To:

```
{age: 50, '..': {age: 49, '..': global-environment}}
```

Then back to:

```
{age: 49, '..': global-environment}
```

However, if we don't shadow `age` with `let`, reassigning within the block changes the original:

```javascript
(() => {
  let age = 49;
  if (true) {
    age = 50;
  }
  return age;
})() //=> 50
```

Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

### Mixing let and const

Some programmers dislike deliberately shadowing variables. The suggestion is that shadowing a variable is confusing code. If you buy that argument, the way that shadowing works in JavaScript exists to protect us from accidentally shadowing a variable when we move code around.

If you dislike deliberately shadowing variables, you'll probably take an even more opprobrious view of mixing `const` and `let` semantics with a shadowed variable:

```javascript
(() => {
  let age = 49;
  if (true) {
    const age = 50;
  }
  age = 51;
  return age;
})() //=> 51
```

Shadowing a `let` with a `const` does not change our ability to rebind the variable in its original scope. And:

```javascript
(() => {
  const age = 49;
  if (true) {
    let age = 50;
  }
  age = 52;
  return age;
})() //=> ERROR: age is read-only
```

Shadowing a `const` with a `let` does not permit it to be rebound in its original scope.

### var

JavaScript has one _more_ way to bind a name to a value, `var`. `var` looks a lot like `let`:

```javascript
const factorial = (n) => {
  let x = n;
  if (x === 1) {
    return 1;
  } else {
    --x;
    return n * factorial(x);
  }
}
factorial(5) //=> 120

const factorial2 = (n) => {
  var x = n;
  if (x === 1) {
    return 1;
  } else {
    --x;
    return n * factorial2(x);
  }
}
factorial2(5) //=> 120
```

But of course, it's not exactly like `let`. It's just different enough to present a source of confusion. First, `var` is not block scoped, it's function scoped, just like function declarations:

```javascript
(() => {
  var age = 49;
  if (true) {
    var age = 50;
  }
  return age;
})() //=> 50
```

Declaring `age` twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All `var` declarations behave as if they were hoisted to the top of the function, a little like function declarations.

But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration _and_ the definition are hoisted. Note this example of a function that uses a helper:

```javascript
const factorial = (n) => {
  return innerFactorial(n, 1);
  function innerFactorial (x, y) {
    if (x == 1) {
      return y;
    } else {
      return innerFactorial(x-1, x * y);
    }
  }
}
factorial(4) //=> 24
```

JavaScript interprets this code as if we had written:

```javascript
const factorial = (n) => {
  let innerFactorial = function innerFactorial (x, y) {
    if (x == 1) {
      return y;
    } else {
      return innerFactorial(x-1, x * y);
    }
  }
  return innerFactorial(n, 1);
}
```

JavaScript hoists the `let` and the assignment. But not so with `var`:

```javascript
const factorial = (n) => {
  return innerFactorial(n, 1);
  var innerFactorial = function innerFactorial (x, y) {
    if (x == 1) {
      return y;
    } else {
      return innerFactorial(x-1, x * y);
    }
  }
}
factorial(4) //=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```

JavaScript hoists the declaration, but not the assignment. It is as if we'd written:

```javascript
const factorial = (n) => {
  let innerFactorial = undefined;
  return innerFactorial(n, 1);
  innerFactorial = function innerFactorial (x, y) {
    if (x == 1) {
      return y;
    } else {
      return innerFactorial(x-1, x * y);
    }
  }
}
factorial(4) //=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```

In that way, `var` is a little like `const` and `let`, we should always declare and bind names before using them. But it's not like `const` and `let` in that it's function scoped, not block scoped.

### Why const and let were invented

`const` and `let` are recent additions to JavaScript. For nearly twenty years, variables were declared with `var` (not counting parameters and function declarations, of course). However, its functional scope was a problem.

We haven't looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. It looks a lot like the for loop in C. Here it is with `var`:

```javascript
var sum = 0;
for (var i = 1; i <= 100; i++) {
  sum = sum + i
}
sum //=> 5050
```

Hopefully, you can think of a faster way to calculate this sum. And perhaps you have noticed that `var i = 1` is tucked away instead of being at the top as we prefer. But is this ever a problem?

Yes. Consider this variation:

```javascript
var introductions = [], names = ['Karl', 'Friedrich', 'Gauss'];
for (var i = 0; i < 3; i++) {
  introductions[i] = "Hello, my name is " + names[i]
}
introductions //=> [ 'Hello, my name is Karl', 'Hello, my name is Friedrich', 'Hello, my name is Gauss' ]
```

So far, so good. Hey, remember that functions in JavaScript are values? Let's get fancy!

```javascript
var introductions = [], names = ['Karl', 'Friedrich', 'Gauss'];
for (var i = 0; i < 3; i++) {
  introductions[i] = (soAndSo) => `Hello, ${soAndSo}, my name is ${names[i]}`
}
introductions //=> [ [Function], [Function], [Function] ]
```

Again, so far, so good. Let's try one of our functions:

```javascript
introductions[1]('Raganwald') //=> 'Hello, Raganwald, my name is undefined'
```

What went wrong? Why didn't it give us 'Hello, Raganwald, my name is Friedrich'? The answer is that pesky `var i`. Remember that `i` is bound in the surrounding environment, so it's as if we wrote:

```javascript
var introductions = [], names = ['Karl', 'Friedrich', 'Gauss'], i = undefined;
for (i = 0; i < 3; i++) {
  introductions[i] = function (soAndSo) {
    return "Hello, " + soAndSo + ", my name is " + names[i]
  }
}
introductions
```

Now, at the time we created each function, `i` had a sensible value, like 0, 1, or 2. But at the time we _call_ one of the functions, `i` has the value 3, which is why the loop terminated. So when the function is called, JavaScript looks `i` up in its enclosing environment (its closure, obviously), and gets the value 3. That's not what we want at all.

The error wouldn't exist at all if we'd used `let` in the first place:

```javascript
let introductions = [], names = ['Karl', 'Friedrich', 'Gauss'];
for (let i = 0; i < 3; i++) {
  introductions[i] = (soAndSo) => `Hello, ${soAndSo}, my name is ${names[i]}`
}
introductions[1]('Raganwald') //=> 'Hello, Raganwald, my name is Friedrich'
```

This small error was a frequent cause of confusion, and in the days when there was no block-scoped `let`, programmers would need to know how to fake it, usually with an IIFE:

```javascript
var introductions = [], names = ['Karl', 'Friedrich', 'Gauss'];
for (var i = 0; i < 3; i++) {
  ((i) => {
    introductions[i] = (soAndSo) => `Hello, ${soAndSo}, my name is ${names[i]}`
  })(i)
}
introductions[1]('Raganwald') //=> 'Hello, Raganwald, my name is Friedrich'
```

Now we're creating a new inner parameter, `i` and binding it to the value of the outer `i`. This works, but `let` is so much simpler and cleaner that it was added to the language in the ECMAScript 2015 specification.

In this book, we will use function declarations sparingly, and not use `var` at all. That does not mean that you should follow the exact same practice in your own code: The purpose of this book is to illustrate certain principles of programming. The purpose of your own code is to get things done. The two goals are often, but not always, aligned.
