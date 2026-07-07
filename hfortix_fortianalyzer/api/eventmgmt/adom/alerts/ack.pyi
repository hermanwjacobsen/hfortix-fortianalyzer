"""Type stubs for eventmgmt.adom.alerts.ack"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomAlertsAck:
    """FortiAnalyzer endpoint: eventmgmt.adom.alerts.ack"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def update(
        self,
        adom: str,
        alertid: list[str],
        update_by: str,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["EventmgmtAdomAlertsAck"]