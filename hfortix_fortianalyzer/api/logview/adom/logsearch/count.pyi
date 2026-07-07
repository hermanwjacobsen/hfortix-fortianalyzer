"""Type stubs for logview.adom.logsearch.count"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class LogviewAdomLogsearchCount:
    """FortiAnalyzer endpoint: logview.adom.logsearch.count"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        tid: str,
        adom: str,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["LogviewAdomLogsearchCount"]