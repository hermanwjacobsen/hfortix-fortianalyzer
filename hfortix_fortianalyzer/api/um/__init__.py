"""FortiAnalyzer um API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import image

__all__ = ["UM"]


class UM:
    """FortiAnalyzer um API endpoints."""

    image: "image.Image"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize UM namespace with JSON-RPC client."""
        from . import image as image_module

        self.image = image_module.Image(client)
