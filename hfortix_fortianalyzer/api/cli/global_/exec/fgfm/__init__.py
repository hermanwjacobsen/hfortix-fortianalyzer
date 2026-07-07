"""FortiAnalyzer fgfm exec API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import reclaim_dev_tunnel

__all__ = ["Fgfm"]


class Fgfm:
    """FortiAnalyzer fgfm exec API endpoints."""

    reclaim_dev_tunnel: "reclaim_dev_tunnel.CliGlobalExecFgfmReclaimDevTunnel"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Fgfm namespace with JSON-RPC client."""
        from . import reclaim_dev_tunnel as reclaim_dev_tunnel_module

        self.reclaim_dev_tunnel = reclaim_dev_tunnel_module.CliGlobalExecFgfmReclaimDevTunnel(client)
