"""Type stubs for eventmgmt.adom.config.correlation-handler"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomConfigCorrelationHandler:
    """FortiAnalyzer endpoint: eventmgmt.adom.config.correlation-handler"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        apiver: int = 3,
        data: dict[str, Any] | None = None,
        filter: list[str] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...


__all__ = ["EventmgmtAdomConfigCorrelationHandler"]