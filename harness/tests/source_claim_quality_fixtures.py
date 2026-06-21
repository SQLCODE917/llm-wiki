"""Labeled fixtures for source-claim quality tests."""

from llmwiki.domain.objects import SourceClaimQualityFixture


def fixtures() -> tuple[SourceClaimQualityFixture, ...]:
    javascript_specs = (
        (
            "Object.assign",
            "Object.assign copies own enumerable properties from source objects into a target.",
            "eligible",
            (),
        ),
        (
            "Closures",
            "A closure is a function with access to bindings from an outer lexical scope.",
            "eligible",
            ("identity",),
        ),
        (
            "Iterators",
            "An iterator object returns successive values through calls to next.",
            "eligible",
            ("function",),
        ),
        (
            "Map",
            "A caller may pass a function to map in order to transform each element.",
            "eligible",
            ("ordinary-modality",),
        ),
        (
            "Generators",
            "There is more to generators than producing a single sequence.",
            "eligible",
            ("ordinary-modality",),
        ),
        (
            "Resources",
            "The source does not specify whether the iterator closes the resource.",
            "eligible",
            ("source-uncertainty",),
        ),
        (
            "Closures",
            "Closures are similar to backpacks that carry bindings for a function.",
            "analogy",
            ("analogy",),
        ),
        (
            "Callbacks",
            "What if a callback could remember state after its creator returns?",
            "rhetorical-example",
            (),
        ),
        (
            "Narrative",
            "Let us take a short detour before returning to functions.",
            "narrative-frame",
            (),
        ),
        (
            "Narrative",
            "Imagine we are visiting our favourite coffee shop.",
            "narrative-frame",
            ("worked-example",),
        ),
        (
            "Source framing",
            "The source discusses closures and function scope.",
            "source-framing",
            ("source-framing",),
        ),
        ("Code", "const result = values.map(value => value * value);", "code-fragment", ()),
        ("Source furniture", "Copyright 2016 by the author.", "source-furniture", ()),
        (
            "Source furniture",
            "http://creativecommons.org/licenses/by-sa/2.0/deed.en",
            "source-furniture",
            (),
        ),
        (
            "Reduce",
            "Reduce combines a collection into one accumulated value.",
            "eligible",
            ("function",),
        ),
        (
            "Objects",
            "Objects have properties that can be read by name.",
            "eligible",
            ("attribute",),
        ),
    )
    antikythera_specs = (
        (
            "Device identity",
            "The Antikythera mechanism is an ancient geared calculating device.",
            "eligible",
            ("identity",),
        ),
        (
            "Function",
            "The device tracked astronomical cycles using a gear train.",
            "eligible",
            ("function",),
        ),
        (
            "Evidence",
            "Inscriptions provide evidence for calendrical and eclipse functions.",
            "eligible",
            ("evidence",),
        ),
        ("Dating", "The wreck was recovered in 1901 near Antikythera.", "eligible", ("temporal",)),
        (
            "Uncertainty",
            "The source does not confirm the workshop that made the mechanism.",
            "eligible",
            ("source-uncertainty",),
        ),
        (
            "Comparison",
            "No comparable geared device was found from the same period.",
            "eligible",
            ("negative-evidence",),
        ),
        (
            "Analogy",
            "The mechanism is similar to a compact astronomical computer.",
            "analogy",
            ("analogy",),
        ),
        ("Question", "How would a user know which dial to read first?", "rhetorical-example", ()),
        (
            "Source framing",
            "The text mentions the bronze fragments and inscription evidence.",
            "source-framing",
            ("source-framing",),
        ),
        (
            "Source furniture",
            "Table of contents lists the recovery chapter.",
            "source-furniture",
            (),
        ),
    )
    sword_world_specs = (
        (
            "Death checks",
            "Characters must make a death check when life force falls below zero.",
            "eligible",
            ("requirement",),
        ),
        (
            "Movement",
            "Movement and actions happen before the next combat round.",
            "eligible",
            ("temporal",),
        ),
        (
            "Poison",
            "The source does not specify every poison progression speed.",
            "eligible",
            ("source-uncertainty",),
        ),
        (
            "Magic",
            "A player may ask an NPC to cast Remove Curse.",
            "eligible",
            ("ordinary-modality",),
        ),
        (
            "Resistance",
            "Resistance rolls compare the target number with a success roll.",
            "eligible",
            ("comparison",),
        ),
        (
            "Example",
            "For example, a warrior can attack with a sword.",
            "eligible",
            ("worked-example",),
        ),
        (
            "Analogy",
            "The adventurer guild is like a home for wandering heroes.",
            "analogy",
            ("analogy",),
        ),
        (
            "Question",
            "How would a character know which monster is hidden?",
            "rhetorical-example",
            (),
        ),
        (
            "Source framing",
            "The section describes monster attacks and damage rolls.",
            "source-framing",
            ("source-framing",),
        ),
        ("Source furniture", "Page 42 lists the combat chapter.", "source-furniture", ()),
    )
    return (
        tuple(
            _quality_fixture(
                f"javascript-{idx:03d}",
                "javascriptallonge.pdf",
                javascript_specs[idx % len(javascript_specs)],
            )
            for idx in range(80)
        )
        + tuple(
            _quality_fixture(
                f"antikythera-{idx:03d}",
                "antikythera-mechanism.md",
                antikythera_specs[idx % len(antikythera_specs)],
            )
            for idx in range(20)
        )
        + tuple(
            _quality_fixture(
                f"sword-world-{idx:03d}",
                "sword-world.pdf",
                sword_world_specs[idx % len(sword_world_specs)],
            )
            for idx in range(20)
        )
    )


def _quality_fixture(
    fixture_id: str,
    source_locator: str,
    spec: tuple[str, str, str, tuple[str, ...]],
) -> SourceClaimQualityFixture:
    heading, statement, eligibility, roles = spec
    return SourceClaimQualityFixture(
        fixture_id=fixture_id,
        source_locator=source_locator,
        heading_path=heading,
        statement=statement,
        expected_claim_eligibility=eligibility,
        expected_claim_role_tags=roles,
    )
