"""FortiAnalyzer logfiles adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import data
    from . import search
    from . import state

__all__ = ["Logfiles"]


class Logfiles:
    """FortiAnalyzer logfiles adom API endpoints."""

    data: "data.LogviewAdomLogfilesData"
    search: "search.LogviewAdomLogfilesSearch"
    state: "state.LogviewAdomLogfilesState"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Logfiles namespace with JSON-RPC client."""
        from . import data as data_module
        from . import search as search_module
        from . import state as state_module

        self.data = data_module.LogviewAdomLogfilesData(client)
        self.search = search_module.LogviewAdomLogfilesSearch(client)
        self.state = state_module.LogviewAdomLogfilesState(client)
