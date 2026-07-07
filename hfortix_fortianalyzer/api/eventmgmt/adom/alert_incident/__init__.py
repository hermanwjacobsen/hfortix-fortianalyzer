"""FortiAnalyzer alert_incident adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import stats

__all__ = ["Alertincident"]


class Alertincident:
    """FortiAnalyzer alert_incident adom API endpoints."""

    stats: "stats.EventmgmtAdomAlertIncidentStats"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Alertincident namespace with JSON-RPC client."""
        from . import stats as stats_module

        self.stats = stats_module.EventmgmtAdomAlertIncidentStats(client)
