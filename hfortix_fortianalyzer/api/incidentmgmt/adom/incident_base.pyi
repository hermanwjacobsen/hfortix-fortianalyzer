"""Type stubs for incidentmgmt.adom.incident"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IncidentmgmtAdomIncident:
    """FortiAnalyzer endpoint: incidentmgmt.adom.incident"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        category: str,
        endpoint: str,
        reporter: str,
        incid: int | str | None = None,
        apiver: int = 3,
        description: str | None = None,
        epid: float | None = None,
        euid: float | None = None,
        severity: Literal["high", "medium", "low"] | None = None,
        status: Literal["draft", "analysis", "response", "closed", "cancelled"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def update(
        self,
        adom: str,
        incid: int | str | None = None,
        apiver: int = 3,
        category: str | None = None,
        description: str | None = None,
        endpoint: str | None = None,
        epid: float | None = None,
        euid: float | None = None,
        lastrevision: float | None = None,
        lastuser: str | None = None,
        severity: Literal["high", "medium", "low"] | None = None,
        status: Literal["draft", "analysis", "response", "closed", "cancelled"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["IncidentmgmtAdomIncident"]