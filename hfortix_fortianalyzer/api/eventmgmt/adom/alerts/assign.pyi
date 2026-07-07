"""Type stubs for eventmgmt.adom.alerts.assign"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomAlertsAssign:
    """FortiAnalyzer endpoint: eventmgmt.adom.alerts.assign"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def update(
        self,
        adom: str,
        alertid: list[str],
        assign_to: str,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["EventmgmtAdomAlertsAssign"]