"""Type stubs for eventmgmt.adom.alertlogs"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomAlertlogs:
    """FortiAnalyzer endpoint: eventmgmt.adom.alertlogs"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        alertid: list[str],
        apiver: int = 3,
        limit: float | None = None,
        offset: float | None = None,
        rulename: str | None = None,
        time_order: Literal["desc", "asc"] | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["EventmgmtAdomAlertlogs"]