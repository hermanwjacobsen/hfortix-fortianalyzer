"""FortiAnalyzer reports adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import data
    from . import state

__all__ = ["Reports"]


class Reports:
    """FortiAnalyzer reports adom API endpoints."""

    data: "data.ReportAdomReportsData"
    state: "state.ReportAdomReportsState"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Reports namespace with JSON-RPC client."""
        from . import data as data_module
        from . import state as state_module

        self.data = data_module.ReportAdomReportsData(client)
        self.state = state_module.ReportAdomReportsState(client)
