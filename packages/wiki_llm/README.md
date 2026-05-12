# wiki_llm

LLM interaction layer for the wiki ingestion pipeline.

## Features

- **Multiple backends**: Bedrock, OpenAI, Anthropic, Codex (local)
- **Unified interface**: Same API across all backends
- **Prompt management**: System prompts and templates
- **Response parsing**: Extract files and JSON from model outputs

## Usage

```python
from wiki_llm.backends import get_backend, ModelConfig
from wiki_llm.prompts import load_system_prompt
from wiki_llm.responses import parse_model_output

# Get backend from environment or explicit name
backend = get_backend("bedrock")  # or WIKI_MODEL_BACKEND env var

# Configure the run
config = ModelConfig(
    worktree=Path("."),
    prefix="phase2",
    system_prompt_style="synthesis",
)

# Run the model
response = backend.run(prompt, config)

# Parse output files
if response.success:
    files = parse_model_output(response.output)
    for path, content in files.items():
        print(f"Generated: {path}")
```

## Backends

| Backend     | Description                   | Requirements                   |
| ----------- | ----------------------------- | ------------------------------ |
| `bedrock`   | AWS Bedrock managed inference | `boto3`, AWS credentials       |
| `openai`    | OpenAI API (GPT-4o)           | `openai`, OPENAI_API_KEY       |
| `anthropic` | Anthropic API (Claude)        | `anthropic`, ANTHROPIC_API_KEY |
| `codex`     | Local models via Codex CLI    | Codex CLI installed            |

## Installation

```bash
pip install -e packages/wiki_llm[all]  # All backends
pip install -e packages/wiki_llm[bedrock]  # AWS Bedrock only
```

## Environment Variables

- `WIKI_MODEL_BACKEND`: Default backend name
- `AWS_PROFILE`, `AWS_REGION`: For Bedrock
- `OPENAI_API_KEY`: For OpenAI
- `ANTHROPIC_API_KEY`: For Anthropic
