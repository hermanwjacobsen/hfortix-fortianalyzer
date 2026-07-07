"""Type stubs for eventmgmt.adom.alerts.comment"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomAlertsComment:
    """FortiAnalyzer endpoint: eventmgmt.adom.alerts.comment"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def update(
        self,
        adom: str,
        alertid: list[str],
        update_by: str,
        apiver: int = 3,
        comment: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["EventmgmtAdomAlertsComment"]