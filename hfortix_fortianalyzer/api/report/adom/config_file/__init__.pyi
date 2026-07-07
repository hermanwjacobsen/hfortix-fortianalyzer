"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .export import ReportAdomConfigFileExport

__all__ = ["Configfile"]


class Configfile:
    """Configfile endpoints."""

    export: ReportAdomConfigFileExport

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
