# Phase 2 Synthesis (JSON Output)

Current date: {{current_date}}
Source slug: `{{slug}}`
Normalized source: `{{normalized_source}}`

## Existing Pages (keep these linked)

{{existing_pages}}

## Create This Page

{{selected_candidates}}

## Evidence Bank

Cite the stable IDs from this evidence bank in your claims:

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
    {
      "heading": "Summary",
      "level": 2,
      "content": "Brief definition of the concept."
    },
    { "heading": "Source-backed details", "level": 2, "claims_table": true },
    {
      "heading": "Why it matters",
      "level": 2,
      "content": "Explanation of importance."
    },
    {
      "heading": "Related pages",
      "level": 2,
      "content": "- [Other Concept](../concepts/other.md)"
    }
  ],
  "claims": [
    { "claim": "First insight in your own words.", "evidence_ids": ["{{slug}}:claim_abc123"] },
    {
      "claim": "Second insight synthesized from source.",
      "evidence_ids": ["{{slug}}:claim_def456", "{{slug}}:claim_ghi789"]
    },
    { "claim": "Third claim with multiple evidence.", "evidence_ids": ["{{slug}}:claim_jkl012"] }
  ]
}
```

Requirements:

- Minimum 3 claims with evidence IDs
- **CRITICAL: Claims must be in your own words, NOT copied from evidence**
  - BAD: "Functions are values" (copied from evidence)
  - GOOD: "JavaScript treats functions as first-class citizens that can be assigned and passed" (synthesized)
- **source_ranges must cover ALL evidence IDs used in claims**
  - If you use evidence IDs whose locators are L3528, L3620, and L3617, your source_ranges must include all three locators
- Set claims_table: true for the Source-backed details section

Output valid JSON only. No markdown fences, no explanation.
