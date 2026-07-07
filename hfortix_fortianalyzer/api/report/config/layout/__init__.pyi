"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .folders import ReportConfigLayoutFolders

__all__ = ["Layout"]


class Layout:
    """Layout endpoints."""

    folders: ReportConfigLayoutFolders

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
