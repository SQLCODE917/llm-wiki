# Cloud Model Backends: Cross-Platform LLM Support

This document designs a unified model backend system that works across:
- **Permissive environments**: Local GPU with codex/ollama
- **Non-permissive environments**: Cloud APIs and AI coding assistants

## Problem Statement

The current architecture assumes local `codex` CLI. Many environments don't permit this:
- **GitHub Codespaces**: No persistent GPU, restricted installs
- **Corporate environments**: No local model installation allowed
- **Lightweight VMs**: Insufficient resources for local inference

However, these environments typically have access to:
- **Cloud LLM APIs**: OpenAI, Anthropic, AWS Bedrock
- **AI coding assistants**: GitHub Copilot, Claude Code, Cursor

## Two Operating Modes

### Mode 1: Scripted Automation (API Backends)

The Python tooling calls an LLM API directly:

```
User runs: pnpm wiki:phase2-single slug page.md --backend openai
    ↓
wiki_phase2_single.py
    ↓
wiki_model_backend.py → OpenAI API
    ↓
Parse response → Write files → Validate
```

### Mode 2: Agent-Assisted (Interactive)

An AI coding assistant (Copilot, Claude Code) IS the agent. It reads AGENTS.md
and executes tasks directly in the workspace:

```
User asks Copilot: "Ingest this PDF following AGENTS.md"
    ↓
Copilot reads AGENTS.md
    ↓
Copilot runs: pnpm wiki:phase0, then edits files, then runs validation
    ↓
Copilot reports completion
```

**Key insight**: AGENTS.md works for ANY LLM that can read markdown. The tooling
just needs to support both automated and interactive workflows.

---

## Target Configurations

| Environment | Mode | Backend | Model |
|---|---|---|---|
| Local 4090 | Scripted | codex | Qwen 30B via ollama |
| Codespaces + OpenAI | Scripted | openai | GPT-4o / o1 |
| Codespaces + Anthropic | Scripted | anthropic | Claude Sonnet 4 |
| Codespaces + Bedrock | Scripted | bedrock | Qwen3-coder 30B |
| Any + GitHub Copilot | Agent | copilot | (Copilot's model) |
| Any + Claude Code | Agent | claude-code | Claude Sonnet 4 |
| Any + Cursor | Agent | cursor | (Cursor's model) |

---

## Architecture

### Backend Abstraction

```
┌──────────────────────────────────────────────────────────────────┐
│                     wiki_model_backend.py                        │
├──────────────────────────────────────────────────────────────────┤
│  get_backend(name) -> ModelBackend                               │
│  run_model(prompt, config) -> ModelResponse                      │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │              Scripted Backends (API calls)               │    │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────────────┐ │    │
│  │  │  codex  │ │ openai  │ │anthropic│ │     bedrock     │ │    │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────────────┘ │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │              Agent Backends (Interactive)                │    │
│  │  ┌─────────┐ ┌───────────┐ ┌─────────┐                   │    │
│  │  │ copilot │ │claude-code│ │  cursor │                   │    │
│  │  └─────────┘ └───────────┘ └─────────┘                   │    │
│  └──────────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────────┘
```

### Configuration

`tools/wiki_model_defaults.json`:

```json
{
  "updated": "2026-05-05",
  "mode": "scripted",
  "backend": "openai",
  "default_candidate": "gpt-4o",
  "backends": {
    "codex": {
      "type": "scripted",
      "bin": "codex",
      "default_profile": "local-4090"
    },
    "openai": {
      "type": "scripted",
      "api_key_env": "OPENAI_API_KEY",
      "model": "gpt-4o",
      "max_tokens": 8192,
      "temperature": 0.1
    },
    "anthropic": {
      "type": "scripted",
      "api_key_env": "ANTHROPIC_API_KEY",
      "model": "claude-sonnet-4-20250514",
      "max_tokens": 8192,
      "temperature": 0.1
    },
    "bedrock": {
      "type": "scripted",
      "region": "us-east-1",
      "model_id": "anthropic.claude-sonnet-4-20250514-v1:0",
      "max_tokens": 8192,
      "temperature": 0.1
    },
    "copilot": {
      "type": "agent",
      "instructions_file": "AGENTS.md"
    },
    "claude-code": {
      "type": "agent",
      "instructions_file": "AGENTS.md"
    },
    "cursor": {
      "type": "agent",
      "instructions_file": "AGENTS.md"
    }
  },
  "phases": {
    "phase1": "openai:gpt-4o",
    "phase2": "openai:gpt-4o",
    "claim_judge": "openai:gpt-4o",
    "query": "openai:gpt-4o",
    "analysis_judge": "openai:gpt-4o"
  }
}
```

Environment variable overrides:
```bash
# Backend selection
export WIKI_MODEL_BACKEND=anthropic     # codex | openai | anthropic | bedrock

# API keys (don't commit these!)
export OPENAI_API_KEY=sk-...
export ANTHROPIC_API_KEY=sk-ant-...

# AWS (for Bedrock)
export AWS_REGION=us-east-1
export AWS_PROFILE=sdai-dev
```

---

## Scripted Backend Implementations

### 1. Codex Backend (Local)

Wraps existing `run_codex()` for local models via ollama:

```python
class CodexBackend(ModelBackend):
    def run(self, prompt: str, config: ModelConfig) -> ModelResponse:
        returncode, paths = run_codex(
            worktree=config.worktree,
            candidate=config.candidate,
            codex_bin=config.codex_bin,
            prompt=prompt,
            timeout=config.timeout,
            prefix=config.prefix,
        )
        return ModelResponse(
            success=returncode == 0,
            output=paths[-1].read_text() if paths else "",
            log_paths=paths,
        )
```

### 2. OpenAI Backend (ChatGPT)

Direct API calls to OpenAI:

```python
import openai
import os

class OpenAIBackend(ModelBackend):
    def __init__(self, model: str = "gpt-4o", max_tokens: int = 8192, temperature: float = 0.1):
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    
    def run(self, prompt: str, config: ModelConfig) -> ModelResponse:
        log_context_stats(prompt, label=f"{config.prefix} prompt (openai)")
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self._system_prompt(config)},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=self.max_tokens,
                temperature=self.temperature,
            )
            
            output_text = response.choices[0].message.content
            finish_reason = response.choices[0].finish_reason
            
            log_paths = self._save_logs(config, prompt, output_text, response)
            
            return ModelResponse(
                success=finish_reason == "stop",
                output=output_text,
                log_paths=log_paths,
                stop_reason=finish_reason,
                usage={
                    "input_tokens": response.usage.prompt_tokens,
                    "output_tokens": response.usage.completion_tokens,
                },
            )
            
        except Exception as e:
            return ModelResponse(success=False, output="", error=str(e), log_paths=[])
    
    def _system_prompt(self, config: ModelConfig) -> str:
        agents_md = (config.worktree / "AGENTS.md").read_text()
        return f"""You are a wiki maintenance agent. Follow these rules exactly:

{agents_md}

Working directory: {config.worktree}
Output file contents in fenced code blocks with the file path as the language tag."""
```

### 3. Anthropic Backend (Claude)

Direct API calls to Anthropic:

```python
import anthropic
import os

class AnthropicBackend(ModelBackend):
    def __init__(self, model: str = "claude-sonnet-4-20250514", max_tokens: int = 8192, temperature: float = 0.1):
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    
    def run(self, prompt: str, config: ModelConfig) -> ModelResponse:
        log_context_stats(prompt, label=f"{config.prefix} prompt (anthropic)")
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                system=self._system_prompt(config),
                messages=[{"role": "user", "content": prompt}],
            )
            
            output_text = response.content[0].text
            stop_reason = response.stop_reason
            
            log_paths = self._save_logs(config, prompt, output_text, response)
            
            return ModelResponse(
                success=stop_reason == "end_turn",
                output=output_text,
                log_paths=log_paths,
                stop_reason=stop_reason,
                usage={
                    "input_tokens": response.usage.input_tokens,
                    "output_tokens": response.usage.output_tokens,
                },
            )
            
        except Exception as e:
            return ModelResponse(success=False, output="", error=str(e), log_paths=[])
```

### 4. AWS Bedrock Backend

Uses boto3 Converse API for AWS-managed models (Claude, Qwen, Llama, etc.):

```python
import boto3
import os

class BedrockBackend(ModelBackend):
    def __init__(
        self,
        model_id: str = "anthropic.claude-sonnet-4-20250514-v1:0",
        region: str = None,
        max_tokens: int = 8192,
        temperature: float = 0.1,
    ):
        self.model_id = model_id
        self.max_tokens = max_tokens
        self.temperature = temperature
        region = region or os.environ.get("AWS_REGION", "us-east-1")
        self.client = boto3.client("bedrock-runtime", region_name=region)
    
    def run(self, prompt: str, config: ModelConfig) -> ModelResponse:
        log_context_stats(prompt, label=f"{config.prefix} prompt (bedrock)")
        
        try:
            response = self.client.converse(
                modelId=self.model_id,
                messages=[{"role": "user", "content": [{"text": prompt}]}],
                inferenceConfig={
                    "maxTokens": self.max_tokens,
                    "temperature": self.temperature,
                },
                system=[{"text": self._system_prompt(config)}],
            )
            
            output_text = response["output"]["message"]["content"][0]["text"]
            stop_reason = response["stopReason"]
            
            log_paths = self._save_logs(config, prompt, output_text, response)
            
            return ModelResponse(
                success=stop_reason in ("end_turn", "stop_sequence"),
                output=output_text,
                log_paths=log_paths,
                stop_reason=stop_reason,
                usage=response.get("usage", {}),
            )
            
        except Exception as e:
            return ModelResponse(success=False, output="", error=str(e), log_paths=[])
```

### Common Helper Methods

All scripted backends share these:

```python
class ModelBackend:
    def _system_prompt(self, config: ModelConfig) -> str:
        """Build system prompt from AGENTS.md."""
        agents_md = (config.worktree / "AGENTS.md").read_text()
        return f"""You are a wiki maintenance agent. Follow these rules exactly:

{agents_md}

Working directory: {config.worktree}
Output file contents in fenced code blocks with the file path as the language tag.
Example:
```wiki/concepts/example.md
---
title: Example
type: concept
---
# Example
Content here.
```"""
    
    def _save_logs(self, config: ModelConfig, prompt: str, output: str, response) -> list[Path]:
        """Save prompt, output, and metadata for debugging."""
        prefix = config.prefix
        worktree = config.worktree
        
        (worktree / f"{prefix}-prompt.md").write_text(prompt)
        (worktree / f"{prefix}-output.md").write_text(output)
        (worktree / f"{prefix}-meta.json").write_text(json.dumps({
            "backend": self.__class__.__name__,
            "usage": getattr(response, "usage", None) or response.get("usage", {}),
        }, indent=2))
        
        return [
            worktree / f"{prefix}-prompt.md",
            worktree / f"{prefix}-output.md",
            worktree / f"{prefix}-meta.json",
        ]
```

---

## Agent-Assisted Mode (Interactive)

When using GitHub Copilot, Claude Code, or Cursor, the AI assistant IS the agent.
No API calls needed — the agent reads AGENTS.md directly and executes tasks.

### How It Works

1. **AGENTS.md is the interface**: Any AI that can read markdown can follow the rules
2. **Deterministic tools still work**: `pnpm wiki:check-source`, `pnpm wiki:lint`, etc.
3. **Human orchestrates**: User asks the agent to perform ingest phases

### Agent-Specific Instructions Files

Create instruction files that each tool reads automatically:

| AI Assistant | Instruction File | Notes |
|---|---|---|
| GitHub Copilot | `.github/copilot-instructions.md` | Auto-loaded in VS Code |
| Claude Code | `CLAUDE.md` | Claude's convention |
| Cursor | `.cursorrules` | Cursor's convention |
| OpenAI Codex | `AGENTS.md` | Codex's convention |

All can point to the same content:

```markdown
<!-- .github/copilot-instructions.md -->
# Copilot Instructions for llm-wiki

Read and follow [AGENTS.md](../AGENTS.md) for all wiki maintenance tasks.

Quick reference:
- Ingest: `pnpm wiki:ingest raw/inbox/<file> --slug <slug>`
- Validate source: `pnpm wiki:check-source <slug>`
- Validate synthesis: `pnpm wiki:check-synthesis <slug>`
- Lint: `pnpm wiki:lint`
```

### Handoff Mode for Scripted→Agent

When scripted automation wants to delegate to an interactive agent:

```python
class AgentHandoffBackend(ModelBackend):
    """
    Generates a task file for human + AI assistant to execute.
    Used when scripted automation hits a task better suited for interactive work.
    """
    
    def run(self, prompt: str, config: ModelConfig) -> ModelResponse:
        handoff_path = config.worktree / f"{config.prefix}-agent-task.md"
        handoff_path.write_text(f"""# Agent Task: {config.prefix}

## Context
- Working directory: `{config.worktree}`
- Task: {config.task_description}

## Instructions

{prompt}

## Validation
After completing, run:
```bash
{config.validation_command}
```

## Mark Complete
When done, create an empty file:
```bash
touch {config.worktree}/{config.prefix}-complete
```
""")
        
        print(f"\n{'='*60}")
        print(f"AGENT HANDOFF: {handoff_path}")
        print(f"Ask your AI assistant (Copilot/Claude/Cursor) to execute this task.")
        print(f"{'='*60}\n")
        
        # Wait for completion marker
        complete_marker = config.worktree / f"{config.prefix}-complete"
        while not complete_marker.exists():
            input("Press Enter after the agent completes (or Ctrl+C to abort)...")
            if complete_marker.exists():
                break
        
        complete_marker.unlink()
        return ModelResponse(
            success=True,
            output="(completed via agent handoff)",
            log_paths=[handoff_path],
        )
```

---

## Unified Backend Selection

```python
# tools/wiki_model_backend.py

from pathlib import Path
import os
import json

def get_backend(name: str = None) -> ModelBackend:
    """Get a model backend by name or from environment."""
    name = name or os.environ.get("WIKI_MODEL_BACKEND", "codex")
    
    config = load_backend_config(name)
    
    if name == "codex":
        return CodexBackend(**config)
    elif name == "openai":
        return OpenAIBackend(**config)
    elif name == "anthropic":
        return AnthropicBackend(**config)
    elif name == "bedrock":
        return BedrockBackend(**config)
    elif name in ("copilot", "claude-code", "cursor"):
        return AgentHandoffBackend(**config)
    else:
        raise ValueError(f"Unknown backend: {name}")


def load_backend_config(name: str) -> dict:
    """Load backend config from wiki_model_defaults.json."""
    defaults_path = Path(__file__).parent / "wiki_model_defaults.json"
    if defaults_path.exists():
        defaults = json.loads(defaults_path.read_text())
        return defaults.get("backends", {}).get(name, {})
    return {}
```

---

## Key Differences: Scripted vs Agent Mode

### Scripted Mode (codex, openai, anthropic, bedrock)

| Aspect | Behavior |
|---|---|
| Execution | Python script calls API, parses response, writes files |
| Sandbox | Worktree isolation (copy of repo) |
| File writes | Parsed from model output, validated before write |
| Tool calling | Text-only initially; tool use optional |
| Human oversight | Validation commands run automatically |

### Agent Mode (copilot, claude-code, cursor)

| Aspect | Behavior |
|---|---|
| Execution | AI assistant runs commands directly in workspace |
| Sandbox | None — operates on real files (use git for safety) |
| File writes | Agent writes directly via editor/terminal |
| Tool calling | Full access to terminal, file system, extensions |
| Human oversight | User watches and approves in real-time |

### Backend Comparison

| Backend | Latency | Cost | Context | Best For |
|---|---|---|---|---|
| codex (local) | Low | ~$0/task | 32K+ | High-volume, privacy |
| openai | Medium | ~$0.10/task | 128K | Quality, long context |
| anthropic | Medium | ~$0.10/task | 200K | Quality, artifacts |
| bedrock | Medium | ~$0.08/task | Varies | AWS integration, compliance |
| copilot | Interactive | Subscription | Varies | Complex tasks, exploration |
| claude-code | Interactive | Subscription | 200K | Complex tasks, artifacts |

---

## Structured Output Parsing

All scripted backends use the same output format:

```python
def parse_model_output(output: str, expected_files: list[str]) -> dict[str, str]:
    """
    Parse model output into file contents.
    
    Expected format:
    ```wiki/path/to/file.md
    file contents here
    ```
    """
    files = {}
    current_file = None
    current_content = []
    
    for line in output.split("\n"):
        if line.startswith("```") and not line.startswith("```\n"):
            if current_file:
                files[current_file] = "\n".join(current_content)
            path = line[3:].strip()
            if path in expected_files or path.endswith(".md"):
                current_file = path
                current_content = []
            else:
                current_file = None
        elif line == "```" and current_file:
            files[current_file] = "\n".join(current_content)
            current_file = None
            current_content = []
        elif current_file:
            current_content.append(line)
    
    return files
```

### Truncation Detection

```python
def check_response_completeness(response: ModelResponse) -> bool:
    """Detect truncated or incomplete responses."""
    if response.stop_reason in ("length", "max_tokens"):
        return False
    if len(response.output) < 100 and "error" not in response.output.lower():
        return False
    return True
```

---

## Configuration

```
Environment variables (highest priority)
    ↓
tools/wiki_model_defaults.json
    ↓
CLI flags (--candidate, --backend)
    ↓
Hardcoded defaults (lowest priority)
```

### Environment Variables

```bash
# Backend selection
export WIKI_MODEL_BACKEND=openai    # codex | openai | anthropic | bedrock | copilot | claude-code

# OpenAI (ChatGPT)
export OPENAI_API_KEY=sk-...

# Anthropic (Claude API)
export ANTHROPIC_API_KEY=sk-ant-...

# AWS Bedrock
export AWS_REGION=us-east-1
export AWS_PROFILE=sdai-dev
# Authenticate with: aws configure sso --profile sdai-dev

# Local codex
export CODEX_BIN=/usr/local/bin/codex
```

### Codespaces Setup (OpenAI/Anthropic)

For simple API-based backends in Codespaces:

```json
{
  "containerEnv": {
    "WIKI_MODEL_BACKEND": "openai"
  },
  "secrets": ["OPENAI_API_KEY"]
}
```

### Codespaces Setup (Bedrock)

```json
{
  "features": {
    "ghcr.io/devcontainers/features/aws-cli:1": {}
  },
  "containerEnv": {
    "WIKI_MODEL_BACKEND": "bedrock",
    "AWS_REGION": "us-east-1"
  },
  "secrets": ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"]
}
```

Or use GitHub OIDC with AWS IAM Identity Center for keyless auth.

### Agent Mode Setup

For Copilot, Claude Code, or Cursor — no environment variables needed.
The agent reads AGENTS.md directly. Ensure instruction files exist:

```bash
# Create instruction files for each AI assistant
cp .github/copilot-instructions.md.example .github/copilot-instructions.md
cp CLAUDE.md.example CLAUDE.md
cp .cursorrules.example .cursorrules
```

---

## Migration Path

### Phase 1: Backend Abstraction (Non-Breaking)

1. Create `tools/wiki_model_backend.py` with abstract interface
2. Move `run_codex()` into `CodexBackend` class
3. Update callers to use `get_backend().run()`
4. Default behavior unchanged (codex)

### Phase 2: Cloud API Backends

1. Implement `OpenAIBackend` and `AnthropicBackend`
2. Add `openai`, `anthropic` to requirements.txt (optional dependencies)
3. Add structured output parsing
4. Test with Phase 2 synthesis tasks

### Phase 3: Bedrock Backend

1. Implement `BedrockBackend`
2. Add `boto3` to requirements.txt (optional dependency)
3. Test with Claude/Qwen models on Bedrock

### Phase 4: Agent Handoff Mode

1. Implement `AgentHandoffBackend` for interactive delegation
2. Create instruction file templates
3. Document agent-assisted workflow
4. Add `--interactive` flag to relevant commands

---

## Testing

### Unit Tests

```python
def test_output_parsing():
    output = """Here's the wiki page:

```wiki/concepts/test-concept.md
---
title: Test Concept
type: concept
---

# Test Concept

This is a test.
```

Done."""
    
    files = parse_model_output(output, ["wiki/concepts/test-concept.md"])
    assert "wiki/concepts/test-concept.md" in files
    assert "# Test Concept" in files["wiki/concepts/test-concept.md"]


def test_truncation_detection():
    response = ModelResponse(output="Hi", stop_reason="max_tokens")
    assert not check_response_completeness(response)
    
    response = ModelResponse(output="Full content here...", stop_reason="stop")
    assert check_response_completeness(response)
```

### Integration Tests

```bash
# Test OpenAI connectivity
WIKI_MODEL_BACKEND=openai python3 -c "
from tools.wiki_model_backend import get_backend
backend = get_backend()
print(f'Backend: {backend.__class__.__name__}')
"

# Test Anthropic connectivity
WIKI_MODEL_BACKEND=anthropic python3 -c "
from tools.wiki_model_backend import get_backend
backend = get_backend()
print(f'Backend: {backend.__class__.__name__}')
"

# Test full Phase 2 flow with each backend
WIKI_MODEL_BACKEND=openai pnpm wiki:phase2-single aoe2-basics ../concepts/test.md --dry-run
WIKI_MODEL_BACKEND=anthropic pnpm wiki:phase2-single aoe2-basics ../concepts/test.md --dry-run
WIKI_MODEL_BACKEND=bedrock pnpm wiki:phase2-single aoe2-basics ../concepts/test.md --dry-run
```

---

## Cost Considerations

| Backend | Cost Model | Approximate Cost/Task | Best For |
|---|---|---|---|
| codex (local) | Electricity | ~$0.01 | High-volume, privacy |
| openai (GPT-4o) | Per-token | ~$0.05-0.15 | Quality, availability |
| anthropic (Claude) | Per-token | ~$0.05-0.15 | Quality, long context |
| bedrock | Per-token | ~$0.05-0.15 | AWS compliance |
| copilot | Subscription | $0 (included) | Interactive, exploration |
| claude-code | Subscription | $0 (included) | Interactive, artifacts |

For high-volume scripted ingestion, local codex or API backends are preferred.
Agent mode is best for complex tasks requiring human judgment.

---

## Security Notes

### API Keys

- Never commit API keys to git
- Use environment variables or secrets management
- Rotate keys if exposed

### AWS Bedrock

- Use IAM roles, not hardcoded keys
- Scope IAM policy to `bedrock:InvokeModel` only
- Enable CloudTrail logging for audit

### Codespaces Secrets

Store in GitHub repository secrets:
- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`
- `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY`
- Or use OIDC federation (preferred for AWS)

### Model Output Validation

Never execute model output directly. Always:
1. Parse into expected structure
2. Validate paths are within worktree
3. Run deterministic validation after writes

---

## Open Questions

1. **Tool use**: Should API backends support tool calling for file writes,
   or stick with text-only + parsing?

2. **Streaming**: APIs support streaming responses. Worth implementing for long
   synthesis tasks to show progress?

3. **Fallback chain**: If one backend fails, should we auto-fallback to another?
   e.g., `openai → anthropic → agent-handoff`

4. **Cost tracking**: Add per-task cost logging using API usage metrics?

5. **Rate limiting**: Handle API rate limits gracefully with backoff?

---

## Summary

This design enables llm-wiki to run in any environment via:

1. **Backend abstraction**: `ModelBackend` interface with pluggable implementations
2. **Scripted backends**: codex (local), openai (ChatGPT), anthropic (Claude), bedrock (AWS)
3. **Agent backends**: copilot, claude-code, cursor for interactive use
4. **Configuration**: Environment variables and JSON config for backend selection
5. **Safety**: Text-only responses with structured parsing, worktree isolation

**Key insight**: AGENTS.md is the universal interface. Whether the model is invoked
via API or is an interactive AI assistant, the same rules apply. The tooling just
needs to support both automated (scripted) and interactive (agent) workflows.

The core wiki workflow (phased ingestion, deterministic validation, evidence grounding)
remains unchanged. Only the model invocation layer is abstracted.
