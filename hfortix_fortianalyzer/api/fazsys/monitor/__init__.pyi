"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .logforward_status import FazsysMonitorLogforwardStatus
    from .system import System

__all__ = ["Monitor"]


class Monitor:
    """Monitor endpoints."""

    logforward_status: FazsysMonitorLogforwardStatus
    system: System

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
