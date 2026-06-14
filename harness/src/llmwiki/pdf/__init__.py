"""PDF ingestion pipeline (docs/2026-06-11-pdf-ingestion-design.md).

Pure domain logic (classify, chunking, manifest, OCR folding) plus thin
adapters for PyMuPDF extraction and the TextRecognizer OCR port.
"""


class PdfError(Exception):
    """PDF pipeline failure; message is safe to show the user."""


class ScannedPdfError(PdfError):
    """Detected an image-only PDF; the OCR page path is not enabled yet."""
