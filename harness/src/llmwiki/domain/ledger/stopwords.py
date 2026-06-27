"""Common-English words that make poor topic anchors for any source.

These are reusable function words plus generic adjectives, adverbs, and
discourse nouns ("thing", "way", "example"). Domain content words —
``function``, ``value``, ``closure``, ``character``, ``damage``, ``king`` — are
deliberately absent so real topics survive. Filtering common English is
source-neutral; it never keys off one source's particular vocabulary.
"""

from __future__ import annotations

_WORDS = """
about above across actually after again against ago all almost along already also although always
among another any anyone anything are aren around back basic because been before being below best
better between both call called calls came can cannot certain clear come comes coming common could
couldn course days didn does doesn doing don done down during each either else enough especially
even ever every everyone everything example examples fact far few find first found from full
general get gets getting give given gives going gone good great half hard has have haven having
held hence here high however instance into isn its itself just keep kept kind kinds know known
large last later least less let like little long look looks lot made main make makes making many
may maybe mean means medi merely might modern more most much must name named names need needs
never new next nothing now number off often once one only onto other others our out over own part
parts perhaps place places point points popular possible probably put quite rather real really
right said same say says seem seems sense set several shall shouldn show shows simple simply since
small some someone something sometime sometimes soon sort sorts still such sure take takes taken
than that the their them then there therefore these they thing things this those though through
thus time times together too took toward true under until upon use used uses using usually various
very want wants was wasn way ways well went were weren what when where whether which while who
whole whom whose why will with within without won work works world would wouldn yet your
"""
COMMON_WORDS = frozenset(_WORDS.split())
