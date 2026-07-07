"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .data import ReportAdomReportsData
    from .state import ReportAdomReportsState

__all__ = ["Reports"]


class Reports:
    """Reports endpoints."""

    data: ReportAdomReportsData
    state: ReportAdomReportsState

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
