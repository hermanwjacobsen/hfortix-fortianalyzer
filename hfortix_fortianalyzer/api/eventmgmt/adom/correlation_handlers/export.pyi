"""Type stubs for eventmgmt.adom.correlation-handlers.export"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomCorrelationHandlersExport:
    """FortiAnalyzer endpoint: eventmgmt.adom.correlation-handlers.export"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        apiver: int = 3,
        attachment: list[str] | None = None,
        data_format: Literal["zip", "txt", "cli"] | None = None,
        filter: list[str] | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["EventmgmtAdomCorrelationHandlersExport"]