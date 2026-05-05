# Local Model Context Limits: Analysis and Recommendations

This document analyzes the context handling in the llm-wiki tooling and proposes improvements
for running 30B models (e.g., Qwen 30B) on a 4090.

## Problem Statement

The system uses `codex exec` to invoke local models for wiki synthesis tasks. Users report
that the model "begins to answer the questions, but then messes up on a tool call." The
hypothesis is context overflow, where the combined prompt exceeds the model's effective
working context.

## Architecture Analysis

### Context Components

The full context sent to a local model consists of:

| Component | Typical Size | Notes |
|---|---|---|
| AGENTS.md | ~26KB (~6500 tokens) | Read by codex, always included |
| Prompt template | ~6KB | phase2-synthesis.md |
| Evidence bank | Variable (~1-10KB) | 10 snippets × N candidates |
| Validation output | Variable (~1-20KB) | On repair attempts |
| Existing pages | Variable | Listed in repair prompts |
| Codex internals | Unknown | Tool definitions, conversation |

For a single-page Phase 2 task, the base prompt (before evidence) is ~32KB. Adding 10
evidence snippets at ~200 chars each adds ~2KB. This is manageable for a first attempt.

However, repair attempts add:
- Previous validation output (~2-20KB)
- Judge report (~2-5KB)
- Claim repair hints (~1-2KB)

After 1-2 repair attempts, total context can easily exceed 50KB (~12,500 tokens).

### 30B Model Constraints

Typical 30B models have:
- **Nominal context**: 8K-32K tokens
- **Effective context**: Quality degrades toward the end of longer contexts
- **Tool call sensitivity**: Smaller models are more likely to malform tool calls under context pressure

The evidence suggests that initial prompts work, but repair prompts fail. This matches
the pattern of working at low context but failing as context grows.

### Current Safeguards

The architecture already includes:
1. **Bounded phases**: Single-page atomic tasks
2. **Deterministic checks**: Validation before/after model calls
3. **Row-wise fallback**: When batch judge fails, retry row-by-row
4. **Evidence range gating**: Limit snippets to relevant source sections

What's missing:
1. **Context measurement**: No token counting before sending prompts
2. **Context limiting**: No truncation or summarization of prior output
3. **Evidence limits**: Evidence bank size not capped
4. **AGENTS.md consideration**: Large instruction file always fully included
5. **Response diagnostics**: No structured logging of where tool calls fail

## Hypotheses

### H1: Repair Prompt Overflow

**Hypothesis**: Repair prompts grow too large because they include full validation output and
previous context, pushing total context beyond the model's effective limit.

**Test**: Log prompt sizes (chars and estimated tokens) at each codex invocation. Compare
success rates vs. prompt size.

**Mitigation**: Truncate validation output to failing lines only. Summarize prior attempts
instead of including full output.

### H2: Evidence Bank Scaling

**Hypothesis**: For candidates with broad topic matches, evidence banks return many snippets
that add marginal value while consuming context.

**Test**: Compare success rates with 10 vs. 5 vs. 3 snippets per candidate.

**Mitigation**: Reduce `per_candidate` limit in evidence bank. Prioritize higher-scoring
snippets more aggressively.

### H3: AGENTS.md Overhead

**Hypothesis**: AGENTS.md (26KB) is always loaded, reducing the effective context available
for actual work by ~6500 tokens.

**Test**: Create a reduced version of AGENTS.md (~8KB) with only Phase 2-relevant rules.
Compare success rates.

**Mitigation**: Phase-specific instruction files that include only relevant rules. Or pass
AGENTS.md as a system prompt and measure if codex already does this efficiently.

### H4: Tool Call Formatting Under Pressure

**Hypothesis**: When context is near the limit, the model produces syntactically malformed
tool calls (missing brackets, incomplete JSON) rather than semantically wrong ones.

**Test**: Log the raw model output before tool parsing. Categorize failures as:
- Malformed JSON (syntax)
- Valid JSON, wrong structure (semantic)
- Truncated response

**Mitigation**: If malformed JSON dominates, focus on context reduction. If wrong structure
dominates, focus on prompt clarity.

### H5: Instruction Density

**Hypothesis**: Prompts have high instruction-to-work ratio. The model reads many constraints
before reaching the actual task, reducing attention on the work.

**Test**: Restructure prompts to put the task summary and evidence first, detailed rules last.
Compare success rates.

**Mitigation**: "Task-first" prompt structure. Move validation commands to end. Group
constraints by priority.

## Measurement Implementation

### 1. Add Prompt Size Logging

In `wiki_phase1_benchmark.py` and `wiki_phase2_benchmark.py`, before `run_codex`:

```python
def estimate_tokens(text: str) -> int:
    """Rough token estimate: ~4 chars per token for English."""
    return len(text) // 4

def log_prompt_stats(prompt: str, prefix: str) -> None:
    chars = len(prompt)
    tokens = estimate_tokens(prompt)
    print(f"{prefix}: {chars:,} chars, ~{tokens:,} tokens")
```

### 2. Log Validation Output Size

Track size of validation output before including in repair prompts:

```python
validation_text = validation_output.strip()
print(f"Validation output: {len(validation_text):,} chars")
if len(validation_text) > 8000:
    print(f"WARNING: Large validation output may exceed effective context")
```

### 3. Structured Failure Logging

Extend `run_codex` to capture and categorize failures:

```python
def categorize_failure(stdout_path: Path, stderr_path: Path) -> str:
    stdout = stdout_path.read_text(errors="ignore")
    stderr = stderr_path.read_text(errors="ignore")
    
    if "json" in stderr.lower() or "parse" in stderr.lower():
        return "malformed_json"
    if "timeout" in stderr.lower():
        return "timeout"
    if "truncat" in stdout.lower():
        return "truncated"
    return "unknown"
```

### 4. Evidence Bank Size Tracking

In `build_evidence_bank`:

```python
bank = "\n".join(sections).rstrip()
print(f"Evidence bank: {len(bank):,} chars, {len(chunks)} total snippets")
return bank
```

## Success Metrics

### Primary Metrics

| Metric | Current | Target | How to Measure |
|---|---|---|---|
| Phase 2 first-attempt success | Unknown | >70% | Track `validation_returncode == 0` on first codex call |
| Repair success rate | Unknown | >50% | Track recovery after deterministic repair |
| Tool call malformation rate | Unknown | <10% | Categorize failures as syntax vs. semantic |

### Secondary Metrics

| Metric | How to Measure |
|---|---|
| Average prompt size | Log chars/tokens per invocation |
| Evidence bank size | Log chars per build_evidence_bank call |
| Context per successful page | Compare prompt size of successful vs. failed runs |
| Time to first failure | Track at which repair attempt failures cluster |

### Diagnostic Outputs

Add to each run report:
- Prompt sizes for initial and repair attempts
- Evidence bank size
- Validation output size
- Failure category (if failed)
- Model response length

## Proposed Code Changes

### Phase 1: Measurement (Non-Breaking)

1. **Add `--verbose-context` flag** to benchmarking tools
2. **Log prompt statistics** before each codex invocation
3. **Categorize failures** in run reports
4. **Track evidence bank sizes**

### Phase 2: Context Reduction (Breaking Changes)

1. **Truncate validation output**:
   - Keep only lines containing `FAIL` or `error`
   - Cap at 4000 chars
   - Summarize: "N additional lines omitted"

2. **Evidence bank limits**:
   - Add `--max-evidence-chars` flag (default 6000)
   - Add `--max-snippets` flag (default 8)
   - Prioritize snippets by score, truncate tail

3. **Repair prompt compression**:
   - Don't repeat full evidence bank in repair prompts
   - Use: "Evidence bank: see initial prompt"
   - Include only the specific failing snippets

### Phase 3: Prompt Restructuring

1. **Task-first structure**:
   ```
   ## Task
   Create exactly one page: {path}
   
   ## Evidence
   {snippets}
   
   ## Validation
   {commands}
   
   ## Detailed Rules
   {constraints}
   ```

2. **Phase-specific AGENTS.md**:
   - Create `AGENTS_phase2_synthesis.md` (~8KB)
   - Include only relevant sections
   - Point to full AGENTS.md for edge cases

### Phase 4: Alternative Approaches

1. **Two-stage prompting**:
   - Stage 1: Model produces a plan (small output)
   - Stage 2: Model executes the plan with evidence
   - Reduces context per stage

2. **Incremental evidence**:
   - Start with 3 snippets
   - If validation fails, add more snippets
   - Don't front-load all evidence

3. **Context-aware repair**:
   - After 2 failed repairs, reset context
   - Start fresh with smaller prompt
   - Use only the most critical constraints

## Testing Protocol

### Baseline Measurement

```bash
# Measure current state
pnpm wiki:phase2-single aoe2-basics ../concepts/aoe2-decision-making.md \
  --candidate local-4090 \
  --verbose-context \
  --report /tmp/baseline-report.md
```

### A/B Testing

For each hypothesis, run 5 Phase 2 tasks with:
- Control: Current implementation
- Test: Modified implementation

Track:
- Success rate (first attempt)
- Success rate (after repairs)
- Prompt sizes
- Failure categories

### Regression Prevention

Add to `pnpm wiki:maintenance`:
- Assert average prompt size < threshold
- Assert evidence bank size < threshold
- Log context statistics in maintenance report

## Implementation Priority

1. **Measurement first**: Add verbose context logging (1 day)
2. **Collect data**: Run 10-20 Phase 2 tasks, log everything (1 day)
3. **Analyze failures**: Categorize by context size vs. failure type (1 day)
4. **Implement mitigations**: Based on data, not assumptions (2-3 days)
5. **Validate improvements**: A/B test against baseline (1 day)

## Appendix: Token Estimation

For rough token counting without a tokenizer:

| Language | Chars per Token |
|---|---|
| English prose | 4.0 |
| Code | 3.5 |
| Markdown with code | 3.7 |

A 30B model with 8K context has ~32,000 chars effective context.
A 30B model with 16K context has ~64,000 chars effective context.

AGENTS.md (26KB) alone uses ~40% of an 8K context window.
