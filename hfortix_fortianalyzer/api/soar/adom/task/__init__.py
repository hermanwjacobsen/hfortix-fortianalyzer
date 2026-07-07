"""FortiAnalyzer task adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import monitor

__all__ = ["Task"]


class Task:
    """FortiAnalyzer task adom API endpoints."""

    monitor: "monitor.SoarAdomTaskMonitor"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Task namespace with JSON-RPC client."""
        from . import monitor as monitor_module

        self.monitor = monitor_module.SoarAdomTaskMonitor(client)
