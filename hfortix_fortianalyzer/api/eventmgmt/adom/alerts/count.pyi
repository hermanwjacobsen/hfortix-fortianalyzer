"""Type stubs for eventmgmt.adom.alerts.count"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomAlertsCount:
    """FortiAnalyzer endpoint: eventmgmt.adom.alerts.count"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        apiver: int = 3,
        filter: str | None = None,
        group_by: Literal["severity", "trigger", "severity_timescale", "eventtype", "mgmt_state", "severity_epdevtype"] | None = None,
        time_range: dict[str, Any] | None = None,
        timescale: Literal["month", "hour"] | None = None,
        timezone: str | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["EventmgmtAdomAlertsCount"]