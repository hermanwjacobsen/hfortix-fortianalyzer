"""Type stubs for fazsys.monitor.system.performance.status"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class FazsysMonitorSystemPerformanceStatus:
    """FortiAnalyzer endpoint: fazsys.monitor.system.performance.status"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["FazsysMonitorSystemPerformanceStatus"]