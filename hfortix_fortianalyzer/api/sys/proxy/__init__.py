"""FortiAnalyzer proxy API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import json

__all__ = ["Proxy"]


class Proxy:
    """FortiAnalyzer proxy API endpoints."""

    json: "json.SysProxyJson"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Proxy namespace with JSON-RPC client."""
        from . import json as json_module

        self.json = json_module.SysProxyJson(client)
