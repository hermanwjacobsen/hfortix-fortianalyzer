"""Type stubs for incidentmgmt.adom.epeu-history"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IncidentmgmtAdomEpeuHistory:
    """FortiAnalyzer endpoint: incidentmgmt.adom.epeu-history"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        incid: str,
        apiver: int = 3,
        attachid: str | None = None,
        dvid: float | None = None,
        endpoint: str | None = None,
        epid: float | None = None,
        epip: str | None = None,
        euid: float | None = None,
        euname: str | None = None,
        eventid: str | None = None,
        fctuid: str | None = None,
        mac: str | None = None,
        notes: str | None = None,
        osname: str | None = None,
        osversion: str | None = None,
        srcinfo: str | None = None,
        srctype: Literal["manual-input", "auto-event-attachement", "manual-event-attachment", "auto-incident", "manual-incident"] | None = None,
        tags: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def delete(
        self,
        adom: str,
        incid: str,
        apiver: int = 3,
        seqid: str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...

    def get(
        self,
        adom: str,
        incid: str,
        apiver: int = 3,
        limit: float | None = None,
        offset: float | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...

    def update(
        self,
        adom: str,
        seqid: str,
        apiver: int = 3,
        attachid: str | None = None,
        dvid: float | None = None,
        endpoint: str | None = None,
        epid: float | None = None,
        epip: str | None = None,
        euid: float | None = None,
        euname: str | None = None,
        eventid: str | None = None,
        fctuid: str | None = None,
        mac: str | None = None,
        notes: str | None = None,
        osname: str | None = None,
        osversion: str | None = None,
        srcinfo: str | None = None,
        srctype: Literal["manual-input", "auto-event-attachement", "manual-event-epeu-history", "auto-incident", "manual-incident"] | None = None,
        tags: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["IncidentmgmtAdomEpeuHistory"]