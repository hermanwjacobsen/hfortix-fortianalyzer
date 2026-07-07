"""FortiAnalyzer template API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import delete
    from . import import_

__all__ = ["Template"]


class Template:
    """FortiAnalyzer template API endpoints."""

    delete: "delete.ReportTemplateDelete"
    import_: "import_.ReportTemplateImport"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Template namespace with JSON-RPC client."""
        from . import delete as delete_module
        from . import import_ as import__module

        self.delete = delete_module.ReportTemplateDelete(client)
        self.import_ = import__module.ReportTemplateImport(client)
