"""Type stubs for eventmgmt.adom.basic-handlers.export"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomBasicHandlersExport:
    """FortiAnalyzer endpoint: eventmgmt.adom.basic-handlers.export"""

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


__all__ = ["EventmgmtAdomBasicHandlersExport"]