---
page_id: javascriptallonge-recipe-more-generators
page_kind: recipe
page_family: recipe-pattern
summary: more generators: reusable source-backed pattern with 3 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: more-generators
projection_coverage: recipe-javascriptallonge-recipe-more-generators@1fe1d9b5407386c1f680f1a2a1e4c49c
---

# more generators

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-we-ll-keep-it-simple-more-generators-6ce23867]].
- Evidence roles: decision, procedure, example.

## Applicability And Rationale

- Our OneTwoThree example used implicit state to output the numbers in sequence. _(javascriptallonge.pdf (source-range-7239e085-01720))_
- And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own. _(javascriptallonge.pdf (source-range-7239e085-01725))_
- We've writing a function that returns an iterator, but we used a generator to do it. _(javascriptallonge.pdf (source-range-7239e085-01725))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01718)_

```
const Numbers = {
*[Symbol.iterator] () {
let i = 0;
while (true) {
yield i++;
}
}
};
for (const i of Numbers) {
console.log(i);
}
//=>
0
1
2
3
4
5
6
7
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01719)_

```
8
9
10
...
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01721)_

```
const Fibonacci = {
[Symbol.iterator]: () => {
let a = 0, b = 1, state = 0;
return {
next: () => {
switch (state) {
case 0:
state = 1;
return {value: a};
case 1:
state = 2;
return {value: b};
case 2:
[a, b] = [b, a + b];
return {value: b};
}
}
}
}
};
for (let n of Fibonacci) {
console.log(n)
}
//=>
0
1
1
2
3
5
8
13
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01722)_

```
21
34
55
89
144
...
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01724)_

```
const Fibonacci = {
*[Symbol.iterator] () {
let a, b;
yield a = 0;
yield b = 1;
while (true) {
[a, b] = [b, a + b]
yield b;
}
}
}
for (const i of Fibonacci) {
console.log(i);
}
//=>
0
1
1
2
3
5
8
13
21
34
55
89
144
...
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01727)_

```
function * fibonacci () {
let a, b;
yield a = 0;
yield b = 1;
while (true) {
[a, b] = [b, a + b]
yield b;
}
}
for (const i of fibonacci()) {
console.log(i);
}
//=>
0
1
1
2
3
5
8
13
21
34
55
89
144
...
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-we-ll-keep-it-simple-more-generators-6ce23867]]
