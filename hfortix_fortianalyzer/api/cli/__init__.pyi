"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .global_ import Global

__all__ = ["Cli"]


class Cli:
    """Cli endpoints."""

    global_: Global

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
