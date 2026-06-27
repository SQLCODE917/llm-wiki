---
page_id: javascriptallonge-section-mutation-e91c1325
page_kind: source
summary: **Mutation**: 27 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-mutation-e91c1325@9c3d68272cfe9ba9c2121b4768855f7c
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

> Context: In JavaScript, almost every type of value can _mutate_ . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using []. You can reassign a value using [] =:
_(context: javascriptallonge.pdf (source-range-83ecb080-01688))_

> **const** oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree _//=> [ 'one', 2, 3 ]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01689))_

> Context: You can even add a value:
_(context: javascriptallonge.pdf (source-range-83ecb080-01690))_

> **const** oneTwoThree = [1, 2, 3]; oneTwoThree[3] = 'four'; oneTwoThree _//=> [ 1, 2, 3, 'four' ]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01693))_

> Context: You can do the same thing with both syntaxes for accessing objects:
_(context: javascriptallonge.pdf (source-range-83ecb080-01694))_

> **const** name = {firstName: 'Leonard', lastName: 'Braithwaite'}; name.middleName = 'Austin' name _//=> { firstName: 'Leonard',_ # lastName: 'Braithwaite', # middleName: 'Austin' }
_(source: javascriptallonge.pdf (source-range-83ecb080-01695))_

> Context: We have established that JavaScript’s semantics allow for two different bindings to refer to the same value. For example:
_(context: javascriptallonge.pdf (source-range-83ecb080-01696))_

> **const** allHallowsEve = [2012, 10, 31] **const** halloween = allHallowsEve;
_(source: javascriptallonge.pdf (source-range-83ecb080-01697))_

> Context: Both halloween and allHallowsEve are bound to the same array value within the local environment. And also: There are two nested environments, and each one binds a name to the exact same array value. In each of these examples, we have created two _aliases_ for the same value. Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value.
_(context: javascriptallonge.pdf (source-range-83ecb080-01698, source-range-83ecb080-01701))_

> **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { _// ..._
_(source: javascriptallonge.pdf (source-range-83ecb080-01699))_

> Context: This is vital. Consider what we already know about shadowing: The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we _mutate_ the value in the inner environment?
_(context: javascriptallonge.pdf (source-range-83ecb080-01702, source-range-83ecb080-01707))_

> **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31];
_(source: javascriptallonge.pdf (source-range-83ecb080-01705))_

> Context: The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we _mutate_ the value in the inner environment?
_(context: javascriptallonge.pdf (source-range-83ecb080-01707))_

> })(allHallowsEve); allHallowsEve _//=> [2012, 10, 31]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01706))_

> **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween[0] = 2013; })(allHallowsEve); allHallowsEve _//=> [2013, 10, 31]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01708))_
