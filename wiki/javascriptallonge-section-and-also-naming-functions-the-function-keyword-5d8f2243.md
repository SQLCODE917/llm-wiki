---
page_id: javascriptallonge-section-and-also-naming-functions-the-function-keyword-5d8f2243
page_kind: source
page_family: section-reference
summary: And also: / Naming Functions / the function keyword: 31 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-naming-functions-the-function-keyword-5d8f2243@83bf53aa8c1afdd207bfdc8f4e7dd53e
---

# And also: / Naming Functions / the function keyword

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-and-also-naming-functions-37c9be8d]] - broader source section: And also: / Naming Functions

### Topics

- [[javascriptallonge-function-keyword]] - topic hub: opens the topic page for Function Keyword

### Other

- [[javascriptallonge-section-and-also-magic-names-the-function-keyword-b8eb1a25]] - same source heading: another source section with the same heading, And also: / Magic Names / the function keyword

## Statements

- JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-7239e085-00503))_
- Something else we're about to discuss is optional. _(javascriptallonge.pdf (source-range-7239e085-00510))_
- We have arguments in parentheses, just like fat arrow functions. _(javascriptallonge.pdf (source-range-7239e085-00511))_
- We do not have a fat arrow, we go directly to the body. _(javascriptallonge.pdf (source-range-7239e085-00512))_
- We always use a block, we cannot write function (str) str + str . This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-7239e085-00513))_
- In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment. _(javascriptallonge.pdf (source-range-7239e085-00523))_
- 33 'Yes of course?' Well, in chapter of a book dedicated to naming functions, it is not surprising that feature we mention has something to do with naming functions. _(javascriptallonge.pdf (source-range-7239e085-00527))_
- Now, the function's actual name has no effect on the environment in which it is used. To whit: _(javascriptallonge.pdf (source-range-7239e085-00529))_
- So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const : _(javascriptallonge.pdf (source-range-7239e085-00531))_
- Clearly, the name even is bound to the function within the function's body . Is it bound to the function outside of the function's body? _(javascriptallonge.pdf (source-range-7239e085-00533))_
- even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't. _(javascriptallonge.pdf (source-range-7239e085-00535))_
- This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-7239e085-00513))_
- Clearly, the name even is bound to the function within the function's body . _(javascriptallonge.pdf (source-range-7239e085-00533))_

## Technical atoms

### Technical frame 1: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00510))_

> Something else we're about to discuss is optional.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00507))_

<a id="atom-technical-atom-4892b44040deaa12"></a>

```
function (str) { return str + str }
```

### Technical frame 2: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00513))_

> We always use a block, we cannot write function (str) str + str . This means that if we want our functions to return a value, we always need to use the return keyword

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00514))_

<a id="atom-technical-atom-fac43b9adefb942a"></a>

> If we leave out the 'something optional' that comes after the function keyword, we can translate all of the fat arrow functions that we've seen into function keyword functions, e.g.

### Technical frame 3: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00523))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00515))_

<a id="atom-technical-atom-263a35e1362152b8"></a>

```
(n) => (1.618**n - -1.618**-n) / 2.236
```

### Technical frame 4: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00523))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00517))_

<a id="atom-technical-atom-4988f07d229ed38d"></a>

```
function (n) {
return (1.618**n - -1.618**-n) / 2.236;
}
```

### Technical frame 5: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00523))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00522))_

<a id="atom-technical-atom-81cb3037dd7ae143"></a>

```
const double = function repeat (str) {
return str + str;
}
```
