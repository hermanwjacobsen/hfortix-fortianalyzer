"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .status import FazsysMonitorSystemPerformanceStatus

__all__ = ["Performance"]


class Performance:
    """Performance endpoints."""

    status: FazsysMonitorSystemPerformanceStatus

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
