"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .image import Image

__all__ = ["UM"]


class UM:
    """UM endpoints."""

    image: Image

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
