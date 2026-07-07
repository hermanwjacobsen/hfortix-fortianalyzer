"""FortiAnalyzer cli API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import global_

__all__ = ["Cli"]


class Cli:
    """FortiAnalyzer cli API endpoints."""

    global_: "global_.Global"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Cli namespace with JSON-RPC client."""
        from . import global_ as global__module

        self.global_ = global__module.Global(client)
