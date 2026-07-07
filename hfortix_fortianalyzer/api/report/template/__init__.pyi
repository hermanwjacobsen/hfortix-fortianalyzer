"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .delete import ReportTemplateDelete
    from .import_ import ReportTemplateImport

__all__ = ["Template"]


class Template:
    """Template endpoints."""

    delete: ReportTemplateDelete
    import_: ReportTemplateImport

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
