---
page_id: javascriptallonge-section-truthiness-and-operators-d8eb6fca
page_kind: source
summary: truthiness and operators: 10 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-truthiness-and-operators-d8eb6fca@1a100849eaa5ec81f9124c5b82c7d6d8
---

# truthiness and operators

From [[javascriptallonge]].

## Statements

- Our logical operators ! , && , and || are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-8eb13d6b-00777))_
- Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user. _(javascriptallonge.pdf (source-range-8eb13d6b-00779))_
- First, and unlike ! , && and || do not necessarily evaluate to true or false . To be precise: _(javascriptallonge.pdf (source-range-8eb13d6b-00781))_
- If we look at our examples above, we see that when we pass true and false to && and || , we do indeed get true or false as a result. But when we pass other values, we no longer get true or false : _(javascriptallonge.pdf (source-range-8eb13d6b-00788))_
- In JavaScript, && and || aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && . _(javascriptallonge.pdf (source-range-8eb13d6b-00790))_
- This is not a subtle distinction. _(javascriptallonge.pdf (source-range-8eb13d6b-00791))_

## Technical atoms

### Technical frame 1: truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00779))_

> Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00778))_

```
!5 //=> false ! undefined //=> true
```

### Technical frame 2: truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00790))_

> In JavaScript, && and || aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00788))_

> But when we pass other values, we no longer get true or false :

### Technical frame 3: truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00790))_

> In JavaScript, && and || aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00789))_

```
1 || 2 //=> 1 null && undefined //=> null undefined && null //=> undefined
```
