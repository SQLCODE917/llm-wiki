# Implementation Plan: Bedrock Backend for Codespaces

## Goal

Enable llm-wiki to run in GitHub Codespaces using AWS Bedrock, supporting:
1. **Interactive mode**: Human uses Copilot chat to perform wiki tasks
2. **CLI mode**: Agent or human uses terminal commands with `--backend bedrock`

## Acceptance Criteria

### AC1: Human can use chat for wiki operations

- [ ] Human asks Copilot: "Ingest this PDF" → Copilot runs `pnpm wiki:phase0`, edits files, validates
- [ ] Human asks Copilot: "Query the wiki about X" → Copilot reads wiki pages, answers
- [ ] Human asks Copilot: "Run maintenance checks" → Copilot runs `pnpm wiki:maintenance`
- [ ] AGENTS.md provides sufficient guidance for Copilot to complete tasks

### AC2: Agent can use CLI for wiki operations

- [ ] `WIKI_MODEL_BACKEND=bedrock pnpm wiki:phase2-single slug page.md` works
- [ ] `WIKI_MODEL_BACKEND=bedrock pnpm wiki:query "question"` works
- [ ] `pnpm wiki:maintenance` works (deterministic, no model needed)
- [ ] Backend selection via environment variable or `--backend` flag

### AC3: Codespaces environment works

- [ ] `.devcontainer/devcontainer.json` configures AWS CLI
- [ ] SSO authentication works: `aws configure sso --profile sdai-dev`
- [ ] Bedrock API calls succeed from Codespace

---

## Phase 1: Backend Abstraction (Foundation)

**Duration**: 1-2 hours

### 1.1 Create `tools/wiki_model_backend.py`

```python
# Abstract interface + backend registry
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path

@dataclass
class ModelConfig:
    worktree: Path
    prefix: str
    timeout: int = 600
    task_description: str = ""
    validation_command: str = ""

@dataclass  
class ModelResponse:
    success: bool
    output: str
    log_paths: list[Path] = None
    stop_reason: str = None
    usage: dict = None
    error: str = None

class ModelBackend(ABC):
    @abstractmethod
    def run(self, prompt: str, config: ModelConfig) -> ModelResponse:
        pass

def get_backend(name: str = None) -> ModelBackend:
    """Factory function for backend selection."""
    ...
```

### 1.2 Move existing `run_codex()` into `CodexBackend`

- Extract from `wiki_phase1_benchmark.py`
- Wrap in `CodexBackend` class
- Keep backward compatibility

### 1.3 Add output parsing utilities

- `parse_model_output()` - extract file contents from fenced blocks
- `check_response_completeness()` - detect truncation

**Validation**:
```bash
python3 -c "from tools.wiki_model_backend import get_backend; print(get_backend('codex'))"
```

---

## Phase 2: Bedrock Backend

**Duration**: 2-3 hours

### 2.1 Implement `BedrockBackend`

```python
class BedrockBackend(ModelBackend):
    def __init__(self, model_id: str, region: str, max_tokens: int, temperature: float):
        ...
    
    def run(self, prompt: str, config: ModelConfig) -> ModelResponse:
        # boto3 converse() call
        ...
```

### 2.2 Add boto3 dependency

```bash
# requirements.txt (optional dependency)
boto3>=1.34.0
```

### 2.3 Add system prompt builder

- Read AGENTS.md
- Add working directory context
- Add output format instructions

### 2.4 Add response parsing

- Parse fenced code blocks into file writes
- Validate paths are within worktree
- Handle truncation

**Validation**:
```bash
export AWS_PROFILE=sdai-dev
export AWS_REGION=us-east-1
python3 -c "
from tools.wiki_model_backend import get_backend
backend = get_backend('bedrock')
print(f'Backend ready: {backend.model_id}')
"
```

---

## Phase 3: CLI Integration

**Duration**: 1-2 hours

### 3.1 Update `wiki_phase2_single.py`

- Add `--backend` flag
- Use `get_backend()` instead of direct `run_codex()`
- Pass worktree and config to backend

### 3.2 Update `wiki_phase1_benchmark.py`

- Same pattern as phase2

### 3.3 Update `wiki_query.py`

- Add `--backend` flag for model-based queries

### 3.4 Update `wiki_model_defaults.json`

```json
{
  "backend": "bedrock",
  "backends": {
    "bedrock": {
      "type": "scripted",
      "region": "us-east-1",
      "model_id": "anthropic.claude-sonnet-4-20250514-v1:0"
    }
  }
}
```

**Validation**:
```bash
WIKI_MODEL_BACKEND=bedrock pnpm wiki:phase2-single aoe2-basics ../concepts/test.md --dry-run
```

---

## Phase 4: Codespaces Configuration

**Duration**: 30 minutes

### 4.1 Create `.devcontainer/devcontainer.json`

```json
{
  "name": "llm-wiki",
  "image": "mcr.microsoft.com/devcontainers/python:3.11",
  "features": {
    "ghcr.io/devcontainers/features/aws-cli:1": {},
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "postCreateCommand": "pnpm install && pip install -r requirements.txt",
  "containerEnv": {
    "AWS_REGION": "us-east-1"
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "github.copilot",
        "github.copilot-chat"
      ]
    }
  }
}
```

### 4.2 Create `.github/copilot-instructions.md`

```markdown
# Copilot Instructions for llm-wiki

Read and follow [AGENTS.md](../AGENTS.md) for all wiki maintenance tasks.

## Quick Reference

### Ingest a PDF
1. `pnpm wiki:phase0 raw/inbox/<file.pdf> <slug>`
2. Create/update `wiki/sources/<slug>.md`
3. `pnpm wiki:check-source <slug>`

### Query the Wiki
1. Read `wiki/index.md` to find relevant pages
2. Read specific wiki pages
3. Answer from wiki content

### Maintenance
- `pnpm wiki:lint`
- `pnpm wiki:maintenance --append-log`
```

### 4.3 Document SSO setup

Add to README or create `docs/codespaces-setup.md`:
```bash
# One-time setup in Codespace
aws configure sso --profile sdai-dev

# Set environment
export AWS_PROFILE=sdai-dev
export WIKI_MODEL_BACKEND=bedrock
```

**Validation**:
- Open repo in Codespace
- Verify AWS CLI available
- Verify Copilot can read instructions

---

## Phase 5: End-to-End Testing

**Duration**: 1-2 hours

### 5.1 Test Interactive Mode (Copilot)

| Test | Steps | Expected |
|---|---|---|
| Simple query | Ask "What's in the wiki?" | Copilot reads index.md, lists pages |
| Maintenance | Ask "Run wiki lint" | Copilot runs `pnpm wiki:lint`, reports results |
| Phase 0 | Drop PDF in inbox, ask "Ingest test.pdf" | Copilot runs phase0, creates normalized source |

### 5.2 Test CLI Mode (Terminal)

```bash
# Test Bedrock connectivity
aws bedrock list-foundation-models --region us-east-1 --profile sdai-dev | head -20

# Test backend initialization
WIKI_MODEL_BACKEND=bedrock python3 -c "
from tools.wiki_model_backend import get_backend
b = get_backend()
print(b)
"

# Test dry-run synthesis
WIKI_MODEL_BACKEND=bedrock pnpm wiki:phase2-single aoe2-basics ../concepts/test.md --dry-run

# Test actual synthesis (if safe)
# WIKI_MODEL_BACKEND=bedrock pnpm wiki:phase2-single aoe2-basics ../concepts/aoe2-economy-balance.md
```

### 5.3 Test Hybrid Mode

1. Agent runs `pnpm wiki:phase0` via terminal
2. Human asks Copilot to complete Phase 1
3. Agent runs `pnpm wiki:check-source` via terminal
4. Human asks Copilot to fix issues

---

## Implementation Order

```
Phase 1: Backend Abstraction
    ↓
Phase 2: Bedrock Backend
    ↓
Phase 3: CLI Integration
    ↓
Phase 4: Codespaces Config
    ↓
Phase 5: Testing
```

**Total estimated time**: 5-8 hours

---

## Files to Create/Modify

| File | Action | Description |
|---|---|---|
| `tools/wiki_model_backend.py` | Create | Backend abstraction + implementations |
| `tools/wiki_phase1_benchmark.py` | Modify | Use backend abstraction |
| `tools/wiki_phase2_single.py` | Modify | Use backend abstraction |
| `tools/wiki_query.py` | Modify | Add --backend flag |
| `tools/wiki_model_defaults.json` | Modify | Add bedrock config |
| `requirements.txt` | Create | Add boto3 |
| `.devcontainer/devcontainer.json` | Create | Codespaces config |
| `.github/copilot-instructions.md` | Create | Copilot guidance |

---

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Bedrock model not available in us-east-1 | Check model availability first, fallback to us-west-2 |
| SSO auth expires mid-task | Document refresh: `aws sso login --profile sdai-dev` |
| Output parsing fails | Add robust error handling, fallback to raw output |
| Context too large for Bedrock | Use existing context limits from DESIGN_local-model-context-limits.md |

---

## Definition of Done

- [ ] `tools/wiki_model_backend.py` exists with CodexBackend and BedrockBackend
- [ ] `--backend bedrock` flag works on wiki:phase2-single
- [ ] `.devcontainer/devcontainer.json` configures Codespaces correctly
- [ ] `.github/copilot-instructions.md` guides Copilot to use AGENTS.md
- [ ] Human successfully completes one ingest via Copilot chat
- [ ] Agent successfully runs one CLI command with Bedrock backend
- [ ] Tests pass for output parsing and truncation detection
