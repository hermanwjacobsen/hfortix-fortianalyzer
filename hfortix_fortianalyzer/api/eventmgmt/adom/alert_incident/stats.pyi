"""Type stubs for eventmgmt.adom.alert-incident.stats"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomAlertIncidentStats:
    """FortiAnalyzer endpoint: eventmgmt.adom.alert-incident.stats"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        apiver: int = 3,
        time_range: dict[str, Any] | None = None,
        timescale: Literal["month", "hour"] | None = None,
        timezone: str | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["EventmgmtAdomAlertIncidentStats"]