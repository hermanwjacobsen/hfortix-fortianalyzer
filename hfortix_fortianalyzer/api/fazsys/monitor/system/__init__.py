"""FortiAnalyzer system monitor API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import performance

__all__ = ["System"]


class System:
    """FortiAnalyzer system monitor API endpoints."""

    performance: "performance.Performance"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize System namespace with JSON-RPC client."""
        from . import performance as performance_module

        self.performance = performance_module.Performance(client)
