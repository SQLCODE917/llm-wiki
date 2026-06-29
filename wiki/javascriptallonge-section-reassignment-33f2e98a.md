---
page_id: javascriptallonge-section-reassignment-33f2e98a
page_kind: source
summary: Reassignment: 16 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-reassignment-33f2e98a@3d93a328e3a1e188efdf19d00b4178f9
---

# Reassignment

From [[javascriptallonge]].

## Statements

- Like some imperative programming languages, JavaScript allows you to re-assign the value bound to parameters. We saw this earlier in rebinding: _(javascriptallonge.pdf (source-range-8eb13d6b-01161))_
- JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-8eb13d6b-01166))_
- Rebinding parameters is usually avoided, but what about rebinding names we declare within a function? What we want is a statement that works like const , but permits us to rebind variables. JavaScript has such a thing, it's called let : _(javascriptallonge.pdf (source-range-8eb13d6b-01167))_
- We took the time to carefully examine what happens with bindings in environments. Let's take the time to explore what happens with reassigning values to variables. The key is to understand that we are rebinding a different value to the same name in the same environment. _(javascriptallonge.pdf (source-range-8eb13d6b-01169))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . We go from: _(javascriptallonge.pdf (source-range-8eb13d6b-01172))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment. _(javascriptallonge.pdf (source-range-8eb13d6b-01177))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . _(javascriptallonge.pdf (source-range-8eb13d6b-01172))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. _(javascriptallonge.pdf (source-range-8eb13d6b-01177))_

## Technical atoms

### Technical frame 1: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01166))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01163))_

```
const evenStevens = (n) => { if (n === 0) { return true ; } else if (n == 1) { return false ; } else { n = n - 2; return evenStevens(n); } } evenStevens(42) //=> true
```

### Technical frame 2: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01166))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01165))_

```
evenStevens = (n) => { if (n === 0) { return true ; } else if (n == 1) { return false ; } else { return evenStevens(n - 2); } } //=> ERROR, evenStevens is read-only
```

### Technical frame 3: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01169))_

> We took the time to carefully examine what happens with bindings in environments. Let's take the time to explore what happens with reassigning values to variables. The key is to understand that we are rebinding a different value to the same name in the same environment.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01168))_

```
let age = 52; age = 53; age //=> 53
```

### Technical frame 4: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01172))_

> Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . We go from:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01171))_

```
(() => { let age = 49; if ( true ) { let age = 50; } return age; })() //=> 49
```

### Technical frame 5: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01177))_

> Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01173))_

```
{age: 49, '..': global-environment} To: {age: 50, '..': {age: 49, '..': global-environment}} Then back to:
```

### Technical frame 6: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01177))_

> Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01174))_

```
{age: 49, '..': global-environment}
```

### Technical frame 7: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01177))_

> Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01176))_

```
(() => { let age = 49; if ( true ) { age = 50; } return age; })() //=> 50
```
