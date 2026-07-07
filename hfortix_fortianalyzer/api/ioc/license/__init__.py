"""FortiAnalyzer license API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import state

__all__ = ["License"]


class License:
    """FortiAnalyzer license API endpoints."""

    state: "state.IocLicenseState"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize License namespace with JSON-RPC client."""
        from . import state as state_module

        self.state = state_module.IocLicenseState(client)
