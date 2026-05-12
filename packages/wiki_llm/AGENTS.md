# wiki_llm — Package Rules

> LLM backend abstraction, prompt management, and response parsing.

---

## Purpose

This package provides a unified interface for LLM interactions:

- Multiple backend support (Bedrock, OpenAI, Anthropic, Codex CLI)
- System prompt loading and template management
- Model output parsing (file extraction, JSON extraction)

---

## Design constraints

1. **May depend on wiki_core and wiki_io.** Can import types from both.
2. **Backend SDKs are optional.** Each backend's SDK is an optional dependency.
3. **No wiki content logic.** This package handles LLM communication, not wiki semantics.
4. **Lazy client initialization.** SDK clients are created on first use, not import.

---

## Module structure

```
wiki_llm/
├── backends/        # LLM backend implementations
│   ├── types.py     # ModelConfig, ModelResponse
│   ├── base.py      # ModelBackend abstract base class
│   ├── bedrock.py   # AWS Bedrock (boto3)
│   ├── openai.py    # OpenAI API
│   ├── anthropic.py # Anthropic API
│   └── codex.py     # Local Codex CLI
├── prompts/         # Prompt loading utilities
│   └── loader.py    # load_system_prompt(), load_prompt_template()
└── responses/       # Output parsing
    └── parser.py    # parse_model_output(), extract_json_from_output()
```

---

## Import conventions

```python
# Preferred: import from submodules
from wiki_llm.backends import get_backend, ModelConfig, ModelResponse
from wiki_llm.prompts import load_system_prompt
from wiki_llm.responses import parse_model_output

# Get backend from environment or explicit name
backend = get_backend()  # Uses WIKI_MODEL_BACKEND env var
backend = get_backend("bedrock")  # Explicit backend
```

---

## Backend selection

The `get_backend()` function selects a backend in this priority order:

1. Explicit `name` parameter
2. `WIKI_MODEL_BACKEND` environment variable
3. Default from `tools/wiki_model_defaults.json`
4. Fallback to `"codex"`

Supported backends:

| Name        | SDK         | Environment Variables       |
| ----------- | ----------- | --------------------------- |
| `bedrock`   | `boto3`     | `AWS_PROFILE`, `AWS_REGION` |
| `openai`    | `openai`    | `OPENAI_API_KEY`            |
| `anthropic` | `anthropic` | `ANTHROPIC_API_KEY`         |
| `codex`     | (CLI)       | None (uses local Codex CLI) |

---

## System prompt styles

The `load_system_prompt(style)` function supports these styles:

| Style              | Description         | Token Budget |
| ------------------ | ------------------- | ------------ |
| `"full"`           | Complete AGENTS.md  | ~7K          |
| `"synthesis"`      | Wiki page synthesis | ~800         |
| `"synthesis-json"` | JSON schema output  | ~500         |
| `"extract"`        | Claim extraction    | ~500         |
| `"query"`          | Query answering     | ~400         |
| `"judge"`          | Claim judging       | ~400         |

Prompt templates live in `tools/prompts/`.

---

## Response parsing

Model outputs often contain fenced code blocks with file paths:

````markdown
Here's the updated page:

```wiki/concepts/example.md
---
title: Example
---
# Example

Content here.
`` `
```
````

Use `parse_model_output()` to extract files:

```python
from wiki_llm.responses import parse_model_output

files = parse_model_output(response.output)
# {'wiki/concepts/example.md': '---\ntitle: Example\n...'}
```

---

## Testing

Tests live in `packages/wiki_llm/tests/`. Run with:

```bash
python -m pytest packages/wiki_llm/tests/ -v
```

Tests do not make actual LLM API calls. They test:

- Configuration handling
- Response parsing
- Prompt loading

Before merging changes:

1. All tests must pass.
2. New backends must follow the `ModelBackend` interface.
3. SDK imports must be lazy (inside methods, not at module level).

---

## When to add code here

Add code to `wiki_llm` when:

- It communicates with an LLM API
- It parses LLM output into structured data
- It manages prompts or model configuration

Do **not** add code here if it:

- Is a pure data type → use `wiki_core`
- Reads/writes wiki state files → use `wiki_io`
- Contains wiki-specific business logic → keep in `tools/`
