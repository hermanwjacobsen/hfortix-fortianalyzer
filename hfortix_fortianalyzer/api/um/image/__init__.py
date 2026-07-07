"""FortiAnalyzer image API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import upgrade

__all__ = ["Image"]


class Image:
    """FortiAnalyzer image API endpoints."""

    upgrade: "upgrade.UmImageUpgrade"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Image namespace with JSON-RPC client."""
        from . import upgrade as upgrade_module

        self.upgrade = upgrade_module.UmImageUpgrade(client)
