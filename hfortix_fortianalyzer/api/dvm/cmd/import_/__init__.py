"""FortiAnalyzer import_ cmd API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import dev_list

__all__ = ["Import"]


class Import:
    """FortiAnalyzer import_ cmd API endpoints."""

    dev_list: "dev_list.DvmCmdImportDevList"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Import namespace with JSON-RPC client."""
        from . import dev_list as dev_list_module

        self.dev_list = dev_list_module.DvmCmdImportDevList(client)
