"""FortiAnalyzer config adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import connectors
    from . import playbooks

__all__ = ["Config"]


class Config:
    """FortiAnalyzer config adom API endpoints."""

    connectors: "connectors.SoarAdomConfigConnectors"
    playbooks: "playbooks.SoarAdomConfigPlaybooks"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Config namespace with JSON-RPC client."""
        from . import connectors as connectors_module
        from . import playbooks as playbooks_module

        self.connectors = connectors_module.SoarAdomConfigConnectors(client)
        self.playbooks = playbooks_module.SoarAdomConfigPlaybooks(client)
