"""wiki_llm — LLM interaction layer for wiki ingestion pipeline.

This package provides model backend abstractions and utilities:
- backends: Multiple LLM backend support (Bedrock, OpenAI, Anthropic, Codex)
- prompts: System prompt loading and templates
- responses: Model output parsing

Usage:
    from wiki_llm.backends import get_backend, ModelConfig
    from wiki_llm.prompts import load_system_prompt
    from wiki_llm.responses import parse_model_output
    
    backend = get_backend("bedrock")
    config = ModelConfig(worktree=Path("."), prefix="phase2")
    response = backend.run(prompt, config)
    files = parse_model_output(response.output)
"""
