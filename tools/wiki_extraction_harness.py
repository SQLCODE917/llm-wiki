#!/usr/bin/env python3
"""Test harness for PDF extraction and chunking evaluation.

Compares different extractors (marker, pymupdf, docling, pdfplumber) and
evaluates chunking quality. Use this to select the best extractor for
a document class.

Usage:
    # Compare extractors on a PDF
    python3 tools/wiki_extraction_harness.py raw/inbox/book.pdf --slug book
    
    # Test with specific extractors
    python3 tools/wiki_extraction_harness.py raw/inbox/book.pdf --extractors marker,pymupdf
    
    # Compare chunking strategies
    python3 tools/wiki_extraction_harness.py raw/inbox/book.pdf --compare-chunking
    
    # Full evaluation with benchmark
    python3 tools/wiki_extraction_harness.py raw/inbox/book.pdf --full-eval
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

# Import our structured chunking module
from wiki_structured_chunking import (
    BlockExtractor, StructuralChunker, ChunkConfig,
    Block, StructuredChunk, QualityReport,
    assess_extraction_quality, count_tokens,
    save_blocks, save_chunks,
)


# ============================================================================
# Extraction Backend Protocol
# ============================================================================

@dataclass
class ExtractionResult:
    """Result from an extraction backend."""
    extractor: str
    success: bool
    markdown_path: Path | None
    markdown_text: str
    extraction_time: float
    error: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    # Quality metrics (filled by analyze)
    char_count: int = 0
    line_count: int = 0
    token_count: int = 0
    page_count: int = 0
    table_count: int = 0
    code_block_count: int = 0
    heading_count: int = 0
    quality_issues: list[str] = field(default_factory=list)


@dataclass
class ChunkingResult:
    """Result from chunking evaluation."""
    strategy: str
    config: ChunkConfig
    blocks: list[Block]
    chunks: list[StructuredChunk]
    quality_report: QualityReport
    chunking_time: float


@dataclass
class ComparisonReport:
    """Full comparison report across extractors and strategies."""
    source_path: str
    source_hash: str
    extraction_results: list[ExtractionResult]
    chunking_results: list[ChunkingResult]
    recommendations: dict[str, str]
    generated_at: str

    def to_dict(self) -> dict:
        return {
            "source_path": self.source_path,
            "source_hash": self.source_hash,
            "extraction_results": [
                {
                    "extractor": r.extractor,
                    "success": r.success,
                    "extraction_time": r.extraction_time,
                    "char_count": r.char_count,
                    "line_count": r.line_count,
                    "token_count": r.token_count,
                    "page_count": r.page_count,
                    "table_count": r.table_count,
                    "code_block_count": r.code_block_count,
                    "heading_count": r.heading_count,
                    "quality_issues": r.quality_issues,
                    "error": r.error,
                }
                for r in self.extraction_results
            ],
            "chunking_results": [
                {
                    "strategy": r.strategy,
                    "config": {
                        "target_tokens": r.config.target_tokens,
                        "soft_max_tokens": r.config.soft_max_tokens,
                        "hard_max_tokens": r.config.hard_max_tokens,
                    },
                    "block_count": len(r.blocks),
                    "chunk_count": len(r.chunks),
                    "total_tokens": r.quality_report.total_tokens,
                    "avg_tokens_per_chunk": r.quality_report.total_tokens / len(r.chunks) if r.chunks else 0,
                    "pages_needing_review": r.quality_report.pages_needing_review,
                    "issues_by_type": r.quality_report.issues_by_type,
                    "chunking_time": r.chunking_time,
                }
                for r in self.chunking_results
            ],
            "recommendations": self.recommendations,
            "generated_at": self.generated_at,
        }


# ============================================================================
# Extraction Backends
# ============================================================================

def extract_with_marker(
    source: Path,
    output_dir: Path,
    marker_bin: str = "marker_single",
) -> ExtractionResult:
    """Extract PDF using marker."""
    start = time.time()

    if not shutil.which(marker_bin):
        return ExtractionResult(
            extractor="marker",
            success=False,
            markdown_path=None,
            markdown_text="",
            extraction_time=0,
            error="marker_single not found in PATH",
        )

    try:
        output_dir.mkdir(parents=True, exist_ok=True)

        env = os.environ.copy()
        env["TORCH_DEVICE"] = env.get("TORCH_DEVICE", "cuda")

        result = subprocess.run(
            [
                marker_bin,
                str(source),
                "--output_format", "markdown",
                "--output_dir", str(output_dir),
                "--disable_tqdm",
            ],
            env=env,
            capture_output=True,
            text=True,
            timeout=600,
        )

        elapsed = time.time() - start

        if result.returncode != 0:
            return ExtractionResult(
                extractor="marker",
                success=False,
                markdown_path=None,
                markdown_text="",
                extraction_time=elapsed,
                error=result.stderr[:500],
            )

        # Find output markdown
        md_files = list(output_dir.rglob("*.md"))
        if not md_files:
            return ExtractionResult(
                extractor="marker",
                success=False,
                markdown_path=None,
                markdown_text="",
                extraction_time=elapsed,
                error="No markdown output produced",
            )

        md_path = md_files[0]
        md_text = md_path.read_text()

        return ExtractionResult(
            extractor="marker",
            success=True,
            markdown_path=md_path,
            markdown_text=md_text,
            extraction_time=elapsed,
        )

    except subprocess.TimeoutExpired:
        return ExtractionResult(
            extractor="marker",
            success=False,
            markdown_path=None,
            markdown_text="",
            extraction_time=600,
            error="Extraction timed out after 600s",
        )
    except Exception as e:
        return ExtractionResult(
            extractor="marker",
            success=False,
            markdown_path=None,
            markdown_text="",
            extraction_time=time.time() - start,
            error=str(e),
        )


def extract_with_pymupdf(source: Path, output_dir: Path) -> ExtractionResult:
    """Extract PDF using PyMuPDF."""
    start = time.time()

    try:
        import pymupdf
    except ImportError:
        return ExtractionResult(
            extractor="pymupdf",
            success=False,
            markdown_path=None,
            markdown_text="",
            extraction_time=0,
            error="pymupdf not installed (pip install pymupdf)",
        )

    try:
        doc = pymupdf.open(source)
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / "source.md"
        page_count = doc.page_count

        lines = []
        lines.append(f"# {source.stem}\n")
        lines.append(f"*Extracted from {source.name} ({page_count} pages)*\n")

        for page_num in range(page_count):
            page = doc[page_num]
            text = page.get_text("text")

            if text.strip():
                lines.append(f"\n---\n<!-- page {page_num + 1} -->\n\n")
                lines.append(text)

        doc.close()

        md_text = "\n".join(lines)
        output_path.write_text(md_text)
        elapsed = time.time() - start

        return ExtractionResult(
            extractor="pymupdf",
            success=True,
            markdown_path=output_path,
            markdown_text=md_text,
            extraction_time=elapsed,
            metadata={"page_count": page_count},
        )

    except Exception as e:
        return ExtractionResult(
            extractor="pymupdf",
            success=False,
            markdown_path=None,
            markdown_text="",
            extraction_time=time.time() - start,
            error=str(e),
        )


def extract_with_pymupdf4llm(source: Path, output_dir: Path) -> ExtractionResult:
    """Extract PDF using PyMuPDF4LLM (optimized for LLM/RAG)."""
    start = time.time()

    try:
        import pymupdf4llm
    except ImportError:
        return ExtractionResult(
            extractor="pymupdf4llm",
            success=False,
            markdown_path=None,
            markdown_text="",
            extraction_time=0,
            error="pymupdf4llm not installed (pip install pymupdf4llm)",
        )

    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / "source.md"

        # Use pymupdf4llm's markdown extraction
        md_text = pymupdf4llm.to_markdown(str(source))
        output_path.write_text(md_text)

        elapsed = time.time() - start

        return ExtractionResult(
            extractor="pymupdf4llm",
            success=True,
            markdown_path=output_path,
            markdown_text=md_text,
            extraction_time=elapsed,
        )

    except Exception as e:
        return ExtractionResult(
            extractor="pymupdf4llm",
            success=False,
            markdown_path=None,
            markdown_text="",
            extraction_time=time.time() - start,
            error=str(e),
        )


def extract_with_docling(source: Path, output_dir: Path) -> ExtractionResult:
    """Extract PDF using Docling."""
    start = time.time()

    try:
        from docling.document_converter import DocumentConverter
    except ImportError:
        return ExtractionResult(
            extractor="docling",
            success=False,
            markdown_path=None,
            markdown_text="",
            extraction_time=0,
            error="docling not installed (pip install docling)",
        )

    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / "source.md"

        converter = DocumentConverter()
        result = converter.convert(str(source))

        # Export as markdown
        md_text = result.document.export_to_markdown()
        output_path.write_text(md_text)

        elapsed = time.time() - start

        return ExtractionResult(
            extractor="docling",
            success=True,
            markdown_path=output_path,
            markdown_text=md_text,
            extraction_time=elapsed,
        )

    except Exception as e:
        return ExtractionResult(
            extractor="docling",
            success=False,
            markdown_path=None,
            markdown_text="",
            extraction_time=time.time() - start,
            error=str(e),
        )


def extract_with_pdfplumber(source: Path, output_dir: Path) -> ExtractionResult:
    """Extract PDF using pdfplumber."""
    start = time.time()

    try:
        import pdfplumber
    except ImportError:
        return ExtractionResult(
            extractor="pdfplumber",
            success=False,
            markdown_path=None,
            markdown_text="",
            extraction_time=0,
            error="pdfplumber not installed (pip install pdfplumber)",
        )

    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / "source.md"

        lines = []
        lines.append(f"# {source.stem}\n")

        with pdfplumber.open(source) as pdf:
            lines.append(
                f"*Extracted from {source.name} ({len(pdf.pages)} pages)*\n")

            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    lines.append(f"\n---\n<!-- page {i + 1} -->\n\n")
                    lines.append(text)

                # Try to extract tables
                tables = page.extract_tables()
                for table in tables:
                    if table and len(table) > 1:
                        lines.append("\n")
                        # Convert to markdown table
                        for j, row in enumerate(table):
                            cleaned = [str(cell or "").replace("\n", " ")
                                       for cell in row]
                            lines.append("| " + " | ".join(cleaned) + " |")
                            if j == 0:
                                lines.append(
                                    "|" + "|".join(["---"] * len(row)) + "|")
                        lines.append("\n")

        md_text = "\n".join(lines)
        output_path.write_text(md_text)
        elapsed = time.time() - start

        return ExtractionResult(
            extractor="pdfplumber",
            success=True,
            markdown_path=output_path,
            markdown_text=md_text,
            extraction_time=elapsed,
        )

    except Exception as e:
        return ExtractionResult(
            extractor="pdfplumber",
            success=False,
            markdown_path=None,
            markdown_text="",
            extraction_time=time.time() - start,
            error=str(e),
        )


EXTRACTORS = {
    "marker": extract_with_marker,
    "pymupdf": extract_with_pymupdf,
    "pymupdf4llm": extract_with_pymupdf4llm,
    "docling": extract_with_docling,
    "pdfplumber": extract_with_pdfplumber,
}


# ============================================================================
# Analysis Functions
# ============================================================================

def analyze_extraction(result: ExtractionResult) -> ExtractionResult:
    """Analyze extraction result for quality metrics."""
    if not result.success:
        return result

    text = result.markdown_text
    lines = text.split('\n')

    result.char_count = len(text)
    result.line_count = len(lines)
    result.token_count = count_tokens(text)

    # Count pages
    page_markers = re.findall(
        r'<!--\s*page\s*(\d+)\s*-->', text, re.IGNORECASE)
    result.page_count = max(map(int, page_markers)) if page_markers else 0

    # Count tables
    result.table_count = len(re.findall(r'^\|.*\|$', text, re.MULTILINE))

    # Count code blocks
    result.code_block_count = text.count('```')

    # Count headings
    result.heading_count = len(re.findall(r'^#{1,6}\s', text, re.MULTILINE))

    # Detect quality issues
    issues = []

    # Replacement characters
    replacement_count = text.count('\ufffd')
    if replacement_count > 0:
        issues.append(f"replacement_chars:{replacement_count}")

    # Broken ligatures
    for lig in ['ﬁ', 'ﬂ', 'ﬀ', 'ﬃ', 'ﬄ']:
        if lig in text:
            issues.append("broken_ligatures")
            break

    # Very short lines (OCR artifacts)
    short_lines = sum(1 for line in lines if 0 < len(line.strip()) < 3)
    if short_lines > len(lines) * 0.1:
        issues.append(f"short_lines:{short_lines}")

    # Suspicious patterns
    if text.count(' . . . ') > 10:
        issues.append("toc_artifacts")

    if re.search(r'(\d)\1{5,}', text):
        issues.append("repeated_digits")

    result.quality_issues = issues

    return result


def evaluate_chunking(
    markdown_text: str,
    doc_id: str,
    strategy: str,
    config: ChunkConfig,
) -> ChunkingResult:
    """Evaluate a chunking strategy on markdown text."""
    start = time.time()

    # Extract blocks
    extractor = BlockExtractor()
    blocks = extractor.extract_from_markdown(markdown_text, doc_id)

    # Pack chunks
    chunker = StructuralChunker(config)
    chunks = chunker.pack(blocks, doc_id)

    # Assess quality
    quality = assess_extraction_quality(blocks, chunks)

    elapsed = time.time() - start

    return ChunkingResult(
        strategy=strategy,
        config=config,
        blocks=blocks,
        chunks=chunks,
        quality_report=quality,
        chunking_time=elapsed,
    )


# ============================================================================
# Main Harness
# ============================================================================

def run_extraction_comparison(
    source: Path,
    output_dir: Path,
    extractors: list[str] | None = None,
) -> list[ExtractionResult]:
    """Run multiple extractors and compare results."""
    if extractors is None:
        extractors = ["marker", "pymupdf", "docling"]

    results = []

    for name in extractors:
        if name not in EXTRACTORS:
            print(f"  SKIP: Unknown extractor '{name}'")
            continue

        print(f"  Running {name}...")
        extractor_output = output_dir / name
        result = EXTRACTORS[name](source, extractor_output)
        result = analyze_extraction(result)
        results.append(result)

        if result.success:
            print(
                f"    ✓ {result.char_count:,} chars, {result.token_count:,} tokens in {result.extraction_time:.1f}s")
            if result.quality_issues:
                print(f"    ⚠ Issues: {', '.join(result.quality_issues)}")
        else:
            print(f"    ✗ Failed: {result.error}")

    return results


def run_chunking_comparison(
    markdown_text: str,
    doc_id: str,
) -> list[ChunkingResult]:
    """Compare different chunking configurations."""
    configs = [
        ("default", ChunkConfig()),
        ("dense_code", ChunkConfig(
            target_tokens=4500,
            soft_max_tokens=5500,
            hard_max_tokens=7000,
        )),
        ("large_prose", ChunkConfig(
            target_tokens=7500,
            soft_max_tokens=8500,
            hard_max_tokens=10000,
        )),
        ("conservative", ChunkConfig(
            target_tokens=5000,
            soft_max_tokens=6000,
            hard_max_tokens=7500,
        )),
    ]

    results = []

    for name, config in configs:
        print(f"  Evaluating {name} strategy...")
        result = evaluate_chunking(markdown_text, doc_id, name, config)
        results.append(result)

        avg_tokens = result.quality_report.total_tokens / \
            len(result.chunks) if result.chunks else 0
        print(
            f"    {len(result.chunks)} chunks, avg {avg_tokens:.0f} tokens/chunk")

    return results


def generate_recommendations(
    extraction_results: list[ExtractionResult],
    chunking_results: list[ChunkingResult],
) -> dict[str, str]:
    """Generate recommendations based on results."""
    recommendations = {}

    # Best extractor by quality (fewer issues)
    successful = [r for r in extraction_results if r.success]
    if successful:
        best_quality = min(successful, key=lambda r: len(r.quality_issues))
        recommendations["best_quality_extractor"] = best_quality.extractor

        fastest = min(successful, key=lambda r: r.extraction_time)
        recommendations["fastest_extractor"] = fastest.extractor

        # Best overall (balance quality and speed)
        def score(r: ExtractionResult) -> float:
            quality_penalty = len(r.quality_issues) * 10
            time_penalty = r.extraction_time
            return quality_penalty + time_penalty

        best_overall = min(successful, key=score)
        recommendations["recommended_extractor"] = best_overall.extractor

    # Best chunking strategy
    if chunking_results:
        # Prefer strategies with token counts close to target
        def chunk_score(r: ChunkingResult) -> float:
            avg = r.quality_report.total_tokens / \
                len(r.chunks) if r.chunks else 0
            deviation = abs(avg - r.config.target_tokens)
            issue_penalty = sum(r.quality_report.issues_by_type.values()) * 50
            return deviation + issue_penalty

        best_chunking = min(chunking_results, key=chunk_score)
        recommendations["recommended_chunking"] = best_chunking.strategy

    return recommendations


def compute_file_hash(path: Path) -> str:
    """Compute SHA-256 hash of a file."""
    sha = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            sha.update(chunk)
    return sha.hexdigest()[:16]


def run_full_evaluation(
    source: Path,
    slug: str,
    output_dir: Path,
    extractors: list[str] | None = None,
    compare_chunking: bool = True,
) -> ComparisonReport:
    """Run full extraction and chunking evaluation."""
    from datetime import datetime

    print(f"\n{'='*60}")
    print(f"Extraction Harness: {source.name}")
    print(f"{'='*60}")

    # Run extraction comparison
    print("\n1. Extraction Comparison")
    print("-" * 40)
    extraction_results = run_extraction_comparison(
        source, output_dir, extractors)

    # Run chunking comparison on best extraction
    chunking_results = []
    if compare_chunking:
        successful = [r for r in extraction_results if r.success]
        if successful:
            # Use the extractor with fewest issues
            best = min(successful, key=lambda r: len(r.quality_issues))
            print(f"\n2. Chunking Comparison (using {best.extractor} output)")
            print("-" * 40)
            chunking_results = run_chunking_comparison(
                best.markdown_text, slug)

    # Generate recommendations
    recommendations = generate_recommendations(
        extraction_results, chunking_results)

    # Create report
    report = ComparisonReport(
        source_path=str(source),
        source_hash=compute_file_hash(source),
        extraction_results=extraction_results,
        chunking_results=chunking_results,
        recommendations=recommendations,
        generated_at=datetime.now().isoformat(),
    )

    # Print summary
    print(f"\n3. Recommendations")
    print("-" * 40)
    for key, value in recommendations.items():
        print(f"  {key}: {value}")

    return report


# ============================================================================
# CLI
# ============================================================================

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Test harness for PDF extraction and chunking evaluation"
    )
    parser.add_argument("source", help="PDF file to evaluate")
    parser.add_argument("--slug", default=None, help="Document ID/slug")
    parser.add_argument("--output-dir", default=None, help="Output directory")
    parser.add_argument(
        "--extractors",
        default=None,
        help="Comma-separated list of extractors (marker,pymupdf,docling,pdfplumber,pymupdf4llm)"
    )
    parser.add_argument(
        "--compare-chunking",
        action="store_true",
        help="Compare chunking strategies"
    )
    parser.add_argument(
        "--full-eval",
        action="store_true",
        help="Run full evaluation with all extractors and chunking comparison"
    )
    parser.add_argument(
        "--save-report",
        action="store_true",
        help="Save comparison report as JSON"
    )
    args = parser.parse_args()

    source = Path(args.source)
    if not source.exists():
        print(f"Error: {source} not found")
        return 1

    slug = args.slug or source.stem
    output_dir = Path(args.output_dir) if args.output_dir else Path(
        ".tmp") / "extraction-harness" / slug
    output_dir.mkdir(parents=True, exist_ok=True)

    extractors = None
    if args.extractors:
        extractors = [e.strip() for e in args.extractors.split(",")]

    # Run evaluation
    if args.full_eval:
        extractors = extractors or [
            "marker", "pymupdf", "docling", "pdfplumber"]
        args.compare_chunking = True

    report = run_full_evaluation(
        source, slug, output_dir,
        extractors=extractors,
        compare_chunking=args.compare_chunking,
    )

    # Save report
    if args.save_report or args.full_eval:
        report_path = output_dir / "comparison_report.json"
        report_path.write_text(json.dumps(report.to_dict(), indent=2))
        print(f"\nReport saved to: {report_path}")

    # Save best extraction's blocks and chunks
    if report.chunking_results:
        best_chunking = next(
            (r for r in report.chunking_results
             if r.strategy == report.recommendations.get("recommended_chunking")),
            report.chunking_results[0]
        )

        blocks_path = output_dir / "blocks.jsonl"
        chunks_path = output_dir / "chunks.jsonl"

        save_blocks(best_chunking.blocks, blocks_path)
        save_chunks(best_chunking.chunks, chunks_path)

        print(f"Blocks saved to: {blocks_path}")
        print(f"Chunks saved to: {chunks_path}")

    print(f"\nOutput directory: {output_dir}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
