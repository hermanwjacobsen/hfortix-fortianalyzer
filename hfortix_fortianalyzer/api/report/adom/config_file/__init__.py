"""FortiAnalyzer config_file adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import export

__all__ = ["Configfile"]


class Configfile:
    """FortiAnalyzer config_file adom API endpoints."""

    export: "export.ReportAdomConfigFileExport"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Configfile namespace with JSON-RPC client."""
        from . import export as export_module

        self.export = export_module.ReportAdomConfigFileExport(client)
