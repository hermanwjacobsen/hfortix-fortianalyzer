"""FortiAnalyzer _meta_fields global_ API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import system

__all__ = ["Metafields"]


class Metafields:
    """FortiAnalyzer _meta_fields global_ API endpoints."""

    system: "system.System"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Metafields namespace with JSON-RPC client."""
        from . import system as system_module

        self.system = system_module.System(client)
