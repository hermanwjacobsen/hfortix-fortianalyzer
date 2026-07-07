"""FortiAnalyzer correlation_handlers adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import export
    from . import import_

__all__ = ["Correlationhandlers"]


class Correlationhandlers:
    """FortiAnalyzer correlation_handlers adom API endpoints."""

    export: "export.EventmgmtAdomCorrelationHandlersExport"
    import_: "import_.EventmgmtAdomCorrelationHandlersImport"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Correlationhandlers namespace with JSON-RPC client."""
        from . import export as export_module
        from . import import_ as import__module

        self.export = export_module.EventmgmtAdomCorrelationHandlersExport(client)
        self.import_ = import__module.EventmgmtAdomCorrelationHandlersImport(client)
