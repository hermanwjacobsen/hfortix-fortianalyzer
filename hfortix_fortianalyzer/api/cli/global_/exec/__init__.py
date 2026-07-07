"""FortiAnalyzer exec global_ API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import fgfm

__all__ = ["Exec"]


class Exec:
    """FortiAnalyzer exec global_ API endpoints."""

    fgfm: "fgfm.Fgfm"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Exec namespace with JSON-RPC client."""
        from . import fgfm as fgfm_module

        self.fgfm = fgfm_module.Fgfm(client)
