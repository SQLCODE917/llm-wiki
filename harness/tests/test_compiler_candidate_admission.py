from llmwiki.domain.compiler_candidate_admission import admit_compiler_page_candidates
from llmwiki.domain.ledger.page_publication import (
    PAGE_FAMILY_PROCEDURE_GUIDE,
    PAGE_FAMILY_RECIPE_PATTERN,
    PageCandidate,
)
from llmwiki.domain.source_profile_selector import select_source_profile
from llmwiki.domain.source_profiles import build_evidence_extraction_plan
from llmwiki.domain.source_records import build_source_record_plan
from llmwiki.domain.source_structure_integrity import build_source_structure_integrity_report
from llmwiki.domain.typed_evidence_producer import DeterministicTypedEvidenceProducer
from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.source_map_builder import build_normalized_source_map


def test_candidate_admission_rejects_procedure_without_evidence_closure() -> None:
    source_map = _source_map(
        (
            _element("h1", "heading", "Procedure", "Procedure", 1),
            _element("p1", "list_item", "Procedure", "1. Choose a value.\n2. Record it.", 1),
        )
    )
    record_set = _record_set(source_map)
    candidate = _candidate(
        "proc",
        PAGE_FAMILY_PROCEDURE_GUIDE,
        tuple(record.typed_evidence_record_id for record in record_set.accepted_records),
    )

    result = admit_compiler_page_candidates(
        source_id=source_map.source_id,
        source_hash=source_map.source_hash,
        candidates=(candidate,),
        record_set=record_set,
        structure_report=build_source_structure_integrity_report(source_map),
        record_plan=build_source_record_plan(source_map),
    )

    assert result.accepted_candidates == ()
    assert result.report.findings[0].finding_code == "procedure-shape-too-few-steps"


def test_candidate_admission_accepts_recipe_with_code_and_context() -> None:
    source_map = _source_map(
        (
            _element("h1", "heading", "Partial Application", "Partial Application", 1),
            _element("c1", "code_block", "Partial Application", "const add = a => b => a + b;", 1),
            _element(
                "p1",
                "paragraph",
                "Partial Application",
                "JavaScript can use functions to delay arguments.",
                1,
            ),
        ),
        locator="javascriptallonge.pdf",
    )
    record_set = _record_set(source_map)
    candidate = _candidate(
        "recipe",
        PAGE_FAMILY_RECIPE_PATTERN,
        tuple(record.typed_evidence_record_id for record in record_set.accepted_records),
    )

    result = admit_compiler_page_candidates(
        source_id=source_map.source_id,
        source_hash=source_map.source_hash,
        candidates=(candidate,),
        record_set=record_set,
        structure_report=build_source_structure_integrity_report(source_map),
        record_plan=build_source_record_plan(source_map),
    )

    assert result.accepted_candidates == (candidate,)
    assert not result.report.findings


def _record_set(source_map):
    artifact = select_source_profile(source_map)
    plan = build_evidence_extraction_plan(
        source_map,
        artifact.source_profile,
        artifact.evidence_vocabulary,
    )
    return DeterministicTypedEvidenceProducer().build_record_set(source_map, artifact, plan)


def _candidate(page_id: str, family: str, support: tuple[str, ...]) -> PageCandidate:
    return PageCandidate(
        page_candidate_id=f"candidate-{page_id}",
        source_id="source",
        source_hash="cd" * 32,
        source_profile_kind="rpg-rules",
        page_id=page_id,
        title="Procedure",
        page_kind="procedure" if family == PAGE_FAMILY_PROCEDURE_GUIDE else "recipe",
        page_family=family,
        origin="test",
        rank_score=1.0,
        source_order=1,
        supporting_evidence_record_ids=support,
    )


def _source_map(elements: tuple[DocumentElement, ...], locator: str = "rules.pdf"):
    return build_normalized_source_map(
        DocumentModel(
            source_locator=locator,
            source_hash="cd" * 32,
            extractor_name="docling",
            extractor_version="test",
            elements=elements,
        )
    )


def _element(
    element_id: str,
    element_kind: str,
    heading_path: str,
    text: str,
    page: int,
) -> DocumentElement:
    return DocumentElement(
        element_id=element_id,
        element_kind=element_kind,
        body_state="body",
        heading_path=heading_path,
        page_start=page,
        page_end=page,
        text=text,
        markdown=f"# {text}" if element_kind == "heading" else text,
    )
