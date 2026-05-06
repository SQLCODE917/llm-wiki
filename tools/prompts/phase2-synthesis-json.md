# Phase 2 Synthesis (JSON Output)

Current date: {{current_date}}
Source slug: `{{slug}}`
Normalized source: `{{normalized_source}}`

## Existing Pages (keep these linked)

{{existing_pages}}

## Create This Page

{{selected_candidates}}

## Evidence Bank

Cite these IDs in your claims:

{{evidence_bank}}

## Output

Return a single JSON object for the page. Example structure:

```json
{
  "path": "wiki/concepts/example.md",
  "frontmatter": {
    "title": "Example Concept",
    "type": "concept",
    "tags": [],
    "status": "draft",
    "last_updated": "{{current_date}}",
    "sources": ["../sources/{{slug}}.md"],
    "source_ranges": ["{{slug}}:normalized:L100-L200"]
  },
  "sections": [
    {"heading": "Summary", "level": 2, "content": "Brief definition of the concept."},
    {"heading": "Source-backed details", "level": 2, "claims_table": true},
    {"heading": "Why it matters", "level": 2, "content": "Explanation of importance."},
    {"heading": "Related pages", "level": 2, "content": "- [Other Concept](../concepts/other.md)"}
  ],
  "claims": [
    {"claim": "First insight in your own words.", "evidence_ids": ["E01"]},
    {"claim": "Second insight synthesized from source.", "evidence_ids": ["E02", "E03"]},
    {"claim": "Third claim with multiple evidence.", "evidence_ids": ["E04"]}
  ]
}
```

Requirements:
- Minimum 3 claims with evidence IDs
- Claims must synthesize evidence, not copy it
- Include source_ranges for the relevant source sections
- Set claims_table: true for the Source-backed details section

Output valid JSON only. No markdown fences, no explanation.
