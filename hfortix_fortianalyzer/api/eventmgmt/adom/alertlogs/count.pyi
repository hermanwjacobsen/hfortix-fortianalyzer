"""Type stubs for eventmgmt.adom.alertlogs.count"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomAlertlogsCount:
    """FortiAnalyzer endpoint: eventmgmt.adom.alertlogs.count"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        alertid: list[str],
        apiver: int = 3,
        rulename: str | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["EventmgmtAdomAlertlogsCount"]