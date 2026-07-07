"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .data import LogviewAdomLogfilesData
    from .search import LogviewAdomLogfilesSearch
    from .state import LogviewAdomLogfilesState

__all__ = ["Logfiles"]


class Logfiles:
    """Logfiles endpoints."""

    data: LogviewAdomLogfilesData
    search: LogviewAdomLogfilesSearch
    state: LogviewAdomLogfilesState

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
