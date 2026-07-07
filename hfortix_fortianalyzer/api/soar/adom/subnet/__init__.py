"""FortiAnalyzer subnet adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import export
    from . import import_

__all__ = ["Subnet"]


class Subnet:
    """FortiAnalyzer subnet adom API endpoints."""

    export: "export.SoarAdomSubnetExport"
    import_: "import_.SoarAdomSubnetImport"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Subnet namespace with JSON-RPC client."""
        from . import export as export_module
        from . import import_ as import__module

        self.export = export_module.SoarAdomSubnetExport(client)
        self.import_ = import__module.SoarAdomSubnetImport(client)
