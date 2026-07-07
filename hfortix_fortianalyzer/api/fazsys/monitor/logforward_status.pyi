"""Type stubs for fazsys.monitor.logforward-status"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class FazsysMonitorLogforwardStatus:
    """FortiAnalyzer endpoint: fazsys.monitor.logforward-status"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        apiver: int = 3,
        id: list[float] | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["FazsysMonitorLogforwardStatus"]