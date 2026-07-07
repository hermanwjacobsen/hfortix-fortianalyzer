"""FortiAnalyzer admin system API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import user

__all__ = ["Admin"]


class Admin:
    """FortiAnalyzer admin system API endpoints."""

    user: "user.CliGlobalMetaFieldsSystemAdminUser"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Admin namespace with JSON-RPC client."""
        from . import user as user_module

        self.user = user_module.CliGlobalMetaFieldsSystemAdminUser(client)
