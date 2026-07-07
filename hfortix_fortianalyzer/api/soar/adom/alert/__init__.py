"""FortiAnalyzer alert adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import indicator

__all__ = ["Alert"]


class Alert:
    """FortiAnalyzer alert adom API endpoints."""

    indicator: "indicator.SoarAdomAlertIndicator"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Alert namespace with JSON-RPC client."""
        from . import indicator as indicator_module

        self.indicator = indicator_module.SoarAdomAlertIndicator(client)
