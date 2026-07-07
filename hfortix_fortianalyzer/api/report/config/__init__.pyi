"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .layout import Layout

__all__ = ["Config"]


class Config:
    """Config endpoints."""

    layout: Layout

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
