"""FortiAnalyzer performance system API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import status

__all__ = ["Performance"]


class Performance:
    """FortiAnalyzer performance system API endpoints."""

    status: "status.FazsysMonitorSystemPerformanceStatus"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Performance namespace with JSON-RPC client."""
        from . import status as status_module

        self.status = status_module.FazsysMonitorSystemPerformanceStatus(client)
