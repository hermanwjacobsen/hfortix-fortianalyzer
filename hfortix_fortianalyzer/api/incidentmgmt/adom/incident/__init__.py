"""FortiAnalyzer incident adom API endpoints."""

from __future__ import annotations

from ..incident_base import IncidentmgmtAdomIncident as IncidentmgmtAdomIncidentBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import stats

__all__ = ["IncidentmgmtAdomIncident"]


class IncidentmgmtAdomIncident(IncidentmgmtAdomIncidentBase):
    """FortiAnalyzer incident adom API endpoints."""

    stats: "stats.IncidentmgmtAdomIncidentStats"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize IncidentmgmtAdomIncident with endpoint methods and child modules."""
        super().__init__(client)

        from . import stats as stats_module

        self.stats = stats_module.IncidentmgmtAdomIncidentStats(client)
