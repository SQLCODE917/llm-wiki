"""Folding figure-OCR text into page markdown (pure).

Recognized text lands directly beneath the figure's image reference,
explicitly marked as machine-recognized. Images with no usable text leave
the reference untouched — the normal, silent case.
"""

from __future__ import annotations

import re

_IMAGE_REF_RE = re.compile(r"^!\[[^\]]*\]\(([^)]+)\)\s*$")

OCR_MARKER = "[figure text (OCR, unverified):"


def fold_ocr_into_page(page_md: str, ocr_by_filename: dict[str, str]) -> str:
    """Insert OCR text under each image ref whose file has usable text.

    *ocr_by_filename* maps image file names (not paths) to recognized text;
    files absent from the map are decorative and stay untouched.
    """
    if not ocr_by_filename:
        return page_md
    out: list[str] = []
    for line in page_md.splitlines():
        out.append(line)
        match = _IMAGE_REF_RE.match(line.strip())
        if match:
            filename = match.group(1).rsplit("/", 1)[-1]
            text = ocr_by_filename.get(filename)
            if text:
                out.append("")
                out.append(f"> {OCR_MARKER} {text}]")
    return "\n".join(out)


def relativize_image_refs(page_md: str, absolute_prefix: str) -> str:
    """Rewrite absolute image paths to cache-relative `images/...` refs."""
    prefix = absolute_prefix.rstrip("/") + "/"
    return page_md.replace(prefix, "images/")
