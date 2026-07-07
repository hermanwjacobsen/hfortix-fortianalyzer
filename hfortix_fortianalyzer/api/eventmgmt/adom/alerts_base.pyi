"""Type stubs for eventmgmt.adom.alerts"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomAlerts:
    """FortiAnalyzer endpoint: eventmgmt.adom.alerts"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        apiver: int = 3,
        filter: str | None = None,
        limit: float | None = None,
        offset: float | None = None,
        time_range: dict[str, Any] | None = None,
        timezone: str | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["EventmgmtAdomAlerts"]