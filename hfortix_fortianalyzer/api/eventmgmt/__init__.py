"""FortiAnalyzer eventmgmt API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import adom

__all__ = ["Eventmgmt"]


class Eventmgmt:
    """FortiAnalyzer eventmgmt API endpoints."""

    adom: "adom.Adom"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Eventmgmt namespace with JSON-RPC client."""
        from . import adom as adom_module

        self.adom = adom_module.Adom(client)
