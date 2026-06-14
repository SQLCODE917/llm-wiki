"""Apple Vision adapter for the TextRecognizer port (macOS, on-device).

VNRecognizeTextRequest over an image file URL. Returns [] when Vision finds
no text (the normal case for decorative figures); raises PdfError when the
engine itself fails — empty and error are distinct by design.
"""

# pyobjc populates framework modules dynamically; static analysis can't see
# their attributes.
# pyright: reportAttributeAccessIssue=false

from __future__ import annotations

from pathlib import Path

from llmwiki.pdf import PdfError
from llmwiki.pdf.recognizer import TextSpan


class AppleVisionRecognizer:
    """On-device OCR via the macOS Vision framework (pyobjc)."""

    def recognize(self, image_path: Path) -> list[TextSpan]:
        try:
            import Foundation
            import Vision
        except ImportError as exc:  # non-darwin or missing pyobjc
            raise PdfError(
                "Apple Vision OCR unavailable (pyobjc-framework-Vision not "
                "installed on this platform)."
            ) from exc

        url = Foundation.NSURL.fileURLWithPath_(str(image_path))
        handler = Vision.VNImageRequestHandler.alloc().initWithURL_options_(url, None)
        request = Vision.VNRecognizeTextRequest.alloc().init()
        request.setRecognitionLevel_(Vision.VNRequestTextRecognitionLevelAccurate)

        ok, error = handler.performRequests_error_([request], None)
        if not ok:
            raise PdfError(f"Vision OCR failed on {image_path.name}: {error}")

        spans: list[TextSpan] = []
        for observation in request.results() or []:
            candidate = observation.topCandidates_(1)
            if candidate:
                spans.append(
                    TextSpan(
                        text=str(candidate[0].string()),
                        confidence=float(candidate[0].confidence()),
                    )
                )
        return spans
