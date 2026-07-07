"""Type stubs for incidentmgmt.adom.incidents"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IncidentmgmtAdomIncidents:
    """FortiAnalyzer endpoint: incidentmgmt.adom.incidents"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def delete(
        self,
        adom: str,
        apiver: int = 3,
        incids: list[str] | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...

    def get(
        self,
        adom: str,
        apiver: int = 3,
        detail_level: str | None = None,
        filter: str | None = None,
        incids: list[str] | None = None,
        limit: float | None = None,
        offset: float | None = None,
        sort_by: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["IncidentmgmtAdomIncidents"]