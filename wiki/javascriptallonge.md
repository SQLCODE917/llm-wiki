---
page_id: javascriptallonge
page_kind: source
summary: Claim-ledger projection (coding): 2043 usable entries, 543 technical atoms, 666 needs-review, 290 linked page(s); write decision write-with-review-work.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources
source_id: javascriptallonge.pdf
projection_coverage: projection-coverage-a340d05e25ddb511@2df79515e39ca172
---

# Document

## Document

### Reg “raganwald” Braithwaite

- How to Do What You Love & Earn What You’re Worth as a Programmer _(javascriptallonge.pdf (source-range-83ecb080-00011))_

> This version was published on 2017-11-03
_(source: javascriptallonge.pdf (source-range-83ecb080-00005))_

> Context: This is a Leanpub book. Leanpub empowers authors and publishers with the Lean Publishing process. Lean Publishing is the act of publishing an in-progress ebook using lightweight tools and many iterations to get reader feedback, pivot until you have the right book and build traction once you do.
_(context: javascriptallonge.pdf (source-range-83ecb080-00007))_

> © 2015 - 2017 Reg “raganwald” Braithwaite
_(source: javascriptallonge.pdf (source-range-83ecb080-00008))_

## Table of Contents

### **Contents**

| **A Pull of the Lever: Prefaces** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | **i** |
| --- | --- |
| About JavaScript Allongé . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ii |
| What JavaScript Allongé is. And isn’t. . . . . . . . . . . . . . . . . . . . . . . . . . . . . | v |
| Foreword to the “Six” edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | viii |
| Forewords to the First Edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ix |
| About The Sample PDF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xi |
| **Prelude: Values and Expressions over Coffee**<br>. . . . . . . . . . . . . . . . . . . . . . . . . | **xiii** |
| values are expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xiv |
| values and identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xvi |
| **A Rich Aroma: Basic Numbers** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | **1** |
| **The first sip: Basic Functions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | **5** |
| As Little As Possible About Functions, But No Less . . . . . . . . . . . . . . . . . . . . . | 7 |
| Ah. I’d Like to Have an Argument, Please. . . . . . . . . . . . . . . . . . . . . . . . . . . | 16 |
| Closures and Scope<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 21 |
| That Constant Coffee Craving<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 26 |
| Naming Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 39 |
| Combinators and Function Decorators . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 45 |
| Building Blocks<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 48 |
| Magic Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 51 |
| Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 55 |
| **Recipes with Basic Functions**<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | **56** |
| Partial Application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 57 |
| Unary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 59 |
| Tap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 61 |
| Maybe<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 63 |
| Once . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 65 |
| Left-Variadic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 66 |
| **Picking the Bean: Choice and Truthiness** . . . . . . . . . . . . . . . . . . . . . . . . . . . . | **71** |

<details>
<summary>Raw table text</summary>

```
|**A Pull of the Lever: Prefaces** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|**i**|
|---|---|
|About JavaScript Allongé . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|ii|
|What JavaScript Allongé is. And isn’t. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|v|
|Foreword to the “Six” edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|viii|
|Forewords to the First Edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|ix|
|About The Sample PDF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|xi|
|**Prelude: Values and Expressions over Coffee**<br>. . . . . . . . . . . . . . . . . . . . . . . . .|**xiii**|
|values are expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|xiv|
|values and identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|xvi|
|**A Rich Aroma: Basic Numbers** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|**1**|
|**The first sip: Basic Functions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|**5**|
|As Little As Possible About Functions, But No Less . . . . . . . . . . . . . . . . . . . . .|7|
|Ah. I’d Like to Have an Argument, Please. . . . . . . . . . . . . . . . . . . . . . . . . . .|16|
|Closures and Scope<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|21|
|That Constant Coffee Craving<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|26|
|Naming Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|39|
|Combinators and Function Decorators . . . . . . . . . . . . . . . . . . . . . . . . . . . .|45|
|Building Blocks<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|48|
|Magic Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|51|
|Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|55|
|**Recipes with Basic Functions**<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|**56**|
|Partial Application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|57|
|Unary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|59|
|Tap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|61|
|Maybe<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|63|
|Once . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|65|
|Left-Variadic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|66|
|**Picking the Bean: Choice and Truthiness** . . . . . . . . . . . . . . . . . . . . . . . . . . . .|**71**|
```

</details>
_(source: javascriptallonge.pdf (source-range-83ecb080-00016))_

| A Pull of the Lever: Prefaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | i |
| --- | --- |
| About JavaScript Allongé . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ii |
| What JavaScript Allongé is. And isn’t. . . . . . . . . . . . . . . . . . . . . . . . . . . . . | v |
| Foreword to the “Six” edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | viii |
| Forewords to the First Edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ix |
| About The Sample PDF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xi |
| Prelude: Values and Expressions over Coffee . . . . . . . . . . . . . . . . . . . . . . . . . | xiii |
| values are expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xiv |
| values and identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xvi |
| A Rich Aroma: Basic Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 1 |
| The first sip: Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 5 |
| As Little As Possible About Functions, But No Less . . . . . . . . . . . . . . . . . . . . . | 7 |
| Ah. I’d Like to Have an Argument, Please. . . . . . . . . . . . . . . . . . . . . . . . . . . | 16 |
| Closures and Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 21 |
| That Constant Coffee Craving . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 26 |
| Naming Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 39 |
| Combinators and Function Decorators . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 45 |
| Building Blocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 48 |
| Magic Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 51 |
| Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 55 |
| Recipes with Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 56 |
| Partial Application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 57 |
| Unary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 59 |
| Tap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 61 |
| Maybe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 63 |
| Once . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 65 |
| Left-Variadic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 66 |
| Picking the Bean: Choice and Truthiness . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 71 |

<details>
<summary>Raw table text</summary>

```
| A Pull of the Lever: Prefaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | i |
| --- | --- |
| About JavaScript Allongé . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ii |
| What JavaScript Allongé is. And isn’t. . . . . . . . . . . . . . . . . . . . . . . . . . . . . | v |
| Foreword to the “Six” edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | viii |
| Forewords to the First Edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ix |
| About The Sample PDF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xi |
| Prelude: Values and Expressions over Coffee . . . . . . . . . . . . . . . . . . . . . . . . . | xiii |
| values are expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xiv |
| values and identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xvi |
| A Rich Aroma: Basic Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 1 |
| The first sip: Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 5 |
| As Little As Possible About Functions, But No Less . . . . . . . . . . . . . . . . . . . . . | 7 |
| Ah. I’d Like to Have an Argument, Please. . . . . . . . . . . . . . . . . . . . . . . . . . . | 16 |
| Closures and Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 21 |
| That Constant Coffee Craving . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 26 |
| Naming Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 39 |
| Combinators and Function Decorators . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 45 |
| Building Blocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 48 |
| Magic Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 51 |
| Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 55 |
| Recipes with Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 56 |
| Partial Application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 57 |
| Unary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 59 |
| Tap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 61 |
| Maybe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 63 |
| Once . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 65 |
| Left-Variadic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 66 |
| Picking the Bean: Choice and Truthiness . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 71 |
```

</details>
_(source: javascriptallonge.pdf (source-range-83ecb080-00017))_

### CONTENTS

| **Composing and Decomposing Data** . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | **77** |
| --- | --- | --- |
| Arrays and Destructuring Arguments<br>. . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 78 |
| Self-Similarity . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 86 |
| Tail Calls (and Default Arguments) . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 94 |
| Garbage, Garbage Everywhere . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 103 |
| Plain Old JavaScript Objects<br>. . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 109 |
| Mutation . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 118 |
| Reassignment<br>. . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 125 |
| Copy on Write . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 135 |
| Tortoises, Hares, and Teleporting Turtles . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 141 |
| Functional Iterators . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 144 |
| Making Data Out Of Functions . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 154 |
| **Recipes with Data** . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | **168** |
| mapWith . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 170 |
| Flip . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 172 |
| Object.assign . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 175 |
| Why? . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 178 |
| **A Warm Cup: Basic Strings and Quasi-Literals** | . . . . . . . . . . . . . . . . . . . . . . . . | **179** |
| **Served by the Pot: Collections** . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | **182** |
| Iteration and Iterables . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 183 |
| Generating Iterables . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 201 |
| Lazy and Eager Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 223 |
| Interlude: The Carpenter Interviews for a Job | . . . . . . . . . . . . . . . . . . . . . . . . | 238 |
| Interactive Generators . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 250 |
| Basic Operations on Iterables . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 261 |
| **The Golden Crema: Appendices and Afterwords** | . . . . . . . . . . . . . . . . . . . . . . . | **265** |
| How to run the examples . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 266 |
| Thanks! . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 268 |
| Copyright Notice . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 270 |
| About The Author . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 274 |

<details>
<summary>Raw table text</summary>

```
|**Composing and Decomposing Data** . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|**77**|
|---|---|---|
|Arrays and Destructuring Arguments<br>. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|78|
|Self-Similarity . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|86|
|Tail Calls (and Default Arguments) . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|94|
|Garbage, Garbage Everywhere . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|103|
|Plain Old JavaScript Objects<br>. . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|109|
|Mutation . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|118|
|Reassignment<br>. . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|125|
|Copy on Write . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|135|
|Tortoises, Hares, and Teleporting Turtles . . .|. . . . . . . . . . . . . . . . . . . . . . . .|141|
|Functional Iterators . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|144|
|Making Data Out Of Functions . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|154|
|**Recipes with Data** . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|**168**|
|mapWith . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|170|
|Flip . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|172|
|Object.assign . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|175|
|Why? . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|178|
|**A Warm Cup: Basic Strings and Quasi-Literals**|. . . . . . . . . . . . . . . . . . . . . . . .|**179**|
|**Served by the Pot: Collections** . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|**182**|
|Iteration and Iterables . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|183|
|Generating Iterables . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|201|
|Lazy and Eager Collections . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|223|
|Interlude: The Carpenter Interviews for a Job|. . . . . . . . . . . . . . . . . . . . . . . .|238|
|Interactive Generators . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|250|
|Basic Operations on Iterables . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|261|
|**The Golden Crema: Appendices and Afterwords**|. . . . . . . . . . . . . . . . . . . . . . .|**265**|
|How to run the examples . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|266|
|Thanks! . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|268|
|Copyright Notice . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|270|
|About The Author . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|274|
```

</details>
_(source: javascriptallonge.pdf (source-range-83ecb080-00019))_

| Composing and Decomposing Data . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 77 |
| --- | --- | --- |
| Arrays and Destructuring Arguments . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 78 |
| Self-Similarity . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 86 |
| Tail Calls (and Default Arguments) . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 94 |
| Garbage, Garbage Everywhere . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 103 |
| Plain Old JavaScript Objects . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 109 |
| Mutation . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 118 |
| Reassignment . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 125 |
| Copy on Write . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 135 |
| Tortoises, Hares, and Teleporting Turtles . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 141 |
| Functional Iterators . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 144 |
| Making Data Out Of Functions . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 154 |
| Recipes with Data . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 168 |
| mapWith . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 170 |
| Flip . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 172 |
| Object.assign . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 175 |
| Why? . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 178 |
| A Warm Cup: Basic Strings and Quasi-Literals | . . . . . . . . . . . . . . . . . . . . . . . . | 179 |
| Served by the Pot: Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 182 |
| Iteration and Iterables . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 183 |
| Generating Iterables . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 201 |
| Lazy and Eager Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 223 |
| Interlude: The Carpenter Interviews for a Job | . . . . . . . . . . . . . . . . . . . . . . . . | 238 |
| Interactive Generators . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 250 |
| Basic Operations on Iterables . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 261 |
| The Golden Crema: Appendices and Afterwords | . . . . . . . . . . . . . . . . . . . . . . . | 265 |
| How to run the examples . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 266 |
| Thanks! . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 268 |
| Copyright Notice . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 270 |
| About The Author . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 274 |

<details>
<summary>Raw table text</summary>

```
| Composing and Decomposing Data . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 77 |
| --- | --- | --- |
| Arrays and Destructuring Arguments . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 78 |
| Self-Similarity . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 86 |
| Tail Calls (and Default Arguments) . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 94 |
| Garbage, Garbage Everywhere . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 103 |
| Plain Old JavaScript Objects . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 109 |
| Mutation . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 118 |
| Reassignment . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 125 |
| Copy on Write . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 135 |
| Tortoises, Hares, and Teleporting Turtles . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 141 |
| Functional Iterators . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 144 |
| Making Data Out Of Functions . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 154 |
| Recipes with Data . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 168 |
| mapWith . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 170 |
| Flip . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 172 |
| Object.assign . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 175 |
| Why? . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 178 |
| A Warm Cup: Basic Strings and Quasi-Literals | . . . . . . . . . . . . . . . . . . . . . . . . | 179 |
| Served by the Pot: Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 182 |
| Iteration and Iterables . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 183 |
| Generating Iterables . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 201 |
| Lazy and Eager Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 223 |
| Interlude: The Carpenter Interviews for a Job | . . . . . . . . . . . . . . . . . . . . . . . . | 238 |
| Interactive Generators . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 250 |
| Basic Operations on Iterables . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 261 |
| The Golden Crema: Appendices and Afterwords | . . . . . . . . . . . . . . . . . . . . . . . | 265 |
| How to run the examples . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 266 |
| Thanks! . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 268 |
| Copyright Notice . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 270 |
| About The Author . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 274 |
```

</details>
_(source: javascriptallonge.pdf (source-range-83ecb080-00020))_

## A Pull of the Lever: Prefaces

### **A Pull of the Lever: Prefaces**

- Some complain that the long pull is more bitter and detracts from the best character of the coffee, others feel it releases even more complexity. _(javascriptallonge.pdf (source-range-83ecb080-00026))_

## About JavaScript Allongé

### **About JavaScript Allongé**

- JavaScript Allongé is a first and foremost, a book about _programming with functions_ . _(javascriptallonge.pdf (source-range-83ecb080-00032))_
- It’s written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope. _(javascriptallonge.pdf (source-range-83ecb080-00032))_
- It’s written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope. _(javascriptallonge.pdf (source-range-83ecb080-00032))_
- _JavaScript Allongé_ begins at the beginning, with values and expressions, and builds from there to discuss types, identity, functions, closures, scopes, collections, iterators, and many more subjects up to working with classes and instances. _(javascriptallonge.pdf (source-range-83ecb080-00033))_
- JavaScript idioms like function combinators and decorators leverage JavaScript’s power to make code easier to read, modify, debug and refactor. _(javascriptallonge.pdf (source-range-83ecb080-00034))_
- It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or code-centric. _(javascriptallonge.pdf (source-range-83ecb080-00034))_

> If those terms seem unfamiliar, don’t worry: JavaScript Allongé takes great delight in explaining what they mean and why they matter.
_(source: javascriptallonge.pdf (source-range-83ecb080-00032))_

### **why the “six” edition?**

- Features like destructuring, block-structured variables, iterables, generators, and the class keyword are poised to make JavaScript programming more expressive. _(javascriptallonge.pdf (source-range-83ecb080-00037))_
- ECMAScript 2015 (formerly called ECMAScript 6 or “ES6”), is ushering in a very large number of improvements to the way programmers can write small, powerful components and combine them into larger, fully featured programs. _(javascriptallonge.pdf (source-range-83ecb080-00037))_
- Over time, programmers discovered ways to roll their own versions of important features. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- For example, JavaScript did not include block-structured variables. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- For example, JavaScript did not include block-structured variables. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- And the variable i is scoped locally to the code within the braces. _(javascriptallonge.pdf (source-range-83ecb080-00043))_
- Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-83ecb080-00043))_
- And the variable i is scoped locally to the code within the braces. _(javascriptallonge.pdf (source-range-83ecb080-00043))_
- Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-83ecb080-00043))_
- Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. _(javascriptallonge.pdf (source-range-83ecb080-00049))_
- Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like: _(javascriptallonge.pdf (source-range-83ecb080-00051))_
- Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like: _(javascriptallonge.pdf (source-range-83ecb080-00051))_
- The first edition of JavaScript Allongé explained these and many other patterns for writing flexible and composable programs in JavaScript, but the intention wasn’t to explain how to work around JavaScript’s missing features: The intention was to explain why the style of programming exemplified by the missing features is important. _(javascriptallonge.pdf (source-range-83ecb080-00053))_
- Working around the missing features was a necessary evil. _(javascriptallonge.pdf (source-range-83ecb080-00054))_
- But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. _(javascriptallonge.pdf (source-range-83ecb080-00055))_
- But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. _(javascriptallonge.pdf (source-range-83ecb080-00055))_
- And i is scoped to the for loop. _(javascriptallonge.pdf (source-range-83ecb080-00057))_
- Not having to work around these kinds of missing features makes JavaScript Allongé a _better book_ , because it can focus on the _why_ to do something and _when_ to do it, instead of on the how to make it work _(javascriptallonge.pdf (source-range-83ecb080-00062))_
- Not having to work around these kinds of missing features makes JavaScript Allongé a _better book_ , because it can focus on the _why_ to do something and _when_ to do it, instead of on the how to make it work _(javascriptallonge.pdf (source-range-83ecb080-00062))_
- JavaScript Allongé, The “Six” Edition packs all the goodness of JavaScript Allongé into a new, updated package that is relevant for programmers working with (or planning to work with) the latest version of JavaScript. _(javascriptallonge.pdf (source-range-83ecb080-00063))_

> Context: For example, block-structured languages allow us to write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00039))_

> **for** ( **int** i = 0; i < array.length; ++i) {
_(source: javascriptallonge.pdf (source-range-83ecb080-00040))_

> **for** (i = 0; i < array.length; ++i) { ( **function** (i) { _// ..._ })(i) }
_(source: javascriptallonge.pdf (source-range-83ecb080-00047))_

> Context: Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like:
_(context: javascriptallonge.pdf (source-range-83ecb080-00051))_

> **function** foo () { **var** first = arguments[0], rest = [].slice.call(arguments, 1); _// ..._ }
_(source: javascriptallonge.pdf (source-range-83ecb080-00052))_

> Context: But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. With ECMASCript 2015, we can write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00055))_

> **for** ( **let** i = 0; i < array.length; ++i) { _// ..._ }
_(source: javascriptallonge.pdf (source-range-83ecb080-00056))_

### **that’s nice. is that the only reason?**

- It would have continued to say much the same things, only with new syntax. _(javascriptallonge.pdf (source-range-83ecb080-00066))_
- If it were just a matter of updating the syntax, the original version of JavaScript Allongé could have simply iterated, slowly replacing old syntax with new. _(javascriptallonge.pdf (source-range-83ecb080-00066))_
- It would have continued to say much the same things, only with new syntax. _(javascriptallonge.pdf (source-range-83ecb080-00066))_
- The original JavaScript Allongé was not just written to teach JavaScript: It was written to describe certain ideas in programming: Working with small, independent entities that compose together to make bigger programs. _(javascriptallonge.pdf (source-range-83ecb080-00067))_
- Thus, the focus on things like writing decorators. _(javascriptallonge.pdf (source-range-83ecb080-00067))_
- As noted above, JavaScript was chosen as the language for Allongé because it hit a sweet spot of having a large audience of programmers and having certain language features that happen to work well with this style of programming. _(javascriptallonge.pdf (source-range-83ecb080-00068))_
- As noted above, JavaScript was chosen as the language for Allongé because it hit a sweet spot of having a large audience of programmers and having certain language features that happen to work well with this style of programming. _(javascriptallonge.pdf (source-range-83ecb080-00068))_
- It makes a number of interesting programming techniques easy to explain and easy to use. _(javascriptallonge.pdf (source-range-83ecb080-00069))_
- ECMAScript 2015 does more than simply update the language with some simpler syntax for a few things and help us avoid warts. _(javascriptallonge.pdf (source-range-83ecb080-00069))_
- But the common thread that runs through all these things is that since they are all simple objects and simple functions, we can use the same set of “programming with functions” techniques to build programs by composing small, flexible, and decoupled entities. _(javascriptallonge.pdf (source-range-83ecb080-00070))_
- Thus, the “six” edition introduces classes and mixins. _(javascriptallonge.pdf (source-range-83ecb080-00070))_
- But even so, in a way it is still explaining the exact same original idea that programs are built out of small, flexible functions composed together. _(javascriptallonge.pdf (source-range-83ecb080-00072))_
- And introducing these new ideas did add substantially to its bulk. _(javascriptallonge.pdf (source-range-83ecb080-00072))_
- Introducing so many new ideas did require a major rethink of the way the book was organized. _(javascriptallonge.pdf (source-range-83ecb080-00072))_

## What JavaScript Allongé is. And isn't.

### **What JavaScript Allongé is. And isn’t.**

- JavaScript Allongé is a book about programming with functions. _(javascriptallonge.pdf (source-range-83ecb080-00079))_
- The focus in this book on the underlying ideas, what we might call the fundamentals, and how they combine to form new ideas. _(javascriptallonge.pdf (source-range-83ecb080-00080))_
- The intention is to improve the way we think about programs. _(javascriptallonge.pdf (source-range-83ecb080-00080))_
- There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others. _(javascriptallonge.pdf (source-range-83ecb080-00081))_
- But while JavaScript Allongé attempts to be provocative, it is not _prescriptive_ . _(javascriptallonge.pdf (source-range-83ecb080-00081))_
- There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others. _(javascriptallonge.pdf (source-range-83ecb080-00081))_
- Choices in development are often driven by social considerations. _(javascriptallonge.pdf (source-range-83ecb080-00082))_
- Software development is a complex field. _(javascriptallonge.pdf (source-range-83ecb080-00082))_
- People often say that software should be written for people to read. _(javascriptallonge.pdf (source-range-83ecb080-00082))_
- Choices in software development are also often driven by requirements specific to the type of software being developed. _(javascriptallonge.pdf (source-range-83ecb080-00083))_
- For example, business software written in-house has a very different set of requirements than a library written to be publicly distributed as open-source. _(javascriptallonge.pdf (source-range-83ecb080-00083))_
- For example, business software written in-house has a very different set of requirements than a library written to be publicly distributed as open-source. _(javascriptallonge.pdf (source-range-83ecb080-00083))_
- If a particular codebase is written with lots of helper functions that place the subject first, like this: _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- Choices in software development must also consider the question of consistency. _(javascriptallonge.pdf (source-range-83ecb080-00086))_
- Then it can be jarring to add new helpers written that place the verb first, like this: _(javascriptallonge.pdf (source-range-83ecb080-00088))_
- Then it can be jarring to add new helpers written that place the verb first, like this: _(javascriptallonge.pdf (source-range-83ecb080-00088))_
- Debuggers encourage the use of functions with explicit or implicit names. _(javascriptallonge.pdf (source-range-83ecb080-00091))_
- Finally, choices in software development cannot ignore the tooling that is used to create and maintain software. _(javascriptallonge.pdf (source-range-83ecb080-00091))_
- Continuous integration encourages the creation of software in tandem with and factored to facilitate the creation of automated test suites. _(javascriptallonge.pdf (source-range-83ecb080-00091))_
- The use of linters[1] makes checking for certain types of undesirable code very cheap. _(javascriptallonge.pdf (source-range-83ecb080-00091))_
- The use of source-code control systems with integrated diffing rewards making certain types of focused changes. _(javascriptallonge.pdf (source-range-83ecb080-00091))_
- JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn’t a book about practicing, it’s a book about thinking. _(javascriptallonge.pdf (source-range-83ecb080-00092))_
- JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn’t a book about practicing, it’s a book about thinking. _(javascriptallonge.pdf (source-range-83ecb080-00092))_

> Context: Choices in software development must also consider the question of consistency. If a particular codebase is written with lots of helper functions that place the subject first, like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-00086))_

> **const** mapWith = (iterable, fn) => ({ [Symbol.iterator]: **function** * () { **for** ( **let** element **of** iterable) { **yield** fn(element); } } });
_(source: javascriptallonge.pdf (source-range-83ecb080-00087))_

### **how this book is organized**

- Code examples within each chapter are small and emphasize exposition rather than serving as patterns for everyday use. _(javascriptallonge.pdf (source-range-83ecb080-00094))_
- Code examples within each chapter are small and emphasize exposition rather than serving as patterns for everyday use. _(javascriptallonge.pdf (source-range-83ecb080-00094))_
- While the content of each chapter builds naturally on what was discussed in the previous chapter, the recipes may draw upon any aspect of the JavaScript programming language. _(javascriptallonge.pdf (source-range-83ecb080-00098))_
- Following some of the chapters are a series of recipes designed to show the application of the chapter’s ideas in practical form. _(javascriptallonge.pdf (source-range-83ecb080-00098))_

## Foreword to the ``Six'' edition

### **Foreword to the “Six” edition**

- That version was planned to have numerous new features (interfaces, namespaces, packages, multimethods, etc.), which would have turned JavaScript into a completely new language. _(javascriptallonge.pdf (source-range-83ecb080-00103))_
- After internal conflict, a settlement was reached in July 2008 and a new plan was made – to abandon ECMAScript 4 and to replace it with two upgrades: _(javascriptallonge.pdf (source-range-83ecb080-00103))_
- Getting there took a while – in a way, the origins of ES6 date back to the year 2000: After ECMAScript 3 was finished, TC39 (the committee evolving JavaScript) started to work on ECMAScript 4. _(javascriptallonge.pdf (source-range-83ecb080-00103))_
- ECMAScript 6 (short name: ES6; official name: ECMAScript 2015) was ratified as a standard on June 17. _(javascriptallonge.pdf (source-range-83ecb080-00103))_
- After internal conflict, a settlement was reached in July 2008 and a new plan was made – to abandon ECMAScript 4 and to replace it with two upgrades: _(javascriptallonge.pdf (source-range-83ecb080-00103))_
- Getting there took a while – in a way, the origins of ES6 date back to the year 2000: After ECMAScript 3 was finished, TC39 (the committee evolving JavaScript) started to work on ECMAScript 4. _(javascriptallonge.pdf (source-range-83ecb080-00103))_
- - A smaller upgrade would bring a few minor enhancements to ECMAScript 3. _(javascriptallonge.pdf (source-range-83ecb080-00104))_
- - A larger upgrade would substantially improve JavaScript, but without being as radical as ECMAScript 4. _(javascriptallonge.pdf (source-range-83ecb080-00105))_
- This upgrade became ECMAScript 6 (some features that were initially discussed will show up later, in upcoming ECMAScript versions). _(javascriptallonge.pdf (source-range-83ecb080-00105))_
- For example: classes and modules. _(javascriptallonge.pdf (source-range-83ecb080-00107))_
- For example: Generators, proxies and WeakMaps. _(javascriptallonge.pdf (source-range-83ecb080-00112))_
- And you’ll do so via ES6 code, handed to you in small, easily digestible pieces. _(javascriptallonge.pdf (source-range-83ecb080-00113))_
- With ECMAScript 6, JavaScript has become much larger as a language. _(javascriptallonge.pdf (source-range-83ecb080-00113))_
- You will learn much about functional programming and object-oriented programming. _(javascriptallonge.pdf (source-range-83ecb080-00113))_
- _JavaScript Allongé, the “Six” Edition_ is both a comprehensive tour of its features and a rich collection of techniques for making better use of them. _(javascriptallonge.pdf (source-range-83ecb080-00113))_

## Forewords to the First Edition

### **Forewords to the First Edition**

### **michael fogus**

- However, I’m very conservative about books – let’s just say that if there was an aftershave scented to the essence of “Used Book Store” then I would be first in line to buy. _(javascriptallonge.pdf (source-range-83ecb080-00123))_
- Not only was this a great book, but it was also a great way to write and distribute books. _(javascriptallonge.pdf (source-range-83ecb080-00123))_
- However, Reg sent me a copy of his book and I was humbled. _(javascriptallonge.pdf (source-range-83ecb080-00123))_
- As a life-long bibliophile and long-time follower of Reg’s online work, I was excited when he started writing books. _(javascriptallonge.pdf (source-range-83ecb080-00123))_
- Not only was this a great book, but it was also a great way to write and distribute books. _(javascriptallonge.pdf (source-range-83ecb080-00123))_
- However, I’m very conservative about books – let’s just say that if there was an aftershave scented to the essence of “Used Book Store” then I would be first in line to buy. _(javascriptallonge.pdf (source-range-83ecb080-00123))_
- On more than one occasion I’ve found myself attempting to reify feedback with content that either no longer existed or was changed beyond recognition. _(javascriptallonge.pdf (source-range-83ecb080-00124))_
- The act of writing is an iterative process with (very often) tight revision loops. _(javascriptallonge.pdf (source-range-83ecb080-00124))_
- However, the process of soliciting feedback, gathering responses, sending out copies, waiting for people to actually read it (if they ever do), receiving feedback and then ultimately making sense out of how to use it takes weeks and sometimes months. _(javascriptallonge.pdf (source-range-83ecb080-00124))_
- However, the process of soliciting feedback, gathering responses, sending out copies, waiting for people to actually read it (if they ever do), receiving feedback and then ultimately making sense out of how to use it takes weeks and sometimes months. _(javascriptallonge.pdf (source-range-83ecb080-00124))_
- Reg has crafted (and continues to craft) not only an interesting book from the perspective of a connoisseur, but also an entertaining exploration into some of the most interesting aspects of his art. _(javascriptallonge.pdf (source-range-83ecb080-00125))_
- No matter how much of an expert you think you are, JavaScript Allongé has something to teach you… about coffee. _(javascriptallonge.pdf (source-range-83ecb080-00125))_
- Reg has crafted (and continues to craft) not only an interesting book from the perspective of a connoisseur, but also an entertaining exploration into some of the most interesting aspects of his art. _(javascriptallonge.pdf (source-range-83ecb080-00125))_
- Instead, every section is motivated by relevant dialog and fortified with compelling source examples. _(javascriptallonge.pdf (source-range-83ecb080-00126))_
- As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time. _(javascriptallonge.pdf (source-range-83ecb080-00126))_
- While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. _(javascriptallonge.pdf (source-range-83ecb080-00126))_
- As a staunch advocate of functional programming, much of what Reg has written rings true to me. _(javascriptallonge.pdf (source-range-83ecb080-00126))_
- However, you’ll not be beaten about the head and neck with dogma. _(javascriptallonge.pdf (source-range-83ecb080-00126))_

### **matthew knox**

- A different kind of language requires a different kind of book. _(javascriptallonge.pdf (source-range-83ecb080-00130))_
- JavaScript holds surprising depths–its scoping rules are neither strictly lexical nor strictly dynamic, and it supports procedural, object-oriented (in several flavors!), and functional programming. _(javascriptallonge.pdf (source-range-83ecb080-00131))_
- It starts with the fundamentals of values, functions, and objects, and then guides you through JavaScript from the inside with exploratory bits of code that illustrate scoping, combinators, context, state, prototypes, and constructors. _(javascriptallonge.pdf (source-range-83ecb080-00135))_

## About The Sample PDF

### **About The Sample PDF**

- If you read _JavaScript Allongé, The “six” edition_ and it doesn’t blow your mind, your money will be cheerfully refunded. _(javascriptallonge.pdf (source-range-83ecb080-00143))_
- This sample edition of the book includes just a portion of the complete book. _(javascriptallonge.pdf (source-range-83ecb080-00143))_

## Prelude: Values and Expressions over Coffee

### **Prelude: Values and Expressions over Coffee**

## values are expressions

### **values are expressions**

- All values are expressions. _(javascriptallonge.pdf (source-range-83ecb080-00161))_
- You say, “I want one of these.” The barista is no fool, she gives it straight back to you, and you get exactly what you want. _(javascriptallonge.pdf (source-range-83ecb080-00161))_
- Yup, you hand over a cup with some coffee infused through partially caramelized sugar. _(javascriptallonge.pdf (source-range-83ecb080-00161))_
- Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). _(javascriptallonge.pdf (source-range-83ecb080-00161))_
- Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). _(javascriptallonge.pdf (source-range-83ecb080-00161))_

### 42

> Context: Let’s try this with something the computer understands easily:
_(context: javascriptallonge.pdf (source-range-83ecb080-00162))_

> The answer is, this is both an expression _and_ a value.[10] The way you can tell that it’s both is very easy: When you type it into JavaScript, you get the same thing back, just like our café Cubano:
_(source: javascriptallonge.pdf (source-range-83ecb080-00165))_

### 42

- All values are expressions. _(javascriptallonge.pdf (source-range-83ecb080-00168))_
- Instead of handing over the finished coffee, we can hand over the ingredients. _(javascriptallonge.pdf (source-range-83ecb080-00168))_
- Astute readers will realize we’re omitting something. _(javascriptallonge.pdf (source-range-83ecb080-00169))_
- Ground coffee is a value. _(javascriptallonge.pdf (source-range-83ecb080-00170))_
- So, boiling water plus ground coffee is an expression, but it isn’t a value.[11] Boiling water is a value. _(javascriptallonge.pdf (source-range-83ecb080-00170))_
- Boiling water plus ground coffee is an expression. _(javascriptallonge.pdf (source-range-83ecb080-00170))_
- You and I both understand that this means “42,” and so does the computer. _(javascriptallonge.pdf (source-range-83ecb080-00174))_
- You and I both understand that this means “42,” and so does the computer. _(javascriptallonge.pdf (source-range-83ecb080-00174))_
- > 11In some languages, expressions are a kind of value unto themselves and can be manipulated. _(javascriptallonge.pdf (source-range-83ecb080-00175))_
- JavaScript is not such a language, expressions in and of themselves are not values. _(javascriptallonge.pdf (source-range-83ecb080-00175))_
- The grandfather of such languages is Lisp. _(javascriptallonge.pdf (source-range-83ecb080-00175))_

> Context: All values are expressions. That’s easy! Are there any other kinds of expressions? Sure! let’s go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let’s hand over some ground coffee plus some boiling water.
_(context: javascriptallonge.pdf (source-range-83ecb080-00168))_

> And if we hand over the espresso, we get the espresso right back.
_(source: javascriptallonge.pdf (source-range-83ecb080-00170))_

> Now we see that “strings” are values, and you can make an expression out of strings and an operator +. Since strings are values, they are also expressions by themselves. But strings with operators are not values, they are expressions. Now we know what was missing with our “coffee grounds plus hot water” example. The coffee grounds were a value, the boiling hot water was a value, and the “plus” operator between them made the whole thing an expression that was not a value.
_(source: javascriptallonge.pdf (source-range-83ecb080-00178))_

## values and identity

### **values and identity**

- And then you’re shown another cup of coffee. _(javascriptallonge.pdf (source-range-83ecb080-00185))_
- For example, the string "2" is not the same thing as the number 2. _(javascriptallonge.pdf (source-range-83ecb080-00186))_
- One is a demitasse, the other a mug. _(javascriptallonge.pdf (source-range-83ecb080-00186))_
- This corresponds to comparing two things in JavaScript that have different _types_ . _(javascriptallonge.pdf (source-range-83ecb080-00186))_
- First, sometimes, the cups are of different kinds. _(javascriptallonge.pdf (source-range-83ecb080-00186))_
- For example, the string "2" is not the same thing as the number 2. _(javascriptallonge.pdf (source-range-83ecb080-00186))_
- This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2. _(javascriptallonge.pdf (source-range-83ecb080-00188))_
- One holds a single, one a double. _(javascriptallonge.pdf (source-range-83ecb080-00188))_
- This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2. _(javascriptallonge.pdf (source-range-83ecb080-00188))_

> Context: Second, sometimes, the cups are of the same type–perhaps two espresso cups–but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2.
_(context: javascriptallonge.pdf (source-range-83ecb080-00188))_

> **true** === **false** _//=> false_ 2 !== 5 _//=> true_ 'two' === 'five' _//=> false_
_(source: javascriptallonge.pdf (source-range-83ecb080-00189))_

### **value types**

- If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. _(javascriptallonge.pdf (source-range-83ecb080-00194))_
- This is the case with the strings, numbers, and booleans we have seen so far. _(javascriptallonge.pdf (source-range-83ecb080-00194))_
- Third, some types of cups have no distinguishing marks on them. _(javascriptallonge.pdf (source-range-83ecb080-00194))_
- Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. _(javascriptallonge.pdf (source-range-83ecb080-00197))_
- We’ll use both terms interchangeably. _(javascriptallonge.pdf (source-range-83ecb080-00197))_
- We haven’t encountered the fourth possibility yet. _(javascriptallonge.pdf (source-range-83ecb080-00198))_
- **Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d’Italia** _(javascriptallonge.pdf (source-range-83ecb080-00200))_

> Context: Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.
_(context: javascriptallonge.pdf (source-range-83ecb080-00197))_

> - 2 + 2 === 4 _//=> true_
_(source: javascriptallonge.pdf (source-range-83ecb080-00195))_

> Context: Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.
_(context: javascriptallonge.pdf (source-range-83ecb080-00197))_

> - (2 + 2 === 4) === (2 !== 5) _//=> true_
_(source: javascriptallonge.pdf (source-range-83ecb080-00196))_

> Context: Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.
_(context: javascriptallonge.pdf (source-range-83ecb080-00197))_

> So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them.
_(source: javascriptallonge.pdf (source-range-83ecb080-00198))_

### **reference types**

- Let’s meet a data structure that is very common in contemporary programming languages, the _Array_ (other languages sometimes call it a List or a Vector). _(javascriptallonge.pdf (source-range-83ecb080-00202))_
- This is an expression, and you can combine [] with other expressions. _(javascriptallonge.pdf (source-range-83ecb080-00205))_
- Notice that you are always generating arrays with the same contents. _(javascriptallonge.pdf (source-range-83ecb080-00207))_
- When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own _unique_ array that is not identical to any other array, even if that other array also looks like [1, 2, 3]. _(javascriptallonge.pdf (source-range-83ecb080-00209))_
- They look the same, but if you examine them with ===, you see that they are different. _(javascriptallonge.pdf (source-range-83ecb080-00210))_
- Every time you evaluate an expression (including typing something in) to create an array, you’re creating a new, distinct value even if it _appears_ to be the same as some other array value. _(javascriptallonge.pdf (source-range-83ecb080-00210))_
- As we’ll see, this is true of many other kinds of values, including _functions_ , the main subject of this book. _(javascriptallonge.pdf (source-range-83ecb080-00210))_

> Context: An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wild with things like:
_(context: javascriptallonge.pdf (source-range-83ecb080-00205))_

> [2-1, 2, 2+1] [1, 1+1, 1+1+1]
_(source: javascriptallonge.pdf (source-range-83ecb080-00206))_

> Context: Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of 42 is identical to every other value of 42? Try these for yourself:
_(context: javascriptallonge.pdf (source-range-83ecb080-00207))_

> [2-1, 2, 2+1] === [1,2,3] [1,2,3] === [1, 2, 3] [1, 2, 3] === [1, 2, 3]
_(source: javascriptallonge.pdf (source-range-83ecb080-00208))_

## A Rich Aroma: Basic Numbers

### **A Rich Aroma: Basic Numbers**

- Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. _(javascriptallonge.pdf (source-range-83ecb080-00215))_
- In computer science, a literal is a notation for representing a fixed value in source code. _(javascriptallonge.pdf (source-range-83ecb080-00215))_
- Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. _(javascriptallonge.pdf (source-range-83ecb080-00215))_
- We saw that an expression consisting solely of numbers, like 42, is a literal. _(javascriptallonge.pdf (source-range-83ecb080-00216))_
- It represents the number forty-two, which is 42 base 10. _(javascriptallonge.pdf (source-range-83ecb080-00216))_
- all numbers are base ten. _(javascriptallonge.pdf (source-range-83ecb080-00220))_
- If we start a literal with a zero, it is an octal literal. _(javascriptallonge.pdf (source-range-83ecb080-00220))_
- So the literal 042 is 42 base 8, which is actually 34 base 10. _(javascriptallonge.pdf (source-range-83ecb080-00220))_
- A computer’s internal representation for numbers is important to understand. _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- Internally, both 042 and 34 have the same representation, as double-precision floating point[13] numbers. _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- For example, the largest integer JavaScript can safely[14] handle is 9007199254740991, or 2[‘53‘] - 1. _(javascriptallonge.pdf (source-range-83ecb080-00222))_
- For example, the largest integer JavaScript can safely[14] handle is 9007199254740991, or 2[‘53‘] - 1. _(javascriptallonge.pdf (source-range-83ecb080-00222))_

> The machine’s representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer’s behaviour surprises us if we don’t know a little about what it’s doing “under the hood.”
_(source: javascriptallonge.pdf (source-range-83ecb080-00221))_

### **floating**

- We can, for example, write 1.5 or 33.33, and JavaScript represents these literals as floating point numbers. _(javascriptallonge.pdf (source-range-83ecb080-00224))_
- But we mentioned that numbers are represented internally as floating point, meaning that they need not be just integers. _(javascriptallonge.pdf (source-range-83ecb080-00224))_
- We can, for example, write 1.5 or 33.33, and JavaScript represents these literals as floating point numbers. _(javascriptallonge.pdf (source-range-83ecb080-00224))_
- Most programmers never encounter the limit on the magnitude of an integer. _(javascriptallonge.pdf (source-range-83ecb080-00224))_
- This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2. _(javascriptallonge.pdf (source-range-83ecb080-00225))_
- It’s tempting to think we now have everything we need to do things like handle amounts of money, but as the late John Belushi would say, “Nooooooooooooooooooooo.” A computer’s internal representation for a floating point number is binary, while our literal number was in base ten. _(javascriptallonge.pdf (source-range-83ecb080-00225))_
- This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2. _(javascriptallonge.pdf (source-range-83ecb080-00225))_
- But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations. _(javascriptallonge.pdf (source-range-83ecb080-00232))_
- > 14Implementations of JavaScript are free to handle larger numbers. _(javascriptallonge.pdf (source-range-83ecb080-00232))_
- For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. _(javascriptallonge.pdf (source-range-83ecb080-00232))_
- For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. _(javascriptallonge.pdf (source-range-83ecb080-00232))_
- For example, “$43.21” will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21. _(javascriptallonge.pdf (source-range-83ecb080-00237))_
- In this book, we need not think about such details, but outside of this book, we must. _(javascriptallonge.pdf (source-range-83ecb080-00237))_
- But as a rule, if you need to work with real numbers, you should have more than a nodding acquaintance with the IEEE Standard for Floating-Point Arithmetic[15] . _(javascriptallonge.pdf (source-range-83ecb080-00237))_
- For example, “$43.21” will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21. _(javascriptallonge.pdf (source-range-83ecb080-00237))_

> Context: One of the most oft-repeated examples is this:
_(context: javascriptallonge.pdf (source-range-83ecb080-00226))_

> - 1.0 + 1.0 _//=> 2_
_(source: javascriptallonge.pdf (source-range-83ecb080-00228))_

> Context: One of the most oft-repeated examples is this:
_(context: javascriptallonge.pdf (source-range-83ecb080-00226))_

> - 1.0 + 1.0 + 1.0 _//=> 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-00229))_

> Context: > 14Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations.
_(context: javascriptallonge.pdf (source-range-83ecb080-00232))_

> 0.1 _//=> 0.1_ 0.1 + 0.1 _//=> 0.2_ 0.1 + 0.1 + 0.1 _//=> 0.30000000000000004_
_(source: javascriptallonge.pdf (source-range-83ecb080-00235))_

> This kind of “inexactitude” can be ignored when performing calculations that have an acceptable deviation. For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript’s calculation is less than a pixel, there is no observable error.
_(source: javascriptallonge.pdf (source-range-83ecb080-00236))_

> Context: This kind of “inexactitude” can be ignored when performing calculations that have an acceptable deviation. For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript’s calculation is less than a pixel, there is no observable error.
_(context: javascriptallonge.pdf (source-range-83ecb080-00236))_

> Professional programmers almost never use floating point numbers to represent monetary amounts.
_(source: javascriptallonge.pdf (source-range-83ecb080-00237))_

### **operations on numbers**

- As we’ve seen, JavaScript has many common arithmetic operators. _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- These can be combined to make more complex expressions, like 2 * 5 + 1. _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. _(javascriptallonge.pdf (source-range-83ecb080-00240))_
- JavaScript has many more operators. _(javascriptallonge.pdf (source-range-83ecb080-00242))_

> Context: In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. So: JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2), because the * operator has a _higher precedence_ than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2, this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the nam
_(context: javascriptallonge.pdf (source-range-83ecb080-00240, source-range-83ecb080-00242))_

> 2 * 5 + 1 _//=> 11_ 1 + 5 * 2 _//=> 11_
_(source: javascriptallonge.pdf (source-range-83ecb080-00241))_

## The first sip: Basic Functions

### **The first sip: Basic Functions**

## As Little As Possible About Functions, But No Less

### **As Little As Possible About Functions, But No Less**

- Functions represent computations to be performed. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- Like numbers, strings, and arrays, they have a representation. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. _(javascriptallonge.pdf (source-range-83ecb080-00258))_

### () => 0

- This is a function that is applied to no values and returns 0. _(javascriptallonge.pdf (source-range-83ecb080-00260))_
- [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. _(javascriptallonge.pdf (source-range-83ecb080-00262))_
- The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. _(javascriptallonge.pdf (source-range-83ecb080-00262))_
- This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. _(javascriptallonge.pdf (source-range-83ecb080-00262))_
- But we must understand that whether we see [Function] or () => 0, internally JavaScript has a full and proper function. _(javascriptallonge.pdf (source-range-83ecb080-00266))_
- I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. _(javascriptallonge.pdf (source-range-83ecb080-00266))_

> Context: This is a function that is applied to no values and returns 0. Let’s verify that our function is a value like all others:
_(context: javascriptallonge.pdf (source-range-83ecb080-00260))_

> If you try the same thing in a browser, you may see something else.
_(source: javascriptallonge.pdf (source-range-83ecb080-00262))_

> Context: What!? Why didn’t it type back () => 0 for us? This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What’s going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a 
_(context: javascriptallonge.pdf (source-range-83ecb080-00262))_

> > 16 The simplest possible function is () => {}, we’ll see that later.
_(source: javascriptallonge.pdf (source-range-83ecb080-00263))_

### **functions and identities**

- Reference types do not. _(javascriptallonge.pdf (source-range-83ecb080-00268))_
- You recall that we have two types of values with respect to identity: Value types and reference types. _(javascriptallonge.pdf (source-range-83ecb080-00268))_
- Value types share the same identity if they have the same contents. _(javascriptallonge.pdf (source-range-83ecb080-00268))_
- “Function” is a reference type. _(javascriptallonge.pdf (source-range-83ecb080-00272))_

### **applying functions**

- The way we use functions is to _apply_ them to zero or more values called _arguments_ . _(javascriptallonge.pdf (source-range-83ecb080-00274))_
- Here’s how we apply a function to some values in JavaScript: Let’s say that _fn_expr_ is an expression that when evaluated, produces a function. _(javascriptallonge.pdf (source-range-83ecb080-00275))_

### _fn_expr_ ( _args_ )

- Right now, we only know about one such expression: () => 0, so let’s use it. _(javascriptallonge.pdf (source-range-83ecb080-00277))_
- We’ll put it in parentheses[17] to keep the parser happy, like we did above: (() => 0). _(javascriptallonge.pdf (source-range-83ecb080-00277))_
- Since we aren’t giving it any arguments, we’ll simply write () after the expression. _(javascriptallonge.pdf (source-range-83ecb080-00277))_
- Right now, we only know about one such expression: () => 0, so let’s use it. _(javascriptallonge.pdf (source-range-83ecb080-00277))_
- > 17If you’re used to other programming languages, you’ve probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. _(javascriptallonge.pdf (source-range-83ecb080-00279))_

### **functions that return values and evaluate expressions**

- We know that (() => 0)() returns 0, and this is unsurprising. _(javascriptallonge.pdf (source-range-83ecb080-00283))_
- Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow. _(javascriptallonge.pdf (source-range-83ecb080-00285))_
- Values like 0 are expressions, as are things like 40 + 2. _(javascriptallonge.pdf (source-range-83ecb080-00286))_
- In the prelude, we looked at expressions. _(javascriptallonge.pdf (source-range-83ecb080-00286))_
- We can put any expression to the right of the arrow. _(javascriptallonge.pdf (source-range-83ecb080-00288))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-83ecb080-00288))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-83ecb080-00288))_
- Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-83ecb080-00291))_

> Context: Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.
_(context: javascriptallonge.pdf (source-range-83ecb080-00285))_

> (() => 1 + 1)() _//=> 2_ (() => "Hello, " + "JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** * **Infinity** )() _//=> Infinity_
_(source: javascriptallonge.pdf (source-range-83ecb080-00287))_

> Context: Yes we can! Functions can return the value of evaluating another function.
_(context: javascriptallonge.pdf (source-range-83ecb080-00291))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.
_(source: javascriptallonge.pdf (source-range-83ecb080-00292))_

### **commas**

- The comma operator in JavaScript is interesting. _(javascriptallonge.pdf (source-range-83ecb080-00298))_
- In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. _(javascriptallonge.pdf (source-range-83ecb080-00303))_

> Context: The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:
_(context: javascriptallonge.pdf (source-range-83ecb080-00298))_

> (1 + 1, 2 + 2) _//=> 4_
_(source: javascriptallonge.pdf (source-range-83ecb080-00300))_

> Context: We can use commas with functions to create functions that evaluate multiple expressions:
_(context: javascriptallonge.pdf (source-range-83ecb080-00301))_

> (() => (1 + 1, 2 + 2))() _//=> 4_
_(source: javascriptallonge.pdf (source-range-83ecb080-00302))_

> Context: We can use commas with functions to create functions that evaluate multiple expressions:
_(context: javascriptallonge.pdf (source-range-83ecb080-00301))_

> This is useful when trying to do things that might involve _side-effects_ , but we’ll get to that later.
_(source: javascriptallonge.pdf (source-range-83ecb080-00303))_

> Context: This is useful when trying to do things that might involve _side-effects_ , but we’ll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00303))_

> () => (1 + 1, 2 + 2)
_(source: javascriptallonge.pdf (source-range-83ecb080-00304))_

> () => ( 1 + 1, 2 + 2
_(source: javascriptallonge.pdf (source-range-83ecb080-00306))_

### **the simplest possible block**

- There’s another thing we can put to the right of an arrow, a _block_ . _(javascriptallonge.pdf (source-range-83ecb080-00311))_

### () => {}

- It returns the result of evaluating a block that has no statements. _(javascriptallonge.pdf (source-range-83ecb080-00314))_

### **undefined**

- In JavaScript, the absence of a value is written undefined, and it means there is no value. _(javascriptallonge.pdf (source-range-83ecb080-00319))_
- It will crop up again. _(javascriptallonge.pdf (source-range-83ecb080-00319))_
- In JavaScript, the absence of a value is written undefined, and it means there is no value. _(javascriptallonge.pdf (source-range-83ecb080-00319))_

### **undefined**

- Like numbers, booleans and strings, JavaScript can print out the value undefined. _(javascriptallonge.pdf (source-range-83ecb080-00322))_
- No matter how you evaluate undefined, you get an identical value back. _(javascriptallonge.pdf (source-range-83ecb080-00325))_
- > 18Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons. _(javascriptallonge.pdf (source-range-83ecb080-00326))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-83ecb080-00326))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-83ecb080-00326))_
- You might think that undefined in JavaScript is equivalent to NULL in SQL. _(javascriptallonge.pdf (source-range-83ecb080-00329))_
- In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can’t be equal. _(javascriptallonge.pdf (source-range-83ecb080-00329))_
- In JavaScript, every undefined is identical to every other undefined. _(javascriptallonge.pdf (source-range-83ecb080-00329))_
- In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can’t be equal. _(javascriptallonge.pdf (source-range-83ecb080-00329))_

> Context: No matter how you evaluate undefined, you get an identical value back. undefined is a value that means “I don’t have a value.” But it’s still a value :-)
_(context: javascriptallonge.pdf (source-range-83ecb080-00325))_

> **undefined** === **undefined**
_(source: javascriptallonge.pdf (source-range-83ecb080-00323))_

### **void**

- We’ve seen that JavaScript represents an undefined value by typing undefined, and we’ve generated undefined values in two ways: _(javascriptallonge.pdf (source-range-83ecb080-00331))_
- void is an operator that takes any value and evaluates to undefined, always. _(javascriptallonge.pdf (source-range-83ecb080-00336))_
- So, when we deliberately want an undefined value, should we use the first, second, or third form?[19] The answer is, use void. _(javascriptallonge.pdf (source-range-83ecb080-00336))_
- The first form works but it’s cumbersome. _(javascriptallonge.pdf (source-range-83ecb080-00337))_
- The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we’ll discuss in Reassignment and Mutation. _(javascriptallonge.pdf (source-range-83ecb080-00337))_

> Context: There’s a third way, with JavaScript’s void operator. Behold: void is an operator that takes any value and evaluates to undefined, always. So, when we deliberately want an undefined value, should we use the first, second, or third form?[19] The answer is, use void. By convention, use void 0.
_(context: javascriptallonge.pdf (source-range-83ecb080-00334, source-range-83ecb080-00336))_

> **void** 0 _//=> undefined_ **void** 1 _//=> undefined_ **void** (2 + 2) _//=> undefined_
_(source: javascriptallonge.pdf (source-range-83ecb080-00335))_

### **back on the block**

- > 19Experienced JavaScript programmers are aware that there’s a fourth way, using a function argument. _(javascriptallonge.pdf (source-range-83ecb080-00340))_
- This was actually the preferred mechanism until void became commonplace. _(javascriptallonge.pdf (source-range-83ecb080-00340))_
- > 20As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined. _(javascriptallonge.pdf (source-range-83ecb080-00341))_

### (() => {})()

- We said that the function returns the result of evaluating a _block_ , and we said that a block is a (possibly empty) list of JavaScript _statements_ separated by semicolons.[21] _(javascriptallonge.pdf (source-range-83ecb080-00346))_
- We haven’t discussed these _statements_ . _(javascriptallonge.pdf (source-range-83ecb080-00348))_
- An expression is a JavaScript statement. _(javascriptallonge.pdf (source-range-83ecb080-00349))_
- There are many kinds of JavaScript statements, but the first kind is one we’ve already met. _(javascriptallonge.pdf (source-range-83ecb080-00349))_
- Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: _(javascriptallonge.pdf (source-range-83ecb080-00349))_
- As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way: _(javascriptallonge.pdf (source-range-83ecb080-00351))_
- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined: _(javascriptallonge.pdf (source-range-83ecb080-00353))_
- Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- This feature was originally created as a kind of helpful error-correction. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- > 21You can also separate statements with line breaks. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- Statements belong inside blocks and only inside blocks. _(javascriptallonge.pdf (source-range-83ecb080-00373))_

> Context: There are many kinds of JavaScript statements, but the first kind is one we’ve already met. An expression is a JavaScript statement. Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:
_(context: javascriptallonge.pdf (source-range-83ecb080-00349, source-range-83ecb080-00351))_

> () => { 2 + 2 } () => { 1 + 1; 2 + 2 }
_(source: javascriptallonge.pdf (source-range-83ecb080-00350))_

> Context: As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:
_(context: javascriptallonge.pdf (source-range-83ecb080-00351))_

> () => { 1 + 1; 2 + 2 }
_(source: javascriptallonge.pdf (source-range-83ecb080-00352))_

> Context: But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:
_(context: javascriptallonge.pdf (source-range-83ecb080-00353))_

> (() => { 2 + 2 })() _//=> undefined_
_(source: javascriptallonge.pdf (source-range-83ecb080-00354))_

> Context: But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:
_(context: javascriptallonge.pdf (source-range-83ecb080-00353))_

> (() => { 1 + 1; 2 + 2 })() _//=> undefined_
_(source: javascriptallonge.pdf (source-range-83ecb080-00355))_

> Context: But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:
_(context: javascriptallonge.pdf (source-range-83ecb080-00353))_

> (() => { 1 + 1; 2 + 2 })() _//=> undefined_
_(source: javascriptallonge.pdf (source-range-83ecb080-00356))_

> Context: The return keyword creates a _return statement_ that immediately terminates the function application and returns the result of evaluating its expression. For example:
_(context: javascriptallonge.pdf (source-range-83ecb080-00364))_

> So how do we get a function that evaluates a block to return a value when applied?
_(source: javascriptallonge.pdf (source-range-83ecb080-00362))_

> Context: The return keyword creates a _return statement_ that immediately terminates the function application and returns the result of evaluating its expression. For example:
_(context: javascriptallonge.pdf (source-range-83ecb080-00364))_

> (() => { 1 + 1; **return** 2 + 2 })() _//=> 4_
_(source: javascriptallonge.pdf (source-range-83ecb080-00365))_

> Context: And also: The return statement is the first statement we’ve seen, and it behaves differently than an expression. For example, you can’t use one as the expression in a simple function, because it isn’t an expression:
_(context: javascriptallonge.pdf (source-range-83ecb080-00366, source-range-83ecb080-00368))_

> (() => { **return** 1 + 1; 2 + 2 })() _//=> 2_
_(source: javascriptallonge.pdf (source-range-83ecb080-00367))_

> The return statement is the first statement we’ve seen, and it behaves differently than an expression. For example, you can’t use one as the expression in a simple function, because it isn’t an expression:
_(source: javascriptallonge.pdf (source-range-83ecb080-00368))_

### **functions that evaluate to functions**

- So we have _a function, that returns a function, that returns zero_ . _(javascriptallonge.pdf (source-range-83ecb080-00378))_
- It’s a function that when applied, evaluates to a function that when applied, evaluates to 0. _(javascriptallonge.pdf (source-range-83ecb080-00378))_
- So… In the next chapter, “I’d Like to Have an Argument, Please,” we’ll see how to make functions practical. _(javascriptallonge.pdf (source-range-83ecb080-00386))_
- We’ve been very clever, but so far this all seems very abstract. _(javascriptallonge.pdf (source-range-83ecb080-00386))_
- Diffraction of a crystal is beautiful and interesting in its own right, but you can’t blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. _(javascriptallonge.pdf (source-range-83ecb080-00386))_

> If an expression that evaluates to a function is, well, an expression, and if a return statement can have any expression on its right side… _Can we put an expression that evaluates to a function on the right side of a function expression?_
_(source: javascriptallonge.pdf (source-range-83ecb080-00375))_

## Ah. I'd Like to Have an Argument, Please.

### **Ah. I’d Like to Have an Argument, Please.**[22]

- We haven’t even said what an argument _is_ , only that our functions don’t have any. _(javascriptallonge.pdf (source-range-83ecb080-00391))_
- Up to now, we’ve looked at functions without arguments. _(javascriptallonge.pdf (source-range-83ecb080-00391))_
- We haven’t even said what an argument _is_ , only that our functions don’t have any. _(javascriptallonge.pdf (source-range-83ecb080-00391))_
- So you know what they are, and I know that you know what they are, but please be patient with the explanation! _(javascriptallonge.pdf (source-range-83ecb080-00392))_
- Most programmers are perfectly familiar with arguments (often called “parameters”). _(javascriptallonge.pdf (source-range-83ecb080-00392))_
- This function has one argument, room, and an empty body. _(javascriptallonge.pdf (source-range-83ecb080-00395))_
- I’m sure you are perfectly comfortable with the idea that this function has two arguments, room, and board. _(javascriptallonge.pdf (source-range-83ecb080-00397))_
- I read that aloud as “When applied to a value representing the diameter, this function _returns_ the diameter times 3.14159265.” _(javascriptallonge.pdf (source-range-83ecb080-00399))_
- To apply a function with an argument (or arguments), we put the argument (or arguments) within the parentheses, like this: _(javascriptallonge.pdf (source-range-83ecb080-00400))_
- You won’t be surprised to see how to write and apply a function to two arguments: _(javascriptallonge.pdf (source-range-83ecb080-00403))_

> Context: I’m sure you are perfectly comfortable with the idea that this function has two arguments, room, and board. What does one do with the arguments? Use them in the body, of course. What do you think this is?
_(context: javascriptallonge.pdf (source-range-83ecb080-00397))_

> (diameter) => diameter * 3.14159265
_(source: javascriptallonge.pdf (source-range-83ecb080-00398))_

> Context: Remember that to apply a function with no arguments, we wrote (() => {})(). To apply a function with an argument (or arguments), we put the argument (or arguments) within the parentheses, like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-00400))_

> ((diameter) => diameter * 3.14159265)(2)
_(source: javascriptallonge.pdf (source-range-83ecb080-00401))_

> ((room, board) => room + board)(800, 150)
_(source: javascriptallonge.pdf (source-range-83ecb080-00407))_

### **a quick summary of functions and bodies**

- How arguments are used in a body’s expression is probably perfectly obvious to you from the examples, especially if you’ve used any programming language (except for the dialect of BASIC–which I recall from my secondary school–that didn’t allow parameters when you called a procedure). _(javascriptallonge.pdf (source-range-83ecb080-00411))_
- How arguments are used in a body’s expression is probably perfectly obvious to you from the examples, especially if you’ve used any programming language (except for the dialect of BASIC–which I recall from my secondary school–that didn’t allow parameters when you called a procedure). _(javascriptallonge.pdf (source-range-83ecb080-00411))_
- One of the important possible statements is a return statement. _(javascriptallonge.pdf (source-range-83ecb080-00413))_

### **call by value**

- That means that when you write some code that appears to apply a function to an expression or expressions, JavaScript evaluates all of those expressions and applies the functions to the resulting value(s). _(javascriptallonge.pdf (source-range-83ecb080-00420))_
- That means that when you write some code that appears to apply a function to an expression or expressions, JavaScript evaluates all of those expressions and applies the functions to the resulting value(s). _(javascriptallonge.pdf (source-range-83ecb080-00420))_
- We’ll see below that while JavaScript always calls by value, the notion of a “value” has additional subtlety. _(javascriptallonge.pdf (source-range-83ecb080-00427))_
- But before we do, let’s look at variables. _(javascriptallonge.pdf (source-range-83ecb080-00427))_
- But before we do, let’s look at variables. _(javascriptallonge.pdf (source-range-83ecb080-00427))_

> Context: So when you write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00424))_

> - ((diameter) => diameter * 3.14159265)(1 + 1) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00425))_

> Context: So when you write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00424))_

> What happened internally is that the expression 1 + 1 was evaluated first, resulting in 2. Then our circumference function was applied to 2.[24]
_(source: javascriptallonge.pdf (source-range-83ecb080-00426))_

### **variables and bindings**

- Right now everything looks simple and straightforward, and we can move on to talk about arguments in more detail. _(javascriptallonge.pdf (source-range-83ecb080-00429))_
- Besides a desire to use long words to sound impressive, this is not going to seem attractive until we find ourselves wanting to discuss the role of the Church of England in 19th century British politics. _(javascriptallonge.pdf (source-range-83ecb080-00431))_
- But there’s another reason for learning the word _antidisestablishmentarianism_ : We might learn how prefixes and postfixes work in English grammar. _(javascriptallonge.pdf (source-range-83ecb080-00432))_
- It has a certain important meaning in its own right, and it’s also an excellent excuse to learn about functions that make functions, environments, variables, and more. _(javascriptallonge.pdf (source-range-83ecb080-00432))_
- In order to talk about how this works, we should agree on a few terms (you may already know them, but let’s check-in together and “synchronize our dictionaries”). _(javascriptallonge.pdf (source-range-83ecb080-00433))_
- The second x, the one in => x, is not an argument, _it’s an expression referring to a variable_ . _(javascriptallonge.pdf (source-range-83ecb080-00433))_
- The first x, the one in (x) => ..., is an _argument_ . _(javascriptallonge.pdf (source-range-83ecb080-00433))_
- The x in the expression that we call a “variable” is itself an expression that is evaluated by looking up the value in the environment. _(javascriptallonge.pdf (source-range-83ecb080-00434))_
- Every time a function is invoked (“invoked” means “applied to zero or more arguments”), a new _environment_ is created. _(javascriptallonge.pdf (source-range-83ecb080-00434))_
- An environment is a (possibly empty) dictionary that maps variables to values by name. _(javascriptallonge.pdf (source-range-83ecb080-00434))_
- Every time a function is invoked (“invoked” means “applied to zero or more arguments”), a new _environment_ is created. _(javascriptallonge.pdf (source-range-83ecb080-00434))_
- > 24 We said that you can’t apply a function to an expression. _(javascriptallonge.pdf (source-range-83ecb080-00435))_
- This has interesting applications, and they will be explored much more thoroughly in Functions That Are Applied to Functions. _(javascriptallonge.pdf (source-range-83ecb080-00435))_
- Well for arguments, that is very simple. _(javascriptallonge.pdf (source-range-83ecb080-00438))_
- When you apply the function to the arguments, an entry is placed in the dictionary for each argument. _(javascriptallonge.pdf (source-range-83ecb080-00438))_
- The value ‘2’ is bound to the name ‘x’ in the environment. _(javascriptallonge.pdf (source-range-83ecb080-00447))_
- The expression ‘x’ (the right side of the function) is evaluated within the environment we just created. _(javascriptallonge.pdf (source-range-83ecb080-00448))_
- The expression ‘x’ (the right side of the function) is evaluated within the environment we just created. _(javascriptallonge.pdf (source-range-83ecb080-00448))_
- The value of a variable when evaluated in an environment is the value bound to the variable’s name in that environment, which is ‘2’ _(javascriptallonge.pdf (source-range-83ecb080-00449))_
- meaning, that the environment is a dictionary, and that the value 2 is bound to the name x, and that there might be other stuff in that dictionary we aren’t discussing right now. _(javascriptallonge.pdf (source-range-83ecb080-00451))_

> Context: Right now everything looks simple and straightforward, and we can move on to talk about arguments in more detail. And we’re going to work our way up from (diameter) => diameter * 3.14159265 to functions like:
_(context: javascriptallonge.pdf (source-range-83ecb080-00429))_

> - (x) => (y) => x
_(source: javascriptallonge.pdf (source-range-83ecb080-00430))_

> Context: How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dictionary for each argument. So when we write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00438))_

> ((x) => x)(2) _//=> 2_
_(source: javascriptallonge.pdf (source-range-83ecb080-00439))_

> Context: What happens is this:
_(context: javascriptallonge.pdf (source-range-83ecb080-00440))_

> 3. One sub-expression, (x) => x evaluates to a function.
_(source: javascriptallonge.pdf (source-range-83ecb080-00443))_

### **call by sharing**

- Now it is time to take another look at the distinction between value and reference types. _(javascriptallonge.pdf (source-range-83ecb080-00453))_
- At that time, we looked at how JavaScript distinguishes objects that are identical from objects that are not. _(javascriptallonge.pdf (source-range-83ecb080-00453))_
- Earlier, we distinguished JavaScript’s _value types_ from its _reference types_ . _(javascriptallonge.pdf (source-range-83ecb080-00453))_
- There is a property that JavaScript strictly maintains: When a value–any value–is passed as an argument to a function, the value bound in the function’s environment must be identical to the original. _(javascriptallonge.pdf (source-range-83ecb080-00454))_
- We said that JavaScript binds names to values, but we didn’t say what it means to bind a name to a value. _(javascriptallonge.pdf (source-range-83ecb080-00455))_
- Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. _(javascriptallonge.pdf (source-range-83ecb080-00455))_
- We said that JavaScript binds names to values, but we didn’t say what it means to bind a name to a value. _(javascriptallonge.pdf (source-range-83ecb080-00455))_
- JavaScript does not place copies of reference values in any environment. _(javascriptallonge.pdf (source-range-83ecb080-00460))_
- JavaScript places _references_ to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-83ecb080-00460))_
- Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types. _(javascriptallonge.pdf (source-range-83ecb080-00461))_
- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. _(javascriptallonge.pdf (source-range-83ecb080-00461))_
- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. _(javascriptallonge.pdf (source-range-83ecb080-00461))_
- > 26 Unless the argument is NaN, which isn’t equal to anything, _including itself_ . _(javascriptallonge.pdf (source-range-83ecb080-00465))_
- > 26 Unless the argument is NaN, which isn’t equal to anything, _including itself_ . _(javascriptallonge.pdf (source-range-83ecb080-00465))_

> Context: Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types.
_(context: javascriptallonge.pdf (source-range-83ecb080-00461))_

> So JavaScript can make as many copies of strings, numbers, or booleans as it wishes.
_(source: javascriptallonge.pdf (source-range-83ecb080-00459))_

> Context: And with that, we’re ready to look at _closures_ . When we combine our knowledge of value types, reference types, arguments, and closures, we’ll understand why this function always evaluates to true no matter what argument[26] you apply it to:
_(context: javascriptallonge.pdf (source-range-83ecb080-00462))_

> - ((ref1, ref2) => ref1 === ref2)(value, value)
_(source: javascriptallonge.pdf (source-range-83ecb080-00464))_

## Closures and Scope

### **Closures and Scope**

- First off, let’s use what we learned above. _(javascriptallonge.pdf (source-range-83ecb080-00472))_

> Context: It’s time to see how a function within a function works: First off, let’s use what we learned above. Given ( _some function_ )( _some argument_ ), we know that we apply the function to the argument, create an environment, bind the value of the argument to the name, and evaluate the function’s expression. So we do that first with this code:
_(context: javascriptallonge.pdf (source-range-83ecb080-00470, source-range-83ecb080-00472))_

> - ((x) => (y) => x)(1)(2) _//=> 1_
_(source: javascriptallonge.pdf (source-range-83ecb080-00471))_

### ((x) => (y) => x)(1)

### (y) => x

- So now we have a value representing that function. _(javascriptallonge.pdf (source-range-83ecb080-00477))_
- Then we’re going to take the value of that function and apply it to the argument 2, something like this: _(javascriptallonge.pdf (source-range-83ecb080-00477))_
- There is no x in its environment, it must come from somewhere else. _(javascriptallonge.pdf (source-range-83ecb080-00479))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from “outside” of a function that are referenced inside a function. _(javascriptallonge.pdf (source-range-83ecb080-00480))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from “outside” of a function that are referenced inside a function. _(javascriptallonge.pdf (source-range-83ecb080-00480))_
- Now let’s enjoy a relaxed Allongé before we continue! _(javascriptallonge.pdf (source-range-83ecb080-00482))_
- Now let’s enjoy a relaxed Allongé before we continue! _(javascriptallonge.pdf (source-range-83ecb080-00482))_

> Context: So now we have a value representing that function. Then we’re going to take the value of that function and apply it to the argument 2, something like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-00477))_

> - ((y) => x)(2)
_(source: javascriptallonge.pdf (source-range-83ecb080-00478))_

> Context: This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from “outside” of a function that are referenced inside a function. For example, here’s the equivalent code in Ruby:
_(context: javascriptallonge.pdf (source-range-83ecb080-00480))_

> lambda { |x| lambda { |y| x } }[1][2] _#=> 1_
_(source: javascriptallonge.pdf (source-range-83ecb080-00481))_

### **if functions without free variables are pure, are closures impure?**

- It contains a _free variable_ , x.[27] A free variable is one that is not bound within the function. _(javascriptallonge.pdf (source-range-83ecb080-00486))_
- Up to now, we’ve only seen one way to “bind” a variable, namely by passing in an argument with the same name. _(javascriptallonge.pdf (source-range-83ecb080-00486))_
- It contains a _free variable_ , x.[27] A free variable is one that is not bound within the function. _(javascriptallonge.pdf (source-range-83ecb080-00486))_
- Now that we know that variables used in a function are either bound or free, we can bifurcate functions into those with free variables and those without: _(javascriptallonge.pdf (source-range-83ecb080-00487))_
- - Functions containing no free variables are called _pure functions_ . _(javascriptallonge.pdf (source-range-83ecb080-00488))_
- - Functions containing one or more free variables are called _closures_ . _(javascriptallonge.pdf (source-range-83ecb080-00489))_
- They always mean the same thing wherever you use them. _(javascriptallonge.pdf (source-range-83ecb080-00490))_
- Pure functions are easiest to understand. _(javascriptallonge.pdf (source-range-83ecb080-00490))_

### () => {}

### (x) => x

- The third one is actually two functions, one inside the other. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- The second doesn’t have any free variables, because its only variable is bound. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- The first function doesn’t have any variables, therefore doesn’t have any free variables. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- The second doesn’t have any free variables, because its only variable is bound. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- The third one is actually two functions, one inside the other. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- The first function doesn’t have any variables, therefore doesn’t have any free variables. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- has a free variable, but the entire expression refers to (x) => ..., and it doesn’t have a free variable: The only variable anywhere in its body is x, which is certainly bound within (x) => .... _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- From this, we learn something: A pure function can contain a closure. _(javascriptallonge.pdf (source-range-83ecb080-00495))_
- If you can’t, give your reasoning for why it’s impossible. _(javascriptallonge.pdf (source-range-83ecb080-00497))_
- Using only what we’ve learned so far, attempt to compose a closure that contains a pure function. _(javascriptallonge.pdf (source-range-83ecb080-00497))_
- Using only what we’ve learned so far, attempt to compose a closure that contains a pure function. _(javascriptallonge.pdf (source-range-83ecb080-00497))_
- We can’t say what it will do with argument (2) without understanding the magic for evaluating the free variable x. _(javascriptallonge.pdf (source-range-83ecb080-00498))_
- Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. _(javascriptallonge.pdf (source-range-83ecb080-00498))_
- Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. _(javascriptallonge.pdf (source-range-83ecb080-00498))_
- 27You may also hear the term “non-local variable.” Both are correct. _(javascriptallonge.pdf (source-range-83ecb080-00499))_

> Context: Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we’ve already seen: The first function doesn’t have any variables, therefore doesn’t have any free variables. The second doesn’t have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ..., and it doesn’t have a free variable: The 
_(context: javascriptallonge.pdf (source-range-83ecb080-00490, source-range-83ecb080-00494))_

> - (x) => (y) => x
_(source: javascriptallonge.pdf (source-range-83ecb080-00493))_

> Context: Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y, we know exactly what it does with (2, 2). But what about this closure: (y) => x + y? We can’t say what it will do with argument (2) without understanding the magic for evaluating the free variable x.
_(context: javascriptallonge.pdf (source-range-83ecb080-00498))_

> If pure functions can contain closures, can a closure contain a pure function?
_(source: javascriptallonge.pdf (source-range-83ecb080-00497))_

### **it’s always the environment**

- We also hand-waved something when describing our environment. _(javascriptallonge.pdf (source-range-83ecb080-00503))_
- To understand how closures are evaluated, we need to revisit environments. _(javascriptallonge.pdf (source-range-83ecb080-00503))_
- As we’ve said before, all functions are associated with an environment. _(javascriptallonge.pdf (source-range-83ecb080-00503))_
- As we’ve said before, all functions are associated with an environment. _(javascriptallonge.pdf (source-range-83ecb080-00503))_
- The variable x isn’t in (y) => ...’s immediate environment, but it is in its parent’s environment, so it evaluates to 1 and that’s what ((y) => x)(2) returns even though it ended up ignoring its own argument. _(javascriptallonge.pdf (source-range-83ecb080-00505))_
- Some people get so excited by this that they write entire books about them, some are great _[a]_ , some–how shall I put this–are interesting _[b]_ if you use Ruby. _(javascriptallonge.pdf (source-range-83ecb080-00506))_
- The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3). _(javascriptallonge.pdf (source-range-83ecb080-00513))_
- Only you call it with (1)(2)(3) instead of (1, 2, 3). _(javascriptallonge.pdf (source-range-83ecb080-00513))_
- Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-83ecb080-00516))_
- The first function is the result of currying _[a]_ the second function. _(javascriptallonge.pdf (source-range-83ecb080-00516))_
- Calling a curried function with only some of its arguments is sometimes called partial application _[b]_ . _(javascriptallonge.pdf (source-range-83ecb080-00516))_
- Calling a curried function with only some of its arguments is sometimes called partial application _[b]_ . _(javascriptallonge.pdf (source-range-83ecb080-00516))_

> Context: To understand how closures are evaluated, we need to revisit environments. As we’ve said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...}? Let’s fill in the blanks!
_(context: javascriptallonge.pdf (source-range-83ecb080-00503))_

> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.
_(source: javascriptallonge.pdf (source-range-83ecb080-00504))_

> Context: Functions can have grandparents too:
_(context: javascriptallonge.pdf (source-range-83ecb080-00509))_

> (x) => (y) => (z) => x + y + z
_(source: javascriptallonge.pdf (source-range-83ecb080-00510))_

> Context: This function does much the same thing as:
_(context: javascriptallonge.pdf (source-range-83ecb080-00511))_

> (x, y, z) => x + y + z
_(source: javascriptallonge.pdf (source-range-83ecb080-00512))_

### **shadowy variables from a shadowy planet**

- An interesting thing happens when a variable has the same name as an ancestor environment’s variable. _(javascriptallonge.pdf (source-range-83ecb080-00520))_
- Although its parent also defines an x, it is ignored when evaluating x + y. _(javascriptallonge.pdf (source-range-83ecb080-00522))_
- JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. _(javascriptallonge.pdf (source-range-83ecb080-00522))_
- When a variable has the same name as an ancestor environment’s binding, it is said to _shadow_ the ancestor. _(javascriptallonge.pdf (source-range-83ecb080-00524))_
- The x in the great-great-grandparent scope is ignored, as are both ws. _(javascriptallonge.pdf (source-range-83ecb080-00524))_
- When evaluating x + y + z, JavaScript will find x and y in the great-grandparent scope and z in the parent scope. _(javascriptallonge.pdf (source-range-83ecb080-00524))_
- This is often a good thing. _(javascriptallonge.pdf (source-range-83ecb080-00525))_

> Context: An interesting thing happens when a variable has the same name as an ancestor environment’s variable. Consider: The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x, it is ignored when evaluating x + y. JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:
_(context: javascriptallonge.pdf (source-range-83ecb080-00520, source-range-83ecb080-00522))_

> - (x) => (x, y) => x + y
_(source: javascriptallonge.pdf (source-range-83ecb080-00521))_

> Context: The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x, it is ignored when evaluating x + y. JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:
_(context: javascriptallonge.pdf (source-range-83ecb080-00522))_

> (x) => (x, y) => (w, z) => (w) => x + y + z
_(source: javascriptallonge.pdf (source-range-83ecb080-00523))_

### **which came first, the chicken or the egg?**

- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. _(javascriptallonge.pdf (source-range-83ecb080-00527))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. _(javascriptallonge.pdf (source-range-83ecb080-00531))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. _(javascriptallonge.pdf (source-range-83ecb080-00531))_
- As we’ll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program. _(javascriptallonge.pdf (source-range-83ecb080-00538))_

> Context: JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': _global environment_ }.
_(context: javascriptallonge.pdf (source-range-83ecb080-00531))_

> If you don’t want your code to operate directly within the global environment, what can you do?
_(source: javascriptallonge.pdf (source-range-83ecb080-00532))_

## That Constant Coffee Craving

### **That Constant Coffee Craving**

- Up to now, all we’ve really seen are _anonymous functions_ , functions that don’t have a name. _(javascriptallonge.pdf (source-range-83ecb080-00543))_
- This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. _(javascriptallonge.pdf (source-range-83ecb080-00543))_
- Naming things is a critical part of programming, but all we’ve seen so far is how to name arguments. _(javascriptallonge.pdf (source-range-83ecb080-00543))_
- In order to bind 3.14159265 to the name PI, we’ll need a function with a parameter of PI applied to an argument of 3.14159265. _(javascriptallonge.pdf (source-range-83ecb080-00548))_
- This one has a few more moving parts, that’s all. _(javascriptallonge.pdf (source-range-83ecb080-00552))_
- But we can use it just like (diameter) => diameter * 3.14159265. _(javascriptallonge.pdf (source-range-83ecb080-00552))_
- This expression, when evaluated, returns a function that calculates circumferences. _(javascriptallonge.pdf (source-range-83ecb080-00552))_
- All of our “functions” are expressions. _(javascriptallonge.pdf (source-range-83ecb080-00552))_
- We can bind anything we want in an expression by wrapping it in a function that is immediately invoked with the value we want to bind.[29] _(javascriptallonge.pdf (source-range-83ecb080-00559))_

> There are other ways to name things in JavaScript, but before we learn some of those, let’s see how to use what we already have to name things. Let’s revisit a very simple example:
_(source: javascriptallonge.pdf (source-range-83ecb080-00544))_

> Context: There are other ways to name things in JavaScript, but before we learn some of those, let’s see how to use what we already have to name things. Let’s revisit a very simple example:
_(context: javascriptallonge.pdf (source-range-83ecb080-00544))_

> (diameter) => diameter * 3.14159265
_(source: javascriptallonge.pdf (source-range-83ecb080-00545))_

> Context: What is this “3.14159265” number? PI[28] , obviously. We’d like to name it so that we can write something like:
_(context: javascriptallonge.pdf (source-range-83ecb080-00546))_

> (diameter) => diameter * PI
_(source: javascriptallonge.pdf (source-range-83ecb080-00547))_

> Context: In order to bind 3.14159265 to the name PI, we’ll need a function with a parameter of PI applied to an argument of 3.14159265. If we put our function expression in parentheses, we can apply it to the argument of 3.14159265:
_(context: javascriptallonge.pdf (source-range-83ecb080-00548))_

> ((PI) => _// ????_ )(3.14159265)
_(source: javascriptallonge.pdf (source-range-83ecb080-00549))_

> Context: What do we put inside our new function that binds 3.14159265 to the name PI when evaluated? Our circumference function, of course:
_(context: javascriptallonge.pdf (source-range-83ecb080-00550))_

> ((PI) => (diameter) => diameter * PI )(3.14159265)
_(source: javascriptallonge.pdf (source-range-83ecb080-00551))_

> ((diameter) => diameter * 3.14159265)(2) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00557))_

> ((PI) => (diameter) => diameter * PI )(3.14159265)(2) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00558))_

### **inside-out**

- There’s another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-83ecb080-00561))_
- We can turn things inside-out by putting the binding inside our diameter calculating function, like this: _(javascriptallonge.pdf (source-range-83ecb080-00561))_
- We can turn things inside-out by putting the binding inside our diameter calculating function, like this: _(javascriptallonge.pdf (source-range-83ecb080-00561))_
- There’s another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-83ecb080-00561))_
- A “magic literal” like 3.14159265 is anathema to sustainable software development. _(javascriptallonge.pdf (source-range-83ecb080-00565))_
- Well, the first one seems simplest, but a half-century of experience has taught us that names matter. _(javascriptallonge.pdf (source-range-83ecb080-00565))_
- The third one is easiest for most people to read. _(javascriptallonge.pdf (source-range-83ecb080-00566))_
- Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated “IIFE.” _(javascriptallonge.pdf (source-range-83ecb080-00567))_
- > 29JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-83ecb080-00567))_
- > 29JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-83ecb080-00567))_
- That’s how it should be, naming PI is its concern, not ours. _(javascriptallonge.pdf (source-range-83ecb080-00571))_
- Everything else is encapsulated in its body. _(javascriptallonge.pdf (source-range-83ecb080-00571))_
- “Exposes” naming PI first, and we have to look inside to find out why we care. _(javascriptallonge.pdf (source-range-83ecb080-00575))_
- “Exposes” naming PI first, and we have to look inside to find out why we care. _(javascriptallonge.pdf (source-range-83ecb080-00575))_
- Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. _(javascriptallonge.pdf (source-range-83ecb080-00577))_
- But then we’ve obfuscated our code, and we don’t want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-83ecb080-00579))_
- But then we’ve obfuscated our code, and we don’t want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-83ecb080-00579))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. _(javascriptallonge.pdf (source-range-83ecb080-00580))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. _(javascriptallonge.pdf (source-range-83ecb080-00580))_

> Context: There’s another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. We can turn things inside-out by putting the binding inside our diameter calculating function, like this: It produces the same result as our previous expressions for a diameter-calculating function:
_(context: javascriptallonge.pdf (source-range-83ecb080-00561, source-range-83ecb080-00563))_

> (diameter) => ((PI) => diameter * PI)(3.14159265)
_(source: javascriptallonge.pdf (source-range-83ecb080-00562))_

> - (diameter) => ((PI) => diameter * PI)(3.14159265)
_(source: javascriptallonge.pdf (source-range-83ecb080-00576))_

> ((PI) => (diameter) => diameter * PI )(3.14159265)
_(source: javascriptallonge.pdf (source-range-83ecb080-00578))_

### **const**

- Another way to write our “circumference” function would be to pass PI along with the diameter argument, something like this: _(javascriptallonge.pdf (source-range-83ecb080-00582))_
- This differs from our example above in that there is only one environment, rather than two. _(javascriptallonge.pdf (source-range-83ecb080-00588))_
- We have one binding in the environment representing our regular argument, and another our “constant.” That’s more efficient, and it’s _almost_ what we wanted all along: A way to bind 3.14159265 to a readable name. _(javascriptallonge.pdf (source-range-83ecb080-00588))_
- This differs from our example above in that there is only one environment, rather than two. _(javascriptallonge.pdf (source-range-83ecb080-00588))_
- JavaScript gives us a way to do that, the const keyword. _(javascriptallonge.pdf (source-range-83ecb080-00589))_
- We’ll learn a lot more about const in future chapters, but here’s the most important thing we can do with const: _(javascriptallonge.pdf (source-range-83ecb080-00589))_
- That’s much better than what we were writing. _(javascriptallonge.pdf (source-range-83ecb080-00592))_
- We use the const keyword in a _const statement_ . _(javascriptallonge.pdf (source-range-83ecb080-00593))_
- We can bind any expression. _(javascriptallonge.pdf (source-range-83ecb080-00602))_
- Amazing how such an important idea–naming functions–can be explained _en passant_ in just a few words. _(javascriptallonge.pdf (source-range-83ecb080-00605))_
- We can bind more than one name-value pair by separating them with commas. _(javascriptallonge.pdf (source-range-83ecb080-00606))_
- > 30We’re into the second chapter and we’ve finally named a function. _(javascriptallonge.pdf (source-range-83ecb080-00608))_

> Context: Another way to write our “circumference” function would be to pass PI along with the diameter argument, something like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-00582))_

> (diameter, PI) => diameter * PI
_(source: javascriptallonge.pdf (source-range-83ecb080-00583))_

> Context: And we could use it like this: This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our “constant.” That’s more efficient, and it’s _almost_ what we wanted all along: A way to bind 3.14159265 to a readable name.
_(context: javascriptallonge.pdf (source-range-83ecb080-00584, source-range-83ecb080-00588))_

> ((diameter, PI) => diameter * PI)(2, 3.14159265) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00587))_

> Context: JavaScript gives us a way to do that, the const keyword. We’ll learn a lot more about const in future chapters, but here’s the most important thing we can do with const:
_(context: javascriptallonge.pdf (source-range-83ecb080-00589))_

> (diameter) => { **const** PI = 3.14159265;
_(source: javascriptallonge.pdf (source-range-83ecb080-00590))_

> Context: It works just as we want. Instead of:
_(context: javascriptallonge.pdf (source-range-83ecb080-00594))_

> ((diameter) => ((PI) => diameter * PI)(3.14159265))(2)
_(source: javascriptallonge.pdf (source-range-83ecb080-00595))_

> ((diameter, PI) => diameter * PI)(2, 3.14159265) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00597))_

> Context: We write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00598))_

> ((diameter) => { **const** PI = 3.14159265; **return** diameter * PI })(2) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00601))_

> Context: We can bind any expression. Functions are expressions, so we can bind helper functions:
_(context: javascriptallonge.pdf (source-range-83ecb080-00602))_

> This underscores what we’ve said: if we have an expression that evaluates to a function, we apply it with ().
_(source: javascriptallonge.pdf (source-range-83ecb080-00604))_

> Context: We can bind more than one name-value pair by separating them with commas. For readability, most people put one binding per line:
_(context: javascriptallonge.pdf (source-range-83ecb080-00606))_

> (d) => { **const** PI = 3.14159265, calc = (diameter) => diameter * PI; **return** "The circumference is " + calc(d) }
_(source: javascriptallonge.pdf (source-range-83ecb080-00607))_

### **nested blocks**

- Up to now, we’ve only ever seen blocks we use as the body of functions. _(javascriptallonge.pdf (source-range-83ecb080-00612))_
- But there are other kinds of blocks. _(javascriptallonge.pdf (source-range-83ecb080-00612))_
- Up to now, we’ve only ever seen blocks we use as the body of functions. _(javascriptallonge.pdf (source-range-83ecb080-00612))_
- The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. _(javascriptallonge.pdf (source-range-83ecb080-00616))_
- We’ve used a block as the else clause, and since it’s a block, we’ve placed a const statement inside it. _(javascriptallonge.pdf (source-range-83ecb080-00621))_
- We’ve used a block as the else clause, and since it’s a block, we’ve placed a const statement inside it. _(javascriptallonge.pdf (source-range-83ecb080-00621))_

> One of the places you can find blocks is in an if statement.
_(source: javascriptallonge.pdf (source-range-83ecb080-00612))_

### **const and lexical scope**

- This seems very straightforward, but alas, there are some semantics of binding names that we need to understand if we’re to place const anywhere we like. _(javascriptallonge.pdf (source-range-83ecb080-00623))_
- We can use any expression in there, and that expression can invoke diameter_fn. _(javascriptallonge.pdf (source-range-83ecb080-00627))_
- It’s more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we’ve elided. _(javascriptallonge.pdf (source-range-83ecb080-00627))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2), PI _is_ bound when we evaluated (diameter) => diameter * PI, and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn. _(javascriptallonge.pdf (source-range-83ecb080-00631))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2), PI _is_ bound when we evaluated (diameter) => diameter * PI, and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn. _(javascriptallonge.pdf (source-range-83ecb080-00631))_
- This is called lexical scoping[31] , because we can discover where a name is bound by looking at the source code for the program. _(javascriptallonge.pdf (source-range-83ecb080-00632))_
- We can see that PI is bound in an environment surrounding (diameter) => diameter * PI, we don’t need to know where diameter_fn is invoked. _(javascriptallonge.pdf (source-range-83ecb080-00632))_
- This is called lexical scoping[31] , because we can discover where a name is bound by looking at the source code for the program. _(javascriptallonge.pdf (source-range-83ecb080-00632))_
- Although we have bound 3 to PI in the environment surrounding diameter_fn(2), the value that counts is 3.14159265, the value we bound to PI in the environment surrounding (diameter) _⇒_ diameter * PI. _(javascriptallonge.pdf (source-range-83ecb080-00635))_
- That much we can carefully work out from the way closures work. _(javascriptallonge.pdf (source-range-83ecb080-00636))_
- Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-83ecb080-00642))_

> Context: Here’s the second formulation of our diameter function, bound to a name using an IIFE:
_(context: javascriptallonge.pdf (source-range-83ecb080-00625))_

> ((diameter_fn) => _// ..._ )( ((PI) => (diameter) => diameter * PI )(3.14159265) )
_(source: javascriptallonge.pdf (source-range-83ecb080-00626))_

> Context: It’s more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we’ve elided. We can use any expression in there, and that expression can invoke diameter_fn. For example: This is called lexical scoping[31] , because we can discover where a name is bound by looking at the source code for the program. We can see that PI is bound in an environment surrounding (diameter) => diameter * PI, we don’t need to know where dia
_(context: javascriptallonge.pdf (source-range-83ecb080-00627, source-range-83ecb080-00632))_

> ((diameter_fn) => diameter_fn(2) )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00630))_

> Context: We can test this by deliberately creating a “conflict:”
_(context: javascriptallonge.pdf (source-range-83ecb080-00633))_

> ((diameter_fn) => ((PI) => diameter_fn(2) )(3) )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00634))_

> ((diameter_fn) => { **const** PI = 3;
_(source: javascriptallonge.pdf (source-range-83ecb080-00640))_

> **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => diameter * PI })() ) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00641))_

### **are consts also from a shadowy planet?**

- They are looked up in the environment where they are declared. _(javascriptallonge.pdf (source-range-83ecb080-00644))_
- Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions. _(javascriptallonge.pdf (source-range-83ecb080-00644))_
- We just saw that values bound with const use lexical scope, just like values bound with parameters. _(javascriptallonge.pdf (source-range-83ecb080-00644))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. _(javascriptallonge.pdf (source-range-83ecb080-00645))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. _(javascriptallonge.pdf (source-range-83ecb080-00645))_
- We can test this by creating another conflict. _(javascriptallonge.pdf (source-range-83ecb080-00646))_
- But instead of binding two different variables to the same name in two different places, we’ll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-83ecb080-00646))_
- And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. _(javascriptallonge.pdf (source-range-83ecb080-00655))_
- This is a book, you’ve already scanned ahead, so you know that the answer is **no** , the inner binding does not overwrite the outer binding: _(javascriptallonge.pdf (source-range-83ecb080-00657))_
- Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. _(javascriptallonge.pdf (source-range-83ecb080-00657))_
- It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-83ecb080-00659))_
- It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-83ecb080-00659))_
- We say that when we bind a variable using a parameter inside another binding, the inner binding _shadows_ the outer binding. _(javascriptallonge.pdf (source-range-83ecb080-00659))_
- Parameters are only bound when we invoke a function. _(javascriptallonge.pdf (source-range-83ecb080-00665))_
- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-83ecb080-00665))_
- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-83ecb080-00665))_
- Parameters are only bound when we invoke a function. _(javascriptallonge.pdf (source-range-83ecb080-00665))_
- We’ll need a gratuitous block. _(javascriptallonge.pdf (source-range-83ecb080-00666))_
- This design rule is called the Principle of Least Privilege[32] , and it has both quality and security implications. _(javascriptallonge.pdf (source-range-83ecb080-00679))_
- Typically, we want to bind our names as close to where we need them as possible. _(javascriptallonge.pdf (source-range-83ecb080-00679))_
- Being able to bind a name inside of a block means that if the name is only needed in the block, we are not “leaking” its binding to other parts of the code that do not need to interact with it. _(javascriptallonge.pdf (source-range-83ecb080-00679))_
- This design rule is called the Principle of Least Privilege[32] , and it has both quality and security implications. _(javascriptallonge.pdf (source-range-83ecb080-00679))_

> Context: Let’s start, as above, by doing this with parameters. We’ll start with:
_(context: javascriptallonge.pdf (source-range-83ecb080-00647))_

> ((PI) => (diameter) => diameter * PI )(3.14159265)
_(source: javascriptallonge.pdf (source-range-83ecb080-00648))_

> Context: And gratuitously wrap it in another IIFE so that we can bind PI to something else:
_(context: javascriptallonge.pdf (source-range-83ecb080-00649))_

> ((PI) => ((PI) => (diameter) => diameter * PI )(3.14159265) )(3)
_(source: javascriptallonge.pdf (source-range-83ecb080-00652))_

> Context: This still evaluates to a function that calculates diameters:
_(context: javascriptallonge.pdf (source-range-83ecb080-00653))_

> ((PI) => ((PI) => (diameter) => diameter * PI )(3.14159265) )(3)(2) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00654))_

> Context: And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the “outer” environment? Let’s rewrite things slightly differently: Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. Does that binding “overwrite” the outer one? Will our function return 6 or 6.2831853? This is a book, you’ve already scanned ahead, so you know that the
_(context: javascriptallonge.pdf (source-range-83ecb080-00655, source-range-83ecb080-00657))_

> ((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265)
_(source: javascriptallonge.pdf (source-range-83ecb080-00656))_

> Context: Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. Does that binding “overwrite” the outer one? Will our function return 6 or 6.2831853? This is a book, you’ve already scanned ahead, so you know that the answer is **no** , the inner binding does not overwrite the outer binding:
_(context: javascriptallonge.pdf (source-range-83ecb080-00657))_

> ((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265)(2) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00658))_

> ((diameter) => { **const** PI = 3.14159265; (() => { **const** PI = 3; })(); **return** diameter * PI; })(2) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00663))_

> Context: This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this: If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:”
_(context: javascriptallonge.pdf (source-range-83ecb080-00673, source-range-83ecb080-00676))_

> ((diameter) => { **const** PI = 3.14159265;
_(source: javascriptallonge.pdf (source-range-83ecb080-00674))_

> Context: This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this: If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:”
_(context: javascriptallonge.pdf (source-range-83ecb080-00673, source-range-83ecb080-00676))_

> **if** ( **true** ) { **const** PI = 3; } **return** diameter * PI; })(2) _//=> would return 6 if const had function scope_
_(source: javascriptallonge.pdf (source-range-83ecb080-00675))_

> Context: This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-00673))_

> If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents.
_(source: javascriptallonge.pdf (source-range-83ecb080-00676))_

> Context: If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:”
_(context: javascriptallonge.pdf (source-range-83ecb080-00676))_

> **if** ( **true** ) { **const** PI = 3.14159265; } **return** diameter * PI; })(2) _//=> would return 6.2831853 if const had function scope_
_(source: javascriptallonge.pdf (source-range-83ecb080-00678))_

### **rebinding**

- JavaScript does not permit us to rebind a name that has been bound with const. _(javascriptallonge.pdf (source-range-83ecb080-00688))_
- We can _shadow_ it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-83ecb080-00688))_
- This is valuable, as it greatly simplifies the analysis of programs to see at a glance that when something is bound with const, we need never worry that its value may change. _(javascriptallonge.pdf (source-range-83ecb080-00689))_

## Naming Functions

### **Naming Functions**

- This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous. _(javascriptallonge.pdf (source-range-83ecb080-00696))_

> Context: Let’s get right to it. This code does _not_ name a function: It doesn’t name the function “repeat” for the same reason that const answer = 42 doesn’t name the number 42. This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous.
_(context: javascriptallonge.pdf (source-range-83ecb080-00694, source-range-83ecb080-00696))_

> **const** repeat = (str) => str + str
_(source: javascriptallonge.pdf (source-range-83ecb080-00695))_

### **the function keyword**

- JavaScript _does_ have a syntax for naming a function, we use the function keyword. _(javascriptallonge.pdf (source-range-83ecb080-00698))_
- Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-83ecb080-00698))_
- Something else we’re about to discuss is optional. _(javascriptallonge.pdf (source-range-83ecb080-00705))_
- We have arguments in parentheses, just like fat arrow functions. _(javascriptallonge.pdf (source-range-83ecb080-00706))_
- We do not have a fat arrow, we go directly to the body. _(javascriptallonge.pdf (source-range-83ecb080-00707))_
- This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-83ecb080-00708))_
- This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-83ecb080-00708))_
- While the name of the function is a property of the function, not of the environment. _(javascriptallonge.pdf (source-range-83ecb080-00720))_
- That may seem confusing, but think of the binding names as properties of the environment, not of the function. _(javascriptallonge.pdf (source-range-83ecb080-00720))_
- This is a _named function expression_ . _(javascriptallonge.pdf (source-range-83ecb080-00720))_
- In this expression, double is the name in the environment, but repeat is the function’s actual name. _(javascriptallonge.pdf (source-range-83ecb080-00720))_
- > 33“Yes of course?” Well, in chapter of a book dedicated to naming functions, it is not surprising that feature we mention has something to do with naming functions. _(javascriptallonge.pdf (source-range-83ecb080-00725))_
- Now, the function’s actual name has no effect on the environment in which it is used. _(javascriptallonge.pdf (source-range-83ecb080-00729))_
- So “actualName” isn’t bound in the environment where we use the named function expression. _(javascriptallonge.pdf (source-range-83ecb080-00733))_
- Here’s a function that determines whether a positive integer is even or not. _(javascriptallonge.pdf (source-range-83ecb080-00733))_
- Clearly, the name even is bound to the function _within the function’s body_ . _(javascriptallonge.pdf (source-range-83ecb080-00735))_
- This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don’t _need_ to name it anywhere else, you needn’t. _(javascriptallonge.pdf (source-range-83ecb080-00740))_
- even is bound within the function itself, but not outside it. _(javascriptallonge.pdf (source-range-83ecb080-00740))_
- even is bound within the function itself, but not outside it. _(javascriptallonge.pdf (source-range-83ecb080-00740))_

> Context: Here’s our repeat function written using a “fat arrow”
_(context: javascriptallonge.pdf (source-range-83ecb080-00699))_

> (str) => str + str
_(source: javascriptallonge.pdf (source-range-83ecb080-00700))_

> We always use a block, we cannot write function (str) str + str.
_(source: javascriptallonge.pdf (source-range-83ecb080-00708))_

> Context: 5. We always use a block, we cannot write function (str) str + str. This means that if we want our functions to return a value, we always need to use the return keyword
_(context: javascriptallonge.pdf (source-range-83ecb080-00708))_

> If we leave out the “something optional” that comes after the function keyword, we can translate all of the fat arrow functions that we’ve seen into function keyword functions, e.g.
_(source: javascriptallonge.pdf (source-range-83ecb080-00709))_

> Context: If we leave out the “something optional” that comes after the function keyword, we can translate all of the fat arrow functions that we’ve seen into function keyword functions, e.g.
_(context: javascriptallonge.pdf (source-range-83ecb080-00709))_

> (n) => (1.618**n - -1.618**-n) / 2.236
_(source: javascriptallonge.pdf (source-range-83ecb080-00710))_

> Context: Here are our example functions written with names:
_(context: javascriptallonge.pdf (source-range-83ecb080-00716))_

> Placing a name between the function keyword and the argument list names the function. Confusingly, the name of the function is not exactly the same thing as the name we may choose to bind to the value of the function. For example, we can write:
_(source: javascriptallonge.pdf (source-range-83ecb080-00718))_

> Context: Placing a name between the function keyword and the argument list names the function. Confusingly, the name of the function is not exactly the same thing as the name we may choose to bind to the value of the function. For example, we can write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00718))_

> **const double** = **function** repeat (str) { **return** str + str; }
_(source: javascriptallonge.pdf (source-range-83ecb080-00719))_

> Context: Now, the function’s actual name has no effect on the environment in which it is used. To whit:
_(context: javascriptallonge.pdf (source-range-83ecb080-00729))_

> **const** bindingName = **function** actualName () { _//..._
_(source: javascriptallonge.pdf (source-range-83ecb080-00730))_

> Context: Now, the function’s actual name has no effect on the environment in which it is used. To whit:
_(context: javascriptallonge.pdf (source-range-83ecb080-00729))_

> }; bindingName _//=> [Function: actualName]_
_(source: javascriptallonge.pdf (source-range-83ecb080-00731))_

> Context: Now, the function’s actual name has no effect on the environment in which it is used. To whit:
_(context: javascriptallonge.pdf (source-range-83ecb080-00729))_

> actualName _//=> ReferenceError: actualName is not defined_
_(source: javascriptallonge.pdf (source-range-83ecb080-00732))_

### **function declarations**

- There is another syntax for naming and/or defining a function. _(javascriptallonge.pdf (source-range-83ecb080-00742))_
- However, there are two important differences. _(javascriptallonge.pdf (source-range-83ecb080-00750))_
- First, function declarations are _hoisted_ to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-83ecb080-00750))_
- In that it binds a name in the environment to a named function. _(javascriptallonge.pdf (source-range-83ecb080-00750))_
- We haven’t actually bound a function to the name fizzbuzz before we try to use it, so we get an error. _(javascriptallonge.pdf (source-range-83ecb080-00755))_
- We haven’t actually bound a function to the name fizzbuzz before we try to use it, so we get an error. _(javascriptallonge.pdf (source-range-83ecb080-00755))_
- This behaviour is intentional on the part of JavaScript’s design to facilitate a certain style of programming where you put the main logic up front, and the “helper functions” at the bottom. _(javascriptallonge.pdf (source-range-83ecb080-00762))_
- The definition of the fizzbuzz is “hoisted” to the top of its enclosing scope (an IIFE in this case). _(javascriptallonge.pdf (source-range-83ecb080-00762))_
- It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const) is essential for working with production code. _(javascriptallonge.pdf (source-range-83ecb080-00762))_

> Context: This behaves a _little_ like:
_(context: javascriptallonge.pdf (source-range-83ecb080-00746))_

> **const** someName = **function** someName () {
_(source: javascriptallonge.pdf (source-range-83ecb080-00747))_

> Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const:
_(source: javascriptallonge.pdf (source-range-83ecb080-00751))_

> Context: Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const:
_(context: javascriptallonge.pdf (source-range-83ecb080-00751))_

> **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> undefined is not a function (evaluating 'fizzbuzz()')_
_(source: javascriptallonge.pdf (source-range-83ecb080-00754))_

> **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> 'FizzBuzz'_
_(source: javascriptallonge.pdf (source-range-83ecb080-00759))_

> Context: Although fizzbuzz is declared later in the function, JavaScript behaves as if we’d written:
_(context: javascriptallonge.pdf (source-range-83ecb080-00760))_

> ( **function** () { **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } **return** fizzbuzz(); })()
_(source: javascriptallonge.pdf (source-range-83ecb080-00761))_

### **function declaration caveats**[34]

- Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-83ecb080-00764))_
- Function declarations are formally only supposed to be made at what we might call the “top level” of a function. _(javascriptallonge.pdf (source-range-83ecb080-00764))_
- Function declarations are formally only supposed to be made at what we might call the “top level” of a function. _(javascriptallonge.pdf (source-range-83ecb080-00764))_
- 34 A number of the caveats discussed here were described in Jyrly Zaytsev’s excellent article Named function expressions demystified. _(javascriptallonge.pdf (source-range-83ecb080-00765))_
- The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. _(javascriptallonge.pdf (source-range-83ecb080-00770))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-83ecb080-00770))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-83ecb080-00770))_
- Another caveat is that a function declaration cannot exist inside of _any_ expression, otherwise it’s a function expression. _(javascriptallonge.pdf (source-range-83ecb080-00771))_
- Another caveat is that a function declaration cannot exist inside of _any_ expression, otherwise it’s a function expression. _(javascriptallonge.pdf (source-range-83ecb080-00771))_
- The parentheses make this an expression, not a function declaration. _(javascriptallonge.pdf (source-range-83ecb080-00775))_

> Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.
_(source: javascriptallonge.pdf (source-range-83ecb080-00770))_

## Combinators and Function Decorators

### **Combinators and Function Decorators**

### **higher-order functions**

- JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. _(javascriptallonge.pdf (source-range-83ecb080-00781))_
- Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function. _(javascriptallonge.pdf (source-range-83ecb080-00781))_
- But before we go on, we’ll talk about some specific types of higher-order functions. _(javascriptallonge.pdf (source-range-83ecb080-00784))_

### **combinators**

- “A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.”–Wikipedia[35] _(javascriptallonge.pdf (source-range-83ecb080-00787))_
- “A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.”–Wikipedia[35] _(javascriptallonge.pdf (source-range-83ecb080-00787))_
- We’d learn that the fundamental combinators are named after birds following the example of Raymond Smullyan’s famous book To Mock a Mockingbird[36] . _(javascriptallonge.pdf (source-range-83ecb080-00788))_
- If we were learning Combinatorial Logic, we’d start with the most basic combinators like S, K, and I, and work up from there to practical combinators. _(javascriptallonge.pdf (source-range-83ecb080-00788))_
- We’d learn that the fundamental combinators are named after birds following the example of Raymond Smullyan’s famous book To Mock a Mockingbird[36] . _(javascriptallonge.pdf (source-range-83ecb080-00788))_
- We won’t be strict about using only previously defined combinators in their construction. _(javascriptallonge.pdf (source-range-83ecb080-00793))_
- We won’t be strict about using only previously defined combinators in their construction. _(javascriptallonge.pdf (source-range-83ecb080-00793))_
- Let’s start with a useful combinator: Most programmers call it _Compose_ , although the logicians call it the B combinator or “Bluebird.” Here is the typical[37] programming implementation: _(javascriptallonge.pdf (source-range-83ecb080-00794))_
- This is, of course, just one example of many. _(javascriptallonge.pdf (source-range-83ecb080-00803))_
- While some programmers believe “There Should Only Be One Way To Do It,” having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-83ecb080-00803))_
- While some programmers believe “There Should Only Be One Way To Do It,” having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-83ecb080-00803))_

> Context: Let’s start with a useful combinator: Most programmers call it _Compose_ , although the logicians call it the B combinator or “Bluebird.” Here is the typical[37] programming implementation:
_(context: javascriptallonge.pdf (source-range-83ecb080-00794))_

> - **const** compose = (a, b) => (c) => a(b(c))
_(source: javascriptallonge.pdf (source-range-83ecb080-00795))_

> **const** addOne = (number) => number + 1;
_(source: javascriptallonge.pdf (source-range-83ecb080-00797))_

> **const** doubleOf = (number) => number * 2;
_(source: javascriptallonge.pdf (source-range-83ecb080-00798))_

> **const** doubleOfAddOne = (number) => doubleOf(addOne(number));
_(source: javascriptallonge.pdf (source-range-83ecb080-00800))_

> Context: You could also write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00801))_

> **const** doubleOfAddOne = compose(doubleOf, addOne);
_(source: javascriptallonge.pdf (source-range-83ecb080-00802))_

### **a balanced statement about combinators**

- Code that uses a lot of combinators tends to name the verbs and adverbs (like doubleOf, addOne, and compose) while avoiding language keywords and the names of nouns (like number). _(javascriptallonge.pdf (source-range-83ecb080-00805))_
- So one perspective is that combinators are useful when you want to emphasize what you’re doing and how it fits together, and more explicit code is useful when you want to emphasize what you’re working with. _(javascriptallonge.pdf (source-range-83ecb080-00805))_

### **function decorators**

- A _function decorator_ is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. _(javascriptallonge.pdf (source-range-83ecb080-00807))_
- > 37As we’ll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. _(javascriptallonge.pdf (source-range-83ecb080-00808))_
- > 38 We’ll see later why an even more useful version would be written (fn) => (...args) => !fn(...args) _(javascriptallonge.pdf (source-range-83ecb080-00809))_
- So instead of writing !someFunction(42), we can write not(someFunction)(42). _(javascriptallonge.pdf (source-range-83ecb080-00813))_
- Function decorators aren’t strict about being pure functions, so there’s more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-83ecb080-00819))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function’s semantics. _(javascriptallonge.pdf (source-range-83ecb080-00819))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function’s semantics. _(javascriptallonge.pdf (source-range-83ecb080-00819))_

> **const** not = (fn) => (x) => !fn(x)
_(source: javascriptallonge.pdf (source-range-83ecb080-00812))_

> Context: So instead of writing !someFunction(42), we can write not(someFunction)(42). Hardly progress. But like compose, we could write either:
_(context: javascriptallonge.pdf (source-range-83ecb080-00813))_

> **const** something = (x) => x != **null** ;
_(source: javascriptallonge.pdf (source-range-83ecb080-00814))_

> Context: And elsewhere, write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00815))_

> **const** nothing = (x) => !something(x);
_(source: javascriptallonge.pdf (source-range-83ecb080-00816))_

> Context: Or we could write: not is a function decorator because it modifies a function while remaining strongly related to the original function’s semantics. You’ll see other function decorators in the recipes, like once and maybe. Function decorators aren’t strict about being pure functions, so there’s more latitude for making decorators than combinators.
_(context: javascriptallonge.pdf (source-range-83ecb080-00817, source-range-83ecb080-00819))_

> **const** nothing = not(something);
_(source: javascriptallonge.pdf (source-range-83ecb080-00818))_

## Building Blocks

### **Building Blocks**

- The weakness is that you will. _(javascriptallonge.pdf (source-range-83ecb080-00824))_
- There are ifs, fors, returns, everything thrown higgledy piggledy together. _(javascriptallonge.pdf (source-range-83ecb080-00824))_
- The strength of JavaScript is that you can do anything. _(javascriptallonge.pdf (source-range-83ecb080-00824))_
- Although you needn’t restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks. _(javascriptallonge.pdf (source-range-83ecb080-00824))_
- When you look at functions within functions in JavaScript, there’s a bit of a “spaghetti code” look to it. _(javascriptallonge.pdf (source-range-83ecb080-00824))_

### **composition**

- You can compose them with explicit JavaScript code as we’ve just done. _(javascriptallonge.pdf (source-range-83ecb080-00828))_
- It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. _(javascriptallonge.pdf (source-range-83ecb080-00828))_
- If that was all there was to it, composition wouldn’t matter much. _(javascriptallonge.pdf (source-range-83ecb080-00831))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-83ecb080-00831))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-83ecb080-00831))_
- In the recipes, we’ll look at a decorator called once: It ensures that a function can only be executed once. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- Once is useful for ensuring that certain side effects are not repeated. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- Thereafter, it does nothing. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- We’ll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined) as an argument. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- In the recipes, we’ll look at a decorator called once: It ensures that a function can only be executed once. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- But once and maybe compose, so you can chain them together as you see fit: _(javascriptallonge.pdf (source-range-83ecb080-00833))_

> **const** cookAndEat = (food) => eat(cook(food));
_(source: javascriptallonge.pdf (source-range-83ecb080-00827))_

> Context: It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators:
_(context: javascriptallonge.pdf (source-range-83ecb080-00828))_

> **const** compose = (a, b) => (c) => a(b(c));
_(source: javascriptallonge.pdf (source-range-83ecb080-00829))_

> Context: It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators:
_(context: javascriptallonge.pdf (source-range-83ecb080-00828))_

> **const** cookAndEat = compose(eat, cook);
_(source: javascriptallonge.pdf (source-range-83ecb080-00830))_

> Context: It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators:
_(context: javascriptallonge.pdf (source-range-83ecb080-00828))_

> The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.
_(source: javascriptallonge.pdf (source-range-83ecb080-00831))_

> Context: If that was all there was to it, composition wouldn’t matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.
_(context: javascriptallonge.pdf (source-range-83ecb080-00831))_

> Of course, you needn’t use combinators to implement either of these ideas, you can use if statements.
_(source: javascriptallonge.pdf (source-range-83ecb080-00833))_

> Context: Of course, you needn’t use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit:
_(context: javascriptallonge.pdf (source-range-83ecb080-00833))_

> - **const** actuallyTransfer= (from, to, amount) => _// do something_
_(source: javascriptallonge.pdf (source-range-83ecb080-00834))_

> Context: Of course, you needn’t use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit:
_(context: javascriptallonge.pdf (source-range-83ecb080-00833))_

> **const** invokeTransfer = once(maybe(actuallyTransfer(...)));
_(source: javascriptallonge.pdf (source-range-83ecb080-00835))_

### **partial application**

- Another basic building block is _partial application_ . _(javascriptallonge.pdf (source-range-83ecb080-00839))_
- In that case, we can’t get the final value, but we can get a function that represents _part_ of our application. _(javascriptallonge.pdf (source-range-83ecb080-00839))_
- The Underscore[39] library provides a higher-order function called _map_ .[40] It applies another function to each element of an array, like this: _(javascriptallonge.pdf (source-range-83ecb080-00840))_
- Code is easier than words for this. _(javascriptallonge.pdf (source-range-83ecb080-00840))_
- The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. _(javascriptallonge.pdf (source-range-83ecb080-00845))_
- mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-83ecb080-00845))_
- We can abstract this one level higher. _(javascriptallonge.pdf (source-range-83ecb080-00845))_
- The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely: _(javascriptallonge.pdf (source-range-83ecb080-00849))_
- > 40Modern JavaScript implementations provide a map method for arrays, but Underscore’s implementation also works with older browsers if you are working with that headache. _(javascriptallonge.pdf (source-range-83ecb080-00851))_
- Partial application also has a combinator, which we’ll see in the partial recipe. _(javascriptallonge.pdf (source-range-83ecb080-00858))_
- We generalized composition with the compose combinator. _(javascriptallonge.pdf (source-range-83ecb080-00858))_

> Context: Code is easier than words for this. The Underscore[39] library provides a higher-order function called _map_ .[40] It applies another function to each element of an array, like this: This code implements a partial application of the map function by applying the function (n) => n * n as its second argument:
_(context: javascriptallonge.pdf (source-range-83ecb080-00840, source-range-83ecb080-00843))_

> _.map([1, 2, 3], (n) => n * n) _//=> [1, 4, 9]_
_(source: javascriptallonge.pdf (source-range-83ecb080-00841))_

> Context: This code implements a partial application of the map function by applying the function (n) => n * n as its second argument:
_(context: javascriptallonge.pdf (source-range-83ecb080-00843))_

> **const** squareAll = (array) => map(array, (n) => n * n);
_(source: javascriptallonge.pdf (source-range-83ecb080-00844))_

> Context: The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.
_(context: javascriptallonge.pdf (source-range-83ecb080-00845))_

> **const** mapWith = (fn) => (array) => map(array, fn);
_(source: javascriptallonge.pdf (source-range-83ecb080-00846))_

> Context: The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.
_(context: javascriptallonge.pdf (source-range-83ecb080-00845))_

> **const** squareAll = mapWith((n) => n * n);
_(source: javascriptallonge.pdf (source-range-83ecb080-00847))_

> Context: The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.
_(context: javascriptallonge.pdf (source-range-83ecb080-00845))_

> squareAll([1, 2, 3]) _//=> [1, 4, 9]_
_(source: javascriptallonge.pdf (source-range-83ecb080-00848))_

> Context: > 41If we don’t want to sort out Underscore, we can also write the following: const map = (a, fn) => a.map(fn);, and trust that it works even though we haven’t discussed methods yet. const map = _.map;
_(context: javascriptallonge.pdf (source-range-83ecb080-00852))_

> **const** safeSquareAll = mapWith(maybe((n) => n * n));
_(source: javascriptallonge.pdf (source-range-83ecb080-00855))_

## Magic Names

### **Magic Names**

- When a function is applied to arguments (or “called”), JavaScript binds the values of arguments to the function’s argument names in an environment created for the function’s execution. _(javascriptallonge.pdf (source-range-83ecb080-00863))_
- What we haven’t discussed so far is that JavaScript also binds values to some “magic” names in addition to any you put in the argument list.[42] _(javascriptallonge.pdf (source-range-83ecb080-00863))_

### **the function keyword**

- There are two separate rules for these “magic” names, one for when you invoke a function using the function keyword, and another for functions defined with “fat arrows.” We’ll begin with how things work for functions defined with the function keyword. _(javascriptallonge.pdf (source-range-83ecb080-00865))_
- The second magic name is very interesting, it’s called arguments, and the most interesting thing about it is that it contains a list of arguments passed to a function: _(javascriptallonge.pdf (source-range-83ecb080-00866))_
- The first magic name is this, and it is bound to something called the function’s context. _(javascriptallonge.pdf (source-range-83ecb080-00866))_
- arguments always contains all of the arguments passed to a function, regardless of how many are declared. _(javascriptallonge.pdf (source-range-83ecb080-00870))_
- It is wise to treat them as read-only at all times. _(javascriptallonge.pdf (source-range-83ecb080-00871))_
- > 42You should never attempt to define your own bindings against “magic” names that JavaScript binds for you. _(javascriptallonge.pdf (source-range-83ecb080-00871))_
- It is wise to treat them as read-only at all times. _(javascriptallonge.pdf (source-range-83ecb080-00871))_
- The most common use of the arguments binding is to build functions that can take a variable number of arguments. _(javascriptallonge.pdf (source-range-83ecb080-00878))_
- We’ll see it used in many of the recipes, starting off with partial application and ellipses. _(javascriptallonge.pdf (source-range-83ecb080-00878))_

> Context: The first magic name is this, and it is bound to something called the function’s context. We will explore this in more detail when we start discussing objects and classes. The second magic name is very interesting, it’s called arguments, and the most interesting thing about it is that it contains a list of arguments passed to a function:
_(context: javascriptallonge.pdf (source-range-83ecb080-00866))_

> **const** plus = **function** (a, b) { **return** arguments[0] + arguments[1]; } plus(2,3) _//=> 5_
_(source: javascriptallonge.pdf (source-range-83ecb080-00867))_

> Context: Although arguments looks like an array, it isn’t an array: It’s more like an object[43] that happens to bind some values to properties with names that look like integers starting with zero: arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-00868, source-range-83ecb080-00870))_

> **const** args = **function** (a, b) { **return** arguments; } args(2,3) _//=> { '0': 2, '1': 3 }_
_(source: javascriptallonge.pdf (source-range-83ecb080-00869))_

> **const** plus = **function** () { **return** arguments[0] + arguments[1]; } plus(2,3) _//=> 5_
_(source: javascriptallonge.pdf (source-range-83ecb080-00875))_

> Context: When discussing objects, we’ll discuss properties in more depth. Here’s something interesting about arguments:
_(context: javascriptallonge.pdf (source-range-83ecb080-00876))_

> **const** howMany = **function** () { **return** arguments['length']; } howMany() _//=> 0_ howMany('hello') _//=> 1_ howMany('sharks', 'are', 'apex', 'predators') _//=> 4_
_(source: javascriptallonge.pdf (source-range-83ecb080-00877))_

### **magic names and fat arrows**

- For example, when this expression’s inner function is defined with function, arguments[0] refers to its only argument, "inner": _(javascriptallonge.pdf (source-range-83ecb080-00881))_
- For example, when this expression’s inner function is defined with function, arguments[0] refers to its only argument, "inner": _(javascriptallonge.pdf (source-range-83ecb080-00881))_
- But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function. _(javascriptallonge.pdf (source-range-83ecb080-00885))_
- Although it seems quixotic for the two syntaxes to have different semantics, it makes sense when you consider the design goal: Fat arrow functions are designed to be very lightweight and are often used with constructs like mapping or callbacks to emulate syntax. _(javascriptallonge.pdf (source-range-83ecb080-00887))_
- It uses mapWith, which we discussed in Building Blocks.[44] We’ll use arguments just to show the difference between using a fat arrow and the function keyword: _(javascriptallonge.pdf (source-range-83ecb080-00888))_
- To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. _(javascriptallonge.pdf (source-range-83ecb080-00888))_
- This works just fine, because arguments[0] refers to the 3 we passed to the function row. _(javascriptallonge.pdf (source-range-83ecb080-00890))_
- This works just fine, because arguments[0] refers to the 3 we passed to the function row. _(javascriptallonge.pdf (source-range-83ecb080-00890))_
- But for the purposes of discussing ideas, we can use the same name twice in two different contexts. _(javascriptallonge.pdf (source-range-83ecb080-00891))_
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. _(javascriptallonge.pdf (source-range-83ecb080-00891))_
- > 44Yes, we also used the name mapWith for working with ordinary collections elsewhere. _(javascriptallonge.pdf (source-range-83ecb080-00891))_
- It’s the same idea, after all. _(javascriptallonge.pdf (source-range-83ecb080-00891))_
- Sometimes, a function is meant to be used as a Big-F function. _(javascriptallonge.pdf (source-range-83ecb080-00896))_
- It has a name, it is called by different pieces of code, it’s a first-class entity in the code. _(javascriptallonge.pdf (source-range-83ecb080-00896))_
- Although this example is clearly unrealistic, there is a general design principle that deserves attention. _(javascriptallonge.pdf (source-range-83ecb080-00896))_
- It has a name, it is called by different pieces of code, it’s a first-class entity in the code. _(javascriptallonge.pdf (source-range-83ecb080-00896))_
- It’s a simple representation of an expression to be computed. _(javascriptallonge.pdf (source-range-83ecb080-00897))_
- In our example above, row is a Big-F function, but (column) => column * arguments[0] is a small-f function, it exists just to give mapWith something to apply. _(javascriptallonge.pdf (source-range-83ecb080-00897))_
- But sometimes, a function is a small-f function. _(javascriptallonge.pdf (source-range-83ecb080-00897))_
- Having magic variables apply to Big-F functions but not to small-G functions makes it much easier to use small-F functions as syntax, treating them as expressions or blocks that can be passed to functions like mapWith. _(javascriptallonge.pdf (source-range-83ecb080-00898))_

> Context: But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function. And thus arguments[0] will refer to "outer", not to "inner":
_(context: javascriptallonge.pdf (source-range-83ecb080-00885))_

> ( **function** () { **return** (() => arguments[0])('inner'); })('outer') _//=> "outer"_
_(source: javascriptallonge.pdf (source-range-83ecb080-00886))_

## Summary

### **Summary**

### **Functions**

- - Functions are values that can be part of expressions, returned from other functions, and so forth. _(javascriptallonge.pdf (source-range-83ecb080-00905))_
- - Functions are _reference values_ . _(javascriptallonge.pdf (source-range-83ecb080-00906))_
- - Functions are applied to arguments. _(javascriptallonge.pdf (source-range-83ecb080-00907))_
- - Fat arrow functions have expressions or blocks as their bodies. _(javascriptallonge.pdf (source-range-83ecb080-00909))_
- - function keyword functions always have blocks as their bodies. _(javascriptallonge.pdf (source-range-83ecb080-00910))_
- - Function bodies have zero or more statements. _(javascriptallonge.pdf (source-range-83ecb080-00911))_
- - Block bodies evaluate to whatever is returned with the return keyword, or to undefined. _(javascriptallonge.pdf (source-range-83ecb080-00913))_
- - JavaScript uses const to bind values to names within block scope. _(javascriptallonge.pdf (source-range-83ecb080-00914))_
- - JavaScript uses const to bind values to names within block scope. _(javascriptallonge.pdf (source-range-83ecb080-00914))_
- - JavaScript uses function declarations to bind functions to names within function scope. _(javascriptallonge.pdf (source-range-83ecb080-00915))_
- - JavaScript uses function declarations to bind functions to names within function scope. _(javascriptallonge.pdf (source-range-83ecb080-00915))_
- - Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-83ecb080-00917))_
- - Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-83ecb080-00917))_
- - Scopes are nested and free variable references closed over. _(javascriptallonge.pdf (source-range-83ecb080-00918))_
- - Variables can shadow variables in an enclosing scope. _(javascriptallonge.pdf (source-range-83ecb080-00919))_

## Recipes with Basic Functions

### **Recipes with Basic Functions**

- Having looked at basic pure functions and closures, we’re going to see some practical recipes that focus on the premise of functions that return functions. _(javascriptallonge.pdf (source-range-83ecb080-00924))_

### **Disclaimer**

- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven’t been discussed in the text to this point, such as methods and/or prototypes. _(javascriptallonge.pdf (source-range-83ecb080-00926))_
- The overall _use_ of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-83ecb080-00926))_
- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven’t been discussed in the text to this point, such as methods and/or prototypes. _(javascriptallonge.pdf (source-range-83ecb080-00926))_
- The overall _use_ of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-83ecb080-00926))_

## Partial Application

### **Partial Application**

- This is such a common tool that many libraries provide some form of partial application. _(javascriptallonge.pdf (source-range-83ecb080-00931))_
- In Building Blocks, we discussed partial application, but we didn’t write a generalized recipe for it. _(javascriptallonge.pdf (source-range-83ecb080-00931))_
- These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost.[48] If you want to bind more than one argument, or you want to leave a “hole” in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. _(javascriptallonge.pdf (source-range-83ecb080-00932))_
- As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware. _(javascriptallonge.pdf (source-range-83ecb080-00940))_
- We’d need a different recipe if we wish to create partial applications of object methods. _(javascriptallonge.pdf (source-range-83ecb080-00940))_
- > 48 callFirst and callLast were inspired by Michael Fogus’ Lemonad. _(javascriptallonge.pdf (source-range-83ecb080-00944))_
- We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument: _(javascriptallonge.pdf (source-range-83ecb080-00947))_

> Context: These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost.[48] If you want to bind more than one argument, or you want to leave a “hole” in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic.
_(context: javascriptallonge.pdf (source-range-83ecb080-00932))_

> **const** heliosSaysHello = callFirst(greet, 'Helios');
_(source: javascriptallonge.pdf (source-range-83ecb080-00934))_

> **const** sayHelloToCeline = callLast(greet, 'Celine');
_(source: javascriptallonge.pdf (source-range-83ecb080-00937))_

> Context: We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument:
_(context: javascriptallonge.pdf (source-range-83ecb080-00947))_

> **const** callLeft = (fn, ...args) =>
_(source: javascriptallonge.pdf (source-range-83ecb080-00948))_

> Context: We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument:
_(context: javascriptallonge.pdf (source-range-83ecb080-00947))_

> (...remainingArgs) => fn(...args, ...remainingArgs);
_(source: javascriptallonge.pdf (source-range-83ecb080-00949))_

> Context: We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument:
_(context: javascriptallonge.pdf (source-range-83ecb080-00947))_

> **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
_(source: javascriptallonge.pdf (source-range-83ecb080-00950))_

## Unary

### **Unary**

- “Unary” is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument. _(javascriptallonge.pdf (source-range-83ecb080-00955))_
- JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. _(javascriptallonge.pdf (source-range-83ecb080-00956))_
- The most common use case is to fix a problem. _(javascriptallonge.pdf (source-range-83ecb080-00956))_
- But some functions have optional second or even third arguments. _(javascriptallonge.pdf (source-range-83ecb080-00961))_
- And when you call parseInt with map, the index is interpreted as a radix. _(javascriptallonge.pdf (source-range-83ecb080-00963))_
- What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-83ecb080-00963))_
- What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-83ecb080-00963))_
- This doesn’t work because parseInt is defined as parseInt(string[, radix]). _(javascriptallonge.pdf (source-range-83ecb080-00963))_
- This doesn’t work because parseInt is defined as parseInt(string[, radix]). _(javascriptallonge.pdf (source-range-83ecb080-00963))_

> Context: The most common use case is to fix a problem. JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. Here it is in action:
_(context: javascriptallonge.pdf (source-range-83ecb080-00956))_

> ['1', '2', '3'].map(parseFloat) _//=> [1, 2, 3]_
_(source: javascriptallonge.pdf (source-range-83ecb080-00957))_

> Context: Let’s try it: This doesn’t work because parseInt is defined as parseInt(string[, radix]). It takes an optional radix argument. And when you call parseInt with map, the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.
_(context: javascriptallonge.pdf (source-range-83ecb080-00959, source-range-83ecb080-00963))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments.
_(source: javascriptallonge.pdf (source-range-83ecb080-00961))_

> Context: If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example: This doesn’t work because parseInt is defined as parseInt(string[, radix]). It takes an optional radix argument. And when you call parseInt with map, the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.
_(context: javascriptallonge.pdf (source-range-83ecb080-00961, source-range-83ecb080-00963))_

> ['1', '2', '3'].map(parseInt) _//=> [1, NaN, NaN]_
_(source: javascriptallonge.pdf (source-range-83ecb080-00962))_

> Context: This doesn’t work because parseInt is defined as parseInt(string[, radix]). It takes an optional radix argument. And when you call parseInt with map, the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.
_(context: javascriptallonge.pdf (source-range-83ecb080-00963))_

> We could write ['1', '2', '3'].map((s) => parseInt(s)), or we could come up with a decorator to do the job for us:
_(source: javascriptallonge.pdf (source-range-83ecb080-00964))_

> Context: We could write ['1', '2', '3'].map((s) => parseInt(s)), or we could come up with a decorator to do the job for us:
_(context: javascriptallonge.pdf (source-range-83ecb080-00964))_

> **const** unary = (fn) =>
_(source: javascriptallonge.pdf (source-range-83ecb080-00967))_

> fn.length === 1
_(source: javascriptallonge.pdf (source-range-83ecb080-00968))_

> Context: And now we can write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00970))_

> ['1', '2', '3'].map(unary(parseInt)) _//=> [1, 2, 3]_
_(source: javascriptallonge.pdf (source-range-83ecb080-00971))_

## Tap

### **Tap**

- It has some surprising applications. _(javascriptallonge.pdf (source-range-83ecb080-00979))_
- One is when you want to do something with a value for sideeffects, but keep the value around. _(javascriptallonge.pdf (source-range-83ecb080-00979))_
- tap is a traditional name borrowed from various Unix shell commands. _(javascriptallonge.pdf (source-range-83ecb080-00981))_
- tap can do more than just act as a debugging aid. _(javascriptallonge.pdf (source-range-83ecb080-00996))_

> **const** K = (x) => (y) => x;
_(source: javascriptallonge.pdf (source-range-83ecb080-00978))_

> Context: It has some surprising applications. One is when you want to do something with a value for sideeffects, but keep the value around. Behold:
_(context: javascriptallonge.pdf (source-range-83ecb080-00979))_

> **const** tap = (value) => (fn) => ( **typeof** (fn) === 'function' && fn(value), value )
_(source: javascriptallonge.pdf (source-range-83ecb080-00980))_

> Context: tap is a traditional name borrowed from various Unix shell commands. It takes a value and returns a function that always returns the value, but if you pass it a function, it executes the function for side-effects. Let’s see it in action as a poor-man’s debugger:
_(context: javascriptallonge.pdf (source-range-83ecb080-00981))_

> tap('espresso')((it) => { console.log(`Our drink is ' **${** it **}** '`) }); _//=> Our drink is 'espresso'_ 'espresso'
_(source: javascriptallonge.pdf (source-range-83ecb080-00982))_

> Context: It’s easy to turn off:
_(context: javascriptallonge.pdf (source-range-83ecb080-00983))_

> tap('espresso')(); _//=> 'espresso'_
_(source: javascriptallonge.pdf (source-range-83ecb080-00984))_

> Context: Libraries like Underscore[49] use a version of tap that is “uncurried:”
_(context: javascriptallonge.pdf (source-range-83ecb080-00985))_

> _.tap('espresso', (it) => console.log(`Our drink is ' **${** it **}** '`) ); _//=> Our drink is 'espresso'_ 'espresso'
_(source: javascriptallonge.pdf (source-range-83ecb080-00986))_

> Context: Now we can write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00992))_

> tap('espresso')((it) => { console.log(`Our drink is ' **${** it **}** '`) }); _//=> Our drink is 'espresso'_ 'espresso'
_(source: javascriptallonge.pdf (source-range-83ecb080-00993))_

## Maybe

### **Maybe**

- A common problem in programming is checking for null or undefined (hereafter called “nothing,” while all other values including 0, [] and false will be called “something”). _(javascriptallonge.pdf (source-range-83ecb080-01001))_
- Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-83ecb080-01001))_
- This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing: _(javascriptallonge.pdf (source-range-83ecb080-01002))_
- Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing: _(javascriptallonge.pdf (source-range-83ecb080-01007))_
- Naturally, there’s a function decorator recipe for that, borrowed from Haskell’s maybe monad[50] , Ruby’s andand[51] , and CoffeeScript’s existential method invocation: _(javascriptallonge.pdf (source-range-83ecb080-01009))_
- If some code ever tries to call model.setSomething with nothing, the operation will be skipped. _(javascriptallonge.pdf (source-range-83ecb080-01021))_

> Context: This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing:
_(context: javascriptallonge.pdf (source-range-83ecb080-01002))_

> **const** isSomething = (value) => value !== **null** && value !== **void** 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-01003))_

> Context: This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing:
_(context: javascriptallonge.pdf (source-range-83ecb080-01002))_

> **const** checksForSomething = (value) => { **if** (isSomething(value)) {
_(source: javascriptallonge.pdf (source-range-83ecb080-01004))_

> Context: Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing:
_(context: javascriptallonge.pdf (source-range-83ecb080-01007))_

> **var** something = isSomething(value) ? doesntCheckForSomething(value) : value;
_(source: javascriptallonge.pdf (source-range-83ecb080-01008))_

> Context: As a bonus, maybe plays very nicely with instance methods, we’ll discuss those later:
_(context: javascriptallonge.pdf (source-range-83ecb080-01018))_

> Model.prototype.setSomething = maybe( **function** (value) { **this** .something = value; });
_(source: javascriptallonge.pdf (source-range-83ecb080-01020))_

## Once

### **Once**

- It ensures that a function can only be called, well, _once_ . _(javascriptallonge.pdf (source-range-83ecb080-01026))_
- once is an extremely helpful combinator. _(javascriptallonge.pdf (source-range-83ecb080-01026))_
- It ensures that a function can only be called, well, _once_ . _(javascriptallonge.pdf (source-range-83ecb080-01026))_
- (Note: There are some subtleties with decorators like once that involve the intersection of state with methods. _(javascriptallonge.pdf (source-range-83ecb080-01034))_

> Context: Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let’s try it:
_(context: javascriptallonge.pdf (source-range-83ecb080-01028))_

> **const** askedOnBlindDate = once( () => "sure, why not?" ); askedOnBlindDate() _//=> 'sure, why not?'_
_(source: javascriptallonge.pdf (source-range-83ecb080-01029))_

> Context: Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let’s try it:
_(context: javascriptallonge.pdf (source-range-83ecb080-01028))_

> askedOnBlindDate() _//=> undefined_
_(source: javascriptallonge.pdf (source-range-83ecb080-01030))_

## Left-Variadic Functions

### **Left-Variadic Functions**

- A _variadic function_ is a function that is designed to accept a variable number of arguments.[52] In JavaScript, you can make a variadic function by gathering parameters. _(javascriptallonge.pdf (source-range-83ecb080-01039))_
- This can be useful when writing certain kinds of destructuring algorithms. _(javascriptallonge.pdf (source-range-83ecb080-01041))_
- For example, we might want to have a function that builds some kind of team record. _(javascriptallonge.pdf (source-range-83ecb080-01041))_
- For example, we might want to have a function that builds some kind of team record. _(javascriptallonge.pdf (source-range-83ecb080-01041))_

> Context: A _variadic function_ is a function that is designed to accept a variable number of arguments.[52] In JavaScript, you can make a variadic function by gathering parameters. For example:
_(context: javascriptallonge.pdf (source-range-83ecb080-01039))_

> **const** abccc = (a, b, ...c) => { console.log(a); console.log(b); console.log(c); }; abccc(1, 2, 3, 4, 5) 1 2 [3,4,5]
_(source: javascriptallonge.pdf (source-range-83ecb080-01040))_

### But we can’t go the other way around:

- > 52English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. _(javascriptallonge.pdf (source-range-83ecb080-01044))_
- ECMAScript 2015 only permits gathering parameters from the _end_ of the parameter list. _(javascriptallonge.pdf (source-range-83ecb080-01048))_

### **a history lesson**

- In “Ye Olde Days,”[53] JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice, or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. _(javascriptallonge.pdf (source-range-83ecb080-01050))_
- “Ye” in “Ye Olde,” was not actually spelled with a “Y” in days of old, it was spelled with a thorn, and is pronounced “the.” Another word, “Ye” in “Ye of little programming faith,” is pronounced “ye,” but it’s a different word altogether. _(javascriptallonge.pdf (source-range-83ecb080-01053))_
- This is a _right-variadic function_ , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument. _(javascriptallonge.pdf (source-range-83ecb080-01060))_

> Context: In “Ye Olde Days,”[53] JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice, or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. Here it is in all of its ECMAScript-5 glory:
_(context: javascriptallonge.pdf (source-range-83ecb080-01050))_

> **var** __slice = Array.prototype.slice;
_(source: javascriptallonge.pdf (source-range-83ecb080-01051))_

> Context: We don’t need rightVariadic any more, because instead of:
_(context: javascriptallonge.pdf (source-range-83ecb080-01056))_

> **var** firstAndButFirst = rightVariadic( **function** test (first, butFirst) { **return** [first, butFirst] });
_(source: javascriptallonge.pdf (source-range-83ecb080-01057))_

> Context: We now simply write:
_(context: javascriptallonge.pdf (source-range-83ecb080-01058))_

> **const** firstAndButFirst = (first, ...butFirst) => [first, butFirst];
_(source: javascriptallonge.pdf (source-range-83ecb080-01059))_

### **overcoming limitations**

- All left-variadic functions have one or more fixed arguments, and the rest are gathered into the leftmost argument. _(javascriptallonge.pdf (source-range-83ecb080-01064))_
- We sure can, by using the techniques from rightVariadic. _(javascriptallonge.pdf (source-range-83ecb080-01065))_
- Our leftVariadic function is a decorator that turns any function into a function that gathers parameters _from the left_ , instead of from the right. _(javascriptallonge.pdf (source-range-83ecb080-01072))_

> Context: It’s nice to have progress. But as noted above, we can’t write:
_(context: javascriptallonge.pdf (source-range-83ecb080-01062))_

> **const** butLastAndLast = (...butLast, last) => [butLast, last];
_(source: javascriptallonge.pdf (source-range-83ecb080-01063))_

> **const** butLastAndLast = leftVariadic((butLast, last) => [butLast, last]);
_(source: javascriptallonge.pdf (source-range-83ecb080-01070))_

### **left-variadic destructuring**

- Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. _(javascriptallonge.pdf (source-range-83ecb080-01074))_
- But we can write our own left-gathering function utility using the same principles without all the tedium: _(javascriptallonge.pdf (source-range-83ecb080-01084))_
- With leftGather, we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function. _(javascriptallonge.pdf (source-range-83ecb080-01086))_

> Context: Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. Another way is when assigning variables, like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-01074))_

> **const** [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid'];
_(source: javascriptallonge.pdf (source-range-83ecb080-01075))_

> Context: Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. Another way is when assigning variables, like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-01074))_

> first _//=> 'why'_ butFirst _//=> ["hello","there","little","droid"]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01076))_

> Context: As with parameters, we can’t gather values from the left when destructuring an array:
_(context: javascriptallonge.pdf (source-range-83ecb080-01077))_

> **const** [...butLast, last] = ['why', 'hello', 'there', 'little', 'droid']; _//=> Unexpected token_
_(source: javascriptallonge.pdf (source-range-83ecb080-01078))_

> Context: We could use leftVariadic the hard way:
_(context: javascriptallonge.pdf (source-range-83ecb080-01079))_

> **const** [butLast, last] = leftVariadic((butLast, last) => [butLast, last])(...['wh\ y', 'hello', 'there', 'little', 'droid']);
_(source: javascriptallonge.pdf (source-range-83ecb080-01082))_

> butLast _//=> ['why', 'hello', 'there', 'little']_ last _//=> 'droid'_
_(source: javascriptallonge.pdf (source-range-83ecb080-01083))_

## Picking the Bean: Choice and Truthiness

### **Picking the Bean: Choice and Truthiness**

- In addition to numbers, we often need to represent a much more basic idea of truth or falsehood. _(javascriptallonge.pdf (source-range-83ecb080-01091))_

### **true**

### **false**

- All values of true are === all other values of true. _(javascriptallonge.pdf (source-range-83ecb080-01097))_
- We can see that is the case by looking at some operators we can perform on boolean values, !, &&, and ||. _(javascriptallonge.pdf (source-range-83ecb080-01097))_
- true and false are value types. _(javascriptallonge.pdf (source-range-83ecb080-01097))_
- Now, note well: We have said what happens if you pass boolean values to !, &&, and ||, but we’ve said nothing about expressions or about passing other values. _(javascriptallonge.pdf (source-range-83ecb080-01103))_

> Context: true and false are value types. All values of true are === all other values of true. We can see that is the case by looking at some operators we can perform on boolean values, !, &&, and ||. To being with, ! is a unary prefix operator that negates its argument. So:
_(context: javascriptallonge.pdf (source-range-83ecb080-01097))_

> ! **true** _//=> false_ ! **false** _//=> true_
_(source: javascriptallonge.pdf (source-range-83ecb080-01100))_

### **truthiness and the ternary operator**

- So are null and undefined, values that semantically represent “no value.” NaN is falsy, a value representing the result of a calculation that is not a number.[54] And there are more: 0 is falsy, a value representing “none of something.” The empty string, '' is falsy, a value representing having no characters. _(javascriptallonge.pdf (source-range-83ecb080-01105))_
- In JavaScript, there is a notion of “truthiness.” Every value is either “truthy” or “falsy.” Obviously, false is falsy. _(javascriptallonge.pdf (source-range-83ecb080-01105))_
- Every other value in JavaScript is “truthy” except the aforementioned false, null, undefined, NaN, 0, and ''. _(javascriptallonge.pdf (source-range-83ecb080-01106))_
- (Many other languages that have a notion of truthiness consider zero and the empty string to be truthy, not falsy, so beware of blindly transliterating code from one language to another!) _(javascriptallonge.pdf (source-range-83ecb080-01106))_
- Every other value in JavaScript is “truthy” except the aforementioned false, null, undefined, NaN, 0, and ''. _(javascriptallonge.pdf (source-range-83ecb080-01106))_
- The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on _truthiness_ , not on boolean values. _(javascriptallonge.pdf (source-range-83ecb080-01107))_
- JavaScript inherited an operator from the C family of languages, the _ternary_ operator. _(javascriptallonge.pdf (source-range-83ecb080-01108))_
- It’s the only operator that takes _three_ arguments. _(javascriptallonge.pdf (source-range-83ecb080-01108))_
- and if first is “truthy”, it evaluates second and that is its value. _(javascriptallonge.pdf (source-range-83ecb080-01112))_
- If first is not truthy, it evaluates third and that is its value. _(javascriptallonge.pdf (source-range-83ecb080-01112))_
- This is a lot like the if statement, however it is an _expression_ , not a statement, and that can be very valuable. _(javascriptallonge.pdf (source-range-83ecb080-01113))_
- It also doesn’t introduce braces, and that can be a help or a hindrance if we want to introduce a new scope or use statements. _(javascriptallonge.pdf (source-range-83ecb080-01113))_
- The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. _(javascriptallonge.pdf (source-range-83ecb080-01119))_
- We certainly don’t want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true. _(javascriptallonge.pdf (source-range-83ecb080-01121))_
- We certainly don’t want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true. _(javascriptallonge.pdf (source-range-83ecb080-01121))_

> Context: Here’re some simple examples of the ternary operator:
_(context: javascriptallonge.pdf (source-range-83ecb080-01114))_

> - 0 ? 'Hello' : 'Good bye' _//=> 'Good bye'_
_(source: javascriptallonge.pdf (source-range-83ecb080-01117))_

> - [1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal' _//=> 'Pentatonic'_
_(source: javascriptallonge.pdf (source-range-83ecb080-01118))_

> Context: The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example:
_(context: javascriptallonge.pdf (source-range-83ecb080-01119))_

> **const** status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den';
_(source: javascriptallonge.pdf (source-range-83ecb080-01120))_

### **truthiness and operators**

- It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-83ecb080-01123))_
- Our logical operators !, &&, and || are a little more subtle than our examples above implied. _(javascriptallonge.pdf (source-range-83ecb080-01123))_
- Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. _(javascriptallonge.pdf (source-range-83ecb080-01128))_
- First, and unlike !, && and || do not necessarily evaluate to true or false. _(javascriptallonge.pdf (source-range-83ecb080-01133))_
- First, and unlike !, && and || do not necessarily evaluate to true or false. _(javascriptallonge.pdf (source-range-83ecb080-01133))_
- If we look at our examples above, we see that when we pass true and false to && and ||, we do indeed get true or false as a result. _(javascriptallonge.pdf (source-range-83ecb080-01140))_
- They don’t operate strictly on logical values, and they don’t commute: a || b is not always equal to b || a, and the same goes for &&. _(javascriptallonge.pdf (source-range-83ecb080-01146))_
- This is not a subtle distinction. _(javascriptallonge.pdf (source-range-83ecb080-01147))_

> But when we pass other values, we no longer get true or false:
_(source: javascriptallonge.pdf (source-range-83ecb080-01140))_

### **|| and && are control-flow operators**

- We’ve seen the ternary operator: It is a _control-flow_ operator, not a logical operator. _(javascriptallonge.pdf (source-range-83ecb080-01149))_
- The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. _(javascriptallonge.pdf (source-range-83ecb080-01159))_
- This is more than just an optimization. _(javascriptallonge.pdf (source-range-83ecb080-01159))_

> **const** even = (n) => n === 0 || (n !== 1 && even(n - 2))
_(source: javascriptallonge.pdf (source-range-83ecb080-01153))_

### **function parameters are eager**

- In contrast to the behaviour of the ternary operator, ||, and &&, function parameters are always : _eagerly evaluated_ _(javascriptallonge.pdf (source-range-83ecb080-01161))_
- In contrast to the behaviour of the ternary operator, ||, and &&, function parameters are always : _eagerly evaluated_ _(javascriptallonge.pdf (source-range-83ecb080-01161))_
- This leads to the infinite recursion we fear. _(javascriptallonge.pdf (source-range-83ecb080-01166))_
- If we need to have functions with control-flow semantics, we can pass anonymous functions. _(javascriptallonge.pdf (source-range-83ecb080-01167))_
- Here we’ve passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation. _(javascriptallonge.pdf (source-range-83ecb080-01171))_

> **const** or = (a, b) => a || b
_(source: javascriptallonge.pdf (source-range-83ecb080-01162))_

> **const** and = (a, b) => a && b
_(source: javascriptallonge.pdf (source-range-83ecb080-01163))_

> **const** even = (n) => or(n === 0, and(n !== 1, even(n - 2)))
_(source: javascriptallonge.pdf (source-range-83ecb080-01164))_

> even(42) _//=> Maximum call stack size exceeded._
_(source: javascriptallonge.pdf (source-range-83ecb080-01165))_

### **summary**

- - Logical operators are based on truthiness and falsiness, not the strict values true and false. _(javascriptallonge.pdf (source-range-83ecb080-01173))_
- - The ternary operator (?:), ||, and && are control flow operators, they do not always return true or false, and they have short-cut semantics. _(javascriptallonge.pdf (source-range-83ecb080-01175))_
- - Function invocation uses eager evaluation, so if we need to roll our own control-flow semantics, we pass it functions, not expressions. _(javascriptallonge.pdf (source-range-83ecb080-01176))_

## Composing and Decomposing Data

### **Composing and Decomposing Data**

- Recursion is the root of computation since it trades description for time.—Alan Perlis, Epigrams in Programming[55] _(javascriptallonge.pdf (source-range-83ecb080-01181))_

## Arrays and Destructuring Arguments

### **Arrays and Destructuring Arguments**

- Arrays are JavaScript’s “native” representation of lists. _(javascriptallonge.pdf (source-range-83ecb080-01187))_
- Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-83ecb080-01187))_
- While we have mentioned arrays briefly, we haven’t had a close look at them. _(javascriptallonge.pdf (source-range-83ecb080-01187))_
- Strings are important because they represent writing. _(javascriptallonge.pdf (source-range-83ecb080-01187))_
- Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-83ecb080-01187))_
- Strings are important because they represent writing. _(javascriptallonge.pdf (source-range-83ecb080-01187))_

### **array literals**

- JavaScript has a literal syntax for creating an array: The [ and ] characters. _(javascriptallonge.pdf (source-range-83ecb080-01189))_
- We can create an array with one or more _elements_ by placing them between the brackets and separating the items with commas. _(javascriptallonge.pdf (source-range-83ecb080-01192))_
- This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. _(javascriptallonge.pdf (source-range-83ecb080-01198))_
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-83ecb080-01198))_
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-83ecb080-01198))_
- We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements: _(javascriptallonge.pdf (source-range-83ecb080-01204))_
- Array literals are expressions, and arrays are _reference types_ . _(javascriptallonge.pdf (source-range-83ecb080-01204))_

> Context: Any expression will work:
_(context: javascriptallonge.pdf (source-range-83ecb080-01194))_

> [ 2, 3, 2 + 2 ] _//=> [2,3,4]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01195))_

> Context: Any expression will do, including names:
_(context: javascriptallonge.pdf (source-range-83ecb080-01199))_

> **const** wrap = (something) => [something];
_(source: javascriptallonge.pdf (source-range-83ecb080-01202))_

> wrap("lunch") _//=> ["lunch"]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01203))_

> Context: Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:
_(context: javascriptallonge.pdf (source-range-83ecb080-01204))_

> [] === [] _//=> false_ [2 + 2] === [2 + 2] _//=> false_
_(source: javascriptallonge.pdf (source-range-83ecb080-01205))_

> Context: Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:
_(context: javascriptallonge.pdf (source-range-83ecb080-01204))_

> **const** array_of_one = () => [1];
_(source: javascriptallonge.pdf (source-range-83ecb080-01206))_

> Context: Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:
_(context: javascriptallonge.pdf (source-range-83ecb080-01204))_

> array_of_one() === array_of_one() _//=> false_
_(source: javascriptallonge.pdf (source-range-83ecb080-01207))_

### **element references**

- Array elements can be extracted using [ and ] as postfix operators. _(javascriptallonge.pdf (source-range-83ecb080-01209))_
- As we can see, JavaScript Arrays are zero-based[56] . _(javascriptallonge.pdf (source-range-83ecb080-01212))_
- We know that every array is its own unique entity, with its own unique reference. _(javascriptallonge.pdf (source-range-83ecb080-01213))_

> Context: Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract:
_(context: javascriptallonge.pdf (source-range-83ecb080-01209))_

> **const** oneTwoThree = ["one", "two", "three"];
_(source: javascriptallonge.pdf (source-range-83ecb080-01210))_

> Context: Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract:
_(context: javascriptallonge.pdf (source-range-83ecb080-01209))_

> oneTwoThree[0] _//=> 'one'_ oneTwoThree[1] _//=> 'two'_ oneTwoThree[2] _//=> 'three'_
_(source: javascriptallonge.pdf (source-range-83ecb080-01211))_

> **const** x = [], a = [x];
_(source: javascriptallonge.pdf (source-range-83ecb080-01217))_

> a[0] === x
_(source: javascriptallonge.pdf (source-range-83ecb080-01218))_

### **destructuring arrays**

- There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-83ecb080-01221))_
- There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-83ecb080-01221))_
- The line const wrapped = [something]; is interesting. _(javascriptallonge.pdf (source-range-83ecb080-01227))_
- In JavaScript, we can actually _reverse_ the statement and place the template on the left and a value on the right: _(javascriptallonge.pdf (source-range-83ecb080-01228))_
- The statement const [something] = wrapped; _destructures_ the array represented by wrapped, binding the value of its single element to the name something. _(javascriptallonge.pdf (source-range-83ecb080-01232))_
- We could do the same thing with (name) => name[1], but destructuring is code that resembles the data it consumes, a valuable coding style. _(javascriptallonge.pdf (source-range-83ecb080-01237))_

> Context: There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. We saw how to construct an array literal using [, expressions, , and ]. Here’s an example of an array literal that uses a name:
_(context: javascriptallonge.pdf (source-range-83ecb080-01221))_

> **const** wrap = (something) => [something];
_(source: javascriptallonge.pdf (source-range-83ecb080-01222))_

> Context: Let’s expand it to use a block and an extra name:
_(context: javascriptallonge.pdf (source-range-83ecb080-01223))_

> **const** wrap = (something) => { **const** wrapped = [something];
_(source: javascriptallonge.pdf (source-range-83ecb080-01224))_

> Context: Let’s expand it to use a block and an extra name:
_(context: javascriptallonge.pdf (source-range-83ecb080-01223))_

> wrap("package") _//=> ["package"]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01226))_

> Context: In JavaScript, we can actually _reverse_ the statement and place the template on the left and a value on the right:
_(context: javascriptallonge.pdf (source-range-83ecb080-01228))_

> **const** unwrap = (wrapped) => { **const** [something] = wrapped;
_(source: javascriptallonge.pdf (source-range-83ecb080-01229))_

> Context: In JavaScript, we can actually _reverse_ the statement and place the template on the left and a value on the right:
_(context: javascriptallonge.pdf (source-range-83ecb080-01228))_

> unwrap(["present"]) _//=> "present"_
_(source: javascriptallonge.pdf (source-range-83ecb080-01231))_

> Context: The statement const [something] = wrapped; _destructures_ the array represented by wrapped, binding the value of its single element to the name something. We can do the same thing with more than one element:
_(context: javascriptallonge.pdf (source-range-83ecb080-01232))_

> **const** surname = (name) => { **const** [first, last] = name; **return** last; }
_(source: javascriptallonge.pdf (source-range-83ecb080-01235))_

> surname(["Reginald", "Braithwaite"]) _//=> "Braithwaite"_
_(source: javascriptallonge.pdf (source-range-83ecb080-01236))_

> Context: Destructuring can nest:
_(context: javascriptallonge.pdf (source-range-83ecb080-01238))_

> **const** description = (nameAndOccupation) => { **const** [[first, last], occupation] = nameAndOccupation;
_(source: javascriptallonge.pdf (source-range-83ecb080-01239))_

### **gathering**

- Here is the most common pattern: Extracting the head and gathering everything but the head from an array: _(javascriptallonge.pdf (source-range-83ecb080-01242))_
- Sometimes we need to extract arrays from arrays. _(javascriptallonge.pdf (source-range-83ecb080-01242))_
- car and cdr[57] are archaic terms that go back to an implementation of Lisp running on the IBM 704 computer. _(javascriptallonge.pdf (source-range-83ecb080-01245))_
- notation does not provide a universal patten-matching capability. _(javascriptallonge.pdf (source-range-83ecb080-01246))_
- Now, when we introduced destructuring, we saw that it is kind-of-sort-of the reverse of array literals. _(javascriptallonge.pdf (source-range-83ecb080-01252))_
- to place the elements of an array inside another array. _(javascriptallonge.pdf (source-range-83ecb080-01262))_

> Context: Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array:
_(context: javascriptallonge.pdf (source-range-83ecb080-01242))_

> **const** [car, ...cdr] = [1, 2, 3, 4, 5];
_(source: javascriptallonge.pdf (source-range-83ecb080-01243))_

> Context: Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array:
_(context: javascriptallonge.pdf (source-range-83ecb080-01242))_

> car _//=> 1_ cdr _//=> [2, 3, 4, 5]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01244))_

> **const** [...butLast, last] = [1, 2, 3, 4, 5]; _//=> ERROR_ **const** [first, ..., last] = [1, 2, 3, 4, 5]; _//=> ERROR_
_(source: javascriptallonge.pdf (source-range-83ecb080-01251))_

> **const** wrapped = [something];
_(source: javascriptallonge.pdf (source-range-83ecb080-01253))_

> **const** [unwrapped] = something;
_(source: javascriptallonge.pdf (source-range-83ecb080-01255))_

> Context: What is the reverse of gathering? We know that:
_(context: javascriptallonge.pdf (source-range-83ecb080-01256))_

> **const** [car, ...cdr] = [1, 2, 3, 4, 5];
_(source: javascriptallonge.pdf (source-range-83ecb080-01257))_

> Context: What is the reverse? It would be:
_(context: javascriptallonge.pdf (source-range-83ecb080-01258))_

> **const** cons = [car, ...cdr];
_(source: javascriptallonge.pdf (source-range-83ecb080-01259))_

> **const** oneTwoThree = ["one", "two", "three"]; ["zero", ...oneTwoThree] _//=> ["zero","one","two","three"]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01261))_

### **destructuring is not pattern matching**

- If it does, assignments are made where appropriate. _(javascriptallonge.pdf (source-range-83ecb080-01264))_
- JavaScript tries its best to assign things, and if there isn’t something that fits, JavaScript binds undefined to the name. _(javascriptallonge.pdf (source-range-83ecb080-01269))_
- But this is not how JavaScript works. _(javascriptallonge.pdf (source-range-83ecb080-01269))_
- That match would fail because the array doesn’t have an element to assign to what. _(javascriptallonge.pdf (source-range-83ecb080-01269))_
- That match would fail because the array doesn’t have an element to assign to what. _(javascriptallonge.pdf (source-range-83ecb080-01269))_
- As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. _(javascriptallonge.pdf (source-range-83ecb080-01274))_
- From its very inception, JavaScript has striven to avoid catastrophic errors. _(javascriptallonge.pdf (source-range-83ecb080-01274))_
- This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-83ecb080-01274))_
- This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-83ecb080-01274))_

> Context: That match would fail because the array doesn’t have an element to assign to what. But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn’t something that fits, JavaScript binds undefined to the name. Therefore:
_(context: javascriptallonge.pdf (source-range-83ecb080-01269))_

> what _//=> undefined_ **const** [which, what, who] = ["duck feet", "tiger tail"]; who _//=> undefined_
_(source: javascriptallonge.pdf (source-range-83ecb080-01271))_

> Context: And if there aren’t any items to assign with ..., JavaScript assigns an empty array: From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.
_(context: javascriptallonge.pdf (source-range-83ecb080-01272, source-range-83ecb080-01274))_

> **const** [...they] = []; they _//=> []_ **const** [which, what, ...they] = ["duck feet", "tiger tail"]; they _//=> []_
_(source: javascriptallonge.pdf (source-range-83ecb080-01273))_

### **destructuring and return values**

> **const** [reg, status] = description([["Reginald", "Braithwaite"], "programmer"]);
_(source: javascriptallonge.pdf (source-range-83ecb080-01280))_

> reg _//=> "Reginald is a programmer"_ status _//=> "ok"_
_(source: javascriptallonge.pdf (source-range-83ecb080-01281))_

### **destructuring parameters**

- There is only one difference: We have not tried gathering. _(javascriptallonge.pdf (source-range-83ecb080-01287))_
- There is only one difference: We have not tried gathering. _(javascriptallonge.pdf (source-range-83ecb080-01287))_
- 59Gathering in parameters has a long history, and the usual terms are to call gathering “pattern matching” and to call a name that is bound to gathered values a “rest parameter.” The term “rest” is perfectly compatible with gather: “Rest” is the noun, and “gather” is the verb. _(javascriptallonge.pdf (source-range-83ecb080-01292))_

> Context: It is very much like an array literal. And consider how we bind values to parameter names:
_(context: javascriptallonge.pdf (source-range-83ecb080-01285))_

> **const** foo = () => ... **const** bar = (name) => ... **const** baz = (a, b, c) => ...
_(source: javascriptallonge.pdf (source-range-83ecb080-01286))_

## Self-Similarity

### **Self-Similarity**

- Recursion is the root of computation since it trades description for time.—Alan Perlis, Epigrams in Programming[60] _(javascriptallonge.pdf (source-range-83ecb080-01297))_
- In Arrays and Destructuring Arguments, we worked with the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-83ecb080-01298))_
- We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-83ecb080-01299))_
- Let’s be more specific. _(javascriptallonge.pdf (source-range-83ecb080-01300))_
- Some data structures, like lists, can obviously be seen as a collection of items. _(javascriptallonge.pdf (source-range-83ecb080-01300))_
- Some are empty, some have three items, some forty-two, some contain numbers, some contain strings, some a mixture of elements, there are all kinds of lists. _(javascriptallonge.pdf (source-range-83ecb080-01300))_
- But we can also define a list by describing a rule for building lists. _(javascriptallonge.pdf (source-range-83ecb080-01301))_
- The first rule is simple: [] is a list. _(javascriptallonge.pdf (source-range-83ecb080-01304))_
- We can express that using a spread. _(javascriptallonge.pdf (source-range-83ecb080-01304))_
- Given an element e and a list list, [e, ...list] is a list. _(javascriptallonge.pdf (source-range-83ecb080-01304))_
- Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists: _(javascriptallonge.pdf (source-range-83ecb080-01306))_
- > 61 Well, actually, this does not work for arrays that contain undefined as a value, but we are not going to see that in our examples. _(javascriptallonge.pdf (source-range-83ecb080-01315))_
- If only there was a function we could call… Like length! _(javascriptallonge.pdf (source-range-83ecb080-01321))_
- We need something for when the array isn’t empty. _(javascriptallonge.pdf (source-range-83ecb080-01321))_
- If an array is not empty, and we break it into two pieces, first and rest, the length of our array is going to be length(first) + length(rest). _(javascriptallonge.pdf (source-range-83ecb080-01321))_
- Well, the length of first is 1, there’s just one element at the front. _(javascriptallonge.pdf (source-range-83ecb080-01321))_
- If only there was a function we could call… Like length! _(javascriptallonge.pdf (source-range-83ecb080-01321))_
- This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-83ecb080-01325))_
- Our length function is _recursive_ , it calls itself. _(javascriptallonge.pdf (source-range-83ecb080-01325))_
- This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-83ecb080-01325))_

> Context: For the purpose of this exploration, we will presume the following:[61]
_(context: javascriptallonge.pdf (source-range-83ecb080-01311))_

> **const** isEmpty = ([first, ...rest]) => first === **undefined** ;
_(source: javascriptallonge.pdf (source-range-83ecb080-01312))_

> Context: For the purpose of this exploration, we will presume the following:[61]
_(context: javascriptallonge.pdf (source-range-83ecb080-01311))_

> isEmpty([]) _//=> true_ isEmpty([0]) _//=> false_ isEmpty([[]]) _//=> false_
_(source: javascriptallonge.pdf (source-range-83ecb080-01313))_

> Context: First, we pick what we call a _terminal case_ . What is the length of an empty array? 0. So let’s start our function with the observation that if an array is empty, the length is 0:
_(context: javascriptallonge.pdf (source-range-83ecb080-01319))_

> **const** length = ([first, ...rest]) => first === **undefined** ? 0 : _// ???_
_(source: javascriptallonge.pdf (source-range-83ecb080-01320))_

> Context: First, we pick what we call a _terminal case_ . What is the length of an empty array? 0. So let’s start our function with the observation that if an array is empty, the length is 0:
_(context: javascriptallonge.pdf (source-range-83ecb080-01319))_

> **const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest);
_(source: javascriptallonge.pdf (source-range-83ecb080-01322))_

> Context: Let’s try it! Our length function is _recursive_ , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.
_(context: javascriptallonge.pdf (source-range-83ecb080-01323, source-range-83ecb080-01325))_

> length([]) _//=> 0_ length(["foo"]) _//=> 1_ length(["foo", "bar", "baz"]) _//=> 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-01324))_

### **linear recursion**

- There is more to recursive solutions that simply functions that invoke themselves. _(javascriptallonge.pdf (source-range-83ecb080-01333))_
- When all small problems have been solved, compose the solutions into one big solution _(javascriptallonge.pdf (source-range-83ecb080-01337))_
- Our solutions are a little simpler in that we don’t really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. _(javascriptallonge.pdf (source-range-83ecb080-01338))_
- The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. _(javascriptallonge.pdf (source-range-83ecb080-01338))_
- The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. _(javascriptallonge.pdf (source-range-83ecb080-01338))_
- Our solutions are a little simpler in that we don’t really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. _(javascriptallonge.pdf (source-range-83ecb080-01338))_
- This simpler form of “divide and conquer” is called _linear recursion_ . _(javascriptallonge.pdf (source-range-83ecb080-01339))_
- Sometimes we want to _flatten_ an array, that is, an array of arrays needs to be turned into one array of elements that aren’t arrays.[62] _(javascriptallonge.pdf (source-range-83ecb080-01339))_
- This simpler form of “divide and conquer” is called _linear recursion_ . _(javascriptallonge.pdf (source-range-83ecb080-01339))_
- We need a test for the terminal case. _(javascriptallonge.pdf (source-range-83ecb080-01340))_
- The usual “terminal case” will be that flattening an empty array will produce an empty array. _(javascriptallonge.pdf (source-range-83ecb080-01345))_
- The next terminal case is that if an element isn’t an array, we don’t flatten it, and can put it together with the rest of our solution directly. _(javascriptallonge.pdf (source-range-83ecb080-01345))_
- > 62 flatten is a very simple unfold, a function that takes a seed value and turns it into an array. _(javascriptallonge.pdf (source-range-83ecb080-01347))_
- Unfolds can be thought of a “path” through a data structure, and flattening a tree is equivalent to a depth-first traverse. _(javascriptallonge.pdf (source-range-83ecb080-01347))_
- Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions. _(javascriptallonge.pdf (source-range-83ecb080-01351))_

### **mapping**

- JavaScript has a built-in function for this, but let’s write our own using linear recursion. _(javascriptallonge.pdf (source-range-83ecb080-01353))_
- Another common problem is applying a function to every element of an array. _(javascriptallonge.pdf (source-range-83ecb080-01353))_
- Functions can take functions as arguments, so let’s “extract” the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together. _(javascriptallonge.pdf (source-range-83ecb080-01362))_
- This specific case of linear recursion is called “mapping,” and it is not necessary to constantly write out the same pattern again and again. _(javascriptallonge.pdf (source-range-83ecb080-01362))_
- This specific case of linear recursion is called “mapping,” and it is not necessary to constantly write out the same pattern again and again. _(javascriptallonge.pdf (source-range-83ecb080-01362))_
- We can write it out using a ternary operator. _(javascriptallonge.pdf (source-range-83ecb080-01365))_
- Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution. _(javascriptallonge.pdf (source-range-83ecb080-01365))_

> Context: If we want to square each number in a list, we could write:
_(context: javascriptallonge.pdf (source-range-83ecb080-01354))_

> **const** squareAll = ([first, ...rest]) => first === **undefined** ? [] : [first * first, ...squareAll(rest)\ ]; squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01355))_

> Context: And if we wanted to “truthify” each element in a list, we could write:
_(context: javascriptallonge.pdf (source-range-83ecb080-01356))_

> **const** truthyAll = ([first, ...rest]) => first === **undefined**
_(source: javascriptallonge.pdf (source-range-83ecb080-01359))_

> truthyAll([ **null** , **true** , 25, **false** , "foo"]) _//=> [false,true,true,false,true]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01361))_

> Context: Given the signature:
_(context: javascriptallonge.pdf (source-range-83ecb080-01363))_

> **const** mapWith = (fn, array) => _// ..._
_(source: javascriptallonge.pdf (source-range-83ecb080-01364))_

> Context: We can write it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution.
_(context: javascriptallonge.pdf (source-range-83ecb080-01365))_

> mapWith((x) => !!x, [ **null** , **true** , 25, **false** , "foo"]) _//=> [false,true,true,false,true]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01367))_

### **folding**

- A function to compute the sum of the squares of a list of numbers might look like this: _(javascriptallonge.pdf (source-range-83ecb080-01369))_
- Let’s rewrite mapWith so that we can use it to sum squares. _(javascriptallonge.pdf (source-range-83ecb080-01378))_
- And now we supply a function that does slightly more than our mapping functions: _(javascriptallonge.pdf (source-range-83ecb080-01380))_
- We can represent a map as a fold, we just need to supply the array rebuilding code: _(javascriptallonge.pdf (source-range-83ecb080-01382))_
- Our foldWith function is a generalization of our mapWith function. _(javascriptallonge.pdf (source-range-83ecb080-01382))_
- And to return to our first example, our version of length can be written as a fold: _(javascriptallonge.pdf (source-range-83ecb080-01389))_

> Context: With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn’t. A function to compute the sum of the squares of a list of numbers might look like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-01369))_

> **const** sumSquares = ([first, ...rest]) => first === **undefined**
_(source: javascriptallonge.pdf (source-range-83ecb080-01372))_

> Context: There are two differences between sumSquares and our maps above:
_(context: javascriptallonge.pdf (source-range-83ecb080-01375))_

> sumSquares([1, 2, 3, 4, 5]) _//=> 55_
_(source: javascriptallonge.pdf (source-range-83ecb080-01374))_

> Context: Let’s rewrite mapWith so that we can use it to sum squares.
_(context: javascriptallonge.pdf (source-range-83ecb080-01378))_

> **const** foldWith = (fn, terminalValue, [first, ...rest]) => first === **undefined** ? terminalValue : fn(first, foldWith(fn, terminalValue, rest));
_(source: javascriptallonge.pdf (source-range-83ecb080-01379))_

> Context: And now we supply a function that does slightly more than our mapping functions:
_(context: javascriptallonge.pdf (source-range-83ecb080-01380))_

> foldWith((number, rest) => number * number + rest, 0, [1, 2, 3, 4, 5]) _//=> 55_
_(source: javascriptallonge.pdf (source-range-83ecb080-01381))_

> Context: Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code:
_(context: javascriptallonge.pdf (source-range-83ecb080-01382))_

> **const** squareAll = (array) => foldWith((first, rest) => [first * first, ...rest],\ [], array); squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01383))_

> Context: And if we like, we can write mapWith using foldWith:
_(context: javascriptallonge.pdf (source-range-83ecb080-01384))_

> **const** mapWith = (fn, array) => foldWith((first, rest) => [fn(first), ...rest], [\ ], array), squareAll = (array) => mapWith((x) => x * x, array);
_(source: javascriptallonge.pdf (source-range-83ecb080-01387))_

> squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01388))_

> Context: And to return to our first example, our version of length can be written as a fold:
_(context: javascriptallonge.pdf (source-range-83ecb080-01389))_

> **const** length = (array) => foldWith((first, rest) => 1 + rest, 0, array);
_(source: javascriptallonge.pdf (source-range-83ecb080-01390))_

> Context: And to return to our first example, our version of length can be written as a fold:
_(context: javascriptallonge.pdf (source-range-83ecb080-01389))_

> length([1, 2, 3, 4, 5]) _//=> 5_
_(source: javascriptallonge.pdf (source-range-83ecb080-01391))_

### **summary**

- Linear recursion is a basic building block of algorithms. _(javascriptallonge.pdf (source-range-83ecb080-01393))_
- Its specialized cases of mapping and folding are especially useful and can be used to build other functions. _(javascriptallonge.pdf (source-range-83ecb080-01393))_
- Its basic form parallels the way linear data structures like lists are constructed: This helps make it understandable. _(javascriptallonge.pdf (source-range-83ecb080-01393))_
- And finally, while folding is a special case of linear recursion, mapping is a special case of folding. _(javascriptallonge.pdf (source-range-83ecb080-01393))_

## Tail Calls (and Default Arguments)

### **Tail Calls (and Default Arguments)**

- The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustrating the basic principles behind using recursion to work with self-similar data structures, but they are not “production-ready” implementations. _(javascriptallonge.pdf (source-range-83ecb080-01398))_
- One of the reasons they are not production-ready is that they consume memory proportional to the size of the array being folded. _(javascriptallonge.pdf (source-range-83ecb080-01398))_
- First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. _(javascriptallonge.pdf (source-range-83ecb080-01401))_
- To do that, it has to evaluate fn(first) and mapWith(fn, rest), then evaluate [fn(first), ...mapWith(fn, rest)]. _(javascriptallonge.pdf (source-range-83ecb080-01401))_
- first is not undefined, so it evaluates [fn(first), …mapWith(fn, rest)]. _(javascriptallonge.pdf (source-range-83ecb080-01401))_
- To do that, it has to evaluate fn(first) and mapWith(fn, rest), then evaluate [fn(first), ...mapWith(fn, rest)]. _(javascriptallonge.pdf (source-range-83ecb080-01401))_
- So we know that JavaScript is going to hang on to 1. _(javascriptallonge.pdf (source-range-83ecb080-01404))_
- JavaScript cannot throw first away. _(javascriptallonge.pdf (source-range-83ecb080-01404))_
- Next, JavaScript invokes mapWith(fn, rest), which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]). _(javascriptallonge.pdf (source-range-83ecb080-01405))_
- depending on the implementation), plus some housekeeping information so it remembers what to do with that value, while it calls the equivalent of mapWith((x) => x * x, [3, 4, 5]). _(javascriptallonge.pdf (source-range-83ecb080-01408))_
- It can start assembling the resulting array and start discarding the information it is saving. _(javascriptallonge.pdf (source-range-83ecb080-01409))_
- Furthermore, doubling the length of an array will double the amount of space we need on the stack, plus double all the work required to set up and tear down the housekeeping data for each call (these are called _call frames_ , and they include the place where the function was called, an environment, and so on). _(javascriptallonge.pdf (source-range-83ecb080-01410))_
- That information is saved on a _call stack_ , and it is quite expensive. _(javascriptallonge.pdf (source-range-83ecb080-01410))_
- In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error. _(javascriptallonge.pdf (source-range-83ecb080-01411))_
- Making algorithms faster is a very highly studied field of computer science. _(javascriptallonge.pdf (source-range-83ecb080-01414))_
- In fact, there are several better ways. _(javascriptallonge.pdf (source-range-83ecb080-01414))_

> Context: This is roughly equivalent to writing:
_(context: javascriptallonge.pdf (source-range-83ecb080-01402))_

> Note that while evaluating mapWith(fn, rest), JavaScript must retain the value first or fn(first), plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result.
_(source: javascriptallonge.pdf (source-range-83ecb080-01404))_

> Context: In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error.
_(context: javascriptallonge.pdf (source-range-83ecb080-01411))_

> mapWith((x) => x * x, [
_(source: javascriptallonge.pdf (source-range-83ecb080-01412))_

### **tail-call optimization**

- This is a tail-call, because it invokes another function and returns its result. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- It isn’t going to do any more work, so it can throw its existing stack frame away. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- There are three places it returns. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- This is interesting, because after sorting out what to supply as arguments (this, args), JavaScript can throw away everything in its current stack frame. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- But the third is fn.apply(this, args). _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- This is interesting, because after sorting out what to supply as arguments (this, args), JavaScript can throw away everything in its current stack frame. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- This is a tail-call, because it invokes another function and returns its result. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- This is a very important characteristic of JavaScript: **If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space.** _(javascriptallonge.pdf (source-range-83ecb080-01421))_
- And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe-wrapped call. _(javascriptallonge.pdf (source-range-83ecb080-01421))_
- That is excellent, but one wrapping is not a big deal. _(javascriptallonge.pdf (source-range-83ecb080-01422))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest). _(javascriptallonge.pdf (source-range-83ecb080-01424))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest). _(javascriptallonge.pdf (source-range-83ecb080-01424))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length, the other happens after the recursive call. _(javascriptallonge.pdf (source-range-83ecb080-01425))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length, the other happens after the recursive call. _(javascriptallonge.pdf (source-range-83ecb080-01425))_

> Context: That is excellent, but one wrapping is not a big deal. When would we really care? Consider this implementation of length: The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest).
_(context: javascriptallonge.pdf (source-range-83ecb080-01422, source-range-83ecb080-01424))_

> **const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest);
_(source: javascriptallonge.pdf (source-range-83ecb080-01423))_

### **converting non-tail-calls to tail-calls**

- The obvious solution is push the 1 + work into the call to length. _(javascriptallonge.pdf (source-range-83ecb080-01430))_
- The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. _(javascriptallonge.pdf (source-range-83ecb080-01436))_
- Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. _(javascriptallonge.pdf (source-range-83ecb080-01436))_
- The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. _(javascriptallonge.pdf (source-range-83ecb080-01436))_
- This version of length calls uses lengthDelaysWork, and JavaScript optimizes that not to take up memory proportional to the length of the string. _(javascriptallonge.pdf (source-range-83ecb080-01444))_
- We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. _(javascriptallonge.pdf (source-range-83ecb080-01459))_
- And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization. _(javascriptallonge.pdf (source-range-83ecb080-01459))_

> Context: The obvious solution is push the 1 + work into the call to length. Here’s our first cut:
_(context: javascriptallonge.pdf (source-range-83ecb080-01430))_

> **const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined**
_(source: javascriptallonge.pdf (source-range-83ecb080-01431))_

> Context: This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. But while we’re doing that, it’s annoying to remember to call it with a zero. Let’s fix that:
_(context: javascriptallonge.pdf (source-range-83ecb080-01436))_

> **const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined**
_(source: javascriptallonge.pdf (source-range-83ecb080-01437))_

> Context: This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. But while we’re doing that, it’s annoying to remember to call it with a zero. Let’s fix that:
_(context: javascriptallonge.pdf (source-range-83ecb080-01436))_

> **const** length = (n) => lengthDelaysWork(n, 0);
_(source: javascriptallonge.pdf (source-range-83ecb080-01439))_

> Context: Or we could use partial application:
_(context: javascriptallonge.pdf (source-range-83ecb080-01440))_

> **const** callLast = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
_(source: javascriptallonge.pdf (source-range-83ecb080-01441))_

> Context: Or we could use partial application:
_(context: javascriptallonge.pdf (source-range-83ecb080-01440))_

> **const** length = callLast(lengthDelaysWork, 0);
_(source: javascriptallonge.pdf (source-range-83ecb080-01442))_

> Context: Or we could use partial application:
_(context: javascriptallonge.pdf (source-range-83ecb080-01440))_

> length(["foo", "bar", "baz"]) _//=> 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-01443))_

> Context: This version of length calls uses lengthDelaysWork, and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith:
_(context: javascriptallonge.pdf (source-range-83ecb080-01444))_

> **const** mapWithDelaysWork = (fn, [first, ...rest], prepend) =>
_(source: javascriptallonge.pdf (source-range-83ecb080-01447))_

> first === **undefined**
_(source: javascriptallonge.pdf (source-range-83ecb080-01448))_

> **const** mapWith = callLast(mapWithDelaysWork, []);
_(source: javascriptallonge.pdf (source-range-83ecb080-01451))_

> mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01452))_

> Context: We can use it with ridiculously large arrays:
_(context: javascriptallonge.pdf (source-range-83ecb080-01453))_

> mapWith((x) => x * x, [
_(source: javascriptallonge.pdf (source-range-83ecb080-01454))_

> Context: We can use it with ridiculously large arrays:
_(context: javascriptallonge.pdf (source-range-83ecb080-01453))_

| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |

<details>
<summary>Raw table text</summary>

```
|0,|1,|2,|3,|4,|5,|6,|7,|8,|9,|
|---|---|---|---|---|---|---|---|---|---|
|10,|11,|12,|13,|14,|15,|16,|17,|18,|19,|
|20,|21,|22,|23,|24,|25,|26,|27,|28,|29,|
|30,|31,|32,|33,|34,|35,|36,|37,|38,|39,|
|40,|41,|42,|43,|44,|45,|46,|47,|48,|49,|
|50,|51,|52,|53,|54,|55,|56,|57,|58,|59,|
|60,|61,|62,|63,|64,|65,|66,|67,|68,|69,|
|70,|71,|72,|73,|74,|75,|76,|77,|78,|79,|
|80,|81,|82,|83,|84,|85,|86,|87,|88,|89,|
|90,|91,|92,|93,|94,|95,|96,|97,|98,|99,|
```

</details>
_(source: javascriptallonge.pdf (source-range-83ecb080-01455))_

### **factorials**

- In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. _(javascriptallonge.pdf (source-range-83ecb080-01462))_
- While this is mathematically elegant, it is computational filigree[63] . _(javascriptallonge.pdf (source-range-83ecb080-01469))_
- Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n - 1). _(javascriptallonge.pdf (source-range-83ecb080-01470))_
- As before, we wrote a factorialWithDelayedWork function, then used partial application (callLast) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-83ecb080-01479))_
- As before, we wrote a factorialWithDelayedWork function, then used partial application (callLast) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-83ecb080-01479))_

> Context: In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example:
_(context: javascriptallonge.pdf (source-range-83ecb080-01462))_

| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |

<details>
<summary>Raw table text</summary>

```
| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |
```

</details>
_(source: javascriptallonge.pdf (source-range-83ecb080-01463))_

> Context: The naïve function for calcuating the factorial of a positive integer follows directly from the definition: Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n - 1). We can do the same conversion, pass in the work to be done:
_(context: javascriptallonge.pdf (source-range-83ecb080-01467, source-range-83ecb080-01470))_

> **const** factorial = (n) => n == 1 ? n : n * factorial(n - 1); factorial(1) _//=> 1_ factorial(5) _//=> 120_
_(source: javascriptallonge.pdf (source-range-83ecb080-01468))_

> **const** callLast = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
_(source: javascriptallonge.pdf (source-range-83ecb080-01476))_

> **const** factorial = callLast(factorialWithDelayedWork, 1);
_(source: javascriptallonge.pdf (source-range-83ecb080-01477))_

> factorial(1) _//=> 1_ factorial(5) _//=> 120_
_(source: javascriptallonge.pdf (source-range-83ecb080-01478))_

### **default arguments**

- But when it calls itself, it will call factorial(5, 6) and that will not mean factorial(5, 1). _(javascriptallonge.pdf (source-range-83ecb080-01484))_
- What we really want is this: We want to write something like factorial(6), and have JavaScript automatically know that we really mean factorial(6, 1). _(javascriptallonge.pdf (source-range-83ecb080-01484))_
- JavaScript provides this exact syntax, it’s called a _default argument_ , and it looks like this: _(javascriptallonge.pdf (source-range-83ecb080-01485))_
- A default argument is concise and readable. _(javascriptallonge.pdf (source-range-83ecb080-01491))_
- Now we don’t need to use two functions. _(javascriptallonge.pdf (source-range-83ecb080-01491))_

> Context: Our problem is that we can directly write:
_(context: javascriptallonge.pdf (source-range-83ecb080-01481))_

> But it is hideous to have to always add a 1 parameter, we’d be demanding that everyone using the factorial function know that we are using a tail-recursive implementation.
_(source: javascriptallonge.pdf (source-range-83ecb080-01483))_

### **defaults and destructuring**

- Now we learn that we can create a default parameter argument. _(javascriptallonge.pdf (source-range-83ecb080-01493))_
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-83ecb080-01500))_

> Context: We saw earlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we create a default destructuring assignment?
_(context: javascriptallonge.pdf (source-range-83ecb080-01493))_

> **const** [first, second = "two"] = ["one"];
_(source: javascriptallonge.pdf (source-range-83ecb080-01496))_

> ` ` **${** first **}** . **${** second **}** _//=> "one . two"_
_(source: javascriptallonge.pdf (source-range-83ecb080-01497))_

> **const** [first, second = "two"] = ["primus", "secundus"];
_(source: javascriptallonge.pdf (source-range-83ecb080-01498))_

> ` ` **${** first **}** . **${** second **}** _//=> "primus . secundus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-01499))_

## Garbage, Garbage Everywhere

### **Garbage, Garbage Everywhere**

- We have now seen how to use Tail Calls to execute mapWith in constant space: _(javascriptallonge.pdf (source-range-83ecb080-01507))_
- But when we try it on very large arrays, we discover that it is _still_ very slow. _(javascriptallonge.pdf (source-range-83ecb080-01512))_
- The right tool to discover why it’s still slow is a memory profiler, but a simple inspection of the program will reveal the following: _(javascriptallonge.pdf (source-range-83ecb080-01512))_
- To do that, we take the array in prepend and push fn(first) onto the end, creating a new array that will be passed to the next invocation of mapWith. _(javascriptallonge.pdf (source-range-83ecb080-01513))_
- The array we had in prepend is no longer used. _(javascriptallonge.pdf (source-range-83ecb080-01517))_
- In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. _(javascriptallonge.pdf (source-range-83ecb080-01517))_
- Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend. _(javascriptallonge.pdf (source-range-83ecb080-01517))_
- Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend. _(javascriptallonge.pdf (source-range-83ecb080-01517))_
- Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another. _(javascriptallonge.pdf (source-range-83ecb080-01518))_
- We may not be creating 3,000 stack frames, but we are creating three thousand new arrays and copying elements into each and every one of them. _(javascriptallonge.pdf (source-range-83ecb080-01518))_
- **Key Point** : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. _(javascriptallonge.pdf (source-range-83ecb080-01519))_
- **Key Point** : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. _(javascriptallonge.pdf (source-range-83ecb080-01519))_
- > 64It needn’t always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. _(javascriptallonge.pdf (source-range-83ecb080-01521))_
- But this is not how JavaScript’s built-in arrays work. _(javascriptallonge.pdf (source-range-83ecb080-01521))_
- > 64It needn’t always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. _(javascriptallonge.pdf (source-range-83ecb080-01521))_

> Context: We have now seen how to use Tail Calls to execute mapWith in constant space:
_(context: javascriptallonge.pdf (source-range-83ecb080-01507))_

> **const** mapWith = (fn, [first, ...rest], prepend = []) => first === **undefined**
_(source: javascriptallonge.pdf (source-range-83ecb080-01508))_

> mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01511))_

### **some history**

- (The very first FORTRAN implementation was also written for the 704). _(javascriptallonge.pdf (source-range-83ecb080-01527))_
- The CPU’s instruction set featured two important macros: CAR would fetch 15 bits representing the Contents of the Address part of the Register, while CDR would fetch the Contents of the Decrement part of the Register. _(javascriptallonge.pdf (source-range-83ecb080-01528))_
- The 704 had a 36-bit word, meaning that it was very fast to store and retrieve 36-bit values. _(javascriptallonge.pdf (source-range-83ecb080-01528))_
- > 66Lisp is still very much alive, and one of the most interesting and exciting programming languages in use today is Clojure, a Lisp dialect that runs on the JVM, along with its sibling ClojureScript, Clojure that transpiles to JavaScript. _(javascriptallonge.pdf (source-range-83ecb080-01530))_
- In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. _(javascriptallonge.pdf (source-range-83ecb080-01533))_
- In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. _(javascriptallonge.pdf (source-range-83ecb080-01533))_
- The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells. _(javascriptallonge.pdf (source-range-83ecb080-01534))_
- Lisp’s basic data type is often said to be the list, but in actuality it was the “cons cell,” the term used to describe two 15-bit values stored in one word. _(javascriptallonge.pdf (source-range-83ecb080-01534))_
- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. _(javascriptallonge.pdf (source-range-83ecb080-01534))_
- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. _(javascriptallonge.pdf (source-range-83ecb080-01534))_
- Lists were represented as linked lists of cons cells, with each cell’s head pointing to an element and the tail pointing to another cons cell. _(javascriptallonge.pdf (source-range-83ecb080-01535))_
- Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-83ecb080-01536))_
- Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being the others), and computers in the late 1950s were extremely small and slow by today’s standards. _(javascriptallonge.pdf (source-range-83ecb080-01536))_
- Although the 704 used core memory, it still used vacuum tubes for its logic. _(javascriptallonge.pdf (source-range-83ecb080-01536))_
- Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-83ecb080-01536))_
- Here’s the scheme in JavaScript, using two-element arrays to represent cons cells: _(javascriptallonge.pdf (source-range-83ecb080-01537))_

> Context: > 66Lisp is still very much alive, and one of the most interesting and exciting programming languages in use today is Clojure, a Lisp dialect that runs on the JVM, along with its sibling ClojureScript, Clojure that transpiles to JavaScript. 67https://en.wikipedia.org/wiki/IBM_704
_(context: javascriptallonge.pdf (source-range-83ecb080-01530))_

> If you had two 15-bit values and wished to write them to the register, the CONS macro would take the values and write them to a 36-bit word.
_(source: javascriptallonge.pdf (source-range-83ecb080-01533))_

> Context: Here’s the scheme in JavaScript, using two-element arrays to represent cons cells:
_(context: javascriptallonge.pdf (source-range-83ecb080-01537))_

> **const** cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;
_(source: javascriptallonge.pdf (source-range-83ecb080-01538))_

> Context: We can make a list by calling cons repeatedly, and terminating it with null:
_(context: javascriptallonge.pdf (source-range-83ecb080-01539))_

> **const** oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, **null** )))));
_(source: javascriptallonge.pdf (source-range-83ecb080-01540))_

### oneToFive

- This is a Linked List[68] , it’s just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference. _(javascriptallonge.pdf (source-range-83ecb080-01548))_
- This is a Linked List[68] , it’s just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference. _(javascriptallonge.pdf (source-range-83ecb080-01548))_
- car is very fast, it simply extracts the first element of the cons cell. _(javascriptallonge.pdf (source-range-83ecb080-01551))_
- In JavaScript, it’s still much, much, much faster to get all the elements except the head from a linked list than from an array. _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- Getting one reference to a structure that already exists is faster than copying a bunch of elements. _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- There’s no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- In Lisp, it’s blazingly fast because it happens in hardware. _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- In JavaScript, it’s still much, much, much faster to get all the elements except the head from a linked list than from an array. _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- So now we understand that in Lisp, a lot of things use linked lists, and they do that in part because it was what the hardware made possible. _(javascriptallonge.pdf (source-range-83ecb080-01556))_
- So now we understand that in Lisp, a lot of things use linked lists, and they do that in part because it was what the hardware made possible. _(javascriptallonge.pdf (source-range-83ecb080-01556))_
- That being said, it is easy to understand and helps us grasp how literals and destructuring works, and how recursive algorithms ought to mirror the self-similarity of the data structures they manipulate. _(javascriptallonge.pdf (source-range-83ecb080-01558))_
- And so it is today that languages like JavaScript have arrays that are slow to split into the equivalent of a car/cdr pair, but instructional examples of recursive programs still have echoes of their Lisp origins. _(javascriptallonge.pdf (source-range-83ecb080-01558))_
- We’ll look at linked lists again when we look at Plain Old JavaScript Objects. _(javascriptallonge.pdf (source-range-83ecb080-01559))_

> Context: Notice that though JavaScript displays our list as if it is composed of arrays nested within each other like Russian Dolls, in reality the arrays refer to each other with references, so [1,[2,[3,[4,[5,null]]]]] is actually more like:
_(context: javascriptallonge.pdf (source-range-83ecb080-01543))_

> **const** node5 = [5, **null** ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2];
_(source: javascriptallonge.pdf (source-range-83ecb080-01546))_

> **const** oneToFive = node1;
_(source: javascriptallonge.pdf (source-range-83ecb080-01547))_

### **so why arrays**

- But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. _(javascriptallonge.pdf (source-range-83ecb080-01565))_
- Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. _(javascriptallonge.pdf (source-range-83ecb080-01565))_
- If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list. _(javascriptallonge.pdf (source-range-83ecb080-01566))_
- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We’ll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-83ecb080-01567))_
- For these and other reasons, almost all languages today make it possible to use a fast array or vector type that is optimized for iteration, and even Lisp now has a variety of data structures that are optimized for specific use cases. _(javascriptallonge.pdf (source-range-83ecb080-01568))_

> Context: If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list?
_(context: javascriptallonge.pdf (source-range-83ecb080-01564))_

> And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.
_(source: javascriptallonge.pdf (source-range-83ecb080-01565))_

> Context: Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.
_(context: javascriptallonge.pdf (source-range-83ecb080-01565))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements.
_(source: javascriptallonge.pdf (source-range-83ecb080-01566))_

### **summary**

- Although we showed how to use tail calls to map and fold over arrays with [first, ...rest], in reality this is not how it ought to be done. _(javascriptallonge.pdf (source-range-83ecb080-01570))_
- But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-83ecb080-01570))_
- But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-83ecb080-01570))_

## Plain Old JavaScript Objects

### **Plain Old JavaScript Objects**

- Lists are not the only way to represent collections of things, but they are the “oldest” data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. _(javascriptallonge.pdf (source-range-83ecb080-01575))_
- Lists are not the only way to represent collections of things, but they are the “oldest” data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. _(javascriptallonge.pdf (source-range-83ecb080-01575))_
- So back when lists were the only things available, programmers would introduce constants to make things easier on themselves: _(javascriptallonge.pdf (source-range-83ecb080-01579))_
- Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. _(javascriptallonge.pdf (source-range-83ecb080-01579))_
- So back when lists were the only things available, programmers would introduce constants to make things easier on themselves: _(javascriptallonge.pdf (source-range-83ecb080-01579))_
- Now they could write user[NAME][LAST] or user[OCCUPATION][TITLE] instead of user[0][1] or user[1][0]. _(javascriptallonge.pdf (source-range-83ecb080-01582))_
- Over time, this need to build heterogeneous data structures with access to members by name evolved into the Dictionary[69] data type, a mapping from a unique set of objects to another set of objects. _(javascriptallonge.pdf (source-range-83ecb080-01582))_
- Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0, we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else. _(javascriptallonge.pdf (source-range-83ecb080-01583))_
- Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0, we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else. _(javascriptallonge.pdf (source-range-83ecb080-01583))_
- JavaScript has dictionaries, and it calls them “objects.” The word “object” is loaded in programming circles, due to the widespread use of the term “object-oriented programming” that was coined by Alan Kay but has since come to mean many, many things to many different people. _(javascriptallonge.pdf (source-range-83ecb080-01584))_
- In JavaScript, an object is a map from string keys to values. _(javascriptallonge.pdf (source-range-83ecb080-01585))_

> Context: Lists are not the only way to represent collections of things, but they are the “oldest” data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. Lists are obviously very handy for homogeneous collections of things, like a shopping list:
_(context: javascriptallonge.pdf (source-range-83ecb080-01575))_

> **const** remember = ["the milk", "the coffee beans", "the biscotti"];
_(source: javascriptallonge.pdf (source-range-83ecb080-01576))_

> Context: And they can be used to store heterogeneous things in various levels of structure:
_(context: javascriptallonge.pdf (source-range-83ecb080-01577))_

> **const** user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\ vaScript Spessore", "CoffeeScript Ristretto"]]];
_(source: javascriptallonge.pdf (source-range-83ecb080-01578))_

> Context: Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves:
_(context: javascriptallonge.pdf (source-range-83ecb080-01579))_

> **const** NAME = 0, FIRST = 0, LAST = 1, OCCUPATION = 1, TITLE = 0, RESPONSIBILITIES = 1;
_(source: javascriptallonge.pdf (source-range-83ecb080-01580))_

> Context: Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves:
_(context: javascriptallonge.pdf (source-range-83ecb080-01579))_

> **const** user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\ vaScript Spessore", "CoffeeScript Ristretto"]]];
_(source: javascriptallonge.pdf (source-range-83ecb080-01581))_

### **literal object syntax**

- JavaScript has a literal syntax for creating objects. _(javascriptallonge.pdf (source-range-83ecb080-01590))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-83ecb080-01596))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-83ecb080-01596))_
- Names needn’t be alphanumeric strings. _(javascriptallonge.pdf (source-range-83ecb080-01602))_
- If the name is an alphanumeric string conforming to the same rules as names of variables, there’s a simplified syntax for accessing the values: _(javascriptallonge.pdf (source-range-83ecb080-01604))_
- Expressions can be used for keys as well. _(javascriptallonge.pdf (source-range-83ecb080-01609))_
- It is very common to associate named function expressions with keys in objects, and there is a “compact method syntax” for binding named function expressions to keywords: _(javascriptallonge.pdf (source-range-83ecb080-01618))_
- (There are some other technical differences between binding a named function expression and using _(javascriptallonge.pdf (source-range-83ecb080-01620))_
- compact method syntax, but they are not relevant here. _(javascriptallonge.pdf (source-range-83ecb080-01623))_

> Context: Two objects created with separate evaluations have differing identities, just like arrays:
_(context: javascriptallonge.pdf (source-range-83ecb080-01592))_

> - { year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 } _//=> false_
_(source: javascriptallonge.pdf (source-range-83ecb080-01593))_

> Context: Objects use [] to access the values by name, using a string:
_(context: javascriptallonge.pdf (source-range-83ecb080-01594))_

> - { year: 2012, month: 6, day: 14 }['day'] _//=> 14_
_(source: javascriptallonge.pdf (source-range-83ecb080-01595))_

> Context: Values contained within an object work just like values contained within an array, we access them by reference to the original:
_(context: javascriptallonge.pdf (source-range-83ecb080-01596))_

> - x = unique(),
_(source: javascriptallonge.pdf (source-range-83ecb080-01598))_

> Context: Values contained within an object work just like values contained within an array, we access them by reference to the original:
_(context: javascriptallonge.pdf (source-range-83ecb080-01596))_

> - y = unique(),
_(source: javascriptallonge.pdf (source-range-83ecb080-01599))_

> - z = unique(), o = { a: x, b: y, c: z };
_(source: javascriptallonge.pdf (source-range-83ecb080-01600))_

> - o['a'] === x && o['b'] === y && o['c'] === z _//=> true_
_(source: javascriptallonge.pdf (source-range-83ecb080-01601))_

> Context: If the name is an alphanumeric string conforming to the same rules as names of variables, there’s a simplified syntax for accessing the values:
_(context: javascriptallonge.pdf (source-range-83ecb080-01604))_

> **const** date = { year: 2012, month: 6, day: 14 };
_(source: javascriptallonge.pdf (source-range-83ecb080-01607))_

> date['day'] === date.day _//=> true_
_(source: javascriptallonge.pdf (source-range-83ecb080-01608))_

> Context: Expressions can be used for keys as well. The syntax is to enclose the key’s expression in [ and ]:
_(context: javascriptallonge.pdf (source-range-83ecb080-01609))_

> { ["p" + "i"]: 3.14159265 } _//=> {"pi":3.14159265}_
_(source: javascriptallonge.pdf (source-range-83ecb080-01610))_

> Context: All containers can contain any value, including functions or other containers, like a fat arrow function:
_(context: javascriptallonge.pdf (source-range-83ecb080-01611))_

> **const** Mathematics = { abs: (a) => a < 0 ? -a : a }; Mathematics.abs(-5) _//=> 5_
_(source: javascriptallonge.pdf (source-range-83ecb080-01612))_

### **destructuring objects**

- It is very common to write things like title: title when destructuring objects. _(javascriptallonge.pdf (source-range-83ecb080-01636))_
- When the label is a valid variable name, it’s often the most obvious variable name as well. _(javascriptallonge.pdf (source-range-83ecb080-01636))_

> Context: And we can also write:
_(context: javascriptallonge.pdf (source-range-83ecb080-01627))_

> surname _//=> "Braithwaite"_ title _//=> "Author"_
_(source: javascriptallonge.pdf (source-range-83ecb080-01629))_

> Context: Terrible grammar and capitalization, but let’s move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it’s often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:
_(context: javascriptallonge.pdf (source-range-83ecb080-01636))_

> **const** description = ({name: { first }, occupation: { title } }) => ` **${** first **}** is a **${** title **}** `;
_(source: javascriptallonge.pdf (source-range-83ecb080-01637))_

> Context: And that same syntax works for literals:
_(context: javascriptallonge.pdf (source-range-83ecb080-01640))_

> **const** abbrev = ({name: { first, last }, occupation: { title } }) => { **return** { first, last, title}; } abbrev(user)
_(source: javascriptallonge.pdf (source-range-83ecb080-01641))_

### **revisiting linked lists**

- But now that we’ve looked at objects, we can use an object instead of a two-element array. _(javascriptallonge.pdf (source-range-83ecb080-01646))_
- In essence, this simple implementation used functions to create an abstraction with named elements. _(javascriptallonge.pdf (source-range-83ecb080-01646))_
- While we’re at it, let’s use contemporary names. _(javascriptallonge.pdf (source-range-83ecb080-01646))_
- As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. _(javascriptallonge.pdf (source-range-83ecb080-01657))_
- The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. _(javascriptallonge.pdf (source-range-83ecb080-01661))_
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-83ecb080-01661))_
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-83ecb080-01661))_
- We could follow the strategy of delaying the work. _(javascriptallonge.pdf (source-range-83ecb080-01662))_
- We have unwittingly _reversed_ the list. _(javascriptallonge.pdf (source-range-83ecb080-01669))_
- This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we’re going to get a backwards copy of the list. _(javascriptallonge.pdf (source-range-83ecb080-01669))_
- Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. _(javascriptallonge.pdf (source-range-83ecb080-01680))_
- Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. _(javascriptallonge.pdf (source-range-83ecb080-01680))_
- Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. _(javascriptallonge.pdf (source-range-83ecb080-01680))_
- Mind you, this is still much, much faster than making partial copies of arrays. _(javascriptallonge.pdf (source-range-83ecb080-01681))_
- For a list of length _n_ , we created _n_ superfluous nodes and copied _n_ superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-01681))_
- Whereas our naïve array algorithm created 2 _n_ superfluous arrays and copied _n_[2] superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-01681))_
- Whereas our naïve array algorithm created 2 _n_ superfluous arrays and copied _n_[2] superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-01681))_

> Context: Earlier, we used two-element arrays as nodes in a linked list:
_(context: javascriptallonge.pdf (source-range-83ecb080-01644))_

> **const** cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;
_(source: javascriptallonge.pdf (source-range-83ecb080-01645))_

> Context: We can then perform the equivalent of [first, ...rest] with direct property accessors:
_(context: javascriptallonge.pdf (source-range-83ecb080-01648))_

> **const** EMPTY = {}; **const** OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } };
_(source: javascriptallonge.pdf (source-range-83ecb080-01651))_

> OneTwoThree.first _//=> 1_ OneTwoThree.rest _//=> {"first":2,"rest":{"first":3,"rest":{}}}_
_(source: javascriptallonge.pdf (source-range-83ecb080-01652))_

> OneTwoThree.rest.rest.first _//=> 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-01653))_

> Context: Taking the length of a linked list is easy: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:
_(context: javascriptallonge.pdf (source-range-83ecb080-01654, source-range-83ecb080-01657))_

> **const** length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1);
_(source: javascriptallonge.pdf (source-range-83ecb080-01655))_

> Context: Taking the length of a linked list is easy: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:
_(context: javascriptallonge.pdf (source-range-83ecb080-01654, source-range-83ecb080-01657))_

> length(OneTwoThree) _//=> 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-01656))_

> Context: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:
_(context: javascriptallonge.pdf (source-range-83ecb080-01657))_

> **const** slowcopy = (node) => node === EMPTY ? EMPTY : { first: node.first, rest: slowcopy(node.rest)};
_(source: javascriptallonge.pdf (source-range-83ecb080-01658))_

> Context: We could follow the strategy of delaying the work. Let’s write that naively:
_(context: javascriptallonge.pdf (source-range-83ecb080-01662))_

> **const** copy2 = (node, delayed = EMPTY) => node === EMPTY
_(source: javascriptallonge.pdf (source-range-83ecb080-01665))_

> Context: Well, well, well. We have unwittingly _reversed_ the list. This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we’re going to get a backwards copy of the list. This isn’t a bad thing by any stretch of the imagination. Let’s call it what it is:
_(context: javascriptallonge.pdf (source-range-83ecb080-01669))_

> **const** reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed });
_(source: javascriptallonge.pdf (source-range-83ecb080-01670))_

> Context: And now, we can make a reversing map:
_(context: javascriptallonge.pdf (source-range-83ecb080-01671))_

> **const** reverseMapWith = (fn, node, delayed = EMPTY) => node === EMPTY
_(source: javascriptallonge.pdf (source-range-83ecb080-01672))_

> Context: And a regular mapWith follows:
_(context: javascriptallonge.pdf (source-range-83ecb080-01674))_

> **const** reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed });
_(source: javascriptallonge.pdf (source-range-83ecb080-01675))_

> Context: And a regular mapWith follows:
_(context: javascriptallonge.pdf (source-range-83ecb080-01674))_

> **const** mapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? reverse(delayed) : mapWith(fn, node.rest, { first: fn(node.first), rest: delayed });
_(source: javascriptallonge.pdf (source-range-83ecb080-01676))_

> Context: And a regular mapWith follows:
_(context: javascriptallonge.pdf (source-range-83ecb080-01674))_

> mapWith((x) => x * x, OneTwoThree) _//=> {"first":1,"rest":{"first":4,"rest":{"first":9,"rest":{}}}}_
_(source: javascriptallonge.pdf (source-range-83ecb080-01677))_

## Mutation

### **Mutation**

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

### **mutation and data structures**

- Mutation is a surprisingly complex subject. _(javascriptallonge.pdf (source-range-83ecb080-01715))_
- In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about. _(javascriptallonge.pdf (source-range-83ecb080-01715))_
- It is possible to compute anything without ever mutating an existing entity. _(javascriptallonge.pdf (source-range-83ecb080-01715))_
- While we’re executing the mapWith function, we’re constructing a new linked list. _(javascriptallonge.pdf (source-range-83ecb080-01716))_
- Let’s recall linked lists from Plain Old JavaScript Objects. _(javascriptallonge.pdf (source-range-83ecb080-01716))_
- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. _(javascriptallonge.pdf (source-range-83ecb080-01716))_

> Context: One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let’s recall linked lists from Plain Old JavaScript Objects. While we’re executing the mapWith function, we’re constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith.
_(context: javascriptallonge.pdf (source-range-83ecb080-01716))_

> But after returning the new list, we then become conservative about mutation. This also makes sense: Linked lists often use structure sharing. For example:
_(source: javascriptallonge.pdf (source-range-83ecb080-01717))_

> const ThreeToFive = OneToFive.rest.rest;
_(source: javascriptallonge.pdf (source-range-83ecb080-01724))_

> ThreeToFive.first = "three"; ThreeToFive.rest.first = "four"; ThreeToFive.rest.rest.first = "five";
_(source: javascriptallonge.pdf (source-range-83ecb080-01727))_

### ThreeToFive

- When we wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of we were getting a reference to the same chain of nodes. _(javascriptallonge.pdf (source-range-83ecb080-01731))_
- Changes made to ThreeToFive affect OneToFive, because they share the same structure. _(javascriptallonge.pdf (source-range-83ecb080-01731))_
- Structure sharing like this is what makes linked lists so fast for taking everything but the first item of a list: We aren’t making a new list, we’re using some of the old list. _(javascriptallonge.pdf (source-range-83ecb080-01732))_
- We just use the data, and the less we mutate it, the fewer the times we have to think about whether making changes will be “safe.” _(javascriptallonge.pdf (source-range-83ecb080-01738))_

> Context: Changes made to ThreeToFive affect OneToFive, because they share the same structure. When we wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of we were getting a reference to the same chain of nodes.
_(context: javascriptallonge.pdf (source-range-83ecb080-01731))_

> OneToFive //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\ r","rest":{"first":"five","rest":{}}}}}}
_(source: javascriptallonge.pdf (source-range-83ecb080-01730))_

> Context: Structure sharing like this is what makes linked lists so fast for taking everything but the first item of a list: We aren’t making a new list, we’re using some of the old list. Whereas destructuring an array with [first, ...rest] does make a copy, so:
_(context: javascriptallonge.pdf (source-range-83ecb080-01732))_

> **const** OneToFive = [1, 2, 3, 4, 5];
_(source: javascriptallonge.pdf (source-range-83ecb080-01735))_

> We don’t have to remember to use copying operations when we pass it as a value to a function, or extract some data from it.
_(source: javascriptallonge.pdf (source-range-83ecb080-01738))_

### **building with mutation**

- Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list: _(javascriptallonge.pdf (source-range-83ecb080-01740))_
- As noted, one pattern is to be more liberal about mutation when building a data structure. _(javascriptallonge.pdf (source-range-83ecb080-01740))_
- If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation: _(javascriptallonge.pdf (source-range-83ecb080-01743))_
- This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. _(javascriptallonge.pdf (source-range-83ecb080-01747))_
- But when we’re in the midst of creating a brand new list, we aren’t sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time. _(javascriptallonge.pdf (source-range-83ecb080-01747))_
- Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. _(javascriptallonge.pdf (source-range-83ecb080-01747))_

> Context: As noted, one pattern is to be more liberal about mutation when building a data structure. Consider our copy algorithm. Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list:
_(context: javascriptallonge.pdf (source-range-83ecb080-01740))_

> **const** reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed });
_(source: javascriptallonge.pdf (source-range-83ecb080-01741))_

> Context: As noted, one pattern is to be more liberal about mutation when building a data structure. Consider our copy algorithm. Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list:
_(context: javascriptallonge.pdf (source-range-83ecb080-01740))_

> **const** copy = (node) => reverse(reverse(node));
_(source: javascriptallonge.pdf (source-range-83ecb080-01742))_

## Reassignment

### **Reassignment**

- Like some imperative programming languages, JavaScript allows you to re-assign the value bound : to parameters. _(javascriptallonge.pdf (source-range-83ecb080-01758))_
- We can _shadow_ it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-83ecb080-01765))_
- JavaScript does not permit us to rebind a name that has been bound with const. _(javascriptallonge.pdf (source-range-83ecb080-01765))_
- What we want is a statement that works like const, but permits us to rebind variables. _(javascriptallonge.pdf (source-range-83ecb080-01766))_
- The key is to understand that we are rebinding a different value to the same name in the same environment. _(javascriptallonge.pdf (source-range-83ecb080-01769))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const. _(javascriptallonge.pdf (source-range-83ecb080-01772))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const. _(javascriptallonge.pdf (source-range-83ecb080-01772))_
- However, if we don’t shadow age with let, reassigning within the block changes the original: _(javascriptallonge.pdf (source-range-83ecb080-01780))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. _(javascriptallonge.pdf (source-range-83ecb080-01782))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. _(javascriptallonge.pdf (source-range-83ecb080-01782))_
- It then rebinds the name in that environment. _(javascriptallonge.pdf (source-range-83ecb080-01782))_

> Context: Rebinding parameters is usually avoided, but what about rebinding names we declare within a function? What we want is a statement that works like const, but permits us to rebind variables. JavaScript has such a thing, it’s called let:
_(context: javascriptallonge.pdf (source-range-83ecb080-01766))_

> **let** age = 52;
_(source: javascriptallonge.pdf (source-range-83ecb080-01767))_

> Context: Rebinding parameters is usually avoided, but what about rebinding names we declare within a function? What we want is a statement that works like const, but permits us to rebind variables. JavaScript has such a thing, it’s called let:
_(context: javascriptallonge.pdf (source-range-83ecb080-01766))_

> age = 53; age _//=> 53_
_(source: javascriptallonge.pdf (source-range-83ecb080-01768))_

### **mixing let and const**

- The suggestion is that shadowing a variable is confusing code. _(javascriptallonge.pdf (source-range-83ecb080-01784))_
- Shadowing a let with a const does not change our ability to rebind the variable in its original scope. _(javascriptallonge.pdf (source-range-83ecb080-01787))_
- Shadowing a const with a let does not permit it to be rebound in its original scope. _(javascriptallonge.pdf (source-range-83ecb080-01791))_

> If you dislike deliberately shadowing variables, you’ll probably take an even more opprobrious view of mixing const and let semantics with a shadowed variable:
_(source: javascriptallonge.pdf (source-range-83ecb080-01785))_

### **var**

- JavaScript has one _more_ way to bind a name to a value, var.[71] var looks a lot like let: _(javascriptallonge.pdf (source-range-83ecb080-01793))_
- First, var is not block scoped, it’s function scoped, just like function declarations: _(javascriptallonge.pdf (source-range-83ecb080-01799))_
- Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. _(javascriptallonge.pdf (source-range-83ecb080-01801))_
- A function declaration can appear anywhere within a function, but the declaration _and_ the definition are hoisted. _(javascriptallonge.pdf (source-range-83ecb080-01802))_
- But, again, it is unwise to expect consistency. _(javascriptallonge.pdf (source-range-83ecb080-01802))_
- A function declaration can appear anywhere within a function, but the declaration _and_ the definition are hoisted. _(javascriptallonge.pdf (source-range-83ecb080-01802))_
- But it’s not like const and let in that it’s function scoped, not block scoped. _(javascriptallonge.pdf (source-range-83ecb080-01818))_
- In that way, var is a little like const and let, we should always declare and bind names before using them. _(javascriptallonge.pdf (source-range-83ecb080-01818))_
- In that way, var is a little like const and let, we should always declare and bind names before using them. _(javascriptallonge.pdf (source-range-83ecb080-01818))_

> **return** n * factorial2(x); } } factorial2(5) _//=> 120_
_(source: javascriptallonge.pdf (source-range-83ecb080-01798))_

> Context: But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration _and_ the definition are hoisted. Note this example of a function that uses a helper:
_(context: javascriptallonge.pdf (source-range-83ecb080-01802))_

> **const** factorial = (n) => {
_(source: javascriptallonge.pdf (source-range-83ecb080-01803))_

> Context: JavaScript hoists the let and the assignment. But not so with var:
_(context: javascriptallonge.pdf (source-range-83ecb080-01809))_

> **const** factorial = (n) => {
_(source: javascriptallonge.pdf (source-range-83ecb080-01810))_

> Context: JavaScript hoists the declaration, but not the assignment. It is as if we’d written:
_(context: javascriptallonge.pdf (source-range-83ecb080-01812))_

> **const** factorial = (n) => {
_(source: javascriptallonge.pdf (source-range-83ecb080-01815))_

> **let** innerFactorial = **undefined** ; **return** innerFactorial(n, 1);
_(source: javascriptallonge.pdf (source-range-83ecb080-01816))_

### **why const and let were invented**

- For nearly twenty years, variables were declared with var (not counting parameters and function declarations, of course). _(javascriptallonge.pdf (source-range-83ecb080-01820))_
- However, its functional scope was a problem. _(javascriptallonge.pdf (source-range-83ecb080-01820))_
- We haven’t looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. _(javascriptallonge.pdf (source-range-83ecb080-01821))_
- Hopefully, you can think of a faster way to calculate this sum.[72] And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. _(javascriptallonge.pdf (source-range-83ecb080-01823))_
- > 72There is a well known story about Karl Friedrich Gauss when he was in elementary school. _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- The other kids were adding the numbers like this: 1 + 2 + 3 + . _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- There are 50 pairs of numbers, so the answer is 50*101 = 5050. _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- If you notice every pair of numbers adds up to 101. _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- But Gauss rearranged the numbers to add them like this: (1 + 100) + (2 + 99) + (3 + 98) + . _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- His teacher got mad at the class and told them to add the numbers 1 to 100 and give him the answer by the end of the class. _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- The answer is that pesky var i. _(javascriptallonge.pdf (source-range-83ecb080-01833))_
- But at the time we _call_ one of the functions, i has the value 3, which is why the loop terminated. _(javascriptallonge.pdf (source-range-83ecb080-01837))_
- So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3. _(javascriptallonge.pdf (source-range-83ecb080-01837))_
- Now, at the time we created each function, i had a sensible value, like 0, 1, or 2. _(javascriptallonge.pdf (source-range-83ecb080-01837))_
- So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3. _(javascriptallonge.pdf (source-range-83ecb080-01837))_
- This small error was a frequent cause of confusion, and in the days when there was no block-scoped let, programmers would need to know how to fake it, usually with an IIFE: _(javascriptallonge.pdf (source-range-83ecb080-01840))_
- This works, but let is so much simpler and cleaner that it was added to the language in the ECMAScript 2015 specification. _(javascriptallonge.pdf (source-range-83ecb080-01844))_
- The two goals are often, but not always, aligned. _(javascriptallonge.pdf (source-range-83ecb080-01845))_
- The purpose of your own code is to get things done. _(javascriptallonge.pdf (source-range-83ecb080-01845))_
- That does not mean that you should follow the exact same practice in your own code: The purpose of this book is to illustrate certain principles of programming. _(javascriptallonge.pdf (source-range-83ecb080-01845))_

> Context: We haven’t looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. It looks a lot like the for loop in C. Here it is with var: > 72There is a well known story about Karl Friedrich Gauss when he was in elementary school. His teacher got mad at the class and told them to add the numbers 1 to 100 and give him the answer by the end of the class. About 30 seconds later Gauss gave him the answer. The other kids were adding the numbers like this: 1 + 2 + 3 + . 
_(context: javascriptallonge.pdf (source-range-83ecb080-01821, source-range-83ecb080-01824))_

> **var** sum = 0; **for** ( **var** i = 1; i <= 100; i++) { sum = sum + i } sum #=> 5050
_(source: javascriptallonge.pdf (source-range-83ecb080-01822))_

> Context: Again, so far, so good. Let’s try one of our functions: What went wrong? Why didn’t it give us ‘Hello, Raganwald, my name is Friedrich’? The answer is that pesky var i. Remember that i is bound in the surrounding environment, so it’s as if we wrote:
_(context: javascriptallonge.pdf (source-range-83ecb080-01831, source-range-83ecb080-01833))_

> introductions[1]('Raganwald') _//=> 'Hello, Raganwald, my name is undefined'_
_(source: javascriptallonge.pdf (source-range-83ecb080-01832))_

## Copy on Write

### **Copy on Write**

- We’ve seen how to build lists with arrays and with linked lists. _(javascriptallonge.pdf (source-range-83ecb080-01852))_
- - When you take the rest of an array with destructuring ([first, ...rest]), you are given a _copy_ of the elements of the array. _(javascriptallonge.pdf (source-range-83ecb080-01853))_
- - When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list. _(javascriptallonge.pdf (source-range-83ecb080-01854))_
- And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-83ecb080-01855))_
- And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-83ecb080-01855))_
- And therefore, modifications to the parent also modify the child, and modifications to the child also modify the parent. _(javascriptallonge.pdf (source-range-83ecb080-01858))_
- We’ll end up reinventing reference counting and garbage collection. _(javascriptallonge.pdf (source-range-83ecb080-01863))_
- If we _know_ that a list doesn’t share any elements with another list, we can safely modify it. _(javascriptallonge.pdf (source-range-83ecb080-01863))_

> Context: When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list.
_(context: javascriptallonge.pdf (source-range-83ecb080-01854))_

> The consequence of this is that if you have an array, and you take it’s “rest,” your “child” array is a copy of the elements of the parent array.
_(source: javascriptallonge.pdf (source-range-83ecb080-01855))_

> Whereas if you have a linked list, and you take it’s “rest,” your “child” list shares its nodes with the “parent” list.
_(source: javascriptallonge.pdf (source-range-83ecb080-01858))_

> Context: Let’s confirm our understanding:
_(context: javascriptallonge.pdf (source-range-83ecb080-01859))_

> parentList.rest.rest.first = "three"; childList.first = "two";
_(source: javascriptallonge.pdf (source-range-83ecb080-01861))_

> Context: Let’s confirm our understanding:
_(context: javascriptallonge.pdf (source-range-83ecb080-01859))_

> parentList _//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\_ {},"rest":{}}}}} childList _//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}_
_(source: javascriptallonge.pdf (source-range-83ecb080-01862))_

### **a few utilities**

- before we go any further, let’s write a few naïve list utilities so that we can work at a slightly higher level of abstraction: _(javascriptallonge.pdf (source-range-83ecb080-01865))_
- before we go any further, let’s write a few naïve list utilities so that we can work at a slightly higher level of abstraction: _(javascriptallonge.pdf (source-range-83ecb080-01865))_
- The main difference is that array[index] = value evaluates to value, while set(index, value, list) evaluates to the modified list. _(javascriptallonge.pdf (source-range-83ecb080-01873))_

> Context: **const** copy = (node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail === **null** ) { **const** { first, rest } = node; **const** newNode = { first, rest }; **return** copy(rest, newNode, newNode); } **else** { **const** { first, rest } = node; **const** newNode = { first, rest }; tail.rest = newNode; **return** copy(node.rest, head, newNode); } } **const** first = ({first, rest}) => first; **const** rest = ({first, rest}) => rest; **con
_(context: javascriptallonge.pdf (source-range-83ecb080-01868))_

> **const** childList = rest(parentList);
_(source: javascriptallonge.pdf (source-range-83ecb080-01871))_

### **copy-on-read**

- Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-83ecb080-01875))_
- One strategy for avoiding problems is to be _pessimistic_ . _(javascriptallonge.pdf (source-range-83ecb080-01875))_
- This strategy is called “copy-on-read”, because when we attempt the parent to “read” the value of a child of the list, we make a copy and read the copy of the child. _(javascriptallonge.pdf (source-range-83ecb080-01879))_
- Thereafter, we can write to the parent or the copy of the child freely. _(javascriptallonge.pdf (source-range-83ecb080-01879))_
- This strategy is called “copy-on-read”, because when we attempt the parent to “read” the value of a child of the list, we make a copy and read the copy of the child. _(javascriptallonge.pdf (source-range-83ecb080-01879))_
- As we expected, making a copy lets us modify the copy without interfering with the original. _(javascriptallonge.pdf (source-range-83ecb080-01880))_
- Our mapWith function would be very expensive if we make a copy every time we call rest(node). _(javascriptallonge.pdf (source-range-83ecb080-01880))_
- Sometimes we don’t need to make a copy because we won’t be modifying the list. _(javascriptallonge.pdf (source-range-83ecb080-01880))_
- Sometimes we don’t need to make a copy because we won’t be modifying the list. _(javascriptallonge.pdf (source-range-83ecb080-01880))_
- But before we fix that, let’s try being lazy about copying. _(javascriptallonge.pdf (source-range-83ecb080-01881))_
- But before we fix that, let’s try being lazy about copying. _(javascriptallonge.pdf (source-range-83ecb080-01881))_

> Context: So back to the problem of structure sharing. One strategy for avoiding problems is to be _pessimistic_ . Whenever we take the rest of a list, make a copy.
_(context: javascriptallonge.pdf (source-range-83ecb080-01875))_

> **const** rest = ({first, rest}) => copy(rest);
_(source: javascriptallonge.pdf (source-range-83ecb080-01876))_

> Context: So back to the problem of structure sharing. One strategy for avoiding problems is to be _pessimistic_ . Whenever we take the rest of a list, make a copy. This strategy is called “copy-on-read”, because when we attempt the parent to “read” the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.
_(context: javascriptallonge.pdf (source-range-83ecb080-01875, source-range-83ecb080-01879))_

> parentList _//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\_ rest":{}}}}} childList //=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
_(source: javascriptallonge.pdf (source-range-83ecb080-01878))_

### **copy-on-write**

> Context: Why are we copying? In case we modify a child list. Ok, what if we do this: Make the copy when we know we are modifying the list. When do we know that? When we call set. We’ll restore our original definition for rest, but change set:
_(context: javascriptallonge.pdf (source-range-83ecb080-01885))_

> **const** rest = ({first, rest}) => rest;
_(source: javascriptallonge.pdf (source-range-83ecb080-01886))_

### parentList

- But our new parent and child lists are copies that contain the desired modifications, without interfering with each other: _(javascriptallonge.pdf (source-range-83ecb080-01891))_

### newParentList

- And now functions like mapWith that make copies without modifying anything, work at full speed. _(javascriptallonge.pdf (source-range-83ecb080-01894))_
- This strategy of waiting to copy until you are writing is called copy-on-write, or “COW:” _(javascriptallonge.pdf (source-range-83ecb080-01895))_
- This strategy of waiting to copy until you are writing is called copy-on-write, or “COW:” _(javascriptallonge.pdf (source-range-83ecb080-01895))_
- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.— Wikipedia[73] _(javascriptallonge.pdf (source-range-83ecb080-01898))_
- Once we’re done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-83ecb080-01900))_
- Looking at the code again, you see that the copy function doesn’t copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. _(javascriptallonge.pdf (source-range-83ecb080-01900))_

## Tortoises, Hares, and Teleporting Turtles

### **Tortoises, Hares, and Teleporting Turtles**

- It was, “Write an algorithm to detect a loop in a linked list, in constant space.” _(javascriptallonge.pdf (source-range-83ecb080-01906))_
- I’m not particularly surprised that I couldn’t think up an answer in a few minutes at the time. _(javascriptallonge.pdf (source-range-83ecb080-01907))_
- This is the “trick answer” to a question about finding a missing integer from a list, so I was trying the old, “Transform this into a problem you’ve already solved[74] ” meta-algorithm. _(javascriptallonge.pdf (source-range-83ecb080-01908))_
- Eventually, I came up with something and tried it (In Java!) on my home PC. _(javascriptallonge.pdf (source-range-83ecb080-01909))_
- I then forgot about it for a while. _(javascriptallonge.pdf (source-range-83ecb080-01909))_
- This algorithm is called “The Tortoise and the Hare,” and was discovered by Robert Floyd in the 1960s. _(javascriptallonge.pdf (source-range-83ecb080-01920))_
- You have two node references, and one traverses the list at twice the speed of the other. _(javascriptallonge.pdf (source-range-83ecb080-01920))_
- No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you’ll detect the loop. _(javascriptallonge.pdf (source-range-83ecb080-01920))_
- No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you’ll detect the loop. _(javascriptallonge.pdf (source-range-83ecb080-01920))_
- This algorithm is called “The Tortoise and the Hare,” and was discovered by Robert Floyd in the 1960s. _(javascriptallonge.pdf (source-range-83ecb080-01920))_
- At the time, I couldn’t think of any way to use hashing to solve the problem, so I gave up and tried to fit this into a powers-of-two algorithm. _(javascriptallonge.pdf (source-range-83ecb080-01923))_
- It seems to be faster under certain circumstances, depending on the size of the loop and the relative costs of certain operations. _(javascriptallonge.pdf (source-range-83ecb080-01926))_
- What’s interesting about these two algorithms is that they both _tangle_ two separate concerns: How to traverse a data structure, and what to do with the elements that you encounter. _(javascriptallonge.pdf (source-range-83ecb080-01927))_

> Context: I went home and pondered the problem. I wanted to solve it. Eventually, I came up with something and tried it (In Java!) on my home PC. I sent him an email sharing my result, to demonstrate my ability to follow through. I then forgot about it for a while. Some time later, I was told that the correct solution was:
_(context: javascriptallonge.pdf (source-range-83ecb080-01909))_

> **const** EMPTY = **null** ;
_(source: javascriptallonge.pdf (source-range-83ecb080-01910))_

> Context: I went home and pondered the problem. I wanted to solve it. Eventually, I came up with something and tried it (In Java!) on my home PC. I sent him an email sharing my result, to demonstrate my ability to follow through. I then forgot about it for a while. Some time later, I was told that the correct solution was:
_(context: javascriptallonge.pdf (source-range-83ecb080-01909))_

> **const** isEmpty = (node) => node === EMPTY;
_(source: javascriptallonge.pdf (source-range-83ecb080-01911))_

> Context: **const** teleportingTurtle = (list) => { **let** speed = 1, rabbit = list, turtle = rabbit; **while** ( **true** ) { **for** ( **let** i = 0; i <= speed; i += 1) { rabbit = rabbit.rest; **if** (rabbit == **null** ) { **return false** ; } **if** (rabbit === turtle) { **return true** ; } } turtle = rabbit; speed *= 2; } **return false** ; }; **const** aList = list(1, 2, 3, 4, 5); teleportingTurtle(aList) _//=> false_ forceAppend(aList, aList.rest.rest);
_(context: javascriptallonge.pdf (source-range-83ecb080-01924))_

> teleportingTurtle(aList); _//=> true_
_(source: javascriptallonge.pdf (source-range-83ecb080-01925))_

## Functional Iterators

### **Functional Iterators**

- But it still relies on foldArrayWith, so it can only sum arrays. _(javascriptallonge.pdf (source-range-83ecb080-01939))_
- The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. _(javascriptallonge.pdf (source-range-83ecb080-01939))_
- But it still relies on foldArrayWith, so it can only sum arrays. _(javascriptallonge.pdf (source-range-83ecb080-01939))_
- Well, we call arraySum with an array, and it has baked into it a method for traversing the array. _(javascriptallonge.pdf (source-range-83ecb080-01941))_
- Perhaps we could extract both of those things. _(javascriptallonge.pdf (source-range-83ecb080-01941))_
- The sumFoldable function doesn’t care what kind of data structure we have, as long as it’s foldable. _(javascriptallonge.pdf (source-range-83ecb080-01949))_
- We’ve found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we’ve completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really). _(javascriptallonge.pdf (source-range-83ecb080-01956))_

> Context: Let’s consider a remarkably simple problem: Finding the sum of the elements of an array. In tailrecursive style, it looks like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-01933))_

> **const** arraySum = ([first, ...rest], accumulator = 0) => first === **undefined** ? accumulator : arraySum(rest, first + accumulator)
_(source: javascriptallonge.pdf (source-range-83ecb080-01934))_

> Context: Let’s consider a remarkably simple problem: Finding the sum of the elements of an array. In tailrecursive style, it looks like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-01933))_

> arraySum([1, 4, 9, 16, 25]) _//=> 55_
_(source: javascriptallonge.pdf (source-range-83ecb080-01935))_

> Context: As we saw earlier, this entangles the mechanism of traversing the array with the business of summing the bits. So we can separate them using fold:
_(context: javascriptallonge.pdf (source-range-83ecb080-01936))_

> **const** arraySum = callLeft(foldArrayWith, (a, b) => a + b, 0); arraySum([1, 4, 9, 16, 25]) _//=> 55_
_(source: javascriptallonge.pdf (source-range-83ecb080-01938))_

> Context: Well, we call arraySum with an array, and it has baked into it a method for traversing the array. Perhaps we could extract both of those things. Let’s rearrange our code a bit:
_(context: javascriptallonge.pdf (source-range-83ecb080-01941))_

> **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
_(source: javascriptallonge.pdf (source-range-83ecb080-01944))_

> **const** foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === **undefined** ? terminalValue : fn(first, foldArrayWith(fn, terminalValue, rest));
_(source: javascriptallonge.pdf (source-range-83ecb080-01945))_

> **const** foldArray = (array) => callRight(foldArrayWith, array);
_(source: javascriptallonge.pdf (source-range-83ecb080-01946))_

> **const** sumFoldable = (folder) => folder((a, b) => a + b, 0);
_(source: javascriptallonge.pdf (source-range-83ecb080-01947))_

> sumFoldable(foldArray([1, 4, 9, 16, 25])) _//=> 55_
_(source: javascriptallonge.pdf (source-range-83ecb080-01948))_

> Context: Here it is summing a tree of numbers:
_(context: javascriptallonge.pdf (source-range-83ecb080-01950))_

> **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
_(source: javascriptallonge.pdf (source-range-83ecb080-01951))_

> Context: Here it is summing a tree of numbers:
_(context: javascriptallonge.pdf (source-range-83ecb080-01950))_

> **const** foldTree = (tree) => callRight(foldTreeWith, tree);
_(source: javascriptallonge.pdf (source-range-83ecb080-01953))_

> **const** sumFoldable = (folder) => folder((a, b) => a + b, 0);
_(source: javascriptallonge.pdf (source-range-83ecb080-01954))_

> sumFoldable(foldTree([1, [4, [9, 16]], 25])) _//=> 55_
_(source: javascriptallonge.pdf (source-range-83ecb080-01955))_

### **iterating**

- Nevertheless, there is some value in being able to express some algorithms as iteration. _(javascriptallonge.pdf (source-range-83ecb080-01960))_
- Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. _(javascriptallonge.pdf (source-range-83ecb080-01960))_
- JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. _(javascriptallonge.pdf (source-range-83ecb080-01961))_
- And worst of all, we’re getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0. _(javascriptallonge.pdf (source-range-83ecb080-01963))_
- Notice that buried inside our loop, we have bound the names done and value. _(javascriptallonge.pdf (source-range-83ecb080-01966))_
- We can put those into a POJO (a Plain Old JavaScript Object). _(javascriptallonge.pdf (source-range-83ecb080-01966))_
- Notice that buried inside our loop, we have bound the names done and value. _(javascriptallonge.pdf (source-range-83ecb080-01966))_
- All the summing code needs to know is to add eachIteration.value. _(javascriptallonge.pdf (source-range-83ecb080-01970))_
- With this code, we make a POJO that has done and value keys. _(javascriptallonge.pdf (source-range-83ecb080-01970))_
- Now this is something else. _(javascriptallonge.pdf (source-range-83ecb080-01976))_
- The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. _(javascriptallonge.pdf (source-range-83ecb080-01976))_
- We can write a different iterator for a different data structure. _(javascriptallonge.pdf (source-range-83ecb080-01977))_

> sum += eachIteration.value; } **return** sum; }
_(source: javascriptallonge.pdf (source-range-83ecb080-01974))_

> iteratorSum(arrayIterator([1, 4, 9, 16, 25])) _//=> 55_
_(source: javascriptallonge.pdf (source-range-83ecb080-01975))_

> **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }
_(source: javascriptallonge.pdf (source-range-83ecb080-01982))_

> **const** aListIterator = listIterator(list(1, 4, 9, 16, 25));
_(source: javascriptallonge.pdf (source-range-83ecb080-01983))_

### **unfolding and laziness**

- When they iterate over an array or linked list, they are traversing something that is already there. _(javascriptallonge.pdf (source-range-83ecb080-01987))_
- A function that starts with a seed and expands it into a data structure is called an _unfold_ . _(javascriptallonge.pdf (source-range-83ecb080-01995))_
- It’s possible to write a generic unfold mechanism, but let’s pass on to what we can do with unfolded iterators. _(javascriptallonge.pdf (source-range-83ecb080-01995))_
- A function that starts with a seed and expands it into a data structure is called an _unfold_ . _(javascriptallonge.pdf (source-range-83ecb080-01995))_
- This business of going on forever has some drawbacks. _(javascriptallonge.pdf (source-range-83ecb080-02001))_
- We can start with take, an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-83ecb080-02001))_
- We can start with take, an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-83ecb080-02001))_
- We’ll need an iterator that produces odd numbers. _(javascriptallonge.pdf (source-range-83ecb080-02003))_
- We could also write a filter for iterators to accompany our mapping function: _(javascriptallonge.pdf (source-range-83ecb080-02009))_
- Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. _(javascriptallonge.pdf (source-range-83ecb080-02013))_

> Context: Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let’s consider the simplest example:
_(context: javascriptallonge.pdf (source-range-83ecb080-01987))_

> **const** NumberIterator = (number = 0) => () => ({ done: **false** , value: number++ })
_(source: javascriptallonge.pdf (source-range-83ecb080-01988))_

> Context: Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let’s consider the simplest example:
_(context: javascriptallonge.pdf (source-range-83ecb080-01987))_

> fromOne = NumberIterator(1);
_(source: javascriptallonge.pdf (source-range-83ecb080-01989))_

> Context: Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let’s consider the simplest example:
_(context: javascriptallonge.pdf (source-range-83ecb080-01987))_

> fromOne().value; _//=> 1_ fromOne().value; _//=> 2_ fromOne().value; _//=> 3_ fromOne().value; _//=> 4_ fromOne().value; _//=> 5_
_(source: javascriptallonge.pdf (source-range-83ecb080-01990))_

> **const** squareOf = callLeft(mapIteratorWith, (x) => x * x)
_(source: javascriptallonge.pdf (source-range-83ecb080-02007))_

> toArray(take(squareOf(odds()), 5)) _//=> [1, 9, 25, 49, 81]_
_(source: javascriptallonge.pdf (source-range-83ecb080-02008))_

> Context: We could also write a filter for iterators to accompany our mapping function:
_(context: javascriptallonge.pdf (source-range-83ecb080-02009))_

> **const** oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1);
_(source: javascriptallonge.pdf (source-range-83ecb080-02011))_

> Context: We could also write a filter for iterators to accompany our mapping function:
_(context: javascriptallonge.pdf (source-range-83ecb080-02009))_

> toArray(take(squareOf(oddsOf(NumberIterator(1))), 5)) _//=> [1, 9, 25, 49, 81]_
_(source: javascriptallonge.pdf (source-range-83ecb080-02012))_

### **bonus**

- In Smalltalk, for example, they are known as collect, select, and detect. _(javascriptallonge.pdf (source-range-83ecb080-02015))_
- Many programmers coming to JavaScript from other languages are familiar with three “canonical” operations on collections: folding, filtering, and finding. _(javascriptallonge.pdf (source-range-83ecb080-02015))_
- In Smalltalk, for example, they are known as collect, select, and detect. _(javascriptallonge.pdf (source-range-83ecb080-02015))_
- This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. _(javascriptallonge.pdf (source-range-83ecb080-02020))_
- This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. _(javascriptallonge.pdf (source-range-83ecb080-02020))_
- And if fn had some sort of side-effect, the program could be buggy. _(javascriptallonge.pdf (source-range-83ecb080-02022))_
- JavaScript would apply fn to every element. _(javascriptallonge.pdf (source-range-83ecb080-02022))_
- If array was very large, and fn very slow, this would consume a lot of unnecessary time. _(javascriptallonge.pdf (source-range-83ecb080-02022))_

> Context: This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:
_(context: javascriptallonge.pdf (source-range-83ecb080-02020))_

> **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);
_(source: javascriptallonge.pdf (source-range-83ecb080-02019))_

> Context: This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:
_(context: javascriptallonge.pdf (source-range-83ecb080-02020))_

> **const** firstInArray = (fn, array) => array.filter(fn)[0];
_(source: javascriptallonge.pdf (source-range-83ecb080-02021))_

### **caveat**

- There are some important implications of stateful functions. _(javascriptallonge.pdf (source-range-83ecb080-02024))_
- One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. _(javascriptallonge.pdf (source-range-83ecb080-02024))_
- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer “own” that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-83ecb080-02025))_

## Making Data Out Of Functions

### **Making Data Out Of Functions**

- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. _(javascriptallonge.pdf (source-range-83ecb080-02032))_
- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-83ecb080-02033))_
- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-83ecb080-02033))_
- They searched for a radically simpler set of tools that could accomplish all of the same things. _(javascriptallonge.pdf (source-range-83ecb080-02040))_
- We can model lists just using functions. _(javascriptallonge.pdf (source-range-83ecb080-02041))_
- They established that arbitrary computations could be represented a small set of axiomatic components. _(javascriptallonge.pdf (source-range-83ecb080-02041))_
- For example, we don’t need arrays to represent lists, or even POJOs to represent nodes in a linked list. _(javascriptallonge.pdf (source-range-83ecb080-02041))_
- For example, we don’t need arrays to represent lists, or even POJOs to represent nodes in a linked list. _(javascriptallonge.pdf (source-range-83ecb080-02041))_
- The oscin.es[77] library contains code for all of the standard combinators and for experimenting using the standard notation. _(javascriptallonge.pdf (source-range-83ecb080-02043))_
- Let’s start with some of the building blocks of combinatory logic, the K, I, and V combinators, nicknamed the “Kestrel”, the “Idiot Bird”, and the “Vireo:” _(javascriptallonge.pdf (source-range-83ecb080-02044))_

> Context: For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list.
_(context: javascriptallonge.pdf (source-range-83ecb080-02033))_

> **const** EMPTY = {}; **const** OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } };
_(source: javascriptallonge.pdf (source-range-83ecb080-02036))_

> OneTwoThree.first _//=> 1_ OneTwoThree.rest.first _//=> 2_
_(source: javascriptallonge.pdf (source-range-83ecb080-02037))_

> OneTwoThree.rest.rest.first _//=> 3_ **const** length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1);
_(source: javascriptallonge.pdf (source-range-83ecb080-02038))_

> length(OneTwoThree) _//=> 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-02039))_

> **const** K = (x) => (y) => x; **const** I = (x) => (x); **const** V = (x) => (y) => (z) => z(x)(y);
_(source: javascriptallonge.pdf (source-range-83ecb080-02049))_

### **the kestrel and the idiot**

- You give it a value, and it returns a constant function that gives that value. _(javascriptallonge.pdf (source-range-83ecb080-02051))_
- The kestrel, or K, is a function that makes constant functions. _(javascriptallonge.pdf (source-range-83ecb080-02051))_
- A _constant function_ is a function that always returns the same thing, no matter what you give it. _(javascriptallonge.pdf (source-range-83ecb080-02051))_
- The _identity function_ is a function that evaluates to whatever parameter you pass it. _(javascriptallonge.pdf (source-range-83ecb080-02056))_
- Given two values, we can say that K always returns the _first_ value: K(x)(y) => x (that’s not valid JavaScript, but it’s essentially how it works). _(javascriptallonge.pdf (source-range-83ecb080-02060))_
- Given two values, we can say that K always returns the _first_ value, and given two values, K(I) always returns the _second_ value. _(javascriptallonge.pdf (source-range-83ecb080-02074))_

> **const** K = (x) => (y) => x; **const** fortyTwo = K(42);
_(source: javascriptallonge.pdf (source-range-83ecb080-02053))_

> fortyTwo(6) _//=> 42_
_(source: javascriptallonge.pdf (source-range-83ecb080-02054))_

> fortyTwo("Hello") _//=> 42_
_(source: javascriptallonge.pdf (source-range-83ecb080-02055))_

> K(6)(7) _//=> 6_
_(source: javascriptallonge.pdf (source-range-83ecb080-02058))_

> K(12)(24) _//=> 12_
_(source: javascriptallonge.pdf (source-range-83ecb080-02059))_

> Context: Now, an interesting thing happens when we pass functions to each other. Consider K(I). From what we just wrote, K(x)(y) => x So K(I)(x) => I. Makes sense. Now let’s tack one more invocation on: What is K(I)(x)(y)? If K(I)(x) => I, then K(I)(x)(y) === I(y) which is y.
_(context: javascriptallonge.pdf (source-range-83ecb080-02061))_

> Therefore, K(I)(x)(y) => y:
_(source: javascriptallonge.pdf (source-range-83ecb080-02062))_

> K(I)(6)(7) _//=> 7_
_(source: javascriptallonge.pdf (source-range-83ecb080-02065))_

> K(I)(12)(24) _//=> 24_
_(source: javascriptallonge.pdf (source-range-83ecb080-02066))_

> K("primus")("secundus") _//=> "primus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02068))_

> K(I)("primus")("secundus") _//=> "secundus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02069))_

> Context: If we are not feeling particularly academic, we can name our functions:
_(context: javascriptallonge.pdf (source-range-83ecb080-02070))_

> **const** first = K, second = K(I);
_(source: javascriptallonge.pdf (source-range-83ecb080-02071))_

> Context: If we are not feeling particularly academic, we can name our functions:
_(context: javascriptallonge.pdf (source-range-83ecb080-02070))_

> first("primus")("secundus") _//=> "primus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02072))_

> Context: If we are not feeling particularly academic, we can name our functions:
_(context: javascriptallonge.pdf (source-range-83ecb080-02070))_

> second("primus")("secundus") _//=> "secundus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02073))_

### **backwardness**

- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. _(javascriptallonge.pdf (source-range-83ecb080-02076))_
- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. _(javascriptallonge.pdf (source-range-83ecb080-02085))_
- So if we wanted to use them with a two-element array, we’d need to have a piece of code that calls some code. _(javascriptallonge.pdf (source-range-83ecb080-02086))_
- Our latin data structure is no longer a dumb data structure, it’s a function. _(javascriptallonge.pdf (source-range-83ecb080-02093))_

> Context: Our first and second functions are a little different than what most people are used to when we talk about functions that access data. If we represented a pair of values as an array, we’d write them like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-02076))_

> **const** first = ([first, second]) => first, second = ([first, second]) => second;
_(source: javascriptallonge.pdf (source-range-83ecb080-02079))_

> **const** latin = ["primus", "secundus"];
_(source: javascriptallonge.pdf (source-range-83ecb080-02080))_

> first(latin) _//=> "primus"_ second(latin) _//=> "secundus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02081))_

> Context: Or if we were using a POJO, we’d write them like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-02082))_

> **const** first = ({first, second}) => first, second = ({first, second}) => second; **const** latin = {first: "primus", second: "secundus"};
_(source: javascriptallonge.pdf (source-range-83ecb080-02083))_

> Context: Or if we were using a POJO, we’d write them like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-02082))_

> first(latin) _//=> "primus"_ second(latin) _//=> "secundus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02084))_

> **const** first = K, second = K(I);
_(source: javascriptallonge.pdf (source-range-83ecb080-02088))_

> **const** latin = (selector) => selector("primus")("secundus");
_(source: javascriptallonge.pdf (source-range-83ecb080-02089))_

> latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02090))_

### **the vireo**

- In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-83ecb080-02095))_
- For consistency with the way combinators are written as functions taking just one parameter, we’ll curry[78] the function: _(javascriptallonge.pdf (source-range-83ecb080-02098))_
- Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specific pair, we’ll use the name aPair by default): _(javascriptallonge.pdf (source-range-83ecb080-02100))_
- It is known to most programmers as .tap. _(javascriptallonge.pdf (source-range-83ecb080-02114))_
- It says, “take these two values and apply them to this function.” There are other, similar combinators that apply values to functions. _(javascriptallonge.pdf (source-range-83ecb080-02114))_
- One notable example is the “thrush” or T combinator: It takes one value and applies it to a function. _(javascriptallonge.pdf (source-range-83ecb080-02114))_
- As an aside, the Vireo is a little like JavaScript’s .apply function. _(javascriptallonge.pdf (source-range-83ecb080-02114))_

> Context: For “data” we access with K and K(I), our “structure” is the function (selector) => selector("primus")("secundus"). Let’s extract those into parameters:
_(context: javascriptallonge.pdf (source-range-83ecb080-02096))_

> (first, second) => (selector) => selector(first)(second)
_(source: javascriptallonge.pdf (source-range-83ecb080-02097))_

> Context: For consistency with the way combinators are written as functions taking just one parameter, we’ll curry[78] the function:
_(context: javascriptallonge.pdf (source-range-83ecb080-02098))_

> (first) => (second) => (selector) => selector(first)(second)
_(source: javascriptallonge.pdf (source-range-83ecb080-02099))_

> Context: Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specific pair, we’ll use the name aPair by default):
_(context: javascriptallonge.pdf (source-range-83ecb080-02100))_

> **const** first = K, second = K(I), pair = (first) => (second) => (selector) => selector(first)(second);
_(source: javascriptallonge.pdf (source-range-83ecb080-02101))_

> Context: Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specific pair, we’ll use the name aPair by default):
_(context: javascriptallonge.pdf (source-range-83ecb080-02100))_

> **const** latin = pair("primus")("secundus");
_(source: javascriptallonge.pdf (source-range-83ecb080-02102))_

> If we change the names to x, y, and z, we get: (x) => (y) => (z) => z(x)(y).
_(source: javascriptallonge.pdf (source-range-83ecb080-02107))_

> **const** first = K, second = K(I), pair = V;
_(source: javascriptallonge.pdf (source-range-83ecb080-02111))_

> **const** latin = pair("primus")("secundus");
_(source: javascriptallonge.pdf (source-range-83ecb080-02112))_

> latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02113))_

### **lists with functions as data**

- Here’s another look at linked lists using POJOs. _(javascriptallonge.pdf (source-range-83ecb080-02117))_
- reverse(delayed) : mapWith(fn, rest(aPair), pair(fn(first(aPair)), delayed)); _(javascriptallonge.pdf (source-range-83ecb080-02124))_
- We write them in a backwards way, but they seem to work. _(javascriptallonge.pdf (source-range-83ecb080-02131))_
- And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else. _(javascriptallonge.pdf (source-range-83ecb080-02133))_
- Presto, **we can use pure functions to represent a linked list** . _(javascriptallonge.pdf (source-range-83ecb080-02133))_
- We used functions to replace arrays and POJOs, but we still use JavaScript’s built-in operators to test for equality (===) and to branch ?:. _(javascriptallonge.pdf (source-range-83ecb080-02137))_

> Context: We can write length and mapWith functions over it:
_(context: javascriptallonge.pdf (source-range-83ecb080-02119))_

> **const** length = (aPair) => aPair === EMPTY ? 0 : 1 + length(rest(aPair));
_(source: javascriptallonge.pdf (source-range-83ecb080-02122))_

> length(l123) _//=> 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-02123))_

> **const** doubled = mapWith((x) => x * 2, l123); first(doubled) _//=> 2_ first(rest(doubled)) _//=> 4_ first(rest(rest(doubled))) _//=> 6_
_(source: javascriptallonge.pdf (source-range-83ecb080-02125))_

> Context: Can we do the same with the linked lists we build out of functions? Yes:
_(context: javascriptallonge.pdf (source-range-83ecb080-02126))_

> **const** first = K, rest = K(I), pair = V, EMPTY = (() => {}); **const** l123 = pair(1)(pair(2)(pair(3)(EMPTY))); l123(first) _//=> 1_ l123(rest)(first)
_(source: javascriptallonge.pdf (source-range-83ecb080-02127))_

### **say “please”**

- This follows the philosophy we used with data structures: The function doing the work inspects the data structure. _(javascriptallonge.pdf (source-range-83ecb080-02139))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-83ecb080-02140))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-83ecb080-02140))_
- Let’s presume we are working with a slightly higher abstraction, we’ll call it a list. _(javascriptallonge.pdf (source-range-83ecb080-02142))_
- Now we’ll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. _(javascriptallonge.pdf (source-range-83ecb080-02144))_
- We can write reverse and mapWith as well. _(javascriptallonge.pdf (source-range-83ecb080-02158))_
- We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else. _(javascriptallonge.pdf (source-range-83ecb080-02162))_

> Context: We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. Here’s length again:
_(context: javascriptallonge.pdf (source-range-83ecb080-02140))_

> **const** length = (aPair) => aPair === EMPTY ? 0 : 1 + length(aPair(rest));
_(source: javascriptallonge.pdf (source-range-83ecb080-02141))_

> Context: Let’s presume we are working with a slightly higher abstraction, we’ll call it a list. Instead of writing length(list) and examining a list, we’ll write something like:
_(context: javascriptallonge.pdf (source-range-83ecb080-02142))_

> **const** length = (list) => list( () => 0, (aPair) => 1 + length(aPair(rest))) );
_(source: javascriptallonge.pdf (source-range-83ecb080-02143))_

> Context: We’ll also write a handy list printer:
_(context: javascriptallonge.pdf (source-range-83ecb080-02149))_

> **const** print = (list) => list( () => "", (aPair) => ` **${** aPair(pairFirst) **} ${** print(aPair(pairRest)) **}** ` );
_(source: javascriptallonge.pdf (source-range-83ecb080-02150))_

> Context: How would all this work? Let’s start with the obvious. What is an empty list?
_(context: javascriptallonge.pdf (source-range-83ecb080-02151))_

> **const** EMPTYLIST = (whenEmpty, unlessEmpty) => whenEmpty()
_(source: javascriptallonge.pdf (source-range-83ecb080-02152))_

> Context: And what is a node of a list?
_(context: javascriptallonge.pdf (source-range-83ecb080-02153))_

> **const** node = (x) => (y) => (whenEmpty, unlessEmpty) => unlessEmpty(pair(x)(y));
_(source: javascriptallonge.pdf (source-range-83ecb080-02154))_

> **const** l123 = node(1)(node(2)(node(3)(EMPTYLIST)));
_(source: javascriptallonge.pdf (source-range-83ecb080-02156))_

> print(l123) _//=> 1 2 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-02157))_

### **functions are not the real point**

- There are lots of similar texts explaining how to construct complex semantics out of functions. _(javascriptallonge.pdf (source-range-83ecb080-02164))_
- You can establish that K and K(I) can represent true and false, model magnitudes with Church Numerals[79] or Surreal Numbers[80] , and build your way up to printing FizzBuzz. _(javascriptallonge.pdf (source-range-83ecb080-02164))_
- Functions are a fundamental building block of computation. _(javascriptallonge.pdf (source-range-83ecb080-02166))_
- They are “axioms” of combinatory logic, and can be used to compute anything that JavaScript can compute. _(javascriptallonge.pdf (source-range-83ecb080-02166))_
- Knowing how to make a linked list out of functions is not really necessary for the working programmer. _(javascriptallonge.pdf (source-range-83ecb080-02167))_
- However, that is not the interesting thing to note here. _(javascriptallonge.pdf (source-range-83ecb080-02167))_
- (Knowing that it can be done, on the other hand, is very important to understanding computer science.) _(javascriptallonge.pdf (source-range-83ecb080-02167))_
- Practically speaking, languages like JavaScript already provide arrays with mapping and folding methods, choice operations, and other rich constructs. _(javascriptallonge.pdf (source-range-83ecb080-02167))_
- Knowing how to make a list out of just functions is a little like knowing that photons are the Gauge Bosons[81] of the electromagnetic force. _(javascriptallonge.pdf (source-range-83ecb080-02168))_

### **a return to backward thinking**

- As it happened, the pair was composed by the vireo (or V combinator): (x) => (y) => (z) => z(x)(y). _(javascriptallonge.pdf (source-range-83ecb080-02176))_
- To make pairs work, we did things _backwards_ , we passed the first and rest functions to the pair, and the pair called our function. _(javascriptallonge.pdf (source-range-83ecb080-02176))_
- All we know is that we can pass the pair function a function of our own, at it will be called with the elements of the pair. _(javascriptallonge.pdf (source-range-83ecb080-02177))_
- But we could have done something completely different. _(javascriptallonge.pdf (source-range-83ecb080-02177))_
- We could have written a pair that stored its elements in an array, or a pair that stored its elements in a POJO. _(javascriptallonge.pdf (source-range-83ecb080-02177))_
- The exact implementation of a pair is hidden from the code that uses a pair. _(javascriptallonge.pdf (source-range-83ecb080-02178))_
- This is a little gratuitous, but it makes the point: The code that uses the data doesn’t reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. _(javascriptallonge.pdf (source-range-83ecb080-02185))_
- We’re passing list what we want done with an empty list, and what we want done with a list that has at least one element. _(javascriptallonge.pdf (source-range-83ecb080-02187))_
- We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-83ecb080-02187))_
- We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-83ecb080-02187))_
- This is fundamentally _not_ the same thing as this code for the length of a linked list: _(javascriptallonge.pdf (source-range-83ecb080-02190))_
- It presumes there is one canonical empty list value. _(javascriptallonge.pdf (source-range-83ecb080-02195))_
- We can fix this with an isEmpty function, but now we’re pushing even more knowledge about the structure of lists into the code that uses them. _(javascriptallonge.pdf (source-range-83ecb080-02195))_
- It presumes you can compare these things with the === operator. _(javascriptallonge.pdf (source-range-83ecb080-02195))_
- This is a fundamental principle of good design. _(javascriptallonge.pdf (source-range-83ecb080-02196))_
- Having a list know itself whether it is empty hides implementation information from the code that uses lists. _(javascriptallonge.pdf (source-range-83ecb080-02196))_
- It is a tenet of Object-Oriented Programming, but it is **not** exclusive to OOP: We can and should design data structures to hide implementation information from the code that use them, whether we are working with functions, objects, or both. _(javascriptallonge.pdf (source-range-83ecb080-02196))_
- There are many tools for hiding implementation information, and we have now seen two particularly powerful patterns: _(javascriptallonge.pdf (source-range-83ecb080-02197))_
- - Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. _(javascriptallonge.pdf (source-range-83ecb080-02198))_

> Context: The exact implementation of a pair is hidden from the code that uses a pair. Here, we’ll prove it:
_(context: javascriptallonge.pdf (source-range-83ecb080-02178))_

> **const** first = K, second = K(I), pair = (first) => (second) => { **const** pojo = {first, second};
_(source: javascriptallonge.pdf (source-range-83ecb080-02179))_

> Context: The exact implementation of a pair is hidden from the code that uses a pair. Here, we’ll prove it:
_(context: javascriptallonge.pdf (source-range-83ecb080-02178))_

> **return** (selector) => selector(pojo.first)(pojo.second); };
_(source: javascriptallonge.pdf (source-range-83ecb080-02180))_

> Context: The exact implementation of a pair is hidden from the code that uses a pair. Here, we’ll prove it:
_(context: javascriptallonge.pdf (source-range-83ecb080-02178))_

> **const** latin = pair("primus")("secundus");
_(source: javascriptallonge.pdf (source-range-83ecb080-02181))_

> latin(second) _//=> "secundus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02184))_

> Context: This is a little gratuitous, but it makes the point: The code that uses the data doesn’t reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. The same thing happens with our lists. Here’s length for lists:
_(context: javascriptallonge.pdf (source-range-83ecb080-02185))_

> **const** length = (list) => list( () => 0, (aPair) => 1 + length(aPair(pairRest))) );
_(source: javascriptallonge.pdf (source-range-83ecb080-02186))_

> Context: We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally _not_ the same thing as this code for the length of a linked list:
_(context: javascriptallonge.pdf (source-range-83ecb080-02190))_

> **const** length = (node, delayed = 0) =>
_(source: javascriptallonge.pdf (source-range-83ecb080-02191))_

> Context: We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally _not_ the same thing as this code for the length of a linked list:
_(context: javascriptallonge.pdf (source-range-83ecb080-02190))_

> node === EMPTY
_(source: javascriptallonge.pdf (source-range-83ecb080-02192))_

## Recipes with Data

### **Recipes with Data**

### **Disclaimer**

- The overall _use_ of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-83ecb080-02207))_
- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven’t been discussed in the text to this point, such as methods and/or prototypes. _(javascriptallonge.pdf (source-range-83ecb080-02207))_
- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven’t been discussed in the text to this point, such as methods and/or prototypes. _(javascriptallonge.pdf (source-range-83ecb080-02207))_
- The overall _use_ of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-83ecb080-02207))_

## mapWith

### **mapWith**

- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. _(javascriptallonge.pdf (source-range-83ecb080-02219))_
- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. _(javascriptallonge.pdf (source-range-83ecb080-02219))_
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. _(javascriptallonge.pdf (source-range-83ecb080-02223))_
- But for the purposes of discussing ideas, we can use the same name twice in two different contexts. _(javascriptallonge.pdf (source-range-83ecb080-02223))_
- > 82Yes, we also used the name mapWith for working with ordinary collections elsewhere. _(javascriptallonge.pdf (source-range-83ecb080-02223))_
- It’s the same idea, after all. _(javascriptallonge.pdf (source-range-83ecb080-02223))_
- If we didn’t use mapWith, we’d could have also used callRight with map to accomplish the same result: _(javascriptallonge.pdf (source-range-83ecb080-02228))_
- mapWith is a very convenient abstraction for a very common pattern. _(javascriptallonge.pdf (source-range-83ecb080-02231))_

> In JavaScript, arrays have a .map method. Map takes a function as an argument, and applies it to each of the elements of the array, then returns the results in another array. For example:
_(source: javascriptallonge.pdf (source-range-83ecb080-02212))_

> Context: In JavaScript, arrays have a .map method. Map takes a function as an argument, and applies it to each of the elements of the array, then returns the results in another array. For example:
_(context: javascriptallonge.pdf (source-range-83ecb080-02212))_

> [1, 2, 3, 4, 5].map(x => x * x) _//=> [1, 4, 9, 16, 25]_
_(source: javascriptallonge.pdf (source-range-83ecb080-02213))_

> Context: We could write a function that behaves like the .map method if we wanted:
_(context: javascriptallonge.pdf (source-range-83ecb080-02214))_

> **const** map = (list, fn) => list.map(fn);
_(source: javascriptallonge.pdf (source-range-83ecb080-02215))_

> Context: **const** map = (list, fn) => list.map(fn); That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map:
_(context: javascriptallonge.pdf (source-range-83ecb080-02215, source-range-83ecb080-02219))_

> **const** mapWith = (fn) => (list) => list.map(fn);
_(source: javascriptallonge.pdf (source-range-83ecb080-02217))_

> Context: That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map:
_(context: javascriptallonge.pdf (source-range-83ecb080-02219))_

> **const** squaresOf = (list) => list.map(x => x * x);
_(source: javascriptallonge.pdf (source-range-83ecb080-02220))_

> Context: **const** squaresOf = (list) => list.map(x => x * x);
_(context: javascriptallonge.pdf (source-range-83ecb080-02220))_

> squaresOf([1, 2, 3, 4, 5]) _//=> [1, 4, 9, 16, 25]_
_(source: javascriptallonge.pdf (source-range-83ecb080-02221))_

> Context: > 82Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It’s the same idea, after all. If we didn’t use mapWith, we’d could have also used callRight with map to accomplish the same result:
_(context: javascriptallonge.pdf (source-range-83ecb080-02223, source-range-83ecb080-02228))_

> **const** squaresOf = mapWith(n => n * n);
_(source: javascriptallonge.pdf (source-range-83ecb080-02226))_

> Context: If we didn’t use mapWith, we’d could have also used callRight with map to accomplish the same result:
_(context: javascriptallonge.pdf (source-range-83ecb080-02228))_

> squaresOf([1, 2, 3, 4, 5]) _//=> [1, 4, 9, 16, 25]_
_(source: javascriptallonge.pdf (source-range-83ecb080-02227))_

> Context: If we didn’t use mapWith, we’d could have also used callRight with map to accomplish the same result:
_(context: javascriptallonge.pdf (source-range-83ecb080-02228))_

> **const** squaresOf = callRight(map, (n => n * n);
_(source: javascriptallonge.pdf (source-range-83ecb080-02229))_

> Context: If we didn’t use mapWith, we’d could have also used callRight with map to accomplish the same result:
_(context: javascriptallonge.pdf (source-range-83ecb080-02228))_

> squaresOf([1, 2, 3, 4, 5]) _//=> [1, 4, 9, 16, 25]_
_(source: javascriptallonge.pdf (source-range-83ecb080-02230))_

## Flip

### **Flip**

- Let’s consider the case whether we have a map function of our own, perhaps from the allong.es[84] library, perhaps from Underscore[85] . _(javascriptallonge.pdf (source-range-83ecb080-02240))_
- What we have now is a function that takes a function and “flips” the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-83ecb080-02253))_
- What we have now is a function that takes a function and “flips” the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-83ecb080-02253))_

> Context: We wrote mapWith like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-02238))_

> **const** mapWith = (fn) => (list) => list.map(fn);
_(source: javascriptallonge.pdf (source-range-83ecb080-02239))_

> Context: Let’s consider the case whether we have a map function of our own, perhaps from the allong.es[84] library, perhaps from Underscore[85] . We could write our function something like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-02240))_

> **const** mapWith = (fn) => (list) => map(list, fn);
_(source: javascriptallonge.pdf (source-range-83ecb080-02241))_

> Context: **const** mapWith = (fn) => (list) => map(list, fn);
_(context: javascriptallonge.pdf (source-range-83ecb080-02241))_

> You can see that if we simplify it:
_(source: javascriptallonge.pdf (source-range-83ecb080-02242))_

> Context: Looking at this, we see we’re conflating two separate transformations. First, we’re reversing the order of arguments. You can see that if we simplify it:
_(context: javascriptallonge.pdf (source-range-83ecb080-02242))_

> **const** mapWith = (fn, list) => map(list, fn);
_(source: javascriptallonge.pdf (source-range-83ecb080-02243))_

> Context: Second, we’re “currying” the function so that instead of defining a function that takes two arguments, it returns a function that takes the first argument and returns a function that takes the second argument and applies them both, like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-02244))_

> **const** mapper = (list) => (fn) => map(list, fn);
_(source: javascriptallonge.pdf (source-range-83ecb080-02245))_

> Context: Let’s return to the implementation of mapWith that relies on a map function rather than a method:
_(context: javascriptallonge.pdf (source-range-83ecb080-02246))_

> **const** mapWith = (fn) => (list) => map(list, fn);
_(source: javascriptallonge.pdf (source-range-83ecb080-02247))_

> Context: We’re going to extract these two operations by refactoring our function to paramaterize map. The first step is to give our parameters generic names:
_(context: javascriptallonge.pdf (source-range-83ecb080-02248))_

> **const** mapWith = (first) => (second) => map(second, first);
_(source: javascriptallonge.pdf (source-range-83ecb080-02249))_

> Context: We’re going to extract these two operations by refactoring our function to paramaterize map. The first step is to give our parameters generic names:
_(context: javascriptallonge.pdf (source-range-83ecb080-02248))_

> **const** wrapper = (fn) =>
_(source: javascriptallonge.pdf (source-range-83ecb080-02251))_

> (first) => (second) => fn(second, first);
_(source: javascriptallonge.pdf (source-range-83ecb080-02252))_

> **const** flipAndCurry = (fn) => (first) => (second) => fn(second, first);
_(source: javascriptallonge.pdf (source-range-83ecb080-02258))_

> Context: Sometimes you want to flip, but not curry:
_(context: javascriptallonge.pdf (source-range-83ecb080-02259))_

> **const** flip = (fn) =>
_(source: javascriptallonge.pdf (source-range-83ecb080-02260))_

> Context: Sometimes you want to flip, but not curry:
_(context: javascriptallonge.pdf (source-range-83ecb080-02259))_

> (first, second) => fn(second, first);
_(source: javascriptallonge.pdf (source-range-83ecb080-02261))_

> Context: This is gold. Consider how we define mapWith now:
_(context: javascriptallonge.pdf (source-range-83ecb080-02262))_

> **var** mapWith = flipAndCurry(map);
_(source: javascriptallonge.pdf (source-range-83ecb080-02263))_

### **self-currying flip**

- Sometimes we’ll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). _(javascriptallonge.pdf (source-range-83ecb080-02266))_

> Context: Sometimes we’ll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We _could_ make that into flip:
_(context: javascriptallonge.pdf (source-range-83ecb080-02266))_

> Now if we write mapWith = flip(map), we can call mapWith(fn, list) or mapWith(fn)(list), our choice.
_(source: javascriptallonge.pdf (source-range-83ecb080-02268))_

### **flipping methods**

- When we learn about context and methods, we’ll see that flip throws the current context away, so it can’t be used to flip methods. _(javascriptallonge.pdf (source-range-83ecb080-02270))_

## Object.assign

### **Object.assign**

- Both needs can be met with Object.assign, a standard function. _(javascriptallonge.pdf (source-range-83ecb080-02282))_

> Context: It’s very common to want to “extend” an object by assigning properties to it:
_(context: javascriptallonge.pdf (source-range-83ecb080-02278))_

> **const** inventory = { apples: 12, oranges: 12 }; inventory.bananas = 54; inventory.pears = 24;
_(source: javascriptallonge.pdf (source-range-83ecb080-02279))_

> Context: Both needs can be met with Object.assign, a standard function. You can copy an object by extending an empty object:
_(context: javascriptallonge.pdf (source-range-83ecb080-02282))_

> Object.assign({}, { apples: 12, oranges: 12 }) _//=> { apples: 12, oranges: 12 }_
_(source: javascriptallonge.pdf (source-range-83ecb080-02283))_

> Context: You can extend one object with another:
_(context: javascriptallonge.pdf (source-range-83ecb080-02284))_

> **const** inventory = { apples: 12, oranges: 12 }; **const** shipment = { bananas: 54, pears: 24 } Object.assign(inventory, shipment)
_(source: javascriptallonge.pdf (source-range-83ecb080-02285))_

### });

## Why?

### **Why?**

- It enables you to make recursive functions without needing to bind a function to a name in an environment. _(javascriptallonge.pdf (source-range-83ecb080-02304))_
- This has little practical utility in JavaScript, but in combinatory logic it’s essential: With fixed-point combinators it’s possible to compute everything computable without binding names. _(javascriptallonge.pdf (source-range-83ecb080-02304))_
- Well, besides all of the practical applications that combinators provide, there is this little thing called _The joy of working things out._ _(javascriptallonge.pdf (source-range-83ecb080-02305))_
- There are many explanations of the Y Combinator’s mechanism on the internet, but resist the temptation to read any of them: Work it out for yourself. _(javascriptallonge.pdf (source-range-83ecb080-02306))_
- One tip is to use JavaScript to name things. _(javascriptallonge.pdf (source-range-83ecb080-02307))_
- Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-83ecb080-02310))_
- Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-83ecb080-02310))_

> Context: This is the canonical Y Combinator[86] :
_(context: javascriptallonge.pdf (source-range-83ecb080-02300))_

> **const** Y = (f) => ( x => f(v => x(x)(v)) )( x => f(v => x(x)(v)) );
_(source: javascriptallonge.pdf (source-range-83ecb080-02301))_

> Context: One tip is to use JavaScript to name things. For example, you could start by writing:
_(context: javascriptallonge.pdf (source-range-83ecb080-02307))_

> **const** Y = (f) => { **const** something = x => f(v => x(x)(v));
_(source: javascriptallonge.pdf (source-range-83ecb080-02308))_

## A Warm Cup: Basic Strings and Quasi-Literals

### **A Warm Cup: Basic Strings and Quasi-Literals**

- An expression is any valid unit of code that resolves to a value.—Mozilla Development Network: Expressions and operators[87] _(javascriptallonge.pdf (source-range-83ecb080-02319))_
- Special characters can be included in a string literal by means of an _escape sequence_ . _(javascriptallonge.pdf (source-range-83ecb080-02320))_
- For example, the escape sequence \n inserts a newline character in a string literal, like this: 'first line\nsecond line'. _(javascriptallonge.pdf (source-range-83ecb080-02320))_
- Special characters can be included in a string literal by means of an _escape sequence_ . _(javascriptallonge.pdf (source-range-83ecb080-02320))_
- There are operators that can be used on strings. _(javascriptallonge.pdf (source-range-83ecb080-02321))_
- String manipulation is extremely common in programming. _(javascriptallonge.pdf (source-range-83ecb080-02323))_
- Writing is a big part of what makes us human, and strings are how JavaScript and most other languages represent writing. _(javascriptallonge.pdf (source-range-83ecb080-02323))_

> Context: There are operators that can be used on strings. The most common is +, it _concatenates_ :
_(context: javascriptallonge.pdf (source-range-83ecb080-02321))_

> 'fu' + 'bar' _//=> 'fubar'_
_(source: javascriptallonge.pdf (source-range-83ecb080-02322))_

### **quasi-literals**

- Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-83ecb080-02325))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-83ecb080-02328))_
- A quasi-literal can contain an expression to be evaluated. _(javascriptallonge.pdf (source-range-83ecb080-02328))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-83ecb080-02328))_
- A quasi-literal is computationally equivalent to an expression using +. _(javascriptallonge.pdf (source-range-83ecb080-02332))_
- However, there is a big semantic difference between a quasi-literal and an expression. _(javascriptallonge.pdf (source-range-83ecb080-02338))_
- Quasi-literals are expressions that resemble their result. _(javascriptallonge.pdf (source-range-83ecb080-02338))_

> Context: Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this “unquoting,” the more contemporary term is “interpolation.” An unquoted expression is inserted in a quasi-literal with ${expression}. The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.
_(context: javascriptallonge.pdf (source-range-83ecb080-02328))_

> `foobar` _//=> 'foobar'_
_(source: javascriptallonge.pdf (source-range-83ecb080-02326))_

> Context: Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this “unquoting,” the more contemporary term is “interpolation.” An unquoted expression is inserted in a quasi-literal with ${expression}. The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.
_(context: javascriptallonge.pdf (source-range-83ecb080-02328))_

> `fizz` + `buzz` _//=> 'fizzbuzz'_
_(source: javascriptallonge.pdf (source-range-83ecb080-02327))_

> Context: For example: A quasi-literal is computationally equivalent to an expression using +. So the above expression could also be written:
_(context: javascriptallonge.pdf (source-range-83ecb080-02329, source-range-83ecb080-02332))_

> - `A popular number for nerds is **${** 40 + 2 **}** `
_(source: javascriptallonge.pdf (source-range-83ecb080-02330))_

> Context: However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They’re easier to read and it’s easier to avid errors like the following:
_(context: javascriptallonge.pdf (source-range-83ecb080-02338))_

> - 'A popular number for nerds is ' + (40 + 2)
_(source: javascriptallonge.pdf (source-range-83ecb080-02336))_

> Context: However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They’re easier to read and it’s easier to avid errors like the following:
_(context: javascriptallonge.pdf (source-range-83ecb080-02338))_

> - 'A popular number for nerds is' + (40 + 2)
_(source: javascriptallonge.pdf (source-range-83ecb080-02339))_

### **evaluation time**

- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function’s body is evaluated. _(javascriptallonge.pdf (source-range-83ecb080-02348))_
- Thus, name is not bound to "Harry", it is bound to 'Arthur Dent', the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-83ecb080-02348))_
- Thus, name is not bound to "Harry", it is bound to 'Arthur Dent', the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-83ecb080-02348))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function’s body is evaluated. _(javascriptallonge.pdf (source-range-83ecb080-02348))_

> **const** name = "Harry";
_(source: javascriptallonge.pdf (source-range-83ecb080-02344))_

> **const** greeting = (name) => `Hello my name is **${** name **}** `;
_(source: javascriptallonge.pdf (source-range-83ecb080-02345))_

> Context: This is exactly what we’d expect if we’d written it like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-02349))_

> **const** greeting = (name) => 'Hello my name is ' + name;
_(source: javascriptallonge.pdf (source-range-83ecb080-02350))_

## Served by the Pot: Collections

### **Served by the Pot: Collections**

- **Some different sized and coloured coffee pots by Antti Nurmesniemi, perhaps his most known design.** _(javascriptallonge.pdf (source-range-83ecb080-02356))_

## Iteration and Iterables

### **Iteration and Iterables**

- Many objects in JavaScript can model collections of things. _(javascriptallonge.pdf (source-range-83ecb080-02363))_
- But sometimes you want to open it up and do things with its contents. _(javascriptallonge.pdf (source-range-83ecb080-02363))_
- Acting on the elements of a collection one at a time is called _iterating over the contents_ , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-83ecb080-02365))_
- Acting on the elements of a collection one at a time is called _iterating over the contents_ , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-83ecb080-02365))_

### **a look back at functional iterators**

- We can do the same thing for objects. _(javascriptallonge.pdf (source-range-83ecb080-02367))_
- Note that it uses the function keyword, so when we invoke it with stack.iterator(), JavaScript sets this to the value of stack. _(javascriptallonge.pdf (source-range-83ecb080-02375))_
- } function, and that’s where this is bound to the value of stack. _(javascriptallonge.pdf (source-range-83ecb080-02376))_
- Since JavaScript doesn’t bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. _(javascriptallonge.pdf (source-range-83ecb080-02376))_
- Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter(). _(javascriptallonge.pdf (source-range-83ecb080-02377))_
- Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter(). _(javascriptallonge.pdf (source-range-83ecb080-02377))_
- We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method: _(javascriptallonge.pdf (source-range-83ecb080-02388))_
- If we write a program with the presumption that “everything is an object,” we can write maps, folds, and filters that work on objects. _(javascriptallonge.pdf (source-range-83ecb080-02393))_
- Our functions don’t need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-83ecb080-02393))_

> **const** iter = stack.iterator(); iter().value _//=> "you!"_ iter().value _//=> "to"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02373))_

> Context: And here’s a sum function implemented as a fold over a functional iterator:
_(context: javascriptallonge.pdf (source-range-83ecb080-02378))_

> **const** iteratorSum = (iterator) => { **let** eachIteration, sum = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02379))_

> Context: And here’s a sum function implemented as a fold over a functional iterator:
_(context: javascriptallonge.pdf (source-range-83ecb080-02378))_

> **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }
_(source: javascriptallonge.pdf (source-range-83ecb080-02380))_

> Context: We can use it with our stack:
_(context: javascriptallonge.pdf (source-range-83ecb080-02381))_

> **const** stack = Stack1();
_(source: javascriptallonge.pdf (source-range-83ecb080-02384))_

> Context: We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:
_(context: javascriptallonge.pdf (source-range-83ecb080-02388))_

> **const** collectionSum = (collection) => { **const** iterator = collection.iterator();
_(source: javascriptallonge.pdf (source-range-83ecb080-02389))_

> Context: We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:
_(context: javascriptallonge.pdf (source-range-83ecb080-02388))_

> **let** eachIteration, sum = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02390))_

> Context: We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:
_(context: javascriptallonge.pdf (source-range-83ecb080-02388))_

> **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }
_(source: javascriptallonge.pdf (source-range-83ecb080-02391))_

> collectionSum(stack) _//=> 6_
_(source: javascriptallonge.pdf (source-range-83ecb080-02392))_

### **iterator objects**

- Iteration for functions and objects has been around for many, many decades. _(javascriptallonge.pdf (source-range-83ecb080-02396))_
- In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. _(javascriptallonge.pdf (source-range-83ecb080-02397))_
- The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-83ecb080-02397))_
- The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-83ecb080-02397))_
- Fortunately, an iterator object is almost as simple as an iterator function. _(javascriptallonge.pdf (source-range-83ecb080-02400))_
- Instead of having a function that you call to get the next element, you have an object with a .next() method. _(javascriptallonge.pdf (source-range-83ecb080-02400))_
- When working with objects, we do things the object way. _(javascriptallonge.pdf (source-range-83ecb080-02410))_
- But having started by building functional iterators, we understand what is happening underneath the object’s scaffolding. _(javascriptallonge.pdf (source-range-83ecb080-02410))_
- Now our .iterator() method is returning an iterator object. _(javascriptallonge.pdf (source-range-83ecb080-02410))_

> **const** stack = Stack2();
_(source: javascriptallonge.pdf (source-range-83ecb080-02404))_

> **const** collectionSum = (collection) => { **const** iterator = collection.iterator();
_(source: javascriptallonge.pdf (source-range-83ecb080-02406))_

> **let** eachIteration, sum = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02407))_

> **while** ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }
_(source: javascriptallonge.pdf (source-range-83ecb080-02408))_

> collectionSum(stack) _//=> 2015_
_(source: javascriptallonge.pdf (source-range-83ecb080-02409))_

### **iterables**

- Since there was no particular standard way to do it, people used all sorts of methods, and their methods returned all sorts of things: Objects with various interfaces, functional iterators, you name it. _(javascriptallonge.pdf (source-range-83ecb080-02412))_
- People have been writing iterators since JavaScript was first released in the late 1990s. _(javascriptallonge.pdf (source-range-83ecb080-02412))_
- So, when a standard way to write iterators was added to the JavaScript language, it didn’t make sense to use a method like .iterator() for it: That would conflict with existing code. _(javascriptallonge.pdf (source-range-83ecb080-02413))_
- Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator. _(javascriptallonge.pdf (source-range-83ecb080-02413))_
- Symbols are unique constants that are guaranteed not to conflict with existing strings. _(javascriptallonge.pdf (source-range-83ecb080-02414))_
- Symbols are a longstanding technique in programming going back to Lisp, where the GENSYM function generated… You guessed it… Symbols.[88] _(javascriptallonge.pdf (source-range-83ecb080-02414))_
- To ensure that the method would not conflict with any existing code, JavaScript provides a _symbol_ . _(javascriptallonge.pdf (source-range-83ecb080-02414))_
- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-83ecb080-02415))_
- > 88 You can read more about JavaScript symbols in Axel Rauschmayer’s Symbols in ECMAScript 2015. _(javascriptallonge.pdf (source-range-83ecb080-02416))_
- Our stack does, so instead of binding the existing iterator method to the name iterator, we bind it to the Symbol.iterator. _(javascriptallonge.pdf (source-range-83ecb080-02419))_
- The for...of loop works directly with any object that is _iterable_ , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. _(javascriptallonge.pdf (source-range-83ecb080-02431))_
- And there’s one more thing: You recall that the spread operator (...) can spread the elements of an array in an array literal or as parameters in a function invocation. _(javascriptallonge.pdf (source-range-83ecb080-02437))_
- Now is the time to note that we can spread any iterable. _(javascriptallonge.pdf (source-range-83ecb080-02438))_
- For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-83ecb080-02444))_
- That might be very wasteful for extremely large collections. _(javascriptallonge.pdf (source-range-83ecb080-02444))_
- For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-83ecb080-02444))_
- And if we have an infinite collection, spreading is going to fail outright as we’re about to see. _(javascriptallonge.pdf (source-range-83ecb080-02445))_

> **const** collectionSum = (collection) => { **const** iterator = collection[Symbol.iterator]();
_(source: javascriptallonge.pdf (source-range-83ecb080-02424))_

> **let** eachIteration, sum = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02425))_

> **while** ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum } collectionSum(stack) _//=> 2015_
_(source: javascriptallonge.pdf (source-range-83ecb080-02426))_

> Context: Indeed we do. Behold the for...of loop:
_(context: javascriptallonge.pdf (source-range-83ecb080-02428))_

> **const** iterableSum = (iterable) => { **let** sum = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02429))_

> Context: Now is the time to note that we can spread any iterable. So we can spread the elements of an iterable into an array literal:
_(context: javascriptallonge.pdf (source-range-83ecb080-02438))_

> - ['some squares', ...someSquares] _//=> ["some squares", 1, 4, 9, 16, 25]_
_(source: javascriptallonge.pdf (source-range-83ecb080-02439))_

> Context: And we can also spread the elements of an array literal into parameters:
_(context: javascriptallonge.pdf (source-range-83ecb080-02440))_

> **const** firstAndSecondElement = (first, second) => ({first, second})
_(source: javascriptallonge.pdf (source-range-83ecb080-02441))_

> Context: And we can also spread the elements of an array literal into parameters:
_(context: javascriptallonge.pdf (source-range-83ecb080-02440))_

> firstAndSecondElement(...stack) _//=> {"first":5,"second":10}_
_(source: javascriptallonge.pdf (source-range-83ecb080-02442))_

### **iterables out to infinity**

- There are useful things we can do with iterables representing an infinitely large collection. _(javascriptallonge.pdf (source-range-83ecb080-02449))_
- Attempting to spread an infinite iterable into an array is always going to fail. _(javascriptallonge.pdf (source-range-83ecb080-02455))_

> Context: Iterables needn’t represent finite collections:
_(context: javascriptallonge.pdf (source-range-83ecb080-02447))_

> **const** Numbers = { [Symbol.iterator] () { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } }
_(source: javascriptallonge.pdf (source-range-83ecb080-02448))_

> Context: There are useful things we can do with iterables representing an infinitely large collection. But let’s point out what we can’t do with them:
_(context: javascriptallonge.pdf (source-range-83ecb080-02449))_

> ['all the numbers', ...Numbers] _//=> infinite loop!_
_(source: javascriptallonge.pdf (source-range-83ecb080-02452))_

### **ordered collections**

- The iterables we’re discussing represent _ordered collections_ . _(javascriptallonge.pdf (source-range-83ecb080-02457))_
- One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. _(javascriptallonge.pdf (source-range-83ecb080-02457))_
- Iterables needn’t represent ordered collections. _(javascriptallonge.pdf (source-range-83ecb080-02461))_
- This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator], and ensuring that our iterators start at the beginning and work forward. _(javascriptallonge.pdf (source-range-83ecb080-02461))_
- Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. _(javascriptallonge.pdf (source-range-83ecb080-02466))_
- Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-83ecb080-02466))_
- Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-83ecb080-02466))_
- To reiterate (hah), an ordered collection represents a (possibly infinite) collection of elements that are in some order. _(javascriptallonge.pdf (source-range-83ecb080-02467))_
- Every time we get an iterator from an ordered collection, we start iterating from the beginning. _(javascriptallonge.pdf (source-range-83ecb080-02467))_
- Right now, we’re just looking at ordered collections. _(javascriptallonge.pdf (source-range-83ecb080-02467))_

> Context: The iterables we’re discussing represent _ordered collections_ . One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. For example:
_(context: javascriptallonge.pdf (source-range-83ecb080-02457))_

> **const** abc = ["a", "b", "c"];
_(source: javascriptallonge.pdf (source-range-83ecb080-02458))_

### **operations on ordered collections**

- Here’s mapWith, it takes an ordered collection, and returns another ordered collection representing a mapping over the original:[89] _(javascriptallonge.pdf (source-range-83ecb080-02469))_
- Let’s define some operations on ordered collections. _(javascriptallonge.pdf (source-range-83ecb080-02469))_
- > 89Yes, we also used the name mapWith for working with ordinary collections elsewhere. _(javascriptallonge.pdf (source-range-83ecb080-02470))_
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. _(javascriptallonge.pdf (source-range-83ecb080-02470))_
- But for the purposes of discussing ideas, we can use the same name twice in two different contexts. _(javascriptallonge.pdf (source-range-83ecb080-02470))_
- It’s the same idea, after all. _(javascriptallonge.pdf (source-range-83ecb080-02470))_
- This illustrates the general pattern of working with ordered collections: We make them _iterables_ , meaning that they have a [Symbol.iterator] method, that returns an _iterator_ . _(javascriptallonge.pdf (source-range-83ecb080-02474))_
- An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order. _(javascriptallonge.pdf (source-range-83ecb080-02474))_
- Many operations on ordered collections return another ordered collection. _(javascriptallonge.pdf (source-range-83ecb080-02475))_
- They do so by taking care to iterate over a result freshly every time we get an iterator for them. _(javascriptallonge.pdf (source-range-83ecb080-02475))_
- Numbers is an ordered collection. _(javascriptallonge.pdf (source-range-83ecb080-02480))_
- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. _(javascriptallonge.pdf (source-range-83ecb080-02483))_
- Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. _(javascriptallonge.pdf (source-range-83ecb080-02483))_
- Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. _(javascriptallonge.pdf (source-range-83ecb080-02483))_
- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. _(javascriptallonge.pdf (source-range-83ecb080-02483))_
- Like mapWith, they preserve the ordered collection semantics of whatever you give them. _(javascriptallonge.pdf (source-range-83ecb080-02496))_
- And here’s a computation performed using operations on ordered collections: We’ll create an ordered collection of square numbers that end in one and are less than 1,000: _(javascriptallonge.pdf (source-range-83ecb080-02497))_
- As we expect from an ordered collection, each time we iterate over UpTo1000, we begin at the beginning. _(javascriptallonge.pdf (source-range-83ecb080-02500))_
- For completeness, here are two more handy iterable functions. _(javascriptallonge.pdf (source-range-83ecb080-02501))_
- first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. _(javascriptallonge.pdf (source-range-83ecb080-02501))_
- like our other operations, rest preserves the ordered collection semantics of its argument. _(javascriptallonge.pdf (source-range-83ecb080-02503))_

> Context: Many operations on ordered collections return another ordered collection. They do so by taking care to iterate over a result freshly every time we get an iterator for them. Consider this example for mapWith:
_(context: javascriptallonge.pdf (source-range-83ecb080-02475))_

> **const** Evens = mapWith((x) => 2 * x, Numbers);
_(source: javascriptallonge.pdf (source-range-83ecb080-02476))_

> Context: Mind you, we can also map non-collection iterables, like RandomNumbers:
_(context: javascriptallonge.pdf (source-range-83ecb080-02484))_

> **const** ZeroesToNines = mapWith((n) => Math.floor(10 * limit), RandomNumbers);
_(source: javascriptallonge.pdf (source-range-83ecb080-02485))_

> mapWith can get a new iterator from RandomNumbers each time we iterate over ZeroesToNines, but if RandomNumbers doesn’t behave like an ordered collection, that’s not mapWith’s fault.
_(source: javascriptallonge.pdf (source-range-83ecb080-02491))_

> Context: And here’s a computation performed using operations on ordered collections: We’ll create an ordered collection of square numbers that end in one and are less than 1,000:
_(context: javascriptallonge.pdf (source-range-83ecb080-02497))_

> [...UpTo1000] _//=>_ [1,81,121,361,441,841,961] [...UpTo1000] _//=>_ [1,81,121,361,441,841,961]
_(source: javascriptallonge.pdf (source-range-83ecb080-02499))_

> Context: For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest]:
_(context: javascriptallonge.pdf (source-range-83ecb080-02501))_

> **const** first = (iterable) => iterable[Symbol.iterator]().next().value; **const** rest = (iterable) => ({ [Symbol.iterator] () { **const** iterator = iterable[Symbol.iterator](); iterator.next(); **return** iterator; } });
_(source: javascriptallonge.pdf (source-range-83ecb080-02502))_

### **from**

- No, of course not, we can do anything we like with them. _(javascriptallonge.pdf (source-range-83ecb080-02505))_
- One useful thing is to write a .from function that gathers an iterable into a particular collection type. _(javascriptallonge.pdf (source-range-83ecb080-02508))_
- And we can assign properties to functions with a . _(javascriptallonge.pdf (source-range-83ecb080-02510))_
- We can do the same with our own collections. _(javascriptallonge.pdf (source-range-83ecb080-02510))_
- And if we assign a function to a property, we’ve created a method. _(javascriptallonge.pdf (source-range-83ecb080-02510))_
- As you recall, functions are mutable objects. _(javascriptallonge.pdf (source-range-83ecb080-02510))_
- Now we can go “end to end,” If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that: _(javascriptallonge.pdf (source-range-83ecb080-02516))_

> Context: One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript’s built-in Array class already has one:
_(context: javascriptallonge.pdf (source-range-83ecb080-02508))_

> Array.from(UpTo1000) _//=> [1,81,121,361,441,841,961]_
_(source: javascriptallonge.pdf (source-range-83ecb080-02509))_

> Stack3.from = **function** (iterable) { **const** stack = **this** ();
_(source: javascriptallonge.pdf (source-range-83ecb080-02512))_

> Pair1.from = (iterable) => ( **function** iterationToList (iteration) { **const** {done, value} = iteration.next();
_(source: javascriptallonge.pdf (source-range-83ecb080-02514))_

> Context: Now we can go “end to end,” If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that:
_(context: javascriptallonge.pdf (source-range-83ecb080-02516))_

> **const** numberList = Pair1.from(untilWith((x) => x > 10, Numbers));
_(source: javascriptallonge.pdf (source-range-83ecb080-02517))_

> Context: Now we can go “end to end,” If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that:
_(context: javascriptallonge.pdf (source-range-83ecb080-02516))_

> Pair1.from(Squares) _//=> {"first":0,_ "rest":{"first":1, "rest":{"first":4, "rest":{ ...
_(source: javascriptallonge.pdf (source-range-83ecb080-02518))_

### **summary**

- _Iterable_ ordered collections can be iterated over or gathered into another collection. _(javascriptallonge.pdf (source-range-83ecb080-02522))_
- Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection from what we want to do with the elements of a collection. _(javascriptallonge.pdf (source-range-83ecb080-02522))_
- Separating concerns with iterators speaks to JavaScript’s fundamental nature: It’s a language that _wants_ to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-83ecb080-02523))_

## Generating Iterables

### **Generating Iterables**

- Iterables look cool, but then again, everything looks amazing when you’re given cherry-picked examples. _(javascriptallonge.pdf (source-range-83ecb080-02530))_
- Iterables look cool, but then again, everything looks amazing when you’re given cherry-picked examples. _(javascriptallonge.pdf (source-range-83ecb080-02530))_
- Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done. _(javascriptallonge.pdf (source-range-83ecb080-02531))_
- This seems blindingly obvious and simple. _(javascriptallonge.pdf (source-range-83ecb080-02532))_
- The Numbers iterable returns an object that updates a mutable variable, n, to deliver number after number. _(javascriptallonge.pdf (source-range-83ecb080-02536))_
- There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers. _(javascriptallonge.pdf (source-range-83ecb080-02537))_
- Then it waits for the next request. _(javascriptallonge.pdf (source-range-83ecb080-02537))_
- It waits until given a request, and then it returns exactly one item. _(javascriptallonge.pdf (source-range-83ecb080-02537))_
- Of course, when we have some code that makes a bunch of something, we don’t usually write it like that. _(javascriptallonge.pdf (source-range-83ecb080-02538))_
- We would _generate_ numbers. _(javascriptallonge.pdf (source-range-83ecb080-02541))_
- And magically, the numbers would pour forth. _(javascriptallonge.pdf (source-range-83ecb080-02541))_
- Well, there are some collections that are much easier to generate than to iterate over. _(javascriptallonge.pdf (source-range-83ecb080-02545))_

> Context: Let’s consider how they work. Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done.
_(context: javascriptallonge.pdf (source-range-83ecb080-02531))_

> Iterators have to arrange its own state such that when you call them, they compute and return the next item.
_(source: javascriptallonge.pdf (source-range-83ecb080-02532))_

> Context: Of course, when we have some code that makes a bunch of something, we don’t usually write it like that. We usually just write something like:
_(context: javascriptallonge.pdf (source-range-83ecb080-02538))_

> **let** n = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02539))_

### **recursive iterators**

- Iterators maintain state, that’s what they do. _(javascriptallonge.pdf (source-range-83ecb080-02547))_
- Generators have to manage the exact same amount of state, but sometimes, it’s much easier to manage that state in a generator. _(javascriptallonge.pdf (source-range-83ecb080-02547))_
- Given an array that might contain arrays, let’s say we want to generate all the “leaf” elements, i.e. _(javascriptallonge.pdf (source-range-83ecb080-02548))_
- elements that are not, themselves, iterable. _(javascriptallonge.pdf (source-range-83ecb080-02548))_
- For example, iterating over a tree. _(javascriptallonge.pdf (source-range-83ecb080-02548))_
- If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next, we’re left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. _(javascriptallonge.pdf (source-range-83ecb080-02555))_
- In essence, both the generation and iteration implementations have stacks, but the generation version’s stack is _implicit_ , while the iteration version’s stack is _explicit_ . _(javascriptallonge.pdf (source-range-83ecb080-02555))_
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We’re reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. _(javascriptallonge.pdf (source-range-83ecb080-02558))_
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We’re reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. _(javascriptallonge.pdf (source-range-83ecb080-02558))_

> Context: They’re of approximately equal complexity. So why bring up generation? Well, there are some collections that are much easier to generate than to iterate over. Let’s look at one:
_(context: javascriptallonge.pdf (source-range-83ecb080-02545))_

> One of those cases is when we have to recursively enumerate something.
_(source: javascriptallonge.pdf (source-range-83ecb080-02547))_

> Context: For example, iterating over a tree. Given an array that might contain arrays, let’s say we want to generate all the “leaf” elements, i.e. elements that are not, themselves, iterable.
_(context: javascriptallonge.pdf (source-range-83ecb080-02548))_

> _// Generation_ **const** isIterable = (something) => !!something[Symbol.iterator];
_(source: javascriptallonge.pdf (source-range-83ecb080-02549))_

### **state machines**

- Some iterables can be modelled as state machines. _(javascriptallonge.pdf (source-range-83ecb080-02560))_
- - The first element of the fibonacci sequence is zero. _(javascriptallonge.pdf (source-range-83ecb080-02561))_
- - The second element of the fibonacci sequence is one. _(javascriptallonge.pdf (source-range-83ecb080-02562))_
- - Every subsequent element of the fibonacci sequence is the sum of the previous two elements. _(javascriptallonge.pdf (source-range-83ecb080-02563))_
- This isn’t a good fit for an iterator, because iterators have one functional entry point and therefore, we’d have to represent our three states explicitly, perhaps using a state pattern[90] : _(javascriptallonge.pdf (source-range-83ecb080-02579))_
- The thing to note here is that our fibonacci generator has three states: generating 0, generating 1, and generating everything after that. _(javascriptallonge.pdf (source-range-83ecb080-02579))_
- The thing to note here is that our fibonacci generator has three states: generating 0, generating 1, and generating everything after that. _(javascriptallonge.pdf (source-range-83ecb080-02579))_
- This isn’t a good fit for an iterator, because iterators have one functional entry point and therefore, we’d have to represent our three states explicitly, perhaps using a state pattern[90] : _(javascriptallonge.pdf (source-range-83ecb080-02579))_
- In a generator, we write “do this, then this, then this.” In an iterator, we have to wrap that up and explicitly keep track of what step we’re on. _(javascriptallonge.pdf (source-range-83ecb080-02587))_
- Again, this is not particularly horrendous, but like the recursive example, we’re explicitly greenspunning the natural linear state. _(javascriptallonge.pdf (source-range-83ecb080-02587))_
- In a generator, we write “do this, then this, then this.” In an iterator, we have to wrap that up and explicitly keep track of what step we’re on. _(javascriptallonge.pdf (source-range-83ecb080-02587))_
- So we see the same thing: The generation version has state, but it’s implicit in JavaScript’s linear control flow. _(javascriptallonge.pdf (source-range-83ecb080-02588))_

> Context: Let’s write a generator:
_(context: javascriptallonge.pdf (source-range-83ecb080-02564))_

> **const** fibonacci = () => { **let** a, b;
_(source: javascriptallonge.pdf (source-range-83ecb080-02566))_

> Context: Let’s write a generator:
_(context: javascriptallonge.pdf (source-range-83ecb080-02564))_

> console.log(a = 0);
_(source: javascriptallonge.pdf (source-range-83ecb080-02567))_

> console.log(b = 1);
_(source: javascriptallonge.pdf (source-range-83ecb080-02568))_

> **while** ( **true** ) { [a, b] = [b, a + b]; console.log(b); }
_(source: javascriptallonge.pdf (source-range-83ecb080-02569))_

> Whereas the iteration version must make that state explicit.
_(source: javascriptallonge.pdf (source-range-83ecb080-02588))_

### **javascript’s generators**

- It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator. _(javascriptallonge.pdf (source-range-83ecb080-02590))_
- Given the title of this chapter, it is not a surprise that JavaScript makes this possible. _(javascriptallonge.pdf (source-range-83ecb080-02590))_
- An iterator written in a generation style is called a _generator_ . _(javascriptallonge.pdf (source-range-83ecb080-02591))_
- We can write an iterator, but use a generation style of programming. _(javascriptallonge.pdf (source-range-83ecb080-02591))_
- An iterator written in a generation style is called a _generator_ . _(javascriptallonge.pdf (source-range-83ecb080-02591))_
- This makes sense, because empty never yields anything. _(javascriptallonge.pdf (source-range-83ecb080-02598))_
- This makes sense, because empty never yields anything. _(javascriptallonge.pdf (source-range-83ecb080-02598))_
- Generator functions can take an argument. _(javascriptallonge.pdf (source-range-83ecb080-02599))_
- Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-83ecb080-02604))_
- Invoking only("you") returns an iterator that we can call with .next(), and it yields "you". _(javascriptallonge.pdf (source-range-83ecb080-02604))_
- Invoking only("you") returns an iterator that we can call with .next(), and it yields "you". _(javascriptallonge.pdf (source-range-83ecb080-02604))_
- Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-83ecb080-02604))_
- It yields the value of something, and then it’s done. _(javascriptallonge.pdf (source-range-83ecb080-02608))_

> Context: 2. We don’t return values or output them to console.log. We “yield” values using the yield keyword.
_(context: javascriptallonge.pdf (source-range-83ecb080-02593))_

> When we invoke the function, we get an iterator object back.
_(source: javascriptallonge.pdf (source-range-83ecb080-02594))_

> When we invoke empty, we get an iterator with no elements.
_(source: javascriptallonge.pdf (source-range-83ecb080-02598))_

> Context: Invoking only("you") returns an iterator that we can call with .next(), and it yields "you". Invoking only more than once gives us fresh iterators each time:
_(context: javascriptallonge.pdf (source-range-83ecb080-02604))_

> only("you").next() _//=>_ {"done": **false** , value: "you"} only("the lonely").next() _//=>_ {"done": **false** , value: "the lonely"}
_(source: javascriptallonge.pdf (source-range-83ecb080-02605))_

> Context: We can invoke the same iterator twice:
_(context: javascriptallonge.pdf (source-range-83ecb080-02606))_

> **const** sixteen = only("sixteen"); sixteen.next() _//=>_ {"done": **false** , value: "sixteen"} sixteen.next() _//=>_ {"done": **true** }
_(source: javascriptallonge.pdf (source-range-83ecb080-02607))_

### **generators are coroutines**

- This is where generators behave very, very differently from ordinary functions. _(javascriptallonge.pdf (source-range-83ecb080-02617))_
- The iterator is in a nascent or “newborn” state. _(javascriptallonge.pdf (source-range-83ecb080-02619))_
- When we call interator.next(), the body of our generator begins to be evaluated. _(javascriptallonge.pdf (source-range-83ecb080-02620))_
- - The rest of the program continues along its way until it makes another call to iterator.next(). _(javascriptallonge.pdf (source-range-83ecb080-02626))_
- - The iterator _resumes execution_ from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-83ecb080-02627))_
- - The rest of the program continues along its way until it makes another call to iterator.next(). _(javascriptallonge.pdf (source-range-83ecb080-02631))_
- - The iterator _resumes execution_ from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-83ecb080-02632))_
- - The rest of the program continues along its way until it makes another call to iterator.next(). _(javascriptallonge.pdf (source-range-83ecb080-02636))_
- - The iterator _resumes execution_ from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-83ecb080-02637))_
- There are no more lines of code, so it ends. _(javascriptallonge.pdf (source-range-83ecb080-02638))_
- The body of our generator runs until it returns, ends, or encounters the next yield statement. _(javascriptallonge.pdf (source-range-83ecb080-02638))_
- This behaviour is not unique to JavaScript, generators are called coroutines[92] in other languages: _(javascriptallonge.pdf (source-range-83ecb080-02640))_
- Coroutines are computer program components that generalize subroutines for nonpreemptive multitasking, by allowing multiple entry points for suspending and resuming execution at certain locations. _(javascriptallonge.pdf (source-range-83ecb080-02641))_
- Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes. _(javascriptallonge.pdf (source-range-83ecb080-02641))_
- Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes. _(javascriptallonge.pdf (source-range-83ecb080-02641))_
- With an iterator, we can call them the _producer_ and the _consumer_ . _(javascriptallonge.pdf (source-range-83ecb080-02642))_
- The iterator is the producer, and the code that iterates over it is the consumer. _(javascriptallonge.pdf (source-range-83ecb080-02642))_
- For example, a “transpiler” might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we’ll see that later): _(javascriptallonge.pdf (source-range-83ecb080-02647))_
- Of course, generators need not be implemented exactly as coroutines. _(javascriptallonge.pdf (source-range-83ecb080-02647))_
- For example, a “transpiler” might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we’ll see that later): _(javascriptallonge.pdf (source-range-83ecb080-02647))_
- But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next(), it runs until it returns, ends, or yields. _(javascriptallonge.pdf (source-range-83ecb080-02649))_
- If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-83ecb080-02649))_
- If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-83ecb080-02649))_

> Context: Here’s a generator that yields three numbers:
_(context: javascriptallonge.pdf (source-range-83ecb080-02610))_

> **const** oneTwoThree = **function** * () { **yield** 1; **yield** 2; **yield** 3; };
_(source: javascriptallonge.pdf (source-range-83ecb080-02613))_

> oneTwoThree().next() _//=>_ {"done": **false** , value: 1} oneTwoThree().next() _//=>_ {"done": **false** , value: 1} oneTwoThree().next() _//=>_ {"done": **false** , value: 1}
_(source: javascriptallonge.pdf (source-range-83ecb080-02614))_

> **const** iterator = oneTwoThree();
_(source: javascriptallonge.pdf (source-range-83ecb080-02615))_

### **generators and iterables**

- Our generator function oneTwoThree is not an iterator. _(javascriptallonge.pdf (source-range-83ecb080-02651))_
- As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3. _(javascriptallonge.pdf (source-range-83ecb080-02652))_
- Recalling the way we wrote ordered collections, we could make a collection that uses a generator function: _(javascriptallonge.pdf (source-range-83ecb080-02652))_
- This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing _(javascriptallonge.pdf (source-range-83ecb080-02659))_
- This object declares a [Symbol.iterator] function that makes it iterable. _(javascriptallonge.pdf (source-range-83ecb080-02664))_
- Because it’s declared *[Symbol.iterator], it’s a generator instead of an iterator. _(javascriptallonge.pdf (source-range-83ecb080-02664))_
- Because it’s declared *[Symbol.iterator], it’s a generator instead of an iterator. _(javascriptallonge.pdf (source-range-83ecb080-02664))_
- So to summarize, ThreeNumbers is an object that we’ve made iterable, by way of writing a _generator_ method for [Symbol.iterator]. _(javascriptallonge.pdf (source-range-83ecb080-02665))_

> Context: Our generator function oneTwoThree is not an iterator. It’s a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call.
_(context: javascriptallonge.pdf (source-range-83ecb080-02651))_

> If we call our generator function more than once, we get new iterators.
_(source: javascriptallonge.pdf (source-range-83ecb080-02652))_

> Context: Now we can use it in a for...of loop, spread it into an array literal, or spread it into a function invocation, because we have written an iterable that uses a generator to return an iterator from its [Symbol.iterator] method.
_(context: javascriptallonge.pdf (source-range-83ecb080-02658))_

> **const** iterator = ThreeNumbers[Symbol.iterator]();
_(source: javascriptallonge.pdf (source-range-83ecb080-02656))_

> Context: generator methods for objects: This object declares a [Symbol.iterator] function that makes it iterable. Because it’s declared *[Symbol.iterator], it’s a generator instead of an iterator.
_(context: javascriptallonge.pdf (source-range-83ecb080-02662, source-range-83ecb080-02664))_

> **const** ThreeNumbers = { *[Symbol.iterator] () { **yield** 1; **yield** 2; **yield** 3 } }
_(source: javascriptallonge.pdf (source-range-83ecb080-02663))_

### **more generators**

- Our OneTwoThree example used implicit state to output the numbers in sequence. _(javascriptallonge.pdf (source-range-83ecb080-02672))_
- We’ve writing a function that returns an iterator, but we used a generator to do it. _(javascriptallonge.pdf (source-range-83ecb080-02681))_
- And the generator’s syntax allows us to use JavaScript’s natural management of state instead of constantly rolling our own. _(javascriptallonge.pdf (source-range-83ecb080-02681))_

### **yielding iterables**

- It works, but as we’ve just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object:[93] _(javascriptallonge.pdf (source-range-83ecb080-02689))_
- > 93There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-83ecb080-02690))_
- > 93There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-83ecb080-02690))_
- If e is not an iterable, yield e. _(javascriptallonge.pdf (source-range-83ecb080-02694))_
- We take advantage of the for...of loop in a plain and direct way: For each element e, if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. _(javascriptallonge.pdf (source-range-83ecb080-02694))_
- This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping. _(javascriptallonge.pdf (source-range-83ecb080-02695))_
- These three lines say, in essence, “yield all the elements of TreeIterable(e), in order.” This comes up quite often when we have collections that are compounds, collections made from other collections. _(javascriptallonge.pdf (source-range-83ecb080-02698))_
- Tucked inside of it is the same three-line idiom for yielding each element of an iterable. _(javascriptallonge.pdf (source-range-83ecb080-02704))_
- yield* is handy when writing generator functions that operate on or create iterables. _(javascriptallonge.pdf (source-range-83ecb080-02711))_

> But if you can write it as a simple generator, write it as a simple generator.
_(source: javascriptallonge.pdf (source-range-83ecb080-02690))_

### **rewriting iterable operations**

- Now that we know about iterables, we can rewrite our iterable operations as generators. _(javascriptallonge.pdf (source-range-83ecb080-02713))_
- No need to explicitly construct an object that has a [Symbol.iterator] method. _(javascriptallonge.pdf (source-range-83ecb080-02719))_
- No need to return an object with a .next() method. _(javascriptallonge.pdf (source-range-83ecb080-02719))_
- We can do the same thing with our other operations like filterWith and untilWith. _(javascriptallonge.pdf (source-range-83ecb080-02720))_
- first works directly with iterators and remains unchanged, but rest can be rewritten as a generator: _(javascriptallonge.pdf (source-range-83ecb080-02726))_

> Context: first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:
_(context: javascriptallonge.pdf (source-range-83ecb080-02726))_

> **const** first = (iterable) => iterable[Symbol.iterator]().next().value;
_(source: javascriptallonge.pdf (source-range-83ecb080-02727))_

> Context: first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:
_(context: javascriptallonge.pdf (source-range-83ecb080-02726))_

> **function** * rest (iterable) { **const** iterator = iterable[Symbol.iterator]();
_(source: javascriptallonge.pdf (source-range-83ecb080-02728))_

### **Summary**

- Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns. _(javascriptallonge.pdf (source-range-83ecb080-02731))_
- And we don’t need to worry about wrapping our values in an object with .done and .value properties. _(javascriptallonge.pdf (source-range-83ecb080-02731))_
- This is especially useful for making iterables. _(javascriptallonge.pdf (source-range-83ecb080-02732))_

## Lazy and Eager Collections

### **Lazy and Eager Collections**

- The operations on iterables are tremendously valuable, but let’s reiterate why we care: In JavaScript, we build single-responsibility objects, and single-responsibility functions, and we compose these together to build more full-featured objects and algorithms. _(javascriptallonge.pdf (source-range-83ecb080-02737))_
- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack _(javascriptallonge.pdf (source-range-83ecb080-02738))_
- If we wanted to flatten collections to arrays, we wrote a .toArray method for each type of collection. _(javascriptallonge.pdf (source-range-83ecb080-02739))_
- in the older style of object-oriented programming, we built “fat” objects. _(javascriptallonge.pdf (source-range-83ecb080-02739))_
- Each collection knew how to map itself (.map), how to fold itself (.reduce), how to filter itself (.filter) and how to find one element within itself (.find). _(javascriptallonge.pdf (source-range-83ecb080-02739))_
- We tell ourselves that, well, a collection ought to know how to map itself. _(javascriptallonge.pdf (source-range-83ecb080-02740))_
- Some methods are only added to a few collections, some are added to all. _(javascriptallonge.pdf (source-range-83ecb080-02740))_
- Some methods are only added to a few collections, some are added to all. _(javascriptallonge.pdf (source-range-83ecb080-02740))_
- Each one has its own variation, but the overall form is identical. _(javascriptallonge.pdf (source-range-83ecb080-02741))_
- That’s a sign that we should work at a higher level of abstraction, and working with iterables is that higher level of abstraction. _(javascriptallonge.pdf (source-range-83ecb080-02741))_
- But we end up recreating the same bits of code in each .map method we create, in each .reduce method we create, in each .filter method we create, and in each .find method. _(javascriptallonge.pdf (source-range-83ecb080-02741))_
- That would be like saying that when we ask a bank teller for some cash, they personally print every bank note. _(javascriptallonge.pdf (source-range-83ecb080-02742))_
- This “fat object” style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don’t need for the collection to handle every single detail. _(javascriptallonge.pdf (source-range-83ecb080-02742))_

### **implementing methods with iteration**

- Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. _(javascriptallonge.pdf (source-range-83ecb080-02744))_
- And they should know how to accomplish the desired result, but they should do so by delegating as much of the work as possible to operations like mapWith. _(javascriptallonge.pdf (source-range-83ecb080-02744))_
- And if we want to create convenience methods, we can reuse common pieces. _(javascriptallonge.pdf (source-range-83ecb080-02745))_
- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack. _(javascriptallonge.pdf (source-range-83ecb080-02745))_
- To use LazyCollection, we mix it into an any iterable object. _(javascriptallonge.pdf (source-range-83ecb080-02759))_
- For simplicity, we’ll show how to mix it into Numbers and Pair. _(javascriptallonge.pdf (source-range-83ecb080-02759))_
- **return this** .array[ **this** .index += 1] = value; }, pop: **function** () { **const** value = **this** .array[ **this** .index]; **this** .array[ **this** .index] = **undefined** ; **if** ( **this** .index >= 0) { **this** .index -= 1 } **return** value }, isEmpty: **function** () { **return this** .index < 0 }, [Symbol.iterator]: **function** () { **let** iterationIndex = **this** .index; **return** { next: () => { **if** (iterationIndex > **this** .index) { iterationIndex = **this** .index; } **if** (iterationIndex < 0) { **return** {done: **true** }; } **else** { **return** {done: **false** , value: **this** .array[iterationIndex--]} } } } } }, LazyCollection); Stack.from = **function** (iterable) { **const** stack = **this** (); **for** ( **let** element **of** iterable) { stack.push(element); } **return** stack; } _(javascriptallonge.pdf (source-range-83ecb080-02772))_
- _// Pair and Stack in action_ Stack.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .first() _//=> 100_ Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0) _(javascriptallonge.pdf (source-range-83ecb080-02775))_

> Context: _// Pair, a/k/a linked lists_
_(context: javascriptallonge.pdf (source-range-83ecb080-02761))_

> **const** EMPTY = { isEmpty: () => **true**
_(source: javascriptallonge.pdf (source-range-83ecb080-02762))_

> **const** isEmpty = (node) => node === EMPTY;
_(source: javascriptallonge.pdf (source-range-83ecb080-02766))_

> _// Stack_ **const** Stack = () => Object.assign({ array: [], index: -1, push: **function** (value) {
_(source: javascriptallonge.pdf (source-range-83ecb080-02769))_

### **lazy collection operations**

- Let’s be precise: _Laziness_ is the characteristic of not doing any work until you know you need the result of the work. _(javascriptallonge.pdf (source-range-83ecb080-02778))_
- “Laziness” is a very pejorative word when applied to people. _(javascriptallonge.pdf (source-range-83ecb080-02778))_
- But it can be an excellent strategy for efficiency in algorithms. _(javascriptallonge.pdf (source-range-83ecb080-02778))_
- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0) Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0) _(javascriptallonge.pdf (source-range-83ecb080-02780))_
- And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. _(javascriptallonge.pdf (source-range-83ecb080-02781))_
- And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. _(javascriptallonge.pdf (source-range-83ecb080-02781))_
- Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. _(javascriptallonge.pdf (source-range-83ecb080-02782))_
- Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. _(javascriptallonge.pdf (source-range-83ecb080-02782))_
- They produce small iterable objects that refer back to the original iteration. _(javascriptallonge.pdf (source-range-83ecb080-02783))_
- Whereas the .map and .filter methods on Pair work with iterators. _(javascriptallonge.pdf (source-range-83ecb080-02783))_
- This expression begins with a stack containing 30 elements. _(javascriptallonge.pdf (source-range-83ecb080-02788))_
- Same with .filter, we get an iterable that can iterate over the even squares, but not an actual stack or array. _(javascriptallonge.pdf (source-range-83ecb080-02788))_
- It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. _(javascriptallonge.pdf (source-range-83ecb080-02788))_
- Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack’s elements, and it only needs to square two of those elements, 29 and 28, to return the answer. _(javascriptallonge.pdf (source-range-83ecb080-02789))_
- Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack’s elements, and it only needs to square two of those elements, 29 and 28, to return the answer. _(javascriptallonge.pdf (source-range-83ecb080-02789))_
- Let’s make iterable numbers. _(javascriptallonge.pdf (source-range-83ecb080-02797))_
- If we mutate a collection after taking an iterable, we might get an unexpected result. _(javascriptallonge.pdf (source-range-83ecb080-02801))_
- This is why “pure” functional languages like Haskell combine lazy semantics with immutable collections, and why even “impure” languages like Clojure emphasize the use of immutable collections. _(javascriptallonge.pdf (source-range-83ecb080-02801))_
- If we mutate a collection after taking an iterable, we might get an unexpected result. _(javascriptallonge.pdf (source-range-83ecb080-02801))_

> Context: Both expressions evaluate to 220. And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript.
_(context: javascriptallonge.pdf (source-range-83ecb080-02781))_

> When working with very large collections and many operations, this can be important.
_(source: javascriptallonge.pdf (source-range-83ecb080-02783))_

> Context: Both expressions evaluate to 220. And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript.
_(context: javascriptallonge.pdf (source-range-83ecb080-02781))_

> The effect is even more pronounced when we use methods like first, until, or take:
_(source: javascriptallonge.pdf (source-range-83ecb080-02784))_

> Context: We can confirm this:
_(context: javascriptallonge.pdf (source-range-83ecb080-02790))_

> If we write the almost identical thing with an array, we get a different behaviour:
_(source: javascriptallonge.pdf (source-range-83ecb080-02792))_

### **eager collections**

- We can make an eager collection out of any collection that is _gatherable_ , meaning it has a .from method: _(javascriptallonge.pdf (source-range-83ecb080-02803))_
- Here is our Pair implementation. _(javascriptallonge.pdf (source-range-83ecb080-02813))_
- Pair is gatherable, because it implements .from(). _(javascriptallonge.pdf (source-range-83ecb080-02813))_
- We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs: _(javascriptallonge.pdf (source-range-83ecb080-02813))_
- Pair is gatherable, because it implements .from(). _(javascriptallonge.pdf (source-range-83ecb080-02813))_

## Interlude: The Carpenter Interviews for a Job

### **Interlude: The Carpenter Interviews for a Job**

- “The Carpenter” was a JavaScript programmer, well-known for a meticulous attention to detail and love for hand-crafted, exquisitely joined code. _(javascriptallonge.pdf (source-range-83ecb080-02825))_
- A few minutes later, he was joined by one of the company’s developers, Christine. _(javascriptallonge.pdf (source-range-83ecb080-02826))_

### **the problem**

- After some small talk, Christine explained that they liked to ask candidates to whiteboard some code. _(javascriptallonge.pdf (source-range-83ecb080-02828))_
- Despite his experience and industry longevity, the Carpenter did not mind being asked to demonstrate that he was, in fact, the person described on the resumé. _(javascriptallonge.pdf (source-range-83ecb080-02828))_
- After some small talk, Christine explained that they liked to ask candidates to whiteboard some code. _(javascriptallonge.pdf (source-range-83ecb080-02828))_
- Many companies use white-boarding code as an excuse to have a technical conversation with a candidate, and The Carpenter felt that being asked to whiteboard code was an excuse to have a technical conversation with a future colleague. _(javascriptallonge.pdf (source-range-83ecb080-02829))_
- Each move consists of moving the chequer one square in the direction of the arrow in the square it occupies. _(javascriptallonge.pdf (source-range-83ecb080-02835))_
- A chequer is placed randomly on the checkerboard. _(javascriptallonge.pdf (source-range-83ecb080-02835))_
- “↑, →, ↑, ↓, ↑, →…” Write an algorithm that will determine whether the game halts, strictly from the called out directions, in finite time and space. _(javascriptallonge.pdf (source-range-83ecb080-02836))_
- The problem is this: The game board is hidden from us. _(javascriptallonge.pdf (source-range-83ecb080-02836))_
- “To save time, we have written a template of the solution for you in ECMASCript 2015 notation. _(javascriptallonge.pdf (source-range-83ecb080-02838))_
- game-board’s size or contents, only that it is given an arrow every time though the while loop. _(javascriptallonge.pdf (source-range-83ecb080-02842))_
- game-board’s size or contents, only that it is given an arrow every time though the while loop. _(javascriptallonge.pdf (source-range-83ecb080-02842))_

> Context: Christine intoned the question, as if by rote:
_(context: javascriptallonge.pdf (source-range-83ecb080-02834))_

> If the arrow should cause the chequer to move off the edge of the board, the game halts.
_(source: javascriptallonge.pdf (source-range-83ecb080-02835))_

> You may use babeljs.io[95] , or ES6Fiddle[96] to check your work.
_(source: javascriptallonge.pdf (source-range-83ecb080-02842))_

> Context: Christine quickly scribbled on the whiteboard:
_(context: javascriptallonge.pdf (source-range-83ecb080-02843))_

> **const** Game = (size = 8) => {
_(source: javascriptallonge.pdf (source-range-83ecb080-02844))_

### **the carpenter’s solution**

- He then coached subsequent candidates to give polished answers to the company’s pet technical questions. _(javascriptallonge.pdf (source-range-83ecb080-02850))_
- The Carpenter was not surprised at the problem. _(javascriptallonge.pdf (source-range-83ecb080-02850))_
- He then coached subsequent candidates to give polished answers to the company’s pet technical questions. _(javascriptallonge.pdf (source-range-83ecb080-02850))_
- To save time, The Carpenter had prepared the same answer for both questions. _(javascriptallonge.pdf (source-range-83ecb080-02852))_
- Bob had, in fact, warned The Carpenter that “Thing” liked to ask either or both of two questions: Determine how to detect a loop in a linked list, and determine whether the chequerboard game would halt. _(javascriptallonge.pdf (source-range-83ecb080-02852))_
- The Carpenter coughed softly, then began. _(javascriptallonge.pdf (source-range-83ecb080-02853))_
- I’ll refactor a touch to make things clearer, for example I’ll extract the board to make it easier to test:” _(javascriptallonge.pdf (source-range-83ecb080-02853))_
- “To begin with, I’ll transform a game into an iterable that generates arrows, using the ‘Starman’ notation for generators. _(javascriptallonge.pdf (source-range-83ecb080-02853))_
- The Carpenter coughed softly, then began. _(javascriptallonge.pdf (source-range-83ecb080-02853))_
- I’ll refactor a touch to make things clearer, for example I’ll extract the board to make it easier to test:” _(javascriptallonge.pdf (source-range-83ecb080-02853))_
- A statefulMap is a lazy map that preserves state from iteration to iteration. _(javascriptallonge.pdf (source-range-83ecb080-02862))_
- “Now that we have an iterable, we can transform the iterable of arrows into an iterable of positions.” The Carpenter sketched quickly. _(javascriptallonge.pdf (source-range-83ecb080-02862))_
- That’s what we need, because we need to know the current position to map each move to the next position.” _(javascriptallonge.pdf (source-range-83ecb080-02862))_
- That’s what we need, because we need to know the current position to map each move to the next position.” _(javascriptallonge.pdf (source-range-83ecb080-02862))_
- “This is a standard idiom we can obtain from libraries, we don’t reinvent the wheel. _(javascriptallonge.pdf (source-range-83ecb080-02863))_
- “Armed with this, it’s straightforward to map an iterable of directions to an iterable of strings representing positions:” _(javascriptallonge.pdf (source-range-83ecb080-02868))_
- “Having turned our game loop into an iterable, we can now see that our problem of whether the game terminates is isomorphic to the problem of detecting whether the positions given ever repeat themselves: If the chequer ever returns to a position it has previously visited, it will cycle endlessly.” _(javascriptallonge.pdf (source-range-83ecb080-02870))_
- Detecting whether the game terminates is equivalent to detecting whether the graph contains a cycle.” _(javascriptallonge.pdf (source-range-83ecb080-02871))_
- “We could draw positions as nodes in a graph, connected by arcs representing the arrows. _(javascriptallonge.pdf (source-range-83ecb080-02871))_
- “There’s an old joke that a mathematician is someone who will take a five-minute problem, then spend an hour proving it is equivalent to another problem they have already solved. _(javascriptallonge.pdf (source-range-83ecb080-02876))_
- I approached this question in that spirit. _(javascriptallonge.pdf (source-range-83ecb080-02876))_
- “There’s an old joke that a mathematician is someone who will take a five-minute problem, then spend an hour proving it is equivalent to another problem they have already solved. _(javascriptallonge.pdf (source-range-83ecb080-02876))_
- The question was, _Given a linked list, detect whether it contains a cycle. _(javascriptallonge.pdf (source-range-83ecb080-02884))_
- I have never forgotten the question, or the general form of the solution. _(javascriptallonge.pdf (source-range-83ecb080-02884))_
- “This is, of course, the most common solution, it is Floyd’s cycle-finding algorithm[97] , although there is some academic dispute as to whether Robert Floyd actually discovered it or was misattributed by Knuth.” _(javascriptallonge.pdf (source-range-83ecb080-02885))_
- “This solution makes use of iterables and a single utility function, statefulMapWith. _(javascriptallonge.pdf (source-range-83ecb080-02892))_

> Context: The Carpenter coughed softly, then began. “To begin with, I’ll transform a game into an iterable that generates arrows, using the ‘Starman’ notation for generators. I’ll refactor a touch to make things clearer, for example I’ll extract the board to make it easier to test:”
_(context: javascriptallonge.pdf (source-range-83ecb080-02853))_

> **const** Board = (size = 8) => {
_(source: javascriptallonge.pdf (source-range-83ecb080-02855))_

> Context: “Now that we have an iterable, we can transform the iterable of arrows into an iterable of positions.” The Carpenter sketched quickly. “We want to take the arrows and convert them to positions. For that, we’ll map the Game iterable to positions. A statefulMap is a lazy map that preserves state from iteration to iteration. That’s what we need, because we need to know the current position to map each move to the next position.”
_(context: javascriptallonge.pdf (source-range-83ecb080-02862))_

> **const** Game = ({board, position}) => {
_(source: javascriptallonge.pdf (source-range-83ecb080-02860))_

> Context: “There’s an old joke that a mathematician is someone who will take a five-minute problem, then spend an hour proving it is equivalent to another problem they have already solved. I approached this question in that spirit. Now that we have created an iterable of values that can be compared with ===, I can show you this function:”
_(context: javascriptallonge.pdf (source-range-83ecb080-02876))_

> **const** tortoiseAndHare = (iterable) => { **const** hare = iterable[Symbol.iterator](); **let** hareResult = (hare.next(), hare.next());
_(source: javascriptallonge.pdf (source-range-83ecb080-02879))_

> hareResult = hare.next();
_(source: javascriptallonge.pdf (source-range-83ecb080-02881))_

> **const** terminates = (game) => tortoiseAndHare(positionsOf(game)) **const** test = [ ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿","￿","￿","￿"] ];
_(source: javascriptallonge.pdf (source-range-83ecb080-02890))_

### **the aftermath**

- This type of solution provided an excellent opportunity to explore lazy versus eager evaluation, the performance of iterators versus native iteration, single responsibility design, and many other rich topics. _(javascriptallonge.pdf (source-range-83ecb080-02894))_
- The Carpenter sat down and waited. _(javascriptallonge.pdf (source-range-83ecb080-02894))_
- The Carpenter was confident that although nobody would write this exact code in production, prospective employers would also recognize that nobody would try to detect whether a chequer game terminates in production, either. _(javascriptallonge.pdf (source-range-83ecb080-02895))_
- Christine looked at the solution on the board, frowned, and glanced at the clock on the wall. _(javascriptallonge.pdf (source-range-83ecb080-02896))_
- “We at the Thing Software company are very grateful you made some time to visit with us, but alas, that is all the time we have today. _(javascriptallonge.pdf (source-range-83ecb080-02897))_
- “I forgot about them, it’s been a while. _(javascriptallonge.pdf (source-range-83ecb080-02903))_

### **after another drink**

- A few drinks later, The Carpenter was telling his Thing story and an engineer named Kidu introduced themself. _(javascriptallonge.pdf (source-range-83ecb080-02907))_
- But I couldn’t help but notice that your solution doesn’t actually meet the stated requirements for a different reason:” _(javascriptallonge.pdf (source-range-83ecb080-02911))_
- I had a look at the code you left on the whiteboard. _(javascriptallonge.pdf (source-range-83ecb080-02911))_
- “I worked at Thing, and Christine told us about your solution. _(javascriptallonge.pdf (source-range-83ecb080-02911))_
- Whereas the problem as stated involves a single stream of directions. _(javascriptallonge.pdf (source-range-83ecb080-02912))_
- “The hasCycle function, a/k/a Tortoise and Hare, requires two separate iterators to do its job. _(javascriptallonge.pdf (source-range-83ecb080-02912))_
- Whereas the problem as stated involves a single stream of directions. _(javascriptallonge.pdf (source-range-83ecb080-02912))_
- “You know, the requirement asked for a finite space algorithm, not a constant state algorithm. _(javascriptallonge.pdf (source-range-83ecb080-02916))_
- The Carpenter stared at Kidu’s solution. _(javascriptallonge.pdf (source-range-83ecb080-02921))_
- “I guess,” he allowed, “It isn’t always necessary to make a solution so awesome it would please the Ghosts of Mars.” _(javascriptallonge.pdf (source-range-83ecb080-02921))_

> **const** hasCycle = (orderedCollection) => { **const** visited = **new** Set();
_(source: javascriptallonge.pdf (source-range-83ecb080-02919))_

## Interactive Generators

### **Interactive Generators**

- We saw how to use them for recursive unfolds and state machines. _(javascriptallonge.pdf (source-range-83ecb080-02926))_
- But there are other times we want to build functions that maintain implicit state. _(javascriptallonge.pdf (source-range-83ecb080-02926))_
- Let’s start by looking at a very simple example of a function that can be written statefully. _(javascriptallonge.pdf (source-range-83ecb080-02926))_
- We used generators to build iterators that maintain implicit state. _(javascriptallonge.pdf (source-range-83ecb080-02926))_
- The moves a player makes are a stream of values, just like the contents of an array can be consider a stream of values. _(javascriptallonge.pdf (source-range-83ecb080-02929))_
- But of course, iterating over a stream of moves requires us to wait for the game to be over so we know what moves were made. _(javascriptallonge.pdf (source-range-83ecb080-02929))_
- Consider, for example, the moves in a game. _(javascriptallonge.pdf (source-range-83ecb080-02929))_
- Let’s take a look at a very simple example, naughts and crosses[99] (We really ought to do something like Chess, but that might be a little out of scope for this chapter). _(javascriptallonge.pdf (source-range-83ecb080-02930))_
- The first player will always be o, and they will always place their chequer in the top-left corner, coincidentally numbered o: _(javascriptallonge.pdf (source-range-83ecb080-02931))_
- x has six possible moves, but they are really just two choices: 3 and anything else: _(javascriptallonge.pdf (source-range-83ecb080-02942))_

### **representing naughts and crosses as a stateless function**

- We could plays naughts and crosses as a stateless function. _(javascriptallonge.pdf (source-range-83ecb080-02952))_
- We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. _(javascriptallonge.pdf (source-range-83ecb080-02952))_
- We can encode the board in several different ways. _(javascriptallonge.pdf (source-range-83ecb080-02962))_
- We’ll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. _(javascriptallonge.pdf (source-range-83ecb080-02973))_
- We can use a POJO to make a map from positions to moves. _(javascriptallonge.pdf (source-range-83ecb080-02973))_

> Context: And if we want to look up what move to make, we can write:
_(context: javascriptallonge.pdf (source-range-83ecb080-02984))_

> 'o', 'x', ' ', ' ' ' ' ' ' , , , 'o', 'x', ' ' _//=> 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-02986))_

> 'o', 'x', ' ', ' ' ' ' ' ' , , , 'o', 'x', ' ' ]) _//=> 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-02992))_

### **representing naughts and crosses as a stateful function**

- In that case, we need a stateful function. _(javascriptallonge.pdf (source-range-83ecb080-02994))_
- The state is encoded entirely in data. _(javascriptallonge.pdf (source-range-83ecb080-03011))_
- Let’s recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. _(javascriptallonge.pdf (source-range-83ecb080-03011))_

> **const** aNaughtsAndCrossesGame = statefulNaughtsAndCrosses();
_(source: javascriptallonge.pdf (source-range-83ecb080-02996))_

> **const** aNaughtsAndCrossesGame = statefulNaughtsAndCrosses();
_(source: javascriptallonge.pdf (source-range-83ecb080-03005))_

### **this seems familiar**

- When we looked at generators, we saw that some iterators are inherently stateful, but sometimes it is awkward to represent them in a fully stateless fashion. _(javascriptallonge.pdf (source-range-83ecb080-03013))_
- Sometimes there is a state machine that is naturally represented implicitly in JavaScript’s control flow rather than explicitly in data. _(javascriptallonge.pdf (source-range-83ecb080-03013))_
- A game like this is absolutely a state machine, and we’ve explicitly coded those states into the lookup table. _(javascriptallonge.pdf (source-range-83ecb080-03014))_
- If we were in full control of the interaction, it would be easy to encode the game play as a decision tree instead of as a lookup table. _(javascriptallonge.pdf (source-range-83ecb080-03015))_
- But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree. _(javascriptallonge.pdf (source-range-83ecb080-03019))_
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn’t represent trees particularly well. _(javascriptallonge.pdf (source-range-83ecb080-03019))_
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn’t represent trees particularly well. _(javascriptallonge.pdf (source-range-83ecb080-03019))_
- Let’s see how it would actually work. _(javascriptallonge.pdf (source-range-83ecb080-03024))_
- But the first glance is deceptive, because we only see what we’ve seen so far. _(javascriptallonge.pdf (source-range-83ecb080-03024))_
- But the first glance is deceptive, because we only see what we’ve seen so far. _(javascriptallonge.pdf (source-range-83ecb080-03024))_

### **interactive generators**

- If we could do that, a generator function that played naughts and crosses would look like this: _(javascriptallonge.pdf (source-range-83ecb080-03026))_
- So far, we have called iterators (and generators) with .next(). _(javascriptallonge.pdf (source-range-83ecb080-03026))_
- Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn’t started yet. _(javascriptallonge.pdf (source-range-83ecb080-03033))_
- We can then get the first move by calling .next(). _(javascriptallonge.pdf (source-range-83ecb080-03033))_
- Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn’t started yet. _(javascriptallonge.pdf (source-range-83ecb080-03033))_
- We can then get the first move by calling .next(). _(javascriptallonge.pdf (source-range-83ecb080-03033))_
- It isn’t a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-83ecb080-03042))_
- But the generator function allows us to maintain state implicitly. _(javascriptallonge.pdf (source-range-83ecb080-03043))_
- And sometimes, we want to use implicit state instead of explicitly storing state in our data. _(javascriptallonge.pdf (source-range-83ecb080-03043))_

> Context: We can then get the first move by calling .next(). Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn’t started yet. If we wanted to pass some state to the generator before it begins, we’d do that with parameters.):
_(context: javascriptallonge.pdf (source-range-83ecb080-03033))_

> **const** aNaughtsAndCrossesGame = generatorNaughtsAndCrosses();
_(source: javascriptallonge.pdf (source-range-83ecb080-03032))_

### **summary**

- We have looked at generators as ways of making iterators over static collections, where state is modelled implicitly in control flow. _(javascriptallonge.pdf (source-range-83ecb080-03045))_
- Again, the salient difference is that an “interactive” generator is stateful, and it embodies its state in its control flow. _(javascriptallonge.pdf (source-range-83ecb080-03046))_

## Basic Operations on Iterables

### **Basic Operations on Iterables**

- Here are the operations we’ve defined on Iterables. _(javascriptallonge.pdf (source-range-83ecb080-03051))_

### **operations that transform one iterable into another**

> **for** ( **let** i = 0; i < numberToTake; ++i) { **const** { done, value } = iterator.next(); **if** (!done) **yield** value; } }
_(source: javascriptallonge.pdf (source-range-83ecb080-03059))_

### **operations that compose two or more iterables into an iterable**

> **function** * zip (...iterables) { **const** iterators = iterables.map(i => i[Symbol.iterator]());
_(source: javascriptallonge.pdf (source-range-83ecb080-03061))_

> Context: Note: zip is also the following special case of zipWith:
_(context: javascriptallonge.pdf (source-range-83ecb080-03063))_

> **const** zip = callFirst(zipWith, (...values) => values);
_(source: javascriptallonge.pdf (source-range-83ecb080-03066))_

### **operations that transform an iterable into a value**

> **const** reduceWith = (fn, seed, iterable) => { **let** accumulator = seed;
_(source: javascriptallonge.pdf (source-range-83ecb080-03068))_

### **memoizing an iterable**

## The Golden Crema: Appendices and Afterwords

### **The Golden Crema: Appendices and Afterwords**

## How to run the examples

### **How to run the examples**

- At the time this book was written, ECMAScript 2015 was not yet widely available. _(javascriptallonge.pdf (source-range-83ecb080-03084))_
- Traceur and Babel are both _transpilers_ , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics. _(javascriptallonge.pdf (source-range-83ecb080-03084))_
- All of the examples in this book were tested using either Google Traceur Compiler[100] , Babel[101] , or both. _(javascriptallonge.pdf (source-range-83ecb080-03084))_
- Traceur and Babel are both _transpilers_ , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics. _(javascriptallonge.pdf (source-range-83ecb080-03084))_
- Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. _(javascriptallonge.pdf (source-range-83ecb080-03104))_
- To see the result of your expressions, you may have to use the console in your web browser. _(javascriptallonge.pdf (source-range-83ecb080-03104))_
- And 4 would appear in your browser’s development console. _(javascriptallonge.pdf (source-range-83ecb080-03109))_
- The care and feeding of node and npm are beyond the scope of this book, but both tools offer clear instructions for those who have already installed node. _(javascriptallonge.pdf (source-range-83ecb080-03110))_
- You can also install the transpilers on your development system and use them with Node[102] on the command line[103] . _(javascriptallonge.pdf (source-range-83ecb080-03110))_

> Context: For example, this ECMAScript 2015 code:
_(context: javascriptallonge.pdf (source-range-83ecb080-03085))_

> **const** before = (decoration) => (method) => **function** () { decoration.apply( **this** , arguments); **return** method.apply( **this** , arguments) };
_(source: javascriptallonge.pdf (source-range-83ecb080-03086))_

> Context: "use strict"
_(context: javascriptallonge.pdf (source-range-83ecb080-03088))_

> **var** before = **function** (decoration) {
_(source: javascriptallonge.pdf (source-range-83ecb080-03089))_

> **const** before = (decoration) => (method) => **function** (...args) { decoration.apply( **this** , args); **return** method.apply( **this** , args) };
_(source: javascriptallonge.pdf (source-range-83ecb080-03101))_

> Context: So instead of just writing:
_(context: javascriptallonge.pdf (source-range-83ecb080-03105))_

> (() => 2 + 2)()
_(source: javascriptallonge.pdf (source-range-83ecb080-03106))_

> Context: And having 4 displayed, you’d need to write:
_(context: javascriptallonge.pdf (source-range-83ecb080-03107))_

> console.log( (() => 2 + 2)() )
_(source: javascriptallonge.pdf (source-range-83ecb080-03108))_

## Thanks!

### **Thanks!**

### **Daniel Friedman and Matthias Felleisen**

- But where _The Little Schemer’s_ primary focus is recursion, _JavaScript Allongé’s_ primary focus is **functions as first-class values** . _(javascriptallonge.pdf (source-range-83ecb080-03120))_
- _JavaScript Allongé_ was inspired by The Little Schemer[104] by Daniel Friedman and Matthias Felleisen. _(javascriptallonge.pdf (source-range-83ecb080-03120))_

### **Richard Feynman**

- Richard Feynman’s QED[105] was another inspiration: A book that explains Quantum Electrodynamics and the “Sum of the Histories” methodology using the simple expedient of explaining how light reflects off a mirror, and showing how most of the things we think are happening–such as light travelling on a straight line, the angle of reflection equalling the angle of refraction, or that a beam of light only interacts with a small portion of the mirror, or that it reflects off a plane–are all wrong. _(javascriptallonge.pdf (source-range-83ecb080-03127))_
- Richard Feynman’s QED[105] was another inspiration: A book that explains Quantum Electrodynamics and the “Sum of the Histories” methodology using the simple expedient of explaining how light reflects off a mirror, and showing how most of the things we think are happening–such as light travelling on a straight line, the angle of reflection equalling the angle of refraction, or that a beam of light only interacts with a small portion of the mirror, or that it reflects off a plane–are all wrong. _(javascriptallonge.pdf (source-range-83ecb080-03127))_

## Copyright Notice

### **Copyright Notice**

> The original words in this book are (c) 2012-2015, Reginald Braithwaite. All rights reserved.
_(source: javascriptallonge.pdf (source-range-83ecb080-03133))_

### **images**

## About The Author

### **About The Author**

- When he’s not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to millions of users, Reg “Raganwald” Braithwaite has authored libraries[221] for JavaScript, CoffeeScript, and Ruby programming such as Allong.es, Method Combinators, Katy, JQuery Combinators, YouAreDaChef, andand, and others. _(javascriptallonge.pdf (source-range-83ecb080-03267))_
- When he’s not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to millions of users, Reg “Raganwald” Braithwaite has authored libraries[221] for JavaScript, CoffeeScript, and Ruby programming such as Allong.es, Method Combinators, Katy, JQuery Combinators, YouAreDaChef, andand, and others. _(javascriptallonge.pdf (source-range-83ecb080-03267))_

### **contact**

## Source review

### Needs review

- “Café Allongé, also called Espresso Lungo, is a drink midway between an Espresso and Americano in strength. There are two different ways to make it. The first, and the one I prefer, is to add a small amount of hot water to a double or quadruple Espresso Ristretto. Like adding a splash of water to wh — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00025))_
- This achieves approximately the same ratio of oils to water as the dilution method, but also releases a different mix of flavours due to the longer extraction. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00026))_
- “The important thing is that neither method of preparation should use so much water as to result in a sickly, pale ghost of Espresso. Moderation in all things.” — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00027))_
- _JavaScript Allongé_ teaches you how to handle complex code, and it also teaches you how to simplify code without dumbing it down. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00035))_
- def foo (first, *rest) # ... — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00050))_
- **function** foo (first, ...rest) { _// ..._ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00060))_
- And presto, rest collects the rest of the arguments without a lot of malarky involving slicing arguments. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00062))_
- Thus, the focus on things like writing decorators. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00067))_
- _But there’s more to it than that_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00067))_
- And these techniques dovetail nicely with Allongé’s focus on composing entities and working with functions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00069))_
- Thus, the “six” edition introduces classes and mixins. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00070))_
- It introduces iterators and generators. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00070))_
- It introduces the notion of implementing private properties with symbols. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00070))_
- We just call some of those functions constructors, others decorators, others functional mixins, and yet others, policies. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00071))_
- From functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so many fruitful directions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00079))_
- **const** filterWith = (fn, iterable) => ({ [Symbol.iterator]: **function** * () { **for** ( **let** element **of** iterable) { **if** (!!fn(element)) **yield** element; } } }); — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00089))_
- There are reasons why the second form is more flexible, especially when used in combination with partial application, but does that outweigh the benefit of having an entire codebase do everything consistently the first way or the second way? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00090))_
- _JavaScript Allongé_ introduces new aspects of programming with functions in each chapter, explaining exactly how JavaScript works. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00094))_
- This upgrade became ECMAScript 5. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00104))_
- For example: classes and modules. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00107))_
- - Better syntax for features that already exist (e.g. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00107))_
- - New functionality in the standard library. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00108))_
- For example: Generators, proxies and WeakMaps. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00112))_
- - Completely new features. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00112))_
- Having written books myself, I know the pain of soliciting and receiving feedback. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00123))_
- books try to hide most of those capabilities away, giving you recipes for writing JavaScript in a way that approximates class-centric programming in other languages. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00135))_
- Not JavaScript Allongé. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00135))_
- It starts with the fundamentals of values, functions, and objects, and then guides you through JavaScript from the inside with exploratory bits of code that illustrate scoping, combinators, context, state, prototypes, and constructors. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00135))_
- Like JavaScript itself, this book gives you a gentle start before showing you its full depth, and like a Cafe Allongé, it’s over too soon. Enjoy! — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00136))_
- Besides, **there’s really no risk at all** . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00143))_
- _The following material is extremely basic, however like most stories, the best way to begin is to start at the very beginning._ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00152))_
- Imagine we are visiting our favourite coffee shop. They will make for you just about any drink you desire, from a short, intense espresso ristretto through a dry cappuccino, up to those coffee-flavoured desert concoctions featuring various concentrated syrups and milks. (You tolerate the existence o — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00153))_
- You express your order at one end of their counter, the folks behind the counter perform their magic, and deliver the coffee you value at the other end. This is exactly how the JavaScript environment works for the purpose of this book. We are going to dispense with web servers, browsers and other co — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00154))_
- Say you hand the barista a café Cubano. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00161))_
- Is this an expression? A value? Neither? Or both? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00164))_
- Let’s hand over some ground coffee plus some boiling water. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00168))_
- let’s go back to the coffee shop. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00168))_
- > "JavaScript" + " " + "Allonge" — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00172))_
- > 10Technically, it’s a _representation_ of a value using Base10 notation, but we needn’t worry about that in this book. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00174))_
- In JavaScript, we test whether two values are identical with the === operator, and whether they are not identical with the !== operator: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00183))_
- 2 === 2 _//=> true_ 'hello' !== 'goodbye' _//=> true_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00184))_
- And then you’re shown another cup of coffee. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00185))_
- 2 === '2' _//=> false_ **true** !== 'true' _//=> true_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00187))_
- Well, JavaScript’s third and fourth possibilities cover that. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00190))_
- An array looks like this: [1, 2, 3]. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00205))_
- Most programmers never encounter the limit on the magnitude of an integer. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00224))_
- In a sense, they behave like little functions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00242))_
- There are lots and lots more operators that can be used with numbers, including bitwise operators like | and & that allow you to operate directly on a number’s binary representation, and a number of other operators that perform assignment or logical comparison that we will look at later. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00248))_
- Let’s start with the second simplest possible function.[16] In JavaScript, it looks like this: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- - (() => 0) _//=> [Function]_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00261))_
- For reasons of appeasing the JavaScript parser, we’ll enclose our functions in parentheses: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00269))_
- Let’s try them out and see. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00269))_
- (() => 0) === (() => 0) — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00270))_
- Let’s put functions to work. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00274))_
- Let’s call the arguments _args_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00275))_
- Since we aren’t giving it any arguments, we’ll simply write () after the expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00277))_
- If not… Welcome to the ALGOL family of programming languages! — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00279))_
- (() => 1)() _//=> 1_ (() => "Hello, JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** )() _//=> Infinity_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00284))_
- (() => (() => 0)())() _//=> 0_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00290))_
- (() => (() => 0 )() )() _//=> 0_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00295))_
- It evaluates to the same thing, 0. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00296))_
- It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00298))_
- So, this is a valid function: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00312))_
- _//=> true_ (() => {})() === (() => {})() _//=> true_ (() => {})() === **undefined** _//=> true_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00324))_
- 1. By evaluating a function that doesn’t return a value (() => {})(), and; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00332))_
- There’s a third way, with JavaScript’s void operator. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00334))_
- Back to our function. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00339))_
- Something like: { statement[1] ; statement[2] ; statement[3] ; ... ; statement[n] } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00347))_
- As you can see, a block with one expression does not behave like an expression, and a block with more than one expression does not behave like an expression constructed with the comma operator: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00357))_
- (() => 2 + 2)() _//=> 4_ (() => { 2 + 2 })() _//=> undefined_ (() => (1 + 1, 2 + 2))() _//=> 4_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00361))_
- (() => { **return** 0 })() _//=> 0_ (() => { **return** 1 })() _//=> 1_ (() => { **return** 'Hello ' + 'World' })() _// 'Hello World'_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00363))_
- The return keyword creates a _return statement_ that immediately terminates the function application and returns the result of evaluating its expression. For example: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00364))_
- Statements belong inside blocks and only inside blocks. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00373))_
- We’ll see a few more of these later. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00373))_
- Some languages simplify this by making everything an expression, but JavaScript maintains this distinction, so when learning JavaScript we also learn about statements like function declarations, for loops, if statements, and so forth. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00373))_
- (() => () => **true** )()() — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00381))_
- () => () => { **return true** ; } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00384))_
- Secondary school mathematics discusses this. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00392))_
- Use them in the body, of course. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00397))_
- It’s a function for calculating the circumference of a circle given the diameter. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00399))_
- To apply a function with an argument (or arguments), we put the argument (or arguments) within the parentheses, like this: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00400))_
- > 22The Argument Sketch from “Monty Python’s Previous Record” and “Monty Python’s Instant Record Collection” — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00404))_
- Expressions consist either of representations of values (like 3.14159265, true, and undefined), operators that combine expressions (like 3 + 2), some special forms like [1, 2, 3] for creating arrays out of expressions, or function ( _arguments_ ) { _body-statements_ } for creating functions. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00412))_
- A return statement accepts any valid JavaScript expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00413))_
- Or a function that returns an array, an array of functions, a function that returns an array of functions, and so forth: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00414))_
- () => [ 1, 2, 3]; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00416))_
- () => [ () => 1, () => 2, () => 3 ]; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00418))_
- Arguments and variables work the same way whether we’re talking about (x) => (y) => x or just plain (x) => x. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00433))_
- You _can_ apply a function to one or more functions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00435))_
- JavaScript parses this whole thing as an expression made up of several sub-expressions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00441))_
- Another, 2, evaluates to the number 2. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00444))_
- JavaScript now evaluates applying the function to the argument 2. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00445))_
- are identical to each other if they have the same content. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00459))_
- And with that, we’re ready to look at _closures_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00462))_
- When we combine our knowledge of value types, reference types, arguments, and closures, we’ll understand why this function always evaluates to true no matter what argument[26] you apply it to: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00462))_
- NaN in JavaScript behaves a lot like NULL in SQL. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00465))_
- Given ( _some function_ )( _some argument_ ), we know that we apply the function to the argument, create an environment, bind the value of the argument to the name, and evaluate the function’s expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00472))_
- The environment belonging to the function with signature (x) => ... becomes {x: 1, ...}, and the result of applying the function is another function value. It makes sense that the result value is a function, because the expression for (x) => ...’s body is: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00475))_
- Then we’re going to take the value of that function and apply it to the argument 2, something like this: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00477))_
- Up to now, we’ve only seen one way to “bind” a variable, namely by passing in an argument with the same name. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00486))_
- has a free variable, but the entire expression refers to (x) => ..., and it doesn’t have a free variable: The only variable anywhere in its body is x, which is certainly bound within (x) => .... — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- Let’s fill in the blanks! — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00503))_
- Only you call it with (1)(2)(3) instead of (1, 2, 3). — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00513))_
- JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00522))_
- But before we do so, there’s one final question: Where does the ancestry start? If there’s no other code in a file, what is (x) => x’s parent environment? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00528))_
- Create an environment for them, of course. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00532))_
- Sometimes, programmers wish to avoid this. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00532))_
- _// ... lots of JavaScript ..._ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00535))_
- What do we put inside our new function that binds 3.14159265 to the name PI when evaluated? Our circumference function, of course: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00550))_
- It produces the same result as our previous expressions for a diameter-calculating function: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00563))_
- ((diameter) => diameter * 3.14159265)(2) _//=> 6.2831853_ ((PI) => (diameter) => diameter * PI )(3.14159265)(2) _//=> 6.2831853_ ((diameter) => ((PI) => diameter * PI)(3.14159265))(2) _//=> 6.2831853_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00564))_
- Every time we invoke the outer function, we’ll invoke the inner function. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00577))_
- And we could use it like this: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00584))_
- Even better, it puts the symbol (like PI) close to the value (3.14159265). — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00592))_
- The const keyword introduces one or more bindings in the block that encloses it. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00592))_
- It doesn’t incur the cost of a function invocation. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00592))_
- It works just as we want. Instead of: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00594))_
- (d) => { **const** calc = (diameter) => { **const** PI = 3.14159265; **return** diameter * PI }; **return** "The circumference is " + calc(d) } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00603))_
- For readability, most people put one binding per line: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00606))_
- (n) => { **const** even = (x) => { **if** (x === 0) **return true** ; **else return** !even(x - 1); } **return** even(n) } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00613))_
- ((n) => { **const** even = (x) => { **if** (x === 0) **return true** ; **else return** !even(x - 1); } **return** even(n) })(13) _//=> false_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00615))_
- (n) => { **const** even = (x) => { **if** (x === 0) **return true** ; **else** { **const** odd = (y) => !even(y); **return** odd(x - 1); } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00617))_
- } **return** even(n) } And this also works: ((n) => { **const** even = (x) => { **if** (x === 0) **return true** ; **else** { **const** odd = (y) => !even(y); **return** odd(x - 1); } } **return** even(n) })(42) _//=> true_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00620))_
- Let’s back up and reconsider how closures work. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00624))_
- Here’s the second formulation of our diameter function, bound to a name using an IIFE: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00625))_
- 31https://en.wikipedia.org/wiki/Scope_(computer_science)#Lexical_scope_vs._dynamic_scope — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00637))_
- And we know that functions create environments. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00644))_
- Let’s start, as above, by doing this with parameters. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00647))_
- Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00657))_
- We say that when we bind a variable using a parameter inside another binding, the inner binding _shadows_ the outer binding. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00659))_
- So what about const. Does it work the same way? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00660))_
- Yes, names bound with const shadow enclosing bindings just like parameters. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00664))_
- That’s why we made all these IIFEs. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00665))_
- **if** ( **true** ) { _// an immediately invoked block statement (IIBS)_ } Let’s try it: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00667))_
- ((diameter) => { **const** PI = 3; **if** ( **true** ) { **const** PI = 3.14159265; **return** diameter * PI; } })(2) _//=> 6.2831853_ ((diameter) => { **const** PI = 3.14159265; **if** ( **true** ) { **const** PI = 3; } **return** diameter * PI; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00668))_
- Ah! const statements don’t just shadow values bound within the environments created by functions, they shadow values bound within environments created by blocks! — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00672))_
- This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00673))_
- Being able to bind a name inside of a block means that if the name is only needed in the block, we are not “leaking” its binding to other parts of the code that do not need to interact with it. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00679))_
- **const** evenStevens = (n) => { **if** (n === 0) { **return true** ; } **else if** (n == 1) { **return false** ; } **else** { n = n - 2; **return** evenStevens(n); } } evenStevens(42) _//=> true_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00685))_
- The line n = n - 2; _rebinds_ a new value to the name n. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00686))_
- evenStevens = (n) => { **if** (n === 0) { **return true** ; } **else if** (n == 1) { **return false** ; } **else** { **return** evenStevens(n - 2); } } _//=> ERROR, evenStevens is read-only_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00687))_
- Let’s get right to it. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00694))_
- It doesn’t name the function “repeat” for the same reason that const answer = 42 doesn’t name the number 42. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00696))_
- And here’s (almost) the exact same function written using the function keyword: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00701))_
- **function** (str) { **return** str + str } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00702))_
- We introduce a function with the function keyword. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00704))_
- **function** (n) { **return** (1.618**n - -1.618**-n) / 2.236; } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00714))_
- This still does not _name_ a function, but as we noted above, functions written with the function keyword have an optional “something else.” Could that “something else” name a function? Yes, of course.[33] — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00715))_
- **const** repeat = **function** repeat (str) { **return** str + str; }; **const** fib = **function** fib (n) { **return** (1.618**n - -1.618**-n) / 2.236; }; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00717))_
- In this book we are not examining JavaScript’s tooling such as debuggers baked into browsers, but we will note that when you are navigating call stacks in all modern tools, the function’s binding name is ignored but its actual name is displayed, so naming functions is very useful even if they don’t  — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00724))_
- someBackboneView.on('click', **function** clickHandler () { _//..._ }); — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00728))_
- ( **function** even (n) { **if** (n === 0) { **return true** } **else return** !even(n - 1) })(5) _//=> false_ ( **function** even (n) { **if** (n === 0) { **return true** } **else return** !even(n - 1) })(2) _//=> true_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00734))_
- ( **function** () { **return** fizzbuzz(); — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00758))_
- ( **function** (camelCase) { **return** fizzbuzz(); — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00768))_
- **if** (camelCase) { **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } } **else** { **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } } })( **true** ) _//=> 'FizzBuzz'? Or ERROR: Can't find variable: fizzbuzz?_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00769))_
- **function** trueDat () { **return true** } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00772))_
- ( **function** trueDat () { **return true** }) — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00774))_
- As we’ve seen, JavaScript functions take values as arguments and return values. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00781))_
- **const** repeat = (num, fn) => (num > 0) ? (repeat(num - 1, fn), fn(num)) : **undefined** repeat(3, **function** (n) { console.log(`Hello **${** n **}** `) }) _//=>_ 'Hello 1' 'Hello 2' 'Hello 3' **undefined** — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00783))_
- But before we go on, we’ll talk about some specific types of higher-order functions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00784))_
- Higher-order functions dominate _JavaScript Allongé_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00784))_
- > 36http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20 — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00790))_
- You’ll find lots more perusing the recipes in this book. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00803))_
- You’ll see other function decorators in the recipes, like once and maybe. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00819))_
- When you look at functions within functions in JavaScript, there’s a bit of a “spaghetti code” look to it. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00824))_
- When a function takes multiple arguments, we “apply” the function to the arguments by evaluating it with all of the arguments, producing a value. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00839))_
- This code implements a partial application of the map function by applying the function (n) => n * n as its second argument: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00843))_
- We’ll discuss mapWith again. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00849))_
- > 41If we don’t want to sort out Underscore, we can also write the following: const map = (a, fn) => a.map(fn);, and trust that it works even though we haven’t discussed methods yet. const map = _.map; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00852))_
- Although arguments looks like an array, it isn’t an array: It’s more like an object[43] that happens to bind some values to properties with names that look like integers starting with zero: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00868))_
- > 43We’ll look at arrays and plain old javascript objects in depth later. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00872))_
- The magic names this and arguments have a different behaviour when you invoke a function that was defined with a fat arrow: Instead of being bound when the function is invoked, the fat arrow function always acquires the bindings for this and arguments from its enclosing scope, just like any other bi — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00880))_
- ( **function** () { **return** ( **function** () { **return** arguments[0]; })('inner'); })('outer') _//=> "inner"_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00884))_
- **const** row = **function** () { **return** mapWith( (column) => column * arguments[0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) _//=> [3,6,9,12,15,18,21,24,27,30,33,36]_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00889))_
- It’s the same idea, after all. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00891))_
- **const** row = **function** () { **return** mapWith( **function** (column) { **return** column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) _//=> [1,4,9,16,25,36,49,64,81,100,121,144]_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00894))_
- Now our inner function binds arguments[0] every time it is invoked, so we get the same result as if we’d written function (column) { return column * column }. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00895))_
- - Expression bodies evaluate to the value of the expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00912))_
- - Function application creates a scope. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00916))_
- You’ll find examples in Lemonad[45] from Michael Fogus, Functional JavaScript[46] from Oliver Steele and the terse but handy node-ap[47] from James Halliday. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00931))_
- **const** callFirst = (fn, larg) => **function** (...rest) { **return** fn.call( **this** , larg, ...rest); } **const** callLast = (fn, rarg) => **function** (...rest) { **return** fn.call( **this** , ...rest, rarg); } **const** greet = (me, you) => `Hello, **${** you **}** , my name is **${** me ** — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00933))_
- JavaScript’s map actually calls each function with _three_ arguments: The element, the index of the element in the array, and the array itself. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00958))_
- In that example, it looks exactly like the mapping function you’ll find in most languages: You pass it a function, and it calls the function with one argument, the element of the array. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00958))_
- However, that’s not the whole story. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00958))_
- [1, 2, 3].map( **function** (element, index, arr) { console.log({element: element, index: index, arr: arr}) }) _//=> { element: 1, index: 0, arr: [ 1, 2, 3 ] } // { element: 2, index: 1, arr: [ 1, 2, 3 ] } // { element: 3, index: 2, arr: [ 1, 2, 3 ] }_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00960))_
- It takes an optional radix argument. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00963))_
- ? fn : **function** (something) { **return** fn.call( **this** , something) } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00969))_
- It takes a value and returns a function that always returns the value, but if you pass it a function, it executes the function for side-effects. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00981))_
- **const** tap = (value, fn) => { **const** curried = (fn) => ( **typeof** (fn) === 'function' && fn(value), value ); **return** fn === **undefined** ? curried : curried(fn); } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00991))_
- tap('espresso', (it) => { console.log(`Our drink is ' **${** it **}** '`) }); _//=> Our drink is 'espresso'_ 'espresso' And if we wish it to do nothing at all, We can write either tap('espresso')() or tap('espresso', null) — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00995))_
- It’s also useful for working with object and instance methods. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-00996))_
- **const** maybe = (fn) => **function** (...args) { **if** (args.length === 0) { **return** } **else** { **for** ( **let** arg **of** args) { **if** (arg == **null** ) **return** ; } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01010))_
- > 50https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01011))_
- **return** fn.apply( **this** , args) } } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01015))_
- As a bonus, maybe plays very nicely with instance methods, we’ll discuss those later: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01018))_
- **const** once = (fn) => { **let** done = **false** ; **return function** () { **return** done ? **void** 0 : ((done = **true** ), fn.apply( **this** , arguments)) } } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01027))_
- You pass it a function, and you get a function back. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01028))_
- It seems some people will only try blind dating once. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01033))_
- It accepts a coach, a captain, and an arbitrary number of players. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01041))_
- **function** team(coach, captain, ...players) { console.log(` **${** captain **}** (captain)`); **for** ( **let** player **of** players) { console.log(player); } console.log(`squad coached by **${** coach **}** `); } team('Luis Enrique', 'Xavi Hernández', 'Marc-André ter Stegen', 'Martín Montoya', ' — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01042))_
- **function** team2(...players, captain, coach) { console.log(` **${** captain **}** (captain)`); **for** ( **let** player **of** players) { console.log(player); } console.log(`squad coached by **${** coach **}** `); } _//=> Unexpected token_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01047))_
- ECMAScript 2015 only permits gathering parameters from the _end_ of the parameter list. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01048))_
- **function** rightVariadic (fn) { **if** (fn.length < 1) **return** fn; **return function** () { **var** ordinaryArgs = (1 <= arguments.length ? __slice.call(arguments, 0, fn.length - 1) : []), restOfTheArgsList = __slice.call(arguments, fn.length - 1), args = (fn.length <= arguments.length ? ordina — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01052))_
- 53Another history lesson. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01053))_
- **const** leftVariadic = (fn) => { **if** (fn.length < 1) { **return** fn; } **else** { **return function** (...args) { **const** gathered = args.slice(0, args.length - fn.length + 1), spread = args.slice(args.length - fn.length + 1); **return** fn.apply( **this** , [gathered].concat(spread) — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01066))_
- butLastAndLast('why', 'hello', 'there', 'little', 'droid') _//=> [["why","hello","there","little"],"droid"]_ — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01071))_
- **const** leftGather = (outputArrayLength) => { **return function** (inputArray) { **return** [inputArray.slice(0, inputArray.length - outputArrayLength + 1)].conc\ at( inputArray.slice(inputArray.length - outputArrayLength + 1) ) } }; **const** [butLast, last] = leftGather(2)(['why', 'hello', 'ther — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01085))_
- We’ve seen operators that act on numeric values, like + and %. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01091))_
- is a unary prefix operator that negates its argument. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01097))_
- **false** && **false** _//=> false_ **false** && **true** _//=> false_ **true** && **false** _//=> false_ **true** && **true** _//=> true_ **false** || **false** _//=> false_ **false** || **true** _//=> true_ **true** || **false** _//=> true_ **true** || **true** _//=> true_ — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01102))_
- We’ll look at those presently. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01103))_
- This affects the way the !, &&, and || operators work. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01107))_
- We’ll look at them in a moment, but first, we’ll look at one more operator. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01107))_
- It’s the only operator that takes _three_ arguments. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01108))_
- > 54We will not discuss JavaScript’s numeric behaviour in much depth in this book, but the most important thing to know is that it implements the IEEE Standard for Floating-Point Arithmetic (IEEE 754), a technical standard for floating-point computation established in 1985 by the Institute of Electr — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01109))_
- So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser(), this — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01128))_
- is an idiom that means “true if currentUser is truthy.” Thus, a function like currentUser() is free to return null, or undefined, or false if there is no current user. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01131))_
- is the way we write “is truthy” in JavaScript. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01132))_
- - && evaluates its left-hand expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01134))_
- - If its left-hand expression evaluates to something falsy, && returns the value of its lefthand expression without evaluating its right-hand expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01135))_
- - If its left-hand expression evaluates to something truthy, && evaluates its right-hand expression and returns the value of the right-hand expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01136))_
- - || evaluates its left-hand expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01137))_
- - If its left-hand expression evaluates to something truthy, || returns the value of its lefthand expression without evaluating its right-hand expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01138))_
- - If its left-hand expression evaluates to something false, || evaluates its right-hand expression and returns the value of the right-hand expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01139))_
- In JavaScript, && and || aren’t boolean logical operators in the logical sense. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01146))_
- If n === 0, JavaScript does not evaluate (n !== 1 && even(n - 2)). This is very important! Imagine that JavaScript evaluated both sides of the || operator before determining its value. n === 0 would be true. What about (n !== 1 && even(n - 2))? Well, it would evaluate even(n - 2), or even(-2) — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01156))_
- and so on and so forth until JavaScript throws up its hands and runs out of stack space. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01157))_
- But that’s not what happens. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01158))_
- It’s best to think of || and && as control-flow operators. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01159))_
- This leads to the infinite recursion we fear. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01166))_
- **const** or = (a, b) => a() || b() **const** and = (a, b) => a() && b() **const** even = (n) => or(() => n === 0, () => and(() => n !== 1, () => even(n - 2))) even(7) _//=> false_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01170))_
- is a logical operator, it always returns true or false. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01174))_
- [1] _//=> [1]_ [2, 3, 4] _//=> [2,3,4]_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01193))_
- We saw how to construct an array literal using [, expressions, , and ]. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01221))_
- **return** ` **${** first **}** is a **${** occupation **}** `; } description([["Reginald", "Braithwaite"], "programmer"]) _//=> "Reginald is a programmer"_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01240))_
- Some other languages call them first and butFirst, or head and tail. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01245))_
- What is the reverse of gathering? We know that: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01256))_
- What is the reverse? It would be: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01258))_
- to place the elements of an array inside another array. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01262))_
- And if there aren’t any items to assign with ..., JavaScript assigns an empty array: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01272))_
- Some languages support multiple return values: A function can return several things at once, like a value and an error code. This can easily be emulated in JavaScript with destructuring: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01276))_
- **const** description = (nameAndOccupation) => { **if** (nameAndOccupation.length < 2) { **return** ["", "occupation missing"] } **else** { **const** [[first, last], occupation] = nameAndOccupation; **return** [` **${** first **}** is a **${** occupation **}** `, "ok"]; } } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01279))_
- It is very much like an array literal. And consider how we bind values to parameter names: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01285))_
- It acts like destructuring. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01287))_
- It _looks_ like destructuring. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01287))_
- **const** numbers = (...nums) => nums; numbers(1, 2, 3, 4, 5) _//=> [1,2,3,4,5]_ **const** headAndTail = (head, ...tail) => [head, tail]; headAndTail(1, 2, 3, 4, 5) _//=> [1,[2,3,4,5]]_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01290))_
- Gathering works with parameters! — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01291))_
- We _gather_ the _rest_ of the parameters. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01292))_
- Consists of an element concatenated with a list . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01303))_
- Let’s convert our rules to array literals. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01304))_
- [] _//=> []_ ["baz", ...[]] _//=> ["baz"]_ ["bar", ...["baz"]] _//=> ["bar","baz"]_ ["foo", ...["bar", "baz"]] _//=> ["foo","bar","baz"]_ — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01305))_
- **const** [first, ...rest] = []; first _//=> undefined_ rest _//=> []:_ **const** [first, ...rest] = ["foo"]; first _//=> "foo"_ rest _//=> []_ **const** [first, ...rest] = ["foo", "bar"]; first _//=> "foo"_ rest _//=> ["bar"]_ **const** [first, ...rest] = ["foo", "bar", "baz"]; first _//=> "foo"_ r — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01310))_
- Armed with our definition of an empty list and with what we’ve already learned, we can build a great many functions that operate on arrays. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01314))_
- its .length. But as an exercise, how would we write a length function using just what we have already? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01318))_
- First, we pick what we call a _terminal case_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01319))_
- But we don’t know the length of rest. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01321))_
- “Recursion” sometimes seems like an elaborate party trick. There’s even a joke about this: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01327))_
- When promising students are trying to choose between pure mathematics and applied engineering, they are given a two-part aptitude test. In the first part, they are led to a laboratory bench and told to follow the instructions printed on the card. They find a bunsen burner, a sparker, a tap, an empty — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01328))_
- Of course, all the students know what to do: They fill the beaker with water, place the stand on the burner and the beaker on the stand, then they turn the burner on and use the sparker to ignite the flame. After a bit the water boils, and they turn off the burner and are lead to a second bench. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01331))_
- The engineers light the burner immediately. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01332))_
- Recursive algorithms follow the “divide and conquer” strategy for solving a problem: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01333))_
- It’s very useful and simple to understand. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01339))_
- Let’s take another example. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01339))_
- We already know how to divide arrays into smaller pieces. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01340))_
- **const** flatten = ([first, ...rest]) => { **if** (first === **undefined** ) { **return** []; } **else if** (!Array.isArray(first)) { **return** [first, ...flatten(rest)]; } **else** { **return** [...flatten(first), ...flatten(rest)]; } } flatten(["foo", [3, 4, []]]) _//=> ["foo",3,4]_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01350))_
- **const** mapWith = (fn, [first, ...rest]) => first === **undefined** ? [] : [fn(first), ...mapWith(fn, rest)]; mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01366))_
- With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01369))_
- 1. Given the terminal case of an empty list, we return a 0 instead of an empty list, and; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01376))_
- We catenate the square of each element to the result of applying sumSquares to the rest of the elements. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01377))_
- Let’s look at how. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01399))_
- **const** mapWith = (fn, [first, ...rest]) => first === **undefined** ? [] : [fn(first), ...mapWith(fn, rest)]; mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01400))_
- Let’s step through its execution. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01401))_
- **const** mapWith = **function** (fn, [first, ...rest]) { **if** (first === **undefined** ) { **return** []; } **else** { **const** _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_temp1, ..._temp2]; **return** _temp3; } } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01403))_
- This keeps on happening, so that JavaScript collects the values 1, 2, 3, 4, and 5 plus housekeeping information by the time it calls mapWith((x) => x * x, []). — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01409))_
- 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77 — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01413))_
- A “tail-call” occurs when a function’s last act is to invoke another function, and then return whatever the other function returns. For example, consider the maybe function decorator: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01418))_
- **const** maybe = (fn) => **function** (...args) { **if** (args.length === 0) { **return** ; } **else** { **for** ( **let** arg **of** args) { **if** (arg == **null** ) **return** ; } **return** fn.apply( **this** , args); } } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01419))_
- The first two don’t return anything, they don’t matter. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- But while we’re doing that, it’s annoying to remember to call it with a zero. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01436))_
- This lengthDelaysWork function calls itself in tail position. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01436))_
- 2980, 2981, 2982, 2983, 2984, 2985, 2986, 2987, 2988, 2989, 2990, 2991, 2992, 2993, 2994, 2995, 2996, 2997, 2998, 2999 ]) — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01457))_
- 5! = 5 x 4 x 3 x 2 x 1 = 120. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01466))_
- The naïve function for calcuating the factorial of a positive integer follows directly from the definition: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01467))_
- **const** factorialWithDelayedWork = (n, work) => n === 1 ? work : factorialWithDelayedWork(n - 1, n * work); **const** factorial = (n) => factorialWithDelayedWork(n, 1); — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01471))_
- **const** factorial = (n, work) => n === 1 ? work : factorial(n - 1, n * work); factorial(1, 1) _//=> 1_ factorial(5, 1) _//=> 120_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01482))_
- **const** factorial = (n, work = 1) => n === 1 ? work : factorial(n - 1, n * work); factorial(1) _//=> 1_ factorial(6) _//=> 720_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01488))_
- **const** length = ([first, ...rest], numberToBeAdded = 0) => first === **undefined** ? numberToBeAdded : length(rest, 1 + numberToBeAdded) length(["foo", "bar", "baz"]) _//=> 3_ **const** mapWith = (fn, [first, ...rest], prepend = []) => first === **undefined** ? prepend : mapWith(fn, rest, [...pre — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01490))_
- We saw earlier that destructuring parameters works the same way as destructuring assignment. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01493))_
- Much slower than the built-in .map method for arrays. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01512))_
- Every time we call mapWith, we’re calling [...prepend, fn(first)]. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01513))_
- Worse, the JavaScript Engine actually copies the elements from prepend into the new array one at a time. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01516))_
- So here’s a question: If this is such a slow approach, why do some examples of “functional” algorithms work this exact way? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01520))_
- Notice that though JavaScript displays our list as if it is composed of arrays nested within each other like Russian Dolls, in reality the arrays refer to each other with references, so [1,[2,[3,[4,[5,null]]]]] is actually more like: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01543))_
- But what about the rest of the list? cdr does the trick: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01552))_
- In Lisp, it’s blazingly fast because it happens in hardware. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- Again, it’s just extracting a reference from a cons cell, it’s very fast. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- Getting back to JavaScript now, when we write [first, ...rest] to gather or spread arrays, we’re emulating the semantics of car and cdr, but not the implementation. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01557))_
- If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01564))_
- In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01565))_
- - { year: 2012, month: 6, day: 14 } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01591))_
- Two objects created with separate evaluations have differing identities, just like arrays: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01592))_
- **const** unique = () => [], — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01597))_
- - { 'first name': 'reginald', 'last name': 'lewis' }['first name'] _//=> 'reginald'_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01603))_
- All containers can contain any value, including functions or other containers, like a fat arrow function: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01611))_
- **const** SecretDecoderRing = { encode: **function** (plaintext) { **return** plaintext .split('') .map( **char** => **char** .charCodeAt() ) .map( code => code + 1 ) .map( code => String.fromCharCode(code) ) .join(''); }, decode: **function** (cyphertext) { **return** cyphertext .split('') .map( ** — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01614))_
- **const** SecretDecoderRing = { encode: **function** encode (plaintext) { **return** plaintext .split('') .map( **char** => **char** .charCodeAt() ) .map( code => code + 1 ) .map( code => String.fromCharCode(code) ) .join(''); }, decode: **function** decode (cyphertext) { **return** cyphertext .spli — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01617))_
- **const** SecretDecoderRing = { encode (plaintext) { **return** plaintext .split('') .map( **char** => **char** .charCodeAt() ) .map( code => code + 1 ) .map( code => String.fromCharCode(code) ) .join(''); }, decode (cyphertext) { **return** cyphertext .split('') .map( **char** => **char** .charCode — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01619))_
- Just as we saw with arrays, we can write destructuring assignments with literal object syntax. So, we can write: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01625))_
- **const** user = { name: { first: "Reginald", last: "Braithwaite" }, occupation: { title: "Author", responsibilities: [ "JavaScript Allongé", "JavaScript Spessore", "CoffeeScript Ristretto" ] } }; user.name.last _//=> "Braithwaite"_ user.occupation.title _//=> "Author"_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01626))_
- **const** {name: { first: given, last: surname}, occupation: { title: title } } = us\ er; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01628))_
- **const** description = ({name: { first: given }, occupation: { title: title } }) => ` **${** given **}** is a **${** title **}** `; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01633))_
- Terrible grammar and capitalization, but let’s move on. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01636))_
- In that case, a linked list of the numbers 1, 2, and 3 will look like this: { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY } } }. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01647))_
- Well, let’s start with the simplest possible thing, making a _copy_ of a list. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01657))_
- ? delayed : copy2(node.rest, { first: node.first, rest: delayed }); — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01666))_
- Well, well, well. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01669))_
- This isn’t a bad thing by any stretch of the imagination. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01669))_
- ? delayed : reverseMapWith(fn, node.rest, { first: fn(node.first), rest: delayed }); reverseMapWith((x) => x * x, OneTwoThree) _//=> {"first":9,"rest":{"first":4,"rest":{"first":1,"rest":{}}}}_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01673))_
- Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01680))_
- Their identities stay the same, but not their structure. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01688))_
- JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01711))_
- Languages like Haskell[70] don’t permit mutation at all. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01715))_
- **const** EMPTY = {}; **const** OneToFive = { first: 1, rest: { first: 2, rest: { first: 3, rest: { first: 4, rest: { first: 5, rest: EMPTY } } } } }; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01721))_
- Changes made to ThreeToFive affect OneToFive, because they share the same structure. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01731))_
- OneToFive _//=> [1,2,3,4,5]_ **const** [a, b, ...ThreeToFive] = OneToFive; ThreeToFive _//=> [3, 4, 5]_ ThreeToFive[0] = "three"; ThreeToFive[1] = "four"; ThreeToFive[2] = "five"; ThreeToFive _//=> ["three","four","five"]_ OneToFive _//=> [1,2,3,4,5]_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01736))_
- In general, it’s easier to reason about data that doesn’t change. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01738))_
- So back to avoiding mutation. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01738))_
- Consider our copy algorithm. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01740))_
- **const** copy = (node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail === **null** ) { **const** { first, rest } = node; **const** newNode = { first, rest }; **return** copy(rest, newNode, newNode); } **else** { **const** { first, rest } = no — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01746))_
- **const** mapWith = (fn, node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail === **null** ) { **const** { first, rest } = node; **const** newNode = { first: fn(first), rest }; **return** mapWith(fn, rest, newNode, newNode); } **else** { **con — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01749))_
- **const** evenStevens = (n) => { **if** (n === 0) { **return true** ; } **else if** (n == 1) { **return false** ; } **else** { n = n - 2; **return** evenStevens(n); } } evenStevens(42) _//=> true_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01760))_
- The line n = n - 2; _rebinds_ a new value to the name n. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01761))_
- evenStevens = (n) => { **if** (n === 0) { **return true** ; } **else if** (n == 1) { **return false** ; } **else** { **return** evenStevens(n - 2); } } _//=> ERROR, evenStevens is read-only_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01762))_
- We took the time to carefully examine what happens with bindings in environments. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01769))_
- Let’s take the time to explore what happens with reassigning values to variables. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01769))_
- (() => { **let** age = 49; **if** ( **true** ) { **let** age = 50; } **return** age; })() _//=> 49_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01771))_
- {age: 50, '..': {age: 49, '..': global-environment}} — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01775))_
- However, if we don’t shadow age with let, reassigning within the block changes the original: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01780))_
- (() => { **let** age = 49; **if** ( **true** ) { age = 50; } **return** age; })() _//=> 50_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01781))_
- It then rebinds the name in that environment. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01782))_
- If you buy that argument, the way that shadowing works in JavaScript exists to protect us from accidentally shadowing a variable when we move code around. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01784))_
- Some programmers dislike deliberately shadowing variables. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01784))_
- (() => { **let** age = 49; **if** ( **true** ) { **const** age = 50; } age = 51; **return** age; })() _//=> 51_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01786))_
- (() => { **const** age = 49; **if** ( **true** ) { **let** age = 50; } age = 52; **return** age; })() _//=> ERROR: age is read-only_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01790))_
- **const** factorial = (n) => { **let** x = n; **if** (x === 1) { **return** 1; } **else** { --x; **return** n * factorial(x); } } factorial(5) _//=> 120_ **const** factorial2 = (n) => { **var** x = n; **if** (x === 1) { **return** 1; } **else** { --x; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01794))_
- So that’s five different ways so far. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01795))_
- Function declarations bind names. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01795))_
- Named function expressions bind names. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01795))_
- Well, parameters bind names. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01795))_
- But of course, it’s not exactly like let. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01799))_
- It’s just different enough to present a source of confusion. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01799))_
- (() => { **var** age = 49; **if** ( **true** ) { **var** age = 50; } **return** age; })() _//=> 50_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01800))_
- **return** innerFactorial(n, 1); **function** innerFactorial (x, y) { **if** (x == 1) { **return** y; } **else** { **return** innerFactorial(x-1, x * y); } } } factorial(4) _//=> 24_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01804))_
- **const** factorial = (n) => { **let** innerFactorial = **function** innerFactorial (x, y) { **if** (x == 1) { **return** y; } **else** { **return** innerFactorial(x-1, x * y); } } **return** innerFactorial(n, 1); } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01808))_
- JavaScript hoists the let and the assignment. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01809))_
- **return** innerFactorial(n, 1); **var** innerFactorial = **function** innerFactorial (x, y) { **if** (x == 1) { **return** y; } **else** { **return** innerFactorial(x-1, x * y); } } } factorial(4) _//=> undefined is not a function (evaluating 'innerFactorial(n, 1)')_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01811))_
- JavaScript hoists the declaration, but not the assignment. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01812))_
- innerFactorial = **function** innerFactorial (x, y) { **if** (x == 1) { **return** y; } **else** { **return** innerFactorial(x-1, x * y); } } } factorial(4) _//=> undefined is not a function (evaluating 'innerFactorial(n, 1)')_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01817))_
- It looks a lot like the for loop in C. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01821))_
- About 30 seconds later Gauss gave him the answer. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- Of course Gauss came up with the answer about 20 times faster than the other kids. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01824))_
- **var** introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; **for** ( **var** i = 0; i < 3; i++) { introductions[i] = "Hello, my name is " + names[i] } introductions _//=> [ 'Hello, my name is Karl', // 'Hello, my name is Friedrich', // 'Hello, my name is Gauss' ]_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01828))_
- Let’s get fancy! — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01829))_
- **var** introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; **for** ( **var** i = 0; i < 3; i++) { introductions[i] = (soAndSo) => `Hello, **${** soAndSo **}** , my name is **${** names[i] **}** ` } introductions _//=> [ [Function], // [Function], // [Function] ]_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01830))_
- Again, so far, so good. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01831))_
- **var** introductions = [], names = ['Karl', 'Friedrich', 'Gauss'], i = **undefined** ; **for** (i = 0; i < 3; i++) { introductions[i] = **function** (soAndSo) { **return** "Hello, " + soAndSo + ", my name is " + names[i] } } introductions — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01836))_
- That’s not what we want at all. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01837))_
- **let** introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; **for** ( **let** i = 0; i < 3; i++) { introductions[i] = (soAndSo) => `Hello, **${** soAndSo **}** , my name is **${** names[i] **}** ` } introductions[1]('Raganwald') _//=> 'Hello, Raganwald, my name is Friedrich'_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01839))_
- **var** introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; **for** ( **var** i = 0; i < 3; i++) { ((i) => { introductions[i] = (soAndSo) => `Hello, **${** soAndSo **}** , my name is **${** names[i] **}** ` } })(i) } introductions[1]('Raganwald') _//=> 'Hello, Raganwald, my name is Friedrich — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01841))_
- Now we’re creating a new inner parameter, i and binding it to the value of the outer i. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01844))_
- And therefore, modifications to the parent also modify the child, and modifications to the child also modify the parent. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01858))_
- **const** parentArray = [1, 2, 3]; **const** [aFirst, ...childArray] = parentArray; parentArray[2] = "three"; childArray[0] = "two"; parentArray _//=> [1,2,"three"]_ childArray _//=> ["two",3]_ **const** EMPTY = { first: {}, rest: {} }; **const** parentList = { first: 1, rest: { first: 2, rest: { fi — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01860))_
- **const** copy = (node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail === **null** ) { **const** { first, rest } = node; **const** newNode = { first, rest }; **return** copy(rest, newNode, newNode); } **else** { **const** { first, rest } = no — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01868))_
- set(2, "three", parentList); set(0, "two", childList); parentList _//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\_ {},"rest":{}}}}} childList _//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01872))_
- Our new at and set functions behave similarly to array[index] and array[index] = value. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01873))_
- So back to the problem of structure sharing. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01875))_
- **const** parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; **const** childList = rest(parentList); **const** newParentList = set(2, "three", parentList); set(0, "two", childList); — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01877))_
- In case we modify a child list. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01885))_
- **const** set = (index, value, list) => index === 0 ? { first: value, rest: list.rest } : { first: list.first, rest: set(index - 1, value, list.rest) }; **const** parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; **const** childList = rest(parentList); **const** newPare — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01887))_
- _//=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{"first":{},"rest":\_ {}}}}} childList _//=> {"first":2,"rest":{"first":3,"rest":{"first":{},"rest":{}}}}_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01890))_
- _//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\_ rest":{}}}}} newChildList //=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}} — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01893))_
- Like all strategies, it makes a tradeoff: It’s much cheaper than pessimistically copying structures when you make an infrequent number of small changes, but if you tend to make a lot of changes to some that you aren’t sharing, it’s more expensive. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01899))_
- I then forgot about it for a while. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01909))_
- I sent him an email sharing my result, to demonstrate my ability to follow through. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01909))_
- **const** pair = (first, rest = EMPTY) => ({first, rest}); **const** list = (...elements) => { **const** [first, ...rest] = elements; **return** elements.length === 0 ? EMPTY : pair(first, list(...rest)) } **const** forceAppend = (list1, list2) => { **if** (isEmpty(list1)) { **return** "FAIL!" } **i — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01912))_
- } } **const** tortoiseAndHare = (aPair) => { **let** tortoisePair = aPair, harePair = aPair.rest; **while** ( **true** ) { **if** (isEmpty(tortoisePair) || isEmpty(harePair)) { **return false** ; } **if** (tortoisePair.first === harePair.first) { **return true** ; } harePair = harePair.rest; **if**  — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01916))_
- **const** teleportingTurtle = (list) => { **let** speed = 1, rabbit = list, turtle = rabbit; **while** ( **true** ) { **for** ( **let** i = 0; i <= speed; i += 1) { rabbit = rabbit.rest; **if** (rabbit == **null** ) { **return false** ; } **if** (rabbit === turtle) { **return true** ; } } turtle = r — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01924))_
- In Functional Iterators, we’ll investigate one pattern for separating these concerns. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01927))_
- Let’s consider a remarkably simple problem: Finding the sum of the elements of an array. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01933))_
- As we saw earlier, this entangles the mechanism of traversing the array with the business of summing the bits. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01936))_
- **const** callLeft = (fn, ...args) => (...remainingArgs) => fn(...args, ...remainingArgs); **const** foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === **undefined** ? terminalValue : fn(first, foldArrayWith(fn, terminalValue, rest)); — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01937))_
- What happens when we want to sum a tree of numbers? Or a linked list of numbers? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01940))_
- fn(foldTreeWith(fn, terminalValue, first), foldTreeWith(fn, terminalValu\ e, rest)) : fn(first, foldTreeWith(fn, terminalValue, rest)); — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01952))_
- **const** arraySum = (array) => { **let** sum = 0; **for** ( **let** i = 0; i < array.length; ++i) { sum += array[i]; } **return** sum } arraySum([1, 4, 9, 16, 25]) _//=> 55_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01962))_
- Once again, we’re mixing the code for iterating over an array with the code for calculating a sum. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01963))_
- **const** arraySum = (array) => { **let** done, sum = 0, i = 0; **while** ((done = i == array.length, !done)) { **const** value = array[i++]; sum += value; } **return** sum } arraySum([1, 4, 9, 16, 25]) _//=> 55_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01965))_
- **const** arraySum = (array) => { **let** iter, sum = 0, index = 0; **while** ( (eachIteration = { done: index === array.length, value: index < array.length ? array[index] : **undefined** }, ++index, !eachIteration.done) ) { sum += eachIteration.value; } **return** sum; } arraySum([1, 4, 9, 16, 25]) — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01969))_
- **const** arrayIterator = (array) => { **let** i = 0; **return** () => { **const** done = i === array.length; **return** { done, value: done ? **undefined** : array[i++] } } } **const** iteratorSum = (iterator) => { **let** eachIteration, sum = 0; **while** ((eachIteration = iterator(), !eachIterati — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01971))_
- **const** EMPTY = **null** ; **const** isEmpty = (node) => node === EMPTY; **const** pair = (first, rest = EMPTY) => ({first, rest}); **const** list = (...elements) => { **const** [first, ...rest] = elements; **return** elements.length === 0 ? EMPTY : pair(first, list(...rest)) } **const** print = ( — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01978))_
- **return** { done, value: first } } } **const** iteratorSum = (iterator) => { **let** eachIteration, sum = 0;; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01981))_
- **const** FibonacciIterator = () => { **let** previous = 0, current = 1; **return** () => { **const** value = current; [previous, current] = [current, current + previous]; **return** {done: **false** , value}; }; }; **const** fib = FibonacciIterator() fib().value _//=> 1_ fib().value _//=> 1_ fib(). — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01994))_
- **const** mapIteratorWith = (fn, iterator) => () => { **const** {done, value} = iterator(); **return** ({done, value: done ? **undefined** : fn(value)}); } **const** squares = mapIteratorWith((x) => x * x, NumberIterator(1)); squares().value _//=> 1_ squares().value — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-01997))_
- Let’s introduce an idea: A function that takes an iterator and returns another iterator. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02001))_
- **const** take = (iterator, numberToTake) => { **let** count = 0; **return** () => { **if** (++count <= numberToTake) { **return** iterator(); } **else** { **return** {done: **true** }; } }; }; **const** toArray = (iterator) => { **let** eachIteration, array = []; **while** ((eachIteration = iterato — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02002))_
- **const** odds = () => { **let** number = 1; **return** () => { **const** value = number; number += 2; **return** {done: **false** , value}; } } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02006))_
- **const** filterIteratorWith = (fn, iterator) => () => { **do** { **const** {done, value} = iterator(); } **while** (!done && !fn(value)); **return** {done, value}; } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02010))_
- We haven’t written anything that finds the first element of an iteration that meets a certain criteria. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02016))_
- So as you traverse the new decorator, you’re changing the state of the original! — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02024))_
- To Mock a Mockingbird[76] established the metaphor of songbirds for the combinators, and ever since then logicians have called the K combinator a “kestrel,” the B combinator a “bluebird,” and so forth. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02042))_
- > 76http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422 — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02045))_
- Very simple, but useful. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02056))_
- Now we’ll take it one more step forward: Passing a value to K gets a function back, and passing a value to that function gets us a value. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02056))_
- Now, an interesting thing happens when we pass functions to each other. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02061))_
- From what we just wrote, K(x)(y) => x So K(I)(x) => I. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02061))_
- Given two values, K(I) always returns the _second_ value. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02067))_
- You pass the data to these functions, and they extract it. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02085))_
- But the first and second we built out of K and I don’t work that way. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02086))_
- You call them and pass them the bits, and they choose what to return. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02086))_
- And instead of passing latin to first or second, we pass first or second to latin. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02093))_
- It’s _exactly backwards_ of the way we write functions that operate on data. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02093))_
- For arrays, we’d write cons = (first, second) => [first, second]. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02095))_
- For “data” we access with K and K(I), our “structure” is the function (selector) => selector("primus")("secundus"). Let’s extract those into parameters: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02096))_
- Without arrays, and without objects, just with functions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02115))_
- Armed with nothing more than K, I, and V, we can make a little data structure that holds two values, the cons cell of Lisp and the node of a linked list. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02115))_
- We’d better try it out to check. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02115))_
- **const** first = ({first, rest}) => first, rest = ({first, rest}) => rest, pair = (first, rest) => ({first, rest}), EMPTY = ({}); **const** l123 = pair(1, pair(2, pair(3, EMPTY))); first(l123) _//=> 1_ first(rest(l123)) _//=> 2_ first(rest(rest(l123))) _//=3_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02118))_
- Can we do the same with the linked lists we build out of functions? Yes: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02126))_
- _//=> 2_ **return** l123(rest)(rest)(first) _//=> 3_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02130))_
- **const** length = (aPair) => aPair === EMPTY ? 0 : 1 + length(aPair(rest)); length(l123) _//=> 3_ And mapWith? **const** reverse = (aPair, delayed = EMPTY) => aPair === EMPTY ? delayed : reverse(aPair(rest), pair(aPair(first))(delayed)); **const** mapWith = (fn, aPair, delayed = EMPTY) => aPair === — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02132))_
- But without building our way up to something insane like writing a JavaScript interpreter using JavaScript functions and no other data structures, let’s take things another step in a slightly different direction. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02136))_
- Instead of writing length(list) and examining a list, we’ll write something like: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02142))_
- **const** pairFirst = K, pairRest = K(I), pair = V; **const** first = (list) => list( () => "ERROR: Can't take first of an empty list", (aPair) => aPair(pairFirst) ); **const** rest = (list) => list( — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02145))_
- () => "ERROR: Can't take first of an empty list", (aPair) => aPair(pairRest) ); **const** length = (list) => list( () => 0, (aPair) => 1 + length(aPair(pairRest))) ); — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02148))_
- Let’s start with the obvious. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02151))_
- And what is a node of a list? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02153))_
- **const** reverse = (list, delayed = EMPTYLIST) => list( () => delayed, (aPair) => reverse(aPair(pairRest), node(aPair(pairFirst))(delayed)) ); print(reverse(l123)); _//=> 3 2 1_ **const** mapWith = (fn, list, delayed = EMPTYLIST) => list( () => reverse(delayed), (aPair) => mapWith(fn, aPair(pairRes — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02161))_
- Deeply important, but not practical when you’re building a bridge. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02168))_
- It’s the QED of physics that underpins the Maxwell’s Equations of programming. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02168))_
- So what _is_ interesting about this? What nags at our brain as we’re falling asleep after working our way through this? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02174))_
- The same thing happens with our lists. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02185))_
- We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02190))_
- The line node === EMPTY presumes a lot of things. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02195))_
- - And instead of testing some property of an entity and making a choice of our own with ?: (or if), pass the entity the work we want done for each case and let it test itself. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02199))_
- This recipe isn’t for map: It’s for mapWith, a function that wraps around map and turns any other function into a mapper. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02216))_
- mapWith differs from map in two ways. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02218))_
- It also “curries” the function: Instead of taking two arguments, it takes one argument and returns a function that takes another argument. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02218))_
- It reverses the arguments, taking the function first and the list second. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02218))_
- It’s the same idea, after all. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02223))_
- Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02231))_
- Looking at this, we see we’re conflating two separate transformations. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02242))_
- First, we’re reversing the order of arguments. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02242))_
- Second, we’re “currying” the function so that instead of defining a function that takes two arguments, it returns a function that takes the first argument and returns a function that takes the second argument and applies them both, like this: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02244))_
- Let’s return to the implementation of mapWith that relies on a map function rather than a method: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02246))_
- We’re going to extract these two operations by refactoring our function to paramaterize map. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02248))_
- **const** flip = (fn) => **function** (first, second) { **if** (arguments.length === 2) { **return** fn(second, first); } **else** { **return function** (second) { **return** fn(second, first); }; }; }; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02267))_
- **const** flipAndCurry = (fn) => (first) => **function** (second) { **return** fn.call( **this** , second, first); } **const** flip = (fn) => **function** (first, second) { **return** fn.call( **this** , second, first); } **const** flip = (fn) => **function** (first, second) { **if** (arguments.leng — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02273))_
- **for** ( **let** fruit **in** shipment) { inventory[fruit] = shipment[fruit] } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02281))_
- _//=> { apples: 12, // oranges: 12, // bananas: 54, // pears: 24 }_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02288))_
- **const** Queue = **function** () { **this** .array = []; **this** .head = 0; **this** .tail = -1 }; Queue.prototype.pushTail = **function** (value) { _// ..._ }; Queue.prototype.pullHead = **function** () { _// ..._ }; Queue.prototype.isEmpty = **function** () { _// ..._ } Into this: **const** Queu — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02290))_
- Assigning properties from one object to another (also called “cloning” or “shallow copying”) is a basic building block that we will later use to implement more advanced paradigms like mixins. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02295))_
- This is the canonical Y Combinator[86] : — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02300))_
- **const** factorial = Y( **function** (fac) { **return function** (n) { **return** (n == 0 ? 1 : n * fac(n - 1)); } }); factorial(5) _//=> 120_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02303))_
- Use it as an excuse to get familiar with your environment’s debugging facility. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02306))_
- Work things out for yourself! — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02311))_
- For example, the escape sequence \n inserts a newline character in a string literal, like this: 'first line\nsecond line'. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02320))_
- Quasi-literals go much further. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02328))_
- > 87https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02333))_
- Like any other expression, quasi-literals are evaluated _late_ , when that line or lines of code is evaluated. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02342))_
- Sometimes you just want to move the box around. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02363))_
- Things like “put a label on every bag of coffee in this box,” Or, “Open the box, take out the bags of decaf, and make a new box with just the decaf.” Or, “go through the bags in this box, and take out the first one marked ‘Espresso’ that contains at least 454 grams of beans.” — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02364))_
- All of these actions involve going through the contents one by one. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02365))_
- **const** Stack1 = () => ({ array:[], index: -1, push (value) { **return this** .array[ **this** .index += 1] = value; }, pop () { **const** value = **this** .array[ **this** .index]; **this** .array[ **this** .index] = **undefined** ; **if** ( **this** .index >= 0) { **this** .index -= 1 } **return — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02370))_
- The way we’ve written .iterator as a method, each object knows how to return an iterator for itself. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02374))_
- Since JavaScript doesn’t bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02376))_
- We can use it with our stack: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02381))_
- **const** Stack2 = () => ({ array: [], index: -1, push (value) { **return this** .array[ **this** .index += 1] = value; }, pop () { **const** value = **this** .array[ **this** .index]; **this** .array[ **this** .index] = **undefined** ; **if** ( **this** .index >= 0) { **this** .index -= 1 } **retur — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02401))_
- **const** Stack3 = () => ({ array: [], index: -1, push (value) { **return this** .array[ **this** .index += 1] = value; }, pop () { **const** value = **this** .array[ **this** .index]; **this** .array[ **this** .index] = **undefined** ; **if** ( **this** .index >= 0) { **this** .index -= 1 } **retur — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02420))_
- Using [Symbol.iterator] instead of .iterator seems like adding an extra moving part for nothing. Do we get anything in return? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02427))_
- **for** ( **const** num **of** iterable) { sum += num; } **return** sum } iterableSum(stack) _//=> 2015_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02430))_
- **const** EMPTY = { isEmpty: () => **true** }; **const** isEmpty = (node) => node === EMPTY; **const** Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { **return false** }, [Symbol.iterator] () { **let** currentPair = **this** ; **return** { next () { **if** (currentPair.isEmpty()) { **r — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02434))_
- One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02444))_
- **for** ( **const** i **of** abc) { console.log(i) } _//=>_ a b c — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02459))_
- **for** ( **const** i **of** abc) { console.log(i) } _//=>_ a b c — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02460))_
- **const** RandomNumbers = { [Symbol.iterator]: () => ({ next () { **return** {value: Math.random()}; } }) } **for** ( **const** i **of** RandomNumbers) { console.log(i) } _//=>_ 0.494052127469331 0.835459444206208 0.1408337657339871 ... — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02464))_
- **for** ( **const** i **of** RandomNumbers) { console.log(i) } _//=>_ 0.7845381607767195 0.4956772483419627 0.20259276474826038 ... — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02465))_
- It’s the same idea, after all. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02470))_
- **const** mapWith = (fn, collection) => ({ [Symbol.iterator] () { **const** iterator = collection[Symbol.iterator](); **return** { next () { **const** {done, value} = iterator.next(); **return** ({done, value: done ? **undefined** : fn(value)}); } } } }); — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02473))_
- **for** ( **const** i **of** Evens) { console.log(i) } _//=>_ 0 2 4 ... **for** ( **const** i **of** Evens) { console.log(i) } _//=>_ 0 2 4 ... — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02477))_
- We invoke mapWith((x) => 2 * x, Numbers) and get Evens. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02480))_
- **const** Evens = { [Symbol.iterator] () { **const** iterator = Numbers[Symbol.iterator](); **return** { next () { **const** {done, value} = iterator.next(); **return** ({done, value: done ? **undefined** : 2 *value}); } } } }; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02481))_
- Every time we write for (const i of Evens), JavaScript calls Evens[Symbol.iterator](). — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02482))_
- So we call it a _collection operation_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02483))_
- **for** ( **const** i **of** ZeroesToNines) { console.log(i) } _//=>_ 5 1 9 ... — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02486))_
- **for** ( **const** i **of** ZeroesToNines) { console.log(i) } _//=>_ 3 — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02487))_
- **const** filterWith = (fn, iterable) => ({ [Symbol.iterator] () { **const** iterator = iterable[Symbol.iterator](); **return** { next () { **do** { **const** {done, value} = iterator.next(); } **while** (!done && !fn(value)); **return** {done, value}; } } } }); **const** untilWith = (fn, iterable)  — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02493))_
- **const** Squares = mapWith((x) => x * x, Numbers); **const** EndWithOne = filterWith((x) => x % 10 === 1, Squares); **const** UpTo1000 = untilWith((x) => (x > 1000), EndWithOne); — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02498))_
- **for** ( **let** element **of** iterable) { stack.push(element); } **return** stack; } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02513))_
- **return** done ? EMPTY : Pair1(value, iterationToList(iteration)); })(iterable[Symbol.iterator]()) — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02515))_
- Let’s consider how they work. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02531))_
- **const** Numbers = { [Symbol.iterator]: () => { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } }; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02535))_
- The Numbers iterable returns an object that updates a mutable variable, n, to deliver number after number. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02536))_
- It waits until given a request, and then it returns exactly one item. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02537))_
- Then it waits for the next request. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02537))_
- Well, we’ve written our iterator as a _server_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02537))_
- **while** ( **true** ) { console.log(n++) } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02540))_
- Let’s put that beside the code for the iterator, minus the iterable scaffolding: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02541))_
- _// Iteration_ **let** n = 0; () => ({done: **false** , value: n++}) _// Generation_ **let** n = 0; **while** ( **true** ) { console.log(n++) } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02542))_
- They’re of approximately equal complexity. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02545))_
- For example, iterating over a tree. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02548))_
- **const** generate = (iterable) => { **for** ( **let** element **of** iterable) { **if** (isIterable(element)) { generate(element) } **else** { console.log(element) } } } generate([1, [2, [3, 4], 5]]) _//=>_ 1 2 3 4 5 — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02550))_
- Now for the iteration version. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02551))_
- We’ll write a functional iterator to keep things simple, but it’s easy to see the shape of the basic problem: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02551))_
- _// Iteration_ **const** isIterable = (something) => !!something[Symbol.iterator]; **const** treeIterator = (iterable) => { **const** iterators = [ iterable[Symbol.iterator]() ]; **return** () => { **while** (!!iterators[0]) { **const** iterationResult = iterators[0].next(); **if** (iterationResult. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02554))_
- Let’s revisit the Fibonacci sequence. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02560))_
- _// Iteration_ **let** a, b, state = 0; **const** fibonacci = () => { **switch** (state) { **case** 0: state = 1; **return** a = 0; **case** 1: state = 2; **return** b = 1; **case** 2: [a, b] = [b, a + b]; **return** b } }; **while** ( **true** ) { console.log(fibonacci()); } _//=>_ 0 1 1 2 3 5 8 13 — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02581))_
- Not a fat arrow. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02592))_
- Not a plain function. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02592))_
- We declare the function using the function * syntax. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02592))_
- We “yield” values using the yield keyword. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02593))_
- We don’t return values or output them to console.log. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02593))_
- We call its .next() method, but it’s done immediately. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02598))_
- > 91We wrote a _generator declaration_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02600))_
- **function** * only (something) { **yield** something; }; only("you").next() _//=>_ {"done": **false** , value: "you"} — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02603))_
- It yields the value of something, and then it’s done. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02608))_
- iterator.next() _//=>_ {"done": **false** , value: 1} iterator.next() _//=>_ {"done": **false** , value: 2} iterator.next() _//=>_ {"done": **false** , value: 3} iterator.next() _//=>_ {"done": **true** } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02616))_
- We call oneTwoThree() and get an iterator. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02618))_
- 4. The body of our generator runs until it returns, ends, or encounters a yield statement, which is yield 1;. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02623))_
- - The iterator _suspends its execution_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02624))_
- - The iterator wraps 1 in {done: false, value: 1} and returns that from the call to .next(). — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02625))_
- 5. The body of our generator runs until it returns, ends, or encounters the next yield statement, which is yield 2;. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02628))_
- - The iterator _suspends its execution_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02629))_
- - The iterator wraps 2 in {done: false, value: 2} and returns that from the call to .next(). — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02630))_
- 6. The body of our generator runs until it returns, ends, or encounters the next yield statement, which is yield 3;. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02633))_
- - The iterator _suspends its execution_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02634))_
- - The iterator wraps 3 in {done: false, value: 3} and returns that from the call to .next(). — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02635))_
- - The iterator returns {done: true} from the call to .next(), and every call to this iterator’s .next() method will return {done: true} from now on. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02639))_
- it “suspends” and the producer starts running. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02646))_
- When the producer yields a value, the producer suspends and the consumer starts running, taking the value from the result of calling .next(). — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02646))_
- **const** oneTwoThree = **function** () { **let** state = 'newborn'; **return** { next () { **switch** (state) { **case** 'newborn': state = 1; **return** {value: 1}; **case** 1: state = 2; **return** {value: 2} **case** 2: state = 3; **return** {value: 3} **case** 3: **return** {done: **true** }; } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02648))_
- It’s a function that returns an iterator when we invoke it. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02651))_
- **const** ThreeNumbers = { [Symbol.iterator]: **function** * () { **yield** 1; **yield** 2; **yield** 3 } } **for** ( **const** i **of** ThreeNumbers) { console.log(i); } _//=>_ 1 2 3 [...ThreeNumbers] _//=>_ [1,2,3] — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02655))_
- iterator.next() _//=>_ {"done": **false** , value: 1} iterator.next() _//=>_ {"done": **false** , value: 2} iterator.next() _//=>_ {"done": **false** , value: 3} iterator.next() _//=>_ {"done": **true** } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02657))_
- Now we can use it in a for...of loop, spread it into an array literal, or spread it into a function invocation, because we have written an iterable that uses a generator to return an iterator from its [Symbol.iterator] method. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02658))_
- **const** Numbers = { *[Symbol.iterator] () { **let** i = 0; **while** ( **true** ) { **yield** i++; } } }; **for** ( **const** i **of** Numbers) { console.log(i); } _//=>_ 0 1 2 3 4 5 6 7 — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02668))_
- **const** Fibonacci = { [Symbol.iterator]: () => { **let** a = 0, b = 1, state = 0; **return** { next: () => { **switch** (state) { **case** 0: state = 1; **return** {value: a}; **case** 1: state = 2; **return** {value: b}; **case** 2: [a, b] = [b, a + b]; **return** {value: b}; } } } } }; **for** ( — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02673))_
- 21 34 55 89 144 ... — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02676))_
- **const** Fibonacci = { *[Symbol.iterator] () { **let** a, b; **yield** a = 0; **yield** b = 1; **while** ( **true** ) { [a, b] = [b, a + b] **yield** b; } } } **for** ( **const** i **of** Fibonacci) { console.log(i); } _//=>_ 0 1 1 2 3 5 8 13 21 34 55 89 144 ... — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02678))_
- Of course, we could just as easily write a generator function for Fibonacci numbers: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02682))_
- **function** * fibonacci () { **let** a, b; **yield** a = 0; **yield** b = 1; **while** ( **true** ) { [a, b] = [b, a + b] **yield** b; } } **for** ( **const** i **of** fibonacci()) { console.log(i); } _//=>_ 0 1 1 2 3 5 8 13 21 34 55 89 144 ... — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02683))_
- Here’s a first crack at a function that returns an iterable object for iterating over trees: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02685))_
- **const** isIterable = (something) => !!something[Symbol.iterator]; **const** TreeIterable = (iterable) => ({ [Symbol.iterator]: **function** * () { **for** ( **const** e **of** iterable) { **if** (isIterable(e)) { **for** ( **const** ee **of** TreeIterable(e)) { **yield** ee; } } **else** { **yield — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02688))_
- We’ve gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02689))_
- **function** * tree (iterable) { **for** ( **const** e **of** iterable) { **if** (isIterable(e)) { **for** ( **const** ee **of** tree(e)) { **yield** ee; } } **else** { **yield** e; } } }; **for** ( **const** i **of** tree([1, [2, [3, 4], 5]])) { console.log(i); } _//=>_ 1 2 3 4 5 — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02693))_
- JavaScript handles the recursion for us using its own execution stack. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02695))_
- **for** ( **const** ee **of** tree(e)) { **yield** ee; } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02697))_
- **function** * append (...iterables) { **for** ( **const** iterable **of** iterables) { **for** ( **const** element **of** iterable) { **yield** element; } } } **const** lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\ "]); — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02701))_
- **for** ( **const** word **of** lyrics) { console.log(word); } _//=>_ a b c one two three **do** re me — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02702))_
- append iterates over a collection of iterables, one element at a time. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02703))_
- Tucked inside of it is the same three-line idiom for yielding each element of an iterable. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02704))_
- **function** * append (...iterables) { **for** ( **const** iterable **of** iterables) { **yield** * iterable; } } **const** lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\ "]); **for** ( **const** word **of** lyrics) { console.log(word); } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02705))_
- yield * yields all of the elements of an iterable, in order. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02709))_
- **const** isIterable = (something) => !!something[Symbol.iterator]; **function** * tree (iterable) { **for** ( **const** e **of** iterable) { **if** (isIterable(e)) { **yield** * tree(e); } **else** { **yield** e; } } }; **for** ( **const** i **of** tree([1, [2, [3, 4], 5]])) { console.log(i); } _// — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02710))_
- **const** mapWith = (fn, iterable) => ({ [Symbol.iterator]: () => { **const** iterator = iterable[Symbol.iterator](); **return** { next: () => { **const** {done, value} = iterator.next(); **return** ({done, value: done ? **undefined** : fn(value)}); } } } }); — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02716))_
- **function** * mapWith (fn, iterable) { **for** ( **const** element **of** iterable) { **yield** fn(element); } } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02718))_
- **function** * mapWith(fn, iterable) { **for** ( **const** element **of** iterable) { **yield** fn(element); } } **function** * filterWith (fn, iterable) { **for** ( **const** element **of** iterable) { **if** (!!fn(element)) **yield** element; } } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02721))_
- **function** * untilWith (fn, iterable) { **for** ( **const** element **of** iterable) { **if** (fn(element)) **break** ; **yield** fn(element); } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02724))_
- Each collection knew how to map itself (.map), how to fold itself (.reduce), how to filter itself (.filter) and how to find one element within itself (.find). — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02739))_
- Over time, this informal “interface” for collections grows by accretion. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02740))_
- But our objects grow fatter and fatter. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02740))_
- **const** extend = **function** (consumer, ...providers) { **for** ( **let** i = 0; i < providers.length; ++i) { **const** provider = providers[i]; **for** ( **let** key **in** provider) { **if** (provider.hasOwnProperty(key)) { consumer[key] = provider[key] } } } **return** consumer }; **const** La — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02749))_
- }, filter(fn) { **return** Object.assign({ [Symbol.iterator]: () => { **const** iterator = **this** [Symbol.iterator](); **return** { next: () => { **do** { **const** { done, value } = iterator.next(); } **while** (!done && !fn(value)); **return** { done, value }; } } } }, LazyCollection) }, find(fn — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02752))_
- }, LazyCollection) }, until(fn) { **return** Object.assign({ [Symbol.iterator]: () => { **const** iterator = **this** [Symbol.iterator](); **return** { next: () => { **let** { done, value } = iterator.next(); done = done || fn(value); **return** ({ done, value: done ? **undefined** : value }); } } } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02755))_
- [Symbol.iterator]: () => { **const** iterator = **this** [Symbol.iterator](); **let** remainingElements = numberToTake; **return** { next: () => { **let** { done, value } = iterator.next(); done = done || remainingElements-- <= 0; **return** ({ done, value: done ? **undefined** : value }); } } } },  — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02758))_
- **const** Numbers = Object.assign({ [Symbol.iterator]: () => { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } }, LazyCollection); — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02760))_
- **const** Pair = (car, cdr = EMPTY) => Object.assign({ car, cdr, isEmpty: () => **false** , [Symbol.iterator]: **function** () { **let** currentPair = **this** ; **return** { next: () => { **if** (currentPair.isEmpty()) { **return** {done: **true** } } **else** { **const** value = currentPair.car; c — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02767))_
- **return** done ? EMPTY : Pair(value, iterationToList(iteration)); })(iterable[Symbol.iterator]()); — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02768))_
- Both expressions evaluate to 220. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02781))_
- But it’s still illustrative to dissect something important: Array’s .map and .filter methods gather their results into new arrays. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02782))_
- This reduces the memory footprint. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02783))_
- Whereas the .map and .filter methods on Pair work with iterators. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02783))_
- Stack.from([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) .map((x) => { console.log(`squaring **${** x **}** `); **return** x * x }) .filter((x) => { console.log(`filtering **${** x **}** `); **return** x % 2 == 0 }) .first() _//=>_ s — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02791))_
- squaring 28 squaring 29 filtering 0 filtering 1 filtering 4 ... — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02795))_
- Arrays copy-on-read, so every time we perform a map or filter, we get a new array and perform all the computations. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02796))_
- **const** Numbers = Object.assign({ [Symbol.iterator]: () => { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } }, LazyCollection); **const** firstCubeOver1234 = Numbers .map((x) => x * x * x) .filter((x) => x > 1234) .first() _//=> 1331_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02800))_
- Balanced against their flexibility, our “lazy collections” use structure sharing. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02801))_
- **const** extend = **function** (consumer, ...providers) { **for** ( **let** i = 0; i < providers.length; ++i) { **const** provider = providers[i]; **for** ( **let** key **in** provider) { **if** (provider.hasOwnProperty(key)) { consumer[key] = provider[key] } } } **return** consumer }; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02804))_
- **const** EagerCollection = (gatherable) => ({ map(fn) { **const** original = **this** ; **return** gatherable.from( ( **function** * () { **for** ( **let** element **of** original) { **yield** fn(element); } })() ); }, reduce(fn, seed) { **let** accumulator = seed; **for** ( **let** element **of th — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02807))_
- **const** original = **this** ; **return** gatherable.from( ( **function** * () { **for** ( **let** element **of** original) { **if** (fn(element)) **break** ; **yield** element; } })() ); }, first() { **return this** [Symbol.iterator]().next().value; }, rest() { **const** iteration = **this** [Symb — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02810))_
- **const** EMPTY = { isEmpty: () => **true** }; **const** isEmpty = (node) => node === EMPTY; **const** Pair = (car, cdr = EMPTY) => Object.assign({ car, cdr, isEmpty: () => **false** , [Symbol.iterator]: **function** () { **let** currentPair = **this** ; **return** { next: () => { **if** (currentPai — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02814))_
- “Win, win” he thought to himself. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02829))_
- On each square, we randomly place an arrow pointing to one of its four sides. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02835))_
- Consider a finite checkerboard of unknown size. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02835))_
- A player moves the chequer, following the rules. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02836))_
- As the player moves the chequer, they calls out the direction of movement, e.g. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02836))_
- _// initialize the board_ **const** board = []; **for** ( **let** i = 0; i < size; ++i) { board[i] = []; **for** ( **let** j = 0; j < size; ++j) { board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)]; } } _// initialize the position_ **let** initialPosition = [ 2 + Math.floor(Math.random() * (size -  — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02845))_
- “What,” Christine asked, “Do you write in place of the three // ??? placeholders to determine whether the game halts?” — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02848))_
- And just as companies often pick a problem that gives them broad latitude for discussing alternate approaches and determining that depth of a candidate’s experience, The Carpenter liked to sketch out solutions that provided an opportunity to judge the interviewer’s experience and provide an easy exc — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02851))_
- **const** MOVE = { "￿": ([x, y]) => [x - 1, y], "￿": ([x, y]) => [x + 1, y], "￿": ([x, y]) => [x, y + 1], "￿": ([x, y]) => [x, y - 1] }; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02854))_
- _// initialize the board_ **const** board = []; **for** ( **let** i = 0; i < size; ++i) { board[i] = []; **for** ( **let** j = 0; j < size; ++j) { board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)]; } } _// initialize the position_ **const** position = [ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02856))_
- Math.floor(Math.random() * size), Math.floor(Math.random() * size) ]; **return** {board, position}; }; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02859))_
- **const** size = board[0].length; **return** ({ *[Symbol.iterator] () { **let** [x, y] = position; **while** (x >= 0 && y >=0 && x < size && y < size) { **const** direction = board[y][x]; **yield** direction; [x, y] = MOVE[direction]([x, y]); } } }); }; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02861))_
- “We want to take the arrows and convert them to positions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02862))_
- For that, we’ll map the Game iterable to positions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02862))_
- **const** statefulMapWith = (fn, seed, iterable) => ({ *[Symbol.iterator] () { **let** value, state = seed; **for** ( **let** element **of** iterable) { [state, value] = fn(state, element); **yield** value; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02864))_
- **const** positionsOf = (game) => statefulMapWith( (position, direction) => { **const** [x, y] = MOVE[direction](position); position = [x, y]; **return** [position, `x: **${** x **}** , y: **${** y **}** `]; }, [0, 0], game); — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02869))_
- **if** (hareResult.done) { **return false** ; } **if** (tortoiseValue === hareResult.value) { **return true** ; } hareResult = hare.next(); — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02882))_
- **if** (hareResult.done) { **return false** ; } **if** (tortoiseValue === hareResult.value) { **return true** ; } } **return false** ; }; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02883))_
- terminates(Game({board: test, position: [0, 0]})) _//=> false_ terminates(Game({board: test, position: [3, 0]})) _//=> true_ terminates(Game({board: test, position: [0, 3]})) _//=> false_ terminates(Game({board: test, position: [3, 3]})) _//=> false_ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02891))_
- It also cleanly separates the mechanics of the game from the algorithm for detecting cycles in a graph.” — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02892))_
- The Carpenter never did hear back from them, but the next day there was an email containing a generous contract from Friends of Ghosts (“FOG”), a codename for a stealth startup doing interesting work, and the Thing interview was forgotten. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02898))_
- Some time later, The Carpenter ran into Bob Plissken at a local technology meet-up. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02899))_
- would say was, _Writes unreadable code_ . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02902))_
- You’re essentially calling for the player to clone themselves and call out the directions in parallel.” — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02912))_
- The Carpenter thought about this for a moment. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02913))_
- “Kidu, you’re right, that’s a fantastic observation. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02913))_
- _// implements Teleporting Tortoise // cycle detection algorithm._ **const** hasCycle = (iterable) => { **let** iterator = iterable[Symbol.iterator](), teleportDistance = 1; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02914))_
- **while** ( **true** ) { **let** {value, done} = iterator.next(), tortoise = value; **if** (done) **return false** ; **for** ( **let** i = 0; i < teleportDistance; ++i) { **let** {value, done} = iterator.next(), hare = value; **if** (done) **return false** ; **if** (tortoise === hare) **return true* — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02915))_
- **for** ( **let** element **of** orderedCollection) { **if** (visited.has(element)) { **return true** ; } visited.add(element); } **return false** ; }; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02920))_
- Consider, for example, the moves in a game. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02929))_
- To save space, we’ll ignore rotations and reflections, and we’ll model the first player’s moves as a stream. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02930))_
- o | | ---+---+--| | ---+---+--| | — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02935))_
- o | 1 | 2 ---+---+--| 4 | 5 ---+---+--| | 8 — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02937))_
- Let’s consider move 1. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02938))_
- o | x | ---+---+--| | ---+---+--| | — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02939))_
- o | x | ---+---+--| | ---+---+--o | | — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02941))_
- o | x | 2 ---+---+--3 | 4 | 5 ---+---+--o | 7 | 8 — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02943))_
- For 2, 4, 5, 7, or 8, we play 3 and win. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02944))_
- o | x | ---+---+--x | | ---+---+--o | | o — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02947))_
- o | x | 2 ---+---+--x | 4 | 5 ---+---+--x | 7 | 8 — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02949))_
- If x plays anything else, including 7, we play 4 and win. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02950))_
- If x plays 4, we play 7 and win. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02950))_
- We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02952))_
- o | x | ---+---+--x | | ---+---+--o | | — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02953))_
- o | x | ---+---+--x | | ---+---+--o | | o — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02955))_
- o | x | ---+---+--| x | ---+---+--o | | — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02959))_
- o | x | ---+---+--o | x | ---+---+--o | | — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02961))_
- Let’s use an array. So this: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02963))_
- o | x | ---+---+--| | ---+---+--| | — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02964))_
- [ 'o', 'x', ' ', ' ' ' ' ' ' , , , ' ' ' ' ' ' , , ] — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02966))_
- o | x | ---+---+--x | | ---+---+--o | | — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02970))_
- [ 'o', 'x', ' ', 'x', ' ', ' ', 'o', ' ', ' ' ] — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02972))_
- ' ' ' ' ' ' , , , ' ' ' ' ' ' , , , ' ' ' ' ' ' , , ]]: 0, [[ — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02975))_
- 'o', 'x', ' ', ' ' ' ' ' ' , , , ' ' ' ' ' ' , , ]]: 6, [[ 'o', 'x', 'x', ' ' ' ' ' ' , , , 'o', ' ', ' ' ]]: 3, [[ 'o', 'x', ' ', 'x', ' ', ' ', 'o', ' ', ' ' ]]: 8, [[ 'o', 'x', ' ', ' ', 'x', ' ', 'o', ' ', ' ' — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02976))_
- ]]: 3, [[ 'o', 'x', ' ', ' ', ' ', 'x', 'o', ' ', ' ' ]]: 3, [[ 'o', 'x', ' ', ' ' ' ' ' ' , , , 'o', 'x', ' ' ]]: 3, [[ 'o', 'x', ' ', ' ' ' ' ' ' , , , 'o', ' ', 'x' ]]: 3 — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02979))_
- { "o,x, , , , , , , ":6, "o,x,x, , , ,o, , ":3, "o,x, ,x, , ,o, , ":8, "o,x, , ,x, ,o, , ":3, "o,x, , , ,x,o, , ":3, "o,x, , , , ,o,x, ":3, "o,x, , , , ,o, ,x":3 } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02983))_
- Our statelessNaughtsAndCrosses function pushes the work of tracking the game’s state onto us, the player. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-02994))_
- **const** statefulNaughtsAndCrosses = () => { **const** state = [ ' ' ' ' ' ' , , , ' ' ' ' ' ' , , , ' ' ' ' ' ' , , ]; **return** (x = **false** ) => { **if** (x) { — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03001))_
- **if** (state[x] === ' ') { state[x] = 'x'; } **else throw** "occupied!" } **let** o = moveLookupTable[state]; state[o] = 'o'; **return** o; } }; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03004))_
- We’ve done almost the exact same thing here with our naughts and crosses game. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03014))_
- **function** browserNaughtsAndCrosses () { **const** x1 = parseInt(prompt('o plays 0, where does x play?')); **switch** (x1) { **case** 1: **const** x2 = parseInt(prompt('o plays 6, where does x play?')); **switch** (x2) { **case** 2: **case** 4: **case** 5: **case** 7: **case** 8: alert('o plays 3' — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03018))_
- However, our solution inverts the control. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03020))_
- We aren’t calling our function with moves, it’s calling us. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03020))_
- values while maintaining the implicit state of the generator’s control flow. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03023))_
- If it _was_ possible, how would it work? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03027))_
- **function** * generatorNaughtsAndCrosses () { **const** x1 = **yield** 0; **switch** (x1) { **case** 1: **const** x2 = **yield** 6; **switch** (x2) { **case** 2: **case** 4: **case** 5: **case** 7: **case** 8: **yield** 3; **break** ; **case** 3: **const** x3 = **yield** 8; **switch** (x3) { **case — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03028))_
- } } **break** ; _// ..._ } } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03031))_
- Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn’t call us. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03042))_
- **function** * mapWith(fn, iterable) { **for** ( **const** element **of** iterable) { **yield** fn(element); } } **function** * mapAllWith (fn, iterable) { **for** ( **const** element **of** iterable) { **yield** * fn(element); } } **function** * filterWith (fn, iterable) { **for** ( **const** eleme — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03053))_
- **function** * take (numberToTake, iterable) { **const** iterator = iterable[Symbol.iterator](); — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03058))_
- **while** ( **true** ) { **const** pairs = iterators.map(j => j.next()), dones = pairs.map(p => p.done), values = pairs.map(p => p.value); **if** (dones.indexOf( **true** ) >= 0) **break** ; **yield** values; } }; **function** * zipWith (zipper, ...iterables) { **const** iterators = iterables.map(i  — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03062))_
- **for** ( **const** element **of** iterable) { accumulator = fn(accumulator, element); } **return** accumulator; }; **const** first = (iterable) => iterable[Symbol.iterator]().next().value; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03069))_
- **function** memoize (generator) { **const** memos = {}, iterators = {}; **return function** * (...args) { **const** key = JSON.stringify(args); **let** i = 0; **if** (memos[key] == **null** ) { memos[key] = []; iterators[key] = generator(...args); } **while** ( **true** ) { **if** (i < memos[key].l — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03071))_
- decoration.apply( **this** , arguments); **return** method.apply( **this** , arguments); — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03092))_
- And it would be “transpiled” into: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03102))_
- **var** before = **function** (decoration) { **return function** (method) { **return function** () { **for** ( **let** _len = arguments.length, args = Array(_len), _key = 0; _key < _le\ n; _key++) { args[_key] = arguments[_key]; } decoration.apply( **this** , args); **return** method.apply( **this** — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03103))_
- He writes about programming on “Raganwald[222] ,” as well as general-purpose ruminations on “Braythwayt Dot Com[223] ”. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-83ecb080-03268))_

### Disposition counts

- non-claim: 1246
