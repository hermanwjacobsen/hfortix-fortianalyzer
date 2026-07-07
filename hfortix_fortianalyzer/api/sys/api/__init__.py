"""FortiAnalyzer api API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import sdnconnector

__all__ = ["API"]


class API:
    """FortiAnalyzer api API endpoints."""

    sdnconnector: "sdnconnector.SysApiSdnconnector"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize API namespace with JSON-RPC client."""
        from . import sdnconnector as sdnconnector_module

        self.sdnconnector = sdnconnector_module.SysApiSdnconnector(client)
