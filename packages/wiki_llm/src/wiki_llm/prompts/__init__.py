"""Prompt loading and template utilities.

Usage:
    from wiki_llm.prompts import load_system_prompt, load_prompt_template
    
    system = load_system_prompt("synthesis")
    template = load_prompt_template("phase2-synthesis")
"""
from wiki_llm.prompts.loader import (
    load_system_prompt,
    load_prompt_template,
    get_available_prompts,
    PROMPT_FILES,
)


__all__ = [
    "load_system_prompt",
    "load_prompt_template",
    "get_available_prompts",
    "PROMPT_FILES",
]
