"""FortiAnalyzer fortiview API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import adom

__all__ = ["Fortiview"]


class Fortiview:
    """FortiAnalyzer fortiview API endpoints."""

    adom: "adom.Adom"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Fortiview namespace with JSON-RPC client."""
        from . import adom as adom_module

        self.adom = adom_module.Adom(client)
