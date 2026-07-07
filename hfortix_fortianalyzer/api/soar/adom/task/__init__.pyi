"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .monitor import SoarAdomTaskMonitor

__all__ = ["Task"]


class Task:
    """Task endpoints."""

    monitor: SoarAdomTaskMonitor

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
