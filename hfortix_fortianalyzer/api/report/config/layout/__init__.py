"""FortiAnalyzer layout config API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import folders

__all__ = ["Layout"]


class Layout:
    """FortiAnalyzer layout config API endpoints."""

    folders: "folders.ReportConfigLayoutFolders"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Layout namespace with JSON-RPC client."""
        from . import folders as folders_module

        self.folders = folders_module.ReportConfigLayoutFolders(client)
