"""Type stubs for incidentmgmt.adom.incident.stats"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IncidentmgmtAdomIncidentStats:
    """FortiAnalyzer endpoint: incidentmgmt.adom.incident.stats"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        stats_item: list[Literal["total", "severity", "category", "status", "outbreak"]],
        apiver: int = 3,
        filter: str | None = None,
        time_range: dict[str, Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["IncidentmgmtAdomIncidentStats"]