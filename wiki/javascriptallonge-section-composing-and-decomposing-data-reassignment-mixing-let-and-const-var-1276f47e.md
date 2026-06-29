---
page_id: javascriptallonge-section-composing-and-decomposing-data-reassignment-mixing-let-and-const-var-1276f47e
page_kind: source
summary: Composing and Decomposing Data / Reassignment / mixing let and const / var: 15 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-reassignment-mixing-let-and-const-var-1276f47e@7271866f9174b91998f07167666fd47f
---

# Composing and Decomposing Data / Reassignment / mixing let and const / var

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-reassignment-mixing-let-and-const-ca678af6]] - broader source section: Composing and Decomposing Data / Reassignment / mixing let and const

## Statements

- JavaScript has one more way to bind a name to a value, var . 71 var looks a lot like let : _(javascriptallonge.pdf (source-range-7239e085-01187))_
- But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations: _(javascriptallonge.pdf (source-range-7239e085-01191))_
- Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations. _(javascriptallonge.pdf (source-range-7239e085-01193))_
- But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. Note this example of a function that uses a helper: _(javascriptallonge.pdf (source-range-7239e085-01194))_
- In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped. _(javascriptallonge.pdf (source-range-7239e085-01200))_
- A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. _(javascriptallonge.pdf (source-range-7239e085-01194))_
- In that way, var is a little like const and let , we should always declare and bind names before using them. _(javascriptallonge.pdf (source-range-7239e085-01200))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Reassignment / mixing let and const / var

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

### Technical frame 2: Composing and Decomposing Data / Reassignment / mixing let and const / var

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

### Technical frame 3: Composing and Decomposing Data / Reassignment / mixing let and const / var

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

### Technical frame 4: Composing and Decomposing Data / Reassignment / mixing let and const / var

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

### Technical frame 5: Composing and Decomposing Data / Reassignment / mixing let and const / var

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

### Technical frame 6: Composing and Decomposing Data / Reassignment / mixing let and const / var

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

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01333))_

> The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01335))_

| entry | content |
| --- | --- |
| 76 | http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422 |
| 77 | http://oscin.es |

<details>
<summary>Raw table text</summary>

```
76 http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422
77 http://oscin.es
```

</details>
