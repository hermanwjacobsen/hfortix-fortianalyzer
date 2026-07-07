"""Type stubs for incidentmgmt.adom.incidents.count"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IncidentmgmtAdomIncidentsCount:
    """FortiAnalyzer endpoint: incidentmgmt.adom.incidents.count"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        apiver: int = 3,
        filter: str | None = None,
        incids: list[str] | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["IncidentmgmtAdomIncidentsCount"]