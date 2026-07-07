"""FortiAnalyzer monitor API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import logforward_status
    from . import system

__all__ = ["Monitor"]


class Monitor:
    """FortiAnalyzer monitor API endpoints."""

    logforward_status: "logforward_status.FazsysMonitorLogforwardStatus"
    system: "system.System"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Monitor namespace with JSON-RPC client."""
        from . import logforward_status as logforward_status_module
        from . import system as system_module

        self.logforward_status = logforward_status_module.FazsysMonitorLogforwardStatus(client)
        self.system = system_module.System(client)
