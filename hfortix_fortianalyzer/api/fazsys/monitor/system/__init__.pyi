"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .performance import Performance

__all__ = ["System"]


class System:
    """System endpoints."""

    performance: Performance

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
