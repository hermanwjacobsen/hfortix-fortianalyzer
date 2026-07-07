"""FortiAnalyzer system _meta_fields API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import admin

__all__ = ["System"]


class System:
    """FortiAnalyzer system _meta_fields API endpoints."""

    admin: "admin.Admin"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize System namespace with JSON-RPC client."""
        from . import admin as admin_module

        self.admin = admin_module.Admin(client)
