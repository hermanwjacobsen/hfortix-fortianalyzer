"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .upgrade import UmImageUpgrade

__all__ = ["Image"]


class Image:
    """Image endpoints."""

    upgrade: UmImageUpgrade

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
