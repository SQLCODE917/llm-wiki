"""Persistable ingest route plan observations."""

from __future__ import annotations

import json
from dataclasses import dataclass

from llmwiki.domain.ingest_route_plan import IngestRoutePlan, IngestRoutePlanScope

INGEST_ROUTE_PLAN_RECORD_VERSION = "ingest-route-plan-record.v1"


@dataclass(frozen=True)
class IngestRoutePlanRecord:
    date: str
    run_id: str
    source_path: str
    scope: IngestRoutePlanScope
    chunk_id: int | None
    profile_ids: tuple[str, ...]
    planned_page_count: int
    route_gap_count: int
    route_gap_summaries: tuple[str, ...]
    planned_page_ids: tuple[str, ...]
    page_writes: tuple[str, ...]
    version: str = INGEST_ROUTE_PLAN_RECORD_VERSION

    @classmethod
    def from_plan(
        cls,
        plan: IngestRoutePlan,
        *,
        date: str,
        run_id: str,
        page_writes: tuple[str, ...] = (),
    ) -> IngestRoutePlanRecord:
        summary = plan.summary()
        return cls(
            date=date,
            run_id=run_id,
            source_path=plan.source_path,
            scope=plan.scope,
            chunk_id=plan.chunk_id,
            profile_ids=plan.profile_ids,
            planned_page_count=summary.planned_page_count,
            route_gap_count=summary.route_gap_count,
            route_gap_summaries=summary.route_gap_summaries,
            planned_page_ids=tuple(page.metadata.page_id for page in plan.planned_pages),
            page_writes=page_writes,
        )

    def to_json_line(self) -> str:
        return json.dumps(
            {
                "version": self.version,
                "date": self.date,
                "run_id": self.run_id,
                "source_path": self.source_path,
                "scope": self.scope,
                "chunk_id": self.chunk_id,
                "profile_ids": list(self.profile_ids),
                "planned_page_count": self.planned_page_count,
                "route_gap_count": self.route_gap_count,
                "route_gap_summaries": list(self.route_gap_summaries),
                "planned_page_ids": list(self.planned_page_ids),
                "page_writes": list(self.page_writes),
            },
            ensure_ascii=False,
            sort_keys=True,
        )


def ingest_route_plan_record_from_json_line(line: str) -> IngestRoutePlanRecord:
    data = json.loads(line)
    return IngestRoutePlanRecord(
        version=data.get("version", INGEST_ROUTE_PLAN_RECORD_VERSION),
        date=data["date"],
        run_id=data.get("run_id", ""),
        source_path=data["source_path"],
        scope=data["scope"],
        chunk_id=data.get("chunk_id"),
        profile_ids=tuple(data.get("profile_ids", [])),
        planned_page_count=data.get("planned_page_count", 0),
        route_gap_count=data.get("route_gap_count", 0),
        route_gap_summaries=tuple(data.get("route_gap_summaries", [])),
        planned_page_ids=tuple(data.get("planned_page_ids", [])),
        page_writes=tuple(data.get("page_writes", [])),
    )


def ingest_route_plan_records_from_jsonl(text: str) -> tuple[IngestRoutePlanRecord, ...]:
    return tuple(
        ingest_route_plan_record_from_json_line(line) for line in text.splitlines() if line.strip()
    )
