"""FortiAnalyzer ha API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import status

__all__ = ["HA"]


class HA:
    """FortiAnalyzer ha API endpoints."""

    status: "status.SysHaStatus"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize HA namespace with JSON-RPC client."""
        from . import status as status_module

        self.status = status_module.SysHaStatus(client)
