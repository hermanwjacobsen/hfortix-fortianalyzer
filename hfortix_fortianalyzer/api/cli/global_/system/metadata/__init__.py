"""FortiAnalyzer metadata system API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import admins

__all__ = ["Metadata"]


class Metadata:
    """FortiAnalyzer metadata system API endpoints."""

    admins: "admins.CliGlobalSystemMetadataAdmins"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Metadata namespace with JSON-RPC client."""
        from . import admins as admins_module

        self.admins = admins_module.CliGlobalSystemMetadataAdmins(client)
