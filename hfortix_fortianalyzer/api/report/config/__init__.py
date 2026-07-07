"""FortiAnalyzer config API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import layout

__all__ = ["Config"]


class Config:
    """FortiAnalyzer config API endpoints."""

    layout: "layout.Layout"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Config namespace with JSON-RPC client."""
        from . import layout as layout_module

        self.layout = layout_module.Layout(client)
