"""FortiAnalyzer incident adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import indicator

__all__ = ["Incident"]


class Incident:
    """FortiAnalyzer incident adom API endpoints."""

    indicator: "indicator.SoarAdomIncidentIndicator"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Incident namespace with JSON-RPC client."""
        from . import indicator as indicator_module

        self.indicator = indicator_module.SoarAdomIncidentIndicator(client)
