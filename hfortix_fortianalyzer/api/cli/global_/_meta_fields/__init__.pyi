"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .system import System

__all__ = ["Metafields"]


class Metafields:
    """Metafields endpoints."""

    system: System

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
