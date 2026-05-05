You are answering a query from the existing LLM-Wiki. Do not edit files.

Question:
What are the key concepts in AoE2 economy?

Use only the supplied wiki pages. If the supplied pages do not cover something, say `not covered in sources`.
Answer concisely and cite the wiki pages you used with relative Markdown links.

Supplied pages:

PAGE: wiki/sources/aoe2-basics.md
TITLE: Noobs guide for AoE2
TYPE: source
CONTENT:
---
title: Noobs guide for AoE2
type: source
source_id: aoe2-basics
source_type: pdf
raw_path: ../../raw/imported/aoe2-basics/
normalized_path: ../../raw/normalized/aoe2-basics/
status: draft
last_updated: 2026-05-03
tags: []
sources: [../../raw/imported/aoe2-basics/original.pdf]
---

# Noobs guide for AoE2

## Summary

This document is an organized arrangement of gameplay concepts simplified and explained out. It is categorized and each category will be written in order from most important to the less important. The author, ptee, is a Finnish player who has been part of the AoE2 community since Jan 2019. He started playing competitively during university studies, improved his skills through practice against AI, and eventually reached around 1700 Elo in DE ladder. The guide is meant to be used in a structured way, focusing on one chapter at a time to fix gameplay issues. It covers foundational concepts, core fundamentals, common edges, and niches of the game, including economy management, unit interactions, map awareness, and team play strategies.

## Key claims

| Claim | Evidence | Locator |
|---|---|---|
| Keeping the town center producing villagers avoids resource losses that grow across the match. | "42 minutes is 2520 seconds and each second a villager at worsts gathers wood at a rate of 0.39 per second." | `normalized:L177` |
| Build orders turn practiced openings into written sequences that reduce villager movement between resources. | "Build orders are this exact thing written out, simplified, tuned into a format where villagers move between resources as little as possible." | `normalized:L189` |
| Build order practice should review idle town center time and unit production timing. | "When you're learning build orders you want to pay attention to your idle TC time and the ability to produce the wanted units as soon as possible." | `normalized:L203` |
| Extensive dark-age walling can delay uptime and hurt the build order. | "walling extensively in dark age will slow down your uptime and hurt your build order significantly." | `normalized:L234` |
| Production buildings can shorten unit travel distance while also helping form walls. | "Similarly stables and ranges should be built in front in order to shorten distance for the units to travel and help with walling." | `normalized:L236` |
| Scouting should look for player resources, enemy activity, and extra map resources. | "what you actually should be doing with the scout is actually looking for your resources, what enemy is doing and where are the extra resources in the map." | `normalized:L260` |
| Later scouting identifies enemy buildings, tech choices, unit lines, and upgrades. | "Later in the game you want to use scouting to know what your opponent is doing, which buildings does he have or what units he is teching into and what sort of upgrades his units have." | `normalized:L268` |
| Economy upgrades can improve resource income without stopping villager production. | "Best thing about these upgrades is that they do not cost TC time, so you do not need to stop producing villagers for them." | `normalized:L288` |
| Economy balance means reducing excess resources so income becomes spent growth or army. | "The less excess you have the better your economy is balanced." | `normalized:L310` |
| Continuous production keeps military buildings from idling after ranges or stables are placed. | "whenever you place down an archery range or stable, ideally it does not ever idle so you can have superior army for contesting map control." | `normalized:L324` |
| Running one archery range continuously requires about four villagers on gold. | "you need 3.5 villagers on gold to run one archery range to produce archers." | `normalized:L326` |
| Lanchester's square law says all-against-all fighting strength scales with the square of group size. | "where combat is all-against-all, fighting strength is proportional to the square of group size" | `normalized:L338` |
| Larger numbers can overcome nominal counter units if the opponent cannot freely kill units. | "you can even win fights against counter units as long as your numbers are high enough." | `normalized:L352` |
| A counter unit must work in the actual situation, not only in theory. | "It counters only on paper but not in actual situation because the opponent can micro." | `normalized:L382` |
| Good castle-age timings depend on low wood count, farms, gold transition, and age-up buildings. | "just by keeping your wood count low and seeding farms and transitioning to gold at proper time and getting the buildings for age up right before you have the resources" | `normalized:L439` |
| Army composition needs trash units, siege units, and a gold-unit power unit. | "To compose your army properly, you need a few different elements in it. Trash units (non-gold costing units), siege units and a power unit (gold unit)." | `normalized:L523` |
| Game plans begin from map generation and civilization power spikes. | "We take into consideration map generation and civ power spikes and start moving from there, that is how we make game plans." | `normalized:L541` |
| Decision making evaluates available information and missing information against the game state. | "Decision making refers to evaluating the information available to you and deriving from the lack of information as much." | `normalized:L557` |
| Water-map play uses a build to gain water control and block transport attempts. | "you use the build and gain control of water and block any attempts to transport." | `normalized:L618` |
| Mixed maps accelerate economy because fishing ships produce food from a separate building. | "Fishing ships cost only wood, which is much easier to gain than food and on top of that you produce them out of a separate building than TC." | `normalized:L636` |
| Team games favor gold units because trade makes gold renewable if started before gold runs out. | "The reason why you use only gold units is because gold is unlimited through trade, you should always start trading before gold runs out" | `normalized:L677` |
| Slinging sends resources through an early market to accelerate one or more allies. | "one or multiple players after reaching feudal age get market as soon as possible and start sending all their resources to their allies." | `normalized:L691` |

## Major concepts

Foundation - Covers basic gameplay mechanics like hotkeys, controls, creating villagers, building placement, scouting, and build orders.
Core fundamentals - Focuses on economy balance, continuous production, Lanchester's law, army usage, and resource management.
Common edges - Addresses economy upgrades, military upgrades, counter units, uptimes, and unit interactions.
Strategic synthesis - Explores map awareness, opening interactions, army composition planning, game plans, decision making, and fitting gameplay elements together.
Map and team contexts - Includes water maps, mixed maps, closed maps, team games, trading, trash-unit trade

[trimmed]
PAGE: wiki/concepts/aoe2-economy-balance.md
TITLE: AoE2 Economy Balance
TYPE: concept
CONTENT:
---
title: AoE2 Economy Balance
type: concept
tags: []
status: draft
last_updated: 2026-05-02
sources: [../sources/aoe2-basics.md]
---

# AoE2 Economy Balance

This balance of economy while producing and using your army is difficult to perfect.

## Source-backed details

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| Economy balance refers to the amount of excess resources a player has. | "So what does economy balance mean, it's the amount of excess resources you are getting in." | `normalized:L310` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Wood shortages can halt the economy even when a temporary gold shortage is survivable. | "You can get away temporarily without gold, but without wood your whole economy just halts." | `normalized:L547` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Having a dock and ability to fish is beneficial for economy. | "This is why having a dock and being able to fish is extremely beneficial for your economy." | `normalized:L551` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Economy upgrades can create villager-equivalent resource advantages without stopping villager production. | "No but seriously, economy upgrades are really important. Imagine being ahead by 2 villagers?" | `normalized:L288` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |

## Source pages

- [Noobs guide for AoE2](../sources/aoe2-basics.md)

PAGE: wiki/concepts/aoe2-mixed-maps.md
TITLE: AoE2 Mixed Maps
TYPE: concept
CONTENT:
---
title: AoE2 Mixed Maps
type: concept
tags: []
status: draft
last_updated: 2026-05-03
sources: [../sources/aoe2-basics.md]
source_ranges:
  - aoe2-basics:normalized:L628-L646
---
# AoE2 Mixed Maps

Mixed maps in Age of Empires II combine water and land, so players must manage fish economy, land army, water control, and map-specific build orders at the same time.

## Source-backed details

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| A mixed map has both water and land. | "What is a mixed map? Well it's a map that has water and land in all simplicity." | `normalized:L630` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Mixed-map examples include Scandinavia, Mediterranean, Nomad, and Four Lakes. | "you have something like Scandinavia which has two waters that are shared, you have mediterranean, nomad and four lakes." | `normalized:L630` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Mixed maps differ in how players approach water; Mediterranean can play more like a water map, while Four Lakes can be more like a land map with extra fish economy. | "some maps like medi play a lot more like water maps but still retain few of the characteristics of mixed maps. While something like Four Lakes is more of a land map with extra fish eco." | `normalized:L632` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Mixed maps require build orders, and some builds are map-specific because starts do not all play the same way. | "you have to have a build for these maps even more urgently than in arabia or other full land maps. Some of the builds are even map specific, not every mixed map plays the start even the same way." | `normalized:L634` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Fishing ships can accelerate economy because they cost wood, are produced from a separate building than the town center, and gather food. | "Fishing ships cost only wood, which is much easier to gain than food and on top of that you produce them out of a separate building than TC." | `normalized:L636` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Ten fishing ships can create a significant economic lead. | "Having just 10 fishing ships already is a significant economic lead which can be impossible to overcome." | `normalized:L638` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Mixed-map resource management can be overwhelming because docks, the town center, and military production may all need to run at the same time. | "But keeping the docs and TC and military production running at the same time and managing your resources can be extremely overwhelming." | `normalized:L638` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Mixed-map play requires reading the situation to decide what units to make and when to stop investing in fish. | "you've to be able to read the situation extremely well to know what units you should make and when to stop investing on fish in order to retain the lead." | `normalized:L638` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Different mixed maps need different fish investment levels rather than one fixed approach. | "Some you might want to invest less on fish by nature while others you really want to go ham on the fish. There is no one set way in doing it." | `normalized:L640` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Feudal-to-castle and castle-to-imperial transitions matter on mixed maps because resources can arrive very quickly. | "it is very important also to figure out the feudal to castle and castle to imp transitions, it is absolutely ridiculous how much resources you get in a short amount of time" | `normalized:L646` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |

## Related pages

- [AoE2 Build Orders](aoe2-build-orders.md)
- [AoE2 Economy Balance](aoe2-economy-balance.md)
- [AoE2 Game Plans](../procedures/aoe2-game-plans.md)
- [AoE2 Resource Management](aoe2-resource-management.md)
- [AoE2 Water Maps](aoe2-water-maps.md)

## Source pages

- [Noobs guide for AoE2](../sources/aoe2-basics.md)

PAGE: wiki/concepts/aoe2-resource-management.md
TITLE: AoE2 Resource Management
TYPE: concept
CONTENT:
---
title: AoE2 Resource Management
type: concept
tags: []
status: draft
last_updated: 2026-05-03
sources: [../sources/aoe2-basics.md]
---
# AoE2 Resource Management

Resource management in Age of Empires II is the ongoing work of turning income into economy growth, army production, age-up resources, and timely retasking instead of letting the wrong resources sit unused.

## Source-backed details

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| The source defines economy as sources of constant resource income, including villagers, trade carts, relics, fishing ships, and feitoria. | "What is an economy, it's anything that brings you constant resource income: villagers, trade carts, relics, fishing ship and even feitoria." | `normalized:L308` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| A more efficient economy turns incoming resources into either economy growth or increased army numbers. | "when one player has a more efficient eco, he has all the resources incoming being used for either growing his economy or to increase his army numbers." | `normalized:L310` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Players should avoid unnecessary banking while still slowly stacking food and gold for the next age-up. | "So while you're spending all of your resources, you want to be slowly stacking up food and gold for the next age up." | `normalized:L312` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Preventing too much excess of the wrong resource can involve tracking resources, adding farms with extra wood, or retasking stone and gold villagers. | "You keep track of your resources, ideally make new farms each time you have 60 wood extra, unless you need some other building like a blacksmith or something else. In the case of stone and gold, you can simply task villagers to work elsewhere." | `normalized:L316` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Continuous military production has resource-income requirements for each production building. | "There are resource income requirements for keeping each stable or barracks running constantly." | `normalized:L326` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| A one-range archer production example needs 3.5 villagers on gold, so the player must assign 4 villagers and accept excess gold. | "you need 3.5 villagers on gold to run one archery range to produce archers." | `normalized:L326` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Castle-age timing can be improved by keeping wood low, seeding farms, transitioning to gold, and adding age-up buildings shortly before resources are ready. | "keeping your wood count low and seeding farms and transitioning to gold at proper time and getting the buildings for age up right before you have the resources is good guideline for getting good castle age timings." | `normalized:L439` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Mixed maps can make resource management overwhelming because docks, the town center, and military production may all need to run at the same time. | "But keeping the docs and TC and military production running at the same time and managing your resources can be extremely overwhelming." | `normalized:L638` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |

## Related pages

- [AoE2 Economy Balance](aoe2-economy-balance.md)
- [AoE2 Build Orders](aoe2-build-orders.md)
- [AoE2 Scouting Techniques](../procedures/aoe2-scouting-techniques.md)
- [AoE2 Economy Upgrades](../references/aoe2-economy-upgrades.md)

## Source pages

- [Noobs guide for AoE2](../sources/aoe2-basics.md)

PAGE: wiki/analyses/2026-05-03-aoe2-water-and-mixed-map-strategy.md
TITLE: How should an AoE2 player adapt strategy across water and mixed maps
TYPE: analysis
CONTENT:
---
title: "How should an AoE2 player adapt strategy across water and mixed maps"
type: analysis
tags: []
status: draft
last_updated: 2026-05-03
sources:
  - ../sources/aoe2-basics.md
---

# How should an AoE2 player adapt strategy across water and mixed maps

An AoE2 player should treat water maps and mixed maps as build-driven, execution-heavy map types, but adapt the focus differently.

On water maps, prioritize a practiced build that contests water, denies transports, and accounts for landings. The source-backed water page says basic water play uses a build to gain water control and block transport attempts (`normalized:L618`), modern water play can involve both water and land because of dark-age transports, fires, and demos (`normalized:L620`), and defending a landing starts with scouting before walling or spending resources on defense (`normalized:L622`). See [AoE2 Water Maps](../concepts/aoe2-water-maps.md).

On mixed maps, plan for water and land at the same time. The mixed-map page defines mixed maps as maps with both water and land (`normalized:L630`), notes that maps such as Mediterranean and Four Lakes demand different approaches to water (`normalized:L632`), and says these maps need builds because the starts are not all the same (`normalized:L634`). See [AoE2 Mixed Maps](../concepts/aoe2-mixed-maps.md).

The main mixed-map economic adjustment is fish. Fishing ships cost wood, are produced outside the town center, and bring in food (`normalized:L636`), so a player can gain a major economy lead, but must also manage docks, the town center, military production, and resources at the same time (`normalized:L638`). The source warns that different mixed maps need different fish investment levels rather than one fixed approach (`normalized:L640`). See [AoE2 Mixed Maps](../concepts/aoe2-mixed-maps.md), [AoE2 Resource Management](../concepts/aoe2-resource-management.md), and [AoE2 Economy Balance](../concepts/aoe2-economy-balance.md).

The practical adaptation is:

1. Identify whether the map is mostly water or mixed water-and-land.
2. Use a map-specific build instead of treating the start like standard Arabia.
3. On water maps, fight for water control and scout for landings.
4. On mixed maps, keep fish economy, land army, and production balance in view together.
5. Reassess fish investment, unit choice, and age transitions as the map state changes.

Specific build orders, exact civilization picks for each water or mixed map, and map-by-map fish investment thresholds are not covered in sources.

## Source pages

- [Noobs guide for AoE2](../sources/aoe2-basics.md)

## Related pages

- [AoE2 Mixed Maps](../concepts/aoe2-mixed-maps.md)
- [AoE2 Map Awareness](../concepts/aoe2-map-awareness.md)
- [AoE2 Resource Management](../concepts/aoe2-resource-management.md)
- [AoE2 Water Maps](../concepts/aoe2-water-maps.md)
- [AoE2 Army Composition](../concepts/aoe2-army-composition.md)
- [AoE2 Build Orders](../concepts/aoe2-build-orders.md)
- [AoE2 Decision Making](../concepts/aoe2-decision-making.md)

PAGE: wiki/concepts/aoe2-army-composition.md
TITLE: AoE2 Army Composition
TYPE: concept
CONTENT:
---
title: AoE2 Army Composition
type: concept
tags: []
status: draft
last_updated: 2026-05-02
sources: [../sources/aoe2-basics.md]
---

# AoE2 Army Composition

Army composition refers to the selection and arrangement of different unit types to create an effective fighting force.

## Source-backed details

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| Army composition planning involves steps to transition from one stage to another in the game. | "So what does army composition planning mean? Well to get from A to B there has to be steps taken in between right?" | `normalized:L531` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Army composition planning considers unit types and their synergies for effective gameplay. | "If you start a game as Portuguese vs Mongols, you can already determine what is the ideal army composition you want to get into right?" | `normalized:L531` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Trash units are used to counter enemy army composition. | "The job of trash is to effectively attempt to counter enemy army composition, so if the enemy is playing halb and arbalest, you want skirms as it's the cost efficient trash unit." | `normalized:L525` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |
| Army composition can be influenced by map awareness and opening interactions. | "Now you've got options like xbows, skirmishers, scorpions and even longswords you could start creating as a response to add to your army composition of full knights." | `normalized:L421` | [Noobs guide for AoE2](../sources/aoe2-basics.md) |

## Source pages

- [Noobs guide for AoE2](../sources/aoe2-basics.md)

