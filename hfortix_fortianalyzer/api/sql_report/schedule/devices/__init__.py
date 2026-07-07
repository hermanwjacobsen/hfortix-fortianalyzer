"""FortiAnalyzer devices schedule API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import interfaces

__all__ = ["Devices"]


class Devices:
    """FortiAnalyzer devices schedule API endpoints."""

    interfaces: "interfaces.SqlReportScheduleDevicesInterfaces"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Devices namespace with JSON-RPC client."""
        from . import interfaces as interfaces_module

        self.interfaces = interfaces_module.SqlReportScheduleDevicesInterfaces(client)
