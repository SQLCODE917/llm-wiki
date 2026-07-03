---
page_id: javascriptallonge-statement
page_kind: concept
page_family: topic-concept
summary: Statement: 6 statement(s) and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-statement@42927cc94151aa03daa8e43385dc0625
---

# Statement

What [[javascriptallonge]] covers about statement:

## Statements

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / a quick summary of functions and bodies

- One of the important possible statements is a return statement. A return statement accepts any valid JavaScript expression. _(javascriptallonge.pdf (source-range-7239e085-00288))_

### And also: / That Constant Coffee Craving / nested blocks

- The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like: _(javascriptallonge.pdf (source-range-7239e085-00442))_

### And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. So where are const variables bound? In the function environment? Or in an environment corresponding to the block? _(javascriptallonge.pdf (source-range-7239e085-00465))_

- Parameters are only bound when we invoke a function. That's why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block? We'll need a gratuitous block. We've seen if statements, what could be more gratuitous than: _(javascriptallonge.pdf (source-range-7239e085-00481))_

### And also: / Summary / Functions

- Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-7239e085-00649))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

- The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do the same thing with more than one element: _(javascriptallonge.pdf (source-range-7239e085-00847))_


## Technical atoms

### Technical frame 1: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00442))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00439))_

<a id="atom-technical-atom-179dd365e9382c9f"></a>

```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else
return !even(x - 1);
}
return even(n)
}
```

### Technical frame 2: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00446))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00443))_

<a id="atom-technical-atom-208e7e2794c15225"></a>

```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else {
const odd = (y) => !even(y);
return odd(x - 1);
}
```

### Technical frame 3: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00446))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00444))_

<a id="atom-technical-atom-a4ff91c073865533"></a>

```
}
return even(n)
}
And this also works:
((n) => {
const even = (x) => {
if (x === 0)
return true;
else {
const odd = (y) => !even(y);
return odd(x - 1);
}
}
return even(n)
})(42)
```

### Technical frame 4: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00446))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00445))_

<a id="atom-technical-atom-4bfc4e7c5cb8ba29"></a>

```
//=> true
```

### Technical frame 5: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00482))_

<a id="atom-technical-atom-2dde6743679c8a4b"></a>

```
if (true) {
// an immediately invoked block statement (IIBS)
}
Let’s try it:
((diameter) => {
const PI = 3;
if (true) {
const PI = 3.14159265;
return diameter * PI;
}
})(2)
//=> 6.2831853
((diameter) => {
const PI = 3.14159265;
if (true) {
const PI = 3;
}
return diameter * PI;
```

### Technical frame 6: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00483))_

<a id="atom-technical-atom-bdd5dd7c22cb3cef"></a>

```
})(2)
//=> 6.2831853
```

### Technical frame 7: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

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

### Technical frame 8: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

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

### Technical frame 9: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00847))_

> The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do the same thing with more than one element:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00846))_

<a id="atom-technical-atom-617a6d44b48762af"></a>

```
const unwrap = (wrapped) => {
const [something] = wrapped;
return something;
}
unwrap(["present"])
//=> "present"
```

### Technical frame 10: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00849))_

> We could do the same thing with (name) => name[1] , but destructuring is code that resembles the data it consumes, a valuable coding style.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00848))_

<a id="atom-technical-atom-5a199409712df05d"></a>

```
const surname = (name) => {
const [first, last] = name;
return last;
}
surname(["Reginald", "Braithwaite"])
//=> "Braithwaite"
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from And also: / That Constant Coffee Craving / nested blocks: (n) => { const even = (x) => { if (x === 0) return true; else return !even(x - 1); } return even(n) } (5 shared atom(s))
- [[javascriptallonge-block]] - shared statements and technical atoms: Block shares source evidence from And also: / Summary / Functions: Blocks also create scopes if const statements are within them.; Block shares technical record from And also: / That Constant Coffee Craving / nested blocks: (n) => { const even = (x) => { if (x === 0) return true; else return !even(x - 1); } return even(n) } (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from And also: / That Constant Coffee Craving / nested blocks: (n) => { const even = (x) => { if (x === 0) return true; else { const odd = (y) => !even(y); return odd(x - 1); } (3 shared atom(s))
- [[javascriptallonge-seen]] - shared technical atoms: Seen shares technical record from And also: / That Constant Coffee Craving / nested blocks: (n) => { const even = (x) => { if (x === 0) return true; else return !even(x - 1); } return even(n) } (3 shared atom(s))
- [[javascriptallonge-environment]] - shared technical atoms: Environment shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: ((diameter) => { const PI = 3.14159265; if (true) { const PI = 3; } return diameter * PI; })(2) //=> would return 6 if const had function scope (2 shared atom(s))
- [[javascriptallonge-parameter]] - shared technical atoms: Parameter shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: if (true) { // an immediately invoked block statement (IIBS) } Let’s try it: ((diameter) => { const PI = 3; if (true) { const PI = 3.14159265; return diameter * PI; ... [truncated] (2 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: ((diameter) => { const PI = 3.14159265; if (true) { const PI = 3; } return diameter * PI; })(2) //=> would return 6 if const had function scope (2 shared atom(s))
- [[javascriptallonge-array]] - shared statements and technical atoms: Array shares source evidence from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays: The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do ... [truncated]; Array shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays: const surname = (name) => { const [first, last] = name; return last; } surname(["Reginald", "Braithwaite"]) //=> "Braithwaite" (1 shared statement(s), 1 shared atom(s))

### Shared claims

- [[javascriptallonge-important]] - shared statements: Important shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / a quick summary of functions and bodies: One of the important possible statements is a return statement. A return statement accepts any valid JavaScript expression. (1 shared statement(s))

## Source

- [[javascriptallonge]]
