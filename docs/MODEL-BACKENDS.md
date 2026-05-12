# Model Backends

This document explains how to configure and use the LLM model backends for wiki ingestion and chat operations.

## Backend Overview

The wiki pipeline supports multiple LLM backends:

| Backend     | Description                   | Use Case                      |
| ----------- | ----------------------------- | ----------------------------- |
| `bedrock`   | AWS Bedrock managed inference | Cloud/Codespaces (default)    |
| `codex`     | Local Codex CLI with ollama   | Local machine with GPU (4090) |
| `openai`    | OpenAI API                    | Cloud with OpenAI account     |
| `anthropic` | Anthropic API                 | Cloud with Anthropic account  |

## Backend Selection

Backend selection follows this priority order:

1. **Explicit `--backend` flag** on CLI commands
2. **`WIKI_MODEL_BACKEND`** environment variable
3. **Default from `tools/wiki_model_defaults.json`**
4. **Fallback to `"codex"`**

### Selection Code Path

```
CLI command (e.g., pnpm wiki:ingest)
    ↓
wiki_llm.backends.get_backend(name=None)
    ↓
1. Check explicit name parameter
2. Check os.environ["WIKI_MODEL_BACKEND"]
3. Load default from tools/wiki_model_defaults.json
4. Fall back to "codex"
    ↓
Return CodexBackend, BedrockBackend, OpenAIBackend, or AnthropicBackend
```

---

## Bedrock Backend (Cloud/Codespaces)

Use this backend when running in GitHub Codespaces or any cloud environment with AWS access.

### Environment Setup

```bash
# Set environment variables
export AWS_PROFILE=sdai-dev
export AWS_REGION=us-east-1
export WIKI_MODEL_BACKEND=bedrock
```

The devcontainer already configures these in `.devcontainer/devcontainer.json`.

### AWS SSO Authentication

```bash
# First-time setup (or after credential expiry)
aws configure sso --profile sdai-dev

# Authenticate (refresh as needed)
aws sso login --profile sdai-dev

# Verify credentials work
aws bedrock list-foundation-models --region us-east-1 --profile sdai-dev | head -5
```

### Running Ingestion with Bedrock

```bash
# Explicit backend flag
pnpm wiki:ingest raw/inbox/document.pdf --slug my-doc --backend bedrock

# Or rely on WIKI_MODEL_BACKEND environment variable
export WIKI_MODEL_BACKEND=bedrock
pnpm wiki:ingest raw/inbox/document.pdf --slug my-doc
```

### Running Chat/Query with Bedrock

```bash
pnpm wiki:query "What is the main concept?" --backend bedrock
```

### Bedrock Configuration

From `tools/wiki_model_defaults.json`:

```json
{
  "bedrock": {
    "region": "us-east-1",
    "model_id": "qwen.qwen3-coder-30b-a3b-v1:0",
    "max_tokens": 8192,
    "temperature": 0.1
  }
}
```

| Parameter     | Default                         | Description                      |
| ------------- | ------------------------------- | -------------------------------- |
| `region`      | `us-east-1`                     | AWS region (or `AWS_REGION` env) |
| `model_id`    | `qwen.qwen3-coder-30b-a3b-v1:0` | Bedrock model identifier         |
| `max_tokens`  | `8192`                          | Maximum output tokens            |
| `temperature` | `0.1`                           | Sampling temperature             |

---

## Codex Backend (Local 4090)

Use this backend when running on a local machine with a GPU (e.g., RTX 4090) and the Codex CLI installed.

### Prerequisites

1. **Codex CLI installed**: The `codex` command must be available on PATH
2. **Ollama running**: Local model server with the appropriate model loaded
3. **GPU available**: CUDA-compatible GPU for inference

### Environment Setup

```bash
# No environment variables required, but you can set defaults
export WIKI_MODEL_BACKEND=codex  # Optional, codex is the fallback default
```

### Running Ingestion with Codex

```bash
# Explicit backend flag
pnpm wiki:ingest raw/inbox/document.pdf --slug my-doc --backend codex

# Or use the default (codex is fallback)
pnpm wiki:ingest raw/inbox/document.pdf --slug my-doc
```

### Running Chat/Query with Codex

```bash
pnpm wiki:query "What is the main concept?" --backend codex
```

### Codex Configuration

From `tools/wiki_model_defaults.json`:

```json
{
  "codex": {
    "bin": "codex",
    "default_profile": "local-4090"
  }
}
```

| Parameter         | Default      | Description                       |
| ----------------- | ------------ | --------------------------------- |
| `bin`             | `codex`      | Path to Codex CLI executable      |
| `default_profile` | `local-4090` | Codex profile for model selection |

### Using a Different Candidate Profile

The `--candidate` flag selects a model profile for synthesis:

```bash
pnpm wiki:ingest raw/inbox/document.pdf --slug my-doc --candidate local-4090
```

---

## OpenAI Backend

### Environment Setup

```bash
export OPENAI_API_KEY=sk-...
export WIKI_MODEL_BACKEND=openai
```

### Configuration

```json
{
  "openai": {
    "api_key_env": "OPENAI_API_KEY",
    "model": "gpt-4o",
    "max_tokens": 8192,
    "temperature": 0.1
  }
}
```

---

## Anthropic Backend

### Environment Setup

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export WIKI_MODEL_BACKEND=anthropic
```

### Configuration

```json
{
  "anthropic": {
    "api_key_env": "ANTHROPIC_API_KEY",
    "model": "claude-sonnet-4-20250514",
    "max_tokens": 8192,
    "temperature": 0.1
  }
}
```

---

## Quick Reference

### Bedrock (Codespaces/Cloud)

```bash
aws sso login --profile sdai-dev
export AWS_PROFILE=sdai-dev AWS_REGION=us-east-1 WIKI_MODEL_BACKEND=bedrock
pnpm wiki:ingest raw/inbox/file.pdf --slug my-doc
```

### Codex (Local 4090)

```bash
pnpm wiki:ingest raw/inbox/file.pdf --slug my-doc --backend codex
```

---

## Architecture

The backend system is implemented in `packages/wiki_llm/`:

```
packages/wiki_llm/src/wiki_llm/backends/
├── __init__.py     # get_backend() factory function
├── types.py        # ModelConfig, ModelResponse dataclasses
├── base.py         # ModelBackend abstract base class
├── bedrock.py      # BedrockBackend (boto3)
├── codex.py        # CodexBackend (subprocess CLI)
├── openai.py       # OpenAIBackend (openai SDK)
└── anthropic.py    # AnthropicBackend (anthropic SDK)
```

### Using Backends in Code

```python
from wiki_llm.backends import get_backend, ModelConfig, ModelResponse

# Get backend from environment or explicit name
backend = get_backend()          # Uses WIKI_MODEL_BACKEND env var
backend = get_backend("bedrock") # Explicit backend

# Configure and run
config = ModelConfig(
    worktree=Path("/tmp/work"),
    prefix="phase2",
    timeout=900,
)
response: ModelResponse = backend.run(prompt, config)

if response.success:
    print(response.output)
else:
    print(f"Error: {response.error}")
```

---

## Troubleshooting

### Bedrock: "Unable to locate credentials"

```bash
# Re-authenticate with SSO
aws configure sso --profile sdai-dev
aws sso login --profile sdai-dev
```

### Bedrock: "Access denied" or model not available

- Verify the model is enabled in your AWS account
- Check the region matches where the model is available

### Codex: "command not found"

- Ensure `codex` CLI is installed and on PATH
- Check that ollama is running with the model loaded

### General: Wrong backend being used

```bash
# Check current backend
echo $WIKI_MODEL_BACKEND

# Force a specific backend
pnpm wiki:ingest ... --backend bedrock
```
