---
page_id: javascriptallonge-section-the-golden-crema-appendices-and-afterwords-733effc6
page_kind: source
summary: The Golden Crema: Appendices and Afterwords: 28 source-backed entries and 17 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-golden-crema-appendices-and-afterwords-733effc6@63a0831e2a8cf2a7a20fe551ec372d6d
---

# The Golden Crema: Appendices and Afterwords

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-the-golden-crema-appendices-and-afterwords-how-to-run-the-examples-64b1941d]] - narrower source section: The Golden Crema: Appendices and Afterwords / How to run the examples
- [[javascriptallonge-section-the-golden-crema-appendices-and-afterwords-thanks-81bd2dc9]] - narrower source section: The Golden Crema: Appendices and Afterwords / Thanks!
- [[javascriptallonge-section-the-golden-crema-appendices-and-afterwords-copyright-notice-c27f07a1]] - narrower source section: The Golden Crema: Appendices and Afterwords / Copyright Notice
- [[javascriptallonge-section-the-golden-crema-appendices-and-afterwords-about-the-author-a9b179d5]] - narrower source section: The Golden Crema: Appendices and Afterwords / About The Author

## Statements by subsection

### The Golden Crema: Appendices and Afterwords / How to run the examples

- At the time this book was written, ECMAScript 2015 was not yet widely available. All of the examples in this book were tested using either Google Traceur Compiler 100 , Babel 101 , or both. Traceur and Babel are both transpilers , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics. _(javascriptallonge.pdf (source-range-7239e085-01965))_
- Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser. _(javascriptallonge.pdf (source-range-7239e085-01976))_
- And 4 would appear in your browser's development console. _(javascriptallonge.pdf (source-range-7239e085-01981))_
- You can also install the transpilers on your development system and use them with Node 102 on the command line 103 . The care and feeding of node and npm are beyond the scope of this book, but both tools offer clear instructions for those who have already installed node . _(javascriptallonge.pdf (source-range-7239e085-01982))_
- Traceur and Babel are both transpilers , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics. _(javascriptallonge.pdf (source-range-7239e085-01965))_

### The Golden Crema: Appendices and Afterwords / Thanks! / Daniel Friedman and Matthias Felleisen

- JavaScript Allongé was inspired by The Little Schemer 104 by Daniel Friedman and Matthias Felleisen. But where The Little Schemer's primary focus is recursion, JavaScript Allongé's primary focus is functions as first-class values . _(javascriptallonge.pdf (source-range-7239e085-01988))_

### The Golden Crema: Appendices and Afterwords / Thanks! / Richard Feynman

- Richard Feynman's QED 105 wasanother inspiration: A book that explains Quantum Electrodynamics and the 'Sum of the Histories' methodology using the simple expedient of explaining how light reflects off a mirror, and showing how most of the things we think are happening-such as light travelling on a straight line, the angle of reflection equalling the angle of refraction, or that a beam of light only interacts with a small portion of the mirror, or that it reflects off a plane-are all wrong. And everything is explained in simple, concise terms that build upon each other logically. _(javascriptallonge.pdf (source-range-7239e085-01993))_
- Richard Feynman's QED 105 wasanother inspiration: A book that explains Quantum Electrodynamics and the 'Sum of the Histories' methodology using the simple expedient of explaining how light reflects off a mirror, and showing how most of the things we think are happening-such as light travelling on a straight line, the angle of reflection equalling the angle of refraction, or that a beam of light only interacts with a small portion of the mirror, or that it reflects off a plane-are all wrong. _(javascriptallonge.pdf (source-range-7239e085-01993))_

### The Golden Crema: Appendices and Afterwords / About The Author

- When he's not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to millions of users, Reg 'Raganwald' Braithwaite has authored libraries 221 for JavaScript, CoffeeScript, and Ruby programming such as Allong.es, Method Combinators, Katy, JQuery Combinators, YouAreDaChef, andand, and others. _(javascriptallonge.pdf (source-range-7239e085-02059))_
- When he's not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to millions of users, Reg 'Raganwald' Braithwaite has authored libraries 221 for JavaScript, CoffeeScript, and Ruby programming such as Allong.es, Method Combinators, Katy, JQuery Combinators, YouAreDaChef, andand, and others. _(javascriptallonge.pdf (source-range-7239e085-02059))_

## Technical atoms

### Technical frame 1: The Golden Crema: Appendices and Afterwords

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01962))_

> [Figure] (p.288)

### Technical frame 2: The Golden Crema: Appendices and Afterwords / How to run the examples

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01965))_

> At the time this book was written, ECMAScript 2015 was not yet widely available. All of the examples in this book were tested using either Google Traceur Compiler 100 , Babel 101 , or both. Traceur and Babel are both transpilers , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01967))_

```
const before = (decoration) =>
(method) =>
function () {
decoration.apply(this, arguments);
return method.apply(this, arguments)
};
```

### Technical frame 3: The Golden Crema: Appendices and Afterwords / How to run the examples

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01976))_

> Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01969))_

```
"use strict"
var before = function (decoration) {
return function (method) {
return function () {
decoration.apply(this, arguments);
return method.apply(this, arguments);
};
};
};
```

### Technical frame 4: The Golden Crema: Appendices and Afterwords / How to run the examples

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01976))_

> Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01971))_

> [Figure] (p.289)

### Technical frame 5: The Golden Crema: Appendices and Afterwords / How to run the examples

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01976))_

> Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01974))_

```
100https://github.com
101http://babeljs.io/
```

### Technical frame 6: The Golden Crema: Appendices and Afterwords / How to run the examples

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01976))_

> Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01975))_

```
const before = (decoration) =>
(method) =>
function (...args) {
decoration.apply(this, args);
return method.apply(this, args)
};
And it would be “transpiled” into:
var before = function (decoration) {
return function (method) {
return function () {
for (let _len = arguments.length, args = Array(_len), _key = 0; _key < _le\
n; _key++) {
args[_key] = arguments[_key];
}
decoration.apply(this, args);
return method.apply(this, args);
};
};
};
```

### Technical frame 7: The Golden Crema: Appendices and Afterwords / How to run the examples

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01981))_

> And 4 would appear in your browser's development console.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01978))_

```
(() => 2 + 2)()
```

### Technical frame 8: The Golden Crema: Appendices and Afterwords / How to run the examples

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01981))_

> And 4 would appear in your browser's development console.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01980))_

```
console.log(
(() => 2 + 2)()
)
```

### Technical frame 9: The Golden Crema: Appendices and Afterwords / Thanks! / Daniel Friedman and Matthias Felleisen

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01988))_

> JavaScript Allongé was inspired by The Little Schemer 104 by Daniel Friedman and Matthias Felleisen. But where The Little Schemer's primary focus is recursion, JavaScript Allongé's primary focus is functions as first-class values .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01986))_

> [Figure] (p.291)

### Technical frame 10: The Golden Crema: Appendices and Afterwords / Thanks! / Richard Feynman

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01993))_

> Richard Feynman's QED 105 wasanother inspiration: A book that explains Quantum Electrodynamics and the 'Sum of the Histories' methodology using the simple expedient of explaining how light reflects off a mirror, and showing how most of the things we think are happening-such as light travelling on a straight line, the angle of reflection equalling the angle of refraction, or that a beam of light only interacts with a small portion of the mirror, or that it reflects off a plane-are all wrong. And 

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01991))_

> [Figure] (p.292)

### Technical frame 11: The Golden Crema: Appendices and Afterwords / Copyright Notice

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01996))_

> The original words in this book are (c) 2012-2015, Reginald Braithwaite. All rights reserved.

### Technical frame 12: The Golden Crema: Appendices and Afterwords / Copyright Notice / images

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-02028))_

```
131http://www.flickr.com/photos/33388953@N04/4017985434/
132http://creativecommons.org/licenses/by/2.0/deed.en
133http://www.flickr.com/photos/tangysd/5953453156/
134http://creativecommons.org/licenses/by-sa/2.0/deed.en
135http://www.flickr.com/photos/digitalcolony/4000837035/
136http://creativecommons.org/licenses/by-sa/2.0/deed.en
137http://www.flickr.com/photos/digitalcolony/4309812256/
138http://creativecommons.org/licenses/by-sa/2.0/deed.en
139http://www.flickr.com/photos/bike/3237859728/
140http://creativecommons.org/licenses/by-sa/2.0/deed.en
141http://www.flickr.com/photos/lacerabbit/2102801319/
142http://creativecommons.org/licenses/by-nd/2.0/deed.en
143http://www.flickr.com/photos/nalundgaard/4785922266/
144http://creativecommons.org/licenses/by-sa/2.0/deed.en
145http://www.flickr.com/photos/paulmccoubrie/6828131856/
146http://creativecommons.org/licenses/by-nd/2.0/deed.en
147http://www.flickr.com/photos/mikecogh/7676649034/
148http://creativecommons.org/licenses/by-sa/2.0/deed.en
149http://www.flickr.com/photos/yellowskyphotography/5641003165/
150http://creativecommons.org/licenses/by-sa/2.0/deed.en
151http://www.flickr.com/photos/andynash/6204253236/
152http://creativecommons.org/licenses/by-sa/2.0/deed.en
153http://www.flickr.com/photos/28705377@N04/5306009552/
154http://creativecommons.org/licenses/by/2.0/deed.en
155http://www.flickr.com/photos/shavejonathan/2343081208/
156http://creativecommons.org/licenses/by/2.0/deed.en
157http://www.flickr.com/photos/ilovememphis/7103931235/
158http://creativecommons.org/licenses/by-nd/2.0/deed.en
159http://www.flickr.com/photos/mikecogh/7561440544/
160http://creativecommons.org/licenses/by-sa/2.0/deed.en
161http://www.flickr.com/photos/dtownsend/6171015997/
162http://creativecommons org/licenses/by-sa/2 0/deed en
```

### Technical frame 13: The Golden Crema: Appendices and Afterwords / About The Author / contact

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-02063))_

> [Figure] (p.297)

### Technical atom 14

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01982))_

> You can also install the transpilers on your development system and use them with Node 102 on the command line 103 . The care and feeding of node and npm are beyond the scope of this book, but both tools offer clear instructions for those who have already installed node .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01983))_

| entry | content |
| --- | --- |
| 102 | http://nodejs.org/ |
| 103 | https://en.wikipedia.org/wiki/REPL |

<details>
<summary>Raw table text</summary>

```
102 http://nodejs.org/
103 https://en.wikipedia.org/wiki/REPL
```

</details>

### Technical atom 15

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-02011))_

| entry | content |
| --- | --- |
| 106 | http://www.flickr.com/photos/trumpetca/ http://creativecommons.org/licenses/by/2.0/deed.en |
| 107 | http://www.flickr.com/photos/avlxyz/4907262046 |
| 108 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 109 | http://www.flickr.com/photos/digitalcolony/5054568279/ |
| 110 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 111 | http://www.flickr.com/photos/everydaylifemodern/1353570874/ |
| 112 | http://creativecommons.org/licenses/by-nd/2.0/deed.en |
| 113 | http://www.flickr.com/photos/everydaylifemodern/434299813/ |
| 114 | http://creativecommons.org/licenses/by-nd/2.0/deed.en |
| 115 | http://www.flickr.com/photos/the_rev/2295096211/ |
| 116 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 117 | http://www.flickr.com/photos/thedigitelmyr/6199419022/ |
| 118 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 119 | http://www.flickr.com/photos/sagamiono/4391542823/ |
| 120 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 121 | http://www.flickr.com/photos/digitalcolony/3924227011/ |
| 122 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 123 | http://www.flickr.com/photos/15481483@N06/6231443466/ |
| 124 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 125 | http://www.flickr.com/photos/tjgfernandes/2785677276/ |
| 126 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 127 | http://www.flickr.com/photos/kirstenloza/4805716699/ |
| 128 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 129 | http://www.flickr.com/photos/jenny-pics/5053954146/ 130 |

<details>
<summary>Raw table text</summary>

```
106 http://www.flickr.com/photos/trumpetca/
http://creativecommons.org/licenses/by/2.0/deed.en
107 http://www.flickr.com/photos/avlxyz/4907262046 108 http://creativecommons.org/licenses/by-sa/2.0/deed.en 109 http://www.flickr.com/photos/digitalcolony/5054568279/ 110 http://creativecommons.org/licenses/by-sa/2.0/deed.en 111 http://www.flickr.com/photos/everydaylifemodern/1353570874/ 112 http://creativecommons.org/licenses/by-nd/2.0/deed.en 113 http://www.flickr.com/photos/everydaylifemodern/434299813/ 114 http://creativecommons.org/licenses/by-nd/2.0/deed.en 115 http://www.flickr.com/photos/the_rev/2295096211/ 116 http://creativecommons.org/licenses/by/2.0/deed.en 117 http://www.flickr.com/photos/thedigitelmyr/6199419022/ 118 http://creativecommons.org/licenses/by-sa/2.0/deed.en 119 http://www.flickr.com/photos/sagamiono/4391542823/ 120 http://creativecommons.org/licenses/by-sa/2.0/deed.en 121 http://www.flickr.com/photos/digitalcolony/3924227011/ 122 http://creativecommons.org/licenses/by-sa/2.0/deed.en 123 http://www.flickr.com/photos/15481483@N06/6231443466/ 124 http://creativecommons.org/licenses/by-sa/2.0/deed.en 125 http://www.flickr.com/photos/tjgfernandes/2785677276/ 126 http://creativecommons.org/licenses/by/2.0/deed.en 127 http://www.flickr.com/photos/kirstenloza/4805716699/ 128 http://creativecommons.org/licenses/by/2.0/deed.en 129 http://www.flickr.com/photos/jenny-pics/5053954146/ 130
```

</details>

### Technical atom 16

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-02045))_

| entry | content |
| --- | --- |
| 163 | http://www.flickr.com/photos/93425126@N00/313053257/ |
| 164 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 165 | http://www.flickr.com/photos/digitalcolony/2833809436/ |
| 166 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 167 | http://www.flickr.com/photos/citizenhelder/5006498068/ |
| 168 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 169 | http://www.flickr.com/photos/joncrel/237026246/ |
| 170 | http://creativecommons.org/licenses/by-nd/2.0/deed.en |
| 171 | http://www.flickr.com/photos/nalundgaard/3163852170/ |
| 172 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 173 | http://www.flickr.com/photos/47000103@N05/6525288841/ |
| 174 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 175 | http://www.flickr.com/photos/lotzman/978418891/ |
| 176 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 177 | http://www.flickr.com/photos/kk/sets/72157626168201654/with/5484839102/ |
| 178 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 179 | https://www.flickr.com/photos/kellan/434503323 |
| 180 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 181 | https://www.flickr.com/photos/whitneyinchicago/3835218626 |
| 182 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 183 | https://www.flickr.com/photos/sankarshan/5165312159 |
| 184 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 185 | https://www.flickr.com/photos/candy-s/7619358284 |
| 186 | https://www.flickr.com/photos/candy-s/ |
| 187 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 188 | https://www.flickr.com/photos/lorentey/22193876 |
| 189 | https://www.flickr.com/photos/lorentey/ |
| 190 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 191 | https://www.flickr.com/photos/kk/5484876862 |
| 192 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 193 | https://www.flickr.com/photos/f_mafra/2956649121 194 http://creativecommons.org/licenses/by-sa/2.0/deed.en coffee pots 195 (c) 2009 Jonas Forth Some rights reserved 196 . |
| 5 | Barrel Roaster 197 (c) 2013 David Lytle Some rights reserved 198 . |

<details>
<summary>Raw table text</summary>

```
163 http://www.flickr.com/photos/93425126@N00/313053257/ 164 http://creativecommons.org/licenses/by-sa/2.0/deed.en 165 http://www.flickr.com/photos/digitalcolony/2833809436/ 166 http://creativecommons.org/licenses/by-sa/2.0/deed.en 167 http://www.flickr.com/photos/citizenhelder/5006498068/ 168 http://creativecommons.org/licenses/by/2.0/deed.en 169 http://www.flickr.com/photos/joncrel/237026246/ 170 http://creativecommons.org/licenses/by-nd/2.0/deed.en 171 http://www.flickr.com/photos/nalundgaard/3163852170/ 172 http://creativecommons.org/licenses/by-sa/2.0/deed.en 173 http://www.flickr.com/photos/47000103@N05/6525288841/ 174 http://creativecommons.org/licenses/by-sa/2.0/deed.en 175 http://www.flickr.com/photos/lotzman/978418891/ 176 http://creativecommons.org/licenses/by/2.0/deed.en 177 http://www.flickr.com/photos/kk/sets/72157626168201654/with/5484839102/ 178 http://creativecommons.org/licenses/by-sa/2.0/deed.en 179 https://www.flickr.com/photos/kellan/434503323 180 http://creativecommons.org/licenses/by/2.0/deed.en 181 https://www.flickr.com/photos/whitneyinchicago/3835218626 182 http://creativecommons.org/licenses/by/2.0/deed.en 183 https://www.flickr.com/photos/sankarshan/5165312159 184 http://creativecommons.org/licenses/by-sa/2.0/deed.en 185 https://www.flickr.com/photos/candy-s/7619358284 186 https://www.flickr.com/photos/candy-s/ 187 http://creativecommons.org/licenses/by/2.0/deed.en 188 https://www.flickr.com/photos/lorentey/22193876 189 https://www.flickr.com/photos/lorentey/ 190 http://creativecommons.org/licenses/by/2.0/deed.en 191 https://www.flickr.com/photos/kk/5484876862 192 http://creativecommons.org/licenses/by-sa/2.0/deed.en 193 https://www.flickr.com/photos/f_mafra/2956649121 194
http://creativecommons.org/licenses/by-sa/2.0/deed.en
coffee pots 195 (c) 2009 Jonas Forth Some rights reserved 196 .
5 Barrel Roaster 197 (c) 2013 David Lytle Some rights reserved 198 .
```

</details>

### Technical atom 17

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-02065))_

| entry | content |
| --- | --- |
| 221 | http://github.com/raganwald |
| 223 | http://braythwayt.com |
| 222 | http://raganwald |
| 224 | https://twitter.com/raganwald |
| 225 | mailto:reg@braythwayt.com |

<details>
<summary>Raw table text</summary>

```
221 http://github.com/raganwald
223 http://braythwayt.com
222 http://raganwald
224 https://twitter.com/raganwald
225 mailto:reg@braythwayt.com
```

</details>
