"""Local LLM-Wiki harness.

Connects a locally served Qwen3-14B (llama-server, via forge's guardrailed
WorkflowRunner) to the three-layer wiki described in docs/llm-wiki.md:
immutable raw sources, an LLM-maintained wiki, and a SCHEMA.md conventions
document.
"""
