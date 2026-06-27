---
page_id: javascriptallonge-section-mutation-e91c1325
page_kind: source
summary: **Mutation**: 27 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-mutation-e91c1325@cb2e6b06b7bed4fd1236b62cd3bc5dcc
---

# **Mutation**

From [[javascriptallonge]].

## Statements

- Recall that you can access a value from within an array or an object using []. _(javascriptallonge.pdf (source-range-83ecb080-01688))_
- Specifically, arrays and objects can mutate. _(javascriptallonge.pdf (source-range-83ecb080-01688))_
- In JavaScript, almost every type of value can _mutate_ . _(javascriptallonge.pdf (source-range-83ecb080-01688))_
- Recall that you can access a value from within an array or an object using []. _(javascriptallonge.pdf (source-range-83ecb080-01688))_
- We have established that JavaScript’s semantics allow for two different bindings to refer to the same value. _(javascriptallonge.pdf (source-range-83ecb080-01696))_
- Both halloween and allHallowsEve are bound to the same array value within the local environment. _(javascriptallonge.pdf (source-range-83ecb080-01698))_
- Both halloween and allHallowsEve are bound to the same array value within the local environment. _(javascriptallonge.pdf (source-range-83ecb080-01698))_
- There are two nested environments, and each one binds a name to the exact same array value. _(javascriptallonge.pdf (source-range-83ecb080-01701))_
- Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value. _(javascriptallonge.pdf (source-range-83ecb080-01701))_
- In each of these examples, we have created two _aliases_ for the same value. _(javascriptallonge.pdf (source-range-83ecb080-01701))_
- Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value. _(javascriptallonge.pdf (source-range-83ecb080-01701))_
- The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. _(javascriptallonge.pdf (source-range-83ecb080-01707))_
- The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. _(javascriptallonge.pdf (source-range-83ecb080-01707))_
- We haven’t rebound the inner name to a different variable, we’ve mutated the value that both bindings share. _(javascriptallonge.pdf (source-range-83ecb080-01709))_
- Now that we’ve finished with mutation and aliases, let’s have a look at it. _(javascriptallonge.pdf (source-range-83ecb080-01709))_
- Mutating existing objects has special implications when two bindings are aliases of the same value. _(javascriptallonge.pdf (source-range-83ecb080-01711))_
- JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects. _(javascriptallonge.pdf (source-range-83ecb080-01711))_
- Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. _(javascriptallonge.pdf (source-range-83ecb080-01713))_
- Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. _(javascriptallonge.pdf (source-range-83ecb080-01713))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01688))_

> In JavaScript, almost every type of value can _mutate_ . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using []. You can reassign a value using [] =:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01689))_

> **const** oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree _//=> [ 'one', 2, 3 ]_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01690))_

> You can even add a value:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01693))_

> **const** oneTwoThree = [1, 2, 3]; oneTwoThree[3] = 'four'; oneTwoThree _//=> [ 1, 2, 3, 'four' ]_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01694))_

> You can do the same thing with both syntaxes for accessing objects:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01695))_

> **const** name = {firstName: 'Leonard', lastName: 'Braithwaite'}; name.middleName = 'Austin' name _//=> { firstName: 'Leonard',_ # lastName: 'Braithwaite', # middleName: 'Austin' }

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01696))_

> We have established that JavaScript’s semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01697))_

> **const** allHallowsEve = [2012, 10, 31] **const** halloween = allHallowsEve;

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01698, source-range-83ecb080-01701))_

> Both halloween and allHallowsEve are bound to the same array value within the local environment. And also: There are two nested environments, and each one binds a name to the exact same array value. In each of these examples, we have created two _aliases_ for the same value. Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01699))_

> **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { _// ..._

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01702, source-range-83ecb080-01707))_

> This is vital. Consider what we already know about shadowing: The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we _mutate_ the value in the inner environment?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01705))_

> **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31];

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01707))_

> The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we _mutate_ the value in the inner environment?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01706))_

> })(allHallowsEve); allHallowsEve _//=> [2012, 10, 31]_

### Technical atom 8

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01708))_

> **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween[0] = 2013; })(allHallowsEve); allHallowsEve _//=> [2013, 10, 31]_
